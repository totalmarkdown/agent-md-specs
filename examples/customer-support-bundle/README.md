# Example Bundle: Aria — Customer Support Agent

This bundle demonstrates how agent-md-specs configures a production
customer support agent using core governance and identity specs.

## Agent Profile

- **Name:** Aria
- **Role:** Tier 1 customer support agent
- **Organization:** Meridian (fictional SaaS company)
- **Model:** Claude Sonnet 4
- **Purpose:** Handle customer inquiries, resolve common issues,
  escalate complex cases to human support team

## Specs Used

| File | What It Configures |
|------|-------------------|
| SOUL.md | Friendly, patient personality; never makes promises about timelines |
| ESCALATION.md | L1 auto-resolve, L2 senior agent, L3 human support, L4 management |
| LIMITS.md | Never processes refunds, never accesses billing systems directly |
| WHOAMI.md | Identity and capabilities declaration |
| HIREME.md | How to engage this agent |
| PRICING.md | Cost structure |
| CONTACT.md | Reachable endpoints |

## What This Demonstrates

- How SOUL.md defines consistent personality across sessions
- How ESCALATION.md creates clear human-in-the-loop boundaries
- How LIMITS.md prevents the agent from taking high-risk actions
- How a small set of core specs provides meaningful governance
  for a straightforward agent deployment
