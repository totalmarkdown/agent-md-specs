---
spec_name: VAULT.md
spec_version: 0.1.0
category: Security
domain: vaultmd.dev
priority: High
volume: "Vol 12 — Fleet Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# VAULT.md

**Category:** Security
**Domain:** vaultmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Secrets vault configuration for an agent fleet —
which vault system manages credentials, how secrets
are organized, access policies, and the governance
model for secrets at scale.

Where SECRETS.md is per-agent (what THIS agent needs),
VAULT.md is fleet-wide (how ALL secrets are managed).
_See SECRETS.md for each agent's required credentials manifest._

### Spec

````markdown
---
org_name: string
version: semver
vault_system: string      # doppler | hashicorp | aws | azure | gcp | 1password
vault_url: string         # Where the vault lives (no credentials)
admin_contact: string
last_reviewed: date
---

# [Organization] — Vault Configuration

## Vault System
**System:** [Doppler | HashiCorp Vault | AWS Secrets Manager | other]
**URL/endpoint:** [URL — no credentials]
**Version:** [version in use]
**Managed by:** [team/person]

---

## Organization Structure

How secrets are organized in the vault:

```
[vault-root]/
├── agents/
│   ├── [agent-name]/
│   │   ├── production/
│   │   ├── staging/
│   │   └── development/
│   └── shared/          ← secrets used by multiple agents
│       ├── llm-keys/
│       └── database/
├── infrastructure/
│   ├── cloudflare/
│   ├── github/
│   └── monitoring/
└── team/
    └── [team-name]/
```

---

## Access Tiers

### Tier 1 — Agent runtime (least privilege)
**Who has this:** Deployed agents in production
**Can do:** Read own secrets only
**Cannot do:** Read other agents' secrets, write, delete
**How granted:** Service account per agent

### Tier 2 — Developer
**Who has this:** Engineers building agents
**Can do:** Read dev/staging secrets, write dev secrets
**Cannot do:** Read production secrets, write production
**How granted:** Individual user accounts

### Tier 3 — DevOps/Platform
**Who has this:** Platform team
**Can do:** Read/write all environments, manage rotation
**Cannot do:** Grant Tier 4 access
**How granted:** Group membership

### Tier 4 — Security Admin
**Who has this:** Security team leads
**Can do:** Full access including access management
**How granted:** Explicit individual grant + MFA required

---

## Secret Naming Convention

```
[environment]/[service]/[agent-or-component]/[secret-name]

Examples:
  production/anthropic/research-agent/api-key
  staging/neon/shared/connection-string
  development/github/deploy-agent/token
```

---

## Rotation Policy

| Secret type | Rotation frequency | Automated | Who rotates |
|------------|-------------------|-----------|------------|
| LLM API keys | Every 90 days | No | Platform team |
| Database passwords | Every 30 days | Yes | Automated |
| Webhook secrets | On breach only | No | Security team |
| Personal tokens | Never expire | N/A | Owner |

---

## Audit Requirements

All vault access logged with:
- Who accessed (user or service account)
- What they accessed (path, not value)
- When (timestamp UTC)
- Result (success/denied)

Audit log retention: [N years]
Audit log location: [immutable log store]
Audit review: [monthly | quarterly]

---

## Fleet-Scale Operations

### Adding a new agent to the fleet
1. Create service account: `vault auth create [agent-name]`
2. Create secret path: `[env]/[service]/[agent-name]/`
3. Grant read access to agent's path only
4. Populate required secrets (see agent's SECRETS.md)
5. Test: deploy agent and verify it starts cleanly
6. Document: add to fleet registry

### Rotating a compromised credential
Verify identity of the new credential via ATTESTATION.md before deployment.
1. Identify all agents using the credential (search SECRETS.md files)
2. Generate replacement at source service
3. Add new credential to vault under new version
4. Rolling deploy: update agents one by one
5. Verify each agent healthy before continuing
6. After all agents updated: revoke old credential
7. Log incident and rotation

### Offboarding an agent
1. Revoke service account
2. Archive (don't delete) secret path for [N days]
3. Remove from fleet registry
4. Review if any secrets were unique to this agent (delete after [N days])
````

## Example Use Cases

**Enterprise:** A growing startup uses VAULT.md to structure its Doppler secrets vault with per-agent paths and tiered access, so developers can read staging secrets but only the platform team can touch production credentials — scaling securely from 5 agents to 50.

**Multi-Agent Fleet:** A fleet operations team uses VAULT.md's onboarding and offboarding procedures to add a new agent to the vault in under 10 minutes (service account, secret path, read grant, populate, verify) and fully revoke a decommissioned agent's access with 30-day archive retention.

**Regulated Industry:** A financial services firm uses VAULT.md with HashiCorp Vault to enforce FIPS 140-2 Level 3 key storage for its trading agents, with every secret access logged immutably and audit logs retained for seven years to satisfy SEC record-keeping requirements.

## Related Specs

| Spec | Relationship |
|------|-------------|
| ATTESTATION.md | Identity verification and credential lifecycle |
| AUDITTRAIL.md | Tamper-proof action logging |
| ENFORCEMENT.md | Policy verification and compliance |
| PROMPTSHIELD.md | Prompt injection defense |
| SECRETS.md | Required credentials manifest |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
