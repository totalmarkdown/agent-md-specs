---
spec_name: MEMORY.md
spec_version: 0.1.0
category: Cognitive
domain: 
priority: High
volume: "Vol 6 — Hierarchy Completion & Identity Anchors"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# MEMORY.md

**Category:** Cognitive
**Domain:** 
**Priority:** High
**Version:** 0.1.0

## MEMORY.md (Agent-specific format)
**Category:** Cognitive  
**Note:** MEMORY.md is already used by Claude Code.  
This is the ENHANCED spec for TotalMarkdown compatibility.

```markdown
---
agent_name: string
version: semver
memory_type: string      # session | persistent | long-term
max_size_chars: number   # Truncate/summarize above this
last_updated: datetime
auto_curate: boolean     # Agent manages its own memory
---

# [Agent Name] — Memory

## About This Memory File
This file is automatically maintained by [Agent Name].
It is loaded at the start of every session.
Maximum size: [N] characters (condensed if exceeded)
Last updated: [datetime]

## Project Context
[What this agent knows about the current project]

## Key Decisions Made
| Decision | Rationale | Date | Revisit if |
|----------|-----------|------|-----------|
| [decision] | [why] | [date] | [condition] |

## Patterns I've Noticed
[Recurring patterns in the work or the data]

## What's Worked Well
[Approaches that have produced good results]

## What Hasn't Worked
[Approaches to avoid]

## Current State
[Where things stand right now — updated each session]

## Pending Items
[Things I need to follow up on]

## People and Agents I've Worked With
| Name | Type | Context | Last interaction |
|------|------|---------|----------------|
| [name] | [human/agent] | [how we've worked together] | [date] |

## Curation Rules
When this file exceeds [N] characters:
1. Summarize "What's Worked Well" and "What Hasn't" 
2. Archive decisions older than [N days] to memory-archive/
3. Remove resolved pending items
4. Keep "Current State" always fresh

## Memory Archive
Older memory condensed into: memory-archive/[YYYY-MM].md
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
