---
spec_name: LEASTPRIVILEGE.md
spec_version: 0.1.0
category: Security
domain: specmd.dev
priority: P0
tier: core
---

# [REPLACE THIS — Agent Name] — Least Privilege Policy

<!-- Zero-trust privilege management: agent gets only what it needs, when it needs it -->

## Default Posture
- **Default access:** deny-all
- **Privilege model:** [REPLACE THIS — RBAC | ABAC | capability-based]
- **Elevation requires:** [REPLACE THIS — human approval | policy engine | self-certify]

## Granted Privileges
<!-- Each privilege should have a justification -->

| Privilege | Scope | Justification | Expires |
|-----------|-------|---------------|---------|
| [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |
| [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |
| [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |

## Temporary Elevation
- **Request method:** [REPLACE THIS — how agent requests elevated privileges]
- **Approval flow:** [REPLACE THIS — who approves and how]
- **Max elevation duration:** [REPLACE THIS — e.g. 15m, 1h, task-scoped]
- **Auto-revoke:** [REPLACE THIS — true | false]

## Privilege Review
- **Review frequency:** [REPLACE THIS — e.g. weekly, monthly, per-deployment]
- **Reviewed by:** [REPLACE THIS — person or automated system]
- **Unused privileges:** [REPLACE THIS — auto-revoke after N days | flag for review]

## Forbidden Actions
<!-- Things this agent must never have access to, even temporarily -->
- [REPLACE THIS — e.g. production database write access]
- [REPLACE THIS — e.g. billing API]
- [REPLACE THIS — e.g. other agents' memory stores]

## Related Specs
- PERMISSIONS.md: [REPLACE THIS — path]
- DELEGATION.md: [REPLACE THIS — path]
- AUDITTRAIL.md: [REPLACE THIS — path]
