---
spec_name: PROTOCOL.md
spec_version: 0.1.0
category: Coordination
domain: protocolmd.dev
priority: High
volume: "Vol 1 — Core Agent Specs"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# PROTOCOL.md

**Category:** Coordination
**Domain:** protocolmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Defines the communication format and rules between agents in a team — 
message structure, acknowledgment requirements, and handoff formats.

### Spec

```markdown
---
protocol_version: semver
compatible_with: list   # Which TEAM.md versions use this protocol
created: date
---

# Inter-Agent Communication Protocol

## Message Format
All inter-agent messages use this structure:
```json
{
  "from": "agent-name",
  "to": "agent-name | human | broadcast",
  "type": "task | result | question | escalation | status",
  "priority": "low | normal | high | urgent",
  "task_id": "unique-id",
  "parent_task_id": "id-of-originating-task",
  "payload": {},
  "timestamp": "ISO-8601",
  "requires_acknowledgment": boolean
}
```

## Message Types

### Task message
Assigns work to another agent:
```json
{
  "type": "task",
  "payload": {
    "instruction": "clear instruction",
    "context": "relevant background",
    "inputs": {},
    "expected_output": "description",
    "deadline": "ISO-8601 or null"
  }
}
```

### Result message
Returns completed work:
```json
{
  "type": "result", 
  "payload": {
    "status": "success | partial | failed",
    "output": {},
    "confidence": 0.0-1.0,
    "notes": "any caveats or observations"
  }
}
```

## Acknowledgment Rules
- Urgent messages: acknowledge within [X seconds]
- Normal messages: acknowledge within [X minutes]
- Low priority: acknowledge within [X hours]
- If no acknowledgment received: [retry | escalate | continue]

## Handoff Requirements
Before handing off to another agent, sending agent must include:
- [ ] Task ID (for tracking)
- [ ] Full context needed to complete the task
- [ ] Any intermediate results produced so far
- [ ] Known constraints or complications
- [ ] Expected output format

## Conflict Resolution
If two agents receive conflicting instructions:
1. Higher priority message takes precedence
2. If same priority: most recent message takes precedence
3. If genuinely ambiguous: escalate per ESCALATION.md
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
