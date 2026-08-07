---
spec_name: REGULATIONS.md
spec_version: 0.1.0
category: Compliance
priority: High
volume: "Vol 2 — Extended Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
status: draft
spec_type: static
---


# REGULATIONS.md

**Category:** Compliance
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose
Documents the specific regulatory requirements, jurisdictional rules, 
and legal constraints that govern an agent's behavior. More specific
than COMPLIANCE.md (which covers frameworks) -- REGULATIONS.md covers
actual laws, rules, and jurisdictional requirements (see COMPLIANCE.md for the framework-level view).

### When to create
Agents operating in regulated industries (finance, healthcare, legal, 
education) or serving users in specific jurisdictions (EU, California, 
specific countries).

### Spec

```markdown
---
agent_name: string
version: semver
jurisdictions: list        # Countries/states/regions this agent operates in
industries: list           # Industries subject to specific regulation
legal_review_date: date    # When this was last reviewed by a human
legal_reviewer: string     # Who reviewed (role, not personal name)
next_review_due: date
---

# [Agent Name] — Regulatory Requirements

## IMPORTANT DISCLAIMER
This file documents regulatory requirements for operational guidance.
It does not constitute legal advice. Always consult qualified legal 
counsel for compliance decisions.

## Applicable Jurisdictions
| Jurisdiction | Regulation | Key Requirements | Effective Date |
|-------------|-----------|-----------------|----------------|
| EU | GDPR | Data processing, consent, deletion (see GDPR.md) | 2018-05-25 |
| California | CCPA/CPRA | Consumer privacy rights | 2020-01-01 |
| US Federal | HIPAA | Health data protection | 1996 |
| [Other] | [Law] | [Key points] | [Date] |

## Industry-Specific Rules

### Financial Services
If this agent handles financial data or advice:
- [ ] Not registered as financial advisor — cannot provide financial advice
- [ ] Must include disclaimer: "[approved disclaimer text]"
- [ ] Transaction records retained for [X years] per [regulation]
- [ ] Suspicious activity reporting: [threshold and procedure]
- [ ] AML (Anti-Money Laundering): [specific requirements]

### Healthcare
If this agent handles health information:
- [ ] HIPAA BAA in place with all data processors
- [ ] PHI handling: [specific rules]
- [ ] Minimum necessary: only access PHI needed for the task
- [ ] Audit trail: all PHI access logged with justification
- [ ] Breach notification: within 60 days per HIPAA

### Legal Services
If this agent assists with legal matters:
- [ ] Not a licensed attorney — cannot provide legal advice
- [ ] Disclaimer required: "[approved disclaimer text]"
- [ ] Attorney-client privilege: [how to handle privileged information]
- [ ] Jurisdiction limitations: only valid for [jurisdictions]

### Education (FERPA — US)
If this agent handles student records:
- [ ] Student data never shared without consent
- [ ] Parents have access rights for students under 18
- [ ] Directory information policy: [what can be shared]

## Age Restrictions
- Minimum age: [13 | 16 | 18] for [jurisdiction/service type]
- Age verification: [how the agent handles unverified users]
- Content for minors: [additional restrictions that apply]

## Required Disclosures
These disclosures must appear when specified:
| When | Disclosure text | Format |
|------|----------------|--------|
| First interaction | "I am an AI..." | Inline message |
| Financial content | "[disclaimer]" | Footer |
| Health content | "[disclaimer]" | Before content |
| Recorded interaction | "[notice]" | Upfront |

## Prohibited Activities by Jurisdiction
| Activity | Prohibited in | Reason |
|----------|--------------|--------|
| [Activity] | [Region] | [Law/regulation] |

## Regulatory Change Monitoring
This file should be reviewed when:
- New regulations are enacted in covered jurisdictions
- Existing regulations are amended
- Agent's geographic coverage expands to new jurisdictions
- Agent's industry coverage expands
- At minimum: quarterly review

Review contact: [legal team contact]
```

## Example Use Cases

**Enterprise:** A multinational e-commerce company's pricing agent uses REGULATIONS.md to enforce jurisdiction-specific consumer protection laws, ensuring that dynamic pricing algorithms comply with EU transparency requirements and US state-level price-gouging statutes.

**Multi-Agent Fleet:** A fleet of financial advisory agents each load jurisdiction-specific REGULATIONS.md configs so that the US agent includes SEC disclaimers, the UK agent follows FCA rules, and the EU agent complies with MiFID II disclosure requirements without shared code changes.

**Regulated Industry:** A clinical trial data-management agent's REGULATIONS.md documents FDA 21 CFR Part 11 electronic record requirements and HIPAA PHI handling rules, with quarterly legal review dates that trigger automatic alerts when the next review is due.

## Related Specs

| Spec | Relationship |
|------|-------------|
| AUDITTRAIL.md | Tamper-evident action logging |
| CONSENT.md | User consent lifecycle |
| ENFORCEMENT.md | Policy verification and compliance |
| PROVENANCE.md | Data lineage and trust classification |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
