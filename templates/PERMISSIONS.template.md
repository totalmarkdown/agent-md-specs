---
spec_name: PERMISSIONS.md
spec_version: 0.1.0
category: Security
domain: specmd.dev
priority: P0
tier: core
---

# [REPLACE THIS — Agent Name] — Resource Permissions

<!-- Explicit access control: what resources this agent can touch and how -->

## Permission Model
- **Type:** [REPLACE THIS — allowlist | denylist | RBAC | ABAC]
- **Default:** [REPLACE THIS — deny-all | allow-read-only]
- **Enforcement:** [REPLACE THIS — runtime | gateway | honor-system]

## Resource Access

### Files & Storage
| Path / Pattern | Read | Write | Delete | Notes |
|----------------|------|-------|--------|-------|
| [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |
| [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |

### APIs & Services
| Service | Methods | Rate Limit | Auth |
|---------|---------|------------|------|
| [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |
| [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |

### Data Stores
| Store | Read | Write | Query Scope |
|-------|------|-------|-------------|
| [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |

## Explicitly Denied
<!-- Resources this agent must never access -->
- [REPLACE THIS — e.g. /etc/shadow, production credentials]
- [REPLACE THIS — e.g. other agents' private memory]
- [REPLACE THIS — e.g. billing endpoints]

## Environment Variables
- **Allowed:** [REPLACE THIS — list of env vars agent may read]
- **Blocked:** [REPLACE THIS — list of env vars agent must never access]

## Permission Changes
- **Requested by:** [REPLACE THIS — who can request permission changes]
- **Approved by:** [REPLACE THIS — who grants changes]
- **Change log:** [REPLACE THIS — where permission changes are recorded]

## Related Specs
- LEASTPRIVILEGE.md: [REPLACE THIS — path]
- DELEGATION.md: [REPLACE THIS — path]
- AUDITTRAIL.md: [REPLACE THIS — path]
