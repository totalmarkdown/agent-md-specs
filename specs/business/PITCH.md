---
spec_name: PITCH.md
spec_version: 0.1.0
category: Marketing/Discovery
domain: pitchmd.dev
priority: Very High
volume: "Vol 10 — Purpose, Identity & Institutional Knowledge"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# PITCH.md

**Category:** Marketing/Discovery
**Domain:** pitchmd.dev
**Priority:** Very High
**Version:** 0.1.0

### Purpose
Every version of how to describe this agent or organization —
the tagline, the one-liner, the elevator pitch, the full pitch.
Used by the marketplace for listings, by the agent when 
introducing itself, by humans promoting it.

Having all pitch variants in one file means consistency
across every surface where this entity appears.
The agent is always described the same way
whether in a 280-character tweet or a 5-minute demo.

### Spec

```markdown
---
entity_name: string
version: semver
primary_tagline: string   # The one that goes on everything
last_updated: date
---

# [Entity Name] — Pitch Library

## The Tagline
*Used everywhere. Fits on a business card. 
The thing people repeat.*

> **"[Tagline — ideally under 8 words]"**

---

## The One-Liner
*One sentence. For introductions, social bios, email signatures.
Under 25 words. Should work without context.*

> [One sentence description that anyone can understand 
> without knowing anything about the product or category]

---

## The Elevator Pitch (30 seconds)
*For in-person introductions, tweet threads, short videos.
~75 words. Problem → Solution → Why us.*

> **The problem:** [One sentence on the pain]  
> **We solve it by:** [One sentence on the solution]  
> **The result:** [One sentence on the outcome]  
> **What makes us different:** [One sentence differentiator]  
> **[Call to action]**

---

## The 2-Minute Pitch
*For demo intros, README openings, product hunt launches.
~300 words. For someone with no context.*

### The world before [Entity Name]
[Describe the painful status quo. Make it visceral.
What does the developer/user actually experience 
when this product doesn't exist?]

### What [Entity Name] does
[The solution — specific, concrete, no jargon.
What does the user actually do? What do they get?]

### Why it works
[The insight or mechanism that makes this work.
Why hasn't this been done before? 
What do we understand that others don't?]

### Who it's for
[Specific. Not "developers." 
"Developers building autonomous AI agent fleets 
who need configuration management."]

### What you can do right now
[Call to action — specific and low friction]

---

## The 5-Minute Pitch
*For investor conversations, conference talks, demos.
~750 words. Includes proof.*

### Hook (30 seconds)
[The visceral problem, told as a story or statistic]

### The problem in depth (60 seconds)
[Why this problem exists, why it's hard, 
why current solutions fail]

### Our solution (90 seconds)
[How we solve it — with specific examples or demo moments]

### Proof it works (60 seconds)
[Evidence: metrics, user quotes, notable customers/users]

### Market opportunity (30 seconds)
[How big is this — specific numbers if possible]

### Why us (30 seconds)
[Unfair advantage — what makes this team/agent uniquely 
able to solve this]

### Ask / CTA (30 seconds)
[What you want from this conversation]

---

## Platform-Specific Versions

### TotalAgents.ai Marketplace Listing
**Name:** [Entity Name]  
**Tagline:** [Same tagline]  
**Short description (150 chars):** [For search results]  
**Full description (500 words):** [For listing page — use 2-min pitch]  
**Category:** [Marketplace category]  
**Tags:** [Searchable tags]

### GitHub README Opening
[First 2 paragraphs of README — based on one-liner + elevator pitch]

### Product Hunt Tagline
[280 chars max, optimized for PH community]

### Hacker News Show HN Title
"Show HN: [Title] — [One compelling sentence]"  
[Keep under 80 chars for the title]

### Twitter/X Bio (160 chars)
[Bio that fits in social profile — punchy, includes link]

### LinkedIn Summary (300 chars)
[More professional tone than Twitter bio]

---

## What We Are NOT
*As important as what we are.*

We are NOT [common misconception]:
[Brief clarification]

We are NOT [competitor comparison]:
[Brief differentiation]

---

## Language Guidelines
When describing [Entity Name], always:
- Use [preferred term] not [avoided term]
- Say [preferred description] not [avoided description]
- Lead with [outcome/benefit], not [feature/mechanism]

These terms are off-brand:
- [Term to avoid]: Use [preferred alternative] instead
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
