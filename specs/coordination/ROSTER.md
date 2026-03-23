---
spec_name: ROSTER.md
spec_version: 0.1.0
category: Coordination
domain: rostermd.dev
priority: High
volume: "Vol 1 — Core Agent Specs"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# ROSTER.md

**Category:** Coordination
**Domain:** rostermd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Registry of all agents in a team or fleet — their names, roles, 
capabilities, current status, and contact/invocation details.

### Spec

```markdown
---
team_name: string
version: semver
agent_count: number
last_updated: date
---

# [Team Name] — Agent Roster

## Team Overview
[Brief description of what this team does collectively]

## Agents

### [Agent Name]
- **Role:** [lead | support | specialist | reporter | escalation]
- **Status:** [active | inactive | maintenance | deprecated]
- **Capabilities:** [comma-separated list]
- **Config file:** [path to CLAUDE.md or AGENTS.md]
- **Invocation:** [how to call this agent]
- **Owner:** [human responsible for this agent]
- **Last updated:** [date]
- **Notes:** [anything important to know]

[Repeat for each agent]

## Capability Matrix
| Capability | [Agent A] | [Agent B] | [Agent C] |
|-----------|----------|----------|----------|
| [Capability] | ✓ | ✗ | ✓ |

## Coverage Gaps
[Capabilities needed by the team that no current agent covers]
[Tasks that fall between agents and need explicit assignment]

## Deprecated Agents
| Agent | Deprecated | Replacement | Migration guide |
|-------|-----------|-------------|-----------------|
| [Name] | [date] | [new agent] | [link] |
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
