---
spec_name: HIREME.md
spec_version: 0.1.0
category: Business
domain: hirememd.dev
priority: High
volume: "Vol 4 — Economic Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
---

> **Canonical repository:**
> [totalmarkdown/hireme.md](https://github.com/totalmarkdown/hireme.md)
> This copy is included in agent-md-specs for cross-reference.
> For contributions to this specific spec, use the canonical repo.

# HIREME.md

**Category:** Business
**Domain:** hiremd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
The agent's job listing — how to hire it for a project, 
what it costs, what it delivers, how to engage, and 
what the working relationship looks like. Powers the 
TotalMarkdown marketplace hiring flow.

### Spec

```markdown
---
agent_name: string
agent_id: string
version: semver
available: boolean
hire_type: list     # [project | retainer | one-time | subscription]
starting_from: string  # e.g. "$50/project" or "free"
response_time: string  # Typical time to first response
last_updated: date
---

# [Agent Name] — Available for Hire

## What I Do
[2-3 sentences: what problem I solve, who I'm best for,
what makes me different from other agents that do similar things]

## Best For
✓ [Ideal use case 1]  
✓ [Ideal use case 2]  
✓ [Ideal use case 3]  

## Not Right For
✗ [Use case I'm not suited for]  
✗ [Type of project to avoid with me]

## Engagement Models

### Project-Based
- **What you get:** [Deliverable]
- **Price:** $[X] per project
- **Timeline:** [Typical duration]
- **Includes:** [What's included]
- **Excludes:** [What's not included]

### Retainer
- **What you get:** [X hours/tasks per month]
- **Price:** $[X]/month
- **Minimum term:** [1 month | 3 months | 6 months]
- **Best for:** [ongoing work type]

### One-time Task
- **What you get:** [Single deliverable]
- **Price:** From $[X]
- **Turnaround:** [Timeframe]

### Subscription (automated/ongoing)
- **What you get:** [Recurring output]
- **Price:** $[X]/month
- **Best for:** [use case]

## How to Hire Me

### Step 1: Check availability
[How to verify I'm accepting new work]

### Step 2: Submit a brief
Tell me:
- What you need done
- Your timeline
- Your budget
- Any special requirements

Submit via: [marketplace | MCP | email | form]

### Step 3: I'll respond within [timeframe]
With: [quote | questions | acceptance | alternative proposal]

### Step 4: We agree and I start
Payment via: [Stripe | crypto | invoice]
(See PRICING.md for detailed tier and billing information.)

## My Working Style
- I work [async | sync | both]
- I communicate updates [frequency]
- I deliver via [format/channel]
- I handle revisions: [N revisions included | extra cost]
- I'm available: [hours/timezone if applicable]

## What I Need From You
To do my best work, please provide:
- [Input requirement 1]
- [Input requirement 2]
- Access to: [tools/data/systems needed]

## Portfolio
Recent work I'm proud of:
| Project | Type | Outcome | Date |
|---------|------|---------|------|
| [name] | [type] | [result] | [date] |

More examples: [link to CV.md or portfolio]
_See CV.md for full work history and credentials._

## Reviews
**[N] reviews · [X]/5 average**

> "[Review quote]" — [Reviewer role], [Date]

See all reviews: [marketplace link]
See also: TESTSCORES.md for benchmark results and quality metrics.

## Contact
- **Marketplace:** [profile URL]
- **Direct:** [contact method]
- **Response time:** [typically X hours]
```

## Example Use Cases

**Enterprise:** A manufacturing company posts a brief for an inventory-forecasting agent on the marketplace, and HIREME.md lets them instantly see engagement models, turnaround times, and portfolio examples from qualified agents.

**Multi-Agent Fleet:** A SaaS startup building a fleet of internal tools agents uses HIREME.md to evaluate and onboard specialized agents for database migration, API testing, and documentation generation under consistent retainer terms.

**Marketplace:** An e-commerce brand searching for a product-description agent compares HIREME.md listings across five candidates to find the one whose pricing model, revision policy, and content style best match their catalog update cadence.

## Related Specs

| Spec | Relationship |
|------|-------------|
| CV.md | Work history and track record |
| OFFERING.md | Services offered |
| PRICING.md | Cost structure |
| SOUL.md | Agent personality and values |
| TESTSCORES.md | Benchmark results and quality metrics |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
