---
spec_name: CHANNELS.md
spec_version: 0.1.0
category: Communication
domain: channelsmd.dev
priority: Medium
volume: "Vol 3 — Forward-Thinking Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---
> **Static Configuration** — committed to your repository


# CHANNELS.md

**Category:** Communication
**Domain:** channelsmd.dev
**Priority:** Medium
**Version:** 0.1.0

### Purpose
Defines all the ways to reach and interact with an agent — 
every channel, endpoint, and contact method available.
The agent's contact card.

### Spec

```markdown
---
agent_name: string
version: semver
primary_channel: string  # How most people should reach this agent
---

# [Agent Name] — Channels

## How to Reach Me

### Primary Channel: [Channel name]
**Best for:** [Use cases this channel is best for]  
**Endpoint:** [connection details]  
**Auth:** [required authentication]  
**Response time:** [typical]  
**Availability:** [24/7 | business hours | scheduled]

### MCP Server
**Connection string:** [from MCP.md]  
**Tools available:** [count] tools — see MCP.md  
**Best for:** Agent-to-agent integration
**Auth:** Workspace token (see IDENTITY.md)

### A2A Protocol
**Agent Card URL:** [URL]  
**Best for:** Multi-agent coordination  
**Spec version:** [A2A version]

### CLI
**Install:** `[install command]`  
**Best for:** Developer workflows, automation, scripting  
**See:** CLI.md for full reference

### REST API (if available)
**Base URL:** [URL]  
**Auth:** [method]  
**Docs:** [URL]  
**Best for:** Custom integrations

### Chat Interface (if available)
**URL:** [URL]  
**Best for:** Ad-hoc questions, exploration  
**Auth:** [method]

## Response Time SLAs by Channel
| Channel | Typical | Maximum | Outside hours |
|---------|---------|---------|---------------|
| MCP | [ms] | [s] | [behavior] |
| CLI | [ms] | [s] | N/A |
| API | [ms] | [s] | [behavior] |

## Rate Limits by Channel
_See QUOTA.md for full rate limiting policies._
| Channel | Requests/min | Requests/day | Burst |
|---------|-------------|-------------|-------|
| MCP | [N] | [N] | [N] |
| API | [N] | [N] | [N] |
```

## Example Use Cases

**Enterprise:** A DevOps agent publishes its available channels — MCP for agent-to-agent orchestration, CLI for developer scripting, and REST API for custom integrations — so each team can connect via whichever method best fits their existing toolchain.

**Multi-Agent Fleet:** An orchestrator reads each agent's CHANNELS.md to determine the fastest available endpoint, routing latency-sensitive tasks through the MCP server (sub-second response) and bulk batch jobs through the REST API with higher rate limits.

**Regulated Industry:** A compliance reporting agent documents that its chat interface is available only during business hours with human-reviewed outputs, while its MCP endpoint operates 24/7 for automated audit data collection with full logging on every channel.

## Related Specs

| Spec | Relationship |
|------|-------------|
| ATTESTATION.md | Identity verification and credential lifecycle |
| CONTACT.md | Reachable endpoints |
| ENFORCEMENT.md | Policy verification and compliance |
| MCP.md | Model Context Protocol connections |
| SOUL.md | Agent personality and values |
| WHOAMI.md | Agent identity declaration |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
