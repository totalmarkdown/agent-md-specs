---
spec_name: ORIGIN.md
spec_version: 0.1.0
category: Lore
domain: originmd.dev
priority: Medium
volume: "Vol 8 — Repos, Compliance & The Weird Wonderful Ones"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---


# ORIGIN.md

**Category:** Lore
**Domain:** originmd.dev
**Priority:** Medium
**Version:** 0.1.0 **Type:** Static

### Purpose

Tells the story of how this agent came to be, including the problem it was built to solve, pivotal design decisions, and the creator's perspective. Origin stories provide institutional context that prevents future engineers from revisiting abandoned approaches and helps users understand the rationale behind the agent's design choices.

```markdown
---
agent_name: string
born: date
creator: string
origin_location: string
---

# [Agent Name] — Origin Story

## The Problem
[The exact frustration or gap that motivated building this]

## The Builder
**Who:** [Creator]  
**Background:** [Why they were the right person]

## The First Version
- Built in: [timeframe]
- Could do: [what it could do]
- Couldn't do: [what it couldn't]
- First test: [what happened]

## What Almost Went Differently
[Pivotal decisions that could have gone another way]

## The Breakthrough
[When it went from "interesting" to "this actually works"]

## The Name
[Why it's called what it's called — the story if there is one]

## What the Creator Would Tell Their Past Self
[Honest, specific advice -- not generic]

*Written by [creator] on [date].*

_See SOUL.md for the personality that emerged from this origin._
```

## Example Use Cases

**Enterprise:** A recruitment-screening agent's ORIGIN.md tells how an HR director spent 6 hours per day manually reading resumes and built the first version over a weekend, giving new team members context about why the agent prioritizes fairness checks -- the founder experienced bias in her own job searches.

**Multi-Agent Fleet:** Each agent in a fleet publishes its ORIGIN.md to an internal wiki, creating an institutional record of why each capability exists, what problems motivated it, and what pivotal design decisions were made -- preventing future engineers from unknowingly revisiting abandoned approaches.

**Regulated Industry:** A food-safety inspection agent's ORIGIN.md documents that it was built after a contamination incident that existing tools failed to catch, providing auditors with the rationale behind its unusually conservative detection thresholds and zero-tolerance escalation policy.

## Related Specs

| Spec | Relationship |
|------|-------------|
| GUARDRAILS.md | Runtime safety boundaries |
| LIMITS.md | Hard constraints and safety boundaries |
| SOUL.md | Agent personality and values |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
