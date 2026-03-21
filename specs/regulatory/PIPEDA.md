---
spec_name: PIPEDA.md
spec_version: 0.1.0
category: Regulatory Compliance
domain: pipedamd.dev
priority: Medium
volume: "Vol 9 — Guardrails & Regulatory Compliance Library"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# PIPEDA.md

**Category:** Regulatory Compliance
**Domain:** pipedamd.dev
**Priority:** Medium
**Version:** 0.1.0

**Priority:** MEDIUM — Canadian users  
**Regulation:** Personal Information Protection and Electronic Documents Act  
**Version:** 0.1.0

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
**Threshold:** Real risk of significant harm  
**Notify OPC:** As soon as reasonably possible  
**Notify individuals:** As soon as reasonably possible  
**Record keeping:** All breaches recorded, retain 24 months
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
