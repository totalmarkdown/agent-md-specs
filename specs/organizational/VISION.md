---
spec_name: VISION.md
spec_version: 0.1.0
category: Organizational Identity
priority: High
volume: "Vol 10 — Purpose, Identity & Institutional Knowledge"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---


# VISION.md

**Category:** Organizational Identity
**Priority:** High
**Version:** 0.1.0 **Type:** Static

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
It's the north star -- distant, aspirational, orienting.
It doesn't have to be achievable in a lifetime.
It just has to be worth aiming at. For the present-tense
vehicle that drives toward this vision, see MISSION.md.

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
Leading indicators that the vision is being realized (see NORTHSTAR.md for the primary metric):
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

## Example Use Cases

**Enterprise:** A logistics company's VISION.md declares "A world where no package is ever lost or delayed," giving its 30 route-optimization and tracking agents a shared aspirational anchor that informs daily tradeoffs between cost and delivery reliability.

**Multi-Agent Fleet:** A developer-tools fleet publishes its vision -- "Every developer ships production-quality code on their first day" -- and uses the vision alignment check to evaluate whether proposed new agent capabilities serve that future state or are tangential.

**Regulated Industry:** A renewable energy company's grid-management agent fleet operates under the vision "A power grid that is 100% renewable and 100% reliable," with leading indicators in NORTHSTAR.md tracking the percentage of renewable energy dispatched without outages.

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
