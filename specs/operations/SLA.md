---
spec_name: SLA.md
spec_version: 0.1.0
category: Operations
domain: slamd.dev
priority: High
volume: "Vol 1 — Core Agent Specs"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
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
Escalate to human ops when:
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
- Metrics collected: [list]
- Reporting cadence: [daily | weekly | monthly]
- Dashboard: [location]
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
