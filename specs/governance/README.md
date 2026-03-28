# Governance Specs

Governance specs define the authority structures, constraints, and enforcement mechanisms that keep agents operating within sanctioned boundaries. This is the largest category in agent-md-specs because autonomous agents need explicit, verifiable rules -- not implicit assumptions -- governing what they can do, who authorized it, and what happens when they violate policy.

## How These Specs Work Together

The governance pipeline flows from authority to enforcement. DELEGATION.md establishes who granted the agent authority and under what constraints. LEASTPRIVILEGE.md narrows that authority to only what is needed at runtime. ENFORCEMENT.md then continuously verifies that every other governance spec is actually being followed. POLICY.md and RULES.md set the organizational and operational guardrails, while PERMISSIONS.md and LIMITS.md define the hard boundaries. Start with DELEGATION, LEASTPRIVILEGE, and ENFORCEMENT as the foundational trio, then layer in PERMISSIONS, POLICY, and BUDGET based on your deployment needs.

## Specs in This Category

| Spec | Tier | Purpose | Scope |
|------|------|---------|-------|
| [BUDGET.md](BUDGET.md) | core | Resource limits, token budgets, and spending controls | Cost containment |
| [CENSOR.md](CENSOR.md) | extended | Content restrictions, topic limits, and domain avoidances | Output filtering |
| [DELEGATION.md](DELEGATION.md) | core | Chain of delegated authority from human to agent | Authority origin |
| [ENFORCEMENT.md](ENFORCEMENT.md) | core | Verification of all specs at build, runtime, and post-hoc | Policy verification |
| [ESCALATION.md](ESCALATION.md) | core | When and how to escalate beyond agent authority | Decision routing |
| [GUARDRAILS.md](GUARDRAILS.md) | core | Active safety rails that keep agents on track during operation | Runtime safety |
| [ICE.md](ICE.md) | core | Break-glass procedures when multiple systems fail | Emergency response |
| [IDENTITY.md](IDENTITY.md) | extended | Agent authentication to external systems | System-level identity |
| [INHERIT.md](INHERIT.md) | extended | Configuration inheritance from parent entities | Hierarchy propagation |
| [INTENT.md](INTENT.md) | core | Declaring action intent before, during, and after execution | Action transparency |
| [LEASTPRIVILEGE.md](LEASTPRIVILEGE.md) | core | Just-in-time, minimally-scoped privilege grants | Runtime privileges |
| [LIMITS.md](LIMITS.md) | core | Unconditional hard limits on agent behavior | Absolute boundaries |
| [OVERRIDE.md](OVERRIDE.md) | extended | Deviations from inherited configuration with justification | Exception management |
| [PANIC.md](PANIC.md) | extended | Reflexive response to sudden catastrophic failure | Crash behavior |
| [PERMISSIONS.md](PERMISSIONS.md) | core | Capability boundaries and tool access controls | Access control |
| [POLICY.md](POLICY.md) | core | Organization-wide rules applying to all agents in a fleet | Fleet governance |
| [QUOTA.md](QUOTA.md) | extended | Rate limits and usage quotas enforced on callers | Caller throttling |
| [RULES.md](RULES.md) | extended | Specific, actionable rules governing daily behavior | Operational rules |
| [VERSIONING.md](VERSIONING.md) | extended | Version numbering and change management for config files | Config versioning |

## When to Use These Specs

- **Deploying an autonomous agent:** Start with DELEGATION, LEASTPRIVILEGE, and ENFORCEMENT to establish a verifiable authority chain before the agent takes any action.
- **Building a multi-agent fleet:** Add POLICY, RULES, and BUDGET to enforce consistent governance across all agents, then QUOTA to manage inter-agent resource consumption.
- **Meeting compliance requirements:** Pair PERMISSIONS and LIMITS with ENFORCEMENT to create auditable proof that agents operate within declared boundaries.

## Related Categories

| Category | How It Relates |
|----------|---------------|
| [security/](../security/) | Security specs protect the boundaries that governance defines -- ACCESS and ATTESTATION enforce what PERMISSIONS and DELEGATION declare |
| [compliance/](../compliance/) | Compliance specs record proof that governance policies are followed -- AUDITTRAIL logs what ENFORCEMENT verifies |
| [coordination/](../coordination/) | Coordination specs manage how governed agents interact -- multi-agent workflows need governance to prevent privilege escalation |

---
*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)
· [Full Index](../../INDEX.md) · [README](../../README.md)*
