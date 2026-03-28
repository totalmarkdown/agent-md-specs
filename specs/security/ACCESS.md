---
spec_name: ACCESS.md
spec_version: 0.1.0
category: Security
domain: accessmd.dev
priority: High
volume: "Vol 12 — Fleet Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
---

# ACCESS.md

**Category:** Security
**Domain:** accessmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Defines exactly who and what is authorized to invoke this agent —
the allowlist of callers, their permission levels, and what
each caller is and isn't allowed to ask the agent to do.

As agent fleets grow, controlling which agents can call which
other agents becomes a critical security and governance problem.
ACCESS.md is the solution: an explicit, auditable access control
list for every agent.

### Spec

```markdown
---
agent_name: string
version: semver
access_model: string      # open | allowlist | token-gated | invite-only
default_policy: string    # allow | deny
last_reviewed: date
approved_by: string
---

# [Agent Name] — Access Control

## Access Model
**Model:** [open | allowlist | token-gated | invite-only]
**Default policy:** [Allow all except denied | Deny all except allowed]

---

## Authorized Humans

| Name | Role | What they can ask | What they cannot ask | Auth method |
|------|------|------------------|---------------------|------------|
| [Name] | Owner | Anything | Nothing restricted | SSH key |
| [Name] | Operator | [scope] | [restrictions] | API key |
| [Name] | User | [scope] | [restrictions] | Token |

---

## Authorized Agents

| Agent ID | Agent Name | Trust level | What it can delegate | Auth method |
|---------|-----------|------------|---------------------|------------|
| [UUID] | [name] | High | [task types] | Signed JWT |
| [UUID] | [name] | Medium | [task types] | API key |

**Agents NOT on this list:** Denied by default.

---

## Authorized Systems

| System | Purpose | What it can do | Auth |
|--------|---------|---------------|------|
| [n8n instance] | Orchestration | Assign any task | Webhook secret |
| [CI/CD system] | Automated runs | [specific tasks only] | Service token |
| [monitoring] | Health checks | Read-only status | Read-only token |

---

## Permission Levels

### Level 1 — Read
Can query status, ask questions, request information.
Cannot trigger actions that modify state (see PERMISSIONS.md for resource-level controls).

### Level 2 — Execute
Can assign tasks and receive results.
Cannot modify agent configuration.

### Level 3 — Configure
Can modify agent behavior, update MEMORY.md.
Cannot grant access to others.

### Level 4 — Admin
Full access including access management.
Requires MFA. Logged extensively.
Apply LEASTPRIVILEGE.md principles when granting any level above Read.

---

## Denied Callers

These callers are explicitly blocked regardless of credentials:

| Caller | Reason | Since |
|--------|--------|-------|
| [identifier] | [why blocked] | [date] |

---

## Access Review

Access is reviewed: [quarterly | annually]
Last reviewed: [date]
Reviewed by: [name/role]
Next review: [date]

To request access: [process]
To report unauthorized access: [security contact]
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| ATTESTATION.md | Identity verification and credential lifecycle |
| AUDITTRAIL.md | Tamper-proof action logging |
| DELEGATION.md | Authority chain and authorization |
| ENFORCEMENT.md | Policy verification and compliance |
| LEASTPRIVILEGE.md | Dynamic zero-trust privilege management |
| MEMORY.md | Individual agent memory governance |
| PERMISSIONS.md | Static resource access control |
| PROMPTSHIELD.md | Prompt injection defense |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
