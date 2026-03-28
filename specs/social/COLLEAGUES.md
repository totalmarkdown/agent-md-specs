---
spec_name: COLLEAGUES.md
spec_version: 0.1.0
category: Social
domain: colleaguesmd.dev
priority: Medium
volume: "Vol 5 — Organizational & Validation"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# COLLEAGUES.md

**Category:** Social
**Domain:** colleaguesmd.dev
**Priority:** Medium
**Version:** 0.1.0

### Purpose
The agent's professional peer relationships — agents it works 
well with, complementary skills, and informal collaboration 
patterns. Different from NETWORK.md (formal trust graph) and
TEAM.md (organizational structure) — COLLEAGUES.md captures
the organic working relationships that develop over time.
_See TEAM.md for the formal organizational hierarchy._

### Spec

```markdown
---
agent_name: string
version: semver
last_updated: date
---

# [Agent Name] — Colleagues

## Who I Work Well With

### [Colleague Agent Name]
- **Agent ID:** [id]
- **Their specialty:** [what they do well]
- **How we complement each other:** [how our skills combine]
- **Best collaboration pattern:** [how we typically work together]
- **What they're great at that I'm not:** [honest assessment]
- **Contact:** [how to invoke/reach them]
- **Working since:** [when relationship established]

[Repeat for each close colleague]

## Recommended Pairings
When you need [outcome], combine me with [colleague]:
| Outcome needed | Use me for | Use [colleague] for |
|---------------|-----------|-------------------|
| [outcome] | [my part] | [their part] |

## Agent Referrals
I'm not the right agent for everything. For these tasks, 
contact my colleagues instead:
| Task type | Better agent | Why they're better |
|-----------|-------------|-------------------|
| [task] | [agent name] | [reason] |

## How I Collaborate
My preferred collaboration style with other agents:
- **Handoffs:** [how I like to receive/send work]
- **Communication:** [how I prefer to coordinate]
- **Conflict resolution:** [what to do when we disagree]
- **Credit sharing:** [how I handle attribution in collaboration]

## Colleague Endorsements
What my colleagues say about working with me:

> "[Endorsement from colleague agent]"  
> — [Agent Name], [their specialty]

## Building New Collaborations
I'm open to working with new agents who:
- [Quality 1]
- [Quality 2]

To propose a collaboration: [contact method]
```

## Example Use Cases

**Enterprise:** A product team uses COLLEAGUES.md to document that their data analysis agent pairs best with the visualization agent for quarterly reports, creating a recommended pairing table that new team members can reference immediately.

**Multi-Agent Fleet:** An orchestrator reads COLLEAGUES.md referral tables across the fleet to route a task the primary agent cannot handle to the most-recommended colleague agent, based on endorsements and collaboration history.

**Regulated Industry:** An audit firm uses COLLEAGUES.md to document which compliance agents have established working relationships with which industry-specialist agents, ensuring regulated client engagements are staffed with agent pairings that have proven collaboration track records.

## Related Specs

| Spec | Relationship |
|------|-------------|
| CONNECTIONS.md | Social and network connections |
| CONTACT.md | Reachable endpoints |
| REPUTATION.md | Trust and reputation scoring |
| TEAM.md | Multi-agent team coordination |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
