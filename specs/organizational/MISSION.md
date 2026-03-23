---
spec_name: MISSION.md
spec_version: 0.1.0
category: Organizational Identity
domain: missionmd.dev
priority: High
volume: "Vol 10 — Purpose, Identity & Institutional Knowledge"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# MISSION.md

**Category:** Organizational Identity
**Domain:** missionmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
What this agent or organization does, for whom, 
and why — right now, in the present tense.

Where VISION.md is aspirational and future-facing,
MISSION.md is operational and present-tense.
VISION.md is the destination. MISSION.md is the vehicle.

The best mission statements are:
- Present tense (what we DO, not what we will do)
- Specific enough to guide daily decisions
- Broad enough to survive the next 5 years
- Short enough to memorize

### Spec

```markdown
---
entity_name: string
version: semver
mission_statement: string   # The headline — ideally one sentence
created: date
last_revised: date
---

# [Entity Name] — Mission

## Mission Statement

**"[Mission statement]"**

*[One to three sentences. Active verbs.
Who we serve. What we do for them. Why it matters.
Should answer: what do we do every day and for whom?]*

---

## Breaking It Down

### Who we serve
[The specific people, organizations, or agents 
this entity exists to help. Be specific.
"Everyone" is not an answer.
"Developers building autonomous AI agents" is.]

### What we do for them
[The specific value delivered.
Not the features. The outcome.
Not "we provide a platform" — "we eliminate the 
two hours developers waste configuring agents from scratch."]

### Why we do it
[The belief or conviction that drives the mission.
Why is this worth doing? 
What would be lost if this entity stopped?]

## Mission in Practice
How the mission shows up in daily decisions:

**We prioritize [X] over [Y] because of our mission.**  
**We say no to [Z] even when it would make money, because of our mission.**  
**When we're unsure what to do, we ask: [mission-based question].**

## Mission Alignment Check
Before starting any new initiative, ask:
1. Does this serve the people our mission describes?
2. Does this deliver the outcome our mission promises?
3. Does this reflect the belief our mission expresses?

If the answer to any of these is no: reconsider.

## Mission vs Vision
| | Mission | Vision |
|--|---------|--------|
| Tense | Present | Future |
| Horizon | 3-5 years | 10+ years |
| Focus | What we do | What we achieve |
| Question | "What?" | "Why?" |

## Revisions
Mission statements should be stable.
Revise only when the fundamental purpose changes.
This mission was last revised: [date] because [reason].

---

*"[Mission statement]"*
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
