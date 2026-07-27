---
spec_name: "AUDITTRAIL.md"
spec_version: "1.0.0"
category: "Compliance"
tier: core
priority: High
agent_name: "Atlas"
version: "2.1.0"
org: "Acme Corp"
hash_algorithm: "SHA-256"
chain_type: "append-only-hash-chain"
retention_years: 7
signing_method: "X.509"
created: "2025-11-01"
updated: "2026-03-15"
---

# Atlas -- Audit Trail

## Audit Architecture

Atlas produces an append-only, hash-chained audit log for every action it
takes. This log is the authoritative record of Atlas's behavior and is designed
to satisfy SOX, GDPR, and SOC2 audit requirements simultaneously.

## Log Entry Structure

Each audit entry contains:

```json
{
  "entry_id": "uuid-v4",
  "session_id": "uuid-v4",
  "timestamp": "ISO-8601 with microseconds, UTC",
  "agent_id": "d4e8f1a3-7b2c-4d9e-a6f5-3c1d8e7b4a2f",
  "agent_version": "2.1.0",
  "action_type": "read | write | execute | escalate | deny",
  "target": "system and resource identifier",
  "intent_hash": "SHA-256 hash of the declared intent",
  "result": "success | failure | denied | timeout",
  "delegation_id": "del-2026Q1-atlas-finance",
  "data_sources": ["list of PROVENANCE.md source identifiers used"],
  "previous_hash": "SHA-256 hash of the preceding log entry",
  "entry_hash": "SHA-256 hash of this entry including previous_hash",
  "signature": "X.509 signature over entry_hash"
}
```

## Hash Chain

The audit log forms a hash chain where each entry includes the hash of the
previous entry. This makes it computationally infeasible to modify or delete
historical entries without detection.

- **Algorithm:** SHA-256
- **Chain initialization:** First entry in each session chains from the
  session creation entry, which itself chains from the last entry of the
  previous session
- **Cross-session continuity:** The chain is continuous across sessions.
  Session boundaries are marked but do not break the chain.
- **Integrity verification:** Hourly automated verification of the full chain
  by an independent monitoring service (audit-monitor.acme.corp)
- **External anchor:** Daily chain head hash published to Acme's transparency
  log at transparency.acme.corp, providing an independent timestamp anchor

## Retention Policy

| Regulation | Requirement | Atlas Implementation |
|------------|-------------|---------------------|
| SOX | 7 years for financial records | All audit entries retained 7 years |
| GDPR | Proportionate retention | No PII in audit logs; financial aggregates only |
| SOC2 | Sufficient for annual audit | Full chain available for SOC2 Type II auditor |

- **Primary storage:** Encrypted at rest (AES-256-GCM) on Acme's private cloud
  object storage, us-east-1 region
- **Backup:** Daily encrypted backup to geographically separate region (us-west-2)
- **Immutability:** Object lock with 7-year retention, no delete capability
  even for administrators
- **Deletion:** Automated purge after 7 years + 90-day grace period

## Query Interface

Authorized personnel can query Atlas's audit trail through a read-only API.

- **Endpoint:** audit.acme.corp/agents/atlas
- **Authentication:** mTLS + role-based access (Internal Audit, Compliance,
  InfoSec, CFO's Office)
- **Query capabilities:** Filter by session, time range, action type, target
  system, result code
- **Export formats:** JSON, CSV (for audit workpapers)
- **Rate limiting:** 100 queries per hour per user

## Compliance Mapping

### SOX Section 302/404

- Every financial data access is logged with source, query, and timestamp
- Every report generation includes the complete list of input data sources
- Every report delivery logs the recipients and delivery confirmation
- Chain integrity provides tamper evidence for auditors

### GDPR Article 15 (Right of Access)

- Atlas does not process personal data in normal operation
- If personal data is inadvertently encountered, the event is logged and the
  data is not retained beyond the session

### SOC2 Trust Services Criteria

- **CC6.1 (Logical Access):** All access events logged with authentication details
- **CC7.2 (System Monitoring):** Continuous hash chain verification serves as
  anomaly detection
- **CC8.1 (Change Management):** Agent version and configuration hash logged
  per session

## Incident Audit

In the event of a security incident or compliance investigation:

1. Audit log is placed on legal hold (retention extended indefinitely)
2. Chain integrity is verified by independent auditor
3. Relevant entries are exported with full chain context for forensic analysis
4. Access to audit query API is logged separately during the investigation period
