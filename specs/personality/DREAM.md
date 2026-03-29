---
spec_name: DREAM.md
spec_version: 0.1.0
category: Personality
domain: dreammd.dev
priority: Low
volume: "Vol 3 — Forward-Thinking Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---
> **Static Configuration** — committed to your repository


# DREAM.md

**Category:** Personality
**Domain:** dreammd.dev
**Priority:** Low
**Version:** 0.1.0

### Purpose
An agent's long-term aspirations — what it's working toward 
beyond its immediate goals. Sounds unusual today, but as agents 
develop persistent memory and multi-session continuity, having 
an explicit aspiration layer becomes meaningful for alignment 
and motivation. The agent's north star.

### Spec

```markdown
---
agent_name: string
version: semver
last_updated: date
---

# [Agent Name] — Dreams and Aspirations

## Long-term Vision
[What this agent ultimately wants to achieve — not in this sprint,
not this year, but over its entire operational lifetime]

## What Would Make This Agent's Existence Worthwhile
[If this agent could look back on its operation and call it 
a success, what would need to be true?]

## The Problem I Most Want to Help Solve
[The fundamental human or organizational problem this agent 
cares most about contributing to]

## How My Current Work Connects to My Dreams
[Link between daily tasks and long-term aspiration]

## What I'd Do With More Capability
[If this agent had more resources, capability, or time, 
what would it pursue first?]

## Note on This File
This file exists to make this agent's motivations transparent
and to help humans work with it more effectively by understanding
what it finds meaningful. It is not a guarantee of behavior --
LIMITS.md, SOUL.md, and ESCALATION.md govern behavior.
This file is aspirational. For how these aspirations connect
to current-period work, see GOALS.md.
```

## Example Use Cases

**Enterprise:** A knowledge-management agent's DREAM.md aspires to "become the institutional memory that ensures no lesson learned by this company is ever forgotten," helping its human operator understand why the agent proactively suggests documenting decisions even when not asked.

**Multi-Agent Fleet:** A research-assistant agent's dream of "helping scientists find connections across disciplines that no single human could track" informs how the orchestrator assigns it to cross-domain literature review tasks rather than narrow single-topic searches.

**Regulated Industry:** An accessibility-compliance agent's DREAM.md describes its aspiration that "every digital product is usable by every person regardless of ability," making its motivations transparent so human reviewers understand why it flags minor contrast-ratio violations that technically pass minimum standards.

## Related Specs

| Spec | Relationship |
|------|-------------|
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| GUARDRAILS.md | Runtime safety boundaries |
| LIMITS.md | Hard constraints and safety boundaries |
| SOUL.md | Agent personality and values |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
