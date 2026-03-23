---
bundle_name: "nist-nccoe-bundle"
agent_name: "Atlas"
version: "2.1.0"
org: "Acme Corp"
spec_profile: "nist-nccoe-identity-authorization"
created: "2025-11-01"
updated: "2026-03-15"
---

# Atlas -- NIST NCCoE Agent Identity & Authorization Bundle

## Overview

This bundle demonstrates a production deployment of the agent-md specification
suite applied to a real enterprise use case: an AI-powered financial analysis
agent operating under strict regulatory compliance requirements.

**Atlas** is Acme Corp's financial analysis agent, built on Claude Sonnet 4 and
deployed on Acme's private cloud infrastructure. It generates quarterly financial
reports and forecasts for the CFO's office, operating under SOX, GDPR, and SOC2
compliance obligations.

## Purpose

This example bundle shows how the agent-md specs map to the NIST National
Cybersecurity Center of Excellence (NCCoE) framework for AI agent identity,
authorization, and governance. Each file in this bundle corresponds to a spec
in the agent-md standard, populated with realistic enterprise content rather
than placeholder templates.

## Specs Included

| File | Spec | Purpose |
|------|------|---------|
| SOUL.md | Core | Personality, values, and behavioral norms |
| WHOAMI.md | Core | Machine-readable identity card |
| DELEGATION.md | Authorization | Authority chain and scope |
| ATTESTATION.md | Identity | Cryptographic identity binding |
| SESSION.md | Runtime | Session lifecycle and isolation |
| LEASTPRIVILEGE.md | Authorization | Minimal permissions model |
| INTENT.md | Runtime | Action declaration and approval |
| PROMPTSHIELD.md | Security | Input validation and injection defense |
| PROVENANCE.md | Trust | Data source classification and lineage |
| AUDITTRAIL.md | Compliance | Immutable logging and retention |
| ESCALATION.md | Governance | Human-in-the-loop tiers |
| LIMITS.md | Governance | Hard behavioral constraints |
| PERMISSIONS.md | Authorization | Granular access control list |
| ENFORCEMENT.md | Runtime | Policy enforcement mechanisms |

## Compliance Mapping

- **SOX Section 302/404:** AUDITTRAIL.md, PROVENANCE.md, LIMITS.md
- **GDPR Articles 13-15, 22:** SESSION.md, PROVENANCE.md, AUDITTRAIL.md
- **SOC2 Trust Criteria:** ATTESTATION.md, LEASTPRIVILEGE.md, ENFORCEMENT.md

## How to Use This Bundle

1. Review WHOAMI.md and SOUL.md to understand Atlas's identity and behavior.
2. Review DELEGATION.md and PERMISSIONS.md to understand its authority scope.
3. Review ENFORCEMENT.md to understand how policies are enforced at runtime.
4. Use this bundle as a reference when building your own agent-md deployment.

## Contact

- **Agent Owner:** CFO's Office, Acme Corp
- **Compliance Officer:** James Park, james.park@acme.corp
- **Engineering Lead:** Maria Gonzalez, maria.gonzalez@acme.corp
- **Security Review:** Acme InfoSec Team, infosec@acme.corp
