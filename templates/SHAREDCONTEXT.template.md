---
spec_name: SHAREDCONTEXT.md
spec_version: 0.1.0
category: Coordination
priority: Very High
tier: core
---

# [REPLACE THIS — Team or System Name] — Shared Context

<!-- Multi-agent shared memory: how agents read and write to a common knowledge space -->

## Context Store
- **Backend:** [REPLACE THIS — Redis | PostgreSQL | file system | in-memory]
- **Location:** [REPLACE THIS — connection string or path]
- **Schema version:** [REPLACE THIS — version of the shared context schema]

## Namespaces
<!-- Logical partitions within shared context -->

| Namespace | Purpose | Read By | Write By |
|-----------|---------|---------|----------|
| [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS — agent IDs] | [REPLACE THIS — agent IDs] |
| [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |

## Data Format
- **Encoding:** [REPLACE THIS — JSON | MessagePack | plain text]
- **Max entry size:** [REPLACE THIS — e.g. 64KB]
- **TTL per entry:** [REPLACE THIS — e.g. 1h, session-scoped, permanent]

## Concurrency
- **Conflict resolution:** [REPLACE THIS — last-write-wins | optimistic locking | CRDT]
- **Locking:** [REPLACE THIS — advisory locks | mutex | none]
- **Consistency model:** [REPLACE THIS — eventual | strong | causal]

## Access Rules
- **Read access:** [REPLACE THIS — which agents can read shared context]
- **Write access:** [REPLACE THIS — which agents can write]
- **Admin access:** [REPLACE THIS — who can clear or restructure context]

## Lifecycle
- **Created when:** [REPLACE THIS — e.g. team session starts]
- **Cleared when:** [REPLACE THIS — e.g. team task completes]
- **Archived:** [REPLACE THIS — true | false — is context saved after clearing]

## Related Specs
- MEMORY.md: [REPLACE THIS — path]
- MEMORYSAFETY.md: [REPLACE THIS — path]
- TEAM.md: [REPLACE THIS — path]
