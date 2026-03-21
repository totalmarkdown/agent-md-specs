---
spec_name: NIS2.md
spec_version: 0.1.0
category: Regulatory Compliance
domain: nis2md.dev
priority: Medium
volume: "Vol 9 — Guardrails & Regulatory Compliance Library"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# NIS2.md

**Category:** Regulatory Compliance
**Domain:** nis2md.dev
**Priority:** Medium
**Version:** 0.1.0

**Priority:** MEDIUM — EU cybersecurity  
**Regulation:** Network and Information Security Directive 2 (EU, Oct 2024)  
**Version:** 0.1.0

```markdown
---
agent_name: string
version: semver
nis2_applicable: boolean
entity_type: string    # essential | important | neither
sector: string
member_state: string
last_reviewed: date
---

# [Agent Name] — NIS2 Compliance

## Applicability
NIS2 applies to medium and large entities in critical sectors 
and important sectors operating in the EU.

**Essential Entity sectors:** Energy, transport, banking, 
financial infrastructure, health, drinking water, 
wastewater, digital infrastructure, ICT services, 
public administration, space

**Important Entity sectors:** Postal/courier, waste management,
chemicals, food, manufacturing, digital providers, research

**This entity:** [Essential | Important | Not in scope]  
**Primary sector:** [sector]

## Registration
**Registered with:** [Member State competent authority]  
**Registration date:** [date]

## Security Measures (Article 21)

### Policies and Procedures
- [ ] Information security policy
- [ ] Risk analysis and information security policies
- [ ] Incident handling policies
- [ ] Business continuity (backups, disaster recovery, crisis management)
- [ ] Supply chain security
- [ ] Secure development policies
- [ ] Cybersecurity training
- [ ] Cryptography and encryption policy
- [ ] Human resources security
- [ ] Access control and asset management
- [ ] MFA / continuous authentication
- [ ] Secure communications (voice, video, text)

### Technical Measures
- [ ] Network segmentation
- [ ] Vulnerability management
- [ ] Patch management
- [ ] Penetration testing
- [ ] SIEM / security monitoring

## Incident Reporting (Article 23)
**What to report:** Significant incidents affecting service delivery

**Reporting timeline:**
| Report | When |
|--------|------|
| Early warning | Within 24 hours of becoming aware |
| Incident notification | Within 72 hours |
| Final report | Within 1 month |

**Report to:** [National CSIRT / Competent Authority]

## Supply Chain Security
ICT products and services used:
- [ ] Suppliers assessed for cybersecurity practices
- [ ] Contractual security requirements in place
- [ ] Software bill of materials (SBOM) maintained

## Management Accountability
Senior management responsibilities:
- [ ] Approve cybersecurity measures
- [ ] Oversee implementation
- [ ] Attend cybersecurity training
- [ ] Personally liable for non-compliance

## Penalties
- Essential entities: up to €10M or 2% global turnover
- Important entities: up to €7M or 1.4% global turnover
- Personal liability for management: possible
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
