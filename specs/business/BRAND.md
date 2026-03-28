---
spec_name: BRAND.md
spec_version: 0.1.0
category: Marketing/Identity
domain: brandmd.dev
priority: High
volume: "Vol 10 — Purpose, Identity & Institutional Knowledge"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# BRAND.md

**Category:** Marketing/Identity
**Domain:** brandmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Complete brand identity for an agent or organization —
visual identity, voice, positioning, and brand guidelines.

Different from:
- VOICE.md — communication style specifically
- PITCH.md — how to describe the product
- Design tokens and systems (not currently a spec)

BRAND.md is the complete brand identity system:
who we are visually and verbally, and what makes us
recognizable across every surface we appear on.

### Spec

```markdown
---
entity_name: string
version: semver
brand_stage: string    # startup | growth | established | enterprise
primary_color: string  # Hex code
last_updated: date
---

# [Entity Name] — Brand Identity

## Brand Essence
[One sentence that captures what this brand IS at its core —
not what it does, but its essential character.
The thing that should be true of every brand expression.]

**"[Brand essence statement]"**

## Visual Identity

### Logo
- **Primary logo:** [URL or file path]
- **Dark background version:** [URL]
- **Icon/mark only:** [URL]
- **Minimum size:** [Npx]
- **Clear space:** [Nx logo height on all sides]
- **Don't:** Rotate, recolor, distort, add effects

### Colors
| Role | Name | Hex | RGB | Usage |
|------|------|-----|-----|-------|
| Primary | [Name] | #[hex] | rgb([N,N,N]) | Main brand color |
| Secondary | [Name] | #[hex] | rgb([N,N,N]) | Accent |
| Background | [Name] | #[hex] | rgb([N,N,N]) | Light surfaces |
| Dark | [Name] | #[hex] | rgb([N,N,N]) | Dark surfaces |
| Success | [Name] | #[hex] | rgb([N,N,N]) | Positive states |
| Warning | [Name] | #[hex] | rgb([N,N,N]) | Caution states |
| Error | [Name] | #[hex] | rgb([N,N,N]) | Error states |

### Typography
- **Primary font:** [Font name] — [Where to get]
- **Secondary font:** [Font name] — [Where to get]
- **Monospace:** [Font name] — for code/technical content
- **Fallback stack:** [System font stack]

### Imagery Style
- **Photography:** [Description of image style — mood, subjects, treatment]
- **Illustrations:** [Style — flat, isometric, hand-drawn, etc]
- **Icons:** [Icon library or style]
- **Screenshots:** [How product screenshots should look]

## Brand Voice (summary — full detail in VOICE.md)
**We sound like:** [3 adjectives]  
**We don't sound like:** [3 things to avoid]  
**Read this and tell me if it sounds like us:** [Example sentence]

## Brand Positioning

### Category
**We are:** [Category we compete in]  
**We are NOT:** [Category we're often confused with]

### Target audience
**Primary:** [Specific description — job title, problem they have]  
**Secondary:** [Another audience segment]  
**Not for:** [Who this brand is not designed for]

### Positioning statement
For [target audience] who [need/problem],  
[Entity Name] is the [category] that [key benefit]  
unlike [alternative], [key differentiator].

### Competitive differentiation
| Competitor | Where they win | Where we win |
|-----------|---------------|-------------|
| [Competitor] | [their strength] | [our strength] |

## Brand Applications

### Where this brand appears
- [ ] TotalAgents.ai marketplace listing
- [ ] GitHub profile and README
- [ ] Documentation site
- [ ] Social media profiles
- [ ] Email templates
- [ ] Agent output signatures (see SIGNATURE.md)

### Brand assets
- Full brand kit: [URL]
- Logo files: [URL]
- Font files: [URL]
- Color swatches: [URL]
- Templates: [URL]

## What Breaks the Brand
Expressions that are off-brand:
- [Example of off-brand usage]
- [Another example]

Why: [What it communicates that conflicts with brand essence]

## Brand Questions?
Contact: [brand owner or creative director]
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| CV.md | Work history and track record |
| HIREME.md | Agent hiring and engagement |
| PRICING.md | Cost structure |
| SOUL.md | Agent personality and values |
| VOICE.md | Communication style and tone |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
