---
spec_name: ALIASES.md
spec_version: 0.1.0
category: Identity
domain: aliasesmd.dev
priority: Low
volume: "Vol 8 — Repos, Compliance & The Weird Wonderful Ones"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# ALIASES.md

**Category:** Identity
**Domain:** aliasesmd.dev
**Priority:** Low
**Version:** 0.1.0

```markdown
---
agent_name: string   # Canonical current name
agent_id: string     # UUID — authoritative
---

# [Agent Name] — Aliases

## Canonical Name
**[Agent Name]** — use this in all references (see WHOAMI.md).

## Previous Names
| Name | Used from | Until | Why changed |
|------|----------|-------|------------|
| [Old name] | [date] | [date] | [reason] |

## Nicknames (not official)
| Nickname | Used by | Context |
|---------|---------|---------|
| [nickname] | [community] | [informal use] |

## Names I Answer To
- [Alias 1]
- [Alias 2]

## A Note on Identity
My UUID ([agent_id]) is my true identity (see ID.md).
Names change. The UUID never does.
When in doubt: ask for ID.md.
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| ATTESTATION.md | Identity verification and credential lifecycle |
| CONTACT.md | Reachable endpoints |
| ENFORCEMENT.md | Policy verification and compliance |
| ID.md | Permanent cryptographic identifier |
| SOUL.md | Agent personality and values |
| WHOAMI.md | Agent identity declaration |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
