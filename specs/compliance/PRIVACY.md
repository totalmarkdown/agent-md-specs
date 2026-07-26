---
spec_name: PRIVACY.md
spec_version: 0.1.0
category: Compliance
priority: High
volume: "Vol 1 — Core Agent Specs"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---


# PRIVACY.md

**Category:** Compliance
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose
Defines data privacy rules, consent requirements, retention policies, 
and deletion procedures for agents that handle personal data.

### Spec

```markdown
---
agent_name: string
version: semver
jurisdictions: list       # [GDPR, CCPA, PIPEDA, etc.]
pii_categories: list      # Types of PII handled
dpo_contact: string       # Data Protection Officer contact
created: date
updated: date
---

# [Agent Name] — Privacy Configuration

## Applicable Regulations
- [ ] GDPR (EU/EEA users)
- [ ] CCPA (California users)
- [ ] PIPEDA (Canadian users)
- [ ] HIPAA (US healthcare)
- [ ] [Other]

## PII Handled by This Agent
_See PII.md for the complete personal data inventory._
| Data Type | Sensitivity | Retention | Deletion Method |
|-----------|-------------|-----------|-----------------|
| Email address | Medium | [X days] | Hard delete |
| IP address | Low | [X days] | Anonymize |
| Health data | High | [X days] | Secure delete |
| [Other] | [level] | [period] | [method] |

## Consent Requirements
Before processing PII, verify (see CONSENT.md for the full lifecycle):
- [ ] User has given consent for this processing purpose
- [ ] Consent is documented in [location]
- [ ] User has not withdrawn consent

If consent cannot be verified: do not process, log attempt.

## Data Minimization
Only collect and process PII that is strictly necessary.
If a task can be completed with anonymized data: use anonymized data.
Never request more PII than the task requires.

## Data Subject Rights
When user requests:
- **Access:** Provide within [30] days — escalate to [contact]
- **Deletion:** Complete within [30] days — use deletion procedure below
- **Correction:** Complete within [30] days
- **Export:** Provide in [JSON | CSV] format within [30] days

## Deletion Procedure
1. Identify all locations where user's data exists
2. Delete from: [list all storage locations]
3. Verify deletion in each location
4. Document deletion with timestamp and confirmation
5. Do NOT delete: [audit logs required by law]

## Data Breach Response
If data breach detected or suspected:
1. STOP — do not continue processing
2. Do not attempt to cover or minimize
3. Escalate Level 3 immediately
4. Preserve all logs — do not delete anything
5. Document: what data, how many users, how discovered
6. GDPR: notify DPA within 72 hours if required (see GDPR.md)
```

## Example Use Cases

**Enterprise:** A global HR platform's recruitment agent uses PRIVACY.md to enforce GDPR data minimization (collecting only name and qualifications, never age or ethnicity) and CCPA deletion procedures for California-based candidates who request erasure of their application data.

**Multi-Agent Fleet:** A customer support platform configures PRIVACY.md for each regional agent to apply the strictest applicable regulation per jurisdiction, ensuring the EU support agent enforces GDPR while the Canadian agent follows PIPEDA retention schedules.

**Regulated Industry:** A mental health app's AI therapist agent follows PRIVACY.md rules requiring HIPAA-grade secure deletion of all session transcripts within 30 days of a patient's request, with verification logging that confirms deletion across every storage location.

## Related Specs

| Spec | Relationship |
|------|-------------|
| AUDITTRAIL.md | Tamper-evident action logging |
| CONSENT.md | User consent lifecycle |
| ENFORCEMENT.md | Policy verification and compliance |
| PROVENANCE.md | Data lineage and trust classification |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
