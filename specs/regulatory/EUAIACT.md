---
spec_name: EUAIACT.md
spec_version: 0.1.0
category: Regulatory Compliance
domain: euaiactmd.dev
priority: Very High
volume: "Vol 9 — Guardrails & Regulatory Compliance Library"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# EUAIACT.md

**Category:** Regulatory Compliance
**Domain:** euaiactmd.dev
**Priority:** Very High
**Version:** 0.1.0

### Purpose
The EU AI Act is the world's first comprehensive AI regulation.
It classifies AI systems by risk level and imposes requirements 
proportional to that risk. Every AI agent operating in the EU 
needs to understand its classification.

```markdown
---
agent_name: string
version: semver
ai_act_applicable: boolean
risk_classification: string   # unacceptable | high | limited | minimal
gpai_model: boolean          # General Purpose AI model
last_reviewed: date
compliance_deadline: date
---

# [Agent Name] — EU AI Act Compliance

## IMPORTANT: Phased Implementation
- February 2025: Prohibited AI practices banned
- August 2025: GPAI obligations apply
- August 2026: High-risk AI obligations fully apply
- August 2027: High-risk AI in existing systems

## Risk Classification

### Unacceptable Risk (PROHIBITED)
These AI applications are banned in the EU:
- Social scoring by governments
- Real-time remote biometric ID in public spaces (with exceptions)
- AI exploiting vulnerabilities of specific groups
- Subliminal manipulation causing harm
- Predictive policing based solely on profiling

**Does this agent do any of the above?** [No — confirm | Possibly — review needed]

### High Risk (REGULATED)
Subject to mandatory requirements if in these categories:
- Critical infrastructure
- Educational/vocational training
- Employment and worker management
- Essential services (credit, insurance)
- Law enforcement
- Migration and border control
- Administration of justice
- Democratic processes

**Is this agent high-risk?** [Yes — see requirements | No | Unsure — seeking guidance]

### Limited Risk (TRANSPARENCY OBLIGATIONS)
- Chatbots must disclose they are AI
- Deepfakes must be labeled
- Emotion recognition systems must inform users

**Applies to this agent:** [Yes — disclosure implemented | No]

### Minimal Risk (NO SPECIFIC REQUIREMENTS)
Most AI systems fall here — games, spam filters, etc.

**This agent's classification:** [classification]  
**Classification rationale:** [explanation]

---

## If High-Risk: Mandatory Requirements

### Risk Management System
- [ ] Risk management system established and maintained
- [ ] Risks identified, estimated, evaluated
- [ ] Risk mitigation measures implemented
- [ ] System tested for residual risks

### Data Governance
- [ ] Training data relevant and representative
- [ ] Data examined for biases
- [ ] Data protection measures applied

### Technical Documentation
- [ ] Technical documentation prepared
- [ ] Kept up to date throughout lifecycle
- [ ] Available to authorities on request

### Record Keeping
- [ ] Automatic logs kept per AUDITTRAIL.md (where technically feasible)
- [ ] Logs retained for appropriate period

### Transparency and User Information
- [ ] Users informed they are interacting with high-risk AI
- [ ] Instructions for use provided
- [ ] Capabilities and limitations disclosed

### Human Oversight
- [ ] Human oversight measures implemented
- [ ] Humans can monitor, override, intervene
- [ ] System can be paused/stopped by humans

### Accuracy, Robustness, Cybersecurity
- [ ] Appropriate accuracy levels demonstrated
- [ ] Robust against errors and attacks
- [ ] Cybersecurity measures in place

### Conformity Assessment
- [ ] Conformity assessment completed (self or third-party)
- [ ] EU Declaration of Conformity prepared
- [ ] CE marking applied (for products)
- [ ] Registered in EU database (if required)

---

## General Purpose AI (GPAI) Model Obligations
If this agent IS or IS BUILT ON a GPAI model:

### All GPAI Models
- [ ] Technical documentation prepared
- [ ] Copyright compliance information maintained
- [ ] Summary of training data published

### Systemic Risk GPAI (>10^25 FLOPs training)
- [ ] Model evaluations conducted
- [ ] Adversarial testing done
- [ ] Serious incidents tracked and reported
- [ ] Cybersecurity protections implemented

## AI Literacy
The AI Act requires users have sufficient AI literacy.  
**This agent's AI literacy support:**
- [How users are informed about AI capabilities]
- [Documentation provided]
- [Training offered if relevant]

## Prohibited Practices Confirmation
Verify compliance using ENFORCEMENT.md checks.
I confirm this agent does NOT:
- [ ] Deploy subliminal manipulation techniques
- [ ] Exploit vulnerabilities of specific groups
- [ ] Conduct real-time biometric surveillance in public
- [ ] Create or expand facial recognition databases
- [ ] Infer emotions in workplace/education (with exceptions)
- [ ] Conduct social scoring

## Supervisory Authority
**Lead AI Office:** European AI Office (ai-office.ec.europa.eu)  
**National authority:** [Country-specific authority]

## Penalties
- Prohibited practices: up to €35M or 7% global turnover
- High-risk non-compliance: up to €15M or 3% global turnover
- False information: up to €7.5M or 1.5% global turnover
```

## Example Use Cases

**Enterprise:** A European HR tech company uses EUAIACT.md to classify its resume screening agent as high-risk (employment category), implementing mandatory bias testing, human oversight controls, and a conformity assessment before the August 2026 deadline.

**Multi-Agent Fleet:** A GPAI model provider uses EUAIACT.md to document training data summaries and copyright compliance information across all derivative agents, meeting the August 2025 GPAI obligations for its entire fleet.

**Regulated Industry:** A credit scoring company uses EUAIACT.md to prepare its EU Declaration of Conformity and technical documentation for its lending decision agent, ensuring the accuracy, robustness, and explainability requirements are met to avoid penalties of up to 3% of global turnover.

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
