---
spec_name: SLA.md
spec_version: 0.1.0
category: Operations
domain: slamd.dev
priority: High
volume: "Vol 1 — Core Agent Specs"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
---

# SLA.md

**Category:** Operations
**Domain:** slamd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Defines service level agreements — response times, uptime targets, 
throughput commitments, and escalation triggers when SLAs are at risk.

### Spec

```markdown
---
agent_name: string
version: semver
service_tier: string   # bronze | silver | gold | platinum
created: date
updated: date
---

# [Agent Name] — Service Level Agreement

## Response Time Targets
| Request Type | Target | Maximum | Priority |
|-------------|--------|---------|----------|
| Standard task | [X min] | [Y min] | normal |
| Urgent task | [X min] | [Y min] | high |
| Batch processing | [X hr] | [Y hr] | low |

## Availability
- **Target uptime:** [99.X]%
- **Planned maintenance window:** [day/time]
- **Maximum planned downtime:** [X hours/month]

## Throughput
- **Maximum concurrent tasks:** [N]
- **Maximum tasks per hour:** [N]
- **Queue depth limit:** [N tasks]

## Escalation Triggers
Escalate to human ops when (see ESCALATION.md for routing):
- Response time exceeds [X minutes]
- Error rate exceeds [X]% in any [Y] minute window
- Queue depth exceeds [N] tasks
- Any single task runs longer than [X minutes]

## Exclusions
SLA does not apply to:
- Scheduled maintenance windows
- Force majeure events
- Requests exceeding defined input limits
- Third-party API outages

## Measurement and Reporting
- Metrics collected: [list] (see MONITOR.md for full metric definitions)
- Reporting cadence: [daily | weekly | monthly]
- Dashboard: [location]
- Cost tracking: see BUDGET.md for spending guardrails
```

## Example Use Cases

**Enterprise:** A SaaS company defines gold-tier SLAs for its enterprise clients' dedicated agents -- 99.9% uptime, 2-minute response time for urgent tasks -- with automatic escalation to human ops when any metric approaches the SLA threshold.

**Multi-Agent Fleet:** A marketplace platform publishes SLA.md for each agent available for hire, letting customers compare response time targets and throughput guarantees before selecting which agent to engage for a project.

**Regulated Industry:** A securities trading firm's order-execution agent commits to sub-500ms response times during market hours with 99.99% availability, with SLA exclusions clearly documenting that third-party exchange outages are not counted against uptime.

## Related Specs

| Spec | Relationship |
|------|-------------|
| BUDGET.md | Cost controls and spending limits |
| CIRCUITBREAKER.md | Failure containment and blast radius |
| ENFORCEMENT.md | Policy verification and compliance |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| HEALTHCHECK.md | Liveness and readiness checks |
| MONITOR.md | Observability and alerting |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
