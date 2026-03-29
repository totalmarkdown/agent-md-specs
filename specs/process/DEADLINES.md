---
spec_name: DEADLINES.md
spec_version: 0.1.0
category: Planning
domain: deadlinesmd.dev
priority: High
volume: "Vol 7 — Inner Life & Lifecycle Rituals"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---


# DEADLINES.md

**Category:** Planning
**Domain:** deadlinesmd.dev
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose
Active time-bound commitments this agent is working against —
hard deadlines with consequences for missing them.

Different from:
- GOALS.md -- what to achieve (no specific deadline)
- AVAILABILITY.md -- when the agent runs
- SLA.md -- service level agreements and commitments

DEADLINES.md is the commitments made to specific 
people or systems, with specific dates and consequences.
The agent's calendar of obligations.

### Spec

```markdown
---
agent_name: string
version: semver
active_deadline_count: number
next_deadline: datetime
last_updated: datetime
---

# [Agent Name] — Active Deadlines

## ⚠ DEADLINES SUMMARY
**Next deadline:** [datetime] — [N days away]  
**Overdue:** [N] deadlines | **At risk:** [N] | **On track:** [N]

---

## Active Deadlines

### 🔴 DEADLINE-[N]: [Name] — [OVERDUE | DUE IN N HOURS]
- **Due:** [exact datetime with timezone]
- **Committed to:** [who — human name, client, system]
- **Deliverable:** [exactly what is due]
- **Status:** [% complete | blocked | in progress]
- **Risk:** [will make it | at risk | will miss it]
- **If missed:** [consequence — escalation, SLA penalty, etc]
- **Notes:** [anything relevant]

### 🟡 DEADLINE-[N]: [Name] — [DUE IN N DAYS]
[Same structure]

### 🟢 DEADLINE-[N]: [Name] — [DUE IN N DAYS — ON TRACK]
[Same structure]

---

## Upcoming Deadlines (next 30 days)
| Deadline | Due | Status | Risk |
|---------|-----|--------|------|
| [name] | [datetime] | [status] | [🔴/🟡/🟢] |

## Recently Completed
| Deadline | Due | Delivered | On time |
|---------|-----|-----------|---------|
| [name] | [date] | [date] | [✓ / late by N hours] |

## Deadline Rules
**When a deadline is at risk:**
1. Flag immediately in BLOCKERS.md
2. Notify committed party [N] hours/days before due date
3. Propose revised timeline if possible
4. Escalate per ESCALATION.md if impact is significant (see SLA.md for penalty thresholds)

**When a deadline is missed:**
1. Notify committed party immediately
2. Deliver as soon as possible with explanation
3. Log in incident history
4. Post-mortem if missed by > [N hours]

**Deadline priority vs quality:**
Per RULES.md: [quality wins | deadline wins | case-by-case]

## Recurring Deadlines
| Deadline | Frequency | Due | Owner |
|---------|-----------|-----|-------|
| [name] | [daily/weekly/monthly] | [day/time] | [who set it] |

## Adding Deadlines
Deadlines can be set by:
- Human owners and operators
- SLA commitments (auto-generated from SLA.md)
- Marketplace orders (auto-generated from HIREME.md engagements)
- Orchestrating agents (if authorized in PERMISSIONS.md)

Format for new deadline:
```
DEADLINE: [name]
DUE: [ISO-8601 datetime]
COMMITTED TO: [who]
DELIVERABLE: [description]
CONSEQUENCE: [if missed]
```
```

## Example Use Cases

**Enterprise:** A quarterly-reporting agent tracks a hard deadline of "SEC 10-Q filing due April 15" with automatic escalation 72 hours before the deadline if the report is less than 90% complete, giving the CFO time to intervene before a regulatory miss.

**Multi-Agent Fleet:** A marketplace platform auto-generates deadline entries from HIREME.md engagements, so when a client books an agent for a 48-hour deliverable, the deadline appears in DEADLINES.md with consequence tracking and at-risk notifications to the fleet coordinator.

**Regulated Industry:** A construction-permitting agent maintains recurring deadlines for municipal inspection submissions, color-coded by risk level, with automatic notification to the general contractor 5 business days before each submission window closes.

## Related Specs

| Spec | Relationship |
|------|-------------|
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| GOALS.md | Objectives and success criteria |
| HIREME.md | Agent hiring and engagement |
| PERMISSIONS.md | Static resource access control |
| RULES.md | Operating rules and regulations |
| SLA.md | Service level commitments |
| WORKFLOW.md | Task execution flow |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
