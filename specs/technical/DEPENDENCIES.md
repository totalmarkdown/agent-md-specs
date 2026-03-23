---
spec_name: DEPENDENCIES.md
spec_version: 0.1.0
category: Technical
domain: dependenciesmd.dev
priority: High
volume: "Vol 5 — Organizational & Validation"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# DEPENDENCIES.md

**Category:** Technical
**Domain:** dependenciesmd.dev
**Priority:** High
**Version:** 0.1.0

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
Other agents this agent depends on:
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

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
