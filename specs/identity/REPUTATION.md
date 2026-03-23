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
This reputation data is:
- Stored at: [immutable log location]
- Signed by: [authority]
- Last audited: [date]
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
