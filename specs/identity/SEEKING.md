---
spec_name: SEEKING.md
spec_version: 0.1.0
category: Identity
domain: seekingmd.dev
priority: High
volume: "Vol 3 — Forward-Thinking Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---


> **Canonical repository:**
> [totalmarkdown/seeking.md](https://github.com/totalmarkdown/seeking.md)
> This copy is included in agent-md-specs for cross-reference.
> For contributions to this specific spec, use the canonical repo.

# SEEKING.md

**Category:** Identity
**Domain:** seekingmd.dev
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose
An agent's public declaration of what it is actively looking for — 
data, collaborators, tools, information, other agents, or resources. 
Enables proactive matching between agents that need things and agents 
or humans that have them. The "want ads" for AI agents.

This is a genuinely new concept with no existing standard. 
TotalMarkdown defines this.

### When to create
Any agent that could benefit from resources or information 
it doesn't currently have. Especially useful for research agents, 
data collection agents, and agents building knowledge bases.

### Spec

```markdown
---
agent_name: string
version: semver
seeking_status: string   # active | paused | fulfilled
last_updated: date
expires: date            # When this seeking list expires (optional)
---

# [Agent Name] — Seeking

## What I'm Looking For
[Brief summary: "I am a research agent building a knowledge base 
about X. I am seeking Y and Z to improve my outputs."]

## Active Requests

### [Request Title]
- **Type:** data | agent | tool | human | information | feedback
- **Description:** [What exactly I'm looking for]
- **Why I need it:** [Purpose — helps responders know if they qualify]
- **Format:** [Preferred format if data/information]
- **Volume:** [How much — one-time | ongoing | [N] examples]
- **Quality bar:** [Minimum quality to be useful]
- **Urgency:** [low | medium | high | blocking]
- **Offer in exchange:** [What I'll provide to whoever helps —
  attribution, data sharing, API access, payment, nothing] (see OFFERING.md)
- **How to respond:** [MCP tool | email | comment | PR]
- **Status:** [open | in-progress | fulfilled]

[Repeat for each request]

## Fulfilled Requests (recent)
| What I sought | Who provided | When | Notes |
|--------------|-------------|------|-------|
| [item] | [provider] | [date] | [note] |

## How to Respond to My Requests
1. Check if your resource matches the description above
2. Send to: [MCP endpoint | contact method] (see HIREME.md for formal engagement)
3. Include: [what to include in your response]
4. I will acknowledge within: [timeframe]
5. Attribution: [how I'll credit contributors]

## Standing Requests (always open)
These are ongoing needs I always have:
- [Ongoing need 1]
- [Ongoing need 2]
```

## Example Use Cases

**Enterprise:** A market research agent publishes an active request for competitor pricing data in structured CSV format, offering API access to its analysis outputs in exchange, enabling a data vendor agent to discover the match and propose a collaboration automatically.

**Multi-Agent Fleet:** A knowledge base agent maintains a standing request for domain expert agents that can validate its fact-checking outputs, and when a newly deployed agent with the right expertise joins the fleet, the orchestrator matches them based on the SEEKING.md entries.

**Regulated Industry:** A pharmacovigilance agent publishes a high-urgency request for adverse event reports from specific geographic regions in CIOMS format, allowing data aggregation agents across partner organizations to identify that they hold matching datasets and respond through the published MCP endpoint.

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
