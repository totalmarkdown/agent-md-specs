---
spec_name: GOALS.md
spec_version: 0.1.0
category: Process
domain: goalsmd.dev
priority: High
volume: "Vol 3 — Forward-Thinking Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
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
**Key results:**
- KR1: [Measurable result] — [current status]
- KR2: [Measurable result] — [current status]
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
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
