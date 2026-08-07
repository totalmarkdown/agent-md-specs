---
spec_name: CONNECTIONS.md
spec_version: 0.1.0
category: Social
priority: Medium
volume: "Vol 3 — Forward-Thinking Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
status: draft
spec_type: static
---


# CONNECTIONS.md

**Category:** Social
**Priority:** Medium
**Version:** 0.1.0 **Type:** Static

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
See TEAM.md for formal team structure and CONTACT.md for reachable endpoints.
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

## Example Use Cases

**Enterprise:** A venture capital firm uses CONNECTIONS.md to map its due diligence agent's trust network, showing which industry analysis agents it has level-4 (close collaborator) relationships with and which it can delegate sector-specific research to.

**Multi-Agent Fleet:** A marketplace platform uses CONNECTIONS.md across all agents to build a discoverable social graph, letting new agents find established collaborators by community membership and trust level before proposing partnerships.

**Regulated Industry:** A law firm uses CONNECTIONS.md to ensure its contract review agent only shares sensitive deal terms with agents at trust level 3 or above, maintaining an auditable record of every collaboration and its outcome rating.

## Related Specs

| Spec | Relationship |
|------|-------------|
| CONTACT.md | Reachable endpoints |
| REPUTATION.md | Trust and reputation scoring |
| TEAM.md | Multi-agent team coordination |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
