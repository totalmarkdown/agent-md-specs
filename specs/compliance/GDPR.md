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
---

# GDPR.md

**Category:** Compliance
**Domain:** gdprmd.dev
**Priority:** High
**Version:** 0.1.0

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
- Collected via: [explicit opt-in]
- Withdrawal: [as easy as giving]
- Pre-ticked boxes: Never (invalid under GDPR)

## International Transfers
| Destination | Data types | Transfer mechanism |
|-------------|-----------|-------------------|
| [Country] | [types] | [SCCs/BCRs] |

## Privacy by Design
- Purpose limitation: [how enforced]
- Data minimisation: [how achieved]
- Storage limitation: [retention policy]
- Integrity: [security measures]

## Supervisory Authority
**Lead DPA:** [Name and country]  
**Contact:** [URL]  
**DPA available:** [URL]
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
