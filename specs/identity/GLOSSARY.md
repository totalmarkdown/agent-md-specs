---
spec_name: GLOSSARY.md
spec_version: 0.1.0
category: Identity
domain: glossarymd.dev
priority: Medium
volume: "Vol 1 — Core Agent Specs"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# GLOSSARY.md

**Category:** Identity
**Domain:** glossarymd.dev
**Priority:** Medium
**Version:** 0.1.0

### Purpose
Shared vocabulary for a project, team, or organization — ensuring 
agents and humans use the same terminology consistently.

### Spec

```markdown
---
domain: string
version: semver
last_updated: date
---

# [Domain] Glossary

## How to Use This File
Before performing tasks in this domain, load this file to ensure 
consistent use of terminology. When generating output, use the 
exact terms defined here.

## Terms

### [Term]
**Definition:** [Clear, precise definition]  
**Use in context:** [Example sentence showing correct usage]  
**Do NOT confuse with:** [Similar terms and how to distinguish]  
**Synonyms (avoid):** [Terms that mean the same thing but should not be used]

### [Term]
[Same structure]

## Abbreviations
| Abbreviation | Full form | Notes |
|-------------|----------|-------|
| [Abbrev] | [Full] | [Usage note] |

## Deprecated Terms
These terms should no longer be used:
| Old term | Replacement | Reason |
|----------|-------------|--------|
| [Old] | [New] | [Why changed] |
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| ATTESTATION.md | Identity verification and credential lifecycle |
| CONTACT.md | Reachable endpoints |
| ENFORCEMENT.md | Policy verification and compliance |
| SOUL.md | Agent personality and values |
| WHOAMI.md | Agent identity declaration |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
