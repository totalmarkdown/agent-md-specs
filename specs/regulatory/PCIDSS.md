---
spec_name: PCIDSS.md
spec_version: 0.1.0
category: Regulatory Compliance
domain: pcidssmd.dev
priority: High
volume: "Vol 9 — Guardrails & Regulatory Compliance Library"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# PCIDSS.md

**Category:** Regulatory Compliance
**Domain:** pcidssmd.dev
**Priority:** High
**Version:** 0.1.0

```markdown
---
agent_name: string
version: semver
pci_applicable: boolean
merchant_level: string    # 1 | 2 | 3 | 4
cardholder_data_handled: boolean
last_qsa_assessment: date
compliance_status: string  # compliant | in-progress | not-applicable
---

# [Agent Name] — PCI-DSS Compliance

## Applicability
PCI-DSS applies to all entities that store, process, 
or transmit cardholder data.

**Cardholder data includes:**
- Primary Account Number (PAN)
- Cardholder name
- Expiration date
- Service code
- Sensitive Authentication Data (SAD)

**This agent:** [stores | processes | transmits | does not touch] cardholder data

## Merchant Level
| Level | Criteria | Annual requirement |
|-------|---------|-------------------|
| 1 | >6M Visa/MC transactions/year | On-site QSA assessment |
| 2 | 1M-6M transactions/year | Annual SAQ + quarterly scan |
| 3 | 20K-1M e-commerce transactions | Annual SAQ + quarterly scan |
| 4 | <20K e-commerce or <1M other | Annual SAQ |

**This agent's level:** [level]

## Scope Reduction
**In scope systems:** [list]  
**Scope reduction measures:**
- Tokenization: [yes — provider: [name] | no]
- Point-to-point encryption: [yes | no]
- Network segmentation: [yes | no]

## 12 PCI-DSS Requirements Status

| Req | Requirement | Status | Notes |
|-----|-------------|--------|-------|
| 1 | Network security controls | [✓/⚠/✗] | |
| 2 | Secure configurations | [✓/⚠/✗] | |
| 3 | Protect stored cardholder data | [✓/⚠/✗] | |
| 4 | Protect data in transit | [✓/⚠/✗] | |
| 5 | Protect against malware | [✓/⚠/✗] | |
| 6 | Secure software development | [✓/⚠/✗] | |
| 7 | Restrict access by need-to-know | [✓/⚠/✗] | |
| 8 | Identify users and authenticate | [✓/⚠/✗] | |
| 9 | Restrict physical access | [✓/⚠/✗] | |
| 10 | Log and monitor all access | [✓/⚠/✗] | |
| 11 | Test systems and networks | [✓/⚠/✗] | |
| 12 | Support information security | [✓/⚠/✗] | |

## Never Store These
Sensitive Authentication Data — NEVER stored post-authorization:
- Full track data
- CAV2/CVC2/CVV2/CID
- PINs/PIN blocks

## Incident Response
If cardholder data breach suspected:
1. Do not delete any data — preserve evidence
2. Isolate affected systems
3. Contact acquiring bank immediately
4. Contact card brands (Visa, Mastercard, etc.)
5. Contact QSA for forensic investigation
6. Notify law enforcement if required

**PCI incident contact:** [acquiring bank contact]

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
