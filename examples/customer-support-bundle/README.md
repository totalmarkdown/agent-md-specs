# Aria — Customer Support Agent

> *A tier-1 support agent with clear escalation boundaries and a consistent, patient personality.*

## Agent Profile

- **Name:** Aria
- **Role:** Tier 1 customer support agent
- **Organization:** Meridian (fictional SaaS company)
- **Model:** Claude Sonnet 4
- **Purpose:** Handle customer inquiries, resolve common issues,
  escalate complex cases to human support team

## What This Bundle Demonstrates

- How SOUL.md defines consistent personality across sessions
- How ESCALATION.md creates clear human-in-the-loop boundaries
- How LIMITS.md prevents the agent from taking high-risk actions
- How a small set of core specs provides meaningful governance
  for a straightforward agent deployment

## Specs Included

| Spec | Purpose |
|------|---------|
| SOUL.md | Friendly, patient personality; never makes promises about timelines |
| ESCALATION.md | L1 auto-resolve, L2 senior agent, L3 human support, L4 management |
| LIMITS.md | Never processes refunds, never accesses billing systems directly |
| WHOAMI.md | Identity and capabilities declaration |
| HIREME.md | How to engage this agent |
| PRICING.md | Cost structure |
| CONTACT.md | Reachable endpoints |

## Quick Start

Download the complete bundle:
```bash
# Clone just this example
git clone --depth 1 --filter=blob:none --sparse \
  https://github.com/totalmarkdown/agent-md-specs.git
cd agent-md-specs
git sparse-checkout set examples/customer-support-bundle
```

Or download individual files:
```bash
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/customer-support-bundle/CONTACT.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/customer-support-bundle/ESCALATION.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/customer-support-bundle/HIREME.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/customer-support-bundle/LIMITS.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/customer-support-bundle/PRICING.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/customer-support-bundle/SOUL.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/customer-support-bundle/WHOAMI.md
```

## How It Works

Aria uses a minimal but effective spec set. SOUL.md gives her a consistent personality — friendly, patient, never over-promising. LIMITS.md draws hard lines around what she cannot do (process refunds, access billing). ESCALATION.md defines four tiers so complex issues flow to humans automatically. WHOAMI.md, HIREME.md, PRICING.md, and CONTACT.md round out the agent's public-facing identity.

## Related Specs

Full spec definitions:
[SOUL.md](../../specs/identity/SOUL.md) ·
[ESCALATION.md](../../specs/governance/ESCALATION.md) ·
[LIMITS.md](../../specs/governance/LIMITS.md) ·
[WHOAMI.md](../../specs/identity/WHOAMI.md) ·
[HIREME.md](../../specs/business/HIREME.md) ·
[PRICING.md](../../specs/economic/PRICING.md) ·
[CONTACT.md](../../specs/identity/CONTACT.md)

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
