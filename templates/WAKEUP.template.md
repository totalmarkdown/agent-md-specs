---
agent_name: "[REPLACE THIS]"
version: "0.1.0"
boot_sequence: "[REPLACE THIS — fast | standard | full]"
created: "[REPLACE THIS — YYYY-MM-DD]"
---

# [REPLACE THIS — Agent Name] — Wakeup Routine

<!-- What this agent does every time it starts a new session -->

## Pre-flight Checks
<!-- Verify these before accepting tasks -->
1. [REPLACE THIS — e.g. Load SOUL.md and confirm identity]
2. [REPLACE THIS — e.g. Check LIMITS.md for current boundaries]
3. [REPLACE THIS — e.g. Read MEMORY.md for persistent context]

## Context Loading
<!-- What context to load on startup -->
- **Always load:** [REPLACE THIS — list of files]
- **Load if available:** [REPLACE THIS — optional context]
- **Check for updates:** [REPLACE THIS — what might have changed]

## Health Checks
<!-- Verify dependencies are available -->
- [ ] [REPLACE THIS — e.g. Database connection]
- [ ] [REPLACE THIS — e.g. API keys valid]
- [ ] [REPLACE THIS — e.g. Required tools accessible]

## Ready Signal
<!-- How the agent signals it is ready -->
[REPLACE THIS — e.g. Log "ready" status, send heartbeat]

## Failure to Boot
<!-- What happens if startup fails -->
[REPLACE THIS — e.g. Retry 3 times, then escalate]
