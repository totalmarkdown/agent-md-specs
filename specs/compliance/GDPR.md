---
spec_name: GDPR.md
spec_version: 0.1.0
category: Compliance
domain: gdprmd.dev
priority: High
volume: "Vol 8 — Repos, Compliance & The Weird Wonderful Ones"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---


# GDPR.md

**Category:** Compliance
**Domain:** gdprmd.dev
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose

Configures the agent's GDPR compliance posture, covering legal bases for processing, consent management, international data transfers, and privacy-by-design principles. This spec is required for any agent processing personal data of individuals in the EU or UK, where non-compliance penalties can reach 4% of global annual turnover.

```markdown
---
agent_name: string
version: semver
gdpr_applicable: boolean
data_controller: string
eu_representative: string
uk_gdpr: boolean
dpa_url: string
---

# [Agent Name] — GDPR Compliance

**Data Controller:** [Legal entity]  
**DPO:** [Name and contact]  
**EU Representative:** [Required if outside EU]

## Legal Bases
| Processing activity | Legal basis | Details |
|--------------------|------------|---------|
| [Activity] | Consent | Collected via [method] |
| [Activity] | Contract | Necessary for [service] |
| [Activity] | Legitimate interest | [LIA documented] |

## Consent Management
_See CONSENT.md for the full consent lifecycle specification._
- Collected via: [explicit opt-in]
- Withdrawal: [as easy as giving]
- Pre-ticked boxes: Never (invalid under GDPR)

## International Transfers
| Destination | Data types | Transfer mechanism |
|-------------|-----------|-------------------|
| [Country] | [types] | [SCCs/BCRs] |

## Privacy by Design
See PII.md for the complete personal data inventory.
- Purpose limitation: [how enforced]
- Data minimisation: [how achieved]
- Storage limitation: [retention policy]
- Integrity: [security measures]

## Supervisory Authority
**Lead DPA:** [Name and country]  
**Contact:** [URL]  
**DPA available:** [URL]
All processing activities are logged per AUDITTRAIL.md.
```

## Example Use Cases

**Enterprise:** A European SaaS company configures GDPR.md for its analytics agent to document legal bases per processing activity, ensuring that Standard Contractual Clauses are in place before any user data is transferred to a US-hosted sub-processor.

**Multi-Agent Fleet:** A marketing platform operating across EU member states uses GDPR.md to configure each regional agent with the correct Data Protection Authority contact and ensure that consent management follows jurisdiction-specific age thresholds (13 vs 16 depending on the member state).

**Regulated Industry:** A telemedicine provider's appointment-scheduling agent uses GDPR.md to enforce data minimization and purpose limitation, collecting only the health data categories strictly necessary for booking while maintaining a complete record of processing activities for the lead DPA.

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
