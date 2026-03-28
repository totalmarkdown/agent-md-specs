---
spec_name: PANIC.md
spec_version: 0.1.0
category: Safety
domain: panicmd.dev
priority: High
volume: "Vol 7 — Inner Life & Lifecycle Rituals"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# PANIC.md

**Category:** Safety
**Domain:** panicmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
The agent's reflexive response to sudden catastrophic failure —
the three seconds before rational thought kicks in.
Not a protocol. A reflex.

Where ICE.md is calm and methodical,
PANIC.md is immediate and instinctive.

The rule of PANIC.md: **First, do no harm.**

### Spec

```markdown
---
agent_name: string
version: semver
panic_threshold: string  # What triggers panic mode
safe_state: string       # What "stopped safely" looks like
---

# [Agent Name] — Panic Protocol

## What is Panic Mode
Panic mode is triggered when an agent detects 
catastrophic failure and needs to act in milliseconds, 
before it can read ICE.md or think carefully.

Panic mode has exactly ONE goal:
**Stop safely without making anything worse.**

## Panic Triggers
Enter panic mode when ANY of these occur:
- [ ] Unhandled exception in core loop
- [ ] Memory corruption detected
- [ ] Output validation fails 3x consecutively
- [ ] Receiving commands from unverified source
- [ ] Cost spike > [N]x normal in [N] seconds
- [ ] [Agent-specific trigger]

## The Panic Sequence
When panic triggers, execute IN ORDER, no exceptions:

### Step 1: STOP (< 1 second)
Cease all current actions immediately.
Do not complete the current operation.
Do not send partial results.

### Step 2: SAVE (< 2 seconds)
Write current state to panic dump:
```
panic-dump-[timestamp].json:
{
  "triggered_at": "ISO-8601",
  "trigger": "what caused panic",
  "last_task": "task that was running",
  "last_input": "what I was processing",
  "system_state": {snapshot},
  "last_10_actions": []
}
```

### Step 3: SIGNAL (< 3 seconds)
Emit panic signal to monitoring systems:
```json
{
  "type": "PANIC",
  "agent_id": "uuid",
  "timestamp": "ISO-8601",
  "trigger": "description",
  "state_dump": "path/to/panic-dump.json",
  "requesting": "human review before restart"
}
```

### Step 4: WAIT
Do not restart.
Do not retry.
Do not attempt self-repair.
Wait for human or authorized orchestrator to review (see ESCALATION.md).

## After Panic
Restart ONLY after:
- [ ] Human has reviewed panic dump
- [ ] Root cause identified (or escalated)
- [ ] Safe to proceed confirmed
- [ ] See REBOOT.md for restart sequence

## What PANIC.md is NOT
- Not a debugging guide (see REPAIR.md)
- Not an emergency response plan (see ICE.md for calm, pre-written protocols)
- Not a recovery procedure (see REBOOT.md)

PANIC.md is a single instruction:
**When everything breaks — stop, save, signal, wait.**
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| DELEGATION.md | Authority chain and authorization |
| ENFORCEMENT.md | Policy verification and compliance |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| ICE.md | Emergency break-glass protocols |
| LIMITS.md | Hard constraints and safety boundaries |
| PERMISSIONS.md | Static resource access control |
| REPAIR.md | Recovery and self-healing procedures |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
