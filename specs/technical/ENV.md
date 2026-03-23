---
spec_name: ENV.md
spec_version: 0.1.0
category: Technical
domain: envmd.dev
priority: High
volume: "Vol 12 — Fleet Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

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

```markdown
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

These must come from the secrets manager — never hardcoded:

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
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
