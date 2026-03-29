---
spec_name: PERMISSIONS.md
spec_version: 0.1.0
category: Governance
domain: permissionsmd.dev
priority: High
volume: "Vol 1 — Core Agent Specs"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
spec_type: static
---


# PERMISSIONS.md

**Category:** Governance
**Domain:** permissionsmd.dev
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose
Defines what an agent is and is not allowed to do — capability boundaries, 
tool access controls, and action restrictions. The access control list for 
AI agent operations.

### When to create
When an agent has access to tools, APIs, or actions that need explicit 
boundaries — especially in multi-agent systems where different agents 
have different privilege levels.

### Spec

```markdown
---
agent_name: string
version: semver
permission_level: restricted | standard | elevated | admin  # Authority source defined in DELEGATION.md
last_reviewed: date
reviewed_by: string
---

# [Agent Name] — Permissions

## Allowed Actions
Actions this agent is explicitly authorized to perform.
For dynamic, just-in-time privilege grants beyond this static list,
see LEASTPRIVILEGE.md.
- [ ] [Action 1]: [scope and limits]
- [ ] [Action 2]: [scope and limits]

## Denied Actions
Actions this agent must never perform (see LIMITS.md for hard constraints that permissions cannot exceed):
- [Action]: [reason for denial]

## Tool Access
Resource-level access controls that implement these permissions
are defined in ACCESS.md.
| Tool | Access Level | Restrictions |
|------|-------------|--------------|
| [Tool] | read-only / read-write / admin | [any limits] |

## Escalation Required
Actions that require human approval before execution (see ESCALATION.md):
- [Action]: [approval process]

## Permission Changes
Enforcement of these permissions at runtime is handled by ENFORCEMENT.md.
- Permissions reviewed: [frequency]
- Changed by: [role/person authorized to change]
- Change log: [location] (all permission checks are logged in AUDITTRAIL.md)
```

## Example Use Cases

**Enterprise:** A marketing analytics agent is granted read-only access to the campaign database and read-write access to its own reporting workspace, with any attempt to modify campaign configurations or access the finance database explicitly denied and logged.

**Multi-Agent Fleet:** Each agent in a content moderation fleet is assigned different permission levels — junior agents get read-only access to flagged content, while senior agents get read-write access to moderation decisions, enforcing a tiered review workflow through static permission boundaries.

**Regulated Industry:** A GDPR-compliant data processing agent has explicit permissions to read anonymized analytics data but is denied access to any table containing raw PII, with every permission change requiring sign-off from the Data Protection Officer and logged in the change history.

## Related Specs

| Spec | Relationship |
|------|-------------|
| ACCESS.md | Who can invoke this agent |
| DELEGATION.md | Authority chain and authorization |
| ENFORCEMENT.md | Policy verification and compliance |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| LEASTPRIVILEGE.md | Dynamic zero-trust privilege management |
| LIMITS.md | Hard constraints and safety boundaries |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
