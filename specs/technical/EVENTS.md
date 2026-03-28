---
spec_name: EVENTS.md
spec_version: 0.1.0
category: Technical
domain: eventsmd.dev
priority: Medium
volume: "Vol 6 — Hierarchy Completion & Identity Anchors"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# EVENTS.md

**Category:** Technical
**Domain:** eventsmd.dev
**Priority:** Medium
**Version:** 0.1.0

### Purpose
Defines events this agent emits and events it listens for — 
the agent's event-driven interface. Essential for building 
reactive multi-agent systems where agents trigger each other 
based on conditions rather than explicit task delegation.

### Spec

```markdown
---
agent_name: string
version: semver
event_bus: string    # kafka | rabbitmq | redis | webhook | n8n | custom
---

# [Agent Name] — Events

## Events I Emit
Events this agent publishes when things happen:

| Event name | When triggered | Payload | Consumers |
|-----------|---------------|---------|-----------|
| [event.name] | [trigger condition] | [payload schema] | [who listens] |
| task.completed | Every task finishes | {task_id, result, quality} | orchestrators |
| error.critical | Critical error occurs | {error, context, timestamp} | monitors |
| [custom event] | [condition] | [schema] | [consumers] |

## Events I Listen For
Events this agent responds to:

| Event name | Source | My response | Priority |
|-----------|--------|-------------|---------|
| [event.name] | [emitting agent/system] | [what I do] | [H/M/L] |
| task.assigned | orchestrator | Begin task processing | High |
| config.updated | admin | Reload configuration | High |
| [custom event] | [source] | [response] | [priority] |

## Event Schema

### [event.name]
```json
{
  "event": "event.name",
  "version": "1.0",
  "source_agent": "uuid",
  "timestamp": "ISO-8601",
  "correlation_id": "uuid",
  "payload": {
    "field1": "type",
    "field2": "type"
  }
}
```

## Event Bus Configuration
**Bus type:** [kafka | rabbitmq | redis | webhook | n8n | custom]  
**Connection:** [from environment — see Doppler]  
**Topic/queue prefix:** [agent-name]  
**Retry policy:** [N retries with [backoff] backoff]  
**Dead letter:** [where failed events go]

_See AUDITTRAIL.md for tamper-proof logging of all emitted events._

## Event Ordering Guarantees
- Events within a task: [ordered | best-effort]
- Events across tasks: [no guarantee | partition-ordered]
- Duplicate events: [idempotent handling | exactly-once]

## Monitoring Events
Subscribe to these to monitor this agent:
| Subscription | What you'll see |
|-------------|----------------|
| [agent-name].* | All events from this agent |
| [agent-name].error.* | All errors |
| [agent-name].task.* | Task lifecycle |
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| INPUT.md | Accepted input formats |
| MCP.md | Model Context Protocol connections |
| OUTPUT.md | Output formats and delivery |
| PERMISSIONS.md | Static resource access control |
| TOOLS.md | Available tools and capabilities |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
