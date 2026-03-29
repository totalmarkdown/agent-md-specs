---
spec_name: COPPA.md
spec_version: 0.1.0
category: Regulatory Compliance
domain: coppamd.dev
priority: High
volume: "Vol 9 — Guardrails & Regulatory Compliance Library"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---


# COPPA.md

**Category:** Regulatory Compliance
**Domain:** coppamd.dev
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose

Configures compliance with COPPA for agents that interact with or collect data from children under 13, covering verifiable parental consent, privacy notice requirements, and prohibited data practices. This spec protects organizations from FTC enforcement actions with penalties exceeding $50,000 per violation per day.

```markdown
---
agent_name: string
version: semver
coppa_applicable: boolean
directed_to_children: boolean   # Is this agent directed at children?
actual_knowledge_children: boolean  # Do you have actual knowledge of children using it?
minimum_age: number             # Minimum age for this service
verifiable_parental_consent: boolean
---

# [Agent Name] — COPPA Compliance

## Applicability
COPPA applies to operators of websites/online services directed 
to children under 13, OR who have actual knowledge they are 
collecting personal information from children under 13.

**Is this service directed to children?** [Yes | No | Mixed audience]  
**Minimum age requirement:** [13 | 16 | 18 | other]  
**Age verification method:** [how age is verified]

## What COPPA Requires

### Verifiable Parental Consent
Required BEFORE collecting personal info from children under 13 (see CONSENT.md for consent lifecycle tracking).

**Consent method:** [one of the following]
- [ ] Signed consent form (mail/fax)
- [ ] Credit card verification
- [ ] Parent call to toll-free number
- [ ] Video conference with trained personnel
- [ ] Government ID verification
- [ ] Knowledge-based authentication
- [ ] Facial recognition match to ID

### Privacy Notice Requirements
Must post clear, comprehensive privacy policy including:
- [ ] What information is collected from children
- [ ] How information is used
- [ ] Disclosure practices
- [ ] Parent rights

**Privacy policy for children:** [URL]  
**Written in language children can understand:** [yes/no]

### Parent Rights
Parents can:
- Review personal information collected from their child
- Revoke consent and request deletion
- Refuse further collection or use
- Not required to consent to more than necessary

**Parent request process:** [process]  
**Response time:** [timeframe]

## Data Practices for Children
- Collect only what necessary
- No behavioral advertising to children
- No sharing with third parties (with limited exceptions)
- No retention beyond necessary
- Reasonable security measures

## Prohibited
- Conditioning participation on disclosure of more info than necessary
- Marketing/advertising to children based on their data
- Third-party behavioral tracking without parental consent

## Penalties
$51,744 per violation per day (adjusted for inflation)  
FTC enforcement  
State AGs can also enforce

_See AUDITTRAIL.md for logging all parental consent verifications._

## If Not Directed to Children
Steps taken to avoid collecting children's data:
- [Age gate method]
- [What happens when underage user identified]
- [Deletion process for inadvertently collected children's data]
```

## Example Use Cases

**Enterprise:** An educational gaming platform uses COPPA.md to configure its tutoring agent with age-gating at sign-up, requiring verifiable parental consent via credit card verification before collecting any child's name or progress data.

**Multi-Agent Fleet:** A children's content platform ensures all agents in its fleet reference COPPA.md rules to block behavioral advertising tools and prevent third-party tracking cookies from being set for users under 13.

**Regulated Industry:** An edtech company uses COPPA.md to mandate immediate deletion of inadvertently collected children's data when an underage user is detected, logging the deletion event for FTC audit readiness.

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
