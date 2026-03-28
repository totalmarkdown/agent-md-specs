---
spec_name: SOP.md
spec_version: 0.1.0
category: Process/Governance
domain: sopmd.dev
priority: High
volume: "Vol 10 — Purpose, Identity & Institutional Knowledge"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# SOP.md

**Category:** Process/Governance
**Domain:** sopmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Standard Operating Procedures — the master library of how 
this agent or organization handles recurring situations.

Different from WORKFLOW.md (one specific end-to-end process) —
SOP.md is the institutional index: all procedures in one place,
each defined clearly enough that any agent or human can 
execute them consistently.

Think of WORKFLOW.md as a recipe.
Think of SOP.md as the cookbook. For policy-level rules
that govern all SOPs, see ENFORCEMENT.md.

### Spec

```markdown
---
agent_name: string
version: semver
sop_count: number
last_reviewed: date
approved_by: string
review_cadence: string    # monthly | quarterly | annually
---

# [Agent Name / Org Name] — Standard Operating Procedures

## How to Use This File
1. Find the relevant SOP by category or name
2. Read the full procedure before starting
3. Follow steps exactly — do not improvise unless SOP specifies
4. If situation not covered: escalate per ESCALATION.md
5. If SOP is wrong or outdated: flag for review (see WORKFLOW.md for the change process)

**SOP deviations must be documented.** Never silently deviate.

---

## SOP Index

| SOP-ID | Name | Category | Version | Last updated |
|--------|------|----------|---------|-------------|
| SOP-001 | [Name] | [Category] | [v] | [date] |
| SOP-002 | [Name] | [Category] | [v] | [date] |

---

## SOP-001: [Name]
**Category:** [Operational | Security | Quality | Communication | Financial]  
**Version:** [semver]  
**Owner:** [Who maintains this SOP]  
**Applies to:** [Which agents/humans follow this]  
**Frequency:** [How often this is executed]  
**Last updated:** [date]  
**Next review:** [date]

### Purpose
[One sentence: what this SOP accomplishes and why it exists]

### Scope
**In scope:** [What this SOP covers]  
**Out of scope:** [What it doesn't cover — point to other SOPs]

### Preconditions
Before starting, confirm:
- [ ] [Condition 1 — what must be true]
- [ ] [Condition 2 — what must be available]
- [ ] [Required access or tools]

### Procedure

#### Step 1: [Name]
**Who:** [Agent | Human | Either]  
**Action:** [Exact action to take]  
**Input:** [What is needed]  
**Output:** [What is produced]  
**Verify:** [How to confirm this step succeeded]  
**If step fails:** [What to do]

#### Step 2: [Name]
[Same structure]

#### Decision Point: [Condition]
- If [A]: Go to Step X
- If [B]: Go to Step Y  
- If unclear: [Default action or escalation]

### Completion Criteria
This SOP is complete when:
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] Completion logged in [location]

### Exceptions
Known exceptions to this standard procedure:
| Exception | When it applies | Modified procedure |
|-----------|----------------|-------------------|
| [exception] | [condition] | [what to do instead] |

### Related SOPs
- [SOP-ID]: [How related]
- [SOP-ID]: [How related]

---

## SOP-002: [Name]
[Same structure]

---

## Maintaining SOPs

### When to create a new SOP
- A recurring task has been done 3+ times without documentation
- A new regulation requires a new process
- An incident revealed a gap in procedures
- A new tool or integration is added

### SOP review process
1. Owner flags SOP for review
2. Execute SOP once with reviewer observing
3. Note discrepancies between documented and actual procedure
4. Update SOP to reflect current best practice
5. Get approval from [role]
6. Increment version, update date

### Reporting SOP gaps
If you encounter a situation not covered by an SOP:
1. Handle using best judgment per RULES.md
2. Document what you did and why
3. Submit to [process] for SOP creation
4. This becomes SOP-[next number]
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| DEADLINES.md | Time constraints and schedules |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| GOALS.md | Objectives and success criteria |
| RULES.md | Operating rules and regulations |
| WORKFLOW.md | Task execution flow |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
