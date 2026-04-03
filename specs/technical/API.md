---
spec_name: API.md
spec_version: 0.1.0
category: Technical
domain: apimd.dev
priority: High
volume: "Vol 2 — Extended Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
spec_type: static
---


# API.md

**Category:** Technical
**Domain:** apimd.dev
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose
Documents all external API integrations for an agent — endpoints, 
authentication, rate limits, error handling, and approved operations.
More specific than MCP.md (see MCP.md) — covers direct HTTP API calls
that don't go through MCP servers.

### When to create
Any agent that makes direct HTTP calls to external APIs without 
going through an MCP server. Also useful as documentation for 
APIs that have an MCP server but where the agent needs to 
understand the underlying API behavior.

### Spec

```markdown
---
agent_name: string
version: semver
api_count: number
created: date
updated: date
---

# [Agent Name] — API Integration Reference

## API Registry

### [API Name]
- **Base URL:** [base URL — not full endpoints]
- **Documentation:** [link to API docs]
- **Auth type:** [Bearer token | API key | OAuth 2.0 | Basic | None]
- **Credential:** [env var name — never actual credential]
- **Version:** [API version in use, e.g. v2]
- **Environment:** [production | sandbox | both]

#### Approved Endpoints
| Method | Path | Purpose | Rate limit | Notes |
|--------|------|---------|-----------|-------|
| GET | /[path] | [purpose] | [N/hour] | [notes] |
| POST | /[path] | [purpose] | [N/hour] | [notes] |

#### Prohibited Endpoints
Never call these endpoints:
- DELETE /[path] — [reason]
- [any other prohibited operations]

#### Request Rules
- Always include: [required headers]
- Never include: [headers to omit for security]
- Timeout: [X seconds]
- Pagination: [how to handle paginated responses]
- Max response size: [X MB — truncate or paginate if larger]

#### Error Handling
| Status Code | Meaning | Action |
|-------------|---------|--------|
| 400 | Bad request | Log full request, fix and retry once |
| 401 | Unauthorized | Refresh token if possible, else escalate |
| 403 | Forbidden | Log, escalate — do not retry |
| 429 | Rate limited | Wait [Retry-After] header seconds, then retry |
| 500 | Server error | Retry with exponential backoff, max 3 times |
| 503 | Unavailable | Wait [X minutes], retry once, then escalate |

[Repeat for each API]

## Request Logging
Log all API calls with:
- Timestamp, method, URL (no query params with credentials)
- Request size (bytes), response size (bytes)
- Status code, response time (ms)
- Task ID (for correlation)
- Never log: request/response body containing credentials or PII (see PERMISSIONS.md)

## API Health Monitoring
Check these endpoints to verify API availability before starting tasks:
| API | Health endpoint | Expected response | Check interval |
|-----|----------------|------------------|----------------|
| [API name] | [endpoint] | [expected status/body] | [interval] |
```

## Example Use Cases

**Enterprise:** A marketing agency uses API.md to document all approved endpoints for its social media management agent, specifying rate limits per platform (Twitter: 300/15min, LinkedIn: 100/day) and prohibiting DELETE operations on published posts without human approval.

**Multi-Agent Fleet:** A fleet operations team uses API.md health monitoring tables to verify all external API dependencies are available before deploying a new agent version, catching a Stripe API sandbox outage before it caused deployment failures.

**Regulated Industry:** A healthcare data platform uses API.md to restrict its patient record agent to read-only GET endpoints on the EHR system, with explicit prohibition of any write or delete operations and request logging that excludes PII from response bodies.

## Related Specs

| Spec | Relationship |
|------|-------------|
| CLI.md | Command-line interface contract |
| INPUT.md | Accepted input formats |
| MCP.md | Model Context Protocol connections |
| OUTPUT.md | Output formats and delivery |
| PERMISSIONS.md | Static resource access control |
| TOOLS.md | Available tools and capabilities |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
