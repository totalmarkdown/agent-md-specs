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
---

# PERMISSIONS.md

**Category:** Governance
**Domain:** permissionsmd.dev
**Priority:** High
**Version:** 0.1.0

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
permission_level: restricted | standard | elevated | admin
last_reviewed: date
reviewed_by: string
---

# [Agent Name] — Permissions

## Allowed Actions
Actions this agent is explicitly authorized to perform:
- [ ] [Action 1]: [scope and limits]
- [ ] [Action 2]: [scope and limits]

## Denied Actions
Actions this agent must never perform:
- [Action]: [reason for denial]

## Tool Access
| Tool | Access Level | Restrictions |
|------|-------------|--------------|
| [Tool] | read-only / read-write / admin | [any limits] |

## Escalation Required
Actions that require human approval before execution:
- [Action]: [approval process]

## Permission Changes
- Permissions reviewed: [frequency]
- Changed by: [role/person authorized to change]
- Change log: [location]
```

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
