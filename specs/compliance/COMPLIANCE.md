---
spec_name: COMPLIANCE.md
spec_version: 0.1.0
category: Compliance
domain: compliancemd.dev
priority: High
volume: "Vol 1 — Core Agent Specs"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# COMPLIANCE.md

**Category:** Compliance
**Domain:** compliancemd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Documents regulatory compliance requirements, approved procedures,
and audit trail requirements for agents operating in regulated industries.
For jurisdiction-specific rules, see REGULATIONS.md.

### Spec

```markdown
---
agent_name: string
version: semver
regulatory_frameworks: list   # [SOC2, ISO27001, HIPAA, PCI-DSS, etc.]
audit_trail_required: boolean
last_compliance_review: date
next_review_due: date
---

# [Agent Name] — Compliance Configuration

## Applicable Frameworks
| Framework | Scope | Controls Relevant to This Agent |
|-----------|-------|--------------------------------|
| SOC2 Type II | Data security | CC6.1, CC7.1, CC8.1 |
| [Other] | [scope] | [controls] |

## Required Audit Trail
Every action must be logged per AUDITTRAIL.md with:
- Timestamp (UTC, millisecond precision)
- Action type
- Input data (hash only for PII)
- Output data (hash only for PII)
- User or system that triggered the action
- Outcome (success | failure | partial)

Log destination: [immutable log store location]  
Log retention: [X years]  
Log access: restricted to [roles]

## Prohibited Actions
In this regulatory context, this agent must NEVER:
- [Specific prohibited action for this industry]
- [Another prohibition]

## Required Controls
- [ ] All data encrypted in transit (TLS 1.2+)
- [ ] All data encrypted at rest (AES-256)
- [ ] Access logging enabled
- [ ] Privileged access requires MFA
- [ ] Data classification applied to all outputs

## Approval Gates
These actions require documented approval before execution:
| Action | Approver | Documentation Required |
|--------|----------|----------------------|
| [Action] | [Role] | [Document type] |

## Evidence Collection
For audits, this agent must be able to provide:
- [ ] Complete action log for any date range
- [ ] Proof of encryption in use
- [ ] Access control list at any point in time
- [ ] Change history for all configuration files
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| AUDITTRAIL.md | Tamper-proof action logging |
| CONSENT.md | User consent lifecycle |
| ENFORCEMENT.md | Policy verification and compliance |
| PROVENANCE.md | Data lineage and trust classification |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
