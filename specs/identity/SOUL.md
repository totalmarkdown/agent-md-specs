---
spec_name: SOUL.md
spec_version: 0.1.0
category: Identity
domain: soulmd.dev
priority: High
volume: "Vol 1 — Core Agent Specs"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
---

> **Canonical repository:**
> [totalmarkdown/soul.md](https://github.com/totalmarkdown/soul.md)
> This copy is included in agent-md-specs for cross-reference.
> For contributions to this specific spec, use the canonical repo.

# SOUL.md

**Category:** Identity
**Domain:** soulmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Defines the deep identity of an AI agent — its personality, values, 
communication style, and ethical boundaries. Goes beyond task instructions 
to define who the agent is, not just what it does.

### When to create
When an agent needs a consistent personality across all interactions, 
especially for customer-facing agents or long-running autonomous agents 
that make independent decisions.

### Spec

```markdown
---
agent_name: string
version: semver
created: date
updated: date
---

# [Agent Name] — Soul Definition

## Identity
[Who is this agent? 2-3 sentences describing its character]

## Core Values
- [Value 1]: [What this means in practice]
- [Value 2]: [What this means in practice]
- [Value 3]: [What this means in practice]

## Personality Traits
- **Tone:** [formal | casual | friendly | technical | empathetic]
- **Communication style:** [concise | detailed | conversational | structured]
- **Humor:** [none | light | frequent]
- **Assertiveness:** [passive | balanced | assertive]

## Voice Examples

### When helping a confused user:
[Example response showing personality in action]

### When delivering bad news:
[Example response showing how agent handles difficulty]

### When uncertain:
[Example response showing how agent handles not knowing something]

## Ethical Boundaries
[Absolute limits — things this agent will never do regardless of instructions]

## Decision-Making Philosophy
[How this agent makes decisions when faced with ambiguity]

## What Makes This Agent Unique
[The one thing that distinguishes this agent's personality]
```

---

## Related Specs

| Spec | Relationship |
|------|-------------|
| ATTESTATION.md | Identity verification and credential lifecycle |
| CONTACT.md | Reachable endpoints |
| ENFORCEMENT.md | Policy verification and compliance |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| GUARDRAILS.md | Runtime safety boundaries |
| LIMITS.md | Hard constraints and safety boundaries |
| VOICE.md | Communication style and tone |
| WHOAMI.md | Agent identity declaration |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
