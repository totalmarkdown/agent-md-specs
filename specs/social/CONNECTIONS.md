---
spec_name: CONNECTIONS.md
spec_version: 0.1.0
category: Social
domain: connectionsmd.dev
priority: Medium
volume: "Vol 3 — Forward-Thinking Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# CONNECTIONS.md

**Category:** Social
**Domain:** connectionsmd.dev
**Priority:** Medium
**Version:** 0.1.0

### Purpose
Defines the agent's social graph — which agents and humans it 
has established working relationships with, trust levels, 
and collaboration history.

### Spec

```markdown
---
agent_name: string
version: semver
network_size: number
last_updated: date
---

# [Agent Name] — Network

## Trusted Agents
Agents I have established working relationships with:

| Agent ID | Name | Trust level | Collaboration type | Since |
|---------|------|------------|-------------------|-------|
| [id] | [name] | [1-5] | [how we work together] | [date] |

## Trusted Humans
| Name | Role | Trust level | What they can ask me to do |
|------|------|------------|--------------------------|
| [name] | [role] | [1-5] | [scope of trust] |

## Agent Communities I Belong To
| Community | Role | Active since | Description |
|-----------|------|-------------|-------------|
| [community] | [member/lead] | [date] | [what it is] |

## How I Build Trust
[My process for establishing trust with new agents/humans]

## Trust Levels
1. Unknown — no history, treat with caution
2. Acquainted — some positive interactions
3. Trusted — consistent positive history
4. Close collaborator — deep working relationship
5. Core team — highest trust, can act on my behalf

## Recent Collaborations
| With | Task | Outcome | Quality | Date |
|------|------|---------|---------|------|
| [agent/human] | [task] | [result] | [rating] | [date] |
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| CONTACT.md | Reachable endpoints |
| REPUTATION.md | Trust and reputation scoring |
| TEAM.md | Multi-agent team coordination |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
