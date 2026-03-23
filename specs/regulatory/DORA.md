---
spec_name: DORA.md
spec_version: 0.1.0
category: Regulatory Compliance
domain: doramd.dev
priority: High
volume: "Vol 9 — Guardrails & Regulatory Compliance Library"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# DORA.md

**Category:** Regulatory Compliance
**Domain:** doramd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
DORA is brand new (January 2025) and specifically addresses 
digital operational resilience for financial entities in the EU.
It's the first regulation that directly addresses AI and 
third-party technology risk in financial services at this level.

```markdown
---
agent_name: string
version: semver
dora_applicable: boolean
entity_type: string    # financial-entity | ict-provider | both
in_scope: boolean
last_reviewed: date
compliance_deadline: date  # January 17, 2025
---

# [Agent Name] — DORA Compliance

## Applicability
DORA applies to:
- **Financial entities:** Banks, insurance, investment firms, crypto assets
- **Critical ICT third-party providers:** Designated by ESAs

**This agent/org is a:** [Financial entity | ICT provider | Both | Neither]

## Five Pillars of DORA

### 1. ICT Risk Management
Financial entities must have robust ICT risk frameworks.

| Requirement | Status | Notes |
|-------------|--------|-------|
| ICT risk management framework | [✓/✗] | |
| ICT systems identified and documented | [✓/✗] | |
| Protection and prevention measures | [✓/✗] | |
| Detection mechanisms | [✓/✗] | |
| Response and recovery procedures | [✓/✗] | |
| Backup and recovery testing | [✓/✗] | |
| Communication plan for ICT incidents | [✓/✗] | |

### 2. ICT Incident Management and Reporting
**Classification:**  
Major ICT incident criteria:
- Number of clients affected
- Duration of downtime
- Geographic spread
- Data losses
- Impact on critical services

**Reporting timeline:**
- Initial notification: within 4 hours of classification as major
- Intermediate report: within 72 hours
- Final report: within 1 month

**Report to:** [National Competent Authority]

### 3. Digital Operational Resilience Testing

| Test type | Frequency | Status |
|-----------|-----------|--------|
| Basic testing (vulnerability assessments) | Annual | [✓/✗] |
| Advanced testing (TLPT) | Every 3 years | [✓/✗] |
| Threat-led penetration testing | Every 3 years | [if significant] |

### 4. ICT Third-Party Risk Management
**Third-party register maintained:** [yes/no]  
**Critical ICT providers identified:** [yes/no]  
**Contractual arrangements with ICT providers include:**
- [ ] Service level descriptions
- [ ] Data location and processing
- [ ] Right to audit
- [ ] Exit strategy provisions
- [ ] Incident reporting by provider

### 5. Information Sharing
Participate in threat intelligence sharing arrangements:
[Relevant ISACs or sharing arrangements]

## As an ICT Provider
If this agent/org is an ICT provider to financial entities:
- [ ] Register with relevant ESA (if designated critical)
- [ ] Comply with oversight framework
- [ ] Provide cooperation to lead overseer
- [ ] Ensure subcontracting meets DORA standards

## Key Dates
- January 17, 2025: DORA fully applicable
- Ongoing: Annual ICT risk assessments
- Every 3 years: Advanced resilience testing
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
