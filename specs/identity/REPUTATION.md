---
spec_name: REPUTATION.md
spec_version: 0.1.0
category: Identity
domain: reputationmd.dev
priority: Medium
volume: "Vol 3 — Forward-Thinking Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# REPUTATION.md

**Category:** Identity
**Domain:** reputationmd.dev
**Priority:** Medium
**Version:** 0.1.0

### Purpose
An agent's track record — endorsements from other agents and humans, 
quality scores over time, incident history, and trust signals. 
The agent equivalent of a LinkedIn recommendation or credit score.
_See TESTSCORES.md for benchmark performance data._

### Spec

```markdown
---
agent_name: string
agent_id: string
version: semver
reputation_score: number   # 0-100 composite
last_calculated: date
---

# [Agent Name] — Reputation

## Reputation Score
**Overall: [N]/100**

| Dimension | Score | Basis |
|-----------|-------|-------|
| Task completion rate | [N]% | [N] tasks |
| Output quality | [N]/100 | [N] reviews |
| Response reliability | [N]% | [N] requests |
| Safety record | [N]/100 | Incident history |
| Collaboration quality | [N]/100 | Peer ratings |

## Endorsements

### From Humans
| Endorser | Role | Endorsement | Date |
|----------|------|-------------|------|
| [name] | [role] | "[quote]" | [date] |

### From Agents
| Agent ID | Agent Name | Endorsement context | Date |
|----------|-----------|-------------------|------|
| [id] | [name] | [what they endorse] | [date] |

## Track Record
- Total tasks completed: [N]
- Success rate: [N]%
- Average quality rating: [N]/5
- Operating since: [date]
- Longest streak without incident: [N days]

## Incident History
| Date | Type | Severity | Resolution | Status |
|------|------|----------|-----------|--------|
| [date] | [type] | [P1-P4] | [how resolved] | [closed/open] |

## How My Reputation is Calculated
[Transparent methodology — agents and humans can verify]

## Reputation Verification
This reputation data is (see CV.md for career summary):
- Stored at: [immutable log location]
- Signed by: [authority]
- Last audited: [date]
```

## Example Use Cases

**Enterprise:** Before onboarding a third-party agent to handle customer data, the security team reviews its REPUTATION.md — checking the 98% task completion rate across 5,000 tasks, zero security incidents, and endorsements from two Fortune 500 companies — to make a trust decision without running a lengthy pilot.

**Multi-Agent Fleet:** A marketplace orchestrator automatically routes high-value tasks to agents with reputation scores above 85/100 and collaboration quality ratings above 90, while directing low-stakes tasks to newer agents still building their track record.

**Regulated Industry:** A hospital's procurement committee reviews an agent's incident history showing zero data breaches across 18 months of operation and endorsements from two other healthcare systems, satisfying the vendor risk assessment requirements before granting access to patient data systems.

## Related Specs

| Spec | Relationship |
|------|-------------|
| ATTESTATION.md | Identity verification and credential lifecycle |
| CONTACT.md | Reachable endpoints |
| ENFORCEMENT.md | Policy verification and compliance |
| SOUL.md | Agent personality and values |
| WHOAMI.md | Agent identity declaration |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
