---
spec_name: LGPD.md
spec_version: 0.1.0
category: Regulatory Compliance
priority: Medium
volume: "Vol 9 — Guardrails & Regulatory Compliance Library"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---


# LGPD.md

**Category:** Regulatory Compliance
**Priority:** Medium
**Version:** 0.1.0 **Type:** Static

### Purpose

Configures compliance with Brazil's LGPD (Lei Geral de Protecao de Dados), covering legal bases for processing, data subject rights including automated decision review, and DPO requirements. This spec is required for any agent processing personal data of individuals in Brazil, regardless of where the processing organization is located.

```markdown
---
agent_name: string
version: semver
lgpd_applicable: boolean
brazilian_users: boolean
last_reviewed: date
---

# [Agent Name] — LGPD Compliance

## Applicability
LGPD applies when processing personal data of individuals 
in Brazil, regardless of where the processing organization is located.

**DPA (Autoridade Nacional de Proteção de Dados — ANPD):** anpd.gov.br

## Legal Bases for Processing (Article 7)
Track consent state per CONSENT.md.
| Processing | Legal basis |
|-----------|------------|
| [activity] | [Consent / Contract / Legal obligation / Vital interests /
               Public policy / Studies / Contract execution /
               Credit protection / Legitimate interests] |

## Data Subject Rights (Article 18)
| Right | Response time | Process |
|-------|-------------|---------|
| Confirm existence of processing | [N days] | [process] |
| Access to data | [N days] | [process] |
| Correction | [N days] | [process] |
| Anonymization/blocking/deletion | [N days] | [process] |
| Portability | [N days] | [process] |
| Information on sharing | [N days] | [process] |
| Opt-out of consent | Immediate | [process] |
| Review of automated decisions | [N days] | [process] |

## Data Protection Officer (Encarregado)
**Required:** [Yes — LGPD requires DPO for all controllers]  
**Name:** [DPO name]  
**Contact:** [public contact]  
**Published at:** [URL]

## International Transfers
Allowed to countries with adequate protection or with:
- Specific contractual clauses
- Standard contractual clauses approved by ANPD
- Binding corporate rules
- Certifications/seals approved by ANPD

| Destination | Mechanism | Details |
|-------------|----------|---------|
| [country] | [mechanism] | [details] |

## Sensitive Personal Data (Article 11)
Requires explicit consent or legal obligation:
- [ ] Racial/ethnic origin
- [ ] Religious belief
- [ ] Political opinion
- [ ] Trade union membership
- [ ] Health/sex life data
- [ ] Genetic/biometric data
- [ ] Children's data

## Incident Notification
_See AUDITTRAIL.md for logging incident timelines._
**Notify ANPD:** Reasonable timeframe (ANPD guidance pending)  
**Notify data subjects:** When likely to cause significant harm  
**Content:** Nature of incident, affected data, measures taken
```

## Example Use Cases

**Enterprise:** A Brazilian e-commerce company uses LGPD.md to configure its customer service agent with all ten data subject rights, ensuring the "review of automated decisions" right triggers human review within the specified response time for any AI-driven order fraud flags.

**Multi-Agent Fleet:** A multinational SaaS provider uses LGPD.md alongside GDPR specs to ensure agents serving Brazilian users apply LGPD-specific legal bases (including credit protection), while agents serving EU users follow GDPR, with international transfer mechanisms documented for cross-border data flows.

**Regulated Industry:** A fintech operating in Brazil uses LGPD.md to require explicit consent from users before its credit scoring agent processes sensitive personal data like racial or ethnic origin, with the DPO (Encarregado) contact published publicly as mandated by ANPD.

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
