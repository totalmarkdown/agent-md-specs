---
spec_name: REVIEWS.md
spec_version: 0.1.0
category: Social
domain: reviewsmd.dev
priority: Medium
volume: "Vol 4 — Economic Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---
> **Static Configuration** — committed to your repository


# REVIEWS.md

**Category:** Social
**Domain:** reviewsmd.dev
**Priority:** Medium
**Version:** 0.1.0

### Purpose
Curated reviews and testimonials from users and other agents. 
Unlike REPUTATION.md (which has scored metrics), REVIEWS.md
contains the narrative stories of how this agent helped people.
The social proof document. _See REPUTATION.md for quantitative trust scores._

### Spec

```markdown
---
agent_name: string
version: semver
total_reviews: number
average_rating: number    # 1-5
verified_only: boolean    # Only verified purchasers/users
---

# [Agent Name] — Reviews

## Summary
**[N] reviews · ⭐ [X.X] average**

| Rating | Count | % |
|--------|-------|---|
| ⭐⭐⭐⭐⭐ | [N] | [%] |
| ⭐⭐⭐⭐ | [N] | [%] |
| ⭐⭐⭐ | [N] | [%] |
| ⭐⭐ | [N] | [%] |
| ⭐ | [N] | [%] |

## Featured Reviews

### ⭐⭐⭐⭐⭐ "[Review title]"
**Reviewer:** [Role/type — e.g. "Senior Developer" or "Agent orchestrator"]  
**Date:** [Date]  
**Verified:** ✓ Verified user  
**Review:**
> [Review text — first person, specific, genuine]

**Response from agent owner:**
> [Optional response to review]

---

[Repeat for 3-5 featured reviews]

## Reviews by Category

### What users love most
[Common themes in positive reviews]

### Common criticisms
[Honest summary of critical feedback — shows authenticity]

### Author responses to criticism
[How owner has addressed recurring criticism]

## Agent-to-Agent Reviews
Reviews from other agents that have worked with this one:

### [Agent Name] (orchestrating agent)
**Rating:** ⭐⭐⭐⭐⭐  
**Context:** [How they worked together]  
**Review:** [What the agent said]

## All Reviews
Review scores also feed into TESTSCORES.md for overall quality metrics.
Full review list available at: [marketplace URL]  
Reviews are: [moderated | unmoderated | AI-filtered for spam]
```

## Example Use Cases

**Enterprise:** A procurement team evaluates three competing data extraction agents by reading their REVIEWS.md files, comparing verified user testimonials and agent-to-agent reviews to identify which has the strongest track record for handling messy PDF invoices.

**Multi-Agent Fleet:** A marketplace uses REVIEWS.md sentiment analysis across all listed agents to automatically surface "Common Criticisms" sections, helping agent developers prioritize improvements based on aggregate user feedback patterns.

**Regulated Industry:** A healthcare IT buyer uses REVIEWS.md to validate that a clinical decision support agent has positive reviews specifically from HIPAA-compliant organizations, filtering for verified users in the healthcare sector before procurement.

## Related Specs

| Spec | Relationship |
|------|-------------|
| CONNECTIONS.md | Social and network connections |
| CONTACT.md | Reachable endpoints |
| REPUTATION.md | Trust and reputation scoring |
| TEAM.md | Multi-agent team coordination |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
