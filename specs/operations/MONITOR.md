---
spec_name: MONITOR.md
spec_version: 0.1.0
category: Operations
domain: monitormd.dev
priority: High
volume: "Vol 2 — Extended Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# MONITOR.md

**Category:** Operations
**Domain:** monitormd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Defines observability configuration — what metrics to emit, 
where to send them, what dashboards exist, and what alerts 
fire under what conditions.

### Spec

```markdown
---
agent_name: string
version: semver
monitoring_stack: string   # Grafana | Datadog | CloudWatch | custom
alert_channel: string      # Slack channel | email | PagerDuty
created: date
updated: date
---

# [Agent Name] — Monitoring Configuration

## Metrics Emitted
| Metric name | Type | Unit | Description | Emit frequency |
|------------|------|------|-------------|----------------|
| tasks_completed_total | counter | count | Tasks finished | On each completion |
| task_duration_seconds | histogram | seconds | Task execution time | On each completion |
| errors_total | counter | count | All errors | On each error |
| tokens_used_total | counter | tokens | API tokens consumed | On each call |
| [custom metric] | [type] | [unit] | [description] | [frequency] |

## Dashboards
| Dashboard | URL | Shows |
|-----------|-----|-------|
| Agent Overview | [URL] | Health, throughput, errors |
| Cost Tracking | [URL] | Token usage, costs |
| [Custom] | [URL] | [what] |

## Alert Rules
| Alert name | Condition | Severity | Notification |
|-----------|-----------|----------|-------------|
| High error rate | errors > [N]% in [X]min | P1 | [channel] immediately |
| Budget warning | spend > [X]% monthly | P2 | [channel] within 1hr |
| Agent down | no heartbeat [N]min | P1 | [channel] immediately |
| Slow response | p99 latency > [X]ms | P3 | [channel] within 4hr |
| [Custom alert] | [condition] | [P1-P4] | [notification] |

## Log Aggregation
- Log destination: [log aggregation service or path]
- Log level: [DEBUG | INFO | WARN | ERROR]
- Log retention: [X days]
- Structured logging: [JSON | plain text]
- Required fields in every log line: timestamp, level, agent, task_id, message
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
