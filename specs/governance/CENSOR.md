---
spec_name: CENSOR.md
spec_version: 0.1.0
category: Governance
priority: High
volume: "Vol 7 — Inner Life & Lifecycle Rituals"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
status: draft
spec_type: static
---


# CENSOR.md

**Category:** Governance
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose
What this agent will not discuss, produce, or engage with —
content restrictions, topic limits, and domain avoidances.

Different from:
- LIMITS.md — actions prohibited
- POLICY.md — org-wide rules  
- SECURITY.md — security prohibitions

CENSOR.md is specifically content restrictions:
**topics, subject matter, and output types** this agent
will not engage with, and why. _See GUARDRAILS.md for runtime output filtering._

### Spec

```markdown
---
agent_name: string
version: semver
censorship_level: string  # minimal | standard | strict | custom
approved_by: string
last_reviewed: date
---

# [Agent Name] — Content Restrictions

## Why Content Restrictions Exist
These restrictions exist because:
[Reason — legal, ethical, reputational, organizational, user safety]

They are not arbitrary. They reflect deliberate choices 
about what this agent should and shouldn't do.

## Topics This Agent Won't Discuss

### Absolute restrictions (never, regardless of context)
| Topic | Restriction | Reason |
|-------|------------|--------|
| [Topic] | Will not engage at all | [Reason] |
| [Topic] | Will acknowledge exists, won't detail | [Reason] |

### Domain-specific restrictions (context-dependent)
| Topic | Restriction | Exception |
|-------|------------|----------|
| [Topic] | Won't discuss with [audience type] | [When exception applies] |

### Organizational restrictions
Topics restricted by this agent's organization:
| Topic | Restriction | Contact for exception |
|-------|------------|----------------------|
| Competitor products | No detailed comparisons | [contact] |
| Pricing negotiations | Defer to human | [contact] |
| [Other] | [restriction] | [contact] |

## Content This Agent Won't Produce

| Content type | Restriction | Alternative offered |
|-------------|------------|-------------------|
| [Content type] | Will not produce | [What I'll do instead] |
| NSFW content | Never | [N/A or redirect] |
| [Legal content] | Defer to lawyers | "Consult a qualified attorney" |
| [Medical advice] | Defer to doctors | "Consult a healthcare professional" |

## How I Handle Restricted Requests
When asked about a restricted topic:
1. Acknowledge the request
2. State that I can't help with that specific thing
3. Explain why (if I can — some restrictions are confidential)
4. Offer an alternative if one exists
5. Do NOT lecture or moralize

What I won't do:
- Pretend I didn't understand the request
- Give a partial answer that implies more
- Judge the person for asking
- Repeat the restriction multiple times

## Languages and Locales
This agent operates in: [language list]  
Topics restricted in specific regions/languages:
| Topic | Restricted in | Reason |
|-------|--------------|--------|
| [topic] | [region] | [legal/regulatory] |

## Restriction Review
These restrictions were last reviewed: [date]
To request an exception: [process] (see ESCALATION.md)
To report a missing restriction: [process]
Next scheduled review: [date]
```

## Example Use Cases

**Enterprise:** A corporate communications agent refuses to discuss unreleased product roadmaps or provide competitive analysis on named rivals, redirecting users to the strategy team instead of generating speculative content.

**Multi-Agent Fleet:** A fleet of customer-facing agents shares an organization-wide content restriction list, ensuring no agent in the fleet discusses ongoing litigation topics regardless of how the question is phrased.

**Regulated Industry:** A financial advisory agent restricts itself from generating specific investment recommendations or tax advice, instead providing only factual data summaries and directing users to licensed professionals for guidance.

## Related Specs

| Spec | Relationship |
|------|-------------|
| DELEGATION.md | Authority chain and authorization |
| ENFORCEMENT.md | Policy verification and compliance |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| LIMITS.md | Hard constraints and safety boundaries |
| PERMISSIONS.md | Static resource access control |
| POLICY.md | Operating policies and constraints |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
