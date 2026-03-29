---
spec_name: SECRETS.md
spec_version: 0.1.0
category: Security
domain: secretsmd.dev
priority: Very High
volume: "Vol 12 — Fleet Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
spec_type: static
---


# SECRETS.md

**Category:** Security
**Domain:** secretsmd.dev
**Priority:** Very High
**Version:** 0.1.0 **Type:** Static

### Purpose
Declares every secret this agent requires to function —
API keys, tokens, credentials, certificates — without
containing the actual values. Acts as a manifest:
"here is what I need, here is where it lives, here is
who controls it."

At fleet scale, SECRETS.md enables:
- Automated secret injection at deployment time
- Audit trails of what secrets each agent can access
- Rotation planning across hundreds of agents
- Incident response (which agents had access to a compromised key)

**Critical rule: SECRETS.md never contains secret values.
Only names, locations, and policies.**

### Spec

```markdown
---
agent_name: string
version: semver
secret_count: number
vault_system: string      # doppler | hashicorp | aws-secrets | azure-kv | env | keychain
environment: string       # development | staging | production | all
last_audited: date
audited_by: string
---

# [Agent Name] — Secrets Manifest

## ⚠ IMPORTANT
This file declares what secrets this agent requires.
It does NOT contain secret values.
Never commit actual credentials to this file.
Secret values live in: [vault system name] (see VAULT.md for fleet-wide vault governance)

---

## Secrets Registry

### [SECRET_NAME]
| Property | Value |
|----------|-------|
| **Environment variable** | `SECRET_NAME` |
| **Purpose** | [What this secret is used for] |
| **Service** | [Which external service this authenticates to] |
| **Type** | [API key | OAuth token | password | certificate | webhook secret] |
| **Scope** | [What permissions this credential has] |
| **Storage** | [Doppler project/config | AWS path | env var name] |
| **Owner** | [Team or person responsible for this credential] |
| **Rotation schedule** | [Every N days | on breach | never | manual] |
| **Last rotated** | [date] |
| **Shared with** | [Other agents that use the same credential, or "none"] |
| **Required** | [yes | no — what happens if missing] |
| **Environments** | [dev | staging | prod | all] |

[Repeat for each secret]

---

## Secrets Summary

| Secret | Type | Required | Rotates | Shared |
|--------|------|---------|---------|--------|
| [SECRET_NAME] | [type] | [yes/no] | [schedule] | [yes/no] |

---

## Access Control

**Who can read these secrets:**
- [Role/agent 1] — [why they need access]
- [Role/agent 2] — [why they need access]

**Who can rotate these secrets:**
- [Role/person] — [process for rotation]

**Who can revoke access:**
- [Role/person] — [process for revocation]

---

## Rotation Procedures

### Rotating [SECRET_NAME]
1. Generate new credential at [service]
2. Add to [vault system] under [path/key]
3. Deploy to affected agents: [list]
4. Verify all agents healthy with new credential
5. Revoke old credential at [service]
6. Update rotation date in this file
7. Log rotation in AUDITTRAIL.md

---

## Breach Response
Verify credential provenance via ATTESTATION.md before re-issuing.

If any secret in this file is compromised:
1. **Immediately:** Revoke the compromised credential at the source service
2. **Within 5 minutes:** Notify [security contact]
3. **Within 1 hour:** Rotate all secrets that share the same service account
4. **Document:** Which agents had access, when breach occurred, impact
5. **Review:** How was this credential exposed? Update procedures.

Emergency rotation contact: [contact]
Security incident process: See ICE.md

---

## Audit Log

| Date | Action | Secret | Performed by | Reason |
|------|--------|--------|-------------|--------|
| [date] | [rotated/revoked/granted] | [secret] | [who] | [why] |
```

## Example Use Cases

**Enterprise:** A media company uses SECRETS.md to declare all API keys its content moderation agent requires — Anthropic, OpenAI, and a custom vision API — specifying that each is stored in Doppler with 90-day rotation, enabling automated rotation without downtime.

**Multi-Agent Fleet:** A platform team uses SECRETS.md manifests across 80 agents to quickly identify every agent affected when a shared database credential is compromised, completing rotation and revocation of the old credential within the 1-hour breach response window.

**Regulated Industry:** A healthcare technology company uses SECRETS.md to ensure its patient data agent's credentials are never hardcoded, with the breach response procedure requiring immediate revocation, 5-minute security notification, and incident documentation meeting HIPAA administrative safeguard requirements.

## Related Specs

| Spec | Relationship |
|------|-------------|
| ATTESTATION.md | Identity verification and credential lifecycle |
| AUDITTRAIL.md | Tamper-proof action logging |
| ENFORCEMENT.md | Policy verification and compliance |
| ICE.md | Emergency break-glass protocols |
| PERMISSIONS.md | Static resource access control |
| PROMPTSHIELD.md | Prompt injection defense |
| SESSION.md | Ephemeral runtime identity and task scope |
| VAULT.md | Secrets storage governance |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
