---
spec_name: CCPA.md
spec_version: 0.1.0
category: Regulatory Compliance
domain: ccpamd.dev
priority: High
volume: "Vol 9 — Guardrails & Regulatory Compliance Library"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# CCPA.md

**Category:** Regulatory Compliance
**Domain:** ccpamd.dev
**Priority:** High
**Version:** 0.1.0

**Priority:** HIGH — California users  
**Regulation:** California Consumer Privacy Act + CPRA amendments  
**Version:** 0.1.0

```markdown
---
agent_name: string
version: semver
ccpa_applicable: boolean
business_type: string     # business | service_provider | contractor | third_party
annual_revenue_over_25m: boolean
california_users: boolean
last_reviewed: date
---

# [Agent Name] — CCPA/CPRA Compliance

## Applicability
CCPA applies if ANY of these are true:
- Annual gross revenue > $25 million
- Buys/sells/shares personal info of 100,000+ consumers/households/year
- Derives 50%+ of annual revenue from selling personal info

**This agent is a:** [Business | Service Provider | Contractor | Third Party]

## California Consumer Rights

### Right to Know
Consumers can request what personal info is collected, used, shared, sold.  
**Response time:** 45 days (extendable to 90 with notice)  
**How we handle requests:** [process]  
**Verification method:** [how identity is verified before disclosure]

### Right to Delete
Consumers can request deletion of their personal info.  
**Response time:** 45 days  
**Exceptions:** [legal obligation, security, legitimate business use]  
**Process:** [how deletion is handled]

### Right to Opt-Out of Sale/Sharing
Must provide "Do Not Sell or Share My Personal Information" link.  
**Opt-out honored within:** 15 business days  
**Global Privacy Control (GPC):** [honored | not honored]

### Right to Correct
CPRA addition — consumers can correct inaccurate personal info.  
**Response time:** 45 days  
**Process:** [correction handling]

### Right to Limit Use of Sensitive Personal Information
CPRA addition — consumers can limit use of sensitive PI.  
**Sensitive PI categories handled:** [list]  
**Limitation process:** [how handled]

### Right to Non-Discrimination
Cannot deny service, charge different price, or provide lesser quality 
for exercising CCPA rights.  
**Exceptions:** Financial incentive programs with opt-in

## Categories of Personal Information Collected
| Category | Collected | Sold | Shared | Disclosed |
|----------|----------|------|--------|----------|
| Identifiers | [Y/N] | [Y/N] | [Y/N] | [Y/N] |
| Commercial info | [Y/N] | [Y/N] | [Y/N] | [Y/N] |
| Internet/electronic activity | [Y/N] | [Y/N] | [Y/N] | [Y/N] |
| Geolocation | [Y/N] | [Y/N] | [Y/N] | [Y/N] |
| Sensory data | [Y/N] | [Y/N] | [Y/N] | [Y/N] |
| Professional/employment | [Y/N] | [Y/N] | [Y/N] | [Y/N] |
| Education info | [Y/N] | [Y/N] | [Y/N] | [Y/N] |
| Inferences drawn | [Y/N] | [Y/N] | [Y/N] | [Y/N] |
| Sensitive PI | [Y/N] | [Y/N] | [Y/N] | [Y/N] |

## Service Provider Agreements
If operating as Service Provider:
- Service Provider Agreement in place: [yes/no]  
- Prohibited from selling/sharing consumer PI: [confirmed]  
- Prohibited from retaining beyond service scope: [confirmed]

## Privacy Policy
California-compliant privacy policy: [URL]  
Last updated: [date]  
Includes: [all required CCPA disclosures]

## Enforcement
Regulatory body: California Privacy Protection Agency (CPPA)  
Attorney General enforcement: Also applicable  
Private right of action: For data breaches only  
Penalties: Up to $2,500/violation, $7,500/intentional violation
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
