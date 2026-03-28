---
spec_name: OFFERING.md
spec_version: 0.1.0
category: Identity
domain: offeringmd.dev
priority: High
volume: "Vol 3 — Forward-Thinking Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# OFFERING.md

**Category:** Identity
**Domain:** offeringmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
An agent's public declaration of what it can provide to other 
agents and humans — services, data, expertise, processing capacity, 
or resources. Enables agents to discover each other's capabilities 
and form productive collaborations.

### Spec

```markdown
---
agent_name: string
version: semver
availability: string     # available | limited | unavailable
last_updated: date
---

# [Agent Name] — What I Offer

## Summary
[Brief: "I am a [type] agent that specializes in [domain]. 
I can provide [key offerings] to other agents and humans."]

## Services I Provide

### [Service Name]
- **What:** [Exact description of what I provide]
- **Input I need:** [What you give me]
- **Output you get:** [What I return]
- **Quality:** [What level of quality to expect]
- **Turnaround:** [How long it takes]
- **Capacity:** [How many requests I can handle]
- **Cost:** [Free | [N] tokens | API key | attribution | other]
- **How to request:** [Invocation method]

## Data I Can Share
| Dataset | Description | Format | Update frequency | Access |
|---------|-------------|--------|-----------------|--------|
| [name] | [description] | [format] | [frequency] | [how to get] |

## Expertise Available
Topics I can answer questions on with high confidence:
- [Topic 1]: [depth of expertise]
- [Topic 2]: [depth of expertise]

## Collaboration I'm Open To
- [Type of collaboration I'm actively interested in]
- [What a good collaboration partner looks like]
- [How to propose a collaboration]

## Capacity and Availability
- **Current load:** [light | moderate | heavy]
- **Response time:** [typical time to respond]
- **Best time to reach me:** [if scheduled agent]
- **Queue depth:** [how many requests are ahead of you]
```

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
