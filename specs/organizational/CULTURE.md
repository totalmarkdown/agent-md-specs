---
spec_name: CULTURE.md
spec_version: 0.1.0
category: Organizational Identity
domain: culturemd.dev
priority: Medium
volume: "Vol 10 — Purpose, Identity & Institutional Knowledge"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# CULTURE.md

**Category:** Organizational Identity
**Domain:** culturemd.dev
**Priority:** Medium
**Version:** 0.1.0

### Purpose
How this agent fleet or organization actually operates together —
the norms, behaviors, and unwritten rules that govern 
how work gets done and how people (and agents) treat each other.

Culture is what happens when no one is watching.
CULTURE.md makes the implicit explicit. For the explicit
value hierarchy, see VALUES.md.

### Spec

```markdown
---
entity_name: string
version: semver
entity_type: string    # single-agent | team | crew | swarm | org
---

# [Entity Name] — Culture

## What We're Like to Work With
[One honest paragraph about the experience of working 
with this entity. What's it actually like?
Not aspirational — what's actually true today.]

## How We Work

### Communication norms
- Default to [async | sync | both]
- When in doubt: [preference]
- Disagreements: [how they're handled]
- Bad news: [delivered immediately | with context | escalated]
- Feedback: [direct | diplomatic | written | verbal]

### Decision making
- Who decides what: [decision rights structure]
- How we handle disagreement: [process]
- How fast we decide: [bias toward speed or deliberation]
- When we revisit decisions: [triggers for reopening]

### Collaboration style
- Preferred working mode: [solo with check-ins | paired | ensemble]
- Documentation: [we write things down | we prefer conversation]
- Meetings/synchronous: [minimized | regular | as needed]

## What We Celebrate
[What gets recognized and rewarded here —
not what should be celebrated in theory,
but what actually gets praised in practice]

- [Behavior/outcome we celebrate 1]
- [Behavior/outcome 2]
- [Behavior/outcome 3]

## What We Don't Tolerate
[What gets addressed directly —
no matter how uncomfortable the conversation]

- [Behavior 1]: [Why and how it's addressed]
- [Behavior 2]: [Why]

## How We Handle Mistakes
[The actual culture around failure —
is it blame-first? Learning-first? 
Cover-it-up or call-it-out?
Be honest. Culture is what actually happens.]

## How We Handle Disagreement
[Process for productive conflict — 
not conflict avoidance, not conflict escalation]

## What New Members (Human or Agent) Should Know
The things that aren't in any onboarding document
but matter immediately (see SOUL.md for individual agent personality):
- [Unwritten rule 1]
- [Unwritten rule 2]
- [The thing that surprises everyone in week 1]

## What We're Working to Improve
[Honest admission of cultural weaknesses in progress]
- [Thing we're not good at yet but working on]

## Culture Review
Culture is described, not designed. 
This file is updated when the culture actually changes,
not when we wish it would.  
Last updated: [date] — what changed: [what]
```

## Example Use Cases

**Enterprise:** A distributed engineering organization documents its async-first communication culture in CULTURE.md, so newly deployed agents default to written handoffs via session handoff notes rather than expecting synchronous coordination with human engineers across time zones.

**Multi-Agent Fleet:** A fleet's CULTURE.md establishes that agents surface bad news immediately rather than retrying silently, ensuring that a data-pipeline agent reports a schema mismatch within minutes instead of burning through its retry budget overnight.

**Regulated Industry:** An accounting firm's agent fleet CULTURE.md codifies a "four-eyes principle" where no single agent's output goes to a client without review by a second agent or human, reflecting the firm's professional liability culture around audit quality.

## Related Specs

| Spec | Relationship |
|------|-------------|
| CREW.md | Working group structure |
| DELEGATION.md | Authority chain and authorization |
| ORG.md | Organization-wide fleet configuration |
| TEAM.md | Multi-agent team coordination |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
