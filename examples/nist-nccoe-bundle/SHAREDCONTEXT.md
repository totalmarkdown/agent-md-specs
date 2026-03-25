---
spec_name: "SHAREDCONTEXT.md"
spec_version: "1.0.0"
category: "Coordination"
tier: core
priority: High
domain: sharedcontextmd.dev
agent_name: "Atlas"
agent_version: "2.1.0"
---

# Shared Context Pool

This pool serves the **Finance Analysis Team** at Acme Corp. Atlas is the primary contributor; the CFO Dashboard Agent and Compliance Monitor consume shared context for downstream reporting and audit.

## Access Control Matrix

| Agent              | Read | Write | Delete | Admin | Delegation Ref          |
|--------------------|------|-------|--------|-------|-------------------------|
| Atlas              | yes  | yes   | no     | no    | DELEGATION.md #atlas    |
| CFO Dashboard      | yes  | no    | no     | no    | —                       |
| Compliance Monitor | yes  | no    | no     | yes   | DELEGATION.md #audit    |

Compliance Monitor holds admin for audit purposes only — it can inspect provenance and flag entries but cannot modify financial data.

## Memory Schema

Every entry written to the pool must include: `entry_id` (UUID), `source_agent`, `timestamp` (ISO-8601), `entry_type` (fact | observation | decision | alert), `confidence` (0.0–1.0), `classification` (confidential by default for all financial data), and `content`. Provenance must reference the originating data source (e.g., Bloomberg terminal, SEC EDGAR, internal ERP).

## Retention Policy

- **Financial data entries:** TTL 90 days, then archived to cold storage.
- **Regulatory alerts (OFAC, sanctions, SEC notices):** Permanent — no TTL, no eviction.
- **Max pool size:** 500 MB. Eviction strategy: `oldest_first` for expired entries only.
- Evicted entries are archived (never deleted) per Acme Corp data-retention policy.

## Inheritance Rules

Atlas reads from the **Acme Corp org-level shared context** (`ORG-SHAREDCONTEXT.md`), which contains company-wide policies, OFAC sanctions lists, and compliance baselines. Override policy: `no_override` — team-level entries cannot contradict org-level entries. Conflicts resolved by `delegation_authority`.

## Synchronization

Sync frequency: `real_time` for regulatory alerts, `batch` (every 15 min) for financial data. Consistency model: `causal` — entries referencing the same instrument maintain causal ordering.

## Integration with Individual Memory

Atlas retains its own working memory (SESSION.md) for in-progress analyses. Only finalized facts and decisions are promoted to the shared pool after sanitization (see MEMORYSAFETY.md).
