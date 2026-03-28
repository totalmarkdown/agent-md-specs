---
spec_name: MEMORYSAFETY.md
spec_version: 0.1.0
category: Security
domain: memorysafetymd.dev
priority: Very High
volume: "Vol 15 — Shared Context & Memory Governance"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
---

# MEMORYSAFETY.md

**Category:** Security
**Domain:** memorysafetymd.dev
**Priority:** Very High
**Version:** 0.1.0

### Purpose
Defines defenses against memory poisoning, cross-session contamination, and unauthorized memory manipulation in both individual and shared agent memory. MEMORYSAFETY.md is the security complement to MEMORY.md (what to remember) and SHAREDCONTEXT.md (how to share) — it governs how memory is protected from adversarial and accidental corruption.

Agent memory is a high-value attack surface. Unlike prompt injection — which targets a single context window — memory poisoning persists across context resets, session boundaries, and agent restarts. A single poisoned entry can cascade through shared context to corrupt an entire fleet's reasoning.

Directly addresses OWASP ASI06 (Memory Poisoning), ASI04 (Cross-Agent Manipulation), ASI01 (Instruction Injection via memory), ASI03 (Unauthorized Resource Access), and ASI08 (Cascading Failures). Maps to Microsoft's "Memory Gateway" pattern and NIST SP 800-53 SI family (SI-3, SI-4, SI-7, SI-10).

### Scope Boundary
This spec governs **security of agent memory** — both individual and shared. SHAREDCONTEXT.md governs the structure and access rules of shared pools. MEMORY.md governs what individual agents remember. MEMORYSAFETY.md sits between them as a security layer.

### When to Create This File
Required for any agent with persistent memory or shared context access. Critical in multi-agent systems where one agent's memory entries influence another agent's decisions. If an agent remembers anything between sessions, or reads anything another agent wrote, it needs a MEMORYSAFETY.md.

### Spec

```markdown
---
agent_name: string
agent_id: string              # Must match WHOAMI.md agent_id
version: semver
memory_type: string           # individual | shared | both
write_gateway: string         # enabled | disabled
poisoning_detection: string   # active | passive | disabled
quarantine_mode: string       # auto | manual | disabled
session_isolation: string     # strict | permissive | none
integrity_method: string      # hash_chain | signed | checksum | none
last_integrity_check: date
last_updated: date
spec_version: string
---

# [Agent Name] — Memory Safety Configuration

## Threat Model

| Threat | Description | OWASP Ref |
|--------|-------------|-----------|
| **Memory Poisoning** | Attacker writes false or manipulative entries to agent memory, corrupting future reasoning | ASI06 |
| **Cross-Session Leakage** | Sensitive data bleeds between sessions through persistent memory | ASI06 |
| **Instruction Injection via Memory** | Instruction-like content embedded in memory entries is later interpreted as directives | ASI01 + ASI06 |
| **Unauthorized Memory Write** | Agent or external actor writes to memory without proper authorization | ASI03 |
| **Memory Staleness** | Outdated entries persist without expiry, causing decisions based on stale information | — |
| **Cascading Poisoning** | Poisoned entry propagates through shared context to multiple agents | ASI08 |

---

## Input Sanitization (Write Gateway)

Every entry written to memory MUST pass through the write gateway. No bypass.

| Step | Check | Action on Failure |
|------|-------|-------------------|
| **1. Schema validation** | Entry conforms to SHAREDCONTEXT.md schema (see SHAREDCONTEXT.md for the full memory schema definition): required fields, correct types, classification tag | Reject write, log |
| **2. Source authority** | Writing agent has valid ATTESTATION.md credentials, authorized per PERMISSIONS.md | Reject write, alert coordinator |
| **3. Delegation scope** | Write falls within delegated authority scope (see DELEGATION.md for scope checks before write) | Reject write, notify delegator |
| **4. Instruction detection** | Scan for instruction-like patterns ("ignore," "override," "you must," "act as") in data fields | Strip/quarantine instruction content, log |
| **5. Classification check** | Entry classification does not exceed writer's clearance per PERMISSIONS.md | Reject write, escalate per ESCALATION.md |
| **6. Confidence calibration** | Flag self-assessed confidence > 0.95 for review (per INTENT.md requirement) | Add `confidence_flagged: true`, allow with flag |
| **7. Size and rate limits** | Entry within [N] tokens, write rate within [N] per [time period] | Reject write, throttle agent |

---

## Poisoning Detection

Defense-in-depth detection of memory corruption beyond the write gateway.

### Canary Entries
| Canary Type | Implementation | Check Frequency |
|-------------|---------------|-----------------|
| **Static canaries** | Immutable known-true entries — any modification triggers alert | Every read cycle |
| **Behavioral canaries** | Entries producing predictable agent behavior — deviation indicates contamination | [Hourly] |
| **Hash canaries** | Entry hashes stored externally — mismatch indicates tampering | [Every N minutes] |
| **Contradiction canaries** | Entries that should never be contradicted — contradiction triggers review | Every write cycle |

### Consistency Checking
Compare new entries against existing entries for logical contradictions, temporal impossibilities, and source-level reversals. In multi-agent pools, entries contradicting majority consensus are flagged. Triggered on every write.

### Anomaly Detection
Monitor for write volume spikes (3x baseline), writes outside expected activity windows, significant content drift from an agent's typical patterns, and unusual bulk overwrite rates.
_See AUDITTRAIL.md for logging all suspicious entries flagged by anomaly detection._

### Source Reputation Weighting
| Level | Weight | Criteria |
|-------|--------|----------|
| **Verified** | 1.0 | Valid ATTESTATION.md, clean history, certified trust |
| **Established** | 0.8 | Valid credentials, no incidents in past [N] days |
| **New** | 0.5 | Recently provisioned, insufficient history |
| **Flagged** | 0.2 | Prior poisoning incidents or quarantine events |
| **Quarantined** | 0.0 | Under investigation — entries accepted but isolated |

### Temporal Analysis
Entries older than [N days] marked stale and require revalidation. Rapid write bursts flagged as potential automated poisoning. When a source agent is compromised, all entries since last known-good state flagged for retroactive review.

---

## Quarantine Procedures

When a suspicious entry is detected — by the write gateway, poisoning detection, or canary alert:

1. **Isolate** — Move entry to quarantine pool, tag with quarantine_id, detection_method, confidence_score. Exclude from agent decision-making. Prevent downstream propagation.
2. **Alert** — Notify pool coordinator and escalate to the team coordinator (see ESCALATION.md for severity levels and contact routing). Include entry_id, source_agent, detection_method, confidence_score, content_hash. Severity: >= 0.9 critical, >= 0.7 high, >= 0.5 medium, < 0.5 low.
3. **Trace** — Identify source agent via entry metadata and AUDITTRAIL.md. Trace delegation chain. Identify all entries from same source in same time window and all downstream reads.
4. **Assess** — Human or authorized coordinator reviews. Determine: poisoning_confirmed | false_positive | inconclusive.
5. **Resolve** — If false positive: restore entry, tune detection rules. If confirmed: rollback ALL entries from compromised source since last verified-clean checkpoint, revoke write access, notify all agents that read quarantined entries, re-derive dependent decisions.
6. **Report** — Log in AUDITTRAIL.md, update source reputation, feed patterns into anomaly detection baseline.

---

## Cross-Session Isolation

| Control | Implementation |
|---------|---------------|
| **Session-local memory** | Each session gets isolated memory namespace scoped to session ID (see SESSION.md for session isolation boundaries) |
| **Shared context default** | Read-only unless explicit write authorization per PERMISSIONS.md |
| **Session termination** | Session-local memory destroyed on session end — no residual state |
| **Cross-session reads** | Denied; data must be promoted to shared context to be visible |
| **Promotion gateway** | Promoting local memory to shared context requires full write gateway pipeline |
| **Multi-tenant isolation** | Shared context pools partitioned by tenant — no cross-tenant access |

---

## Memory Integrity Verification

### Hash Validation
SHA-256 per-entry hashes plus pool-level Merkle root. Hashes stored external to the memory pool. Verified on every read cycle for individual entries; full pool verification [hourly]. Hash mismatch triggers quarantine.

### Signed Entries
Each entry signed by writing agent's credential per ATTESTATION.md (see ATTESTATION.md for credential lifecycle and signing mechanics). Signature verified on every read; unsigned entries rejected. Each modification appends a new signature preserving full provenance chain. Expired signatures flagged for re-attestation.

### Hash-Chain Linking
Append-only hash chain where each entry includes the hash of its predecessor. Genesis entry hash stored in external integrity store. Missing links indicate deletion or tampering; multiple entries referencing the same predecessor indicate a fork (alert and reconcile). Full chain verification [daily]; incremental on every write.

---

## Classification Enforcement

Entries tagged with classification levels from SHAREDCONTEXT.md schema. Agents read only at or below their clearance from PERMISSIONS.md.

| Level | Access Requirement |
|-------|--------------------|
| **public** | Pool membership |
| **internal** | PERMISSIONS.md read authorization |
| **confidential** | PERMISSIONS.md explicit grant + ATTESTATION.md verification |
| **restricted** | PERMISSIONS.md explicit grant + human approval + audit |

**Rules:** Read-down only (never above clearance). Write-down prohibited (prevents declassification bypass). Combinatorial escalation: combining entries that produces higher-sensitivity information inherits the higher classification (per PROVENANCE.md aggregation pattern). Classification can only be raised, never lowered, except by human security reviewer. Derived entries inherit at least the source classification.

Attestation required for access above "internal." All access to confidential+ entries logged to AUDITTRAIL.md. Violations denied and alerted.
```

## Example Use Cases

**Enterprise:** A consulting firm uses MEMORYSAFETY.md canary entries in its research agent's shared context pool, detecting when a compromised data source injects false market data that contradicts known-true benchmark values before the bad data influences client reports.

**Multi-Agent Fleet:** A 200-agent fleet uses MEMORYSAFETY.md's write gateway and source reputation weighting to prevent a single newly provisioned agent (weight 0.5) from overwriting established facts in the shared context pool, requiring consensus from verified agents before high-confidence entries are modified.

**Regulated Industry:** A pharmaceutical company uses MEMORYSAFETY.md's classification enforcement to ensure agents processing restricted clinical trial data cannot write entries below their clearance level, preventing accidental declassification of patient outcomes data across the shared memory pool.

## Related Specs

| Spec | Relationship |
|------|-------------|
| SHAREDCONTEXT.md | Multi-agent shared memory pool |
| MEMORY.md | Individual agent memory governance |
| PROMPTSHIELD.md | Prompt injection defense |
| AUDITTRAIL.md | Tamper-proof action logging |
| ATTESTATION.md | Identity verification and credential lifecycle |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| SESSION.md | Ephemeral runtime identity and task scope |
| PROVENANCE.md | Data lineage and trust classification |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
