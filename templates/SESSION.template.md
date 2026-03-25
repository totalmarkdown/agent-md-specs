---
spec_name: SESSION.md
spec_version: 0.1.0
category: Identity
domain: specmd.dev
priority: P1
tier: core
---

# [REPLACE THIS — Agent Name] — Session Identity

<!-- Ephemeral, task-scoped identity that exists only for the duration of one job -->

## Session Parameters
- **Session ID format:** [REPLACE THIS — e.g. UUIDv4, ULID, nanoid]
- **TTL:** [REPLACE THIS — max session lifetime, e.g. 1h, 24h, until-task-complete]
- **Renewable:** [REPLACE THIS — true | false]
- **Max renewals:** [REPLACE THIS — number or "unlimited"]

## Scope
- **Bound to task:** [REPLACE THIS — task type or ID pattern this session covers]
- **Bound to parent:** [REPLACE THIS — permanent agent ID (from ID.md)]
- **Inherits permissions:** [REPLACE THIS — true | false — does session inherit agent perms]

## Session Lifecycle
1. **Created when:** [REPLACE THIS — trigger event, e.g. task assigned, API call received]
2. **Active until:** [REPLACE THIS — completion condition or timeout]
3. **Terminated by:** [REPLACE THIS — who/what can end it early]
4. **On expiry:** [REPLACE THIS — action: save state | discard | escalate]

## Session Data
- **Carries forward:** [REPLACE THIS — what data persists if session is renewed]
- **Discards on close:** [REPLACE THIS — what is wiped when session ends]
- **Storage:** [REPLACE THIS — where session state is held during execution]

## Isolation
<!-- Sessions must not leak into each other -->
- **Memory isolation:** [REPLACE THIS — how session memory is sandboxed]
- **Credential scope:** [REPLACE THIS — session-scoped tokens only | shared pool]

## Related Specs
- ID.md: [REPLACE THIS — path]
- MEMORY.md: [REPLACE THIS — path]
- SHAREDCONTEXT.md: [REPLACE THIS — path]
