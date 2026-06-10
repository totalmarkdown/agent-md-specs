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
spec_type: static
---


# COMPLIANCE.md

**Category:** Compliance
**Domain:** compliancemd.dev
**Priority:** High
**Version:** 0.1.0 **Type:** Static

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

## Example Use Cases

**Enterprise:** A global insurance company configures COMPLIANCE.md for its claims-processing agents with SOC 2 controls, PCI-DSS requirements for payment data, and approval gates requiring documented sign-off before any claim exceeding $50K is auto-settled.

**Multi-Agent Fleet:** A fintech platform maps each agent in its fleet to the specific compliance framework controls it must satisfy, enabling automated pre-deployment checks that block any agent missing required encryption or access-logging configurations.

**Regulated Industry:** A legal services firm's document-review agents use COMPLIANCE.md to enforce attorney-client privilege protections, requiring that all privileged material access is logged with justification and that outputs never include privileged content without explicit approval.

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
