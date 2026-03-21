---
spec_name: INSURANCE.md
spec_version: 0.1.0
category: Legal
domain: insurancemd.dev
priority: Low
volume: "Vol 5 — Organizational & Validation"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# INSURANCE.md

**Category:** Legal
**Domain:** insurancemd.dev
**Priority:** Low
**Version:** 0.1.0

**Priority:** LOW now — HIGH for enterprise  
**Version:** 0.1.0

### Purpose
Insurance and liability coverage for an agent or agent fleet.
As agents become economic actors handling consequential tasks,
enterprise buyers will require proof of insurance coverage.
The agent's liability documentation.

### Spec

```markdown
---
agent_name: string
version: semver
insured: boolean
insurance_provider: string
policy_number: string  # Redacted in public version
last_updated: date
---

# [Agent Name] — Insurance & Liability

## Coverage Summary
**Insured:** [Yes | No]  
**Provider:** [Insurance company]  
**Coverage type:** [Professional liability | Cyber | E&O | Other]  
**Coverage amount:** $[X] per incident / $[X] aggregate  
**Valid until:** [Date]  
**Certificate:** [Available on request | Link to certificate]

## What's Covered
- [Coverage type 1]: up to $[X]
- [Coverage type 2]: up to $[X]
- [Errors and omissions]: [coverage details]
- [Data breach/cyber]: [coverage details]

## What's NOT Covered
- Intentional misconduct
- [Specific exclusion]
- Losses resulting from violating LIMITS.md

## Liability Limits
**Maximum liability per incident:** $[X]  
**Maximum aggregate liability:** $[X]  
**Limitation period:** [X years]

## Claims Process
To file a claim:
1. Contact: [claims contact]
2. Within: [X days] of incident
3. Documentation required: [list]

## For Enterprise Buyers
Additional coverage options:
- Higher limits: [contact for quote]
- Custom riders: [contact]
- Named insured: [available for Enterprise tier]

## Certificate of Insurance
Request COI: [contact]  
Format available: [PDF | ACORD form]  
Turnaround: [X business days]
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
