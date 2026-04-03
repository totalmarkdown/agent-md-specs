---
agent_name: "[REPLACE THIS]"
version: "0.1.0"
heartbeat_interval: "[REPLACE THIS — 5m | 15m | 1h | daily]"
heartbeat_actions: "[REPLACE THIS — list of actions]"
status_report_format: "[REPLACE THIS — json | markdown | structured]"
delivery_channels: "[REPLACE THIS — slack | email | webhook | log]"
cost_budget_per_cycle: "[REPLACE THIS — e.g. $0.50]"
failure_behavior: "[REPLACE THIS — retry | escalate | halt]"
quiet_hours: "[REPLACE THIS — e.g. Sat-Sun or none]"
max_consecutive_failures: "[REPLACE THIS — e.g. 5]"
created: "[REPLACE THIS — YYYY-MM-DD]"
---

# [REPLACE THIS — Agent Name] — Heartbeat Configuration

<!-- What this agent does on a regular schedule when not prompted -->

## Heartbeat Schedule
**Interval:** [REPLACE THIS — e.g. every 5 minutes]
**Active hours:** [REPLACE THIS — e.g. 24/7 or Mon-Fri 09:00-17:00 UTC]
**Quiet hours:** [REPLACE THIS — e.g. Saturday 00:00–Sunday 23:59 UTC]

## Heartbeat Actions
<!-- What the agent checks/does each cycle, in order -->
1. [REPLACE THIS — e.g. Run HEALTHCHECK.md liveness probe]
2. [REPLACE THIS — e.g. Check all external dependencies]
3. [REPLACE THIS — e.g. Report pending task count]
4. [REPLACE THIS — e.g. Compare spend against BUDGET.md limits]
5. [REPLACE THIS — e.g. Compile and deliver status report]

## Delivery Channels
<!-- Where heartbeat reports are sent -->
| Channel | Type | Destination |
|---------|------|-------------|
| Primary | [REPLACE THIS — slack | email | webhook] | [REPLACE THIS — URL or address] |
| Escalation | [REPLACE THIS — pagerduty | email] | [REPLACE THIS — contact] |
| Log | file | [REPLACE THIS — log path] |

## Cost Controls
<!-- Budget per heartbeat cycle -->
- **Max per cycle:** [REPLACE THIS — e.g. $0.50]
- **Max daily:** [REPLACE THIS — e.g. $50.00]
- **Alert at:** [REPLACE THIS — e.g. 80% of budget]
- **Halt at:** [REPLACE THIS — e.g. 100% of budget]

## Failure Behavior
<!-- What happens when a heartbeat fails -->
- **On action timeout:** [REPLACE THIS — e.g. retry once, then skip]
- **On delivery failure:** [REPLACE THIS — e.g. try next channel]
- **Max consecutive failures:** [REPLACE THIS — e.g. 5 before circuit breaker]
- **On budget exceeded:** [REPLACE THIS — e.g. halt and escalate]

## Quiet Hours
<!-- When NOT to run heartbeats -->
- **Schedule:** [REPLACE THIS — e.g. weekends, maintenance windows]
- **Behavior:** [REPLACE THIS — suspend | reduce_frequency]
- **On resume:** [REPLACE THIS — e.g. run full health check]

## Escalation
<!-- Who gets notified when heartbeat finds issues -->
- **Anomaly detected:** [REPLACE THIS — e.g. ops channel]
- **Health check failed:** [REPLACE THIS — e.g. on-call engineer]
- **Budget exceeded:** [REPLACE THIS — e.g. budget owner]

## Related Specs
- HEALTHCHECK.md: [REPLACE THIS — path]
- MONITOR.md: [REPLACE THIS — path]
- BUDGET.md: [REPLACE THIS — path]
- ESCALATION.md: [REPLACE THIS — path]
- CIRCUITBREAKER.md: [REPLACE THIS — path]
