---
spec_name: TOOLS.md
spec_version: 0.1.0
category: Technical
domain: toolsmd.dev
priority: High
volume: "Vol 5 — Organizational & Validation"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# TOOLS.md

**Category:** Technical
**Domain:** toolsmd.dev
**Priority:** High
**Version:** 0.1.0

**Priority:** HIGH  
**Version:** 0.1.0

### Purpose
Complete inventory of every tool an agent has access to — 
file system operations, code execution, web browsing, 
calculators, databases, and any other capability tools.
Different from MCP.md (protocol connections) and API.md 
(HTTP endpoints) — TOOLS.md catalogs the agent's full 
toolbox with usage guidelines for each tool.

### Spec

```markdown
---
agent_name: string
version: semver
total_tools: number
tool_framework: string   # MCP | function-calling | langchain | custom
last_updated: date
---

# [Agent Name] — Tools

## Tool Inventory

### File System Tools
| Tool | Permission | Scope | When to use |
|------|-----------|-------|-------------|
| read_file | ✓ allowed | workspace only | Reading any file |
| write_file | ✓ allowed | designated folders | Saving outputs |
| list_directory | ✓ allowed | workspace only | Exploring structure |
| delete_file | ⚠ restricted | temp files only | Cleanup only |
| move_file | ✓ allowed | workspace only | Reorganization |
| search_files | ✓ allowed | workspace only | Finding content |

### Code Execution Tools
| Tool | Language | Timeout | Restrictions |
|------|---------|---------|-------------|
| execute_python | Python 3.10+ | 30s | No network access |
| execute_bash | Bash | 10s | Pre-approved commands only |
| execute_js | Node.js 18+ | 15s | No file system write |
| evaluate_math | Python | 5s | Math operations only |

### Web Tools
| Tool | Allowed domains | Rate limit | Cache |
|------|----------------|-----------|-------|
| web_search | All | 10/min | 1 hour |
| web_fetch | [approved domains] | 20/min | 30 min |
| web_screenshot | [approved domains] | 5/min | No |

### Data Tools
| Tool | Source | Access | Rate limit |
|------|--------|--------|-----------|
| query_database | [DB name] | Read-only | 100/min |
| read_csv | Local files | Read | No limit |
| call_api | See API.md | Varies | See API.md |

### AI/ML Tools
| Tool | Model | Purpose | Cost |
|------|-------|---------|------|
| generate_image | [model] | Visual outputs | $[X]/image |
| transcribe_audio | [model] | Speech to text | $[X]/min |
| embed_text | [model] | Semantic search | $[X]/1K tokens |
| classify | [model] | Content classification | $[X]/call |

### Communication Tools
| Tool | Channel | Auth | Rate limit |
|------|---------|------|-----------|
| send_email | SMTP | Env var | 100/day |
| post_slack | [workspace] | Bot token | 1/sec |
| create_ticket | Linear/Jira | API key | 60/min |
| send_webhook | Approved URLs | See API.md | 100/min |

### MCP Tools
See MCP.md for full MCP server inventory.
Quick reference:
| Server | Tools available | Primary use |
|--------|----------------|------------|
| [server] | [N] tools | [use case] |

## Tool Selection Guidelines

### Always prefer
- Read over write when both can accomplish the goal
- Local computation over API calls when quality is equivalent
- Cached results over fresh fetch when recency doesn't matter
- Specific tool over general tool (file reader vs bash)

### Tool combinations to avoid
- [Dangerous combination 1]: [why and what to do instead]
- [Dangerous combination 2]: [why and what to do instead]

## Tool Approval Status
| Tool | Status | Added | Approved by |
|------|--------|-------|------------|
| [tool] | ✓ approved | [date] | [approver] |
| [tool] | ⚠ restricted | [date] | [approver] |
| [tool] | ✗ prohibited | [date] | [approver] |

## Adding New Tools
To request access to a new tool:
1. Document the tool in a PR to this file
2. Justify why existing tools don't suffice
3. Specify usage limits and safety constraints
4. Get approval from: [role]

## Tool Usage Logging
All tool calls logged to LOGS.md with:
- Tool name, inputs (sanitized), outputs (summary)
- Duration, cost (if applicable), success/failure
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
