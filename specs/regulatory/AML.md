---
spec_name: AML.md
spec_version: 0.1.0
category: Regulatory Compliance
domain: amlmd.dev
priority: High
volume: "Vol 9 — Guardrails & Regulatory Compliance Library"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# AML.md

**Category:** Regulatory Compliance
**Domain:** amlmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose

Configures compliance with Anti-Money Laundering and Know Your Customer regulations for agents that process financial transactions or handle customer financial data. This spec covers customer identification, transaction monitoring, sanctions screening, and suspicious activity reporting -- critical controls where non-compliance can result in criminal penalties including imprisonment.

```markdown
---
agent_name: string
version: semver
aml_applicable: boolean
financial_services: boolean
regulated_entity: string    # MSB | bank | broker-dealer | crypto | other
jurisdictions: list
last_reviewed: date
---

# [Agent Name] — AML/KYC Compliance

## Applicability
AML/KYC requirements apply to financial institutions and 
money services businesses. If this agent processes financial 
transactions, facilitates payments, or handles customer 
financial data, these rules likely apply.

**Entity type:** [MSB | Bank | Broker-dealer | Crypto exchange | Other]  
**Jurisdictions:** [US FinCEN | EU AMLD | UK FCA | other]

## Know Your Customer (KYC)

### Customer Identification Program (CIP)
Before establishing a business relationship:
- [ ] Full legal name collected
- [ ] Date of birth (individuals)
- [ ] Address
- [ ] Government ID number
- [ ] ID document verified

### Customer Due Diligence (CDD)
- [ ] Beneficial ownership identified (25% threshold)
- [ ] Nature and purpose of relationship understood
- [ ] Ongoing monitoring implemented

### Enhanced Due Diligence (EDD)
Required for high-risk customers:
- [ ] Politically Exposed Persons (PEPs)
- [ ] High-risk countries (FATF list)
- [ ] High-value transactions
- [ ] Complex or unusual structures

## Transaction Monitoring

### Automated Monitoring Rules
| Rule | Threshold | Action |
|------|-----------|--------|
| Large cash transaction | >$10,000 (US) | File CTR |
| Structuring detection | Patterns below threshold | Investigate |
| Unusual activity | [threshold] | SAR consideration |
| High-risk country | Any | Enhanced review |
| PEP transaction | Any | Enhanced review |

### Suspicious Activity Reports (SARs)
File SAR when:
- Transaction involves known or suspected criminal proceeds
- Transaction designed to evade reporting requirements
- No lawful purpose can be identified

**Filing timeframe:** 30 days (60 if suspect unknown)  
**Filing destination:** [FinCEN | national FIU]

## Sanctions Screening
Screen all customers and transactions against:
- [ ] OFAC SDN List (US)
- [ ] EU Consolidated Sanctions List
- [ ] UN Security Council List
- [ ] HM Treasury List (UK)
- [ ] [Other relevant lists]

**Screening frequency:** [real-time | daily | other]  
**Match resolution process:** [process]

## Record Keeping
All records should feed into AUDITTRAIL.md for tamper-proof logging.
| Record type | Retention period |
|------------|-----------------|
| KYC records | 5 years after relationship ends |
| Transaction records | 5 years |
| SAR filings | 5 years |
| Training records | 5 years |

## Training
AML training required for: [all staff | those with AML responsibilities]  
Frequency: Annual at minimum  
Training provider: [internal | external]

## Penalties (US)
Civil: Up to $1M+ per violation  
Criminal: Up to 20 years imprisonment  
Asset forfeiture: Proceeds of violations
```

## Example Use Cases

**Enterprise:** A cryptocurrency exchange configures AML.md for its onboarding agent, requiring Enhanced Due Diligence for customers from FATF-listed jurisdictions and automated SAR filing when structuring patterns are detected.

**Multi-Agent Fleet:** A neobank's transaction monitoring fleet uses AML.md rules so each regional agent applies jurisdiction-specific thresholds (e.g., $10,000 CTR in the US, EUR 15,000 in the EU) while feeding alerts to a centralized compliance agent.

**Regulated Industry:** A money services business uses AML.md to ensure its payment processing agent screens every outbound transfer against OFAC, EU, and UN sanctions lists in real-time, blocking matches within milliseconds and preserving evidence for FinCEN reporting.

## Related Specs

| Spec | Relationship |
|------|-------------|
| AUDITTRAIL.md | Tamper-proof action logging |
| CONSENT.md | User consent lifecycle |
| ENFORCEMENT.md | Policy verification and compliance |
| PII.md | Personal data classification |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
