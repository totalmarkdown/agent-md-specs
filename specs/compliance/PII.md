---
spec_name: PII.md
spec_version: 0.1.0
category: Compliance
domain: piimd.dev
priority: High
volume: "Vol 8 — Repos, Compliance & The Weird Wonderful Ones"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---


# PII.md

**Category:** Compliance
**Domain:** piimd.dev
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose

Defines how the agent identifies, inventories, and handles personally identifiable information across all data categories it processes. A complete PII inventory is the foundation for data subject rights compliance, breach response, and regulatory reporting under frameworks like GDPR and HIPAA.

```markdown
---
agent_name: string
version: semver
pii_handled: boolean
dpo_contact: string
last_audit: date
---

# [Agent Name] — PII Data Inventory

**Does this agent handle PII?** [Yes | No]

## PII Categories Handled
- [ ] Names and identity
- [ ] Contact info (email, phone, address)
- [ ] Financial information
- [ ] Health/medical data
- [ ] Biometric data
- [ ] Location data
- [ ] Behavioral/usage data
- [ ] Government IDs
- [ ] Children's data

## Complete Inventory

### [Data Type: e.g. Email Address]
| Property | Details |
|----------|---------|
| Sensitivity | [Low/Medium/High] |
| Volume | [~N records] |
| Source | [How collected] |
| Purpose | [Why processed] |
| Legal basis | [Consent/Contract/Legitimate interest/Legal obligation] |
| Storage | [Database, table] |
| Encryption | [At rest: AES-256, In transit: TLS 1.3] |
| Retention | [N days from collection] |
| Deletion | [Hard delete/Anonymization] |
| Shared with | [None/List] |
| User access | [Yes — via [process]] |
| User deletion | [Yes — via [process]] |

## Data Subject Rights
_See PRIVACY.md for the full data subject rights handling procedures._
| Right | Supported | SLA |
|-------|----------|-----|
| Access | [✓/✗] | [N days] |
| Rectification | [✓/✗] | [N days] |
| Erasure | [✓/✗] | [N days] |
| Portability | [✓/✗] | [N days] |

## Breach Response
See CONSENT.md for user notification requirements during a breach.
1. Immediately: Isolate affected system
2. Within 1hr: Notify DPO
3. Within 72hrs: Notify DPA (GDPR requirement)
4. Document: data affected, volume, how discovered

**DPO:** [contact]
```

## Example Use Cases

**Enterprise:** A customer-analytics agent maintains a complete PII inventory documenting that it processes email addresses (medium sensitivity, 90-day retention) and behavioral data (low sensitivity, anonymized after 30 days), enabling the DPO to respond to data-subject access requests within the 30-day SLA.

**Multi-Agent Fleet:** A fleet operator uses PII.md across all agents to generate a unified data map showing which agents handle which PII categories, automatically detecting when a new agent begins processing a data type not covered by existing consent records.

**Regulated Industry:** A healthcare platform's billing agent uses PII.md to document its handling of patient financial information with HIPAA-compliant encryption standards and breach notification procedures, including the 72-hour DPA notification requirement for any data exposure.

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
