---
spec_name: OVERRIDE.md
spec_version: 0.1.0
category: Governance
priority: High
volume: "Vol 13 — Hierarchy & Inheritance"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
status: draft
spec_type: static
---


# OVERRIDE.md

**Category:** Governance
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose
Documents every place where this entity deviates from
its inherited configuration — what was overridden, why,
who approved it, and whether it's still justified.

OVERRIDE.md exists for one reason: **accountability**.
It is the companion to INHERIT.md, which declares the inheritance chain.

Anyone with access to ORG-level config and this file
can instantly see every deviation from standard policy
across the entire fleet. Security audits become a
matter of reading OVERRIDE.md files.

The discipline of writing an override forces the question:
"Is this deviation actually justified?" Often the answer
is no, and the override gets removed before it's documented.

### Spec

````markdown
---
entity_name: string
entity_type: string      # agent | team | crew | swarm
override_count: number
last_reviewed: date
reviewed_by: string      # Human who reviewed all overrides
next_review: date
---

# [Entity Name] — Configuration Overrides

## Override Summary
**[N] active overrides** from parent configuration.

Overrides are reviewed quarterly. Unjustified overrides
are removed. Justified overrides are re-approved.

Last reviewed: [date] by [reviewer]
Next review: [date]

---

## Active Overrides

### OVERRIDE-001: [Short title]
**File overridden:** [BUDGET.md | RULES.md | VOICE.md | etc.]
**Inherited from:** [parent entity name]
**Override type:** [full replacement | partial | additive | restrictive]

**What changed:**
[Specific description of what is different from the inherited version.
Be precise — "increased daily budget from $50 to $200" not "changed budget".]

**Why:**
[Business or technical justification. Must be specific.
"We need higher limits" is not sufficient.
"This crew processes enterprise batch jobs that average $150/day
at current volume — the $50 limit causes daily interruptions
that require manual intervention 3x per week" is sufficient.]

**Approved by:** [Name and role]
**Approved date:** [date]
**Review date:** [when this override should be re-evaluated]
**Still justified?** [Yes — condition still applies | Under review | Should be removed]

**Org policy compliance:**
This override does not violate ORG-level absolute policies because:
[Explanation — or "N/A — this is not overriding an absolute policy"]

---

### OVERRIDE-002: [Short title]
[Same structure]

---

## Pending Overrides (awaiting approval)

| Override | Requested by | Requested | Status |
|---------|-------------|-----------|--------|
| [description] | [name] | [date] | [pending approval | under review] |

---

## Rejected Overrides (recent, for reference)

| Override | Requested | Rejected | Reason |
|---------|-----------|---------|--------|
| [description] | [date] | [date] | [why rejected] |

---

## What Cannot Be Overridden

These are inherited from ORG level and are absolute:
- POLICY.md — organizational rules (no exceptions)
- LIMITS.md — hard stops (no exceptions)
- COMPLIANCE.md — regulatory requirements (no exceptions)
- SECURITY.md core rules (security minimums cannot be relaxed)

Attempting to override these will:
1. Fail validation
2. Generate an alert to the security team
3. Be logged in the audit trail

---

## Override Review Process

To propose a new override:
1. Document it in this file using the format above
2. Include specific justification (not vague)
3. Identify which org policies it does and doesn't affect
4. Get approval from: [approval authority]
5. Set a review date (max [N months] from approval)

To remove an override:
1. Delete or comment out the section
2. Note the removal date and reason
3. Verify the entity still functions correctly with inherited config
4. No approval needed to remove overrides

---

## Audit Trail

All changes to this file are tracked in git history (see AUDITTRAIL.md).
For compliance purposes, this file should never be
force-pushed or have history rewritten.

Override history is automatically available via:
```bash
git log --follow OVERRIDE.md
git diff [commit]...[commit] OVERRIDE.md
```
````

## Example Use Cases

**Enterprise:** An enterprise batch processing crew overrides its inherited BUDGET.md to increase the daily spending limit from $50 to $200, documenting that the higher limit is justified by average daily job costs of $150 and that the previous limit caused three manual interventions per week.

**Multi-Agent Fleet:** A fleet security audit reviews all OVERRIDE.md files across 80 agents in minutes, identifying two agents with expired override justifications and one agent whose voice override was never re-approved, flagging all three for immediate review.

**Regulated Industry:** A pharmaceutical manufacturing agent documents an override to its inherited RULES.md that relaxes a data retention period from 10 years to 7 years for non-GMP data, with explicit approval from the quality assurance director and a re-evaluation date tied to the next FDA inspection cycle.

## Related Specs

| Spec | Relationship |
|------|-------------|
| BUDGET.md | Cost controls and spending limits |
| DELEGATION.md | Authority chain and authorization |
| ENFORCEMENT.md | Policy verification and compliance |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| LIMITS.md | Hard constraints and safety boundaries |
| PERMISSIONS.md | Static resource access control |
| POLICY.md | Operating policies and constraints |
| RULES.md | Operating rules and regulations |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
