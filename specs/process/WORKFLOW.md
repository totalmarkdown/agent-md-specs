---
spec_name: WORKFLOW.md
spec_version: 0.1.0
category: Process
priority: High
volume: "Vol 1 — Core Agent Specs"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---


# WORKFLOW.md

**Category:** Process
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose
Defines a repeatable, step-by-step process for an agent to follow. 
More detailed than SKILL.md (which defines capabilities), WORKFLOW.md 
defines complete end-to-end processes with decision points, loops, 
and conditional branches.

### When to create
When a task has 5+ steps, involves conditional logic, requires
human approval at specific points, or needs to be reproducible
across different sessions or agents. For multi-agent coordination,
see TEAM.md.

### Spec

```markdown
---
workflow_name: string
version: semver
trigger: string          # What starts this workflow
estimated_duration: string  # e.g. "5-10 minutes"
requires_human: boolean  # Does any step require human approval? See ESCALATION.md
intent_ref: string       # See INTENT.md — declare intent before execution
provenance_ref: string   # See PROVENANCE.md for data lineage tracking
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
**Intent:** [Declare what this step intends to accomplish] _(see INTENT.md — always declare before executing)_
**Input:** [What is consumed] _(track lineage per PROVENANCE.md)_
**Output:** [What is produced]
**Success condition:** [How to know this step succeeded]
**On failure:** [What to do if this step fails] _(see CIRCUITBREAKER.md for failure isolation)_

### Step 2: [Name]
[Same structure]

### Decision Point: [Condition]
- **If [condition A]:** Go to Step X
- **If [condition B]:** Go to Step Y
- **If uncertain:** Escalate per ESCALATION.md routing rules

### Human Approval Gate (if required)
**Requires approval from:** [Role or person] (see ESCALATION.md for routing)
**What to present:** [What information to show the human]
**Timeout:** [What to do if no response in X hours]

## Completion
[What defines successful completion]
[What artifacts are produced]
[Who/what to notify]

## Error Recovery
[See REPAIR.md for general recovery — list workflow-specific overrides here.]
Apply CIRCUITBREAKER.md patterns when step failures risk cascading to downstream steps.
```

---

## Example Use Cases

**Enterprise:** A content-publishing agent follows a 7-step WORKFLOW.md that includes a human approval gate at step 5 (editorial review) with a 4-hour timeout, after which the workflow auto-escalates to the managing editor rather than publishing unapproved content.

**Multi-Agent Fleet:** A CI/CD pipeline fleet defines interconnected workflows where the build agent's completion triggers the test agent's workflow, which upon success triggers the deployment agent's workflow -- each with explicit failure recovery and rollback steps documented per-agent.

**Regulated Industry:** A loan-origination agent follows a WORKFLOW.md with mandatory decision points at credit check, income verification, and regulatory disclosure steps, where each branch documents the exact conditions for approval, denial, or escalation to a licensed loan officer.

## Related Specs

| Spec | Relationship |
|------|-------------|
| DEADLINES.md | Time constraints and schedules |
| GOALS.md | Objectives and success criteria |
| REPAIR.md | Recovery and self-healing procedures |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
