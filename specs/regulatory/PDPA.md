---
spec_name: PDPA.md
spec_version: 0.1.0
category: Regulatory Compliance
domain: pdpamd.dev
priority: Medium
volume: "Vol 9 — Guardrails & Regulatory Compliance Library"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# PDPA.md

**Category:** Regulatory Compliance
**Domain:** pdpamd.dev
**Priority:** Medium
**Version:** 0.1.0

```markdown
---
agent_name: string
version: semver
thailand_pdpa: boolean
singapore_pdpa: boolean
last_reviewed: date
---

# [Agent Name] — PDPA Compliance

## Two PDPAs — Know Which Applies

### Thailand PDPA (effective June 2022)
Applies to: collection/use/disclosure of personal data of 
individuals in Thailand.

### Singapore PDPA (effective 2012, amended 2021)
Applies to: collection/use/disclosure of personal data of 
individuals in Singapore by private organisations.

---

## Thailand PDPA

### Legal Bases
- Consent (explicit for sensitive data)
- Contract necessity
- Vital interests
- Legal obligation
- Legitimate interests (with balancing test)
- Public task

### Data Subject Rights
| Right | Timeframe |
|-------|-----------|
| Access | 30 days |
| Correction | 30 days |
| Erasure | 30 days |
| Restriction | Prompt |
| Portability | 30 days |
| Objection | Prompt |

### Sensitive Personal Data (requires explicit consent)
- [ ] Racial/ethnic origin
- [ ] Political opinions
- [ ] Religious/philosophical beliefs
- [ ] Sexual behavior
- [ ] Criminal records
- [ ] Health data
- [ ] Disability
- [ ] Labor union membership
- [ ] Genetic/biometric data

### DPO Required If: Large scale processing, sensitive data, systematic monitoring  
**DPO contact:** [name, contact]

### Breach Notification
- Notify PDPC: within 72 hours
- Notify data subjects: without delay if likely to affect rights

---

## Singapore PDPA

### Obligations
- **Consent:** Obtain consent before collection (deemed consent possible)
- **Purpose limitation:** Use only for notified purpose
- **Notification:** Notify purpose before/at collection
- **Access and correction:** Within 30 days
- **Accuracy:** Reasonable effort to ensure accuracy
- **Protection:** Security safeguards
- **Retention limitation:** Delete when no longer necessary
- **Transfer limitation:** Adequate protection in destination country

### Do Not Call (DNC) Registry
If sending marketing to Singapore numbers:
- Check DNC registry before calling/texting
- Frequency: within 30 days before contact

### Breach Notification (2021 amendment)
- Notify PDPC: within 3 days if significant harm likely
- Notify individuals: as soon as reasonably practicable
- Significant harm = [financial loss, physical harm, distress, etc]

### Penalties
- Up to SGD 1,000,000 per breach
- Enhanced financial penalties (2021): up to 10% of annual turnover
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
