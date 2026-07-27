---
spec_name: EVENTS.md
spec_version: 0.1.0
category: Technical
priority: Medium
volume: "Vol 6 — Hierarchy Completion & Identity Anchors"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---


# EVENTS.md

**Category:** Technical
**Priority:** Medium
**Version:** 0.1.0 **Type:** Static

### Purpose
Defines events this agent emits and events it listens for — 
the agent's event-driven interface. Essential for building 
reactive multi-agent systems where agents trigger each other 
based on conditions rather than explicit task delegation.

### Spec

````markdown
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

_See AUDITTRAIL.md for tamper-evident logging of all emitted events._

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
````

## Example Use Cases

**Enterprise:** A customer success team configures EVENTS.md so their support agent emits a `ticket.escalated` event whenever sentiment analysis detects frustration, triggering a separate agent to draft a proactive outreach email to the account manager.

**Multi-Agent Fleet:** An orchestrator subscribes to `task.completed` events from all worker agents via EVENTS.md, using correlation IDs to track end-to-end workflow progress and triggering the next agent in the pipeline within seconds of completion.

**Regulated Industry:** A trading firm uses EVENTS.md to ensure its compliance monitoring agent emits `error.critical` events for every trade that exceeds risk thresholds, with the event bus configured for exactly-once delivery so no violation alert is lost or duplicated.

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
