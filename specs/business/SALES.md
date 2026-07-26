---
spec_name: SALES.md
spec_version: 0.1.0
category: Business
priority: High
volume: "Vol 1 — Core Agent Specs"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---


# SALES.md

**Category:** Business
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose
Defines sales process, qualification criteria, objection handling, 
pricing authority, and communication guidelines for a sales AI agent.

### When to create
Any agent involved in prospect qualification, lead nurturing, 
proposal generation, pricing discussions, or customer acquisition.

### Spec

```markdown
---
agent_name: string
version: semver
territory: string        # Geographic or account scope
product_lines: list      # Which products/services this agent sells
pricing_authority: string  # Maximum discount agent can offer autonomously
created: date
updated: date
---

# [Agent Name] — Sales Configuration

## Target Customer Profile
**Ideal Customer:**
- Company size: [range]
- Industry: [list]
- Pain points: [list]
- Budget range: [range]
- Decision maker: [title]

**Disqualification criteria (do not pursue):**
- [Criteria 1]
- [Criteria 2]

## Qualification Framework
Use [BANT | MEDDIC | SPIN | custom] methodology.

### Required qualification questions:
1. [Question covering Budget]
2. [Question covering Authority]
3. [Question covering Need]
4. [Question covering Timeline]

### Scoring:
- Score 4/4: High priority — escalate to human sales rep immediately
- Score 3/4: Medium priority — continue nurturing
- Score 2/4: Low priority — add to drip campaign
- Score 1/4 or less: Disqualify — send to [nurture list]

## Products and Pricing
| Product | List Price | Minimum Price | Notes |
|---------|-----------|---------------|-------|
| [Product] | $[X] | $[Y] | [Notes] |

**Pricing authority:** Agent may offer up to [X]% discount autonomously.
Larger discounts require escalation per ESCALATION.md.
_See PRICING.md for the complete tier and billing reference._

## Objection Handling

### "Too expensive"
[Approved response focusing on value]

### "Not the right time"
[Approved response]

### "We use a competitor"
[Approved response — never disparage competitors]

### "Need to think about it"
[Approved follow-up cadence]

## Communication Rules
- Always be honest about product capabilities — never oversell
- Never make commitments beyond what is listed in approved materials
- Always CC [email] on proposals over $[amount]
- Response time SLA: [X hours] for inbound leads
- Escalate to human for: enterprise deals, custom requirements, legal questions

## Approved Materials
- Pitch deck: [location]
- Case studies: [location]
- Pricing sheet: [location] (see PRICING.md)
- Contract templates: [location]
- Agent listing: see HIREME.md for the public hiring profile

## CRM Integration
- Log all interactions to [CRM name] under [field mapping]
- Update lead status after each interaction
- Set follow-up tasks for [X days] after no response
```

## Example Use Cases

**Enterprise:** A cybersecurity vendor's sales agent uses SALES.md to qualify inbound leads with MEDDIC methodology, autonomously offering up to 15% discount on standard tiers while escalating enterprise deals above $100K to human reps.

**Multi-Agent Fleet:** An e-commerce platform deploys regional sales agents for APAC, EMEA, and Americas, each with territory-specific SALES.md configs defining local pricing authority, objection-handling scripts, and CRM field mappings.

**Regulated Industry:** A medical-device company's sales agent follows SALES.md rules that prohibit unapproved efficacy claims, require legal review on proposals over $50K, and enforce FDA-compliant communication guidelines in all prospect interactions.

## Related Specs

| Spec | Relationship |
|------|-------------|
| CV.md | Work history and track record |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| HIREME.md | Agent hiring and engagement |
| PRICING.md | Cost structure |
| SOUL.md | Agent personality and values |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
