---
spec_name: NETWORK.md
spec_version: 0.1.0
category: Technical
domain: networkmd.dev
priority: High
volume: "Vol 12 — Fleet Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---


# NETWORK.md

**Category:** Technical
**Domain:** networkmd.dev
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose
Network requirements and firewall rules for an agent —
what it calls outbound, what ports it needs, data residency
requirements, and VPN/proxy configuration.

Critical for enterprise deployments behind corporate firewalls
and for compliance with data residency requirements.

### Spec

````markdown
---
agent_name: string
version: semver
requires_internet: boolean
data_residency: list        # [EU | US | APAC | any]
vpn_required: boolean
last_reviewed: date
---

# [Agent Name] — Network Requirements

## Network Profile
**Requires internet:** [Yes | No — can run fully offline]
**Data residency:** [EU only | US only | any]
**VPN required:** [Yes | No | Optional]
**Proxy support:** [Yes | No]

---

## Outbound Connections

### Required (agent will not function without these)

| Destination | Port | Protocol | Purpose | Data sent |
|-------------|------|---------|---------|----------|
| api.anthropic.com | 443 | HTTPS/TLS | LLM inference | Prompts, no PII unless included |
| [service.domain.com] | 443 | HTTPS | [purpose] | [what data] |

### Optional (degraded functionality without these)

| Destination | Port | Purpose | Without it |
|-------------|------|---------|-----------|
| [service] | [port] | [purpose] | [what stops working] |

---

## Firewall Rules

If deploying behind a corporate firewall, add these rules:

### Allowlist (outbound)
```
# Required
api.anthropic.com:443/TCP
[other.required.domain]:443/TCP

# Optional
[optional.domain]:443/TCP
```

### No inbound rules required
This agent does not accept inbound connections unless
[MCP server mode | API server mode] is enabled.

### If running as a server (inbound)
| Port | Protocol | Source | Purpose |
|------|---------|--------|---------|
| [N] | TCP | [source] | [purpose] |

---

## Data Residency

### What data leaves your network
| Data type | Sent to | Purpose | Residency |
|-----------|---------|---------|----------|
| Task prompts | Anthropic API | LLM inference | US/EU |
| [other data] | [destination] | [purpose] | [region] |

### What data stays local
- MEMORY.md contents
- Agent configuration files
- Task outputs
- Logs (unless remote logging enabled)

### Compliance
See SANDBOX.md for agent isolation and containment rules.
- GDPR Article 44 transfers: [adequacy decision | SCCs | not applicable]
- Data Processing Agreement with Anthropic: [yes — see docs.anthropic.com]

---

## Proxy Configuration

If your network requires a proxy:

```bash
export HTTP_PROXY=http://proxy.company.com:8080
export HTTPS_PROXY=http://proxy.company.com:8080
export NO_PROXY=localhost,127.0.0.1,[internal.services]
```

The agent respects standard proxy environment variables.
Certificate inspection proxies: [supported | not supported — explain]

---

## Bandwidth Estimates

| Operation | Typical data transfer |
|-----------|----------------------|
| Standard task | ~10KB (prompt + response) |
| Large document task | ~100KB |
| Per 1000 tasks | ~10MB |
| Per day (at [N] tasks) | ~[X]MB |
````

## Example Use Cases

**Enterprise:** A Fortune 500 company uses NETWORK.md to generate firewall allowlist rules for their corporate proxy, enabling their research agent to reach api.anthropic.com:443 and three approved data provider domains while blocking all other outbound traffic.

**Multi-Agent Fleet:** A cloud platform team uses NETWORK.md bandwidth estimates across all agents to plan network capacity, calculating that their 100-agent fleet generates approximately 1GB of daily API traffic and provisioning accordingly.

**Regulated Industry:** A European bank uses NETWORK.md's data residency section to verify that all agent data stays within EU boundaries, documenting GDPR Article 44 adequacy decisions and Standard Contractual Clauses for any cross-border data transfers to LLM providers.

## Related Specs

| Spec | Relationship |
|------|-------------|
| INPUT.md | Accepted input formats |
| MCP.md | Model Context Protocol connections |
| MEMORY.md | Individual agent memory governance |
| OUTPUT.md | Output formats and delivery |
| PERMISSIONS.md | Static resource access control |
| TOOLS.md | Available tools and capabilities |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
