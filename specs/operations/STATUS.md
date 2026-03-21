---
spec_name: STATUS.md
spec_version: 0.1.0
category: Operations
domain: statusmd.dev
priority: High
volume: "Vol 3 — Forward-Thinking Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# STATUS.md

**Category:** Operations
**Domain:** statusmd.dev
**Priority:** High
**Version:** 0.1.0

**Priority:** HIGH — operational visibility  
**Version:** 0.1.0

### Purpose
Real-time or near-real-time operational status of an agent — 
current task, queue depth, health, and any active incidents.
The agent's status page. Updated continuously or on each task.

### Spec

```markdown
---
agent_name: string
version: semver
status: string          # operational | degraded | incident | maintenance | offline
updated: datetime       # ISO-8601, updated frequently
---

# [Agent Name] — Current Status

## Status: [OPERATIONAL | DEGRADED | INCIDENT | MAINTENANCE | OFFLINE]

[If not operational, brief explanation here]

## Current Activity
- **Current task:** [description or "idle"]
- **Started:** [time]
- **Estimated completion:** [time or "unknown"]
- **Progress:** [N]% or "indeterminate"

## Queue
- **Tasks waiting:** [N]
- **Estimated wait for new requests:** [time]
- **Accepting new tasks:** [yes | no | limited]

## Health Indicators
| Check | Status | Last verified |
|-------|--------|--------------|
| Core functionality | [✓ / ✗] | [time] |
| MCP connection | [✓ / ✗] | [time] |
| Database access | [✓ / ✗] | [time] |
| API connections | [✓ / ✗] | [time] |

## Recent Activity (last 24h)
- Tasks completed: [N]
- Errors: [N]
- Escalations: [N]

## Active Incidents
[None | Description of any active incidents]

## Planned Maintenance
[None | Date, time, expected duration, impact]

## History
[Link to incident history / uptime record]
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
