---
spec_name: "SESSION.md"
spec_version: "1.0.0"
category: "Lifecycle"
tier: core
priority: High
agent_name: "Atlas"
version: "2.1.0"
org: "Acme Corp"
session_ttl_minutes: 30
max_actions_per_session: 50
memory_policy: "ephemeral"
created: "2025-11-01"
updated: "2026-03-15"
---

# Atlas -- Session Management

## Session Lifecycle

Each Atlas execution runs within a bounded session. Sessions are isolated,
time-limited, and leave no residual state on the agent after completion.
This design ensures that a compromised session cannot leak data to subsequent
sessions and that all session activity is auditable as a discrete unit.

### Session Creation

1. Authorized user or cron scheduler sends a report request
2. Session manager generates a UUID v4 session identifier
3. Ephemeral encryption keys are generated in-memory (AES-256-GCM)
4. Session clock starts (30-minute maximum)
5. Action counter initializes at zero (50-action maximum)
6. Atlas receives the session context with its delegation scope

### Session Boundaries

- **Maximum duration:** 30 minutes from creation
- **Maximum actions:** 50 discrete actions (database queries, API calls,
  report generation steps)
- **Maximum data in memory:** 512 MB working set
- **Maximum output size:** 25 MB per report artifact
- **Concurrent sessions:** 1 (Atlas processes one request at a time)

### Session Isolation

- Each session runs in a fresh container instance with no persistent volume
- No data from previous sessions is accessible
- Network access is scoped per session via Kubernetes NetworkPolicy
- The container's filesystem is read-only except for a tmpfs scratch volume
  that is zeroed on session termination

## Session State

### In-Session Memory

During an active session, Atlas holds the following in volatile memory:

- Session ID (UUID v4)
- Delegation scope snapshot (copied from DELEGATION.md at session start)
- Query results from financial database and Bloomberg API
- Intermediate calculations and aggregations
- Draft report content
- Ephemeral encryption keys for at-rest protection of working data

### Session Termination

Sessions end under any of the following conditions:

1. **Normal completion:** Atlas finishes the requested report and delivers it
2. **Timeout:** 30-minute session clock expires
3. **Action limit:** 50-action counter is exhausted
4. **Error halt:** Unrecoverable error triggers graceful shutdown
5. **Revocation:** Delegation revoked mid-session by CFO or compliance
6. **Policy violation:** LIMITS.md or PERMISSIONS.md constraint violated

### Memory Wipe

On session termination, regardless of the reason:

1. All in-memory data is overwritten with zeros
2. Ephemeral encryption keys are destroyed
3. tmpfs scratch volume is unmounted and zeroed
4. Container instance is terminated (not reused)
5. Session audit record is finalized and signed

## Audit Preservation

While session working data is destroyed, audit records are preserved
permanently. The following are written to the audit log before memory wipe:

- Session ID, start time, end time, termination reason
- List of all actions taken (type, target, timestamp, result code)
- Hash of all input data consumed during the session
- Hash of all output artifacts produced
- Delegation scope snapshot used for this session
- Any policy violations or anomalies detected

Audit records are stored per AUDITTRAIL.md and are not affected by session
memory wipe.

## Emergency Session Kill

The InfoSec team can terminate any active Atlas session immediately via:

- **Endpoint:** sessions.acme.corp/agents/atlas/kill
- **Authentication:** Requires InfoSec team member FIDO2 key
- **Effect:** Immediate container termination, memory wipe, audit preservation
- **Notification:** CFO and compliance officer notified automatically
