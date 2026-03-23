# NIST Crosswalk

Mapping of agent-md-specs to NIST AI Risk Management Framework (AI RMF 1.0)
and the NCCoE Concept Paper on AI Agent Identity and Authorization (Feb 2026).

---

## NCCoE Concept Paper — Question-by-Question Mapping

### 1. Identification
> "How might agents be identified in an enterprise architecture?"
> "What metadata is essential for an AI agent's identity?"

| Spec | What It Provides |
|------|-----------------|
| WHOAMI.md | Declarative identity document — name, version, capabilities, owner |
| ID.md | Permanent UUID anchor — cryptographic, immutable identifier |
| ATTESTATION.md | Identity verification — SPIFFE, X.509, DID, hardware/software binding |
| SESSION.md | Ephemeral task-scoped identity (answers "ephemeral vs fixed?" question) |
| CONTACT.md | Reachable endpoints — MCP, API, email, human owner |

### 2. Authentication
> "What constitutes a strong authentication for an AI agent?"
> "How do we handle key management for agents?"

| Spec | What It Provides |
|------|-----------------|
| ATTESTATION.md | Authentication methods, key lifecycle (issuance, rotation, revocation) |
| SECRETS.md | What secrets the agent needs (never the values themselves) |
| SESSION.md | Ephemeral session credentials, key generation and destruction |

### 3. Authorization
> "How can zero-trust principles be applied to agent authorization?"
> "How do we establish 'least privilege' for an agent?"
> "What are the mechanisms for an agent to prove its authority?"
> "How might an agent convey the intent of its actions?"
> "How do we handle delegation of authority for 'on behalf of' scenarios?"
> "How do we bind agent identity with human identity?"

| Spec | What It Provides |
|------|-----------------|
| DELEGATION.md | On-behalf-of authority chains, human-agent binding, scope constraints |
| LEASTPRIVILEGE.md | Zero-trust privilege management, JIT escalation, auto de-escalation |
| PERMISSIONS.md | Static permission declarations |
| ACCESS.md | Who/what can invoke this agent |
| INTENT.md | Pre-action intent declaration with confidence levels |
| LIMITS.md | Hard stops — what the agent will never do regardless of delegation |
| ESCALATION.md | Human-in-the-loop triggers and procedures |
| BUDGET.md | Financial authorization limits |
| ENFORCEMENT.md | How all authorization specs are verified at runtime |

### 4. Auditing and Non-Repudiation
> "How can we ensure that agents log their actions in a tamper-proof manner?"
> "How do we ensure non-repudiation for agent actions?"
> "How do we bind actions back to human authorization?"

| Spec | What It Provides |
|------|-----------------|
| AUDITTRAIL.md | Tamper-proof action records, non-repudiation, compliance mapping |
| INTENT.md | Intent-action cryptographic binding (proves agent did what it said) |
| DELEGATION.md | Accountability chain linking actions to human authorization |
| ENFORCEMENT.md | Audit verification and tamper detection mechanisms |

### 5. Data Flow Tracking
> "Track and maintain provenance of user prompts and data input sources"

| Spec | What It Provides |
|------|-----------------|
| PROVENANCE.md | Data lineage, input trust classification, aggregation sensitivity |
| INPUT.md | What the agent accepts — formats, validation, size limits |
| OUTPUT.md | What the agent produces — schemas, format guarantees |

### 6. Prompt Injection
> "What controls help prevent both direct and indirect prompt injections?"
> "After prompt injection occurs, what controls minimize the impact?"

| Spec | What It Provides |
|------|-----------------|
| PROMPTSHIELD.md | Injection prevention, detection, containment, recovery, testing |
| GUARDRAILS.md | Runtime safety boundaries (general) |
| LIMITS.md | Hard stops that override all input including injected instructions |
| ENFORCEMENT.md | Runtime enforcement of injection defense specs |

### 7. Enforcement (Cross-Cutting)
> Implicit across all NIST questions: "How do we verify agents follow their own declarations?"

| Spec | What It Provides |
|------|-----------------|
| ENFORCEMENT.md | Pre-deployment validation, runtime monitoring, behavioral drift detection, audit verification, compliance attestation reports |

---

## NIST AI Risk Management Framework (AI RMF 1.0) Mapping

### GOVERN (Policies, processes, procedures, and practices)

| AI RMF Subcategory | Spec(s) | Coverage |
|-------------------|---------|----------|
| GOVERN 1.1 — Legal and regulatory requirements | EUAIACT.md, GDPR.md, HIPAA.md, CCPA.md | Full |
| GOVERN 1.2 — Trustworthy AI characteristics | SOUL.md, LIMITS.md, GUARDRAILS.md | Full |
| GOVERN 1.4 — Organizational practices | ORG.md, POLICY.md, TEAM.md | Full |
| GOVERN 1.5 — Risk management processes | ESCALATION.md, ICE.md, RISKS.md | Full |
| GOVERN 2.1 — Roles and responsibilities | DELEGATION.md, REPORTSTO.md, PERMISSIONS.md | Full |
| GOVERN 2.2 — Workforce diversity and skills | CREW.md, TEAM.md, EXPERTISE.md | Partial |
| GOVERN 4.1 — Organizational practices | AUDITTRAIL.md, MONITOR.md, ENFORCEMENT.md | Full |
| GOVERN 5.1 — Feedback mechanisms | FEEDBACK.md, ESCALATION.md | Full |
| GOVERN 6.1 — Decommissioning policies | LEGACY.md, SESSION.md | Full |

### MAP (Contextualize AI risks)

| AI RMF Subcategory | Spec(s) | Coverage |
|-------------------|---------|----------|
| MAP 1.1 — Intended purpose | SOUL.md, GOALS.md, CHARTER.md | Full |
| MAP 1.5 — Organizational risk tolerance | LIMITS.md, BUDGET.md, LEASTPRIVILEGE.md | Full |
| MAP 2.1 — Scientific integrity | VALIDATION.md, PROVENANCE.md | Full |
| MAP 2.3 — AI system categorization | WHOAMI.md, MODEL.md, EUAIACT.md | Full |
| MAP 3.4 — Risks of third-party components | DEPENDENCIES.md, TOOLS.md, PROVENANCE.md | Full |
| MAP 5.1 — Impacts to individuals | PII.md, PRIVACY.md, CENSOR.md | Full |

### MEASURE (Assess, analyze, and track AI risks)

| AI RMF Subcategory | Spec(s) | Coverage |
|-------------------|---------|----------|
| MEASURE 1.1 — Risk metrics | KPI.md, PERFORMANCE.md, TESTSCORES.md | Full |
| MEASURE 2.5 — Evaluation of computational bias | EVAL.md, VALIDATION.md | Partial |
| MEASURE 2.6 — Assessment of computational robustness | PROMPTSHIELD.md, GUARDRAILS.md | Full |
| MEASURE 4.1 — Measurement approaches | MONITOR.md, HEALTHCHECK.md, AUDITTRAIL.md | Full |

### MANAGE (Manage AI risks)

| AI RMF Subcategory | Spec(s) | Coverage |
|-------------------|---------|----------|
| MANAGE 1.1 — Risk response | ESCALATION.md, ICE.md, PANIC.md | Full |
| MANAGE 1.3 — Risk response actions | GUARDRAILS.md, PROMPTSHIELD.md, LIMITS.md | Full |
| MANAGE 2.1 — Resources for risk management | BUDGET.md, SECRETS.md, VAULT.md | Full |
| MANAGE 2.2 — Contingency processes | ICE.md, REBOOT.md, REPAIR.md | Full |
| MANAGE 3.1 — Pre-deployment testing | TESTING.md, TESTSCORES.md, EVAL.md | Full |
| MANAGE 3.2 — Pre-deployment verification | ENFORCEMENT.md (pre-deployment validation) | Full |
| MANAGE 4.1 — Post-deployment monitoring | MONITOR.md, HEALTHCHECK.md, HEARTBEAT.md, ENFORCEMENT.md | Full |
| MANAGE 4.2 — Incident response | ESCALATION.md, AUDITTRAIL.md, ICE.md | Full |

---

## Relevant NIST Publications Referenced

| Publication | How agent-md-specs Aligns |
|-------------|--------------------------|
| SP 800-207 Zero Trust Architecture | LEASTPRIVILEGE.md, ATTESTATION.md, ENFORCEMENT.md |
| SP 800-63-4 Digital Identity Guidelines | WHOAMI.md, ID.md, ATTESTATION.md |
| NISTIR 8587 Token Protection | SESSION.md, ATTESTATION.md, SECRETS.md |
| AI RMF 1.0 (AI 100-1) | Full crosswalk above |
| NCCoE Concept Paper (Feb 2026) | Full question mapping above |

---

## The Accountability Chain

These specs together create a complete, auditable chain
from human authorization to tamper-proof record:

```
DELEGATION.md      -> Who authorized this agent?
WHOAMI.md + ID.md  -> Who is this agent?
ATTESTATION.md     -> Can it prove its identity?
SESSION.md         -> What is its current runtime scope?
LEASTPRIVILEGE.md  -> What is it allowed to do right now?
INTENT.md          -> What does it intend to do?
PROMPTSHIELD.md    -> Is the input safe to act on?
PROVENANCE.md      -> Where did the data come from?
     [ACTION TAKEN]
AUDITTRAIL.md      -> What happened, provably?
ENFORCEMENT.md     -> Can we verify all of the above?
ESCALATION.md      -> Should a human review this?
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
