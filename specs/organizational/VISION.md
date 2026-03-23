---
spec_name: VISION.md
spec_version: 0.1.0
category: Organizational Identity
domain: visionmd.dev
priority: High
volume: "Vol 10 — Purpose, Identity & Institutional Knowledge"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# VISION.md

**Category:** Organizational Identity
**Domain:** visionmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
The long-horizon picture of what the world looks like 
when this agent or organization has fully succeeded.

The hierarchy of purpose:
```
VISION.md    ← The future we're creating (10+ years)
MISSION.md   ← What we do to get there (present tense)
STRATEGY.md  ← How we're doing it this period (1-3 years)
GOALS.md     ← What we're doing this quarter
```

VISION.md is the answer to "why does any of this matter?"
It's the north star — distant, aspirational, orienting.
It doesn't have to be achievable in a lifetime.
It just has to be worth aiming at.

### Spec

```markdown
---
entity_name: string
version: semver
vision_statement: string   # One sentence max — the headline
created: date
last_revised: date
---

# [Entity Name] — Vision

## Vision Statement
*[One sentence. Present tense as if it has happened.
Ambitious. Specific enough to be meaningful.
Broad enough to endure.]*

**"[Vision statement]"**

---

## The World We're Building Toward

[2-4 paragraphs describing what the world looks like 
when this vision is realized.

Not a product roadmap. Not a strategy document.
The actual world — what's different, what's better,
who benefits, what problems no longer exist.

Written with conviction. This is a declaration, not a plan.]

## Why This Matters
[The problem in the current world that makes this vision necessary.
What is broken, missing, or unjust that this vision corrects?]

## Who Benefits
When this vision is realized, who wins?
- [Beneficiary 1]: [How their world is better]
- [Beneficiary 2]: [How their world is better]
- [Beneficiary 3]: [How their world is better]

## Our Role in This Vision
[This entity is not the only one working toward this vision.
Where do we fit? What's our specific contribution?
What would be missing if we didn't exist?]

## How We'll Know We're Getting There
Leading indicators that the vision is being realized:
- [Indicator 1] — if we see this, we're on track
- [Indicator 2] — if we see this, we're on track

## What Would Change This Vision
The vision could evolve if:
- [Condition 1 — e.g. the problem is solved a different way]
- [Condition 2 — e.g. a larger opportunity emerges]

Vision statements are stable but not permanent.
This one was last revised: [date] because [reason].

---

*"[Vision statement]"*  
*— [Entity name], [year]*
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
