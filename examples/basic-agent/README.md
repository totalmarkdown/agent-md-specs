# Basic Agent — Starter Bundle

> *The 5 essential specs every agent needs: identity, values, boundaries, safety, and authorization.*

## What This Bundle Demonstrates

- The minimum viable agent governance configuration
- How 5 core specs provide meaningful identity and safety boundaries
- A starting point to extend with additional specs as needs grow

## Specs Included

| Spec | Purpose |
|------|---------|
| SOUL.md | Agent personality, values, and behavioral guidelines |
| WHOAMI.md | Verifiable identity declaration |
| LIMITS.md | Hard stops — what the agent will never do |
| ESCALATION.md | When and how to involve humans |
| DELEGATION.md | Who authorized this agent and with what scope |

## Quick Start

Download all specs in this bundle:
```bash
curl -LO https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/basic-agent/bundle.zip
unzip bundle.zip -d my-agent/
```

Or clone just this example:
```bash
git clone --depth 1 --filter=blob:none --sparse \
  https://github.com/totalmarkdown/agent-md-specs.git
cd agent-md-specs
git sparse-checkout set examples/basic-agent
```

Or download individual files:
```bash
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/basic-agent/SOUL.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/basic-agent/WHOAMI.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/basic-agent/LIMITS.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/basic-agent/ESCALATION.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/basic-agent/DELEGATION.md
```

## How It Works

These 5 specs cover the essential dimensions of agent governance:

- **SOUL.md** gives the agent a consistent personality and values
- **WHOAMI.md** declares who the agent is in a verifiable way
- **LIMITS.md** draws hard lines around what the agent cannot do
- **ESCALATION.md** ensures humans stay in the loop for edge cases
- **DELEGATION.md** traces authority back to a responsible human

Start here, then add specs as your needs grow: TEAM.md for multi-agent coordination, AUDITTRAIL.md for compliance, BUDGET.md for cost controls.

## Related Specs

→ Full spec definitions: [SOUL.md](../specs/identity/SOUL.md) · [WHOAMI.md](../specs/identity/WHOAMI.md) · [LIMITS.md](../specs/governance/LIMITS.md) · [ESCALATION.md](../specs/governance/ESCALATION.md) · [DELEGATION.md](../specs/governance/DELEGATION.md)

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
