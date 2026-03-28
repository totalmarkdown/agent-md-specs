---
spec_name: LICENSE.md
spec_version: 0.1.0
category: Legal
domain: licensemd.dev
priority: Medium
volume: "Vol 2 — Extended Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# LICENSE.md

**Category:** Legal
**Domain:** licensemd.dev
**Priority:** Medium
**Version:** 0.1.0

### Purpose
Defines the license terms for an agent bundle on the marketplace --
what buyers can and cannot do with the files, attribution requirements,
commercial use rules, and modification rights (see PRICING.md for the commercial terms).

### Spec

```markdown
---
bundle_name: string
author: string
version: semver
license_type: string   # MIT | Apache-2.0 | CC-BY | proprietary | custom
commercial_use: boolean
modification_allowed: boolean
distribution_allowed: boolean
created: date
---

# [Bundle Name] — License

## License Type
**[License name]** — [brief description of what this means]

## Permissions
| Permission | Allowed |
|-----------|---------|
| Personal use | ✓ |
| Commercial use | [✓/✗] |
| Modification | [✓/✗] |
| Distribution | [✓/✗] |
| Private use | ✓ |
| Sublicensing | [✓/✗] |
| Patent use | [✓/✗] |

## Conditions
| Condition | Required |
|-----------|---------|
| License notice | [✓/✗] — include this LICENSE.md with distributions |
| Copyright notice | [✓/✗] — retain author credit |
| State changes | [✓/✗] — document modifications made |
| Same license | [✓/✗] — derivatives must use same license |

## Limitations
| Limitation | |
|-----------|--|
| Liability | Author provides no warranty |
| Trademark | Cannot use author's name/brand to endorse derivatives |
| Patent claims | [any patent restrictions] |

## Attribution
If required, use this attribution:
> "[Bundle name]" by [author] — [link to original]

## Commercial License
For commercial use beyond what this license permits:
Contact: [email or marketplace profile URL]
Custom licensing available for enterprise deployments.

## Full License Text
[Full text of chosen license, or link to standard license text]

## Example Use Cases

**Enterprise:** A large consulting firm evaluates an agent bundle's LICENSE.md to confirm that Apache-2.0 terms permit internal modification and redistribution to client environments without requiring open-sourcing of their proprietary configurations.

**Multi-Agent Fleet:** A platform operator checks LICENSE.md for every agent in the fleet to ensure all license conditions (attribution, same-license derivatives) are satisfied before bundling agents into a commercial product offering.

**Regulated Industry:** A financial services company's compliance team reviews LICENSE.md to verify that a data-analysis agent's license permits use in regulated environments and does not include clauses that conflict with their data-retention or audit obligations.

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
