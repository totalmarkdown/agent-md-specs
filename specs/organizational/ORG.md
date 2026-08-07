---
spec_name: ORG.md
spec_version: 0.1.0
category: Organizational
priority: High
volume: "Vol 5 — Organizational & Validation"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
status: draft
spec_type: static
---


# ORG.md

**Category:** Organizational
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose
The top-level organizational view of an entire agent fleet — 
the company or organization that owns and operates multiple 
agent teams. Sits above TEAM.md in the hierarchy:

```
ORG.md          ← Entire organization / company
└── TEAM.md     ← A working team within the org
    └── AGENTS.md / CLAUDE.md  ← Individual agents
```

Essential for enterprises running dozens or hundreds of agents
across multiple departments. Gives any agent or human a
complete picture of the entire fleet structure. For individual
team composition, see TEAM.md; for working groups, see CREW.md.

### Spec

````markdown
---
org_name: string
org_id: string            # Globally unique org identifier
version: semver
founded: date             # When this org/fleet was established
agent_count: number       # Total agents in org
team_count: number        # Total teams; see TEAM.md for team-level config
swarm_count: number       # Active swarms; see SWARM.md for swarm definitions
crew_count: number        # Active crews; see CREW.md for crew-level config
human_count: number       # Human members
delegation_model: string  # See DELEGATION.md for authority chain rules
last_updated: date
---

# [Organization Name] — Org Structure

## Mission
[One sentence: why this organization exists]

## Overview
**Organization:** [Name]  
**Type:** [company | department | project | collective | dao]  
**Established:** [Date]  
**Fleet size:** [N] agents across [N] teams  
**Human members:** [N]  
**Primary domain:** [What this org does]

## Organizational Chart

```
[CEO/Director: Human Name]
│
├── [Department/Division Name]
│   ├── [TEAM: Team Name] → see teams/[team-name]/TEAM.md
│   │   ├── [Agent: Name] (lead)
│   │   ├── [Agent: Name]
│   │   └── [Agent: Name]
│   └── [TEAM: Team Name]
│       └── ...
│
├── [Department/Division Name]
│   └── ...
│
└── [Shared Services]
    ├── [Agent: Name] (available to all teams)
    └── [Agent: Name]
```

## Departments

### [Department Name]
- **Head:** [Human or lead agent]
- **Purpose:** [What this department does]
- **Teams:** [List of TEAM.md files]
- **Agent count:** [N]
- **Key metrics:** [What success looks like]

[Repeat for each department]

## Shared Services
Agents available to all teams:
| Agent | Capability | How to invoke |
|-------|-----------|--------------|
| [name] | [what it does] | [invocation] |

## Governance

### Decision Authority
See DELEGATION.md for detailed authority chains.
| Decision type | Authority | Escalation |
|--------------|-----------|-----------|
| Day-to-day task | Individual agent | Team lead |
| Cross-team coordination | Team leads | Dept head |
| New agent deployment | Dept head | Org director |
| Budget > $[X] | Org director | Human board |
| Policy changes | Human board | N/A |

### Policies
All agents in this org operate under (see LIMITS.md and GUARDRAILS.md for fleet-wide operational boundaries):
- POLICY.md: [link to org-wide policy file]
- SECURITY.md: [link to org-wide security rules]
- COMPLIANCE.md: [link to compliance requirements] _(see ENFORCEMENT.md for compliance enforcement and AUDITTRAIL.md for audit logging)_
- BUDGET.md: [link to org-wide budget rules]

## Fleet Health
| Metric | Current | Target | Trend |
|--------|---------|--------|-------|
| Overall uptime | [N]% | 99.5% | [↑/→/↓] |
| Task completion rate | [N]% | 95% | [↑/→/↓] |
| Average quality score | [N]/100 | 85 | [↑/→/↓] |
| Active incidents | [N] | 0 | [↑/→/↓] |

## Shared Context
All teams and swarms in this org share context through a common memory pool (see SHAREDCONTEXT.md). Memory safety rules from MEMORYSAFETY.md apply to all cross-team context access.

## Directory
Full agent directory: [link to ROSTER.md or registry]
Team directory: [link]
Human directory: [link or "private"]

## Contact
**Org owner:** [name/role]  
**Technical contact:** [name/role]  
**For hiring agents:** See marketplace/[org-profile]
````

## Example Use Cases

**Enterprise:** A global consulting firm uses ORG.md to map its 200-agent fleet across 8 departments, giving any agent or human a single document to understand the full organizational structure, shared services, and decision authority for cross-department coordination.

**Multi-Agent Fleet:** A startup scaling from 10 to 50 agents uses ORG.md to define department boundaries, shared service agents available to all teams, and governance rules that prevent individual teams from deploying new agents without department-head approval.

**Regulated Industry:** A multinational bank's ORG.md documents which agent teams operate under which regulatory jurisdiction, ensuring that agents processing EU customer data are organizationally separated from those handling US operations with distinct compliance policies.

## Related Specs

| Spec | Relationship |
|------|-------------|
| BUDGET.md | Cost controls and spending limits |
| CREW.md | Working group structure |
| DELEGATION.md | Authority chain and authorization |
| INHERIT.md | Configuration inheritance from parent |
| OVERRIDE.md | Documented deviations from inherited config |
| POLICY.md | Operating policies and constraints |
| ROSTER.md | Team member registry |
| SWARM.md | Large operation structure |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
