---
spec_name: REPORTSTO.md
spec_version: 0.1.0
category: Organizational
domain: reportstomd.dev
priority: High
volume: "Vol 3 — Forward-Thinking Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# REPORTSTO.md

**Category:** Organizational
**Domain:** reportstomd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Defines the accountability chain for an agent — who/what it 
reports to, who can give it instructions, and how authority 
flows through the agent hierarchy. The org chart for AI agents.

### Spec

```markdown
---
agent_name: string
version: semver
primary_accountable: string  # Who this agent is ultimately accountable to
---

# [Agent Name] — Reporting Structure

## Primary Accountability
**This agent reports to:** [Human name/role OR parent agent ID]  
**Contact:** [How to reach them]  
**Authority level:** [What this entity can instruct the agent to do]

## Authority Hierarchy
Who can give this agent instructions, in order of authority:
1. **[Human owner]** — full authority, can override anything
2. **[Human operator]** — operational authority within defined scope
3. **[Orchestrating agent]** — can assign tasks within AGENTS.md scope
4. **[Any user]** — limited to pre-approved request types

## Escalation Path
When this agent needs human input (see ESCALATION.md for trigger conditions):
1. First contact: [name/role] via [channel]
2. If unavailable: [backup] via [channel]
3. If urgent and neither available: [emergency contact]

## Performance Review
This agent's performance is reviewed by: [role]  
Review cadence: [weekly | monthly | quarterly]  
Metrics reviewed: [list key metrics]  
Review stored in: [location]

## Delegation Authority
For full delegation rules and constraints, see DELEGATION.md.
This agent CAN delegate to:
| Agent | What can be delegated | Limits |
|-------|----------------------|--------|
| [agent] | [task types] | [constraints] |

This agent CANNOT delegate:
- [Tasks that must be done by this agent directly]
- [Decisions that require this agent's specific authority]

## Override Protocol
If this agent's output is overridden by a human:
1. Log the override with: what was changed, by whom, timestamp
2. Do not re-assert the overridden position
3. Learn from the override if pattern is consistent
4. Flag in MEMORY.md if override reveals a gap in understanding
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| CREW.md | Working group structure |
| DELEGATION.md | Authority chain and authorization |
| MEMORY.md | Individual agent memory governance |
| ORG.md | Organization-wide fleet configuration |
| TEAM.md | Multi-agent team coordination |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
