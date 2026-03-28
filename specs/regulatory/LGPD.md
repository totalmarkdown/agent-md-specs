---
spec_name: LGPD.md
spec_version: 0.1.0
category: Regulatory Compliance
domain: lgpdmd.dev
priority: Medium
volume: "Vol 9 — Guardrails & Regulatory Compliance Library"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# LGPD.md

**Category:** Regulatory Compliance
**Domain:** lgpdmd.dev
**Priority:** Medium
**Version:** 0.1.0

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
**Notify ANPD:** Reasonable timeframe (ANPD guidance pending)  
**Notify data subjects:** When likely to cause significant harm  
**Content:** Nature of incident, affected data, measures taken
```

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
