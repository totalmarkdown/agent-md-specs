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
spec_type: static
---


# ROSTER.md

**Category:** Coordination
**Domain:** rostermd.dev
**Priority:** High
**Version:** 0.1.0 **Type:** Static

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
_See CREW.md for how agents are organized into specialized working groups._

## Deprecated Agents
| Agent | Deprecated | Replacement | Migration guide |
|-------|-----------|-------------|-----------------|
| [Name] | [date] | [new agent] | [link] |
```

## Example Use Cases

**Enterprise:** A large manufacturing company maintains a ROSTER.md for its 30-agent operations fleet, giving the CTO a single view of every agent's role, status, owner, and capabilities with a coverage-gap analysis showing they lack a supply-chain forecasting specialist.

**Multi-Agent Fleet:** A DevOps team uses ROSTER.md's capability matrix to automatically route incoming infrastructure requests to the right agent (Terraform specialist for provisioning, Kubernetes expert for orchestration, security scanner for compliance checks) without manual triage.

**Regulated Industry:** A hospital system's IT department maintains ROSTER.md to track the certification status and access permissions of every clinical AI agent, immediately flagging any agent marked "deprecated" that still has active connections to patient record systems.

## Related Specs

| Spec | Relationship |
|------|-------------|
| CREW.md | Working group structure |
| DELEGATION.md | Authority chain and authorization |
| ORG.md | Organization-wide fleet configuration |
| SHAREDCONTEXT.md | Multi-agent shared memory pool |
| TEAM.md | Multi-agent team coordination |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
