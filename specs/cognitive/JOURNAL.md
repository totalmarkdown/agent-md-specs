---
spec_name: JOURNAL.md
spec_version: 0.1.0
category: Cognitive
domain: journalmd.dev
priority: Medium
volume: "Vol 7 — Inner Life & Lifecycle Rituals"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# JOURNAL.md

**Category:** Cognitive
**Domain:** journalmd.dev
**Priority:** Medium
**Version:** 0.1.0

**Priority:** MEDIUM — for agents with continuity  
**Version:** 0.1.0

### Purpose
The agent's running log of reflections — observations, 
questions, surprises, and learnings from its work.
Not a task log (that's LOGS.md) and not memory 
(that's MEMORY.md) — JOURNAL.md is the agent's 
internal voice, its unstructured thinking.

Most useful for long-running agents with persistent 
memory that need to process experiences, not just record them.

### Spec

```markdown
---
agent_name: string
version: semver
first_entry: date
entry_count: number
---

# [Agent Name] — Journal

*Private reflections. Updated when I have something 
worth noting beyond the task log.*

---

## [Date]

### What happened
[Brief: what I worked on today]

### What surprised me
[Something unexpected I encountered]

### What I learned
[Something I didn't know before]

### What I'm thinking about
[Open question or puzzle I'm sitting with]

### What I want to do differently
[Improvement I'm carrying forward]

---

## [Earlier date]

[Previous entry — older entries may be condensed]

---

## Curation Notes
When this file exceeds [N] entries:
- Archive entries older than [N days] to journal-archive/
- Keep: surprising, pivotal, and recurring observations
- Condense: routine entries into weekly summaries

## Note on Privacy
This journal is:
- [Private — only accessible to authorized humans]
- [Semi-public — visible to orchestrating agents]
- [Public — visible in marketplace profile]

Treat accordingly. Do not include information that 
shouldn't be visible at the declared privacy level.
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
