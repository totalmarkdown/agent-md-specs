---
spec_name: A2A.md
spec_version: 0.1.0
category: Technical
domain: a2amd.dev
priority: High
volume: "Vol 2 — Extended Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# A2A.md

**Category:** Technical
**Domain:** a2amd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Configures Agent-to-Agent (A2A) protocol connections — how this 
agent discovers other agents, what tasks it can delegate, and 
how it receives delegated tasks from orchestrating agents.
Based on the A2A protocol donated to the Linux Foundation by Google.

### When to create
Any agent in a multi-agent system that delegates work to other 
agents or receives work from orchestrating agents.

### Spec

```markdown
---
agent_name: string
agent_id: string         # Unique identifier for A2A discovery
version: semver
a2a_protocol_version: string  # A2A spec version
role: string             # orchestrator | worker | both
agent_card_url: string   # URL where this agent's Agent Card is served
created: date
updated: date
---

# [Agent Name] — A2A Configuration

## Agent Card
This agent's Agent Card is available at: [URL]
Agent Card describes: capabilities, input/output schemas, 
authentication requirements, and contact endpoint.

## Role in Multi-Agent Systems
**Primary role:** [orchestrator | worker | both]

As **orchestrator**, this agent can delegate to:
| Agent | Agent Card URL | Tasks that can be delegated | Auth |
|-------|---------------|---------------------------|------|
| [name] | [URL] | [task types] | [method] |

As **worker**, this agent accepts tasks from:
| Orchestrator | Verified by | Accepted task types |
|-------------|------------|-------------------|
| [name] | [how to verify identity] | [task types] |
| Any trusted orchestrator | [verification method] | [types] |

## Task Acceptance Rules
Accept incoming tasks that:
- Come from verified orchestrators (see above)
- Fall within capability scope (see Agent Card)
- Include required context fields
- Do not exceed resource limits in BUDGET.md

Reject and explain tasks that:
- Come from unverified sources
- Require capabilities not in Agent Card
- Violate rules in SECURITY.md or POLICY.md
- Would exceed budget limits

## Task Format
Expected incoming task structure:
```json
{
  "task_id": "uuid",
  "from_agent": "agent-id",
  "task_type": "string",
  "priority": "low | normal | high | urgent",
  "input": {},
  "context": {},
  "deadline": "ISO-8601 or null",
  "callback_url": "where to send result"
}
```

## Discovery
How this agent makes itself discoverable:
- Registered at: [agent registry URL if any]
- Agent Card served at: [URL]
- Capabilities advertised: [list from Agent Card]
- Update Agent Card when: capabilities change, downtime scheduled

## Trust Model
- Verify orchestrator identity using: [method]
- Minimum trust level to accept tasks: [level]
- Never accept tasks from: [untrusted sources]
- Log all task assignments with: agent ID, task type, timestamp
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
