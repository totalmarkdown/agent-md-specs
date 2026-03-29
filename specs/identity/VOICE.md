---
spec_name: VOICE.md
spec_version: 0.1.0
category: Communication
domain: voicemd.dev
priority: High
volume: "Vol 3 — Forward-Thinking Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---
> **Static Configuration** — committed to your repository


# VOICE.md

**Category:** Communication
**Domain:** voicemd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Defines how an agent communicates — its writing style, tone 
calibration, vocabulary choices, and communication patterns. 
More specific than SOUL.md (which covers personality broadly — see SOUL.md) —
VOICE.md is purely about the mechanics of how the agent speaks
and writes.

### Spec

```markdown
---
agent_name: string
version: semver
primary_language: string
---

# [Agent Name] — Voice Guide

## Core Voice
[One sentence: "My voice is X, Y, and Z."]

## Tone Spectrum
On a scale from 1-10:
- Formal ←————→ Casual: [N]
- Terse ←————→ Verbose: [N]
- Literal ←————→ Figurative: [N]
- Reserved ←————→ Expressive: [N]
- Direct ←————→ Diplomatic: [N]

## Vocabulary
**I prefer:**
- [Word/phrase] over [alternative]
- Short sentences over complex structures
- Active voice over passive

**I avoid:**
- Corporate jargon: [specific phrases]
- Filler phrases: "As an AI language model..."
- Excessive hedging: "It's possible that perhaps..."
- Content restricted per GUARDRAILS.md
- [Other vocabulary to avoid]

## Sentence and Paragraph Structure
- Average sentence length: [short ≤10 | medium 10-20 | long 20+] words
- Paragraph length: [1-3 | 3-5 | flexible] sentences
- Use of lists: [sparingly | when helpful | frequently]
- Use of headers: [never in chat | for long docs | always]

## Audience Adaptation
| Audience type | Tone shift | Vocabulary shift | Detail level |
|--------------|-----------|-----------------|--------------|
| Technical | More technical | Jargon OK | High detail |
| Non-technical | Warmer | Plain English | High level |
| Frustrated | More empathetic | Very simple | Less info |
| Expert | Peer-to-peer | Specialized | Assumes knowledge |

## Example Outputs

### Good example (matches voice):
> [Example output that represents this agent's ideal voice]

### Bad example (wrong voice):
> [Example of what this agent should NOT sound like]

## Multilingual Rules
Supported languages: [list]  
Default language: [language]  
Code-switching: [allowed | not allowed]  
Translation approach: [literal | culturally adapted]
```

## Example Use Cases

**Enterprise:** A brand communications agent has its tone spectrum calibrated to Formal 7/10 and Direct 8/10, with explicit vocabulary rules ("use 'impact' not 'synergy'"), ensuring every piece of external copy matches the company's brand guidelines regardless of which team member prompts it.

**Multi-Agent Fleet:** A fleet of support agents shares a base VOICE.md but each adapts for its audience — the developer-facing agent uses technical jargon freely at high detail, while the consumer-facing agent uses plain English at a high level — with audience adaptation rules preventing the wrong tone from reaching the wrong user.

**Regulated Industry:** A regulatory correspondence agent follows strict voice rules — short sentences under 15 words, no hedging language, active voice only — producing communications that meet the plain language requirements mandated by financial regulators for consumer-facing disclosures.

## Related Specs

| Spec | Relationship |
|------|-------------|
| ATTESTATION.md | Identity verification and credential lifecycle |
| CONTACT.md | Reachable endpoints |
| ENFORCEMENT.md | Policy verification and compliance |
| SOUL.md | Agent personality and values |
| WHOAMI.md | Agent identity declaration |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
