---
spec_name: ENV.md
spec_version: 0.1.0
category: Technical
domain: envmd.dev
priority: High
volume: "Vol 12 — Fleet Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---
> **Static Configuration** — committed to your repository


# ENV.md

**Category:** Technical
**Domain:** envmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Complete environment variable specification for an agent —
all variables it reads from the environment, their types,
defaults, validation rules, and which environments they apply to.

Different from SECRETS.md (security-sensitive credentials only) —
ENV.md covers ALL environment variables including non-sensitive
configuration like log levels, feature flags, port numbers,
and service URLs.

### Spec

````markdown
---
agent_name: string
version: semver
env_count: number
env_file_locations: list   # .env.development, .env.production, etc.
secrets_manager: string    # where sensitive vars come from
---

# [Agent Name] — Environment Variables

## Quick Reference

```bash
# Minimum required to run in development
export NODE_ENV=development
export [REQUIRED_VAR_1]=[value]
export [REQUIRED_VAR_2]=[value]
# Sensitive vars — load from Doppler or .env.local:
# [SECRET_VAR_1], [SECRET_VAR_2]
```

---

## Variable Reference

### Application

| Variable | Type | Default | Required | Description |
|----------|------|---------|---------|-------------|
| `NODE_ENV` | string | development | yes | Runtime environment |
| `PORT` | number | 3000 | no | Port to listen on |
| `LOG_LEVEL` | string | info | no | debug/info/warn/error |
| `[VAR_NAME]` | [type] | [default] | [yes/no] | [description] |

### External Services (non-sensitive)

| Variable | Type | Default | Required | Description |
|----------|------|---------|---------|-------------|
| `[SERVICE_URL]` | string | [url] | yes | [service] endpoint |
| `[SERVICE_TIMEOUT_MS]` | number | 30000 | no | Request timeout |

### Feature Flags

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| `FEATURE_[NAME]` | boolean | false | [What this enables] |

### Sensitive Variables (see SECRETS.md for full detail)

These must come from the secrets manager (see VAULT.md for fleet-wide governance) — never hardcoded:

| Variable | Source | Description |
|----------|--------|-------------|
| `[SECRET_VAR]` | Doppler/[project] | [what it is] |

---

## Environment Files

| File | Purpose | Committed to git |
|------|---------|-----------------|
| `.env.example` | Template with all vars, no values | Yes |
| `.env.local` | Local overrides | No — gitignored |
| `.env.development` | Dev defaults | Yes (no secrets) |
| `.env.production` | Prod config (no secrets) | Yes |
| `.env.test` | Test environment | Yes |

---

## Validation

At startup, the agent validates all required variables are set.
Missing required variables cause immediate startup failure with
a clear error message listing what is missing.

```bash
# Validate environment before starting
[agent-cli] env validate

# Show all current env vars (names only, values masked)
[agent-cli] env list --mask-values
```

---

## Environment Differences

| Variable | Development | Staging | Production |
|----------|-------------|---------|-----------|
| `LOG_LEVEL` | debug | info | warn |
| `[VAR]` | [dev value] | [staging value] | [prod value] |
````

## Example Use Cases

**Enterprise:** A platform team uses ENV.md to provide new developers with a copy-paste quick reference of the minimum required environment variables to run the agent locally, eliminating the "it works on my machine" problem across a 30-person engineering team.

**Multi-Agent Fleet:** A fleet deployment system reads ENV.md from each agent to auto-generate .env files per environment, validating all required variables are set before startup and failing fast with a clear error listing any missing configuration.

**Regulated Industry:** A government agency uses ENV.md to separate sensitive variables (loaded from a FedRAMP-authorized secrets manager) from non-sensitive configuration (LOG_LEVEL, PORT), ensuring environment files committed to git never contain classified values.

## Related Specs

| Spec | Relationship |
|------|-------------|
| INPUT.md | Accepted input formats |
| MCP.md | Model Context Protocol connections |
| OUTPUT.md | Output formats and delivery |
| PERMISSIONS.md | Static resource access control |
| SECRETS.md | Required credentials manifest |
| TOOLS.md | Available tools and capabilities |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
