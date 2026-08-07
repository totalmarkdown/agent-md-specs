---
spec_name: DEPENDENCIES.md
spec_version: 0.1.0
category: Technical
priority: High
volume: "Vol 5 — Organizational & Validation"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
status: draft
spec_type: static
---


# DEPENDENCIES.md

**Category:** Technical
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose
Complete list of everything this agent depends on to function — 
software packages, other agents, external services, data sources, 
and human inputs. Makes dependency chains visible and enables 
impact analysis when dependencies change.

### Spec

```markdown
---
agent_name: string
version: semver
critical_dependency_count: number  # Must-have dependencies
optional_dependency_count: number
last_updated: date
---

# [Agent Name] — Dependencies

## Dependency Summary
| Type | Critical | Optional | Total |
|------|---------|---------|-------|
| Software packages | [N] | [N] | [N] |
| Other agents | [N] | [N] | [N] |
| External services | [N] | [N] | [N] |
| Data sources | [N] | [N] | [N] |
| Human inputs | [N] | [N] | [N] |

## Software Dependencies

### Runtime Requirements
| Package | Version | Purpose | License | Critical |
|---------|---------|---------|---------|---------|
| [package] | [version] | [use] | [license] | [yes/no] |

### Optional Enhancements
| Package | Version | Adds | Without it |
|---------|---------|------|-----------|
| [package] | [version] | [feature] | [degraded behavior] |

## Agent Dependencies
Other agents this agent depends on (see VERSION.md for version compatibility):
| Agent | Version | Purpose | Critical | Fallback |
|-------|---------|---------|---------|---------|
| [agent] | [version] | [why needed] | [yes/no] | [what if unavailable] |

## External Service Dependencies
| Service | Purpose | Availability SLA | If unavailable |
|---------|---------|-----------------|---------------|
| [service] | [use] | [uptime %] | [fallback behavior] |

## Data Source Dependencies
| Source | Data type | Update frequency | If stale/unavailable |
|--------|-----------|-----------------|---------------------|
| [source] | [type] | [frequency] | [impact + fallback] |

## Human Dependencies
Tasks that require human input to complete:
| Human input needed | When | From whom | Timeout behavior |
|-------------------|------|----------|-----------------|
| [input type] | [trigger] | [role] | [what happens if not received] |

## Dependency Health
| Dependency | Status | Last checked | Issues |
|-----------|--------|-------------|--------|
| [dep] | [✓ healthy / ⚠ degraded / ✗ down] | [time] | [none / description] |

## Update Policy
| Dependency type | Update frequency | Testing required | Approval |
|----------------|-----------------|-----------------|---------|
| Security patches | Immediately | Smoke test | Auto |
| Minor versions | Monthly | Full test suite | Team lead |
| Major versions | Quarterly | Full test + eval | Human approval |

## Dependency Audit
Last full dependency audit: [date]  
Next scheduled audit: [date]  
Audit command: `[audit command]`
```

## Example Use Cases

**Enterprise:** A fintech company uses DEPENDENCIES.md to identify that its payment processing agent depends on three critical external services (Stripe, Plaid, SendGrid), each with documented fallback behaviors — so when Plaid has an outage, the agent degrades gracefully to manual bank verification.

**Multi-Agent Fleet:** A fleet manager uses DEPENDENCIES.md across all agents to build a dependency graph, discovering that 12 agents share a critical dependency on a single translation service and creating a redundancy plan before the next incident.

**Regulated Industry:** An aerospace manufacturer uses DEPENDENCIES.md to document human input dependencies for its quality inspection agent, specifying that engineer sign-off is required within 4 hours for critical defect findings and defining timeout behavior when approval is not received.

## Related Specs

| Spec | Relationship |
|------|-------------|
| INPUT.md | Accepted input formats |
| MCP.md | Model Context Protocol connections |
| OUTPUT.md | Output formats and delivery |
| PERMISSIONS.md | Static resource access control |
| TOOLS.md | Available tools and capabilities |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
