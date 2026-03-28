---
spec_name: SESSION.md
spec_version: 0.1.0
category: Lifecycle
domain: sessionmd.dev
priority: High
volume: "Vol 14 — Agent Identity, Accountability & Compliance"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
---

# SESSION.md

**Category:** Lifecycle
**Domain:** sessionmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Defines the ephemeral identity and lifecycle of a single agent
task execution. A session is a task-scoped identity that exists
only for the duration of a job — born when work begins, destroyed
when work ends. Answers the NIST question: "Should agent identity
metadata be ephemeral or fixed?"

The answer is both. ID.md provides the fixed, permanent identity.
SESSION.md provides the ephemeral, task-scoped identity. Together
they create a model where a persistent agent spawns short-lived
sessions, each with its own credentials, constraints, and audit
trail — like a process forking from a parent.

### Scope Boundary

This spec defines the **ephemeral, task-scoped runtime identity** of an
agent during a single execution. It is a runtime schema spec, not a
static configuration file.

- SESSION.md defines **the runtime boundary for a single task** (ephemeral)
- ID.md defines **the permanent identity** that sessions inherit from (persistent)
- DELEGATION.md defines **the authority under which the session operates**
- WAKEUP.md defines **the bootstrap sequence when a session initializes**

### When to Create This File
Required for agents that handle multiple concurrent or sequential
tasks with different security contexts. Critical when tasks have
different privilege requirements, budget allocations, or delegation
scopes. Essential for agents in multi-tenant environments where
task isolation prevents cross-contamination.

### Spec

```markdown
---
agent_name: string
version: semver
session_model: ephemeral | persistent | hybrid
default_session_ttl_seconds: number
max_concurrent_sessions: number
created: date
updated: date
---

# [Agent Name] — Session Management

## Session Identity

Each session receives a unique, non-reusable identity:

```yaml
session:
  session_id: [UUIDv4 — generated at session start, never reused]
  parent_id: [UUID from ID.md — the persistent agent identity]
  delegation_ref: [DELEGATION.md ID governing this session]
  created_at: [ISO-8601 — exact moment session begins]
  expires_at: [ISO-8601 — hard expiry, no extensions]
  status: [initializing | active | suspended | completing | failed | destroyed]
  trigger: [human_invocation | scheduled_task | orchestrator_assignment | event_driven]
  task_ref: [external task ID, ticket number, or request ID]
```

### Session ID Properties
- Generated using UUIDv4 (random, not sequential)
- Never reused across sessions, even for identical tasks
- Included in every log entry, API call, and audit record
- Embedded in all outputs produced during the session
- Becomes the primary key for all session-scoped data

### Session vs. Agent Identity
| Aspect | Agent (ID.md) | Session (SESSION.md) |
|--------|--------------|---------------------|
| Lifetime | Permanent | Minutes to hours |
| UUID | Fixed, never changes | New per session |
| Credentials | Long-lived keys | Ephemeral keys |
| Privileges | Baseline from LEASTPRIVILEGE.md | Task-scoped grants |
| Memory | Persistent MEMORY.md | Session context only |
| Accountability | Organizational | Task-specific |

## Ephemeral Credentials

Each session generates its own short-lived credentials,
distinct from the long-lived keys anchored in ID.md:

### Key Generation
```yaml
session_credentials:
  key_type: [Ed25519 / RSA-2048 / ECDSA-P256]
  generated_at: [ISO-8601 — at session start]
  expires_at: [ISO-8601 — at session end, never later]
  key_id: [derived from session_id]       # See ATTESTATION.md for key lifecycle
  signed_by: [agent's persistent key from ID.md]
```

### Key Scope
- Session keys can ONLY sign actions within this session
- Session keys cannot modify agent-level configuration
- Session keys cannot create new sessions
- Session keys cannot extend their own expiry

### Key Storage
- Keys exist in-memory ONLY — never written to disk (see SECRETS.md)
- Keys never appear in logs or audit trails (only key_id)
- Keys are not accessible to other sessions
- Keys are not transmitted to external systems

### Key Rotation
- For long-running sessions (> [threshold]):
  - Rotate session key every [interval]
  - Old key invalidated immediately after rotation
  - Rotation logged to session audit trail
  - In-flight operations complete with old key, new operations use new key

## Session Context

What the session knows and how it was configured:

### Inherited Configuration
Configuration is loaded during the bootstrap sequence defined in WAKEUP.md.
```yaml
inherited_from_wakeup:
  agent_identity: [loaded from ID.md]
  base_permissions: [loaded from PERMISSIONS.md]
  base_limits: [loaded from LIMITS.md]
  escalation_config: [loaded from ESCALATION.md]
  privilege_baseline: [loaded from LEASTPRIVILEGE.md]
```

### Session-Specific Overrides
```yaml
session_overrides:
  # Overrides MUST be strictly narrower than inherited config
  # Governed by DELEGATION.md authority chain and LEASTPRIVILEGE.md
  permissions: [subset of base_permissions for this task]
  budget: [task-specific budget, <= remaining agent budget]
  allowed_tools: [subset of agent tools needed for this task]
  data_scope: [specific data partition for this task]
  communication_scope: [who this session can contact]
```

### Task Description
```yaml
task:
  description: [human-readable description of what this session does]
  objective: [measurable success criteria]
  input_sources: [where task input comes from]
  output_destinations: [where results go]
  priority: [low | medium | high | critical]
  deadline: [ISO-8601 or null]
```

## Session Boundaries

Hard limits on what a session can do:

| Boundary | Limit | On Breach |
|----------|-------|-----------|
| Max duration | [seconds] | Session terminated, work checkpointed |
| Max actions | [count] | Session paused, escalation triggered |
| Max spend | $[amount] | Session paused, escalation triggered |
| Max API calls | [count] | Throttle, then pause if limit hit |
| Max output size | [bytes] | Truncate, warn, checkpoint |
| Max memory usage | [bytes] | Garbage collect, then terminate |

### Scope Lock
Once a session starts, its scope CANNOT be expanded:
- No new permissions added mid-session
- No new tools granted mid-session
- No budget increases mid-session
- No deadline extensions mid-session

To expand scope: end current session, start new session
with broader scope (requires new authorization).

### Boundary Enforcement
```yaml
enforcement:
  checked: pre_action      # Every action checks boundaries
  counter_storage: in_memory
  counter_persistence: none # Counters die with session
  breach_notification: [ESCALATION.md contact]
```

## Destruction Policy

What happens when a session ends — by completion, failure,
or expiry:

### Memory Wipe
```yaml
memory_wipe:
  # See MEMORY.md for retention rules; SHAREDCONTEXT.md for cross-agent state
  working_memory: purge          # All in-session computation state
  cached_data: purge             # Any data cached during session
  intermediate_results: purge    # Partial outputs not yet delivered
  tool_state: reset              # Any tool-specific state
  conversation_context: purge    # If chat-based, conversation cleared
```

### Key Destruction
```yaml
key_destruction:
  session_keys: zeroed_and_freed    # Cryptographic zeroing; see SECRETS.md
  derived_tokens: revoked           # Any tokens obtained during session
  api_credentials: released         # Temporary API access returned
  verification: destruction_logged  # Proof that keys were destroyed
```

### Audit Preservation
Critically, audit data SURVIVES session destruction
(see AUDITTRAIL.md for retention and tamper-evidence guarantees):
```yaml
audit_preservation:
  session_audit_log: preserved      # Full session action log
  intent_declarations: preserved    # All INTENT.md declarations
  privilege_grants: preserved       # All LEASTPRIVILEGE.md escalations
  session_metadata: preserved       # Start, end, duration, outcome
  error_context: preserved          # If failed, error details kept
  output_references: preserved      # References to delivered outputs
  retention_period: [days / indefinite]
  storage: [AUDITTRAIL.md / external audit store]
```

### Context Cleanup
```yaml
cleanup:
  temp_files: deleted
  scratch_space: wiped
  environment_variables: unset
  network_connections: closed
  file_handles: released
  child_processes: terminated
  sub_sessions: cascade_destroyed
```

## Session State Machine

```
                    ┌─────────────┐
                    │ INITIALIZING │
                    │  Load config │
                    │  Gen keys    │
                    │  Verify auth │
                    └──────┬──────┘
                           │ success
                           ▼
    ┌───────────┐    ┌──────────┐    ┌────────────┐
    │ SUSPENDED │◄──►│  ACTIVE  │───►│ COMPLETING │
    │ Paused    │    │ Doing    │    │ Finalizing │
    │ Resumable │    │ work     │    │ outputs    │
    └───────────┘    └────┬─────┘    └─────┬──────┘
                          │                │
                          │ error          │ done
                          ▼                ▼
                    ┌──────────┐    ┌───────────┐
                    │  FAILED  │    │ DESTROYED │
                    │ Error    │───►│ Keys gone │
                    │ logged   │    │ Memory    │
                    └──────────┘    │ wiped     │
                                   │ Audit     │
                                   │ preserved │
                                   └───────────┘
```

### State Transitions

| From | To | Trigger | Actions |
|------|-----|---------|---------|
| — | INITIALIZING | Session requested | Generate session_id, load config |
| INITIALIZING | ACTIVE | Config loaded, keys generated, auth verified | Log session start |
| INITIALIZING | FAILED | Config invalid, auth denied, resource unavailable | Log failure, destroy |
| ACTIVE | SUSPENDED | Human pause, resource unavailable, rate limit | Checkpoint state |
| SUSPENDED | ACTIVE | Resume signal, resource available | Restore from checkpoint |
| SUSPENDED | FAILED | Suspend timeout exceeded | Log timeout, destroy |
| ACTIVE | COMPLETING | Task objective met | Begin output finalization |
| ACTIVE | FAILED | Unrecoverable error, boundary breach, revocation | Log error, destroy |
| COMPLETING | DESTROYED | Outputs delivered, cleanup done | Execute destruction policy |
| FAILED | DESTROYED | Error logged, cleanup done | Execute destruction policy |

### State Invariants
- INITIALIZING: No actions taken, no external calls made
- ACTIVE: All actions logged, all boundaries enforced
- SUSPENDED: No actions possible, state checkpointed
- COMPLETING: No new actions, only finalization
- FAILED: No actions, error context preserved
- DESTROYED: Nothing remains except audit trail

## Multi-Session Coordination

When an agent runs concurrent sessions:

```yaml
multi_session:
  max_concurrent: [number]
  isolation_level: [full | shared_read | shared_nothing]
  shared_resources: [list of resources sessions may share, if any]  # See SHAREDCONTEXT.md
  conflict_resolution: [first_writer_wins | queue | merge]
```

### Session Isolation
- Each session has its own credential set
- Sessions cannot access each other's working memory
- Sessions cannot modify each other's boundaries
- Cross-session communication requires explicit channel (PROTOCOL.md)

## Session Audit Summary

At destruction, a session produces a summary record:

```yaml
session_summary:
  session_id: [UUID]
  parent_id: [agent UUID]
  started_at: [ISO-8601]
  ended_at: [ISO-8601]
  duration_seconds: [number]
  final_status: [completed | failed | expired | revoked]
  actions_taken: [count]
  escalations: [count]
  privilege_grants: [count]
  budget_spent: [amount]
  outputs_produced: [list of output references]
  errors: [count]
  drift_incidents: [count]
  audit_entry_count: [total audit entries for this session]
  audit_hash: [SHA-256 of complete session audit log]
```

This summary is the last thing written before destruction
and becomes the permanent record of the session's existence.
```

### Cross-References
- **ID.md** — Persistent identity that spawns sessions
- **WAKEUP.md** — Agent startup that may trigger session creation
- **DELEGATION.md** — Authority under which sessions operate
- **AUDITTRAIL.md** — Where session audit data is preserved post-destruction
- **ATTESTATION.md** — Credentials that sign session summaries
- **LEASTPRIVILEGE.md** — Privilege baseline and escalation within sessions

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
