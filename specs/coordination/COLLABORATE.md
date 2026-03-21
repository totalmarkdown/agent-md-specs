---
spec_name: COLLABORATE.md
spec_version: 0.1.0
category: Coordination
domain: collaboratemd.dev
priority: High
volume: "Vol 2 — Extended Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# COLLABORATE.md

**Category:** Coordination
**Domain:** collaboratemd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Defines how multiple humans and agents collaborate on shared work — 
roles, responsibilities, communication norms, review processes, 
conflict resolution, and contribution guidelines.

### When to create
Any project or workspace with 2+ contributors (human or AI). 
Especially important when mixing human and AI contributors 
to set clear expectations for both.

### Spec

```markdown
---
project_name: string
version: semver
contributor_count: number
human_count: number
agent_count: number
collaboration_model: string  # async | real-time | hybrid
created: date
updated: date
---

# [Project Name] — Collaboration Guide

## Team Composition
| Contributor | Type | Role | Availability | Contact |
|------------|------|------|--------------|---------|
| [Name] | Human | [Role] | [timezone/hours] | [contact] |
| [Agent] | AI | [Role] | 24/7 | [invocation] |

## Contribution Model
**Model:** [async | real-time | hybrid]  
**Primary communication channel:** [Slack | email | comments in tool]  
**Meeting cadence:** [daily standup | weekly sync | async only]

## Work Assignment
- New tasks assigned by: [human lead | rotation | agent triage]
- Agent tasks: [types of work agents handle autonomously]
- Human tasks: [types of work requiring human judgment]
- Collaborative tasks: [work requiring both human + agent]

## Review Process
All contributions go through:
1. **Self-review:** Author checks against acceptance criteria
2. **Agent review:** [which agent reviews, what it checks]
3. **Human review:** [who reviews, turnaround time]
4. **Approval:** [how many approvals needed to merge/accept]

### Review SLAs
- Agent review: within [X minutes]
- Human review: within [X hours/days]
- Escalated review: within [X hours]

## Contribution Guidelines

### For Humans
- Before starting: check [HANDOFF.md | task board] for current status
- Minimum change size: [avoid trivial edits — batch small changes]
- Documentation: update [relevant MD files] when making changes
- Communication: notify team in [channel] for changes affecting others

### For Agents
- Before starting: read current MEMORY.md for project context
- Scope: only modify files within designated workspace path
- Attribution: always record changes in document_attributions
- Uncertain? Escalate per ESCALATION.md rather than guessing
- After completing: update MEMORY.md with learnings

## Conflict Resolution

### Content conflicts (two contributors edited same section)
1. Later edit wins by default (last-write-wins per REPAIR.md)
2. Losing version preserved in version history
3. Human reviewer flags if losing version had important content
4. Add comment explaining the merge decision

### Opinion conflicts (disagreement on approach)
1. Both positions documented in a comment thread
2. Decision escalated to [role] for final call
3. Decision logged in HANDOFF.md with rationale
4. No contribution blocked more than [X hours] waiting for resolution

### Human vs Agent conflict
- Agent output that contradicts human decision: human wins
- Human can override any agent contribution with comment explaining why
- Agent should not re-assert overridden position

## Communication Norms
- Async first: default to written communication
- Response time: humans [X hours], agents [X minutes]
- Tagging: use @name to request human attention
- Urgency: prefix urgent messages with [URGENT]
- No blame: focus on the work, not the contributor
- Context: always include enough context for async readers

## Onboarding New Contributors
New humans: read ONBOARDING.md, then [list of files to read first]
New agents: read CLAUDE.md, MEMORY.md, ROSTER.md, this file
First contribution: [suggested starter task]
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
