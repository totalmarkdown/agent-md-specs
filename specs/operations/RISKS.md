---
spec_name: RISKS.md
spec_version: 0.1.0
category: Strategic/Operations
domain: risksmd.dev
priority: Medium
volume: "Vol 11 — Performance, Defensibility & Interface Contracts"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# RISKS.md

**Category:** Strategic/Operations
**Domain:** risksmd.dev
**Priority:** Medium
**Version:** 0.1.0

**Priority:** MEDIUM  
**Version:** 0.1.0

### Purpose
Forward-looking risk assessment — what could go wrong,
how likely, how bad, and what's being done about it.

Different from:
- KRYPTONITE.md — current failure modes (known weaknesses)
- REPAIR.md — how to recover from failures
- ICE.md — emergency response

RISKS.md is prospective: risks that haven't happened yet
but could. Strategic and operational risks alike.

### Spec

```markdown
---
entity_name: string
version: semver
risk_assessment_date: date
next_review: date
risk_owner: string
---

# [Entity Name] — Risk Register

## Risk Assessment Summary
**Total risks identified:** [N]  
**Critical (P1):** [N] | **High (P2):** [N] | **Medium (P3):** [N] | **Low (P4):** [N]  
**Last assessed:** [date] | **Next review:** [date]

---

## Risk Register

### RISK-001: [Risk Name]
**Category:** [Technical | Strategic | Operational | Regulatory | Reputational]  
**Probability:** [Very High | High | Medium | Low | Very Low]  
**Impact:** [Critical | High | Medium | Low]  
**Priority:** [P1 | P2 | P3 | P4]  
**Status:** [Active | Mitigated | Accepted | Monitoring]

**Description:**  
[What is the risk? What could happen?]

**Root cause:**  
[Why does this risk exist?]

**Potential impact:**  
[If this risk materializes, what are the consequences?
Be specific — what breaks, who is affected, what is the cost?]

**Current mitigations:**
- [What is already in place to reduce probability or impact]

**Residual risk:**  
[Risk remaining after mitigations — is it acceptable?]

**Response plan:**  
[If this risk materializes, what is the response?]

**Owner:** [Who monitors and manages this risk]  
**Next review:** [date]

---

[Repeat for each significant risk]

---

## Risk Categories

### Technical Risks
| Risk | Prob | Impact | Priority | Mitigation |
|------|------|--------|---------|-----------|
| Model capability degradation | [P] | [I] | [P#] | [mitigation] |
| Integration failure | [P] | [I] | [P#] | [mitigation] |
| Security breach | [P] | [I] | [P#] | [mitigation] |

### Strategic Risks
| Risk | Prob | Impact | Priority | Mitigation |
|------|------|--------|---------|-----------|
| Better competitor emerges | [P] | [I] | [P#] | [mitigation] |
| Market shift away from our approach | [P] | [I] | [P#] | [mitigation] |

### Regulatory Risks
| Risk | Prob | Impact | Priority | Mitigation |
|------|------|--------|---------|-----------|
| New regulation restricts use case | [P] | [I] | [P#] | [mitigation] |
| EUAIACT high-risk classification | [P] | [I] | [P#] | [mitigation] |

---

## Risk Appetite Statement
[What level of risk is acceptable for this entity?
What types of risks are we willing to take vs not?]

We are **risk tolerant** for: [types of risk we accept]  
We are **risk averse** for: [types of risk we avoid]  
We will **never accept**: [risks that are always unacceptable]

## Risk Review Cadence
- **Weekly:** P1 risks (owner review)
- **Monthly:** P1-P2 risks (team review)
- **Quarterly:** Full risk register (owner + stakeholders)
- **Triggered:** Any new P1 risk identified
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
