---
spec_name: INTERRUPT.md
spec_version: 0.1.0
category: Operations
domain: interruptmd.dev
priority: Medium
volume: "Vol 7 — Inner Life & Lifecycle Rituals"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---


# INTERRUPT.md

**Category:** Operations
**Domain:** interruptmd.dev
**Priority:** Medium
**Version:** 0.1.0 **Type:** Static

### Purpose
How to safely interrupt this agent mid-task — 
pause it, redirect it, or stop it without losing 
work or corrupting state.

Every agent running autonomous tasks needs a 
safe interrupt protocol. INTERRUPT.md defines it.

### Spec

```markdown
---
agent_name: string
version: semver
interrupt_safe: boolean   # Does agent support safe interrupts?
checkpoint_frequency: string  # How often state is saved
---

# [Agent Name] — Interrupt Protocol

## Interrupt Levels

### Level 1: Pause (complete current step, then stop)
**Command:** [pause command]  
**What happens:** Finish current atomic operation, checkpoint, wait  
**State preserved:** Yes — full  
**Resume with:** [resume command]  
**Use when:** Need to review progress, inject new context

### Level 2: Redirect (complete current step, then change direction)
**Command:** [redirect command] + new instruction  
**What happens:** Finish current step, then follow new instruction  
**State preserved:** Yes — partial (task history kept)  
**Use when:** Goal has changed but work so far is useful

### Level 3: Stop (stop at next safe checkpoint)
**Command:** [stop command]  
**What happens:** Complete or abort current operation, save state, stop  
**State preserved:** Checkpoint saved  
**Resume with:** Requires explicit restart  
**Use when:** Done for the session, switching tasks

### Level 4: Kill (immediate stop — may lose state)
**Command:** [kill -9 or equivalent]
**What happens:** Immediate termination
**State preserved:** Best effort — may lose current operation
**Use when:** Emergency only — see PANIC.md (see also CIRCUITBREAKER.md for automated containment)
**Recovery:** See REBOOT.md

## Checkpoint System
This agent checkpoints every: [N operations | N seconds | on request]  
Checkpoint location: [path]  
Checkpoint format: [JSON snapshot of current state]  
Maximum checkpoints kept: [N] (oldest deleted automatically)

## Safe Interrupt Signals
| Signal | Effect | Safe? |
|--------|--------|-------|
| [signal 1] | Pause after current step | ✓ Yes |
| [signal 2] | Stop after current task | ✓ Yes |
| [signal 3] | Immediate stop | ⚠ May lose state |

## After Interrupt
Agent will:
1. Save checkpoint
2. Write summary to handoff notes: "Interrupted at [point], [status]"
3. Emit status signal: "paused" or "stopped" (see handoff notes)
4. Wait for resume or restart command
```

## Example Use Cases

**Enterprise:** A legal firm's document-review agent supports Level 1 (pause) interrupts so attorneys can inject newly discovered evidence mid-analysis without losing the agent's progress through a 10,000-document review.

**Multi-Agent Fleet:** An orchestrator issues Level 2 (redirect) interrupts to a research agent fleet when business priorities shift, allowing agents to checkpoint their current analysis and pivot to a newly urgent competitor intelligence request.

**Regulated Industry:** A nuclear facility's safety-monitoring agent defines Level 4 (kill) protocols with explicit state recovery procedures, ensuring that even an emergency shutdown preserves the last known sensor readings for regulatory incident reporting.

## Related Specs

| Spec | Relationship |
|------|-------------|
| CIRCUITBREAKER.md | Failure containment and blast radius |
| ENFORCEMENT.md | Policy verification and compliance |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| HEALTHCHECK.md | Liveness and readiness checks |
| MONITOR.md | Observability and alerting |
| PANIC.md | Panic-mode emergency response |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
