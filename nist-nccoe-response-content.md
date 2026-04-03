# Response to NCCoE Concept Paper: "Accelerating the Adoption of Software and AI Agent Identity and Authorization"

**Submitted by:** TotalMarkdown.ai
**Date:** March 2026
**Contact:** contact@totalmarkdown.ai
**Repository:** https://github.com/totalmarkdown/agent-md-specs
**Release:** https://github.com/totalmarkdown/agent-md-specs/releases/tag/v1.2.0-nist-submission
**License:** CC0 1.0 Universal (Public Domain)

---

## 1. Executive Response

### The Problem

AI agents operating in production environments need to declare far more than task instructions. They need verifiable identity, scoped authority, auditable intent, tamper-proof action records, and provable compliance with declared constraints. Current agent configuration approaches — including AGENTS.md (AAIF), CLAUDE.md (Anthropic), and ad-hoc program files — address behavior and project instructions but leave identity, authorization, and accountability undefined. As frontier model capabilities continue to advance rapidly, the need for declarative, verifiable governance frameworks for autonomous agents becomes increasingly urgent — not as a constraint on innovation, but as the infrastructure that enables responsible deployment at scale.

### Our Approach

agent-md-specs is a proposed open standard library of 179 Markdown file type specifications covering every dimension of AI agent governance. The framework defines a declarative vocabulary layer that sits between human-readable policy definition and machine-enforceable runtime controls.

The specifications serve two distinct purposes:

**Static configuration specs** (e.g., WHOAMI.md, LIMITS.md, DELEGATION.md) are committed to version control and define the agent's permanent identity, constraints, and organizational configuration. They change infrequently and are version-controlled like any configuration file.

**Runtime schema specs** (e.g., INTENT.md, SESSION.md, AUDITTRAIL.md) define the format and validation rules for ephemeral data generated during agent execution — API payloads, session tokens, and audit log entries. These are not files overwritten on disk; they are schemas that runtime systems consume.

This distinction means agent-md-specs functions as a declarative policy specification that compiles down into machine-enforceable rules via policy engines (e.g., OPA/Rego), API gateways, and identity providers — not as a file-based runtime system.

Crucially, while authored in human-readable Markdown, every Core specification is governed by a corresponding JSON Schema, enabling native integration into Zero Trust Policy Enforcement Points (PEPs) and API gateways without format translation.

### Why Markdown

While machine-native formats (JSON, YAML) are necessary for runtime execution, they fail as human-auditable governance artifacts. Compliance officers, security architects, and enterprise CISOs need to read and approve the policies that govern agent behavior. Markdown provides this human readability while remaining machine-parseable via YAML frontmatter and structured sections. JSON Schema definitions are provided for all core specifications, enabling automated validation at three levels: syntax, completeness, and content conformance.

Every spec file contains YAML frontmatter — structured, typed, schema-validated metadata — inside a Markdown document. The same file serves as both the human-readable policy (auditable by compliance officers) and the machine-consumable configuration (parseable by any standard YAML library in three lines of code). JSON Schema definitions for all Core specs enable automated conformance validation. No special compiler is required — the policies humans approve are identical to the data machines enforce.

### Ecosystem Context

> *"Markdown is becoming the human-readable contract for what the agent should do, when it should do it, and what resources it should use."* — Visual Studio Magazine, February 2026

The markdown-as-agent-configuration pattern is already an industry standard: AGENTS.md (60,000+ repositories), CLAUDE.md and SKILL.md (Anthropic ecosystem), and Karpathy's program.md (59,000+ stars). agent-md-specs standardizes and extends this pattern into the identity, governance, compliance, and accountability dimensions that production deployments require.

**No new infrastructure required.** agent-md-specs integrates directly into existing API gateways, OPA/Rego policies, CI/CD pipelines, and identity providers. It defines the policy layer — existing runtime systems enforce it.

This submission aligns with the White House's March 2026 AI Legislative Recommendations, which emphasize the need for industry-led AI standards and the establishment of regulatory sandboxes for AI innovation.

---

## 2. Mapping to NCCoE Concept Paper Questions

### 2.1 Identification

*"How might agents be identified in an enterprise architecture? What metadata is essential for an AI agent's identity?"*

- **WHOAMI.md** — Declarative identity document: name, version, capabilities, model, owner, organizational affiliation.
- **ID.md** — Permanent UUID anchor with cryptographic binding.
- **ATTESTATION.md** — Identity verification via SPIFFE/SPIRE workload identities, X.509 certificates, or Decentralized Identifiers (DIDs), with hardware binding (TPM/HSM) and software binding (container hash, model checksum). Directly implements SP 800-63-4 identity assurance levels.
- **SESSION.md** — Ephemeral, task-scoped identity addressing the concept paper's question of whether identity should be persistent or dynamic. Each session generates short-lived credentials that are destroyed on task completion.

### 2.2 Authentication

*"What constitutes strong authentication for an AI agent? How do we handle key management?"*

- **ATTESTATION.md** defines the complete credential lifecycle: issuance, rotation schedule, revocation mechanisms, and compromise recovery procedures. Maps to SPIFFE/SPIRE for workload attestation and supports FIDO2/YubiKey for human-in-the-loop identity binding.
- **SECRETS.md** declares what credentials the agent requires without storing values — the manifest that infrastructure teams provision from.

### 2.3 Authorization

*"How can zero-trust principles be applied? How do we establish least privilege? How do we handle delegation of authority? How might an agent convey the intent of its actions?"*

- **DELEGATION.md** — Defines the complete authority chain from human principal to agent, including scope constraints, time bounds, budget caps, geographic restrictions, sub-delegation policies (enforcing scope narrowing), and revocation mechanisms. Maps directly to OAuth 2.0 On-Behalf-Of (OBO) token exchange flows. Addresses the "confused deputy" problem by requiring explicit scope allow-lists rather than deny-lists.
- **LEASTPRIVILEGE.md** — Implements SP 800-207 zero-trust principles with a minimal privilege baseline, just-in-time escalation requiring explicit approval, automatic de-escalation after use, and a defined policy for unknown actions (deny-and-log by default).
- **INTENT.md** — Addresses the concept paper's novel question: "How might an agent convey the intent of its actions?" Defines a structured format for pre-action intent declaration with confidence scoring, impact assessment, and human review thresholds. Includes a critical requirement that confidence scores be derived from external evaluators, not agent self-assessment. Intent declarations are cryptographically bound to subsequent audit trail entries via hash inclusion.
- **CONSENT.md** — Addresses the user consent lifecycle — how end-user permission is obtained, recorded, verified, and revoked for agent actions affecting individuals. It defines structured consent records with scope, expiry, evidence, and revocation fields, and requires that consent cover specific agents in multi-agent systems. Maps to GDPR Article 7 (conditions for consent), CCPA §1798.100-120, and EU AI Act Article 13 (transparency for high-risk systems).

### 2.4 Auditing and Non-Repudiation

*"How can we ensure tamper-proof, verifiable logging? How do we ensure non-repudiation? How do we bind actions back to human authorization?"*

- **AUDITTRAIL.md** — Defines a tamper-resistant audit record format with hash-chain integrity, cryptographic signing via the agent's attestation credentials, and compliance-specific retention mappings (GDPR Article 30: 3 years, HIPAA §164.312: 6 years, SOC2 CC7.2: 1 year, EU AI Act Article 12: 10 years). Each entry links to the delegation chain, the declared intent, and input/output hashes — providing complete non-repudiation from action back to human authorization.

### 2.5 Data Flow Tracking

*"Track and maintain provenance of user prompts and data input sources to support risk determinations."*

- **PROVENANCE.md** — Defines input source registries with trust classification (trusted/verified/unverified/untrusted/adversarial), prompt provenance tracking, context window hashing, transformation logs, and critically, data classification escalation rules — addressing the concept paper's question about determining sensitivity when individually non-sensitive data points become sensitive when aggregated by an agent.

### 2.6 Prompt Injection

*"What controls help prevent direct and indirect prompt injections? After injection occurs, what controls minimize the impact?"*

- **PROMPTSHIELD.md** — Comprehensive defense-in-depth specification covering instruction boundary enforcement, privilege separation between user instructions and retrieved content, content sandboxing for untrusted tool outputs, canary token detection, containment procedures (halt, quarantine, rollback), recovery playbooks, and red team testing requirements. Treats prompt injection as a capability integrity problem — ensuring malicious inputs cannot alter the agent's fundamental authorization boundaries — rather than merely an input filtering challenge.

### 2.7 Shared Memory Security

*Addresses OWASP ASI06 (Memory Poisoning) — recognized by NIST CAISI*

NIST CAISI's RFI on AI Agent Security explicitly identifies "memory management vulnerabilities" as a threat category. OWASP's Top 10 for Agentic Applications (ASI06, recognized by NIST CAISI) lists memory poisoning as a top attack vector — where an attacker injects false facts into an agent's persistent memory to manipulate future behavior.

We address this through two complementary specifications:

- **SHAREDCONTEXT.md** — Defines the governance framework for multi-agent shared memory pools — access control matrices tied to delegation authority, structured entry schemas with confidence scoring and classification levels, retention policies with TTL enforcement, and inheritance rules across the organizational hierarchy (org → swarm → crew → team → agent). It ensures that shared context is structured, access-controlled, and auditable.
- **MEMORYSAFETY.md** — Defines the security layer — input sanitization (write gateway), poisoning detection via canary entries and anomaly analysis, quarantine procedures for suspicious entries, cross-session isolation to prevent context leakage, memory integrity verification via hash chains and signed entries, and classification enforcement ensuring agents can only read entries at or below their clearance level.

### 2.8 Failure Containment

*Addresses OWASP ASI08 (Cascading Failures) — recognized by NIST CAISI*

OWASP's ASI08 notes that "one agent's error propagates across an entire multi-agent workflow faster than any human can intervene" and that "most agent architectures have no equivalent to circuit breakers."

- **CIRCUITBREAKER.md** — Defines failure containment boundaries using the standard circuit breaker pattern (Closed → Open → Half-Open) with agent-specific extensions: failure thresholds (consecutive errors, error rate, latency, resource exhaustion), blast radius boundaries at each organizational level (agent → team → crew → swarm), fallback behaviors (cached results, graceful degradation, queue-for-retry, escalate to human), retry policies with exponential backoff, and cascading prevention rules including timeout enforcement, bulkhead isolation, fan-out limits, and poison pill detection.

---

## 3. The Accountability Chain

These specifications create a complete, verifiable chain from human authorization to tamper-proof record, with each step mapped to its operational phase and SP 800-207 Zero Trust Architecture component:

| Step | Specification | Question Answered | Phase | ZTA Component |
|------|--------------|-------------------|-------|---------------|
| 1 | DELEGATION.md | Who authorized this agent? | Pre-deployment | Policy Information Point |
| 2 | CONSENT.md | Did the user give permission? | Pre-deployment | Policy Information Point |
| 3 | WHOAMI.md + ID.md | Who is this agent? | Pre-deployment | Policy Information Point |
| 4 | ATTESTATION.md | Can it prove its identity? | Runtime (continuous) | Policy Information Point |
| 5 | SESSION.md | What is its runtime scope? | Runtime (per-task) | Microsegmentation boundary |
| 6 | LEASTPRIVILEGE.md | What can it do right now? | Runtime (per-action) | Policy Decision Point |
| 7 | INTENT.md | What does it intend to do? | Runtime (per-action) | Trust zone boundary |
| 8 | PROMPTSHIELD.md | Is the input safe? | Runtime (per-input) | Policy Enforcement Point |
| 9 | PROVENANCE.md | Where did the data come from? | Runtime (per-input) | Policy Information Point |
| 10 | SHAREDCONTEXT.md | Is shared memory trustworthy? | Runtime | Policy Information Point |
| 11 | MEMORYSAFETY.md | Has memory been poisoned? | Runtime | Policy Enforcement Point |
| | **[ACTION TAKEN]** | | | |
| 12 | CIRCUITBREAKER.md | Did something fail? Contain it. | On-failure | Policy Enforcement Point |
| 13 | AUDITTRAIL.md | What happened, provably? | Post-action | Continuous Diagnostics |
| 14 | ENFORCEMENT.md | Can we verify all of the above? | Continuous | Policy Enforcement Point |
| 15 | ESCALATION.md | Should a human review this? | On-trigger | Human override boundary |

The ENFORCEMENT.md meta-specification defines three verification layers:

1. **Pre-deployment validation** — CI/CD pipeline checks via the agent-md-validator CLI tool, ensuring all declared specs pass structural and content validation before an agent is deployed.
2. **Runtime monitoring** — Behavioral drift detection against declared constraints, enforced via external interceptors (API gateways, policy engines such as OPA/Rego), not on-agent self-policing. This distinction is critical: enforcement occurs at infrastructure-level policy enforcement points, not within the agent itself.
3. **Post-hoc audit** — Cryptographic verification of the audit trail against declared intents and delegation chains, with external audit anchors for independent verification.

---

## 4. Demonstration: The Atlas Enterprise Example

The repository includes a complete enterprise example bundle demonstrating all accountability chain specs in a realistic financial services scenario.

**Agent:** Atlas v2.1 — Financial Analysis Agent
**Organization:** Acme Corp (fictional)
**Delegated by:** CFO Sarah Chen
**Model:** Claude Sonnet 4.6
**Purpose:** Generate quarterly financial reports and forecasts for the CFO's office

The Atlas bundle contains 19 fully configured specification files showing:

- **Delegation** scoped to read-only financial data and report generation, expiring quarterly, with no sub-delegation permitted and revocation via the compliance portal
- **User consent** via employee onboarding agreement covering AI-assisted financial analysis
- **Identity verification** via SPIFFE workload identity (spiffe://acme.corp/finance/agents/atlas) with X.509 certificate from Acme Corp Internal CA and 90-day key rotation
- **Session boundaries** of 30 minutes maximum with ephemeral in-memory-only credentials, a maximum of 50 actions per session, and mandatory memory wipe on completion (audit entries preserved)
- **Just-in-time privilege escalation** requiring CFO FIDO2 digital approval for email sending, with automatic de-escalation after single use
- **Shared memory governance** with financial data canary entries, write gateway sanitization, and cross-session isolation
- **Failure containment** via circuit breaker with 3-failure threshold, cached report fallback, and cascading prevention
- **Tamper-proof audit trail** using SHA-256 hash chains with 7-year retention for SOX compliance, signed entries using the agent's X.509 certificate, and a query endpoint for auditor access
- **Prompt injection defenses** including financial-domain canary tokens, SQL injection pattern blocking, and a containment procedure that halts execution and alerts the compliance team
- **Hard limits** that can never be overridden: never execute trades, never access HR/personnel data, never communicate outside the acme.corp network, never process data from OFAC-sanctioned entities

Repository path: examples/nist-nccoe-bundle/

This bundle represents the level of governance documentation that a financial services compliance team would require before approving deployment of an AI agent with access to sensitive data.

---

## 5. Standards Alignment and Next Steps

### Relationship to Referenced Standards

agent-md-specs is designed as a complementary vocabulary layer that works alongside — not against — the standards and protocols referenced in the concept paper:

| Standard | Role | How agent-md-specs Relates |
|----------|------|---------------------------|
| MCP (AAIF) | Tool connectivity protocol | agent-md-specs governs which MCP connections are authorized via PERMISSIONS.md and ACCESS.md |
| AGENTS.md (AAIF) | Project-specific instructions | agent-md-specs adds the identity, governance, and accountability layer that AGENTS.md does not address |
| OAuth 2.0 / OIDC | Authorization transport | DELEGATION.md defines the authorization policy; OAuth transports it at runtime |
| SPIFFE/SPIRE | Workload identity framework | ATTESTATION.md specifies SPIFFE as a primary verification method with SPIRE integration |
| SP 800-207 | Zero Trust Architecture | The 15-step accountability chain maps to PEP, PDP, and PIP components |
| SP 800-63-4 | Digital Identity Guidelines | WHOAMI.md + ATTESTATION.md implement identity assurance levels |
| NGAC | Attribute-based access control | LEASTPRIVILEGE.md defines the dynamic policies that NGAC enforces |
| OWASP Agentic Top 10 (2026) | Agentic security threats (recognized by NIST CAISI) | ASI06 → MEMORYSAFETY.md, ASI08 → CIRCUITBREAKER.md |

### Tooling and Validation

- **agent-md-validator** (v0.1.0): Open-source CLI tool that validates YAML frontmatter, required sections, cross-references, and tier compliance across spec files. Repository: https://github.com/totalmarkdown/agent-md-validator
- **JSON Schemas**: Machine-readable schema definitions for all 47 Core specifications, enabling automated conformance validation at three levels: Level 1 (syntax), Level 2 (completeness), Level 3 (content constraints).

### Governance

The project follows a formal specification lifecycle (Draft, Proposed, Stable, Deprecated, Retired) with an RFC process for Core spec changes, defined criteria for tier promotion and demotion, and semantic versioning for both individual specs and the library as a whole. All 179 specifications are CC0 public domain with zero licensing friction for adoption by government agencies, enterprises, or standards bodies.

### Invitation

We welcome the opportunity to participate in future NCCoE workshops, demonstration projects, or working groups related to AI agent identity and authorization — including collaboration on building a demonstrable reference architecture using the agent-md-specs framework. The complete framework — including all 179 specifications, JSON schemas, validator tooling, seven example bundles, and the NIST crosswalk mapping — is available at:

**https://github.com/totalmarkdown/agent-md-specs**

---

*Submitted by TotalMarkdown.ai · CC0 1.0 Universal (Public Domain) · March 2026*
