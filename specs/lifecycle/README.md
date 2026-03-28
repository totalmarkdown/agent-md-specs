# Lifecycle Specs

Specs for agent lifecycle from first awakening through daily sessions to eventual retirement. These specs define the rituals at each transition point -- what happens when an agent boots for the first time, starts a session, ends a session, recovers from downtime, and is finally decommissioned. Without lifecycle specs, agents have no memory of how they started and no plan for how they end.

## How These Specs Work Together

HELLOWORLD.md fires exactly once in an agent's lifetime -- the very first awakening, before any task or memory exists. After that, every work period follows the WAKEUP.md / SESSION.md / SLEEP.md cycle: WAKEUP.md runs the pre-flight checklist at session start, SESSION.md scopes the ephemeral identity and constraints for the duration of the task, and SLEEP.md commits state and runs the closing routine before the agent goes idle.

REBOOT.md handles the special case of recovery after unexpected or planned downtime -- distinct from a normal wakeup because it must assess what was lost and reconcile state before resuming. At end of life, LEGACY.md governs decommissioning: knowledge transfer, successor designation, and lessons preserved for future agents.

Typical adoption order: WAKEUP.md and SLEEP.md first (every agent needs session boundaries), then SESSION.md for task-scoped identity, then HELLOWORLD.md and REBOOT.md for edge cases, and finally LEGACY.md when the agent nears retirement.

## Specs in This Category

| Spec | Tier | Purpose | Scope |
|------|------|---------|-------|
| HELLOWORLD.md | extended | First-ever awakening and self-introduction (runs once) | Per-agent |
| LEGACY.md | extended | Decommissioning, knowledge transfer, and successor designation | Per-agent |
| REBOOT.md | extended | Restart sequence and recovery after downtime | Per-agent |
| SESSION.md | core | Ephemeral task-scoped identity and lifecycle constraints | Per-session |
| SLEEP.md | extended | End-of-session closing routine and state commit | Per-session |
| WAKEUP.md | core | Start-of-session pre-flight checklist and initialization | Per-session |

## When to Use These Specs

- **Building a new agent:** Start with HELLOWORLD.md for first-run behavior, then WAKEUP.md and SLEEP.md for the daily session cycle.
- **Scoping task execution:** Use SESSION.md to give each job its own ephemeral identity, credentials, and audit trail alongside the agent's permanent identity.
- **Handling unexpected downtime:** Use REBOOT.md to define recovery behavior distinct from normal startup -- assessing lost state before resuming work.
- **Retiring an agent gracefully:** Use LEGACY.md to ensure knowledge is transferred, outputs are archived, and successors are designated before shutdown.

## Related Categories

| Category | How It Relates |
|----------|---------------|
| [identity/](../identity/) | ID.md provides the permanent identity that SESSION.md's ephemeral identity extends per-task |
| [operations/](../operations/) | Operations specs (HEALTHCHECK, MONITOR) keep agents healthy between lifecycle transitions |
| [coordination/](../coordination/) | TEAM and SHAREDCONTEXT define the collaborative context that lifecycle specs initialize and tear down |

---
*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)
· [Full Index](../../INDEX.md) · [README](../../README.md)*
