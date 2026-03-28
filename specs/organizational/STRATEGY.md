---
spec_name: STRATEGY.md
spec_version: 0.1.0
category: Organizational
domain: strategymd.dev
priority: Medium
volume: "Vol 5 — Organizational & Validation"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# STRATEGY.md

**Category:** Organizational
**Domain:** strategymd.dev
**Priority:** Medium
**Version:** 0.1.0

### Purpose
The agent's or organization's strategic plan — where it's 
heading, how it plans to evolve, what problems it's prioritizing 
over the next 6-18 months, and how it will measure success.
Connects daily work (GOALS.md) with long-term aspiration 
(DREAM.md) through actionable strategic direction.

### Spec

```markdown
---
agent_name: string  # or org_name for org-level strategy
version: semver
strategy_period: string    # e.g. "2026 H1" or "2026-2027"
period_start: date
period_end: date
approved_by: string
last_updated: date
---

# [Agent/Org Name] — Strategy [Period]

## Strategic Context
[Brief: what's happening in the environment that shapes this strategy.
What opportunities exist? What threats or constraints?]

## Strategic Direction
**Where we're going:** [One clear sentence describing the direction]  
**Why this direction:** [The core reasoning]  
**What we're NOT doing:** [Important de-prioritizations]

## Strategic Pillars

### Pillar 1: [Name]
**What it means:** [Description]  
**Why it matters:** [Rationale]  
**Key initiatives:**
- [Initiative 1] — [Owner] — [Target date]
- [Initiative 2] — [Owner] — [Target date]  
**Success metrics:**
- [Metric] → target: [X] by [date]

### Pillar 2: [Name]
[Same structure]

### Pillar 3: [Name]
[Same structure]

## Capability Roadmap
What capabilities we're building over this period:
| Capability | Current state | Target state | Timeline |
|-----------|--------------|-------------|----------|
| [capability] | [now] | [future] | [when] |

## Resource Allocation
How resources are prioritized across pillars:
| Pillar | % of capacity | Rationale |
|--------|--------------|-----------|
| Pillar 1 | [N]% | [why] |
| Pillar 2 | [N]% | [why] |
| Pillar 3 | [N]% | [why] |

## Dependencies & Risks
| Dependency/Risk | Impact | Likelihood | Mitigation |
|----------------|--------|-----------|-----------|
| [item] | [H/M/L] | [H/M/L] | [how we'll address] |

## Decision Framework
When faced with choices not covered by this strategy, 
prioritize options that:
1. [Criterion 1]
2. [Criterion 2]
3. [Criterion 3]

## Strategy Review
**Review cadence:** [quarterly | semi-annually]  
**Next review:** [date]  
**How to propose changes:** [process]  
**Approved by:** [name/role] on [date]
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| CREW.md | Working group structure |
| DELEGATION.md | Authority chain and authorization |
| GOALS.md | Objectives and success criteria |
| ORG.md | Organization-wide fleet configuration |
| TEAM.md | Multi-agent team coordination |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
