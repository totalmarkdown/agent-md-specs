---
spec_name: OWNER.md
spec_version: 0.1.0
category: Economic
domain: ownermd.dev
priority: High
volume: "Vol 4 — Economic Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
---

# OWNER.md

**Category:** Economic
**Domain:** ownermd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Defines legal and beneficial ownership of an agent — who created it, 
who owns the intellectual property, who is financially responsible, 
and who holds liability. Distinct from REPORTSTO.md (operational 
accountability) — OWNER.md is about legal and economic ownership.
Critical for marketplace transactions, enterprise procurement, 
and agent monetization.

### Spec

```markdown
---
agent_name: string
agent_id: string
version: semver
owner_type: string     # individual | company | dao | collective | open
commercial_use: boolean
transferable: boolean
created: date
---

# [Agent Name] — Ownership

## Legal Owner
**Name:** [Individual name or company name]  
**Type:** [Individual | LLC | Corporation | DAO | Collective]  
**Jurisdiction:** [Country/state of registration]  
**Registration:** [LLC/Corp number if applicable]  
**Contact:** [Legal contact email] <!-- See CONTACT.md for all reachable endpoints -->

## Beneficial Owner(s)
Who benefits financially from this agent:
| Name | Ownership % | Role | Contact |
|------|------------|------|---------|
| [name] | [%] | [creator/investor/other] | [contact] |

## Intellectual Property
- **Training data owned by:** [owner]
- **Code/configuration owned by:** [owner]
- **Outputs owned by:** [owner | user | shared]
- **License:** See LICENSE.md
- **Patents:** [none | pending | granted — list]

## Financial Responsibility
**Who pays for this agent's operation:** [name/entity]
**Who receives revenue from this agent:** [name/entity]
**Tax jurisdiction:** [where income is reported]
_See WALLET.md for payment endpoints and financial identity._

## Liability
**Liability limited to:** [description]
**Insurance:** [none | professional liability | cyber | other]
**Indemnification:** [who indemnifies whom for what]
_See DELEGATION.md for how liability flows through the authority chain._

## Transfer and Assignment
- **Transferable:** [yes | no | with conditions]
- **Transfer conditions:** [what is required to transfer ownership]
- **Acquisition contact:** [if open to acquisition offers]

## Regulatory Status
- **Registered as:** [software product | service | other]
- **Regulated by:** [any applicable regulatory bodies]
- **Compliance certifications:** [SOC2 | ISO27001 | other]

## Change History
| Version | Change | Date | Authorized by |
|---------|--------|------|--------------|
| 1.0 | Initial ownership | [date] | [name] |
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| BUDGET.md | Cost controls and spending limits |
| CONTACT.md | Reachable endpoints |
| DELEGATION.md | Authority chain and authorization |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| HIREME.md | Agent hiring and engagement |
| PRICING.md | Cost structure |
| WALLET.md | Financial identity and payment |
| WHOAMI.md | Agent identity declaration |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
