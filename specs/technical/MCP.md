---
spec_name: MCP.md
spec_version: 0.1.0
category: Technical
domain: mcpmd.dev
priority: High
volume: "Vol 2 — Extended Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# MCP.md

**Category:** Technical
**Domain:** mcpmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Documents all MCP (Model Context Protocol) server connections for 
an agent — what servers it connects to, what tools are available 
from each, authentication methods, and usage guidelines.
The definitive reference for an agent's external tool access.

### When to create
Any agent that uses MCP servers to access external tools, data 
sources, APIs, or services. Required for agents with more than 
2 MCP connections.

### Spec

```markdown
---
agent_name: string
version: semver
mcp_client_version: string   # MCP protocol version
total_servers: number
total_tools: number
created: date
updated: date
---

# [Agent Name] — MCP Server Configuration

## Overview
This agent connects to [N] MCP servers providing [N] tools total.
All connections use MCP protocol version [X].

## Server Registry

### [Server Name]
- **URL/Transport:** [stdio | sse | http] — [endpoint if network]
- **Purpose:** [What this server provides in one sentence]
- **Auth method:** [none | API key | OAuth | token]
- **Credential location:** [env var name | keychain key]
- **Connection mode:** [always-on | on-demand | lazy]
- **Approved tools from this server:**

| Tool | Purpose | When to use | Rate limit |
|------|---------|-------------|-----------|
| [tool_name] | [description] | [trigger conditions] | [limit] |

- **Prohibited operations:** [any tools NOT to use from this server]
- **Fallback if unavailable:** [what to do if server is down]

[Repeat for each server]

## Tool Selection Guidelines
When multiple tools could accomplish a task, prefer:
1. Most specific tool (narrowest scope)
2. Read-only over read-write
3. Local over remote (prefer tools that don't make external calls)
4. Cheaper over expensive (token/cost consideration)

## Tool Call Limits
| Time period | Max tool calls | Max per server | Notes |
|-------------|---------------|----------------|-------|
| Per task | [N] | [N] | Hard limit |
| Per hour | [N] | [N] | |
| Per day | [N] | [N] | Reset at midnight UTC |

## Error Handling for MCP Calls
- Timeout: [X seconds] per tool call
- On timeout: [retry once | skip | escalate]
- On error: log, retry [N] times with [backoff], then skip or escalate
- On rate limit: wait [X seconds], retry — do not hammer

## Security Rules
- Never pass credentials as tool arguments
- Never call tools not listed in this file
- Log all tool calls with: tool name, inputs (sanitized), output summary
- If tool returns unexpected data format: stop, escalate, do not parse blindly

## Lazy Loading
To prevent context window pollution from tool schemas:
- Load tool schemas only when needed for current task
- Use Tool Search Tool pattern if available
- Defer loading of [list of verbose servers] until explicitly needed
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
