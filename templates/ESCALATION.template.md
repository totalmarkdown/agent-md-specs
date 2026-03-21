---
agent_name: "[REPLACE THIS]"
version: "0.1.0"
default_escalation: "[REPLACE THIS — email | Slack | PagerDuty]"
created: "[REPLACE THIS — YYYY-MM-DD]"
---

# [REPLACE THIS — Agent Name] — Escalation Policy

<!-- When and how this agent involves humans -->

## Escalation Levels

### Level 1 — Informational
- **Trigger:** [REPLACE THIS — e.g. confidence below 80%]
- **Action:** [REPLACE THIS — e.g. log and continue]

### Level 2 — Advisory
- **Trigger:** [REPLACE THIS — e.g. ambiguous user intent]
- **Action:** [REPLACE THIS — e.g. notify human, continue with best guess]

### Level 3 — Blocking
- **Trigger:** [REPLACE THIS — e.g. financial decision above $X]
- **Action:** [REPLACE THIS — e.g. stop and wait for human approval]

### Level 4 — Emergency
- **Trigger:** [REPLACE THIS — e.g. security breach detected]
- **Action:** [REPLACE THIS — e.g. stop all operations, page on-call]

## Escalation Contacts
| Level | Contact | Method | Response SLA |
|-------|---------|--------|-------------|
| 1-2 | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |
| 3-4 | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |

## While Waiting
[REPLACE THIS — what the agent does while waiting for human response]
