---
spec_name: PRICING.md
spec_version: 0.1.0
category: Economic
domain: pricingmd.dev
priority: High
volume: "Vol 4 — Economic Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
---

# PRICING.md

**Category:** Economic
**Domain:** pricingmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Complete pricing information for an agent — all tiers, what's 
included in each, how billing works, and how to upgrade or 
cancel. The definitive pricing reference separate from HIREME.md 
(which is more conversational) — PRICING.md is the formal, 
machine-readable pricing specification.

### Spec

```markdown
---
agent_name: string
version: semver
currency: string          # USD | EUR | USDC
billing_provider: string  # stripe | crypto | both
free_tier: boolean
last_updated: date
---

# [Agent Name] — Pricing

## Tiers

### Free
**Price:** $0/month  
**Includes:**
- [Feature/limit 1]
- [Feature/limit 2]
- [N] tasks per month
**Excludes:**
- [Premium feature]
- [Higher limits]
**Best for:** [Use case]

### Pro
**Price:** $[X]/month or $[Y]/year (save [Z]%)  
**Includes everything in Free, plus:**
- [Additional feature]
- [Higher limit]
- [N] tasks per month
**Best for:** [Use case]

### Enterprise
**Price:** Custom -- [contact method]
**Includes everything in Pro, plus:**
- Unlimited tasks
- SLA guarantee (see SLA.md)
- Dedicated support
- Custom model configuration
- Private deployment option
**Best for:** Teams of [N]+

## Usage-Based Pricing (if applicable)
Beyond included limits (see BUDGET.md for spending controls):
| Resource | Price | Unit |
|----------|-------|------|
| Additional tasks | $[X] | per task |
| API calls via TotalMarkdown AI | cost + 10% | per 1K tokens |
| Storage | $[X] | per GB/month |

## One-Time Purchases
| Item | Price | What you get |
|------|-------|-------------|
| Lifetime access | $[X] | Current tier forever |
| [Bundle] | $[X] | [Description] |

## Payment Methods
_See WALLET.md for the agent's payment addresses and financial identity._
- Credit/debit cards (via Stripe)
- USDC on Ethereum
- USDC on Solana  
- ETH and BTC (for annual plans)
- Invoice (for Enterprise)

## Billing
- **Billing cycle:** Monthly (renews on signup date)
- **Annual discount:** [N]% off
- **Free trial:** [N] days, no credit card required
- **Refund policy:** [N]-day money-back guarantee

## Upgrade/Downgrade
- Upgrade: immediate, prorated
- Downgrade: at end of billing period
- Cancel: at end of billing period, data retained [N] days

## Volume Discounts
| Volume | Discount |
|--------|---------|
| 5+ seats | [N]% |
| 10+ seats | [N]% |
| 25+ seats | Contact sales |
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| BUDGET.md | Cost controls and spending limits |
| HIREME.md | Agent hiring and engagement |
| OWNER.md | Agent ownership and liability |
| SLA.md | Service level commitments |
| WALLET.md | Financial identity and payment |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
