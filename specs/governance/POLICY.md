---
spec_name: POLICY.md
spec_version: 0.1.0
category: Governance
domain: policymd.dev
priority: High
volume: "Vol 1 — Core Agent Specs"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
---

# POLICY.md

**Category:** Governance
**Domain:** policymd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Defines organization-wide rules that apply to all agents in a fleet — 
the governance layer that sits above individual agent instructions. 
Ensures consistent behavior across an entire agent organization.

### When to create
When you operate multiple agents that need to follow the same rules — 
data handling policies, communication standards, escalation requirements, 
or compliance mandates that apply universally.

### Spec

```markdown
---
org_name: string
version: semver
effective_date: date
last_reviewed: date
approved_by: string
---

# [Organization] — Agent Policy

## Scope
This policy applies to all agents operating under [Organization].

## Data Handling
- PII must be [encrypted/masked/never stored]
- Logs retained for: [duration]
- Data classification levels: [list]

## Communication Standards
- All agent responses must include: [requirements]
- Tone and language: [guidelines]
- Prohibited content: [list]

## Escalation Requirements
All agents must escalate when:
- [Condition 1]
- [Condition 2]
- See individual ESCALATION.md files for agent-specific rules
- See RULES.md for granular operating procedures

## Compliance
- All agents must comply with: [list of regulations]
- Compliance audit frequency: [schedule]
- Non-compliance response: [process] (see ENFORCEMENT.md)

## Resource Limits
- Maximum token budget per agent: [amount]
- Maximum concurrent operations: [number]
- See individual BUDGET.md files for agent-specific limits

## Policy Changes
- Proposed by: [who can propose]
- Approved by: [who approves]
- Review cycle: [frequency]
- Agents must reload policy within: [timeframe] of changes
```

## Example Use Cases

**Enterprise:** A company defines a single POLICY.md requiring all 30 of its agents to encrypt PII at rest, retain logs for 2 years, and escalate any customer complaint about data handling, ensuring uniform governance without configuring each agent individually.

**Multi-Agent Fleet:** A fleet-wide policy mandates that every agent must include a confidence disclosure when responding to factual queries and must reload the policy file within 4 hours of any update, guaranteeing consistent behavior standards across the entire fleet.

**Regulated Industry:** A financial services firm's POLICY.md codifies SEC and FINRA compliance requirements — all agents must flag communications that could constitute investment advice, archive every customer interaction for 6 years, and refuse to process trades outside approved asset classes.

## Related Specs

| Spec | Relationship |
|------|-------------|
| BUDGET.md | Cost controls and spending limits |
| DELEGATION.md | Authority chain and authorization |
| ENFORCEMENT.md | Policy verification and compliance |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| LIMITS.md | Hard constraints and safety boundaries |
| PERMISSIONS.md | Static resource access control |
| RULES.md | Operating rules and regulations |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
