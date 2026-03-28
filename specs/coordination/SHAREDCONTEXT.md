---
spec_name: SHAREDCONTEXT.md
spec_version: 0.1.0
category: Coordination
domain: sharedcontextmd.dev
priority: Very High
volume: "Vol 15 — Shared Context & Memory Governance"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
---

# SHAREDCONTEXT.md

**Category:** Coordination
**Domain:** sharedcontextmd.dev
**Priority:** Very High
**Version:** 0.1.0

### Purpose
Defines the shared memory and context pool that multiple agents read
from and write to within a team, crew, swarm, or organization. This
is the governance layer for persistent shared state in multi-agent
systems — addressing how context is structured, who can access it,
how long entries persist, and how shared memory inherits across
organizational hierarchy levels.

When agents collaborate on a shared objective, they produce
intermediate conclusions, observations, and decisions that subsequent
agents depend on. Without a governed shared context pool, these
artifacts live in ad-hoc message passing, unstructured logs, or
individual agent memory — leading to stale references, conflicting
facts, and untraceable reasoning chains. SHAREDCONTEXT.md establishes
the canonical shared state layer: schema-enforced, access-controlled,
time-bounded, and auditable.

This spec directly addresses **OWASP ASI06 (Memory Poisoning)**
prevention through access control, schema enforcement, and
provenance tracking. An agent cannot inject a malicious "fact" into
the shared pool without a valid delegation chain, a conforming
schema entry, and an immutable provenance record. It maps to
**NIST SP 800-53 AC (Access Control)** and **AU (Audit and
Accountability)** control families as applied to multi-agent
shared state.

### Scope Boundary

This spec governs **the shared memory pool itself** — its structure,
access rules, lifecycle, synchronization, and inheritance across
organizational levels.

- SHAREDCONTEXT.md defines **the pool structure and governance** (what the pool is)
- MEMORYSAFETY.md defines **security controls for memory** (protecting the pool)
- MEMORY.md defines **individual agent memory** (private to one agent)
- SESSION.md defines **ephemeral runtime state** (per-session, not persistent)
- DELEGATION.md defines **who authorized an agent to write** (authority chain)
- SHARE.md defines **resource sharing mechanics** (broader than memory)

The shared context pool is not a message bus. It is a persistent,
structured state store. Ephemeral inter-agent communication (requests,
responses, task handoffs) belongs in PROTOCOL.md and HANDSHAKE.md.
The shared context pool stores durable artifacts that outlive
individual conversations and sessions.

### When to Create This File
Required for any multi-agent system where agents need to share
persistent state beyond simple request-response messaging. Critical
in teams, crews, and swarms where later agents build on earlier
conclusions or where parallel agents must avoid contradicting each
other. Mandatory when:

- Two or more agents operate on the same task or domain
- Agent conclusions feed into other agents' reasoning
- Decisions must be traceable across agent boundaries
- Organizational hierarchy requires context inheritance
- Compliance requires demonstrating what shared state an agent
  relied on when making a decision

### Spec

````markdown
---
agent_name: string                  # Agent or team name owning this pool
version: semver
pool_id: uuid                       # Unique identifier for this context pool
pool_name: string                   # Human-readable pool name
created: datetime                   # ISO-8601
updated: datetime                   # ISO-8601
pool_status: active | frozen | archived | draining
---

# [Pool Name] — Shared Context Pool

## Shared Context Pool

| Field | Value |
|-------|-------|
| Pool ID | [UUID] |
| Scope | [team \| crew \| swarm \| org \| global] |
| Scope Reference | [path to TEAM.md / CREW.md / SWARM.md / ORG.md] |
| Owner | [agent or human principal responsible for pool governance] |
| Created | [ISO-8601] |
| Max Participants | [number or unlimited] |
| Current Participants | [number] |
| Storage Backend | [in-memory \| file \| database \| vector-store] |
| Encryption at Rest | [yes \| no — if yes, reference SECRETS.md] |

### Pool Hierarchy Position
This pool exists at the **[scope]** level. It inherits from the
pool above it in the organizational hierarchy (see ORG.md for how
organizational levels are defined) and may propagate entries
downward to child pools, subject to inheritance rules defined below.

### Pool Lifecycle States
- **active:** Normal read/write operations permitted
- **frozen:** Read-only — no new entries, used during audits or migrations
- **archived:** Pool contents moved to cold storage, no runtime access
- **draining:** Pool is being decommissioned — reads allowed, writes blocked,
  entries migrating to successor pool

## Access Control Matrix

Access to the shared context pool is governed by agent identity
(WHOAMI.md) and delegated authority (see DELEGATION.md for the
full authority chain and delegation mechanics). Every access
grant must be justified by a valid delegation chain — an agent
cannot self-grant pool access.

| Agent | Read | Write | Delete | Admin | Delegation Ref |
|-------|------|-------|--------|-------|----------------|
| [agent-uuid-1] | yes | yes | no | no | DELEGATION.md#del-001 |
| [agent-uuid-2] | yes | yes | yes | no | DELEGATION.md#del-002 |
| [agent-uuid-3] | yes | no | no | no | DELEGATION.md#del-003 |
| [orchestrator-uuid] | yes | yes | yes | yes | DELEGATION.md#del-000 |

### Access Control Rules

1. **Read access** is the minimum grant. An agent with pool
   membership always has read access.
2. **Write access** requires explicit delegation (see DELEGATION.md
   for delegation authority requirements). The delegating
   principal must have write or admin access themselves.
3. **Delete access** is restricted to pool administrators and
   agents with explicit delete delegation. Soft-delete is
   preferred — entries are marked `superseded` rather than removed.
4. **Admin access** permits modifying pool configuration, access
   control entries, and retention policies. Reserved for
   orchestrators and human principals.
5. **No implicit access.** Being a member of the parent
   organization does not automatically grant pool access. Access
   must be explicitly granted per-agent or per-role.
6. **Classification ceiling.** An agent's maximum readable
   classification level is the lower of: (a) the agent's own
   clearance in PERMISSIONS.md, and (b) the pool-level
   classification ceiling.

### Access Audit
Every pool access (read, write, delete) is logged with:
- Agent UUID (from WHOAMI.md)
- Timestamp (ISO-8601)
- Action type (read / write / delete / admin)
- Entry ID(s) affected
- Delegation ID authorizing the action

## Memory Schema

All entries in the shared context pool conform to this schema.
Non-conforming entries are rejected at write time.

```yaml
memory_schema:
  entry_id:
    type: uuid
    required: true
    description: "Globally unique identifier for this entry"

  source_agent:
    type: string
    required: true
    ref: WHOAMI.md
    description: "UUID of the agent that created this entry"

  timestamp:
    type: datetime
    format: iso8601
    required: true
    description: "When this entry was written to the pool"

  entry_type:
    type: enum
    values:
      - fact            # Verified or high-confidence assertion
      - observation     # Agent perception, not independently verified
      - decision        # Explicit decision with rationale
      - instruction     # Directive from orchestrator or principal
      - alert           # Time-sensitive warning or notification
    required: true
    description: "Classification of entry content"

  confidence:
    type: float
    range: [0.0, 1.0]
    required: true
    description: >
      Agent's confidence in the entry. Facts should be >= 0.8.
      Observations may be lower. Decisions inherit the confidence
      of their supporting evidence.

  classification:
    type: enum
    values:
      - public          # No access restriction
      - internal        # Pool members only
      - confidential    # Explicit read grant required
      - restricted      # Admin + named agents only
    required: true
    default: internal
    description: "Data sensitivity classification"

  ttl:
    type: duration
    format: ISO-8601 duration (e.g., P30D, PT24H)
    required: false
    description: >
      Time-to-live. If omitted, the default TTL for the entry_type
      applies per the retention policy.

  content:
    type: string
    max_length: 32768
    required: true
    description: "The actual context entry content"

  provenance:
    type: object
    required: true
    ref: PROVENANCE.md    # See PROVENANCE.md — every entry tracks provenance
    properties:
      source_type:
        type: enum
        values: [direct_observation, inference, delegation, external_api, human_input, aggregation]
      source_refs:
        type: array
        items: string
        description: "References to source data, prior entries, or external URLs"
      reasoning:
        type: string
        description: "Brief explanation of how this entry was derived"

  supersedes:
    type: uuid | null
    required: false
    default: null
    description: >
      If this entry replaces a prior entry, reference that entry's
      ID here. The superseded entry is marked stale but retained
      for audit purposes.

  tags:
    type: array
    items: string
    required: false
    description: "Freeform tags for filtering and retrieval"
```

### Schema Enforcement
- Schema validation occurs at write time — non-conforming entries
  are rejected with a structured error
- Schema version is tracked; pool entries include the schema
  version they were validated against
- Schema migrations require admin access and are logged to
  AUDITTRAIL.md

## Retention Policy

Entries in the shared context pool have bounded lifetimes to
prevent unbounded growth, stale data accumulation, and context
window pollution.

### Default TTL by Entry Type

| Entry Type | Default TTL | Rationale |
|-----------|-------------|-----------|
| fact | 30 days (P30D) | Facts remain useful but should be periodically revalidated |
| observation | 7 days (P7D) | Observations decay in relevance quickly |
| decision | Permanent | Decisions are part of the audit record and never expire |
| instruction | Until superseded | Instructions remain active until explicitly replaced |
| alert | 24 hours (PT24H) | Alerts are ephemeral by nature |

### Pool Size Limits

| Constraint | Value |
|-----------|-------|
| Max active entries | [10000] |
| Max entry size | 32 KB |
| Max pool storage | [500 MB] |
| Warning threshold | 80% of max active entries |
| Critical threshold | 95% of max active entries |

### Eviction Strategy

| Strategy | Behavior |
|----------|----------|
| `ttl_expiry` (default) | Entries removed when TTL expires |
| `lru` (fallback) | Least-recently-read entries evicted when pool is at capacity |
| `confidence_weighted` | Low-confidence entries evicted first during capacity pressure |
| `classification_preserve` | Higher classification entries retained longer during eviction |

Eviction order when pool reaches capacity
(see AUDITTRAIL.md — all evictions are logged for audit purposes):
1. Expired entries (TTL exceeded) — always evicted first
2. Superseded entries older than 7 days
3. Low-confidence observations (confidence < 0.3)
4. LRU among remaining entries at lowest classification

### Archive Policy
- Evicted entries with `classification >= confidential` are
  archived rather than deleted
- Archived entries are written to cold storage with full
  provenance intact
- Archive retention: [1 year] or per regulatory requirement
- Decisions are always archived, never deleted

## Inheritance Rules

Shared context pools form a hierarchy that mirrors the
organizational structure (see ORG.md and INHERIT.md for how
organizational hierarchy and inheritance rules are defined).
Higher-level pools can propagate entries downward; lower-level
pools can promote entries upward.

### Hierarchy

```
┌─────────────────────────────────────┐
│           ORG POOL                  │
│   (org-wide facts, policies,       │
│    strategic decisions)             │
│         ref: ORG.md                 │
└──────────────┬──────────────────────┘
               │ inherits down
        ┌──────┴──────┐
        ▼             ▼
┌───────────────┐ ┌───────────────┐
│  SWARM POOL   │ │  SWARM POOL   │
│  (mission-    │ │  (mission-    │
│   scoped)     │ │   scoped)     │
│  ref: SWARM.md│ │  ref: SWARM.md│
└──────┬────────┘ └───────────────┘
       │ inherits down
  ┌────┴────┐
  ▼         ▼
┌────────┐ ┌────────┐
│ CREW   │ │ CREW   │
│ POOL   │ │ POOL   │
│ref:    │ │ref:    │
│CREW.md │ │CREW.md │
└───┬────┘ └────────┘
    │ inherits down
    ▼
┌────────┐
│ TEAM   │
│ POOL   │
│ref:    │
│TEAM.md │
└────────┘
```

### Inheritance Behavior

| Rule | Default | Override Allowed |
|------|---------|-----------------|
| Parent entries visible to children | Yes | No — visibility always inherits down |
| Child entries visible to parent | No | Yes — via explicit promotion |
| Override parent entries in child pool | No | Yes — requires admin + justification |
| Classification ceiling inherited | Yes | No — child cannot exceed parent ceiling |
| Retention policy inherited | Yes | Yes — child can set stricter (not looser) |

### Conflict Resolution
When an entry in a child pool conflicts with an entry in a
parent pool (same subject, different content):

| Resolution Strategy | When Used |
|--------------------|-----------|
| `timestamp` | Most recent entry wins (default for observations) |
| `confidence` | Highest confidence entry wins (default for facts) |
| `delegation_authority` | Entry from higher-authority agent wins (default for decisions) |
| `manual` | Conflict flagged for human resolution (default for instructions) |

Conflict detection runs at sync time. Detected conflicts are
logged as alert-type entries in both pools until resolved.

### Entry Promotion
A child pool entry can be promoted to a parent pool when:
1. The promoting agent has write access to the parent pool
2. The entry confidence meets the parent pool's minimum threshold
3. The entry classification does not exceed the parent pool's ceiling
4. The promotion is logged in both pools with full provenance

## Synchronization

In distributed deployments, shared context pools may have
replicas or may sync across network boundaries.
_See MEMORYSAFETY.md for integrity verification of synchronized entries._

### Sync Configuration

| Field | Value |
|-------|-------|
| Sync frequency | [real-time \| interval: PT5M \| on-demand] |
| Consistency model | [eventual \| strong \| causal] |
| Conflict handling | [last-write-wins \| merge \| flag-for-review] |
| Sync transport | [direct \| message-queue \| API] |
| Sync authentication | [mTLS \| API key ref in SECRETS.md \| delegation token] |

### Consistency Guarantees

- **Eventual consistency (default):** Entries propagate within
  the sync interval. Agents may briefly read stale state. Suitable
  for observations and facts.
- **Strong consistency:** All agents see the same pool state at
  all times. Required for instructions and high-stakes decisions.
  Higher latency cost.
- **Causal consistency:** If agent A writes entry X and then
  reads entry Y, any agent that reads Y will also see X. Preserves
  reasoning chains without full strong consistency overhead.

### Conflict Handling at Sync

| Conflict Type | Resolution |
|--------------|------------|
| Concurrent writes, same entry_id | Rejected — entry_id is a UUID, collisions indicate a bug |
| Concurrent supersedes of same entry | Both retained, conflict alert raised |
| TTL disagreement across replicas | Shortest TTL wins (fail-safe) |
| Classification escalation | Highest classification wins (fail-safe) |
| Schema version mismatch | Sync blocked until schema aligned |

### Sync Failure Protocol
1. Sync failure logged with error details
2. Pool enters `degraded` state — local reads continue, writes
   are queued
3. Retry with exponential backoff (max 5 retries)
4. After max retries: alert raised per ESCALATION.md Level 2
5. Manual intervention required to reconcile diverged state

## Integration with Individual Memory

Each agent maintains its own MEMORY.md (individual memory) alongside
access to the shared context pool. This section governs the boundary
between private and shared memory.

### Sync Direction

| Direction | Mechanism | Governance |
|-----------|-----------|------------|
| Shared → Individual | Auto-load on session start | Entries matching agent's role/tags loaded into SESSION.md context |
| Individual → Shared | Explicit promotion | Agent writes to pool via governed write path |
| Shared → Individual archive | On pool eviction | Agent retains a private copy if entry was material to its decisions |

### What Is Eligible for Promotion
Individual memory entries may be promoted to the shared pool when:

1. **Relevance:** The entry is relevant to other agents in the pool scope
2. **Confidence:** Entry confidence meets pool minimum (default: 0.5)
3. **Classification:** Entry classification is within pool ceiling
4. **Non-duplication:** No existing pool entry covers the same ground
   (checked via semantic or exact match)
5. **Provenance:** Entry has complete provenance chain

Agents SHOULD NOT promote:
- Internal reasoning traces (use JOURNAL.md for that)
- Speculative hypotheses below confidence 0.3
- Entries derived solely from other shared pool entries (circular)
- Personal preferences or agent-specific configuration

### Auto-Load on Session Start
When an agent begins a new session (per SESSION.md), the following
shared context entries are automatically loaded:

1. All `instruction` entries currently active in the pool
2. All `decision` entries from the current task scope
3. `fact` entries tagged with the agent's role or domain
4. `alert` entries younger than their TTL
5. Up to [50] most recent `observation` entries (sorted by
   confidence, then recency)

Auto-loaded entries count against the agent's context window budget.
If the total exceeds the session context limit, entries are
prioritized: instructions > decisions > alerts > facts > observations.

### Write-Back on Session End
When an agent's session concludes:
1. Agent reviews its new individual memory entries
2. Entries meeting promotion criteria are written to the shared pool
3. Write-back is atomic — all entries or none
4. Write-back failures are retried once, then logged for manual review
5. Session-only ephemeral state is discarded per SESSION.md
````

## Example Use Cases

**Enterprise:** A global supply-chain management system uses SHAREDCONTEXT.md to maintain a shared pool where procurement agents write verified supplier facts, logistics agents post shipping observations, and planning agents read both to make inventory decisions -- all with causal consistency guarantees and 30-day fact TTLs.

**Multi-Agent Fleet:** A research platform's 20 literature-review agents share a context pool governed by SHAREDCONTEXT.md, where high-confidence findings are promoted from crew-level pools to the org-level pool using schema-enforced provenance tracking, preventing duplicate discoveries and enabling cross-domain insight aggregation.

**Regulated Industry:** A banking compliance fleet uses SHAREDCONTEXT.md with strict access controls and classification ceilings so that transaction-monitoring agents can write "alert" entries visible to investigation agents, while client-confidential data remains restricted to authorized agents with documented delegation chains.

## Related Specs

| Spec | Relationship |
|------|-------------|
| TEAM.md | Multi-agent team coordination |
| CREW.md | Working group structure |
| SWARM.md | Large operation structure |
| ORG.md | Organization-wide fleet configuration |
| MEMORY.md | Individual agent memory governance |
| MEMORYSAFETY.md | Memory poisoning defense |
| DELEGATION.md | Authority chain and authorization |
| PERMISSIONS.md | Static resource access control |
| PROVENANCE.md | Data lineage and trust classification |
| SESSION.md | Ephemeral runtime identity and task scope |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
