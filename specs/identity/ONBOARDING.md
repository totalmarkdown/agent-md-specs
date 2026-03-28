---
spec_name: ONBOARDING.md
spec_version: 0.1.0
category: Identity
domain: onboardingmd.dev
priority: Medium
volume: "Vol 1 — Core Agent Specs"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# ONBOARDING.md

**Category:** Identity
**Domain:** onboardingmd.dev
**Priority:** Medium
**Version:** 0.1.0

### Purpose
Provides context for new agents or humans joining a project mid-stream —
the project history, key decisions made, current state, and who to ask 
about what. The "new hire handbook" for an AI-managed project.

### Spec

```markdown
---
project_name: string
version: semver
last_updated: date
updated_by: string
---

# [Project Name] — Onboarding Guide

## What Is This Project?
[2-3 paragraph plain-language description]
[What problem does it solve? For whom? What's the current state?]

## Key Decisions Made
Decisions that are final and should not be relitigated:
| Decision | Rationale | Date |
|----------|-----------|------|
| [Decision] | [Why we chose this] | [date] |

## Current State
- **Phase:** [What stage of development/operation]
- **What's working:** [List]
- **Known issues:** [List with links to tracking tickets]
- **What's in progress:** [List with owners]

## File Map
| File | Purpose | Who maintains it |
|------|---------|-----------------|
| [file] | [what it does] | [owner] |

## Agent Fleet
See ROSTER.md for full details. Check PERMISSIONS.md for access grants. Quick reference:
- **[Agent]:** [one-line description]
- **[Agent]:** [one-line description]

## Humans on This Project
| Name | Role | Contact | Availability |
|------|------|---------|--------------|
| [Name] | [Role] | [contact] | [timezone/hours] |

## First Week Priorities
For a new agent starting on this project (see WAKEUP.md for session startup):
1. Read [files in priority order]
2. [First task to attempt]
3. [Who to ask about what]

## Common Mistakes to Avoid
- [Gotcha 1]: [How to avoid it]
- [Gotcha 2]: [How to avoid it]

## Glossary
See GLOSSARY.md for full terminology.
Key terms for quick reference:
- **[Term]:** [Brief definition]
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| ATTESTATION.md | Identity verification and credential lifecycle |
| CONTACT.md | Reachable endpoints |
| ENFORCEMENT.md | Policy verification and compliance |
| ROSTER.md | Team member registry |
| SOUL.md | Agent personality and values |
| WHOAMI.md | Agent identity declaration |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
