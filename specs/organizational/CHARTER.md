---
spec_name: CHARTER.md
spec_version: 0.1.0
category: Organizational
domain: chartermd.dev
priority: Medium
volume: "Vol 3 — Forward-Thinking Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# CHARTER.md

**Category:** Organizational
**Domain:** chartermd.dev
**Priority:** Medium
**Version:** 0.1.0

### Purpose
The formal mandate authorizing this agent's existence and operation — 
who approved it, for what purpose, under what constraints, 
and what would cause it to be decommissioned. The agent's 
founding document.

### Spec

```markdown
---
agent_name: string
version: semver
charter_approved_by: string
charter_approved_date: date
charter_expires: date        # When this must be reviewed/renewed
charter_status: string       # active | under-review | suspended | revoked
---

# [Agent Name] — Charter

## Mission Statement
[Why this agent exists — formal, specific, bounded]

## Authorized By
**Approving authority:** [Human name/role]  
**Date approved:** [Date]  
**Approval reference:** [Ticket/document number]  
**Valid until:** [Expiry date — must be renewed]

## Scope of Authority
This agent is authorized to:
- [Specific authorized activity 1]
- [Specific authorized activity 2]

This agent is explicitly NOT authorized to:
- [Out of scope activity 1]
- [Out of scope activity 2]

## Resources Allocated
| Resource | Allocation | Notes |
|----------|-----------|-------|
| Budget | $[X]/month | Per BUDGET.md |
| Compute | [specification] | |
| Data access | [what data] | |
| Staff time | [X hours/week] for oversight | |

## Success Criteria
This agent's charter will be considered successful if:
- [Measurable success criterion 1]
- [Measurable success criterion 2]

## Review Cadence
**Charter review:** [quarterly | annually]  
**Reviewed by:** [role]  
**Next review:** [date]

## Decommission Criteria
This agent will be decommissioned if:
- [Criterion 1 — e.g. success criteria not met in 6 months]
- [Criterion 2 — e.g. better alternative exists]
- [Criterion 3 — e.g. charter not renewed by expiry date]

## Amendment History
| Version | Change | Approved by | Date |
|---------|--------|------------|------|
| 1.0 | Initial charter | [approver] | [date] |
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
