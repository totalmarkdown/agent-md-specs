---
spec_name: IDENTITY.md
spec_version: 0.1.0
category: Governance
domain: identitymd.dev
priority: High
volume: "Vol 2 — Extended Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# IDENTITY.md

**Category:** Governance
**Domain:** identitymd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Defines how an agent authenticates itself to external systems, 
how it verifies the identity of systems communicating with it, 
and how it manages credentials and certificates.

### Spec

```markdown
---
agent_name: string
agent_id: string          # Globally unique identifier
version: semver
identity_provider: string # Where identity is managed
created: date
updated: date
---

# [Agent Name] — Identity Configuration

## Agent Identity
- **Agent ID:** [UUID — stable, never changes]
- **Public key:** [location of public key certificate]
- **Identity provider:** [where this agent's identity is managed]

## Authentication to External Systems
| System | Method | Credential location | Rotation schedule |
|--------|--------|-------------------|------------------|
| [system] | [OAuth/key/cert] | [keychain key] | [schedule] |

## Verification of Incoming Requests
When receiving requests, verify identity using:
- Orchestrators: [verification method]
- MCP clients: [verification method]
- Human users: [auth method — defer to application layer]

## Credential Rotation
- API keys: rotate every [N days]
- OAuth tokens: refresh before expiry
- Certificates: renew [N days] before expiry
- On rotation: test new credential before invalidating old

## Identity Audit
Log all authentication events:
- Successful auth: timestamp, system, method
- Failed auth: timestamp, system, failure reason
- Credential rotation: timestamp, system, who rotated
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| DELEGATION.md | Authority chain and authorization |
| ENFORCEMENT.md | Policy verification and compliance |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| LIMITS.md | Hard constraints and safety boundaries |
| PERMISSIONS.md | Static resource access control |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
