---
spec_name: GLOSSARY.md
spec_version: 0.1.0
category: Identity
priority: Medium
volume: "Vol 1 — Core Agent Specs"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---


# GLOSSARY.md

**Category:** Identity
**Priority:** Medium
**Version:** 0.1.0 **Type:** Static

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
consistent use of terminology (see ONBOARDING.md for first-time setup). When generating output, use the 
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
These terms should no longer be used (see VERSIONING.md for deprecation timelines):
| Old term | Replacement | Reason |
|----------|-------------|--------|
| [Old] | [New] | [Why changed] |
```

## Example Use Cases

**Enterprise:** A financial services team defines "AUM" as "Assets Under Management" in their glossary, ensuring every agent in the division uses the exact term instead of synonyms like "managed assets" or "portfolio value," eliminating ambiguity in generated reports.

**Multi-Agent Fleet:** A fleet of agents spanning legal, finance, and engineering domains each inherits the org-level glossary and adds domain-specific terms, so when a legal agent hands off a task to a finance agent, both use the same definition of "material adverse change."

**Regulated Industry:** A pharmaceutical agent's glossary defines "adverse event" with the exact FDA regulatory definition, preventing the agent from using looser synonyms that could cause misclassification in safety reports submitted to regulators.

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
