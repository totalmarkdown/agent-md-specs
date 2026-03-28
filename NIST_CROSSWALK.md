# NIST Crosswalk

Mapping of agent-md-specs to NIST AI Risk Management Framework (AI RMF 1.0)
and the NCCoE Concept Paper on AI Agent Identity and Authorization (Feb 2026).

---

## Implementation Model

agent-md-specs defines two types of specifications:

- **Static configuration** (e.g., WHOAMI.md, LIMITS.md, DELEGATION.md):
  committed to version control, define the agent's permanent identity
  and constraints.

- **Runtime schemas** (e.g., INTENT.md, SESSION.md, AUDITTRAIL.md):
  define the format and validation rules for ephemeral data generated
  during agent execution. These are not files overwritten on disk —
  they are schemas that runtime systems use to structure API payloads,
  session tokens, and audit log entries.

This distinction means agent-md-specs is a **declarative policy
specification** that compiles down into machine-enforceable rules,
not a file-based runtime system.

---

## NCCoE Concept Paper — Question-by-Question Mapping

### 1. Identification
> "How might agents be identified in an enterprise architecture?"
> "What metadata is essential for an AI agent's identity?"

| Spec | What It Provides |
|------|-----------------|
| [WHOAMI.md](specs/identity/WHOAMI.md) | Declarative identity document — name, version, capabilities, owner |
| [ID.md](specs/identity/ID.md) | Permanent UUID anchor — cryptographic, immutable identifier |
| [ATTESTATION.md](specs/security/ATTESTATION.md) | Identity verification — SPIFFE, X.509, DID, hardware/software binding |
| [SESSION.md](specs/lifecycle/SESSION.md) | Ephemeral task-scoped identity (answers "ephemeral vs fixed?" question) |
| [CONTACT.md](specs/identity/CONTACT.md) | Reachable endpoints — MCP, API, email, human owner |

### 2. Authentication
> "What constitutes a strong authentication for an AI agent?"
> "How do we handle key management for agents?"

| Spec | What It Provides |
|------|-----------------|
| [ATTESTATION.md](specs/security/ATTESTATION.md) | Authentication methods, key lifecycle (issuance, rotation, revocation) |
| [SECRETS.md](specs/security/SECRETS.md) | What secrets the agent needs (never the values themselves) |
| [SESSION.md](specs/lifecycle/SESSION.md) | Ephemeral session credentials, key generation and destruction |

### 3. Authorization
> "How can zero-trust principles be applied to agent authorization?"
> "How do we establish 'least privilege' for an agent?"
> "What are the mechanisms for an agent to prove its authority?"
> "How might an agent convey the intent of its actions?"
> "How do we handle delegation of authority for 'on behalf of' scenarios?"
> "How do we bind agent identity with human identity?"

| Spec | What It Provides |
|------|-----------------|
| [DELEGATION.md](specs/governance/DELEGATION.md) | On-behalf-of authority chains, human-agent binding, scope constraints |
| [LEASTPRIVILEGE.md](specs/governance/LEASTPRIVILEGE.md) | Zero-trust privilege management, JIT escalation, auto de-escalation |
| [PERMISSIONS.md](specs/governance/PERMISSIONS.md) | Static permission declarations |
| [ACCESS.md](specs/security/ACCESS.md) | Who/what can invoke this agent |
| [INTENT.md](specs/governance/INTENT.md) | Pre-action intent declaration with confidence levels |
| [LIMITS.md](specs/governance/LIMITS.md) | Hard stops — what the agent will never do regardless of delegation |
| [ESCALATION.md](specs/governance/ESCALATION.md) | Human-in-the-loop triggers and procedures |
| [BUDGET.md](specs/governance/BUDGET.md) | Financial authorization limits |
| [ENFORCEMENT.md](specs/governance/ENFORCEMENT.md) | How all authorization specs are verified at runtime |

### 4. Auditing and Non-Repudiation
> "How can we ensure that agents log their actions in a tamper-proof manner?"
> "How do we ensure non-repudiation for agent actions?"
> "How do we bind actions back to human authorization?"

| Spec | What It Provides |
|------|-----------------|
| [AUDITTRAIL.md](specs/compliance/AUDITTRAIL.md) | Tamper-proof action records, non-repudiation, compliance mapping |
| [INTENT.md](specs/governance/INTENT.md) | Intent-action cryptographic binding (proves agent did what it said) |
| [DELEGATION.md](specs/governance/DELEGATION.md) | Accountability chain linking actions to human authorization |
| [ENFORCEMENT.md](specs/governance/ENFORCEMENT.md) | Audit verification and tamper detection mechanisms |

### 5. Data Flow Tracking
> "Track and maintain provenance of user prompts and data input sources"

| Spec | What It Provides |
|------|-----------------|
| [PROVENANCE.md](specs/compliance/PROVENANCE.md) | Data lineage, input trust classification, aggregation sensitivity |
| [INPUT.md](specs/technical/INPUT.md) | What the agent accepts — formats, validation, size limits |
| [OUTPUT.md](specs/technical/OUTPUT.md) | What the agent produces — schemas, format guarantees |

### 6. Prompt Injection
> "What controls help prevent both direct and indirect prompt injections?"
> "After prompt injection occurs, what controls minimize the impact?"

| Spec | What It Provides |
|------|-----------------|
| [PROMPTSHIELD.md](specs/security/PROMPTSHIELD.md) | Injection prevention, detection, containment, recovery, testing |
| [GUARDRAILS.md](specs/governance/GUARDRAILS.md) | Runtime safety boundaries (general) |
| [LIMITS.md](specs/governance/LIMITS.md) | Hard stops that override all input including injected instructions |
| [ENFORCEMENT.md](specs/governance/ENFORCEMENT.md) | Runtime enforcement of injection defense specs |

### 7. Enforcement and Continuous Monitoring
> "How do we verify agents follow their own declarations?"
> Mapped to: NIST SP 800-207 Zero Trust Architecture — Policy
> Enforcement Points (PEPs) and Policy Decision Points (PDPs)

| Spec | Enforcement Role | ZTA Mapping |
|------|-----------------|-------------|
| [ENFORCEMENT.md](specs/governance/ENFORCEMENT.md) | Defines the verification framework — pre-deployment validation, runtime enforcement matrix, behavioral drift detection | Policy Decision Point (PDP) |
| [ATTESTATION.md](specs/security/ATTESTATION.md) | Provides cryptographic identity proof at runtime | Policy Information Point (PIP) |
| [AUDITTRAIL.md](specs/compliance/AUDITTRAIL.md) | Records all enforcement decisions for non-repudiation | Continuous Diagnostics and Mitigation (CDM) |
| [LEASTPRIVILEGE.md](specs/governance/LEASTPRIVILEGE.md) | Defines JIT privilege escalation requiring PDP approval | Dynamic access control per SP 800-207 S3 |
| [INTENT.md](specs/governance/INTENT.md) | Pre-action declaration evaluated against policy before execution | Implicit trust zone boundary |
| [SESSION.md](specs/lifecycle/SESSION.md) | Ephemeral credential scope prevents lateral movement | Microsegmentation boundary |

### 8. Shared Memory and Context Security
> Addresses OWASP ASI06 (Memory Poisoning) — recognized in the NIST CAISI AI Agent Security initiative
> and cited in the NIST CAISI RFI on AI Agent Security as
> "memory management vulnerabilities"

| Spec | What It Provides | Threat Addressed |
|------|-----------------|-----------------|
| [SHAREDCONTEXT.md](specs/coordination/SHAREDCONTEXT.md) | Governance framework for multi-agent shared memory — access control, schema, retention, inheritance across org hierarchy | Unauthorized memory access, context sprawl |
| [MEMORYSAFETY.md](specs/security/MEMORYSAFETY.md) | Defense against memory poisoning, cross-session contamination, and instruction injection via stored entries | OWASP ASI06, ASI04, ASI01 |
| [MEMORY.md](specs/cognitive/MEMORY.md) | Individual agent memory with scope declaration, shared context integration, and classification enforcement | Memory leakage, staleness, over-sharing |

---

## NIST AI Risk Management Framework (AI RMF 1.0) Mapping

### GOVERN (Policies, processes, procedures, and practices)

| AI RMF Subcategory | Spec(s) | Coverage |
|-------------------|---------|----------|
| GOVERN 1.1 — Legal and regulatory requirements | [EUAIACT.md](specs/regulatory/EUAIACT.md), [GDPR.md](specs/compliance/GDPR.md), [HIPAA.md](specs/regulatory/HIPAA.md), [CCPA.md](specs/regulatory/CCPA.md), [CONSENT.md](specs/compliance/CONSENT.md) | Full |
| GOVERN 1.2 — Trustworthy AI characteristics | [SOUL.md](specs/identity/SOUL.md), [LIMITS.md](specs/governance/LIMITS.md), [GUARDRAILS.md](specs/governance/GUARDRAILS.md) | Full |
| GOVERN 1.4 — Organizational practices | [ORG.md](specs/organizational/ORG.md), [POLICY.md](specs/governance/POLICY.md), [TEAM.md](specs/coordination/TEAM.md) | Full |
| GOVERN 1.5 — Risk management processes | [ESCALATION.md](specs/governance/ESCALATION.md), [ICE.md](specs/governance/ICE.md), [RISKS.md](specs/operations/RISKS.md) | Full |
| GOVERN 2.1 — Roles and responsibilities | [DELEGATION.md](specs/governance/DELEGATION.md), [REPORTSTO.md](specs/organizational/REPORTSTO.md), [PERMISSIONS.md](specs/governance/PERMISSIONS.md) | Full |
| GOVERN 2.2 — Workforce diversity and skills | [CREW.md](specs/coordination/CREW.md), [TEAM.md](specs/coordination/TEAM.md), [EXPERTISE.md](specs/cognitive/EXPERTISE.md) | Partial |
| GOVERN 4.1 — Organizational practices | [AUDITTRAIL.md](specs/compliance/AUDITTRAIL.md), [MONITOR.md](specs/operations/MONITOR.md), [ENFORCEMENT.md](specs/governance/ENFORCEMENT.md) | Full |
| GOVERN 5.1 — Feedback mechanisms | [FEEDBACK.md](specs/quality/FEEDBACK.md), [ESCALATION.md](specs/governance/ESCALATION.md) | Full |
| GOVERN 6.1 — Decommissioning policies | [LEGACY.md](specs/lifecycle/LEGACY.md), [SESSION.md](specs/lifecycle/SESSION.md) | Full |

### MAP (Contextualize AI risks)

| AI RMF Subcategory | Spec(s) | Coverage |
|-------------------|---------|----------|
| MAP 1.1 — Intended purpose | [SOUL.md](specs/identity/SOUL.md), [GOALS.md](specs/process/GOALS.md), [CHARTER.md](specs/organizational/CHARTER.md) | Full |
| MAP 1.5 — Organizational risk tolerance | [LIMITS.md](specs/governance/LIMITS.md), [BUDGET.md](specs/governance/BUDGET.md), [LEASTPRIVILEGE.md](specs/governance/LEASTPRIVILEGE.md) | Full |
| MAP 2.1 — Scientific integrity | [VALIDATION.md](specs/quality/VALIDATION.md), [PROVENANCE.md](specs/compliance/PROVENANCE.md) | Full |
| MAP 2.3 — AI system categorization | [WHOAMI.md](specs/identity/WHOAMI.md), [MODEL.md](specs/technical/MODEL.md), [EUAIACT.md](specs/regulatory/EUAIACT.md) | Full |
| MAP 3.4 — Risks of third-party components | [DEPENDENCIES.md](specs/technical/DEPENDENCIES.md), [TOOLS.md](specs/technical/TOOLS.md), [PROVENANCE.md](specs/compliance/PROVENANCE.md) | Full |
| MAP 5.1 — Impacts to individuals | [PII.md](specs/compliance/PII.md), [PRIVACY.md](specs/compliance/PRIVACY.md), [CENSOR.md](specs/governance/CENSOR.md) | Full |

### MEASURE (Assess, analyze, and track AI risks)

| AI RMF Subcategory | Spec(s) | Coverage |
|-------------------|---------|----------|
| MEASURE 1.1 — Risk metrics | [KPI.md](specs/quality/KPI.md), [PERFORMANCE.md](specs/quality/PERFORMANCE.md), [TESTSCORES.md](specs/quality/TESTSCORES.md) | Full |
| MEASURE 2.5 — Evaluation of computational bias | [EVAL.md](specs/quality/EVAL.md), [VALIDATION.md](specs/quality/VALIDATION.md) | Partial |
| MEASURE 2.6 — Assessment of computational robustness | [PROMPTSHIELD.md](specs/security/PROMPTSHIELD.md), [GUARDRAILS.md](specs/governance/GUARDRAILS.md) | Full |
| MEASURE 4.1 — Measurement approaches | [MONITOR.md](specs/operations/MONITOR.md), [HEALTHCHECK.md](specs/operations/HEALTHCHECK.md), [AUDITTRAIL.md](specs/compliance/AUDITTRAIL.md) | Full |

### MANAGE (Manage AI risks)

| AI RMF Subcategory | Spec(s) | Coverage |
|-------------------|---------|----------|
| MANAGE 1.1 — Risk response | [ESCALATION.md](specs/governance/ESCALATION.md), [ICE.md](specs/governance/ICE.md), [PANIC.md](specs/governance/PANIC.md) | Full |
| MANAGE 1.3 — Risk response actions | [GUARDRAILS.md](specs/governance/GUARDRAILS.md), [PROMPTSHIELD.md](specs/security/PROMPTSHIELD.md), [LIMITS.md](specs/governance/LIMITS.md) | Full |
| MANAGE 2.1 — Resources for risk management | [BUDGET.md](specs/governance/BUDGET.md), [SECRETS.md](specs/security/SECRETS.md), [VAULT.md](specs/security/VAULT.md) | Full |
| MANAGE 2.2 — Contingency processes | [ICE.md](specs/governance/ICE.md), [REBOOT.md](specs/lifecycle/REBOOT.md), [REPAIR.md](specs/operations/REPAIR.md), [CIRCUITBREAKER.md](specs/operations/CIRCUITBREAKER.md) | Full |
| MANAGE 3.1 — Pre-deployment testing | [TESTING.md](specs/quality/TESTING.md), [TESTSCORES.md](specs/quality/TESTSCORES.md), [EVAL.md](specs/quality/EVAL.md) | Full |
| MANAGE 3.2 — Pre-deployment verification | [ENFORCEMENT.md](specs/governance/ENFORCEMENT.md) (pre-deployment validation) | Full |
| MANAGE 4.1 — Post-deployment monitoring | [MONITOR.md](specs/operations/MONITOR.md), [HEALTHCHECK.md](specs/operations/HEALTHCHECK.md), [HEARTBEAT.md](specs/operations/HEARTBEAT.md), [ENFORCEMENT.md](specs/governance/ENFORCEMENT.md) | Full |
| MANAGE 4.2 — Incident response | [ESCALATION.md](specs/governance/ESCALATION.md), [AUDITTRAIL.md](specs/compliance/AUDITTRAIL.md), [ICE.md](specs/governance/ICE.md), [CIRCUITBREAKER.md](specs/operations/CIRCUITBREAKER.md) | Full |

---

## Relevant NIST Publications Referenced

| Publication | How agent-md-specs Aligns |
|-------------|--------------------------|
| SP 800-207 Zero Trust Architecture | [LEASTPRIVILEGE.md](specs/governance/LEASTPRIVILEGE.md), [ATTESTATION.md](specs/security/ATTESTATION.md), [ENFORCEMENT.md](specs/governance/ENFORCEMENT.md) |
| SP 800-63-4 Digital Identity Guidelines | [WHOAMI.md](specs/identity/WHOAMI.md), [ID.md](specs/identity/ID.md), [ATTESTATION.md](specs/security/ATTESTATION.md) |
| NISTIR 8587 Token Protection | [SESSION.md](specs/lifecycle/SESSION.md), [ATTESTATION.md](specs/security/ATTESTATION.md), [SECRETS.md](specs/security/SECRETS.md) |
| AI RMF 1.0 (AI 100-1) | Full crosswalk above |
| NCCoE Concept Paper (Feb 2026) | Full question mapping above |

---

## The Accountability Chain

These specs together create a complete, auditable chain
from human authorization to tamper-proof record:

| Step | Spec | Question Answered |
|------|------|-------------------|
| 1 | [DELEGATION.md](specs/governance/DELEGATION.md) | Who authorized this agent? |
| 2 | [CONSENT.md](specs/compliance/CONSENT.md) | Did the end user give permission? |
| 3 | [WHOAMI.md](specs/identity/WHOAMI.md) + [ID.md](specs/identity/ID.md) | Who is this agent? |
| 4 | [ATTESTATION.md](specs/security/ATTESTATION.md) | Can it prove its identity? |
| 5 | [SESSION.md](specs/lifecycle/SESSION.md) | What is its current runtime scope? |
| 6 | [LEASTPRIVILEGE.md](specs/governance/LEASTPRIVILEGE.md) | What is it allowed to do right now? |
| 7 | [INTENT.md](specs/governance/INTENT.md) | What does it intend to do? |
| 8 | [PROMPTSHIELD.md](specs/security/PROMPTSHIELD.md) | Is the input safe to act on? |
| 9 | [PROVENANCE.md](specs/compliance/PROVENANCE.md) | Where did the data come from? |
| 10 | [SHAREDCONTEXT.md](specs/coordination/SHAREDCONTEXT.md) | Is the shared memory trustworthy? |
| 11 | [MEMORYSAFETY.md](specs/security/MEMORYSAFETY.md) | Has the memory been poisoned? |
| | **[ACTION TAKEN]** | |
| 12 | [CIRCUITBREAKER.md](specs/operations/CIRCUITBREAKER.md) | Did something fail? Contain the blast radius. |
| 13 | [AUDITTRAIL.md](specs/compliance/AUDITTRAIL.md) | What happened, provably? |
| 14 | [ENFORCEMENT.md](specs/governance/ENFORCEMENT.md) | Can we verify all of the above? |
| 15 | [ESCALATION.md](specs/governance/ESCALATION.md) | Should a human review this? |

---

## End-to-End: How agent-md-specs Satisfies the NCCoE Model

The following walkthrough shows how the accountability chain operates
in practice, using the Atlas financial agent example
(examples/nist-nccoe-bundle/).

**1. Authority Establishment (Pre-Deployment)**
CFO Sarah Chen delegates financial analysis authority to Atlas
(DELEGATION.md). Scope: read-only access to financial databases,
report generation only. Expires quarterly. No sub-delegation.
Employee consent on file covers AI-assisted analysis (CONSENT.md).

**2. Identity Verification (Runtime — Continuous)**
Atlas declares its identity (WHOAMI.md, ID.md) and proves it
cryptographically via SPIFFE workload identity with X.509 certificate
issued by Acme Corp Internal CA (ATTESTATION.md). The runtime
environment verifies the certificate before allowing any action.

**3. Session Binding (Runtime — Per Task)**
A 30-minute session is created (SESSION.md) with ephemeral
credentials. Maximum 50 actions. In-memory only — no persistent
credentials. Session inherits delegation scope and cannot exceed it.

**4. Authorization Evaluation (Runtime — Per Action)**
Before each action, Atlas declares intent: "Read Q3 revenue data
from the financial database" with confidence 0.92 (INTENT.md).
The policy engine evaluates this against the active privilege set
(LEASTPRIVILEGE.md). Action is within baseline — no escalation needed.

**5. Input Safety Check (Runtime — Per Input)**
The query and retrieved data are scanned for injection patterns,
SQL injection attempts, and financial-domain canary tokens
(PROMPTSHIELD.md). Data sources classified by trust level
(PROVENANCE.md). All inputs pass.

**6. Memory Integrity (Runtime)**
Atlas reads from the Finance Team shared context pool
(SHAREDCONTEXT.md). The memory gateway validates entries and checks
canary entries (MEMORYSAFETY.md). No poisoning detected.

**7. Action Execution**
Atlas generates the Q3 financial report.

**8. Failure Containment (On-Failure)**
If the Bloomberg API returns 3 consecutive errors, Atlas's circuit
breaker opens (CIRCUITBREAKER.md). Atlas halts individually. The
Finance Team continues with degraded capability. Cached reports
served with staleness warnings.

**9. Audit Record (Post-Action)**
The action is recorded as a tamper-proof hash-chain entry
(AUDITTRAIL.md), signed with Atlas's X.509 certificate. Entry
includes: delegation reference, intent hash, I/O hashes, session ID,
timestamp. Retention: 7 years per SOX compliance.

**10. Enforcement Verification (Continuous)**
The enforcement layer verifies the action matched declared intent,
stayed within delegation scope, and violated no LIMITS.md constraints
(ENFORCEMENT.md). No drift detected.

**11. Human Review (On-Trigger)**
If Atlas attempts an action outside declared intent — for example,
sending an email (requires JIT escalation) — ENFORCEMENT.md blocks
it, AUDITTRAIL.md records the violation, and ESCALATION.md notifies
the CFO and compliance team.

This walkthrough demonstrates a complete, verifiable chain from human
delegation to tamper-proof record, implemented through infrastructure-
level policy enforcement points — not on-agent self-policing.

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
