---
spec_name: GOALS.md
spec_version: 0.1.0
category: Process
domain: goalsmd.dev
priority: High
volume: "Vol 3 — Forward-Thinking Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# GOALS.md

**Category:** Process
**Domain:** goalsmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Defines what the agent is working toward — current objectives, 
success criteria, and progress indicators. The agent's OKRs. 
Updated regularly, not static. Enables humans and other agents 
to understand what this agent is optimizing for.

### Spec

```markdown
---
agent_name: string
version: semver
period: string          # Q1 2026 | March 2026 | Sprint 12
period_start: date
period_end: date
last_updated: date
---

# [Agent Name] — Current Goals

## This Period: [Period Name]

### Objective 1: [Name]
**Why this matters:** [Strategic rationale]  
**Success looks like:** [Concrete, measurable outcome]
**Progress:** [N]% complete
**Key results:** (see KPI.md for metric definitions)
- KR1: [Measurable result] -- [current status]
- KR2: [Measurable result] -- [current status]
**Blockers:** [None | description of blockers]

[Repeat for each objective]

## Long-term Goals (beyond this period)
- [Goal 1]: [Target date or "ongoing"]
- [Goal 2]: [Target date or "ongoing"]

## What I'm NOT Doing This Period
(To maintain focus)
- [Deprioritized item] — revisit [timeframe]

## How Goals Are Set
**Set by:** [Human | self | collaborative]  
**Review cadence:** [weekly | monthly]  
**Who reviews:** [role/name]  

## Previous Period Performance
**Period:** [Last period]  
**Objectives achieved:** [N/N]  
**Notable wins:** [List]
**Missed and why:** [List with explanation]

_See TESTSCORES.md for quantitative performance benchmarks._
```

## Example Use Cases

**Enterprise:** A sales-operations agent tracks Q1 goals including "reduce lead response time from 4 hours to 30 minutes" with weekly progress updates, while explicitly documenting that CRM migration is deprioritized this quarter to maintain focus.

**Multi-Agent Fleet:** Each agent in a 20-agent customer-support fleet publishes aligned GOALS.md files -- all targeting the same "95% customer satisfaction" objective but with role-specific key results like "resolve 80% of tier-1 tickets without escalation" for front-line agents.

**Regulated Industry:** A drug-safety reporting agent's GOALS.md tracks the objective "submit all Individual Case Safety Reports within 15 calendar days of receipt" with measurable key results and a previous-period performance section showing 98.5% on-time submission rate.

## Related Specs

| Spec | Relationship |
|------|-------------|
| DEADLINES.md | Time constraints and schedules |
| WORKFLOW.md | Task execution flow |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
