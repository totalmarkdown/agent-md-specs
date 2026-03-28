---
spec_name: WORKFLOW.md
spec_version: 0.1.0
category: Process
domain: workflowmd.dev
priority: High
volume: "Vol 1 — Core Agent Specs"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# WORKFLOW.md

**Category:** Process
**Domain:** workflowmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Defines a repeatable, step-by-step process for an agent to follow. 
More detailed than SKILL.md (which defines capabilities), WORKFLOW.md 
defines complete end-to-end processes with decision points, loops, 
and conditional branches.

### When to create
When a task has 5+ steps, involves conditional logic, requires 
human approval at specific points, or needs to be reproducible 
across different sessions or agents.

### Spec

```markdown
---
workflow_name: string
version: semver
trigger: string          # What starts this workflow
estimated_duration: string  # e.g. "5-10 minutes"
requires_human: boolean  # Does any step require human approval?
created: date
updated: date
---

# [Workflow Name]

## Trigger
[Exact phrase or condition that starts this workflow]

## Prerequisites
- [What must be true before starting]
- [What files/data/access must be available]

## Steps

### Step 1: [Name]
**Action:** [Exactly what to do]  
**Input:** [What is consumed]  
**Output:** [What is produced]  
**Success condition:** [How to know this step succeeded]  
**On failure:** [What to do if this step fails]  

### Step 2: [Name]
[Same structure]

### Decision Point: [Condition]
- **If [condition A]:** Go to Step X
- **If [condition B]:** Go to Step Y
- **If uncertain:** [Escalate | Ask human | Use default]

### Human Approval Gate (if required)
**Requires approval from:** [Role or person]  
**What to present:** [What information to show the human]  
**Timeout:** [What to do if no response in X hours]

## Completion
[What defines successful completion]
[What artifacts are produced]
[Who/what to notify]

## Error Recovery
[See REPAIR.md for general recovery — list workflow-specific overrides here]
```

---

## Related Specs

| Spec | Relationship |
|------|-------------|
| DEADLINES.md | Time constraints and schedules |
| GOALS.md | Objectives and success criteria |
| REPAIR.md | Recovery and self-healing procedures |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
