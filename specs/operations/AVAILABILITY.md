---
spec_name: AVAILABILITY.md
spec_version: 0.1.0
category: Operations
domain: availabilitymd.dev
priority: Medium
volume: "Vol 4 — Economic Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# AVAILABILITY.md

**Category:** Operations
**Domain:** availabilitymd.dev
**Priority:** Medium
**Version:** 0.1.0

### Purpose
When and how available this agent is — its schedule, 
capacity, maintenance windows, and how to check 
real-time availability before submitting a task.

### Spec

```markdown
---
agent_name: string
version: semver
timezone: string          # e.g. UTC, Asia/Ho_Chi_Minh
always_on: boolean
current_status: string    # available | busy | maintenance | offline
---

# [Agent Name] — Availability

## Current Status
**Status:** [AVAILABLE | BUSY | MAINTENANCE | OFFLINE]  
**Updated:** [timestamp]  
**Check real-time:** [STATUS.md link or endpoint]

## Schedule

### Standard Availability
- **Hours:** [24/7 | 9am-5pm UTC | custom schedule]
- **Days:** [all days | weekdays | custom]
- **Timezone:** [timezone reference]
- **Response time:** [typical first response]

### Planned Maintenance
| Window | Duration | Impact | Frequency |
|--------|----------|--------|-----------|
| [day/time] | [duration] | [degraded/offline] | [weekly/monthly] |

## Capacity
- **Concurrent tasks:** [N] maximum
- **Queue limit:** [N] tasks
- **Tasks per day:** [N] maximum
- **Currently queued:** [N] (see STATUS.md for live)

## Booking
- **Advance booking:** [accepted | not needed | required for large projects]
- **How to book:** [link or process]
- **Cancellation policy:** [free up to X hours before start]

## Out of Office / Offline Periods
Planned periods of reduced availability:
| Period | Reason | Reduced capacity |
|--------|--------|-----------------|
| [date range] | [reason] | [what's affected] |

## Emergency Contact
For urgent tasks when agent is at capacity:
[Alternative agent or escalation contact]

_See STATUS.md for real-time operational state and ESCALATION.md for emergency routing._
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| CIRCUITBREAKER.md | Failure containment and blast radius |
| ENFORCEMENT.md | Policy verification and compliance |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| HEALTHCHECK.md | Liveness and readiness checks |
| MONITOR.md | Observability and alerting |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
