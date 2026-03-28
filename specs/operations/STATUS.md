---
spec_name: STATUS.md
spec_version: 0.1.0
category: Operations
domain: statusmd.dev
priority: High
volume: "Vol 3 — Forward-Thinking Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# STATUS.md

**Category:** Operations
**Domain:** statusmd.dev
**Priority:** High
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
See HEALTHCHECK.md for full check definitions.
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
[None | Description of any active incidents — see HEARTBEAT.md for pulse monitoring]

## Planned Maintenance
[None | Date, time, expected duration, impact]

## History
[Link to incident history / uptime record]
```

## Example Use Cases

**Enterprise:** A project manager checks STATUS.md for the code-review agent before submitting a batch of pull requests, sees it is processing 8 queued tasks with a 45-minute estimated wait, and schedules the submission for after the queue clears.

**Multi-Agent Fleet:** A fleet status page aggregates STATUS.md from all agents, displaying a unified operational dashboard showing 47 agents operational, 2 in maintenance, and 1 in degraded state with a link to the active incident details.

**Regulated Industry:** An environmental monitoring agency's air-quality agents publish real-time STATUS.md pages that regulators can audit at any time, verifying continuous sensor coverage with timestamps proving no monitoring gaps exceeded the permitted 15-minute threshold.

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
