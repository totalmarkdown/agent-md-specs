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
Defines the license terms for an agent bundle on the marketplace — 
what buyers can and cannot do with the files, attribution requirements, 
commercial use rules, and modification rights.

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

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
```
