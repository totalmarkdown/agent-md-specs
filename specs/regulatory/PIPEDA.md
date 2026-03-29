---
spec_name: PIPEDA.md
spec_version: 0.1.0
category: Regulatory Compliance
domain: pipedamd.dev
priority: Medium
volume: "Vol 9 — Guardrails & Regulatory Compliance Library"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---
> **Static Configuration** — committed to your repository


# PIPEDA.md

**Category:** Regulatory Compliance
**Domain:** pipedamd.dev
**Priority:** Medium
**Version:** 0.1.0

### Purpose

Configures compliance with Canada's PIPEDA and Quebec's Law 25, structuring privacy obligations around the 10 Fair Information Principles. This spec ensures agents handling personal information of Canadian residents implement meaningful consent, breach notification, and privacy-by-default requirements that vary by province.

```markdown
---
agent_name: string
version: semver
pipeda_applicable: boolean
canadian_users: boolean
quebec_law25: boolean    # Quebec's Law 25 — stricter than PIPEDA
last_reviewed: date
---

# [Agent Name] — PIPEDA Compliance

## Applicability
PIPEDA applies to commercial activities involving personal 
information of Canadian residents.  
**Quebec Law 25** (in effect since 2023) adds stricter requirements 
for Quebec residents.

## The 10 Fair Information Principles

### 1. Accountability
**Privacy Officer:** [name/role]  
**Contact:** [email]  
**Third parties:** Contractually required to maintain equivalent protection

### 2. Identifying Purposes
Purposes identified BEFORE or AT TIME of collection:  
| Purpose | Data used | Legal basis |
|---------|-----------|------------|
| [purpose] | [data] | [basis] |

### 3. Consent
Track consent lifecycle per CONSENT.md.
- Meaningful consent obtained before collection
- Language: plain, easy to understand
- Opt-in for sensitive information
- Withdrawal: available at any time
- No bundled consent for unrelated purposes

### 4. Limiting Collection
Collect only what is necessary for stated purpose.

### 5. Limiting Use, Disclosure, Retention
- Used only for purpose collected
- Retained only as long as necessary
- Retention schedule: [schedule]

### 6. Accuracy
Personal information kept accurate, complete, up-to-date.  
Correction process: [how individuals can correct info]

### 7. Safeguards
Security measures appropriate to sensitivity:  
[Description of security measures per SECURITY.md]

### 8. Openness
Privacy policy: [URL]  
Available in: [English | French | both]

### 9. Individual Access
Response time: 30 days  
Process: [how to request access]  
Exceptions: [legal privilege, third party info, etc]

### 10. Challenging Compliance
Process for complaints: [process]  
Office of the Privacy Commissioner: [URL]

## Quebec Law 25 Additions
For Quebec residents:
- Privacy Impact Assessment (PIA) required for new systems
- Explicit consent for sensitive data
- Privacy by default required
- Right to be forgotten
- Automated decision-making disclosure
- Commissioner notification for breaches with real risk of injury

## Breach Notification
_See AUDITTRAIL.md for logging all breach notifications._
**Threshold:** Real risk of significant harm  
**Notify OPC:** As soon as reasonably possible  
**Notify individuals:** As soon as reasonably possible  
**Record keeping:** All breaches recorded, retain 24 months
```

## Example Use Cases

**Enterprise:** A Canadian insurance company uses PIPEDA.md to configure its claims processing agent with all 10 Fair Information Principles, ensuring meaningful consent is obtained in plain language before collecting policyholder medical information.

**Multi-Agent Fleet:** A cross-border SaaS provider uses PIPEDA.md alongside Quebec Law 25 additions for agents serving Quebec residents, requiring Privacy Impact Assessments for new agent capabilities and privacy-by-default settings that go beyond baseline PIPEDA requirements.

**Regulated Industry:** A Canadian telecom uses PIPEDA.md to implement breach notification for its customer service agent, recording all breaches and retaining records for 24 months while notifying the Office of the Privacy Commissioner whenever there is a real risk of significant harm.

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
