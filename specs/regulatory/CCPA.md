---
spec_name: CCPA.md
spec_version: 0.1.0
category: Regulatory Compliance
priority: High
volume: "Vol 9 — Guardrails & Regulatory Compliance Library"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---


# CCPA.md

**Category:** Regulatory Compliance
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose

Configures compliance with California's CCPA and CPRA, covering consumer rights to know, delete, correct, and opt out of the sale or sharing of personal information. This spec is essential for agents handling data of California residents where the business meets CCPA revenue, volume, or revenue-source thresholds.

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
Consumers can request what personal info is collected, used, shared, sold (see CONSENT.md for consent lifecycle management).  
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
_See AUDITTRAIL.md for logging all consumer rights requests._
Regulatory body: California Privacy Protection Agency (CPPA)  
Attorney General enforcement: Also applicable  
Private right of action: For data breaches only  
Penalties: Up to $2,500/violation, $7,500/intentional violation
```

## Example Use Cases

**Enterprise:** A retail company's customer data agent uses CCPA.md to automatically process "Right to Delete" requests within 45 days, coordinating deletion across its marketing database, analytics platform, and CRM while logging exceptions for legal holds.

**Multi-Agent Fleet:** A data broker's agent fleet uses CCPA.md to enforce "Do Not Sell" opt-outs across all downstream agents within 15 business days, ensuring Global Privacy Control signals are honored consistently.

**Regulated Industry:** An adtech company configures CCPA.md so its profiling agent categorizes all personal information by the nine CCPA categories, enabling accurate disclosures in its annual privacy report and reducing audit findings from the California Privacy Protection Agency.

## Related Specs

| Spec | Relationship |
|------|-------------|
| AUDITTRAIL.md | Tamper-evident action logging |
| CONSENT.md | User consent lifecycle |
| ENFORCEMENT.md | Policy verification and compliance |
| PII.md | Personal data classification |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
