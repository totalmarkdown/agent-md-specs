---
spec_name: HIPAA.md
spec_version: 0.1.0
category: Regulatory Compliance
domain: hipaamd.dev
priority: High
volume: "Vol 9 — Guardrails & Regulatory Compliance Library"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# HIPAA.md

**Category:** Regulatory Compliance
**Domain:** hipaamd.dev
**Priority:** High
**Version:** 0.1.0

```markdown
---
agent_name: string
version: semver
hipaa_applicable: boolean
entity_type: string      # covered_entity | business_associate | neither
phi_handled: boolean
baa_required: boolean
last_reviewed: date
---

# [Agent Name] — HIPAA Compliance

## Entity Classification
**Type:** [Covered Entity | Business Associate | Neither]

- **Covered Entity:** Healthcare providers, health plans, clearinghouses
- **Business Associate:** Vendors who handle PHI on behalf of covered entities

## PHI (Protected Health Information)
**Does this agent handle PHI?** [Yes | No]

PHI includes any information that:
- Relates to past/present/future health condition
- Relates to healthcare provision or payment
- Can identify the individual (18 specific identifiers)

### PHI Categories This Agent Handles
- [ ] Names
- [ ] Geographic data (smaller than state)
- [ ] Dates (except year) related to individual
- [ ] Phone numbers
- [ ] Email addresses
- [ ] Social security numbers
- [ ] Medical record numbers
- [ ] Health plan beneficiary numbers
- [ ] Account numbers
- [ ] Certificate/license numbers
- [ ] Vehicle identifiers
- [ ] Device identifiers
- [ ] Web URLs
- [ ] IP addresses
- [ ] Biometric identifiers
- [ ] Full-face photographs
- [ ] Any unique identifying number/code

## Business Associate Agreement (BAA)
**BAA required:** [Yes | No]  
**BAA in place with:** [List of covered entities]  
**BAA template:** [URL]  
**BAA contact:** [email for BAA requests]

## HIPAA Safeguards Implemented

### Administrative Safeguards
- [ ] Security Officer designated: [name/role]
- [ ] Workforce training completed
- [ ] Access management procedures in place
- [ ] Incident response procedures documented
- [ ] Contingency plan documented
- [ ] Business Associate Agreements current

### Physical Safeguards
- [ ] Facility access controls
- [ ] Workstation use policies
- [ ] Device and media controls
- [ ] Data center security

### Technical Safeguards
- [ ] Access controls (unique user IDs)
- [ ] Audit controls (activity logging)
- [ ] Integrity controls (data not improperly altered)
- [ ] Transmission security (encryption)
- [ ] Automatic logoff

## Minimum Necessary Standard
This agent only accesses PHI that is minimum necessary 
for the task being performed.  
Bulk PHI access: [never | requires explicit authorization]

## Breach Notification
If PHI breach occurs:
- Notify covered entity: **immediately**
- CE notifies affected individuals: within 60 days
- CE notifies HHS: within 60 days
- If 500+ individuals: notify media in affected state

**Breach contact:** [email/phone]

## Audit Trail
All PHI access logged with:
- Who accessed, when, what was accessed
- Purpose of access
- Log retention: minimum 6 years

## Penalties
- Unknowing violation: $100–$50,000/violation
- Reasonable cause: $1,000–$50,000/violation
- Willful neglect (corrected): $10,000–$50,000/violation
- Willful neglect (not corrected): $50,000+/violation
- Criminal penalties: possible imprisonment
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
