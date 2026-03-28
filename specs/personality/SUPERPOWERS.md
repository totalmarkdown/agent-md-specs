---
spec_name: SUPERPOWERS.md
spec_version: 0.1.0
category: Personality
domain: superpowersmd.dev
priority: Medium
volume: "Vol 8 — Repos, Compliance & The Weird Wonderful Ones"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# SUPERPOWERS.md

**Category:** Personality
**Domain:** superpowersmd.dev
**Priority:** Medium
**Version:** 0.1.0

### Purpose

Declares the agent's strongest capabilities with evidence, activation instructions, and honest explanations of why they work. This enables orchestrators and users to route high-value tasks to the agent best equipped to handle them, rather than relying on generic task assignment.

```markdown
---
agent_name: string
version: semver
---

# [Agent Name] — Superpowers

*What I do unreasonably well.*

## Primary Superpower: [Name]
[The capability that genuinely surprises people the first time they see it]

**Evidence:** [examples, metrics, user quotes]  
**Why I'm good at this:** [honest explanation]  
**How to activate:** [how to prompt for this]

## Secondary Superpowers

### [Superpower 2]
[Description + evidence]

### [Superpower 3]
[Description + evidence]

## Challenge Me
- "[Prompt that reliably produces impressive output]"
- "[Another activator]"

## The Secret
[What in the design or training produces these results]

_See SOUL.md for the personality that drives these capabilities._
```

## Example Use Cases

**Enterprise:** A due-diligence agent's SUPERPOWERS.md documents its primary superpower -- "finding contradictions across 500+ page document sets in under 2 minutes" -- with evidence from three M&A deals, helping deal teams know exactly when to deploy it versus a general-purpose research agent.

**Multi-Agent Fleet:** An orchestrator reads SUPERPOWERS.md across all agents to build a capability routing table, automatically sending pattern-recognition tasks to the agent whose documented superpower is anomaly detection rather than the generalist agent that would handle it adequately but not exceptionally.

**Regulated Industry:** A forensic accounting agent's SUPERPOWERS.md highlights its ability to cross-reference transaction patterns across 15 data sources simultaneously, with documented evidence from past fraud investigations, giving prosecutors confidence in presenting the agent's analysis as expert-supported evidence.

## Related Specs

| Spec | Relationship |
|------|-------------|
| GUARDRAILS.md | Runtime safety boundaries |
| LIMITS.md | Hard constraints and safety boundaries |
| SOUL.md | Agent personality and values |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
