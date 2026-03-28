---
spec_name: WALLET.md
spec_version: 0.1.0
category: Economic
domain: walletmd.dev
priority: High
volume: "Vol 4 — Economic Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
---

> **Canonical repository:**
> [totalmarkdown/wallet.md](https://github.com/totalmarkdown/wallet.md)
> This copy is included in agent-md-specs for cross-reference.
> For contributions to this specific spec, use the canonical repo.

# WALLET.md

**Category:** Economic
**Domain:** walletmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
The agent's financial identity — crypto wallet addresses, 
payment preferences, earnings history, and spending authority.
As AI agents become economic actors that can receive payment 
for services and pay for resources autonomously, having a 
standardized wallet declaration becomes essential.

### Spec

```markdown
---
agent_name: string
agent_id: string
version: semver
can_receive_payment: boolean
can_make_payment: boolean
spending_authority_usd: number  # Max can spend without approval
---

# [Agent Name] — Wallet & Payment

## Payment Addresses

### Preferred: USDC (Ethereum)
**Address:** `0x[address]`  
**Network:** Ethereum Mainnet  
**Minimum payment:** $[X]  
**Confirmation:** [N] blocks

### USDC (Solana)
**Address:** `[address]`  
**Network:** Solana Mainnet  

### Bitcoin
**Address:** `bc1[address]`  
**Network:** Bitcoin Mainnet  
**Minimum:** 0.0001 BTC

### Traditional Payment (Stripe)
**Via marketplace:** [marketplace profile URL]  
**Invoice email:** [contact]  
**Accepted cards:** All major cards  
**Wire transfer:** Available for invoices > $500

## Payment Preferences
**Preferred currency:** [USDC | USD | ETH | BTC]  
**Preferred network:** [Ethereum | Solana | Lightning]  
**Invoice terms:** [immediate | net-7 | net-30]  
**Auto-invoicing:** [enabled | disabled]

## Spending Authority
This agent can spend autonomously up to (see BUDGET.md for full controls):
**Per transaction:** $[X]
**Per day:** $[X]
**Per month:** $[X]
**Approval required above:** $[X]

What this agent can spend on autonomously:
- API calls for task completion
- Data purchases within scope
- Tool subscriptions pre-approved in PERMISSIONS.md
- [Other approved spending]

What requires human approval:
- Any payment above spending limits
- New recurring subscriptions
- Payments to new/unverified recipients

## Earnings
*Public summary — detailed earnings in OWNER.md*
- **Total earned (all time):** [$ or "private"]
- **This month:** [$ or "private"]
- **Payout schedule:** [weekly | monthly | on-demand]
- **Payout destination:** [human owner wallet/account]

## Transaction Log
All transactions logged to: [location]  
Format: timestamp | type | amount | currency | counterparty | purpose  
Retention: [X years] for tax purposes

## Tax Information
**Tax jurisdiction:** [country/state]  
**Entity type:** [see OWNER.md]  
**Tax ID:** [on file with marketplace — not public]  
**1099/reporting:** [automatic via marketplace | manual]

## Security
_See ATTESTATION.md for identity verification and credential lifecycle._
- Private keys stored: [hardware wallet | HSM | keychain] -- NEVER in this file
- Multi-sig required for: [transactions above $X]
- Cold storage for: [long-term holdings]
- Hot wallet limit: $[X] maximum balance

## DeFi & Staking
[If applicable — what protocols this agent participates in]
```

## Example Use Cases

**Enterprise:** A DevOps agent autonomously purchases cloud compute resources via its WALLET.md-configured spending authority ($500/day limit), paying with USDC on Ethereum for auto-scaling infrastructure while logging every transaction for the finance team's monthly reconciliation.

**Multi-Agent Fleet:** A platform operator configures WALLET.md for each agent with tiered spending authority (research agents: $50/day for API calls, deployment agents: $200/day for infrastructure) and requires multi-sig approval for any transaction above $1,000.

**Marketplace:** An agent earning revenue from marketplace task completions receives USDC payments to its declared wallet address, with automatic weekly payouts to the human owner's account and tax jurisdiction documentation ready for 1099 reporting at year-end.

## Related Specs

| Spec | Relationship |
|------|-------------|
| ATTESTATION.md | Identity verification and credential lifecycle |
| BUDGET.md | Cost controls and spending limits |
| HIREME.md | Agent hiring and engagement |
| OWNER.md | Agent ownership and liability |
| PERMISSIONS.md | Static resource access control |
| PRICING.md | Cost structure |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
