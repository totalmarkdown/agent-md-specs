---
spec_name: TEAM.md
spec_version: 0.1.0
category: Coordination
domain: teammd.dev
priority: High
volume: "Vol 1 — Core Agent Specs"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
spec_type: static
---
> **Static Configuration** — committed to your repository


> **Canonical repository:**
> [totalmarkdown/team.md](https://github.com/totalmarkdown/team.md)
> This copy is included in agent-md-specs for cross-reference.
> For contributions to this specific spec, use the canonical repo.

# TEAM.md

**Category:** Coordination
**Domain:** teammd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Defines a coordinated group of AI agents working together on a shared goal. 
Describes each agent's role, how they communicate, and how they hand off 
work between each other.

### When to create
When 2 or more agents collaborate on a workflow where the output of one 
agent becomes the input of another, or where agents work in parallel on 
related tasks.

### Spec

```markdown
---
team_name: string          # Human-readable team name
version: semver            # e.g. 1.0.0
purpose: string            # One sentence — see GOALS.md for detailed objectives
orchestration: string      # sequential | parallel | conditional | lead-delegates
shared_memory: boolean     # Governed by SHAREDCONTEXT.md and MEMORYSAFETY.md
delegation_ref: string     # Path to team-level DELEGATION.md
budget_ref: string         # Path to team-level BUDGET.md
escalation_ref: string     # Path to team-level ESCALATION.md
limits_ref: string         # Path to team-level LIMITS.md
circuit_breaker_ref: string  # Path to CIRCUITBREAKER.md for failure containment
created: date
updated: date
---

# [Team Name]

## Purpose
[2-3 sentences describing what this team accomplishes together]

## Agents

### [Agent Name] — [Role]
- **Bundle:** path/to/agent/  _(must contain WHOAMI.md and SOUL.md at minimum)_
- **Identity:** Verified via ATTESTATION.md
- **Role:** lead | support | specialist | reporter | escalation
- **Delegation:** Inherits from team DELEGATION.md (see INHERIT.md)
- **Triggers:** ["list", "of", "trigger", "phrases"]
- **Inputs:** What this agent receives (see INPUT.md)
- **Outputs:** What this agent produces (see OUTPUT.md)
- **Hands off to:** [Next agent name or "human"] — logged in AUDITTRAIL.md

[Repeat for each agent]

## Handoff Protocol
[How agents pass context between each other]
[What format handoff messages take — recorded in AUDITTRAIL.md]
[What triggers a handoff — may trigger ESCALATION.md if human needed]
[Intent must be declared via INTENT.md before handoff execution]
_See HANDSHAKE.md for inter-agent handoff protocol details._

## Shared Context
Governed by SHAREDCONTEXT.md. All agents in this team read from and
write to a shared context pool with access controls defined in the
team's SHAREDCONTEXT.md file. Memory integrity is enforced via
MEMORYSAFETY.md — including input sanitization, canary entries, and
quarantine procedures for suspicious entries.

- **Shared context path:** [path to team SHAREDCONTEXT.md]
- **Memory safety path:** [path to team MEMORYSAFETY.md]
- **Individual memory:** Each agent maintains its own MEMORY.md
  which can sync to/from shared context per MEMORY.md scope rules.
_See BUDGET.md for team-level cost controls and spending limits._

## Failure Handling
Governed by CIRCUITBREAKER.md at the team level.

- **Agent failure:** [Which agent takes over — see team roster above]
- **Circuit breaker trigger:** [N consecutive failures or N% error rate]
- **Blast radius:** Agent-level halt; team continues with degraded capability
- **Fallback:** [Cached results | graceful degradation | escalate to human]
- **Escalation:** Per ESCALATION.md — L1 auto-retry, L2 team lead, L3 human
- **Recovery:** CIRCUITBREAKER.md half-open testing before full restoration

## Success Criteria
[How the team knows it has completed its goal]
_Measurable targets: see KPI.md. Service commitments: see SLA.md._
```

### Common Team Patterns
- Customer support team (triage → resolve → escalate → follow-up)
- Content pipeline (research → draft → edit → publish → analyze)
- Security audit team (scan → analyze → report → remediate)
- Sales team (qualify → demo → proposal → close → onboard)

---

## Example Use Cases

**Enterprise:** An enterprise customer support team of 4 agents (triage, technical troubleshooting, billing resolution, satisfaction survey) operates with lead-delegates orchestration, shared memory for customer context persistence, and circuit-breaker rules that escalate to human agents after 3 consecutive resolution failures.

**Multi-Agent Fleet:** A SaaS company's content pipeline team (research, draft, edit, publish, analytics) uses sequential orchestration with defined handoff protocols, where each agent passes structured context to the next and the analytics agent feeds performance data back to improve future research priorities.

**Regulated Industry:** A financial advisory team of agents (client intake, risk profiling, portfolio recommendation, compliance review) operates under strict delegation rules where the compliance-review agent has veto authority and every recommendation is logged to the audit trail before client delivery.

## Related Specs

| Spec | Relationship |
|------|-------------|
| BUDGET.md | Cost controls and spending limits |
| CREW.md | Working group structure |
| DELEGATION.md | Authority chain and authorization |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| MEMORY.md | Individual agent memory governance |
| ORG.md | Organization-wide fleet configuration |
| SHAREDCONTEXT.md | Multi-agent shared memory pool |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
