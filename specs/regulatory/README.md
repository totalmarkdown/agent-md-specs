# Regulatory Specs

Specific regulation compliance templates for agents operating under legal frameworks. These specs provide structured, machine-readable compliance declarations for major data protection laws, industry standards, and AI-specific regulations. They turn legal requirements into actionable agent configuration that can be validated automatically.

## How These Specs Work Together

EUAIACT is the most comprehensive starting point -- as the first major AI-specific regulation, it sets the pattern for risk classification and compliance documentation. CCPA, LGPD, PDPA, and PIPEDA cover regional data protection with overlapping but distinct requirements. HIPAA, FERPA, and COPPA address sector-specific data rules for healthcare, education, and children. SOC2, ISO27001, and PCIDSS provide industry security frameworks. DORA and NIS2 target digital resilience for financial and critical infrastructure. NISTAIRF and AML round out the set with AI risk management and anti-money-laundering. Adopt specs based on your agent's jurisdiction and industry -- most agents need EUAIACT or CCPA plus one industry framework.

## Specs in This Category

| Spec | Tier | Purpose | Scope |
|------|------|---------|-------|
| [AML.md](AML.md) | Extended | Anti-money laundering compliance for financial agents | Financial crime prevention |
| [CCPA.md](CCPA.md) | Extended | California Consumer Privacy Act compliance | US state data privacy |
| [COPPA.md](COPPA.md) | Extended | Children's Online Privacy Protection Act compliance | Child data protection |
| [DORA.md](DORA.md) | Extended | Digital Operational Resilience Act for EU financial entities | Financial sector resilience |
| [EUAIACT.md](EUAIACT.md) | Extended | EU AI Act risk classification and compliance requirements | AI-specific regulation |
| [FERPA.md](FERPA.md) | Extended | Family Educational Rights and Privacy Act compliance | Education data protection |
| [HIPAA.md](HIPAA.md) | Extended | Health Insurance Portability and Accountability Act compliance | Healthcare data protection |
| [ISO27001.md](ISO27001.md) | Extended | ISO/IEC 27001:2022 information security management | Security certification |
| [LGPD.md](LGPD.md) | Extended | Brazil's General Data Protection Law compliance | Brazilian data privacy |
| [NIS2.md](NIS2.md) | Extended | EU Network and Information Security Directive compliance | Critical infrastructure security |
| [NISTAIRF.md](NISTAIRF.md) | Extended | NIST AI Risk Management Framework 1.0 alignment | US AI risk management |
| [PCIDSS.md](PCIDSS.md) | Extended | Payment Card Industry Data Security Standard compliance | Payment data protection |
| [PDPA.md](PDPA.md) | Extended | Thailand/Singapore Personal Data Protection Act compliance | Southeast Asian data privacy |
| [PIPEDA.md](PIPEDA.md) | Extended | Canada's Personal Information Protection compliance | Canadian data privacy |
| [SOC2.md](SOC2.md) | Extended | System and Organization Controls 2 compliance | Service organization trust |

## When to Use These Specs

- **Deploying agents in the EU:** Start with EUAIACT for AI-specific requirements, add DORA or NIS2 if operating in financial or critical infrastructure sectors.
- **Handling personal data:** Pick the relevant regional spec (CCPA, LGPD, PDPA, PIPEDA) based on where your users are located, plus HIPAA or FERPA for sector-specific data.
- **Achieving enterprise trust:** SOC2, ISO27001, and PCIDSS provide the security certifications that enterprise buyers require before procurement.

## Related Categories

| Category | How It Relates |
|----------|---------------|
| [compliance/](../compliance/) | AUDITTRAIL and COMPLIANCE provide the general framework regulatory specs implement |
| [governance/](../governance/) | POLICY and GUARDRAILS enforce the rules that regulatory specs define |
| [security/](../security/) | Security specs implement the technical controls regulatory specs require |
| [quality/](../quality/) | VALIDATION and TESTING verify that regulatory requirements are actually met |

---
*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)
· [Full Index](../../INDEX.md) · [README](../../README.md)*
