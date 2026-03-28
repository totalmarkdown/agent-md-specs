# NIST NCCoE Reviewer Guide

A guided tour of agent-md-specs for reviewers evaluating this
submission in response to the NCCoE concept paper "Accelerating
the Adoption of Software and AI Agent Identity and Authorization."

---

## Start Here (5 Minutes)

1. **[NIST_CROSSWALK.md](NIST_CROSSWALK.md)** — Direct mapping of
   our specs to the 6 question areas in the concept paper, plus
   the NIST AI Risk Management Framework (Govern, Map, Measure, Manage).

2. **[The Accountability Chain](#see-it-in-practice-10-minutes)** in
   the README — Our 14-step verification chain from human delegation
   to tamper-proof audit trail, mapped to SP 800-207 Zero Trust
   Architecture components (PEP/PDP/PIP).

---

## The 20 Specs That Answer Your Questions (15 Minutes)

Each spec below maps to a specific question from pages 3-4 of the
concept paper. Links go directly to the spec files.

### Question 1: Identification
*"How might agents be identified? What metadata is essential?"*

- [WHOAMI.md](specs/identity/WHOAMI.md) — Declarative identity document
- [ID.md](specs/identity/ID.md) — Permanent cryptographic UUID
- [ATTESTATION.md](specs/security/ATTESTATION.md) — Identity proof
  via SPIFFE/SPIRE, X.509, DID — with hardware/software binding
- [SESSION.md](specs/lifecycle/SESSION.md) — Ephemeral task-scoped
  identity (answers your "ephemeral vs fixed?" question)

### Question 2: Authentication
*"What constitutes strong authentication? Key management?"*

- [ATTESTATION.md](specs/security/ATTESTATION.md) — Complete
  credential lifecycle: issuance, rotation, revocation, recovery.
  References SP 800-63-4 and SPIFFE/SPIRE.

### Question 3: Authorization
*"Zero-trust? Least privilege? Delegation? Intent?"*

- [DELEGATION.md](specs/governance/DELEGATION.md) — Authority chain
  from human to agent with OAuth 2.0 OBO mapping
- [LEASTPRIVILEGE.md](specs/governance/LEASTPRIVILEGE.md) — Dynamic
  zero-trust privileges per SP 800-207
- [INTENT.md](specs/governance/INTENT.md) — Pre-action intent
  declaration (answers your novel question about conveying intent)
- [CONSENT.md](specs/compliance/CONSENT.md) — End-user permission
  lifecycle (GDPR Article 7, CCPA, EU AI Act Article 13)
- [PERMISSIONS.md](specs/governance/PERMISSIONS.md) — Static resource
  access control
- [LIMITS.md](specs/governance/LIMITS.md) — Hard stops
- [ESCALATION.md](specs/governance/ESCALATION.md) — Human-in-the-loop

### Question 4: Auditing and Non-Repudiation
*"Tamper-proof logging? Non-repudiation? Binding to human authority?"*

- [AUDITTRAIL.md](specs/compliance/AUDITTRAIL.md) — Hash-chain
  audit records with cryptographic signing and compliance retention
  mappings (GDPR, HIPAA, SOC2, EU AI Act)

### Question 5: Data Flow Tracking
*"Provenance of prompts and data input sources?"*

- [PROVENANCE.md](specs/compliance/PROVENANCE.md) — Input source
  registries, trust classification, transformation logs, and data
  classification escalation on aggregation

### Question 6: Prompt Injection
*"Prevention and mitigation controls?"*

- [PROMPTSHIELD.md](specs/security/PROMPTSHIELD.md) — Defense-in-depth
  covering direct/indirect injection, canary tokens, containment,
  recovery, and red team testing

### Cross-Cutting: Memory Security
*Addresses OWASP ASI06 (Memory Poisoning) — recognized by NIST CAISI*

- [SHAREDCONTEXT.md](specs/coordination/SHAREDCONTEXT.md) — Multi-agent
  shared memory governance
- [MEMORYSAFETY.md](specs/security/MEMORYSAFETY.md) — Memory poisoning
  defense and integrity verification

### Cross-Cutting: Failure Containment
*Addresses OWASP ASI08 (Cascading Failures) — recognized by NIST CAISI*

- [CIRCUITBREAKER.md](specs/operations/CIRCUITBREAKER.md) — Blast
  radius limits, retry policies, cascading prevention

### Cross-Cutting: Enforcement
*"How do we verify agents follow their own declarations?"*

- [ENFORCEMENT.md](specs/governance/ENFORCEMENT.md) — Pre-deployment
  validation, runtime monitoring, behavioral drift detection, and
  post-hoc audit verification. Defines where enforcement occurs
  (external policy enforcement points, not on-agent self-policing).

---

## See It in Practice (10 Minutes)

**[examples/nist-nccoe-bundle/](examples/nist-nccoe-bundle/)** —
A complete enterprise financial agent ("Atlas" at Acme Corp) configured
with all 20 specs above. Shows realistic delegation from a CFO,
SPIFFE workload identity, 30-minute session boundaries, hash-chain
audit trails with 7-year SOX retention, and prompt injection defenses
with financial-domain canary tokens.

---

## How It Works Architecturally

**Static specs** (WHOAMI.md, LIMITS.md, DELEGATION.md) are committed
to version control — they define the agent's permanent configuration.

**Runtime schema specs** (INTENT.md, SESSION.md, AUDITTRAIL.md)
define the format for API payloads, session tokens, and audit entries
generated at runtime. They are not files overwritten on disk — they
are schemas consumed by policy engines, API gateways, and logging
infrastructure.

This means agent-md-specs is a **declarative policy specification**
that compiles into machine-enforceable rules, not a file-based
runtime system.

### From Markdown to Runtime

Every spec file contains YAML frontmatter — structured, typed,
schema-validated metadata — inside a Markdown document. This means
the same file serves as both the human-readable policy (the Markdown
body, auditable by compliance officers) and the machine-consumable
configuration (the YAML frontmatter, parseable by any standard YAML
library in three lines of code). JSON Schema definitions for all
Core specs enable automated conformance validation. No special
compiler or translation layer is required — the policies humans
approve are identical to the data machines enforce.

---

## Validation Tooling

- **[agent-md-validator](https://github.com/totalmarkdown/agent-md-validator)**
  — CLI tool validating frontmatter, required sections, and cross-references
- **[schemas/](schemas/)** — JSON Schema definitions for all Core specs,
  enabling automated conformance validation

---

## Standards Alignment

| Referenced Standard | How We Align |
|--------------------|-------------|
| SP 800-207 Zero Trust | Accountability chain maps to PEP/PDP/PIP |
| SP 800-63-4 Digital Identity | WHOAMI.md + ATTESTATION.md |
| SPIFFE/SPIRE | ATTESTATION.md primary verification method |
| OAuth 2.0 / OIDC | DELEGATION.md maps to OBO token exchange |
| NGAC | LEASTPRIVILEGE.md defines dynamic policies |
| MCP (AAIF) | agent-md-specs governs MCP connections |
| AGENTS.md (AAIF) | Complementary — we add identity/governance |
| OWASP Agentic Top 10 | ASI06 → MEMORYSAFETY, ASI08 → CIRCUITBREAKER |

---

## Key Design Decisions

- **CC0 Public Domain** — zero licensing friction for government adoption
- **Markdown format** — human-readable for compliance officers, machine-parseable via YAML frontmatter and JSON Schema
- **46 Core + 132 Extended** — tiered for progressive adoption
- **External enforcement** — specs define policy, runtime systems enforce it (not on-agent self-policing)

---

## Contact

For questions about this submission or to discuss participation in
future NCCoE workshops or demonstration projects:

**TotalMarkdown.ai**
Email: totalmarkdown@gmail.com
Repository: https://github.com/totalmarkdown/agent-md-specs
Discussions: https://github.com/totalmarkdown/agent-md-specs/discussions

---

*Submitted in response to NCCoE concept paper "Accelerating the
Adoption of Software and AI Agent Identity and Authorization"
(February 2026). CC0 1.0 Universal — Public Domain.*
