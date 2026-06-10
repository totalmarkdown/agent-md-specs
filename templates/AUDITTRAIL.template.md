---
spec_name: AUDITTRAIL.md
spec_version: 0.1.0
category: Observability
domain: specmd.dev
priority: P0
tier: core
---

# [REPLACE THIS — Agent Name] — Audit Trail

<!-- Tamper-evident logging of all agent actions for accountability and forensics -->

## What Gets Logged
<!-- Every logged event must include: timestamp, agent_id, action, target, outcome -->

| Event Type | Logged | Detail Level |
|------------|--------|-------------|
| Actions taken | [REPLACE THIS — always | on-error | sampled] | [REPLACE THIS] |
| Decisions made | [REPLACE THIS] | [REPLACE THIS] |
| Resources accessed | [REPLACE THIS] | [REPLACE THIS] |
| Permissions used | [REPLACE THIS] | [REPLACE THIS] |
| Errors encountered | [REPLACE THIS] | [REPLACE THIS] |
| Delegations issued | [REPLACE THIS] | [REPLACE THIS] |

## Log Format
```json
{
  "timestamp": "[REPLACE THIS — ISO 8601]",
  "agent_id": "[REPLACE THIS — UUID]",
  "session_id": "[REPLACE THIS — session UUID]",
  "action": "[REPLACE THIS — verb]",
  "target": "[REPLACE THIS — resource]",
  "outcome": "[REPLACE THIS — success | failure | partial]",
  "metadata": {}
}
```

## Storage
- **Primary store:** [REPLACE THIS — e.g. append-only log, S3, database]
- **Retention period:** [REPLACE THIS — e.g. 90 days, 1 year, indefinite]
- **Tamper protection:** [REPLACE THIS — hash chain | signed entries | WORM storage | none]

## Integrity
- **Hash algorithm:** [REPLACE THIS — SHA-256, BLAKE3, or "none"]
- **Chain verification:** [REPLACE THIS — how to verify the log has not been altered]
- **Backup:** [REPLACE THIS — where backups are stored]

## Access Control
- **Who can read:** [REPLACE THIS — roles or individuals]
- **Who can delete:** [REPLACE THIS — "no one" recommended]
- **Who can export:** [REPLACE THIS — roles or individuals]

## Related Specs
- PROVENANCE.md: [REPLACE THIS — path]
- ENFORCEMENT.md: [REPLACE THIS — path]
- PERMISSIONS.md: [REPLACE THIS — path]
