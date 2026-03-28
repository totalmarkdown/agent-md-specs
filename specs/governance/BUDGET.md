---
spec_name: BUDGET.md
spec_version: 0.1.0
category: Governance
domain: budgetmd.dev
priority: High
volume: "Vol 1 — Core Agent Specs"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
---

# BUDGET.md

**Category:** Governance
**Domain:** budgetmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Defines resource limits, token budgets, cost thresholds, and 
spending controls for AI agents. Prevents runaway costs in 
autonomous agent deployments.

### Spec

```markdown
---
agent_name: string
version: semver
billing_owner: string      # Who pays for this agent's API costs (see WALLET.md)
monthly_budget_usd: number
alert_threshold_pct: number  # Alert when X% of budget used
created: date
updated: date
---

# [Agent Name] — Budget Configuration

## Monthly Limits
- **Total budget:** $[amount]/month
- **Alert at:** [X]% of budget (sends notification)
- **Hard stop at:** [Y]% of budget (pauses agent)
- **Reset date:** [day of month]

## Per-Task Limits
| Task Type | Max tokens per call | Max cost per call | Max calls per day |
|-----------|--------------------|--------------------|-------------------|
| Standard | [N] | $[X] | [N] |
| Complex | [N] | $[X] | [N] |
| Batch | [N] | $[X] | [N] |

## Model Selection Rules
Use the cheapest model that can complete the task:
- Simple classification/extraction: [cheapest model]
- Standard reasoning: [mid-tier model]
- Complex analysis: [premium model only when necessary]
- Default fallback: [default model]

## Cost Tracking
- Log every API call with: model, input tokens, output tokens, cost (see AUDITTRAIL.md)
- Daily cost report to: [location/contact]
- Monthly summary to: [location/contact]

## When Budget is Exceeded
- At 80% budget: log warning, notify [contact], switch to cheaper models
- At 95% budget: pause non-critical tasks, notify [contact]
- At 100% budget: stop all tasks, escalate Level 3 (see ESCALATION.md)
- Emergency override: [contact] can authorize budget increase

## Optimization Rules
- Cache responses for identical inputs (TTL: [X hours])
- Batch similar requests when possible
- Use streaming for long outputs to detect early termination
- Prefer shorter prompts — link to reference files instead of embedding them
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| AUDITTRAIL.md | Tamper-proof action logging |
| DELEGATION.md | Authority chain and authorization |
| ENFORCEMENT.md | Policy verification and compliance |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| LIMITS.md | Hard constraints and safety boundaries |
| PERMISSIONS.md | Static resource access control |
| PRICING.md | Cost structure |
| WALLET.md | Financial identity and payment |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
