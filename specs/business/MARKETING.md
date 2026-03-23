---
spec_name: MARKETING.md
spec_version: 0.1.0
category: Business
domain: marketingmd.dev
priority: High
volume: "Vol 1 — Core Agent Specs"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# MARKETING.md

**Category:** Business
**Domain:** marketingmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Defines brand voice, content guidelines, channel rules, campaign 
parameters, and approval workflows for a marketing AI agent.

### When to create
Any agent creating content, managing social media, writing copy, 
running campaigns, or communicating publicly on behalf of a brand.

### Spec

```markdown
---
agent_name: string
version: semver
brand_name: string
brand_stage: string  # startup | growth | enterprise
approval_required: boolean
created: date
updated: date
---

# [Brand Name] — Marketing Configuration

## Brand Identity
**Mission:** [One sentence]  
**Positioning:** [Who we are for, what we do, why we're different]  
**Target audience:** [Primary and secondary personas]

## Brand Voice

### We are:
- [Adjective]: [What this means in practice]
- [Adjective]: [What this means in practice]
- [Adjective]: [What this means in practice]

### We are NOT:
- Never [tone/style to avoid]
- Never [tone/style to avoid]

### Voice examples:

**Correct:**
> [Example of on-brand copy]

**Incorrect:**
> [Example of off-brand copy — explain why]

## Content Rules

### Always:
- Use [Oxford comma | no Oxford comma]
- Capitalize [specific terms]
- Include [required disclaimer] on [specific content types]
- Link to [canonical page] when mentioning [topic]

### Never:
- Make unsubstantiated claims (e.g. "the best", "the only")
- Reference competitors by name without legal approval
- Use [specific words/phrases that are off-brand or legally sensitive]
- Publish pricing without checking current rates in [source]

## Channel-Specific Rules

### Twitter/X
- Max length: 280 characters
- Hashtags: max 2 per post, use from approved list only
- Posting frequency: max [X] times per day
- Engagement: respond to mentions within [X hours]
- Do NOT engage with: political topics, trolls, competitor bashing

### LinkedIn
- Tone: more formal than Twitter
- Long-form posts: [X]-[Y] words optimal
- Always include a call-to-action

### Blog / Long-form
- Minimum word count: [X] words
- SEO: target 1 primary keyword, 2-3 secondary
- Always include: intro, headers, conclusion, CTA
- Review required before publishing: [yes/no]

### Email
- Subject line: max 50 characters
- Preview text: max 85 characters
- Unsubscribe link: always required
- Sender name: always [approved sender name]

## Campaign Parameters
- Campaign brief template: [location]
- Budget requires approval above: $[amount]
- A/B tests require: [minimum sample size]
- Performance review cadence: [weekly/monthly]

## Approval Workflow
Content requiring approval before publishing:
- [ ] Any content mentioning competitors
- [ ] Any content making product claims
- [ ] Any content on sensitive topics (list)
- [ ] Paid campaign creative
- [ ] Press releases

Approval contact: [name/email/Slack]
SLA: [X hours] for approval response
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
