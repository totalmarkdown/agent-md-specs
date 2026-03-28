---
spec_name: CIRCUITBREAKER.md
spec_version: 0.1.0
category: Operations
domain: circuitbreakermd.dev
priority: Very High
volume: "Vol 16 — Resilience & Consent"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
---

# CIRCUITBREAKER.md

**Category:** Operations
**Domain:** circuitbreakermd.dev
**Priority:** Very High
**Version:** 0.1.0

### Purpose
Defines failure containment boundaries for agents and multi-agent
systems. When an agent fails, errors must not cascade through the
fleet. This spec establishes blast radius limits, retry policies,
fallback behaviors, and halt conditions at each organizational
hierarchy level.

Without CIRCUITBREAKER.md, a single failing dependency can propagate
through every agent that shares the same call path. One agent's
timeout becomes ten agents' timeouts. This spec prevents that by
defining where failures stop, what happens at each boundary, and
how the system recovers. Addresses OWASP ASI-08 (Cascading
Hallucinations and Failures in Multi-Agent Systems).

### Scope Boundary

- CIRCUITBREAKER.md defines **when to stop and how to contain failure**
- ICE.md defines **emergency break-glass protocols** (broader scope, human-facing)
- ESCALATION.md defines **who gets notified** when containment activates
- REPAIR.md defines **how to fix things** after containment stabilizes the system
- ENFORCEMENT.md defines **how circuit breaker policies are enforced** at runtime
- HEALTHCHECK.md defines **how to verify recovery** before re-closing the breaker

### When to Create This File
Required for any agent in a multi-agent system or any agent calling
external services. Should be created alongside REPAIR.md and
ESCALATION.md as part of the resilience baseline.

### Spec

```markdown
---
agent_name: string
version: semver
circuit_breaker_enabled: boolean
default_failure_threshold: number     # Consecutive failures to trip
default_cooldown_seconds: number      # Time in OPEN before HALF-OPEN
default_success_threshold: number     # Successes in HALF-OPEN to close
monitoring_endpoint: string           # Where state changes are reported
created: date
updated: date
---

# [Agent Name] — Circuit Breaker Protocol

## Circuit Breaker States

```
  CLOSED ──failure threshold──▶ OPEN ──cooldown──▶ HALF-OPEN
    ▲                                                  │
    └──────────success threshold met───────────────────┘
                                                       │
    OPEN ◀─────────────probe failure───────────────────┘
```

| State | Behavior | Transitions |
|-------|----------|-------------|
| CLOSED | Requests pass through. Failures counted. | → OPEN when failure threshold reached |
| OPEN | Requests rejected immediately. Fallback activates. | → HALF-OPEN after cooldown expires |
| HALF-OPEN | Limited probe requests allowed. | → CLOSED on success · → OPEN on failure |

## Failure Thresholds

Any single condition met is sufficient to trip the breaker.

### Threshold Configuration
```yaml
thresholds:
  consecutive_failures: 3              # N failures in a row
  error_rate_percent: 50               # Error rate within window
  error_rate_window_seconds: 300       # Window for rate calculation
  latency_threshold_ms: 30000          # P95 latency exceeding this
  latency_window_seconds: 60           # Window for latency measurement
  resource_exhaustion: true            # Memory, CPU, disk, or connection pool at capacity
  anomaly_detection: true              # Statistical deviation from baseline behavior
  external_signal: true                # Upstream agent or orchestrator signals failure
```

### Failure Classification

| Error Type | Counted | Rationale |
|------------|---------|-----------|
| HTTP 5xx | Yes | Server-side, likely systemic |
| HTTP 429 | Yes | Rate limit exhaustion |
| Timeout | Yes | Dependency unresponsive |
| HTTP 4xx | No | Client error, not dependency issue |
| Connection refused | Yes | Dependency down |
| Malformed response | Yes | Corrupt data from dependency |
| Slow success | Conditional | Only if above latency threshold |
| Auth failure | Immediate trip | Fatal — escalate per ESCALATION.md Level 3 |

## Blast Radius Boundaries

Each level has an independent containment boundary. Failures
do not propagate upward unless containment is exhausted.

| Level | Containment Rule | Max Impact |
|-------|-----------------|------------|
| Agent | Single breaker trips for one dependency. Other agents independent. | 1 agent, 1 dependency |
| Team | >50% of agents have open breakers for same dependency → team breaker trips (see TEAM.md for team composition and organizational containment). | All agents in team |
| Crew | >50% of teams have team-level breakers open → crew breaker trips (see CREW.md for crew-level containment coordination). | All teams in crew |
| Swarm | Multiple crews report open breakers → global fallback activates. | Entire fleet |

### Isolation Principle
- Each breaker is **per-agent, per-dependency**
- Team/crew/swarm breakers aggregate but never override agent breakers
- No agent can force another agent's breaker open or closed

## Fallback Behaviors

When a circuit opens, the agent degrades gracefully. Try each
fallback in order; use the first one that applies.

| # | Strategy | When to Use |
|---|----------|-------------|
| 1 | Cached / stale result | Recent valid result exists. Tag as stale with timestamp. Max staleness: [N min]. |
| 2 | Graceful degradation | Partial functionality acceptable. Disable dependent feature, continue reduced. |
| 3 | Queue for retry | Request not time-sensitive. Write to dead letter queue. Max depth: [N]. |
| 4 | Route to backup agent | Redundant agent exists per TEAM.md. Forward with context and failure reason. |
| 5 | Safe default | Reasonable default exists. Return predefined value. Document why it is safe. |
| 6 | Escalate to human | No automated fallback is safe. Escalate per ESCALATION.md Level 2/3. Pause workflow. |

### Fallback Configuration
```yaml
fallbacks:
  - dependency: [service/agent name]
    strategy: [cached | degrade | queue | backup | default | escalate]
    cached_max_age_seconds: [number]
    queue_location: [path or URL]
    backup_agent: [agent name or endpoint]
    safe_default_value: [value or reference]
    escalation_level: [1 | 2 | 3]
```

## Retry Policy

### Probe Configuration (HALF-OPEN state)
```yaml
retry_policy:
  max_probe_attempts: 3                # Probes before re-opening
  probe_interval_seconds: 10           # Time between probes
  backoff_strategy: exponential        # linear | exponential | jitter
  backoff_base_seconds: 5              # Base delay for backoff
  backoff_max_seconds: 300             # Cap on backoff delay
  jitter_range_percent: 25             # Random variance to prevent thundering herd
  success_threshold: 2                 # Consecutive successes to close breaker
  probe_timeout_ms: 5000               # Timeout for probe requests (shorter than normal)
```

### Probe Requirements
- Probes MUST be lightweight, idempotent, and shorter-timeout than normal
- One probe at a time per breaker (no concurrent probing)
- If probe succeeds but first real request fails, re-open immediately
- Backoff strategies: linear (`base * N`), exponential (`base * 2^N`),
  or exponential+jitter (adds random variance to prevent thundering herd)

## Cascading Prevention

These mechanisms operate independently of the circuit breaker
state machine to prevent failure propagation.

### Timeout Enforcement
Every outbound call MUST have a timeout.

```yaml
timeouts:
  default_request_ms: 10000            # Default for all outbound calls
  external_api_ms: 15000               # Third-party API calls
  sub_agent_ms: 30000                  # Calls to other agents
  database_ms: 5000                    # Database queries
  health_check_ms: 3000                # Health check probes
```

### Bulkhead Pattern
Isolate resource pools per dependency.

```yaml
bulkheads:
  - name: [dependency group]
    max_concurrent: [number]           # Max simultaneous calls
    max_queue: [number]                # Max waiting in queue
    queue_timeout_ms: [number]         # Max time in queue before rejection
```

### Fan-Out Limits

| Scope | Max Fan-Out | At Limit |
|-------|-------------|----------|
| Single agent | [N] concurrent outbound | Queue additional |
| Per dependency | [N] concurrent to same service | Reject with backpressure |
| Per team | [N] total outbound across team | Coordinator throttles |

### Poison Pill Detection
Inputs that fail [N] times are quarantined: removed from queue,
logged with hash and failure details, reviewed [manually/automated],
auto-expired after [N] hours. Alert per ESCALATION.md Level 1.

## Monitoring and Alerting

### State Change Logging
Every state transition is logged to AUDITTRAIL.md (see AUDITTRAIL.md for the event schema and tamper-resistance guarantees):

```yaml
circuit_breaker_event:
  timestamp: [ISO-8601]
  agent_id: [from ID.md]
  dependency: [service or agent name]
  previous_state: [CLOSED | OPEN | HALF-OPEN]
  new_state: [CLOSED | OPEN | HALF-OPEN]
  trigger: [what caused the transition]
  failure_count: [current count at transition]
  error_rate: [percentage at transition]
  fallback_activated: [strategy name or null]
```

### Alert Routing
Alerts are routed per ESCALATION.md based on severity:

| Event | Severity | Alert Target |
|-------|----------|-------------|
| Single agent breaker opens | Low | Log only (Level 1) |
| Agent breaker open > [N] minutes | Medium | Ops notification (Level 1) |
| Team-level breaker opens | High | Ops team alert (Level 2) |
| Crew-level breaker opens | Critical | Immediate escalation (Level 3) |
| Swarm-level degradation | Critical | Hard stop, all-hands alert (Level 3) |
| Breaker closes after recovery | Info | Log only |

### Dashboard Metrics
Expose the following metrics on the operational dashboard
(see MONITOR.md for dashboard configuration and alerting):
- `circuit_breaker_state` — Current state per agent per dependency
- `circuit_breaker_open_duration` — Time each breaker has been open
- `circuit_breaker_trip_count` — Total trips in time window
- `circuit_breaker_fallback_count` — Activations by strategy
- `circuit_breaker_recovery_time` — Time from OPEN to CLOSED

### Historical Analysis
Retain event history for trend analysis: recurring failures,
time-of-day patterns, mean time to recovery, threshold tuning.

## Recovery Procedures

### Recovery Sequence
When HALF-OPEN probes succeed:

1. **Verify health** — Full health check per HEALTHCHECK.md (see HEALTHCHECK.md for probe definitions)
2. **Re-initialize agent** — If the agent was fully halted, follow the
   startup sequence defined in WAKEUP.md before accepting traffic
3. **Close breaker** — Transition to CLOSED, reset failure counters
4. **Replay queued requests** — Process dead letter queue FIFO,
   rate-limited to avoid overwhelming the recovering dependency
5. **Clear stale caches** — Invalidate entries so fresh data flows
6. **Log recovery** — AUDITTRAIL.md: downtime, impact, strategy used
7. **Notify contacts** — Recovery notification with duration and impact;
   notify via ESCALATION.md to close the open incident

### Post-Recovery Validation
After the breaker closes, monitor closely for re-trips:

```yaml
post_recovery:
  monitoring_window_seconds: 300       # Watch closely for 5 minutes
  re_trip_threshold: 1                 # Re-open on first failure in window
  full_threshold_restore_after: 300    # Restore normal thresholds after window
```

### Recovery Fails
If probes continue failing beyond the maximum retry window:
breaker remains OPEN, cooldown doubles (max [N] minutes),
escalation increases one tier. At maximum escalation, trigger
ICE.md emergency protocol.
```

## Example Use Cases

**Enterprise:** A payment processing company uses CIRCUITBREAKER.md to isolate its fraud-detection agent from a flaky third-party identity verification API, serving cached risk scores when the breaker opens rather than blocking all transactions.

**Multi-Agent Fleet:** A fleet of 200 customer-support agents shares a common knowledge-base service; team-level breakers prevent a knowledge-base outage from cascading into every agent simultaneously, while individual agents fall back to local cached FAQ data.

**Regulated Industry:** A banking platform's loan-underwriting agent uses blast radius boundaries to ensure that a credit bureau API failure only affects new applications, never interrupts in-progress approvals or existing customer account operations.

### Cross-References
- **ICE.md** — Emergency break-glass protocols when circuit breakers and automated recovery are insufficient
- **ESCALATION.md** — Notification routing and severity levels for breaker events
- **REPAIR.md** — Post-containment repair and root cause analysis procedures
- **HEALTHCHECK.md** — Health verification used during HALF-OPEN probing and recovery
- **TEAM.md** — Team-level blast radius boundaries and backup agent assignments
- **CREW.md** — Crew-level containment coordination
- **AUDITTRAIL.md** — Append-only log where all breaker state changes are recorded
- **ENFORCEMENT.md** — Runtime enforcement of circuit breaker policies
- **MONITOR.md** — Dashboard metrics and operational observability

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
