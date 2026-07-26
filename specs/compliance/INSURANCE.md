---
spec_name: INSURANCE.md
spec_version: 0.1.0
category: Legal
priority: Low
volume: "Vol 5 — Organizational & Validation"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---


# INSURANCE.md

**Category:** Legal
**Priority:** Low
**Version:** 0.1.0 **Type:** Static

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
_See COMPLIANCE.md for the regulatory obligations that inform coverage requirements._

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

## Example Use Cases

**Enterprise:** An enterprise buyer requires proof of $5M professional liability coverage before allowing an AI agent to process financial reconciliation tasks; INSURANCE.md provides the coverage summary and certificate-of-insurance request process in a standard format.

**Multi-Agent Fleet:** A platform operator uses INSURANCE.md across their fleet to verify that every agent handling customer data carries cyber liability insurance, flagging any uninsured agents before they are promoted to production.

**Regulated Industry:** A legal technology company's contract-drafting agent publishes INSURANCE.md with errors-and-omissions coverage details, giving law firms confidence that financial recourse exists if the agent produces a materially flawed contract clause.

## Related Specs

| Spec | Relationship |
|------|-------------|
| AUDITTRAIL.md | Tamper-evident action logging |
| CONSENT.md | User consent lifecycle |
| ENFORCEMENT.md | Policy verification and compliance |
| LIMITS.md | Hard constraints and safety boundaries |
| PROVENANCE.md | Data lineage and trust classification |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
