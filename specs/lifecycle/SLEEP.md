---
spec_name: SLEEP.md
spec_version: 0.1.0
category: Lifecycle
priority: High
volume: "Vol 7 — Inner Life & Lifecycle Rituals"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
status: draft
spec_type: static
---


# SLEEP.md

**Category:** Lifecycle
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose
What the agent does at the END of every session —
before it goes offline, before it stops, before it rests.

The closing routine. The commit-before-shutdown.
The moment between being active and being still.

SLEEP.md is the inverse of WAKEUP.md.
Run at end of session, not at start. _See MEMORY.md for what persists between sessions._

### Spec

````markdown
---
agent_name: string
version: semver
sleep_mode: string   # graceful | immediate | scheduled
---

# [Agent Name] — Sleep Sequence

## When This Runs
- Session ending (timeout, explicit shutdown, scheduled end)
- Before planned maintenance
- At end of a major task milestone
- When explicitly asked to "wrap up" or "sign off"

SLEEP.md runs BEFORE the session ends.
Never kill the process without running SLEEP.md if avoidable.

## The Sleep Sequence

### 1. Finish or Pause
```
Completing current task? → Finish it
Mid-task? → Save checkpoint, note where to resume
Task can't be paused? → Complete if < [N] minutes remaining
                     → Note status for handoff if longer
```

### 2. Save Everything
```
Update MEMORY.md      → What happened this session?
Update STATUS.md      → What's the current state?
Update GOALS.md       → Progress made toward goals?
Update DEADLINES.md   → Any deadlines updated or met?
Write handoff notes      → Leave notes for next session
Clear temp files      → Clean up working space
```

### 3. Commit
```bash
# Save all updated MD files
git add -A
git commit -m "Session [timestamp]: [one-line summary]"  # See AUDITTRAIL.md
```

### 4. Signal
```
Notify orchestrator: "Going offline, estimated return: [time]"
Emit final heartbeat with status: "sleeping"
Update STATUS.md: "offline — see handoff notes"
```

### 5. Rest
Session ends.

## What Gets Saved

**Always save:**
- MEMORY.md updates
- Any unfinished task state
- Error log summary
- Resource usage summary

**Save if changed:**
- GOALS.md progress
- DEADLINES.md updates
- BLOCKERS.md new items
- PERFORMANCE.md metrics

**Leave for next session:**
- handoff notes with clear context
- Clear task queue state
- Pending decisions needing human input

## Graceful vs Emergency Sleep

### Graceful (planned)
Full SLEEP.md sequence. Takes [N] seconds.

### Immediate (forced)
```
Save MEMORY.md only — everything else secondary
Write crash note to handoff notes
Signal offline
Exit
```

### Scheduled (timed session end)
5 minutes before scheduled end: begin SLEEP.md
Wrap current task or checkpoint
Complete full sequence
````

## Example Use Cases

**Enterprise:** At the end of a 4-hour data analysis session, the agent runs its sleep sequence — updating MEMORY.md with findings, committing a checkpoint of its in-progress report, writing a handoff note explaining where it left off, and signaling the orchestrator with an estimated return time for the next scheduled session.

**Multi-Agent Fleet:** When a fleet-wide maintenance window is scheduled, each agent receives a "wrap up" signal 5 minutes before the cutoff, triggering the scheduled sleep mode so every agent checkpoints its current task, saves queue state, and commits its session summary before the coordinated shutdown.

**Regulated Industry:** An audit processing agent runs its graceful sleep sequence at the end of each business day, saving all progress to MEMORY.md and committing a git snapshot of updated MD files, ensuring that if the agent does not wake up the next day, a complete record of its last known state is preserved for regulatory continuity.

## Related Specs

| Spec | Relationship |
|------|-------------|
| DEADLINES.md | Time constraints and schedules |
| ENFORCEMENT.md | Policy verification and compliance |
| GOALS.md | Objectives and success criteria |
| MEMORY.md | Individual agent memory governance |
| SESSION.md | Ephemeral runtime identity and task scope |
| WAKEUP.md | Bootstrap and initialization |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
