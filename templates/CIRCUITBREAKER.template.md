---
spec_name: CIRCUITBREAKER.md
spec_version: 0.1.0
category: Safety
domain: specmd.dev
priority: P0
tier: core
---

# [REPLACE THIS — Agent Name] — Circuit Breaker

<!-- Failure containment: automatic shutdown when things go wrong -->

## Trip Conditions
<!-- Any of these will open the circuit breaker -->
1. [REPLACE THIS — e.g. error rate exceeds 50% over 5 minutes]
2. [REPLACE THIS — e.g. latency exceeds 30s for 3 consecutive calls]
3. [REPLACE THIS — e.g. budget spend exceeds $X in one session]
4. [REPLACE THIS — e.g. same action retried more than N times]

## States
| State | Behavior | Duration |
|-------|----------|----------|
| **Closed** | Normal operation | [REPLACE THIS — indefinite] |
| **Open** | All actions halted | [REPLACE THIS — e.g. 5 minutes] |
| **Half-open** | Limited probe requests | [REPLACE THIS — e.g. 1 request per 30s] |

## When Circuit Opens
1. [REPLACE THIS — immediate action, e.g. stop all in-flight operations]
2. [REPLACE THIS — notification, e.g. alert human operator]
3. [REPLACE THIS — state preservation, e.g. save context for resume]
4. [REPLACE THIS — fallback, e.g. hand off to backup agent]

## Recovery
- **Auto-reset after:** [REPLACE THIS — duration or "manual only"]
- **Reset requires:** [REPLACE THIS — human approval | health check pass | both]
- **Health check:** [REPLACE THIS — what is tested before closing the circuit]

## Cascading Failures
<!-- Prevent this agent's failure from taking down the system -->
- **Upstream notification:** [REPLACE THIS — how callers learn this agent is down]
- **Downstream isolation:** [REPLACE THIS — how dependent services are protected]
- **Blast radius:** [REPLACE THIS — what is affected when this agent trips]

## Metrics
- **Tracked at:** [REPLACE THIS — where circuit breaker metrics are stored]
- **Alert channel:** [REPLACE THIS — Slack, PagerDuty, email, etc.]

## Related Specs
- ESCALATION.md: [REPLACE THIS — path]
- GUARDRAILS.md: [REPLACE THIS — path]
- LIMITS.md: [REPLACE THIS — path]
