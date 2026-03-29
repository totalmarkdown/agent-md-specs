---
spec_name: MEMORY.md
spec_version: 0.1.0
category: Cognitive
domain: memorymd.dev
priority: High
volume: "Vol 6 — Hierarchy Completion & Identity Anchors"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
spec_type: static
---


# MEMORY.md

**Category:** Cognitive
**Domain:** 
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose

Defines what an agent remembers across sessions and how that memory is structured, classified, and curated. Without persistent memory governance, agents lose institutional knowledge at every session boundary, forcing users to re-explain context and risking inconsistent behavior over time.

**Note:** MEMORY.md is already used by Claude Code.  
This is the ENHANCED spec for TotalMarkdown compatibility.

````markdown
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

## Memory Scope Declaration

Every agent must declare the scope of its memory:

```yaml
memory_scope: individual | team | crew | org | global
shared_context_ref: [path to SHAREDCONTEXT.md if scope > individual]  # See SHAREDCONTEXT.md when scope > individual
````

- **individual**: Memory is private to this agent. Not shared.
- **team/crew/org/global**: Agent participates in a shared context pool.
  Must reference the applicable SHAREDCONTEXT.md file.

## Shared Context Integration

How this agent's individual memory interacts with shared context
(see SHAREDCONTEXT.md for the full shared memory pool governance):

### Reading from Shared Context
- Which shared context entries are loaded at session start
  (reference: SESSION.md inherited configuration)
- How shared context entries are merged with individual memory
- Conflict resolution: if individual memory contradicts shared context,
  which takes precedence? (default: shared context for facts,
  individual for preferences/learned behaviors)

### Writing to Shared Context
- What types of individual memory entries are eligible for promotion
  to shared context (e.g., confirmed facts, not speculative observations)
- Promotion criteria: minimum confidence threshold, human approval
  required, automatic for certain entry types
- Must comply with MEMORYSAFETY.md write gateway sanitization

## Memory Classification

Every memory entry carries a classification level:
- **public**: Can be shared with any agent or external system
- **internal**: Can be shared within the organization only
- **confidential**: Can be shared only with agents at same or higher clearance
- **restricted**: Cannot be shared — individual memory only

Classification must be assigned at write time and cannot be downgraded
without human approval (via ESCALATION.md). _See PERMISSIONS.md for how
agent clearance levels determine accessible classification tiers._
_See MEMORYSAFETY.md for classification enforcement and poisoning defense._

## Destruction Policy

Aligned with SESSION.md destruction policy:
- Session-scoped memories: destroyed when session ends
  (see SESSION.md for session lifecycle, destruction triggers, and what survives session end)
- Persistent individual memories: retained across sessions,
  subject to TTL and retention policy
- Shared context entries: governed by SHAREDCONTEXT.md retention policy,
  survive individual session destruction
- On agent decommissioning (see LEGACY.md for the full retirement
  process and what happens to memory on decommissioning): individual
  memories are archived or destroyed per retention policy; shared
  context entries persist (they belong to the team/org, not the agent)

## Example Use Cases

**Enterprise:** A project management agent maintains persistent memory of key architectural decisions, team preferences, and past sprint outcomes so that each new session starts with full project context rather than requiring re-explanation.

**Multi-Agent Fleet:** A fleet of support agents each maintain individual memories classified as "internal" while promoting confirmed resolution patterns to a shared context pool, ensuring institutional knowledge survives individual agent session boundaries.

**Regulated Industry:** A banking compliance agent's memory entries carry classification levels (confidential for client data, public for regulatory guidance), with destruction policies aligned to data-retention regulations that automatically archive entries after the mandated holding period.

## Related Specs

| Spec | Relationship |
|------|-------------|
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| LEGACY.md | Retirement and decommissioning |
| MEMORYSAFETY.md | Memory poisoning defense |
| PROVENANCE.md | Data lineage and trust classification |
| SESSION.md | Ephemeral runtime identity and task scope |
| SHAREDCONTEXT.md | Multi-agent shared memory pool |
| SOUL.md | Agent personality and values |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
