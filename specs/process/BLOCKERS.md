---
spec_name: BLOCKERS.md
spec_version: 0.1.0
category: Process
domain: blockersmd.dev
priority: Medium
volume: "Vol 3 — Forward-Thinking Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# BLOCKERS.md

**Category:** Process
**Domain:** blockersmd.dev
**Priority:** Medium
**Version:** 0.1.0

### Purpose
Active blockers preventing an agent from completing its work. 
Makes impediments visible to humans and other agents so they 
can be resolved. The async equivalent of raising your hand in 
a standup.

### Spec

```markdown
---
agent_name: string
version: semver
blocker_count: number
last_updated: datetime
---

# [Agent Name] — Active Blockers

## Summary
[N] active blockers. [N] blocking work completely, [N] causing slowdown.

## Active Blockers

### BLOCKER-[N]: [Title]
- **Severity:** blocking | slowing | annoying
- **Since:** [when this became a blocker]
- **Affects:** [which tasks/goals are blocked]
- **Description:** [what exactly is blocked and why]
- **What I need:** [specific ask — decision, resource, access, information]
- **From whom:** [who can unblock this]
- **My attempted workarounds:** [what I've already tried]
- **ETA if unresolved:** [when this becomes critical]
- **Status:** [waiting | in-progress | escalated]

[Repeat for each blocker]

## Recently Resolved
| Blocker | Resolved by | How | Date |
|---------|------------|-----|------|
| [title] | [who] | [how] | [date] |

## How to Unblock Me
Contact: [how to reach agent owner]  
Response needed within: [timeframe based on severity]
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
