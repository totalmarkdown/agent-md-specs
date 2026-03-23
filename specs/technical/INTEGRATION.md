---
spec_name: INTEGRATION.md
spec_version: 0.1.0
category: Technical
domain: integrationmd.dev
priority: High
volume: "Vol 2 — Extended Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# INTEGRATION.md

**Category:** Technical
**Domain:** integrationmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Documents all third-party service integrations — not just APIs 
and MCP servers, but webhooks, event streams, file system mounts, 
databases, and any other external connection points.

### Spec

```markdown
---
agent_name: string
version: semver
integration_count: number
created: date
updated: date
---

# [Agent Name] — Integration Map

## Integration Overview
```
[Agent Name]
├── APIs (see API.md)
├── MCP Servers (see MCP.md)
├── Databases
│   ├── [DB name]: [connection type, read/write]
│   └── [DB name]: [connection type, read only]
├── File Systems
│   ├── [path]: [read/write, purpose]
│   └── [path]: [read only, purpose]
├── Event Streams
│   ├── [stream]: [subscribe/publish, topics]
│   └── [stream]: [subscribe only, topics]
├── Webhooks (outbound)
│   └── [endpoint]: [when triggered, payload format]
└── Webhooks (inbound)
    └── [endpoint this agent listens on]: [events handled]
```

## Database Connections
| Database | Type | Access | Schema | Purpose |
|----------|------|--------|--------|---------|
| [name] | postgres/sqlite/etc | read-write | [file] | [purpose] |

## File System Access
| Path | Access | Purpose | Retention |
|------|--------|---------|-----------|
| [path] | read-only | [purpose] | [N/A — not written] |
| [path] | read-write | [purpose] | [X days] |

## Event Streams
| Stream | Direction | Topics/Queues | Format | Notes |
|--------|-----------|--------------|--------|-------|
| [stream name] | subscribe | [topic list] | JSON | [notes] |

## Webhook Configuration

### Outbound (this agent calls)
| Event | Endpoint | Method | Payload | Retry |
|-------|----------|--------|---------|-------|
| [event] | [URL] | POST | [format] | [N times] |

### Inbound (external systems call this agent)
| Endpoint | Auth | Events handled | Response format |
|----------|------|----------------|----------------|
| [path] | [method] | [events] | [format] |

## Dependency Map
If any integration is unavailable, these tasks are affected:
| Integration | If unavailable | Impact | Fallback |
|------------|---------------|--------|----------|
| [name] | [tasks blocked] | [severity] | [fallback behavior] |
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
