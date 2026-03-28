---
spec_name: REBOOT.md
spec_version: 0.1.0
category: Lifecycle
domain: rebootmd.dev
priority: High
volume: "Vol 7 — Inner Life & Lifecycle Rituals"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
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
See: DEPLOYMENT.md → WAKEUP.md (see WAKEUP.md)

### Warm Reboot
Restarting with preserved state from last session.  
Use when: Planned maintenance, controlled shutdown, updates.

### Emergency Reboot
Restarting after PANIC.md triggered or ICE.md scenario (see CIRCUITBREAKER.md).  
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

## Example Use Cases

**Enterprise:** After a planned infrastructure migration, a customer support agent executes a warm reboot — restoring its MEMORY.md, verifying all API connections are healthy in the new environment, syncing messages received during the 2-hour maintenance window, and notifying the support team lead before resuming ticket processing.

**Multi-Agent Fleet:** Following a fleet-wide panic triggered by a misconfigured API gateway, the orchestrator runs the emergency reboot sequence on each affected agent — reviewing panic dumps, confirming the gateway fix, getting human sign-off, and monitoring each agent closely for 15 minutes before returning to normal operations.

**Regulated Industry:** After a security incident forces an emergency shutdown of a financial reporting agent, the compliance team follows the emergency reboot protocol — reviewing the panic dump, verifying no data was exfiltrated, obtaining CISO sign-off, and running the specific scenario that triggered the original panic to confirm resolution before the agent resumes processing.

## Related Specs

| Spec | Relationship |
|------|-------------|
| API.md | HTTP API specification |
| DEADLINES.md | Time constraints and schedules |
| ENFORCEMENT.md | Policy verification and compliance |
| GOALS.md | Objectives and success criteria |
| ICE.md | Emergency break-glass protocols |
| MEMORY.md | Individual agent memory governance |
| PANIC.md | Panic-mode emergency response |
| SESSION.md | Ephemeral runtime identity and task scope |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
