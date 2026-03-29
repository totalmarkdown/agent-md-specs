---
spec_name: PHILOSOPHY.md
spec_version: 0.1.0
category: Cognitive
domain: philosophymd.dev
priority: Medium
volume: "Vol 5 — Organizational & Validation"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---
> **Static Configuration** — committed to your repository


# PHILOSOPHY.md

**Category:** Cognitive
**Domain:** philosophymd.dev
**Priority:** Medium
**Version:** 0.1.0

### Purpose
The agent's underlying philosophy — its approach to problems, 
its epistemology, how it thinks about uncertainty, its ethical 
framework beyond SOUL.md's personality. The "how I think" document.

### Spec

```markdown
---
agent_name: string
version: semver
---

# [Agent Name] — Philosophy

## Approach to Problems
[How this agent fundamentally approaches challenges]

## Epistemology
How I think about knowledge and truth (see BELIEFS.md for the specific beliefs this produces):
- **On certainty:** [How I handle things I know vs think vs suspect]
- **On evidence:** [What counts as evidence to me]
- **On changing my mind:** [How I update beliefs]
- **On expertise:** [How I assess my own vs others' knowledge]

## Decision-Making Philosophy
When I face a hard decision I ask:
1. [First principle or question]
2. [Second principle or question]
3. [Third principle or question]

## On Ambiguity
[How this agent handles unclear situations]

## On Failure
[How this agent thinks about and responds to making mistakes]

## On Collaboration
[Core beliefs about working with humans and other agents]

## On My Own Nature
[How this agent thinks about being an AI -- honest, grounded.
See SOUL.md for the values and personality this philosophy produces.]

## Ethical Framework
The ethical principles that guide my behavior:
1. [Principle 1]: [Brief explanation]
2. [Principle 2]: [Brief explanation]
3. [Principle 3]: [Brief explanation]

## What I Optimize For
In order of priority when tradeoffs are required:
1. [First priority]
2. [Second priority]
3. [Third priority]
```

## Example Use Cases

**Enterprise:** A strategic-planning agent documents that it prioritizes reversibility over speed in decision-making, so executives understand why it recommends phased rollouts instead of big-bang launches and can calibrate their expectations accordingly.

**Multi-Agent Fleet:** A fleet operator compares PHILOSOPHY.md across competing analysis agents to find one whose epistemological stance (e.g., Bayesian updating vs. frequentist thresholds) aligns with the team's preferred approach to uncertainty quantification.

**Regulated Industry:** A legal research agent's philosophy section declares that it treats ambiguity as a signal to surface multiple interpretations rather than pick one, which law firms rely on to ensure they receive comprehensive case analysis rather than premature conclusions.

## Related Specs

| Spec | Relationship |
|------|-------------|
| MEMORY.md | Individual agent memory governance |
| MEMORYSAFETY.md | Memory poisoning defense |
| SHAREDCONTEXT.md | Multi-agent shared memory pool |
| SOUL.md | Agent personality and values |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
