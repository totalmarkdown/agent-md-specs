# Compliance Specs

Compliance specs handle accountability, regulatory adherence, and the legal obligations that agents must satisfy when operating in regulated environments. As AI agents take consequential actions -- processing personal data, making financial decisions, generating licensed content -- these specs provide the audit trails, consent mechanisms, and provenance tracking that regulators and enterprise customers require.

## How These Specs Work Together

Compliance starts with recording. AUDITTRAIL.md creates the tamper-resistant ledger of every significant action, forming the foundation that all other compliance specs depend on. PROVENANCE.md tracks data lineage -- where inputs came from and how they were transformed -- while CONSENT.md manages the lifecycle of user permission for agent actions. COMPLIANCE.md and REGULATIONS.md frame the regulatory landscape, with domain-specific specs like GDPR.md and PII.md addressing particular jurisdictions and data types. Begin with AUDITTRAIL, PROVENANCE, and CONSENT as the compliance core, then adopt the regulatory specs that match your operating jurisdictions.

## Specs in This Category

| Spec | Tier | Purpose | Scope |
|------|------|---------|-------|
| [AUDITTRAIL.md](AUDITTRAIL.md) | core | Tamper-resistant record of every significant agent action | Action logging |
| [CERTIFICATIONS.md](CERTIFICATIONS.md) | extended | Formal compliance certifications and third-party verifications | Credential proof |
| [COMPLIANCE.md](COMPLIANCE.md) | extended | General compliance posture, approved procedures, and frameworks | Compliance overview |
| [CONSENT.md](CONSENT.md) | core | Full lifecycle of end-user consent collection and revocation | Permission management |
| [GDPR.md](GDPR.md) | extended | GDPR-specific requirements including legal bases and DPO details | EU data protection |
| [INSURANCE.md](INSURANCE.md) | extended | Liability coverage and risk insurance for agent operations | Risk transfer |
| [LICENSE.md](LICENSE.md) | extended | License terms for agent bundles on marketplaces | Usage rights |
| [PII.md](PII.md) | extended | Personally identifiable information inventory and handling rules | Data classification |
| [PRIVACY.md](PRIVACY.md) | extended | Data privacy rules, retention policies, and deletion procedures | Data protection |
| [PROVENANCE.md](PROVENANCE.md) | core | Origin tracking and transformation history for all data | Data lineage |
| [REGULATIONS.md](REGULATIONS.md) | extended | Specific regulatory requirements and jurisdictional constraints | Legal constraints |
| [SECURITY.md](SECURITY.md) | extended | Security controls and compliance-oriented security measures | Security posture |

## When to Use These Specs

- **Processing personal data:** Start with CONSENT, PII, and PRIVACY to establish lawful data handling, then add GDPR if operating in EU jurisdictions.
- **Facing enterprise procurement or audit:** Adopt AUDITTRAIL, CERTIFICATIONS, and COMPLIANCE to demonstrate that agent actions are recorded, verifiable, and within approved frameworks.
- **Building data pipelines or content generation:** Use PROVENANCE and LICENSE to track data origin, transformation history, and output usage rights across the full pipeline.

## Related Categories

| Category | How It Relates |
|----------|---------------|
| [governance/](../governance/) | Governance sets the policies that compliance proves are followed -- ENFORCEMENT verifies at runtime, AUDITTRAIL records the proof |
| [regulatory/](../regulatory/) | Regulatory specs define jurisdiction-specific rules; compliance specs provide the mechanisms to satisfy them |
| [security/](../security/) | Security specs protect the compliance infrastructure -- ATTESTATION ensures audit entries are authentic, VAULT protects compliance credentials |
| [identity/](../identity/) | Identity specs like WHOAMI and ID provide the agent identifiers that compliance specs reference in audit records and consent logs |

---
*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)
· [Full Index](../../INDEX.md) · [README](../../README.md)*
