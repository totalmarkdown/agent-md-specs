---
spec_name: QUOTA.md
spec_version: 0.1.0
category: Governance
domain: quotamd.dev
priority: Medium
volume: "Vol 12 — Fleet Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# QUOTA.md

**Category:** Governance
**Domain:** quotamd.dev
**Priority:** Medium
**Version:** 0.1.0

### Purpose
Rate limits and usage quotas this agent enforces on callers.
Different from BUDGET.md (what the agent itself spends) and
SLA.md (what the agent promises) — QUOTA.md defines the limits
placed on the people and systems calling this agent.

### Spec

```markdown
---
agent_name: string
version: semver
quota_enforcement: string   # hard | soft | advisory
rate_limit_per: string      # ip | user | agent | org
---

# [Agent Name] — Quotas & Rate Limits

## Rate Limits

### Per caller (default)
| Window | Limit | Burst | On exceed |
|--------|-------|-------|----------|
| Per second | [N] requests | [N] | 429 + retry-after |
| Per minute | [N] requests | — | 429 |
| Per hour | [N] requests | — | 429 + notify |
| Per day | [N] requests | — | 429 + notify |

### Per organization (enterprise)
| Window | Limit | Notes |
|--------|-------|-------|
| Per minute | [N] requests | Shared across org |
| Per month | [N] tasks | Hard limit |

---

## Usage Quotas

### Free tier
- Tasks per month: [N]
- Max tokens per task: [N]
- Max concurrent tasks: [N]
- Storage: [N MB]
- On limit reached: [graceful error | queue | contact]

### Pro tier
- Tasks per month: [N]
- Max tokens per task: [N]
- Max concurrent tasks: [N]
- On limit reached: [notify at 80%, hard stop at 100%]

### Enterprise
- Custom limits per agreement
- Contact: [sales contact]

---

## Limit Response Format

When a caller exceeds limits, the response is:

```json
{
  "error": "rate_limit_exceeded",
  "message": "You have exceeded [limit type]",
  "limit": N,
  "used": N,
  "resets_at": "ISO-8601",
  "retry_after": N
}
```

HTTP status: 429 Too Many Requests

---

## Quota Monitoring

Callers can check their current usage:

```bash
# Check current quota status
[agent-cli] quota status --caller [your-id]

# Response shows:
# Current period: [start] to [end]
# Tasks used: N/N
# Tokens used: N/N
# Rate limit: N req/min (current: N)
```

---

## Increasing Limits

To request higher limits:
[Contact process or upgrade URL]

Enterprise customers: [sales contact]
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| BUDGET.md | Cost controls and spending limits |
| DELEGATION.md | Authority chain and authorization |
| ENFORCEMENT.md | Policy verification and compliance |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| LIMITS.md | Hard constraints and safety boundaries |
| PERMISSIONS.md | Static resource access control |
| SLA.md | Service level commitments |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
