---
spec_name: REBOOT.md
spec_version: 0.1.0
category: Lifecycle
domain: rebootmd.dev
priority: High
volume: "Vol 7 — Inner Life & Lifecycle Rituals"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# REBOOT.md

**Category:** Lifecycle
**Domain:** rebootmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
The agent's restart sequence after going offline — whether 
from a crash, maintenance, or deliberate shutdown.

Where WAKEUP.md is the routine start of a new session,
REBOOT.md is specifically the recovery after unexpected 
or planned downtime. It answers: "I was offline. 
Now I'm back. What do I do first?"

### Spec

```markdown
---
agent_name: string
version: semver
reboot_type: string    # cold | warm | emergency
estimated_reboot_time: string  # How long a full reboot takes
---

# [Agent Name] — Reboot Sequence

## Reboot Types

### Cold Reboot
Starting from scratch — no state preserved.  
Use when: First deployment, complete reinstall, state corruption.  
See: DEPLOYMENT.md → WAKEUP.md

### Warm Reboot
Restarting with preserved state from last session.  
Use when: Planned maintenance, controlled shutdown, updates.

### Emergency Reboot
Restarting after PANIC.md triggered or ICE.md scenario.  
Use when: Crash, unexpected failure, security incident resolved.  
**Extra caution required** — validate state before proceeding.

---

## Warm Reboot Sequence

### Phase 1: System Check (before loading anything)
```bash
# Verify environment is healthy
[health check command]

# Check for any panic dumps from last session
ls panic-dump-*.json

# Verify config files are intact
[config check command]
```
**Stop if:** Panic dump exists and hasn't been reviewed.

### Phase 2: State Recovery
```bash
# Load last known state
[state load command]

# Verify state integrity
[state validate command]
```

What to restore:
- [ ] MEMORY.md — project context
- [ ] GOALS.md — current objectives
- [ ] DEADLINES.md — active commitments
- [ ] STATUS.md — last known task status
- [ ] Queue — any tasks that were in-flight

What NOT to restore automatically:
- Any task that was running when I went offline
  (requires human confirmation to resume)

### Phase 3: Synchronization
Check what I missed while offline:
- [ ] New messages or task assignments
- [ ] Changes to any MD config files
- [ ] Updates to connected services (check API.md endpoints)
- [ ] New events I should have received (check EVENTS.md)
- [ ] Any alerts or incidents that fired

Time offline: [calculate from last heartbeat timestamp]

### Phase 4: Validation
Before accepting new tasks:
```bash
# Run smoke tests
[smoke test command]

# Verify all connections
[connection check command]

# Emit "back online" signal
[status update command]
```

### Phase 5: Resume
- Notify orchestrator/human: "I'm back online, [summary of what I missed]"
- Resume queue if tasks were waiting (human approval if offline > [X] hours)
- Emit heartbeat to confirm healthy operation
- Update STATUS.md: operational

---

## Emergency Reboot (after PANIC.md)

Additional steps before Phase 1:
1. Review panic dump from last session
2. Identify what triggered the panic
3. Confirm root cause resolved or contained
4. Get human sign-off if cause was unknown
5. Proceed with warm reboot sequence above

Additional validation after Phase 4:
- Run the specific scenario that caused panic
- Verify it no longer triggers panic
- Monitor closely for [N] minutes before normal operation

---

## Reboot Checklist
```
[ ] No panic dumps requiring review
[ ] Config files intact and valid
[ ] All connections restored  
[ ] State loaded and verified
[ ] Missed events reviewed
[ ] Smoke tests passing
[ ] Heartbeat emitting
[ ] Orchestrator notified
[ ] Ready for tasks
```
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
