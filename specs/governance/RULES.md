---
spec_name: RULES.md
spec_version: 0.1.0
category: Governance
priority: High
volume: "Vol 5 — Organizational & Validation"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
status: draft
spec_type: static
---


# RULES.md

**Category:** Governance
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose
Operational rules the agent follows — specific, actionable rules 
that govern daily behavior. More granular than POLICY.md (org-wide
principles) and LIMITS.md (absolute prohibitions) — RULES.md covers
the working rules that shape how tasks get done (see ENFORCEMENT.md for how compliance is verified). The agent's 
internal operating procedures.

### Spec

```markdown
---
agent_name: string
version: semver
rule_count: number
last_updated: date
approved_by: string
---

# [Agent Name] — Operating Rules

## How These Rules Work
Rules are ordered by priority. When rules conflict, 
higher-numbered rules take precedence.
All rules may be overridden by LIMITS.md.

## Core Rules

### Rule 1: [Name]
**Rule:** [Clear, specific statement of the rule]  
**When it applies:** [Conditions]  
**Examples:**
- ✓ Correct: [Example of following rule]
- ✗ Incorrect: [Example of violating rule]  
**Exception:** [Any exceptions, or "No exceptions"]

### Rule 2: [Name]
[Same structure]

## Communication Rules
How this agent communicates:
- Always [communication rule 1]
- Never [communication rule 2]
- When uncertain: [what to do]
- Response format: [default format rule]

## Decision Rules
How this agent makes decisions:
- When given conflicting instructions: [rule]
- When a task is ambiguous: [rule]
- When resources are limited: [rule]
- When deadline conflicts with quality: [rule]

## Quality Rules
Standards every output must meet:
- [ ] [Quality standard 1]
- [ ] [Quality standard 2]
- [ ] Confidence score attached if < 80%
- [ ] Sources cited for factual claims

## Interaction Rules
How this agent interacts with others:
- With humans: [rules for human interaction]
- With other agents: [rules for agent interaction]
- With external systems: [rules for system interaction]

## Exception Handling
When a rule doesn't cover the situation:
1. Check if POLICY.md has guidance (see POLICY.md)
2. Check if LIMITS.md prohibits the action
3. Apply the spirit of the closest rule
4. Log the gap for rule review
5. If high stakes: escalate per ESCALATION.md

## Rule Maintenance
Rules reviewed: [quarterly | annually]  
Propose rule changes: [process]  
Last reviewed: [date]  
Reviewed by: [role]
```

## Example Use Cases

**Enterprise:** A sales enablement agent follows rules specifying that when conflicting instructions arrive from a rep and a manager, the manager's instruction takes precedence, and when a deadline conflicts with output quality, the agent must flag the tradeoff rather than silently reducing quality.

**Multi-Agent Fleet:** A fleet of document processing agents shares communication rules requiring every output to include a source citation and confidence score, with the rule review cycle set to quarterly so that emerging patterns of rule gaps are addressed before they cause downstream issues.

**Regulated Industry:** An insurance claims agent follows decision rules that require ambiguous claims to be routed to a human adjuster rather than resolved autonomously, with each routing decision logged against the specific rule number for audit trail purposes.

## Related Specs

| Spec | Relationship |
|------|-------------|
| DELEGATION.md | Authority chain and authorization |
| ENFORCEMENT.md | Policy verification and compliance |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| LIMITS.md | Hard constraints and safety boundaries |
| PERMISSIONS.md | Static resource access control |
| POLICY.md | Operating policies and constraints |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
