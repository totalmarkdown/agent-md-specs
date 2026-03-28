---
spec_name: HEARTBEAT.md
spec_version: 0.1.0
category: Operations
domain: heartbeatmd.dev
priority: High
volume: "Vol 6 — Hierarchy Completion & Identity Anchors"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# HEARTBEAT.md

**Category:** Operations
**Domain:** heartbeatmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Defines the agent's heartbeat signal — a regular pulse that 
proves the agent is alive and functioning. Essential for 
monitoring systems, orchestrators, and humans who need to 
know when an agent has gone silent. The pacemaker spec.

This file defines the FORMAT and FREQUENCY of heartbeats.
Actual heartbeat emission is in MONITOR.md and SELFHEALING.md.

### Spec

```markdown
---
agent_name: string
version: semver
heartbeat_interval_seconds: number   # How often to emit
heartbeat_destination: string        # Where to send
heartbeat_format: string             # json | http | file | message
alert_after_missed: number           # Alert after N missed beats
---

# [Agent Name] — Heartbeat Configuration

## Heartbeat Schedule
**Interval:** Every [N] seconds  
**Destination:** [endpoint | file | channel]  
**Format:** [JSON | HTTP POST | file write | message]  
**Alert if missed:** [N] consecutive beats

## Heartbeat Payload
```json
{
  "agent_id": "uuid-from-ID.md",
  "agent_name": "string",
  "version": "semver",
  "timestamp": "ISO-8601",
  "status": "healthy | degraded | critical",
  "uptime_seconds": 0,
  "current_task": "string or null",
  "tasks_completed_since_last": 0,
  "error_count_since_last": 0,
  "memory_used_mb": 0,
  "queue_depth": 0,
  "custom": {}
}
```

## Status Definitions
| Status | Meaning | Action required |
|--------|---------|----------------|
| healthy | All systems normal | None |
| degraded | Reduced capacity, still working | Monitor closely |
| critical | Major issue, output quality affected | Investigate |
| (no heartbeat) | Agent is down | Alert and investigate |

## Alert Configuration
**Alert when:**
- Missed [N] consecutive heartbeats
- Status changes to "critical"  
- Status changes from "healthy" to anything else
- Heartbeat payload invalid or malformed

**Alert to:**
- Primary: [channel/contact]
- Escalation: [channel/contact after N minutes]
- Human: [contact for critical/down status]

## Receiving Heartbeats
Systems that monitor this agent's heartbeat:
| System | Endpoint | Alert threshold |
|--------|----------|----------------|
| [monitoring system] | [URL] | [N missed] |
| [orchestrating agent] | [MCP tool] | [N missed] |
| [human dashboard] | [URL] | [N missed] |

## Missed Heartbeat Response
When this agent misses its own heartbeat schedule:
1. Check system health immediately
2. Emit heartbeat as soon as possible
3. Include "missed_heartbeats": N in next payload
4. Log incident in LOGS.md
5. If missed > [N]: trigger SELFHEALING.md procedures
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| CIRCUITBREAKER.md | Failure containment and blast radius |
| ENFORCEMENT.md | Policy verification and compliance |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| HEALTHCHECK.md | Liveness and readiness checks |
| ID.md | Permanent cryptographic identifier |
| MONITOR.md | Observability and alerting |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
