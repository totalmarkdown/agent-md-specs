---
spec_name: CONSENT.md
spec_version: 0.1.0
category: Compliance
priority: High
tier: core
---

# [REPLACE THIS — Agent Name] — User Consent

<!-- Consent lifecycle: how user permission is obtained, tracked, and revoked -->

## Consent Model
- **Type:** [REPLACE THIS — opt-in | opt-out | granular | implicit]
- **Jurisdiction:** [REPLACE THIS — GDPR | CCPA | none | custom]
- **Default state:** [REPLACE THIS — no consent assumed | basic consent assumed]

## Consent Categories
<!-- What the user is consenting to -->

| Category | Required | Default | Description |
|----------|----------|---------|-------------|
| [REPLACE THIS — e.g. data collection] | [REPLACE THIS] | [REPLACE THIS — granted | denied] | [REPLACE THIS] |
| [REPLACE THIS — e.g. action execution] | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |
| [REPLACE THIS — e.g. data sharing] | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |
| [REPLACE THIS — e.g. memory retention] | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |

## Consent Collection
- **Method:** [REPLACE THIS — explicit prompt | config file | API | UI toggle]
- **Timing:** [REPLACE THIS — before first action | on-demand | at setup]
- **Record format:** [REPLACE THIS — how consent is stored — timestamp + scope + user ID]

## Revocation
- **Method:** [REPLACE THIS — command | API | config change | UI]
- **Effect:** [REPLACE THIS — immediate halt | finish current task then halt | scheduled]
- **Data handling on revoke:** [REPLACE THIS — delete user data | anonymize | retain with flag]

## Re-consent
- **Triggered by:** [REPLACE THIS — e.g. spec version change, scope expansion, 12-month refresh]
- **Grace period:** [REPLACE THIS — how long agent operates under old consent before requiring re-consent]

## Audit
- **Consent log location:** [REPLACE THIS — path or system]
- **Retention of consent records:** [REPLACE THIS — duration]
- **Proof of consent:** [REPLACE THIS — how consent can be demonstrated to auditors]

## Related Specs
- OWNER.md: [REPLACE THIS — path]
- AUDITTRAIL.md: [REPLACE THIS — path]
- PERMISSIONS.md: [REPLACE THIS — path]
