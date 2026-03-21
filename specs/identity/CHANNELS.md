---
spec_name: CHANNELS.md
spec_version: 0.1.0
category: Communication
domain: channelsmd.dev
priority: Medium
volume: "Vol 3 — Forward-Thinking Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# CHANNELS.md

**Category:** Communication
**Domain:** channelsmd.dev
**Priority:** Medium
**Version:** 0.1.0

**Priority:** MEDIUM  
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
**Auth:** Workspace token

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
| Channel | Requests/min | Requests/day | Burst |
|---------|-------------|-------------|-------|
| MCP | [N] | [N] | [N] |
| API | [N] | [N] | [N] |
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
