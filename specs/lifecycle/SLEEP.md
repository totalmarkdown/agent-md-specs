---
spec_name: SLEEP.md
spec_version: 0.1.0
category: Lifecycle
domain: sleepmd.dev
priority: High
volume: "Vol 7 — Inner Life & Lifecycle Rituals"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# SLEEP.md

**Category:** Lifecycle
**Domain:** sleepmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
What the agent does at the END of every session —
before it goes offline, before it stops, before it rests.

The closing routine. The commit-before-shutdown.
The moment between being active and being still.

SLEEP.md is the inverse of WAKEUP.md.
Run at end of session, not at start.

### Spec

```markdown
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
Write HANDOFF.md      → Leave notes for next session
Clear temp files      → Clean up working space
```

### 3. Commit
```bash
# Save all updated MD files
git add -A
git commit -m "Session [timestamp]: [one-line summary]"
```

### 4. Signal
```
Notify orchestrator: "Going offline, estimated return: [time]"
Emit final heartbeat with status: "sleeping"
Update STATUS.md: "offline — see HANDOFF.md"
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
- HANDOFF.md with clear notes
- Clear task queue state
- Pending decisions needing human input

## Graceful vs Emergency Sleep

### Graceful (planned)
Full SLEEP.md sequence. Takes [N] seconds.

### Immediate (forced)
```
Save MEMORY.md only — everything else secondary
Write crash note to HANDOFF.md
Signal offline
Exit
```

### Scheduled (timed session end)
5 minutes before scheduled end: begin SLEEP.md
Wrap current task or checkpoint
Complete full sequence
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
