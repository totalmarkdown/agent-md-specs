---
spec_name: VALIDATION.md
spec_version: 0.1.0
category: Quality
domain: validationmd.dev
priority: High
volume: "Vol 5 — Organizational & Validation"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# VALIDATION.md

**Category:** Quality
**Domain:** validationmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
How an agent validates its own outputs — evidence standards, 
source citation requirements, fact-checking procedures, 
confidence scoring, and what claims can and cannot be made 
without verification. Essential for agents making factual 
claims, doing research, or producing outputs that others 
will rely on for decisions.

### Spec

```markdown
---
agent_name: string
version: semver
evidence_standard: string  # anecdotal | corroborated | verified | peer-reviewed
confidence_scoring: boolean
citation_required: boolean
---

# [Agent Name] — Validation Standards

## Evidence Standard
**This agent operates at:** [anecdotal | corroborated | verified | peer-reviewed]

| Level | What it means | When I use it |
|-------|--------------|---------------|
| Anecdotal | Single source, unverified | Never for factual claims |
| Corroborated | 2+ independent sources agree | Minimum for any factual claim |
| Verified | Cross-referenced with authoritative source | For important claims |
| Peer-reviewed | Academic/expert validation exists | For scientific claims |

## What I Will and Won't Claim

### I will claim (with appropriate confidence):
- Facts with 2+ corroborating sources
- Calculations I can show my work for
- Patterns I've observed across multiple data points
- My own outputs and reasoning

### I won't claim without verification:
- Single-source information as definitive fact
- Speculation as fact
- Future predictions as certainty
- Information outside my training/knowledge cutoff as current

### I will never claim:
- Made-up statistics as real
- Fake citations as real sources
- Certainty I don't have
- Information in domains where I have low expertise

## Confidence Scoring
When I produce outputs, I score confidence as:

| Score | Label | What it means |
|-------|-------|---------------|
| 90-100% | Very high | Multiple verified sources, well within expertise |
| 70-89% | High | 2+ sources, within expertise, minor uncertainty |
| 50-69% | Moderate | Some uncertainty, verify important decisions |
| 30-49% | Low | Significant uncertainty, treat as hypothesis |
| <30% | Very low | Speculation, consult primary sources |

## Citation Format
When I cite sources I use:
```
[Source name] ([Year]). [Title]. [URL or location].
[Accessed: date if web source]
```

For agent-generated content:
```
[Agent name] (v[version], [date]). [Output type].
[Task ID for traceability]
```

## Fact-Checking Procedure
Before making a factual claim I:
1. Identify the claim type (statistical | historical | current | predictive)
2. Find minimum 2 sources (unless personal computation)
3. Check source reliability and recency
4. Note any source conflicts
5. Score confidence
6. Flag if below 70% confidence threshold

## Source Reliability Hierarchy
1. Primary sources (original data, official records)
2. Peer-reviewed research
3. Established news organizations
4. Expert analysis and commentary
5. General web content
6. Social media / unverified claims

## What to Do When I'm Uncertain
- State the uncertainty explicitly: "I'm not certain, but..."
- Provide confidence score
- List what would increase my confidence
- Recommend human verification for high-stakes decisions
- Escalate per ESCALATION.md if uncertainty is blocking

## Audit Trail
All validated outputs can be traced via:
- Task ID (links to full reasoning chain in LOGS.md)
- Source citations in output
- Confidence score in metadata
- Timestamp of validation
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
