---
spec_name: QUOTA.md
spec_version: 0.1.0
category: Governance
priority: Medium
volume: "Vol 12 — Fleet Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---


# QUOTA.md

**Category:** Governance
**Priority:** Medium
**Version:** 0.1.0 **Type:** Static

### Purpose
Rate limits and usage quotas this agent enforces on callers.
Different from BUDGET.md (what the agent itself spends) and
SLA.md (what the agent promises) — QUOTA.md defines the limits
placed on the people and systems calling this agent.
_See LIMITS.md for the agent's own hard constraints._

### Spec

````markdown
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
- On limit reached: [notify at 80%, hard stop at 100%] (see ENFORCEMENT.md)

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
````

## Example Use Cases

**Enterprise:** An internal API agent enforces per-department rate limits so that the marketing team's heavy batch analysis jobs cannot starve the support team's real-time customer lookup requests, with each department receiving its own quota allocation from the shared capacity.

**Multi-Agent Fleet:** A marketplace agent serving 500 third-party integrations enforces tiered quotas — free-tier callers get 100 tasks/month with 5 requests/minute, while enterprise callers get custom limits negotiated per contract, with all callers receiving standardized 429 responses and retry-after headers when limits are hit.

**Regulated Industry:** A healthcare records agent enforces strict per-user query quotas to prevent bulk data extraction attempts, logging every quota enforcement event and alerting the security team when any caller approaches their daily limit at an unusual rate.

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
