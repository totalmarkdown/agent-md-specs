---
spec_name: NISTAIRF.md
spec_version: 0.1.0
category: Regulatory Compliance
domain: nistairdmd.dev
priority: Medium
volume: "Vol 9 — Guardrails & Regulatory Compliance Library"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# NISTAIRF.md

**Category:** Regulatory Compliance
**Domain:** nistairdmd.dev
**Priority:** Medium
**Version:** 0.1.0

**Framework:** NIST AI Risk Management Framework 1.0  
**Version:** 0.1.0

```markdown
---
agent_name: string
version: semver
nist_airf_adopted: boolean
implementation_tier: string   # 1-partial | 2-risk-informed | 3-repeatable | 4-adaptive
last_reviewed: date
---

# [Agent Name] — NIST AI RMF Compliance

## Framework Overview
The NIST AI RMF organizes AI risk management into four functions: 
GOVERN, MAP, MEASURE, MANAGE.

**Implementation Tier:** [1-Partial | 2-Risk Informed | 3-Repeatable | 4-Adaptive]

## GOVERN
Organizational practices for AI risk management.

| Activity | Status | Notes |
|----------|--------|-------|
| AI risk policies established | [✓/✗] | |
| Accountability structures defined | [✓/✗] | |
| Workforce AI risk training | [✓/✗] | |
| Organizational risk tolerance defined | [✓/✗] | |
| AI transparency and explainability commitments | [✓/✗] | |

## MAP
Context established for AI risk assessment.

| Activity | Status | Notes |
|----------|--------|-------|
| AI system purpose documented | [✓/✗] | |
| Stakeholders identified | [✓/✗] | |
| AI risks categorized | [✓/✗] | |
| Risk tolerance applied | [✓/✗] | |
| Scientific and technical knowledge considered | [✓/✗] | |

## MEASURE
AI risks analyzed and assessed.

| Activity | Status | Notes |
|----------|--------|-------|
| Risk evaluation methods defined | [✓/✗] | |
| AI system tested and evaluated | [✓/✗] | |
| Bias testing conducted | [✓/✗] | |
| Performance benchmarks established | [✓/✗] | |
| Effectiveness of risk responses tracked | [✓/✗] | |

## MANAGE
AI risks prioritized and addressed.

| Activity | Status | Notes |
|----------|--------|-------|
| Risk treatment plans implemented | [✓/✗] | |
| Residual risks monitored | [✓/✗] | |
| Incident response procedures in place | [✓/✗] | |
| Risk management outcomes documented | [✓/✗] | |

## Trustworthy AI Characteristics
NIST identifies these characteristics of trustworthy AI:
| Characteristic | How this agent addresses it |
|---------------|---------------------------|
| Accountable (see AUDITTRAIL.md) | [approach] |
| Explainable | [approach] |
| Fair/Bias-managed | [approach] |
| Interpretable | [approach] |
| Privacy-enhanced (see CONSENT.md) | [approach] |
| Reliable | [approach] |
| Safe | [approach] |
| Secure/Resilient | [approach] |
| Transparent | [approach] |
| Valid/Tested | [approach] |
```

## Example Use Cases

**Enterprise:** A US federal contractor uses NISTAIRF.md to structure its AI risk management program at Tier 3 (Repeatable), documenting all four functions (GOVERN, MAP, MEASURE, MANAGE) for its document analysis agents to satisfy government procurement requirements.

**Multi-Agent Fleet:** A platform company uses NISTAIRF.md's trustworthy AI characteristics to create a standardized scorecard for all agents in its fleet, ensuring each agent demonstrates accountability, fairness, and transparency before being approved for production.

**Regulated Industry:** A US banking institution uses NISTAIRF.md to complement its existing risk management framework, documenting bias testing results and risk treatment plans for its lending decision agent to satisfy OCC and Federal Reserve AI governance expectations.

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
