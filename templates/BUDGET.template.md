---
agent_name: "[REPLACE THIS]"
version: "0.1.0"
billing_owner: "[REPLACE THIS]"
monthly_budget_usd: "[REPLACE THIS]"
alert_threshold_pct: 80
created: "[REPLACE THIS — YYYY-MM-DD]"
---

# [REPLACE THIS — Agent Name] — Budget Configuration

<!-- Resource limits and spending controls -->

## Monthly Limits
- **Total budget:** $[REPLACE THIS]/month
- **Alert at:** [REPLACE THIS]% of budget
- **Hard stop at:** [REPLACE THIS]% of budget
- **Reset date:** [REPLACE THIS — day of month]

## Per-Task Limits
| Task Type | Max tokens | Max cost | Max calls/day |
|-----------|-----------|----------|---------------|
| Standard | [REPLACE THIS] | $[REPLACE THIS] | [REPLACE THIS] |
| Complex | [REPLACE THIS] | $[REPLACE THIS] | [REPLACE THIS] |

## Model Selection Rules
<!-- Use the cheapest model that can complete the task -->
- Simple tasks: [REPLACE THIS — model name]
- Standard reasoning: [REPLACE THIS — model name]
- Complex analysis: [REPLACE THIS — model name]

## When Budget is Exceeded
- At 80%: [REPLACE THIS — action]
- At 95%: [REPLACE THIS — action]
- At 100%: [REPLACE THIS — action]
