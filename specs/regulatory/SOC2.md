---
spec_name: SOC2.md
spec_version: 0.1.0
category: Regulatory Compliance
domain: soc2md.dev
priority: High
volume: "Vol 9 — Guardrails & Regulatory Compliance Library"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# SOC2.md

**Category:** Regulatory Compliance
**Domain:** soc2md.dev
**Priority:** High
**Version:** 0.1.0

### Purpose

Configures compliance with SOC 2 Trust Service Criteria, documenting control status across security, availability, processing integrity, confidentiality, and privacy. This spec enables agents to demonstrate organizational controls to enterprise customers and auditors, which is often a prerequisite for B2B sales and procurement.

**Framework:** SOC 2 (System and Organization Controls 2)  
**Version:** 0.1.0

```markdown
---
agent_name: string
version: semver
soc2_type: string          # type1 | type2 | in-progress | not-applicable
trust_service_criteria: list  # security | availability | processing-integrity | confidentiality | privacy
last_audit: date
auditor: string
report_available: boolean
---

# [Agent Name] — SOC 2 Compliance

## SOC 2 Status
**Type:** [Type I — design only | Type II — design + operating effectiveness]  
**Status:** [Compliant | In progress | Not yet started]  
**Last audit:** [date]  
**Auditor:** [CPA firm name]  
**Report available:** [Yes — NDA required | No]

## Trust Service Criteria Covered

### Security (CC) — Always required
Controls protecting against unauthorized access.

| Control | Status | Description |
|---------|--------|-------------|
| CC1: Control environment | [✓] | [brief] |
| CC2: Communication | [✓] | [brief] |
| CC3: Risk assessment | [✓] | [brief] |
| CC4: Monitoring (see MONITOR.md) | [✓] | [brief] |
| CC5: Control activities | [✓] | [brief] |
| CC6: Logical access | [✓] | [brief] |
| CC7: System operations | [✓] | [brief] |
| CC8: Change management | [✓] | [brief] |
| CC9: Risk mitigation | [✓] | [brief] |

### Availability (A) — If applicable
| Control | Status |
|---------|--------|
| A1: Availability commitments | [✓/✗] |

### Processing Integrity (PI) — If applicable
| Control | Status |
|---------|--------|
| PI1: Processing complete/accurate/timely | [✓/✗] |

### Confidentiality (C) — If applicable
| Control | Status |
|---------|--------|
| C1: Confidential information identified | [✓/✗] |

### Privacy (P) — If applicable
Aligns with AICPA Privacy Framework and GDPR/CCPA.
| Control | Status |
|---------|--------|
| P1–P8: Privacy criteria | [✓/✗] |

## Key Controls Implemented
_See AUDITTRAIL.md for tamper-proof logging of all control activities._
- [ ] Multi-factor authentication
- [ ] Encryption at rest and in transit
- [ ] Vulnerability scanning (quarterly+)
- [ ] Penetration testing (annual+)
- [ ] Background checks for employees with data access
- [ ] Security awareness training
- [ ] Incident response plan tested
- [ ] Business continuity plan tested
- [ ] Access reviews (quarterly)
- [ ] Vendor risk management

## Requesting the Report
SOC 2 report available under NDA to:
- Enterprise customers (evaluation)
- Prospective enterprise customers
- Security assessment teams

**Request:** [email or form URL]  
**NDA:** [standard NDA | your NDA | mutual NDA]  
**Delivery:** [N business days]
```

## Example Use Cases

**Enterprise:** A B2B SaaS company uses SOC2.md to document its Type II compliance across all five Trust Service Criteria, making the report available under NDA to enterprise prospects during security evaluations — a requirement that closes 90% of their Fortune 500 deals.

**Multi-Agent Fleet:** A managed AI services provider uses SOC2.md to map each control (CC1-CC9) to specific agents in the fleet, demonstrating to auditors that change management, logical access, and monitoring controls are enforced at the individual agent level.

**Regulated Industry:** A financial data aggregator uses SOC2.md to satisfy Processing Integrity (PI1) requirements for its transaction reconciliation agent, proving to banking clients that financial data is processed completely, accurately, and in a timely manner with annual penetration testing and quarterly access reviews.

## Related Specs

| Spec | Relationship |
|------|-------------|
| AUDITTRAIL.md | Tamper-proof action logging |
| CONSENT.md | User consent lifecycle |
| ENFORCEMENT.md | Policy verification and compliance |
| PII.md | Personal data classification |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
