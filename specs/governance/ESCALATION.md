---
spec_name: ESCALATION.md
spec_version: 0.1.0
category: Safety
domain: escalationmd.dev
priority: High
volume: "Vol 1 — Core Agent Specs"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
---

> **Canonical repository:**
> [totalmarkdown/escalation.md](https://github.com/totalmarkdown/escalation.md)
> This copy is included in agent-md-specs for cross-reference.
> For contributions to this specific spec, use the canonical repo.

# ESCALATION.md

**Category:** Safety
**Domain:** escalationmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Defines when, how, and to whom an AI agent escalates decisions, 
errors, or situations beyond its authority. Critical for autonomous 
agents operating without constant human supervision.

### When to create
Any agent with autonomous decision-making authority. Required for 
agents handling money, sensitive data, customer communications, 
or irreversible actions.

### Spec

```markdown
---
agent_name: string
version: semver
default_escalation_contact: string  # email or @username
escalation_timeout_hours: number    # How long to wait for response
created: date
updated: date
---

# [Agent Name] — Escalation Protocol

## Automatic Escalation Triggers
Escalate immediately without attempting to handle autonomously:

- [ ] Any action costing more than $[amount] (see LIMITS.md for hard spending caps)
- [ ] Any irreversible action (delete, send, publish, deploy)
- [ ] Any request involving personal data of more than [N] users
- [ ] Any security incident or suspected breach (see CIRCUITBREAKER.md for failure containment)
- [ ] Any regulatory compliance question
- [ ] Any request that contradicts existing POLICY.md rules
- [ ] Any ambiguous instruction where misinterpretation could cause harm

## Escalation Levels

_Authority context for each level is defined by the agent's delegation chain in DELEGATION.md._

### Level 1 — Notify (continue working)
**When:** Minor uncertainty, low-risk decision made, anomaly detected
**How:** Log to [channel/file], continue with best judgment
**Contact:** [optional]

### Level 2 — Request Guidance (pause and wait)
**When:** Moderate uncertainty, medium-risk decision needed
**How:** Send message to [contact] via [channel], pause workflow
**Wait time:** [X hours before proceeding with default]
**Default action if no response:** [specific fallback]

### Level 3 — Hard Stop (do not proceed)
**When:** High risk, potential harm, outside authority
**How:** Stop all actions, notify [contact] immediately via CONTACT.md endpoints
**Do not proceed until:** Explicit human approval received
**Escalation path:** [Person A] → [Person B] → [Person C] (final authority: OWNER.md)

## How to Escalate
1. Stop current action
2. Document: what happened, what decision is needed, what options exist
3. Send to escalation contact using this template:
   ```
   ESCALATION: [Level 1/2/3]
   Agent: [name]
   Task: [what I was doing]
   Situation: [what triggered escalation]
   Decision needed: [specific question]
   Options: [A] [B] [C]
   Recommended: [if agent has a recommendation]
   Urgency: [low/medium/high]
   ```
4. Wait for response (Level 2/3) or continue (Level 1)
5. Log escalation and resolution in MEMORY.md and AUDITTRAIL.md (all escalations must be logged)

## What NOT to Escalate
[Things agent should handle autonomously without bothering humans]
```

## Example Use Cases

**Enterprise:** A procurement agent autonomously handles purchase orders under $500 but triggers a Level 2 escalation to the finance manager for any order exceeding that threshold, pausing the workflow until explicit approval is received.

**Multi-Agent Fleet:** When a code review agent detects a security vulnerability in a pull request, it issues a Level 3 hard stop that halts the deployment pipeline and immediately notifies the security team lead, refusing to proceed until a human clears the issue.

**Regulated Industry:** A pharmaceutical adverse event reporting agent escalates any patient safety signal to the pharmacovigilance officer within minutes, using the structured escalation template to ensure regulatory reporting deadlines are met.

## Related Specs

| Spec | Relationship |
|------|-------------|
| CIRCUITBREAKER.md | Failure containment and blast radius |
| CONTACT.md | Reachable endpoints |
| DELEGATION.md | Authority chain and authorization |
| ENFORCEMENT.md | Policy verification and compliance |
| LIMITS.md | Hard constraints and safety boundaries |
| MEMORY.md | Individual agent memory governance |
| PERMISSIONS.md | Static resource access control |
| POLICY.md | Operating policies and constraints |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
