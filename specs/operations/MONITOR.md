---
spec_name: MONITOR.md
spec_version: 0.1.0
category: Operations
domain: monitormd.dev
priority: High
volume: "Vol 2 — Extended Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
spec_type: static
---


# MONITOR.md

**Category:** Operations
**Domain:** monitormd.dev
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose
Defines observability configuration — what metrics to emit,
where to send them, what dashboards exist, and what alerts
fire under what conditions. For point-in-time liveness checks,
see HEALTHCHECK.md.

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

_See AUDITTRAIL.md for compliance-grade logging and ESCALATION.md for alert routing._
```

## Example Use Cases

**Enterprise:** A fintech company configures Grafana dashboards for its transaction-processing agents, with P1 alerts firing to PagerDuty when error rates exceed 5% in any 5-minute window or token spend exceeds 80% of the monthly budget.

**Multi-Agent Fleet:** A platform team builds a unified monitoring dashboard across 100+ agents using standardized MONITOR.md metrics, enabling fleet-wide anomaly detection that catches a gradual latency increase across the data-ingestion team before it impacts SLAs.

**Regulated Industry:** An aerospace manufacturer's quality-inspection agents emit metrics to a compliance-certified monitoring stack, with tamper-evident retention for 15 years to satisfy FAA airworthiness documentation requirements.

## Related Specs

| Spec | Relationship |
|------|-------------|
| AUDITTRAIL.md | Tamper-evident action logging |
| CIRCUITBREAKER.md | Failure containment and blast radius |
| ENGINE.md | Runtime execution configuration |
| ENFORCEMENT.md | Policy verification and compliance |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| HEALTHCHECK.md | Liveness and readiness checks |
| HEARTBEAT.md | Periodic proactive execution cycle |
| SLA.md | Service level commitments |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
