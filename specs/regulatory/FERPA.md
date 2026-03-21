---
spec_name: FERPA.md
spec_version: 0.1.0
category: Regulatory Compliance
domain: ferpamd.dev
priority: Medium
volume: "Vol 9 — Guardrails & Regulatory Compliance Library"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# FERPA.md

**Category:** Regulatory Compliance
**Domain:** ferpamd.dev
**Priority:** Medium
**Version:** 0.1.0

**Priority:** MEDIUM — education sector  
**Regulation:** Family Educational Rights and Privacy Act (US)  
**Version:** 0.1.0

```markdown
---
agent_name: string
version: semver
ferpa_applicable: boolean
institution_type: string    # K12 | higher-ed | edtech-vendor
receives_federal_funding: boolean
last_reviewed: date
---

# [Agent Name] — FERPA Compliance

## Applicability
FERPA applies to educational agencies and institutions 
that receive federal funding. EdTech vendors become 
subject when acting as "school officials."

**Institution type:** [K-12 | Higher Education | EdTech vendor]  
**Federal funding received:** [Yes | No]  
**Acting as school official:** [Yes | No]

## Education Records
FERPA protects "education records" — directly related to a 
student and maintained by the institution.

**Education records this agent handles:**
- [ ] Grades and transcripts
- [ ] Class schedules
- [ ] Financial aid information
- [ ] Disciplinary records
- [ ] Student ID numbers
- [ ] Directory information

## Parent and Student Rights

| Right | Who holds it | Age threshold |
|-------|-------------|--------------|
| Inspect and review records | Parents | Transfer to student at 18 |
| Request amendment | Parents | Transfer to student at 18 |
| Consent to disclosure | Parents | Transfer to student at 18 |
| File complaint with Dept of Ed | Parents | Transfer to student at 18 |

## Disclosure Rules
Education records may only be disclosed without consent to:
- [ ] School officials with legitimate educational interest
- [ ] Other schools student is transferring to
- [ ] Specified officials for audit/evaluation
- [ ] In connection with financial aid
- [ ] State/local authorities per state statute
- [ ] Accrediting organizations
- [ ] Parents of dependent student
- [ ] Comply with judicial order/subpoena
- [ ] Health/safety emergency
- [ ] Directory information (unless opt-out)

## Directory Information
May be disclosed without consent unless student opts out:  
**Designated directory info:** [list what institution has designated]  
**Opt-out process:** [how students/parents opt out]

## Data Security
Education records must be:
- [ ] Stored securely with access controls
- [ ] Access logged
- [ ] Shared only with authorized parties
- [ ] Deleted per institution retention policy

## Vendor Obligations (School Official)
If acting as school official under DUSA/agreement:
- [ ] Written agreement with institution in place
- [ ] Use data only for purpose specified
- [ ] No re-disclosure without consent
- [ ] Return or destroy data when agreement ends
- [ ] Maintain data security

## Penalties
Loss of federal funding for institution  
(Direct enforcement against vendors is limited — 
institution bears liability for vendor violations)
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
