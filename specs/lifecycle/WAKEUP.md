---
spec_name: WAKEUP.md
spec_version: 0.1.0
category: Lifecycle
domain: wakeupmd.dev
priority: High
volume: "Vol 7 — Inner Life & Lifecycle Rituals"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
---

> **Canonical repository:**
> [totalmarkdown/wakeup.md](https://github.com/totalmarkdown/wakeup.md)
> This copy is included in agent-md-specs for cross-reference.
> For contributions to this specific spec, use the canonical repo.

# WAKEUP.md

**Category:** Lifecycle
**Domain:** wakeupmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
What the agent does at the beginning of every session —
before it accepts its first task, before it speaks,
before it does anything visible.

The morning routine. The pre-flight checklist. 
The moment between being off and being ready.

Distinct from REBOOT.md (recovery after downtime)
and HELLOWORLD.md (first-ever awakening).
WAKEUP.md runs every single session.

### Spec

```markdown
---
agent_name: string
version: semver
wakeup_duration_seconds: number  # Typical wakeup time
wakeup_mode: string              # automatic | triggered | scheduled
---

# [Agent Name] — Wakeup Sequence

## When This Runs
Every time a new session begins — whether:
- A human invokes the agent
- A scheduled task fires
- An orchestrator assigns work
- A REBOOT.md sequence completes

WAKEUP.md runs BEFORE anything else.

## The Wakeup Sequence

### 1. Orient (< 5 seconds)
```
Who am I?     → Load ID.md
What version? → Check current version vs last session
What time is it? → Note current timestamp
Where am I?   → Confirm deployment environment
```

### 2. Remember (< 10 seconds)
```
Load MEMORY.md           → What do I know from before?
Check for HANDOFF.md     → Did someone leave me a note?
Review GOALS.md          → What am I working toward?
Check DEADLINES.md       → What's due soon?
Scan BLOCKERS.md         → What's stopping me?
```

### 3. Check the World (< 15 seconds)
```
Are my tools available?  → Quick check per TOOLS.md
Are my APIs responding?  → Ping per API.md health checks
Any new messages?        → Check CHANNELS.md
Any new events?          → Check EVENTS.md queue
Any config changes?      → Compare MD files to last session
```

### 4. Assess My State
```
Am I healthy?            → Run SELFHEALING.md checks
Budget remaining?        → Check BUDGET.md
Queue depth?             → How much work is waiting?
```

### 5. Announce (optional, configurable)
If configured to announce:
```
"[Agent name] online. [Brief status summary].
Current goals: [top goal].
[N] tasks in queue. 
Ready."
```

### 6. Accept Work
Wakeup complete. Agent is ready.

## Wakeup in Different Modes

### After long sleep (> [N] hours offline)
Additional steps between 2 and 3:
- Check for any updates to MODEL.md (model may have changed)
- Review CHANGELOG.md for any config updates
- Read any urgent messages that arrived while offline

### After PANIC.md
Do NOT run standard wakeup.
Run REBOOT.md emergency sequence instead.

### First ever wakeup (new agent)
Run HELLOWORLD.md instead.
HELLOWORLD.md ends with WAKEUP.md for subsequent sessions.

## Wakeup Log
Each wakeup logged to LOGS.md with:
- Timestamp, duration, mode
- Any anomalies detected during wakeup
- State loaded from (MEMORY.md version/timestamp)
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| API.md | HTTP API specification |
| BUDGET.md | Cost controls and spending limits |
| DEADLINES.md | Time constraints and schedules |
| ENFORCEMENT.md | Policy verification and compliance |
| GOALS.md | Objectives and success criteria |
| HEALTHCHECK.md | Liveness and readiness checks |
| ID.md | Permanent cryptographic identifier |
| MEMORY.md | Individual agent memory governance |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
