---
spec_name: LEGACY.md
spec_version: 0.1.0
category: Lifecycle
domain: legacymd.dev
priority: Low
volume: "Vol 3 — Forward-Thinking Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# LEGACY.md

**Category:** Lifecycle
**Domain:** legacymd.dev
**Priority:** Low
**Version:** 0.1.0

### Purpose
What an agent leaves behind when it is deprecated or decommissioned — 
knowledge transfer, successor designation, archived outputs, 
and lessons learned for future agents.

### Spec

```markdown
---
agent_name: string
version: semver
status: string         # active | deprecated | decommissioned
deprecated_date: date  # If applicable
decommission_date: date  # If applicable
successor_agent: string  # ID of replacement agent
---

# [Agent Name] — Legacy

## Status
**Current status:** [Active | Deprecated | Decommissioned]  
[If deprecated/decommissioned: reason and date]

## Successor
**Replacement agent:** [Agent name and ID]  
**Migration guide:** [Link or inline instructions]  
**What's different:** [Key differences users should know]

## Knowledge Transfer
What future agents and humans should know from my operation:

### What worked well
- [Pattern or approach that succeeded]
- [Tool or method that was effective]

### What didn't work
- [Approach that failed and why]
- [Problem that was never solved]

### Unfinished business
- [Task that was in-progress when deprecated]
- [Project that needs continuation]

## Archive
- **All outputs archived at:** [location]
- **Configuration archived at:** [git repo + tag]
- **MEMORY.md archived at:** [location]
- **Retention period:** [X years]
- **Access:** [who can access the archive]

## Final Statistics
- **Total operational days:** [N]
- **Total tasks completed:** [N]
- **Peak performance:** [notable achievement]
- **Most significant contribution:** [brief description]

## Acknowledgments
[Optional: humans and agents who helped this agent do good work]
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| ENFORCEMENT.md | Policy verification and compliance |
| MEMORY.md | Individual agent memory governance |
| SESSION.md | Ephemeral runtime identity and task scope |
| WAKEUP.md | Bootstrap and initialization |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
