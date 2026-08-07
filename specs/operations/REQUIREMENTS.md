---
spec_name: REQUIREMENTS.md
spec_version: 0.1.0
category: Operations
priority: Very High
volume: "Vol 12 — Fleet Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
status: draft
spec_type: static
---


# REQUIREMENTS.md

**Category:** Operations
**Priority:** Very High
**Version:** 0.1.0 **Type:** Static

### Purpose
The complete "can I run this agent?" document —
everything needed to deploy and operate this agent:
hardware minimums, OS requirements, runtime versions,
network access, all API keys and MCP connections,
and estimated running cost.

Where DEPENDENCIES.md lists software packages and
TOOLS.md lists available tools, REQUIREMENTS.md is
the unified pre-flight checklist. Before deploying
this agent, read this file.

### Spec

````markdown
---
agent_name: string
version: semver
minimum_viable: boolean   # Can it run with just the required items?
estimated_monthly_cost: string
last_updated: date
---

# [Agent Name] — Requirements

## At a Glance

| Category | Minimum | Recommended |
|----------|---------|------------|
| RAM | [N GB] | [N GB] |
| CPU | [N cores] | [N cores] |
| Storage | [N GB] | [N GB] |
| Network | [bandwidth] | [bandwidth] |
| Monthly cost | ~$[X] | ~$[X] |

---

## Hardware Requirements

### Minimum (agent will run but may be slow)
- **RAM:** [N GB]
- **CPU:** [N cores, architecture]
- **Storage:** [N GB free disk space]
- **GPU:** [not required | optional for X | required for Y]

### Recommended (optimal performance)
- **RAM:** [N GB]
- **CPU:** [N cores]
- **Storage:** [N GB SSD]
- **GPU:** [specification if needed]

### Known good hardware configurations
- Mac Mini M4 Pro (16GB+) — tested, works well
- Ubuntu 22.04 on [cloud instance type] — tested, production use
- [Other configurations]

---

## Software Requirements

### Runtime
| Software | Minimum version | Recommended | Install |
|----------|----------------|-------------|---------|
| [Runtime e.g. Node.js] | [version] | [version] | [command] |
| [Python] | [version] | [version] | [command] |
| [Docker] | [version] | [version] | [url] |

### Operating System
- **Linux:** Ubuntu 20.04+ / Debian 11+ / RHEL 8+
- **macOS:** 13 (Ventura)+
- **Windows:** WSL2 with Ubuntu 22.04 (not native Windows)

### Required CLI Tools
| Tool | Version | Purpose | Install |
|------|---------|---------|---------|
| [tool] | [version] | [use] | [command] |

---

## Network Requirements

### Outbound connections required
| Destination | Port | Protocol | Purpose |
|-------------|------|---------|---------|
| api.anthropic.com | 443 | HTTPS | LLM inference |
| [other service] | [port] | [protocol] | [purpose] |

### Firewall rules needed
If deploying behind a corporate firewall, allow outbound to:
```
api.anthropic.com:443
[other required domains]:443
```

### Data residency
- Data processed in: [regions]
- Data stored in: [regions]
- Compliant with: [GDPR | CCPA | HIPAA | other]

---

## API Credentials Required

All credentials should be stored in SECRETS.md system.
This table shows what you need to obtain before deployment.

| Credential | Service | Where to obtain | Required | Monthly cost |
|-----------|---------|----------------|---------|-------------|
| LLM API key | Anthropic | console.anthropic.com | Yes | ~$[X] |
| [other key] | [service] | [URL] | [yes/no] | ~$[X] |

---

## MCP Servers Required

| MCP Server | Purpose | Install | Required |
|-----------|---------|---------|---------|
| [server name] | [what it provides] | [install command] | [yes/no] |

See MCP.md for full MCP configuration details. For step-by-step first-run instructions, see SETUP.md.

---

## External Services Required

| Service | Purpose | Free tier | Required |
|---------|---------|-----------|---------|
| [Neon] | Database | Yes (limited) | Yes |
| [service] | [purpose] | [yes/no] | [yes/no] |

---

## Estimated Running Costs

Based on [N] tasks per day at average [N] tokens per task:

| Cost item | Per day | Per month | Notes |
|-----------|---------|-----------|-------|
| LLM API (input) | $[X] | $[X] | [N] tokens/day |
| LLM API (output) | $[X] | $[X] | [N] tokens/day |
| Database | $[X] | $[X] | [plan] |
| [other] | $[X] | $[X] | |
| **Total** | **~$[X]** | **~$[X]** | |

---

## Pre-deployment Checklist

```bash
# Run this to verify all requirements are met
[agent-cli] requirements check

# What it verifies:
[ ] Node/Python/runtime version meets minimum
[ ] Required environment variables set (see ENV.md)
[ ] All API credentials valid (see SECRETS.md)
[ ] All MCP servers reachable
[ ] Database connection successful
[ ] Sufficient disk space
[ ] Network access to required endpoints
```

---

## Quick Start

If all requirements are met, get running in [N] minutes:

```bash
# 1. Clone and install
git clone [repo]
cd [agent]
[install command]

# 2. Configure environment
cp .env.example .env.local
# Edit .env.local with your credentials
# Or: doppler run -- [start command]

# 3. Verify requirements
[agent-cli] requirements check

# 4. Start
[start command]

# 5. Smoke test (see HEALTHCHECK.md for full verification)
[test command]
```
````

## Example Use Cases

**Enterprise:** A multinational deploys its compliance-monitoring agent across AWS regions using REQUIREMENTS.md as the pre-flight checklist -- verifying that each region has the required Anthropic API access, minimum 8GB RAM instances, and outbound firewall rules for all dependency endpoints.

**Multi-Agent Fleet:** A platform team uses REQUIREMENTS.md across 40 agents to generate a unified infrastructure bill-of-materials, identifying that 12 agents share the same Neon database dependency and planning capacity accordingly before a product launch.

**Regulated Industry:** A defense contractor's intelligence-analysis agent documents ITAR-compliant data residency constraints in REQUIREMENTS.md, ensuring deployment only occurs in US-based infrastructure with FedRAMP-authorized cloud services.

## Related Specs

| Spec | Relationship |
|------|-------------|
| CIRCUITBREAKER.md | Failure containment and blast radius |
| ENFORCEMENT.md | Policy verification and compliance |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| HEALTHCHECK.md | Liveness and readiness checks |
| MCP.md | Model Context Protocol connections |
| MONITOR.md | Observability and alerting |
| SECRETS.md | Required credentials manifest |
| TOOLS.md | Available tools and capabilities |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
