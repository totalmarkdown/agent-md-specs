---
spec_name: TEAM.md
spec_version: 0.1.0
category: Coordination
domain: teammd.dev
priority: High
volume: "Vol 1 — Core Agent Specs"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
---

> **Canonical repository:**
> [totalmarkdown/team.md](https://github.com/totalmarkdown/team.md)
> This copy is included in agent-md-specs for cross-reference.
> For contributions to this specific spec, use the canonical repo.

# TEAM.md

**Category:** Coordination
**Domain:** teammd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Defines a coordinated group of AI agents working together on a shared goal. 
Describes each agent's role, how they communicate, and how they hand off 
work between each other.

### When to create
When 2 or more agents collaborate on a workflow where the output of one 
agent becomes the input of another, or where agents work in parallel on 
related tasks.

### Spec

```markdown
---
team_name: string          # Human-readable team name
version: semver            # e.g. 1.0.0
purpose: string            # One sentence describing what this team does
orchestration: string      # sequential | parallel | conditional | lead-delegates
shared_memory: boolean     # Do agents share a MEMORY.md file?
created: date
updated: date
---

# [Team Name]

## Purpose
[2-3 sentences describing what this team accomplishes together]

## Agents

### [Agent Name] — [Role]
- **Bundle:** path/to/agent/CLAUDE.md
- **Role:** lead | support | specialist | reporter | escalation
- **Triggers:** ["list", "of", "trigger", "phrases"]
- **Inputs:** What this agent receives
- **Outputs:** What this agent produces
- **Hands off to:** [Next agent name or "human"]

[Repeat for each agent]

## Handoff Protocol
[How agents pass context between each other]
[What format handoff messages take]
[What triggers a handoff]

## Shared Context
[What all agents share — shared MEMORY.md path, shared data sources]

## Failure Handling
[What happens when an agent fails or times out]
[Which agent or human takes over]

## Success Criteria
[How the team knows it has completed its goal]
```

### Example use cases
- Customer support team (triage → resolve → escalate → follow-up)
- Content pipeline (research → draft → edit → publish → analyze)
- Security audit team (scan → analyze → report → remediate)
- Sales team (qualify → demo → proposal → close → onboard)

---

## Related Specs

| Spec | Relationship |
|------|-------------|
| BUDGET.md | Cost controls and spending limits |
| CREW.md | Working group structure |
| DELEGATION.md | Authority chain and authorization |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| MEMORY.md | Individual agent memory governance |
| ORG.md | Organization-wide fleet configuration |
| SHAREDCONTEXT.md | Multi-agent shared memory pool |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
