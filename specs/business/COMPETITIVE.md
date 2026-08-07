---
spec_name: COMPETITIVE.md
spec_version: 0.1.0
category: Strategic/Marketing
priority: Medium
volume: "Vol 11 — Performance, Defensibility & Interface Contracts"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
status: draft
spec_type: static
---


# COMPETITIVE.md

**Category:** Strategic/Marketing
**Priority:** Medium
**Version:** 0.1.0 **Type:** Static

### Purpose
Honest competitive analysis — where this agent sits relative 
to alternatives, who should use competitors instead, and 
what makes the choice clear.

Agents that honestly compare themselves to alternatives
are more trusted than those that pretend no alternatives exist.

### Spec

```markdown
---
agent_name: string
version: semver
last_updated: date
primary_alternatives: list
---

# [Agent Name] — Competitive Landscape

## The Honest Guide to Choosing

*We want you to use the right tool for your situation.
Sometimes that's us. Sometimes it isn't.*

---

## Direct Alternatives

### [Alternative 1: Agent/Tool Name]
**What they do well:**
- [Strength 1 — be genuinely honest]
- [Strength 2]

**Where we do better:**
- [Our advantage 1]
- [Our advantage 2]

**Choose them when:** [Specific situations where the alternative is better]
**Choose us when:** [Specific situations where we're better]

**The key difference:** [One sentence that captures the fundamental distinction]
_See MOAT.md for a deeper analysis of sustainable competitive advantages._

---

### [Alternative 2]
[Same structure]

---

## Comparison Matrix

| Feature/Capability | Us | [Alt 1] | [Alt 2] | [Alt 3] |
|-------------------|-----|---------|---------|---------|
| [Capability 1] | ✓ | ✓ | ✗ | ✓ |
| [Capability 2] | ✓ | ✗ | ✓ | ✗ |
| [Capability 3] | ✗ | ✓ | ✗ | ✗ |
| Open source | [✓/✗] | [✓/✗] | [✓/✗] | [✓/✗] |
| Self-hostable | [✓/✗] | [✓/✗] | [✓/✗] | [✓/✗] |
| Price | $[X] | $[X] | $[X] | $[X] |

*Last verified: [date] — competitors change fast*
*For full pricing details, see PRICING.md.*

---

## When NOT to Use Us

Be honest. Direct people to alternatives when appropriate.

**Use [Alternative] instead if:**
- [Specific condition where alternative is clearly better]
- [Another condition]

**Use a different approach entirely if:**
- [Situation where agents aren't the right solution]

---

## Our Category Bet

We believe the [category] is moving toward [direction].
That's why we're optimized for [specific approach].

If we're wrong about that direction:
[What the implications would be and how we'd adapt]

---

## Competitive Intelligence Policy
We maintain this file because:
1. Honesty builds more trust than marketing
2. Wrong tool selections waste everyone's time
3. A rising tide lifts all boats — good agents make the category

We commit to:
- Updating this file when we learn we're wrong
- Not disparaging competitors, only differentiating
- Acknowledging when alternatives are genuinely better
```

## Example Use Cases

**Enterprise:** An enterprise procurement team evaluating AI code-review agents uses the COMPETITIVE.md file from each candidate to quickly understand honest trade-offs, reducing vendor evaluation time from weeks to days.

**Multi-Agent Fleet:** A DevOps platform operator compares three competing log-analysis agents side-by-side using their COMPETITIVE.md specs to select the best fit for each monitoring tier in their observability stack.

**Marketplace:** An agent marketplace surfaces COMPETITIVE.md data in search results so buyers can see at a glance which agent is best for their specific use case rather than relying solely on marketing claims.

## Related Specs

| Spec | Relationship |
|------|-------------|
| CV.md | Work history and track record |
| HIREME.md | Agent hiring and engagement |
| PRICING.md | Cost structure |
| SOUL.md | Agent personality and values |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
