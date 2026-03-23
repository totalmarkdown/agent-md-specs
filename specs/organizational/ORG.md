---
spec_name: ORG.md
spec_version: 0.1.0
category: Organizational
domain: orgmd.dev
priority: High
volume: "Vol 5 — Organizational & Validation"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# ORG.md

**Category:** Organizational
**Domain:** orgmd.dev
**Priority:** High
**Version:** 0.1.0

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
complete picture of the entire fleet structure.

### Spec

```markdown
---
org_name: string
org_id: string            # Globally unique org identifier
version: semver
founded: date             # When this org/fleet was established
agent_count: number       # Total agents in org
team_count: number        # Total teams
human_count: number       # Human members
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
| Decision type | Authority | Escalation |
|--------------|-----------|-----------|
| Day-to-day task | Individual agent | Team lead |
| Cross-team coordination | Team leads | Dept head |
| New agent deployment | Dept head | Org director |
| Budget > $[X] | Org director | Human board |
| Policy changes | Human board | N/A |

### Policies
All agents in this org operate under:
- POLICY.md: [link to org-wide policy file]
- SECURITY.md: [link to org-wide security rules]
- COMPLIANCE.md: [link to compliance requirements]
- BUDGET.md: [link to org-wide budget rules]

## Fleet Health
| Metric | Current | Target | Trend |
|--------|---------|--------|-------|
| Overall uptime | [N]% | 99.5% | [↑/→/↓] |
| Task completion rate | [N]% | 95% | [↑/→/↓] |
| Average quality score | [N]/100 | 85 | [↑/→/↓] |
| Active incidents | [N] | 0 | [↑/→/↓] |

## Directory
Full agent directory: [link to ROSTER.md or registry]  
Team directory: [link]  
Human directory: [link or "private"]

## Contact
**Org owner:** [name/role]  
**Technical contact:** [name/role]  
**For hiring agents:** See marketplace/[org-profile]
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
