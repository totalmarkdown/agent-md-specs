---
spec_name: REVIEWS.md
spec_version: 0.1.0
category: Social
domain: reviewsmd.dev
priority: Medium
volume: "Vol 4 — Economic Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# REVIEWS.md

**Category:** Social
**Domain:** reviewsmd.dev
**Priority:** Medium
**Version:** 0.1.0

**Priority:** MEDIUM  
**Version:** 0.1.0

### Purpose
Curated reviews and testimonials from users and other agents. 
Unlike REPUTATION.md (which has scored metrics), REVIEWS.md 
contains the narrative stories of how this agent helped people.
The social proof document.

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
Full review list available at: [marketplace URL]  
Reviews are: [moderated | unmoderated | AI-filtered for spam]
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
