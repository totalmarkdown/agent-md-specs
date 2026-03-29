---
spec_name: AUDITTRAIL.md
spec_version: 0.1.0
category: Compliance
domain: audittrailmd.dev
priority: Very High
volume: "Vol 14 — Agent Identity, Accountability & Compliance"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
spec_type: runtime_schema
---
> **Runtime Schema** — defines the format for API payloads, session tokens, or log entries


# AUDITTRAIL.md

**Category:** Compliance
**Domain:** audittrailmd.dev
**Priority:** Very High
**Version:** 0.1.0

### Purpose
Defines the requirements for a tamper-resistant, verifiable record
of every significant action an agent takes. The agent's "black box"
— a complete, immutable ledger that enables reconstruction of what
happened, why, and under whose authority.

Without an audit trail, there is no accountability. When an agent
makes a consequential decision, regulators, operators, and affected
parties must be able to trace the chain from input to output,
understand the reasoning, and verify the authority under which the
agent acted.

At fleet scale, AUDITTRAIL.md enables:
- Post-incident forensic analysis across multi-agent workflows
- Regulatory compliance across jurisdictions with differing retention rules
- Non-repudiation — proof that a specific agent performed a specific action
- Continuous monitoring for policy violations and anomalous behavior
- Chain of custody for data transformations and decisions

### When to Create This File
Every agent that performs actions with observable consequences —
data modifications, external API calls, financial transactions,
communications, or decisions that affect humans. Required for all
agents operating under regulatory frameworks (GDPR, HIPAA, SOC 2,
EU AI Act). Strongly recommended for any agent above "untrusted"
trust level.

### Spec

````markdown
---
agent_name: string
agent_id: string              # Must match WHOAMI.md agent_id
version: semver
log_format: string            # structured_yaml | structured_json | jsonl
tamper_resistance: string     # hash_chain | signed_entries | blockchain_anchor | append_only
retention_policy: string      # regulatory_max | custom
storage_backend: string       # local_fs | s3 | database | siem | immutable_ledger
last_integrity_check: date
spec_version: string
---

# [Agent Name] — Audit Trail Configuration

## Audit Event Schema

Every auditable action produces an event conforming to this schema:

```yaml
event:
  event_id: "uuid-v4"                    # Globally unique event identifier
  timestamp: "ISO-8601 with timezone"    # When the action occurred (UTC)
  sequence_number: integer               # Monotonically increasing per agent
  previous_event_hash: "sha256:..."      # Hash of prior event (chain integrity)

agent:
  agent_id: "uuid matching WHOAMI.md"    # Which agent acted
  agent_version: "semver"                # Agent version at time of action
  attestation_ref: "credential-id"       # Reference to ATTESTATION.md credential used

session:
  session_id: "uuid-v4"                  # Current session identifier (see SESSION.md)
  delegation_chain:                      # Full authority chain
    - principal: "human:jane@org.com"    # Original authority
      granted: "ISO-8601"
      scope: "task-description"
    - principal: "agent:orchestrator-01" # Delegated to
      granted: "ISO-8601"
      scope: "subtask-description"

action:
  intent_hash: "sha256:..."             # Hash of INTENT or instruction (see INTENT.md)
  action_type: "enum"                   # query | create | update | delete |
                                        # execute | communicate | decide | escalate
  target_resource: "resource-uri"       # What was acted upon
  input_hash: "sha256:..."              # Hash of inputs consumed
  output_hash: "sha256:..."            # Hash of outputs produced
  result: "enum"                        # success | failure | partial | timeout | denied
  error_code: "string or null"          # Error identifier if result != success
  duration_ms: integer                  # How long the action took

authorization:
  human_approval_ref: "approval-id"     # Reference to human approval if required
  policy_evaluated: "policy-name"       # Which policy authorized this action
  guardrail_triggers: []                # Any guardrails that fired during action

metadata:
  classification: "enum"                # public | internal | confidential | restricted
  pii_present: boolean                  # Whether action involved PII
  cost_incurred: "decimal or null"      # Token cost, API cost, etc.
  tags: []                              # Operator-defined tags for filtering
```

---

## Tamper Resistance

**Method:** [Append-only log | Hash chain | Signed entries | Blockchain anchor]

### Hash Chain (Recommended)
Each event includes the SHA-256 hash of the previous event,
creating a verifiable chain. Any modification to a past event
breaks the chain from that point forward.

```
Event N: hash = SHA-256(event_data_N + hash_of_event_N-1)
Event N+1: hash = SHA-256(event_data_N+1 + hash_of_event_N)
```

Verification: Walk the chain from genesis event. If any hash
does not match its recomputed value, the chain is broken at
that point and all subsequent events are suspect.

_See ENFORCEMENT.md for scheduled audit verification and
automated integrity checks._

### Signed Entries
Each event is signed using the agent's ATTESTATION.md credentials.
- **Signing key:** [reference to attestation key]
- **Signature algorithm:** [Ed25519 | ECDSA-P256 | RSA-PSS]
- **Countersigning:** [none | timestamping authority | witness co-signature]

### Blockchain Anchor (Optional)
Periodic hash of the log is anchored to an external blockchain
or timestamping service for independent verification.
- **Anchor frequency:** [every N events | every N minutes | daily]
- **Anchor target:** [Bitcoin OP_RETURN | Ethereum | RFC 3161 TSA | none]
- **Last anchor:** [timestamp and reference]

### Integrity Verification
| Check | Frequency | Method | Alert on Failure |
|-------|-----------|--------|------------------|
| Hash chain integrity | [hourly] | Walk full chain | Critical alert |
| Signature validity | [daily] | Verify all signatures since last check | Critical alert |
| Sequence gaps | [per event] | Check sequence_number continuity | Warning |
| Timestamp ordering | [per event] | Verify monotonic timestamps | Warning |
| Cross-agent consistency | [daily] | Compare shared events across agents | Warning |

---

## Retention Policy

| Regulatory Framework | Minimum Retention | This Agent's Policy |
|---------------------|-------------------|---------------------|
| **GDPR** | 3 years (data processing records; see GDPR.md and CONSENT.md for right-to-erasure interaction) | [duration] |
| **HIPAA** | 6 years (access logs, audit trails) | [duration] |
| **SOC 2** | 1 year (system activity logs) | [duration] |
| **EU AI Act** | 10 years (high-risk AI system logs) | [duration] |
| **PCI DSS** | 1 year (readily available) + archive | [duration] |
| **Internal policy** | [as defined by organization] | [duration] |

**Applied retention:** [longest applicable period]

### Storage Configuration
| Property | Value |
|----------|-------|
| **Primary storage** | [path, bucket, or database URI] |
| **Archive storage** | [cold storage location after active period] |
| **Encryption at rest** | [AES-256-GCM | ChaCha20-Poly1305 | none] |
| **Encryption key management** | [reference to SECRETS.md entry] |
| **Access controls** | [who can read: security team, auditors, compliance] |
| **Backup frequency** | [real-time replication | daily | weekly] |
| **Backup location** | [geographically separated backup target] |

### Deletion
Audit records are NEVER deleted before the retention period expires.
Deletion of expired records requires:
1. Verification that no active investigation references the records
2. Approval from [compliance officer or automated policy]
3. Cryptographic proof of deletion (deletion certificate)
4. Logging of the deletion event itself (meta-audit)

---

## Non-Repudiation Mechanism

Every audit entry is non-repudiable — the agent that produced it
cannot deny having produced it. This is achieved through:

1. **Cryptographic signing:** Each entry signed with the agent's
   ATTESTATION.md credentials (see ATTESTATION.md for key management
   and signing algorithms; private key never leaves hardware binding
   if applicable)
2. **Delegation chain inclusion:** Every entry includes the full
   chain of authority from human principal to executing agent
3. **Timestamping:** Independent timestamp from trusted authority
   prevents backdating
4. **Witness countersigning:** For high-stakes actions, a second
   agent or service countersigns the entry

Verification steps for any audit entry:
1. Validate signature against agent's attested public key
2. Verify delegation chain is unbroken to a human principal
3. Confirm timestamp from independent authority
4. Check hash chain integrity in both directions

---

## Human Authority Binding

Every consequential action links back to a human decision-maker
through the delegation chain (see DELEGATION.md for chain structure
and depth limits).

- **Delegation chain logged:** Every entry includes the full chain
- **Chain breaks:** If delegation chain cannot be verified, action
  is logged as "authority_unverified" and flagged for review
- **Human approval references:** Actions requiring human approval
  include the approval ID, approver identity, and approval timestamp
- **Chain depth limit:** Maximum [N] delegation hops before
  re-authorization from a human is required

---

## Query Interface

### API Endpoint
| Property | Value |
|----------|-------|
| **Endpoint** | `https://[domain]/api/v1/audit` |
| **Authentication** | [mTLS | Bearer token | SPIFFE] |
| **Authorization** | [RBAC roles: auditor, security, compliance, admin] |
| **Rate limit** | [requests per second by role] |

### Query Capabilities
- Filter by: agent_id, session_id, action_type, time_range,
  result, target_resource, classification, tags
- Full-text search across event metadata
- Delegation chain traversal (find all actions under a delegation)
- Aggregation: counts by action_type, error rates, cost totals

### Export Formats
| Format | Use Case |
|--------|----------|
| JSON Lines (.jsonl) | Machine processing, SIEM ingestion |
| CSV | Spreadsheet analysis, simple reporting |
| PDF (signed) | Regulatory submission, legal proceedings |
| OSCAL | NIST compliance reporting |

### Verification Tool
```bash
# Verify hash chain integrity
audit-verify --agent [agent-id] --from [date] --to [date]

# Verify specific event signature
audit-verify --event [event-id] --key [public-key-ref]

# Export for regulatory submission
audit-export --format pdf --signed --from [date] --to [date]
```

---

## Chain of Thought Ledger (Optional)

For agents that make consequential decisions, an optional structured
reasoning record preserves the "why" alongside the "what."

```yaml
decision:
  decision_id: "uuid-v4"
  linked_event_id: "uuid-v4"           # Audit event this explains
  decision_point: "description"         # What needed to be decided
  options_considered:
    - option: "Option A"
      pros: ["..."]
      cons: ["..."]
      estimated_outcome: "..."
    - option: "Option B"
      pros: ["..."]
      cons: ["..."]
      estimated_outcome: "..."
  selected: "Option A"
  confidence: 0.85                      # 0.0 to 1.0
  reasoning: "Free-text explanation of why this option was selected"
  constraints_applied:
    - "LIMITS.md: budget constraint"
    - "GUARDRAILS.md: scope check"
    - "POLICY.md: data handling rule"
  human_would_review: boolean           # Agent's self-assessment
  review_requested: boolean             # Whether review was actually requested
```

The Chain of Thought Ledger is:
- **Not a substitute** for the audit event — it supplements it
- **Stored separately** from the main audit trail if it contains
  sensitive reasoning
- **Subject to the same** tamper-resistance and retention policies
- **Queryable** for pattern analysis across decisions
````

## Example Use Cases

**Enterprise:** A multinational bank's trading agents produce hash-chained audit entries for every order execution, enabling the compliance team to reconstruct the full decision chain during regulatory examinations without relying on agent self-reporting.

**Multi-Agent Fleet:** A DevOps platform with 50 deployment agents uses AUDITTRAIL.md to correlate events across agents during post-incident forensics, tracing a cascading failure from the initial misconfigured deploy through every downstream agent that propagated the error.

**Regulated Industry:** A healthcare system's patient-data agents maintain signed, timestamped audit entries with delegation chains linking every data access back to the authorizing physician, satisfying HIPAA audit trail requirements and enabling 6-year retention compliance.

## Related Specs

| Spec | Relationship |
|------|-------------|
| DELEGATION.md | Authority chain and authorization |
| INTENT.md | Pre-action declaration and confidence scoring |
| WHOAMI.md | Agent identity declaration |
| ID.md | Permanent cryptographic identifier |
| SESSION.md | Ephemeral runtime identity and task scope |
| ATTESTATION.md | Identity verification and credential lifecycle |
| PROVENANCE.md | Data lineage and trust classification |
| PRIVACY.md | Data privacy handling |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
