---
spec_name: "ENFORCEMENT.md"
spec_version: "1.0.0"
category: "Governance"
tier: core
priority: High
agent_name: "Atlas"
version: "2.1.0"
org: "Acme Corp"
enforcement_model: "layered"
ci_validator: "agent-md-validator v1.2.0"
drift_detection: "continuous"
created: "2025-11-01"
updated: "2026-03-15"
---

# Atlas -- Enforcement

## Enforcement Model

Atlas's policies are enforced across three layers: pre-deployment validation,
runtime enforcement, and continuous audit verification. Each layer operates
independently so that a failure in one layer does not compromise the others.

## Pre-Deployment Enforcement

### CI/CD Validation

Before any Atlas deployment reaches production, the agent-md-validator tool
runs as a mandatory CI/CD pipeline step.

- **Tool:** agent-md-validator v1.2.0
- **Pipeline:** Acme GitLab CI, `finance-agents` project
- **Stage:** `validate-agent-specs` (runs before container build)
- **Blocking:** Pipeline fails if validation fails; no manual override

### Validation Checks

| Spec | Check | Severity |
|------|-------|----------|
| WHOAMI.md | Agent ID matches registry, SPIFFE ID valid format | Critical |
| SOUL.md | Required sections present (Personality, Values, Ethical Boundaries) | Critical |
| DELEGATION.md | Delegator identity verified against HR directory, expiration date in future | Critical |
| ATTESTATION.md | Certificate chain valid, key rotation within policy | Critical |
| LIMITS.md | All hard stops present and unmodified from approved baseline | Critical |
| PERMISSIONS.md | Permissions subset of delegation scope, no denied resources in grants | Critical |
| SESSION.md | TTL within policy bounds, memory wipe configured | High |
| LEASTPRIVILEGE.md | Baseline privileges subset of PERMISSIONS.md grants | High |
| INTENT.md | Approval-required actions list matches LEASTPRIVILEGE.md JIT actions | High |
| PROMPTSHIELD.md | Red team date within 60 days, pattern library version current | Medium |
| PROVENANCE.md | All source endpoints resolvable, trust levels assigned | Medium |
| AUDITTRAIL.md | Retention period meets regulatory minimum (7 years) | Critical |
| ESCALATION.md | All levels defined, contacts valid, SLAs specified | High |
| ENFORCEMENT.md | Self-referential integrity check passes | Medium |

### Spec Integrity

- All spec files are signed with the Engineering Lead's GPG key
- SHA-256 hashes of all specs are stored in the deployment manifest
- Any modification to a spec file between validation and deployment triggers
  a pipeline failure

## Runtime Enforcement

### LIMITS Enforcement

- **Mechanism:** Blocklist evaluator runs before every Atlas action
- **Implementation:** Sidecar container (`limits-enforcer`) intercepts all
  Atlas actions via service mesh (Istio)
- **Hard stops:** Evaluated against a compiled blocklist derived from LIMITS.md
  at deployment time
- **Violation response:** Action blocked, session terminated, L4 escalation

### PERMISSIONS Enforcement

- **Mechanism:** IAM policy sync
- **Implementation:** PERMISSIONS.md is compiled into Acme IAM policies at
  deployment time. IAM policies are the authoritative enforcement point;
  PERMISSIONS.md is the human-readable source of truth.
- **Sync validation:** IAM policy hash compared against PERMISSIONS.md hash
  hourly. Drift triggers alert and automatic re-sync.
- **Network enforcement:** Kubernetes NetworkPolicy restricts Atlas pod
  egress to only permitted endpoints listed in PERMISSIONS.md

### LEASTPRIVILEGE Enforcement

- **Mechanism:** JIT privilege broker
- **Implementation:** `privilege-broker` service manages JIT escalation
  requests. Atlas submits escalation request; broker verifies approval
  via compliance portal API; broker grants temporary credential; broker
  revokes credential after use or timeout.
- **Credential type:** Short-lived OAuth 2.0 tokens (5-minute TTL)
- **Audit:** All escalation requests, grants, uses, and revocations logged

### PROMPTSHIELD Enforcement

- **Mechanism:** Input scanner
- **Implementation:** All inputs to Atlas pass through `prompt-scanner`
  sidecar before reaching the agent. Scanner applies pattern matching,
  boundary validation, and encoding detection.
- **Pattern updates:** Monthly, aligned with red team cycle
- **Bypass:** Not possible. Scanner is inline, not advisory.

### SESSION Enforcement

- **Mechanism:** Session manager with hardware timer
- **Implementation:** `session-manager` sidecar tracks session duration
  and action count. Enforces TTL via container kill after timeout.
  Action counter enforced at the service mesh level.
- **Clock source:** NTP-synchronized hardware clock, not application timer

## Drift Detection

Continuous monitoring detects drift between deployed configuration and
spec-defined policies.

### Monitored Signals

| Signal | Check Frequency | Alert Threshold |
|--------|----------------|-----------------|
| IAM policy vs PERMISSIONS.md hash | Hourly | Any mismatch |
| Network policy vs permitted endpoints | Hourly | Any mismatch |
| Container image hash vs ATTESTATION.md | On pod restart | Any mismatch |
| Blocklist version vs LIMITS.md hash | Hourly | Any mismatch |
| Certificate expiration | Daily | < 14 days remaining |
| Delegation expiration | Daily | < 7 days remaining |

### Drift Response

1. Alert sent to compliance-drift.acme.corp webhook
2. Engineering on-call notified via PagerDuty
3. Automatic re-sync attempted for IAM and network policies
4. If re-sync fails or drift is in critical spec: Atlas sessions suspended
   pending manual review

## Audit Verification

### Hash Chain Verification

- **Frequency:** Hourly automated verification of full audit chain
- **Verifier:** Independent service (`audit-verifier`) with read-only access
  to audit log storage
- **Alert:** Chain break triggers immediate compliance notification

### External Anchor

- **Endpoint:** transparency.acme.corp
- **Frequency:** Daily publication of chain head hash
- **Purpose:** Independent timestamp anchor prevents backdating of audit entries
- **Verification:** External auditors can verify chain integrity against
  published anchors during SOC2 and SOX audits
