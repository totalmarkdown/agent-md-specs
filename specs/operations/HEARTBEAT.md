---
spec_name: HEARTBEAT.md
spec_version: 0.1.0
category: Operations
domain: heartbeatmd.dev
priority: High
volume: "Vol 8 — Technical"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
spec_type: static
---


# HEARTBEAT.md

**Category:** Operations
**Domain:** heartbeatmd.dev
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose
Defines periodic proactive execution cycles — scheduled autonomous
checks, status reporting, cost controls, and delivery routing.
Unlike HEALTHCHECK.md (passive health probes) and MONITOR.md
(metrics collection), HEARTBEAT.md defines what the agent actively
DOES on a regular schedule when not prompted.

A heartbeat is not just an "I'm alive" signal. It is a scheduled
autonomous work cycle: check systems, run diagnostics, report status,
enforce budgets, and route findings to the right channels. WAKEUP.md
handles session startup. SESSION.md handles per-task scoping.
HEARTBEAT.md handles what happens between tasks — the continuous
autonomous rhythm that keeps an agent proactively useful.

### When to Create This File
Required for any agent that operates continuously or semi-autonomously
and needs to perform periodic checks, report status, or enforce cost
controls without being prompted. Should be created alongside
HEALTHCHECK.md, MONITOR.md, and BUDGET.md as part of the
observability and cost governance baseline.

### Spec

````markdown
---
agent_name: string
version: semver
heartbeat_interval: string           # "5m" | "15m" | "1h" | "daily"
heartbeat_actions: list              # What to check/do each cycle
status_report_format: string         # json | markdown | structured
delivery_channels: list             # Where to send reports
cost_budget_per_cycle: string        # Max spend per heartbeat cycle
failure_behavior: string            # retry | escalate | halt
quiet_hours: string                 # When NOT to run heartbeats
escalation_on_anomaly: string       # Who gets notified on anomaly
max_consecutive_failures: number    # Before circuit breaker triggers
health_check_integration: string    # Link to HEALTHCHECK.md probes
created: date
updated: date
---

# [Agent Name] — Heartbeat Configuration

## Heartbeat Schedule

**Interval:** [heartbeat_interval]
**Active hours:** [schedule or "24/7"]
**Quiet hours:** [quiet_hours — e.g. "Saturday 00:00–Sunday 23:59 UTC"]
**Timezone:** [timezone]

## Heartbeat Actions

Actions performed each cycle, in order:

| # | Action | Description | Timeout | On Failure |
|---|--------|-------------|---------|------------|
| 1 | Health probe | Run HEALTHCHECK.md liveness and readiness checks | [N]s | Log + continue |
| 2 | Dependency scan | Verify all external dependencies are reachable | [N]s | Flag degraded |
| 3 | Queue check | Report pending task count and oldest task age | [N]s | Log + continue |
| 4 | Budget check | Compare spend-to-date against BUDGET.md limits | [N]s | Alert if > [X]% |
| 5 | Anomaly scan | Check metrics for statistical deviation from baseline | [N]s | Escalate |
| 6 | Status report | Compile and deliver status report | [N]s | Retry once |
| 7 | [Custom action] | [Description] | [N]s | [behavior] |

## Status Report Format

Reports are delivered in [status_report_format] format.

### JSON Format
```json
{
  "agent_id": "uuid-from-ID.md",
  "agent_name": "string",
  "heartbeat_number": 0,
  "timestamp": "ISO-8601",
  "interval": "5m",
  "status": "healthy | degraded | critical",
  "uptime_seconds": 0,
  "health_checks": {
    "liveness": "pass | fail",
    "readiness": "pass | fail",
    "dependencies": {
      "database": "ok | degraded | down",
      "llm_api": "ok | degraded | down",
      "external_services": "ok | degraded | down"
    }
  },
  "workload": {
    "tasks_completed_since_last": 0,
    "tasks_pending": 0,
    "oldest_pending_seconds": 0,
    "error_count_since_last": 0
  },
  "budget": {
    "cycle_spend": "$0.00",
    "daily_spend": "$0.00",
    "monthly_spend": "$0.00",
    "budget_remaining_percent": 100,
    "budget_alert": false
  },
  "anomalies_detected": [],
  "next_heartbeat": "ISO-8601"
}
```

### Markdown Format
```markdown
## Heartbeat — [Agent Name] — [timestamp]
**Status:** [healthy | degraded | critical]
**Uptime:** [duration]

### Health: [pass/fail summary]
### Workload: [N] completed, [N] pending, [N] errors
### Budget: $[X] spent today ($[Y] remaining)
### Anomalies: [none | list]
```

## Delivery Channels

Reports are sent to all configured channels each cycle:

| Channel | Type | Destination | Priority filter |
|---------|------|-------------|----------------|
| Primary | [slack | email | webhook] | [URL or address] | All statuses |
| Operations | [webhook | log] | [URL or path] | degraded + critical |
| Escalation | [pagerduty | email] | [contact] | critical only |
| Log | file | [log path] | All (append) |

### Channel Failure
If a delivery channel fails:
1. Retry once after [N] seconds
2. Fall back to next channel in priority order
3. Always write to local log regardless of channel status
4. If all channels fail, escalate per ESCALATION.md Level 2

## Cost Budget Per Cycle

Each heartbeat cycle has a maximum budget to prevent runaway costs:

```yaml
cost_controls:
  max_per_cycle: $[amount]           # Hard limit per heartbeat
  max_daily: $[amount]               # Daily ceiling across all cycles
  max_monthly: $[amount]             # Monthly ceiling
  alert_threshold_percent: 80        # Alert when spend exceeds this %
  halt_threshold_percent: 100        # Halt heartbeats when exceeded
  budget_source: BUDGET.md           # Reference for overall limits
```

When budget is exceeded:
- At alert threshold: notify via delivery channels
- At halt threshold: stop heartbeat cycle, escalate per ESCALATION.md
- Resume only when budget resets or is manually increased

## Failure Behavior

What happens when a heartbeat cycle fails:

| Failure Type | Behavior | Max Retries | Escalation |
|-------------|----------|-------------|------------|
| Action timeout | Retry with backoff | [N] | After max retries |
| Delivery failure | Try next channel | [N] | After all channels fail |
| Health check fail | Log + flag degraded | 0 | If [N] consecutive |
| Budget exceeded | Halt heartbeats | 0 | Immediate |
| Unhandled error | Log + continue | 1 | After [N] occurrences |

### Consecutive Failure Tracking

**max_consecutive_failures:** [N]

When [N] consecutive heartbeat cycles fail entirely:
1. Trigger CIRCUITBREAKER.md for the heartbeat subsystem
2. Escalate per ESCALATION.md Level 2
3. Enter degraded mode — extend interval to [N]x normal
4. Require manual intervention to resume normal schedule

## Quiet Hours

Periods when heartbeats are suspended or reduced:

```yaml
quiet_hours:
  schedule: "[cron expression or human-readable]"
  behavior: suspend | reduce_frequency
  reduced_interval: "[interval if reduce_frequency]"
  resume_action: full_health_check    # Run full check on resume
  exceptions:
    - critical_alerts_still_fire: true
    - budget_checks_continue: true
```

During quiet hours:
- Standard heartbeat actions are [suspended | reduced]
- Critical monitoring continues per exceptions
- First heartbeat after quiet hours runs a full health check
- See WAKEUP.md for full re-initialization if needed

## Escalation on Anomaly

When a heartbeat detects anomalies:

| Anomaly Type | Severity | Notify | Response Time |
|-------------|----------|--------|---------------|
| Metric deviation > [N] stddev | Warning | Ops channel | Next business hour |
| Dependency degraded | Medium | Ops team | Within [N] minutes |
| Budget threshold exceeded | High | Budget owner + ops | Within [N] minutes |
| Health check failure | High | On-call engineer | Immediate |
| Security anomaly | Critical | Security team + ESCALATION.md Level 3 | Immediate |

Escalation contacts are defined in ESCALATION.md. Anomaly
detection baselines are established from MONITOR.md metrics.

## Health Check Integration

Each heartbeat cycle includes HEALTHCHECK.md probes:

```yaml
health_integration:
  run_probes: [liveness, readiness]  # Which HEALTHCHECK.md probes
  probe_timeout_ms: 5000             # Shorter than normal for heartbeat
  include_in_report: true            # Include results in status report
  on_probe_failure:
    liveness: escalate_immediately
    readiness: flag_degraded
```

_See HEALTHCHECK.md for probe definitions and MONITOR.md for metrics collection._
````

## Example Use Cases

**Enterprise:** A financial monitoring agent runs heartbeats every 5 minutes during market hours, checking portfolio data feeds, verifying API connections to three exchanges, enforcing a $2.50/cycle budget limit, and delivering JSON status reports to a Slack operations channel — with automatic escalation to the trading desk if any data feed shows latency above 500ms.

**Multi-Agent Fleet:** A fleet of 50 customer-support agents reports heartbeats every 15 minutes to a central orchestrator, which aggregates workload metrics to rebalance ticket routing, detects agents approaching budget limits before they halt, and identifies anomalous error patterns across the fleet before they cascade.

**Regulated Industry:** A pharmaceutical company's clinical-trial data agents run hourly heartbeats that verify data pipeline integrity, confirm encryption status on all patient data connections, log compliance metrics to a tamper-proof audit system per AUDITTRAIL.md, and automatically suspend operations during defined quiet hours to align with data processing windows approved by the IRB.

## Related Specs

| Spec | Relationship |
|------|-------------|
| BUDGET.md | Cost controls enforced per heartbeat cycle |
| CIRCUITBREAKER.md | Triggered on consecutive heartbeat failures |
| ESCALATION.md | Anomaly and failure notification routing |
| HEALTHCHECK.md | Liveness and readiness probes run each cycle |
| MONITOR.md | Metrics collection and dashboard configuration |
| SESSION.md | Per-task scoping between heartbeat cycles |
| SLA.md | Service level commitments verified each cycle |
| WAKEUP.md | Session startup and re-initialization |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
