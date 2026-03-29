# Sentinel — Multi-Agent Fleet Bundle

> *A 3-agent financial data pipeline governed entirely by human-readable Markdown specs.*

Most multi-agent frameworks (CrewAI, LangGraph, AutoGen) define agent coordination in code — buried in Python classes, YAML configs, or graph definitions. When something goes wrong, auditing behavior means reading source code. Non-technical stakeholders (compliance, management) can't review what agents are allowed to do.

agent-md-specs solves this with a layered, human-readable structure:

- **TEAM.md** defines the crew: members, pipeline order, handoff protocol, shared constraints
- **Individual agent specs** (SOUL.md, LIMITS.md, INPUT.md, OUTPUT.md) define each agent's personality, boundaries, and data contracts
- **Shared governance** (BUDGET.md, ESCALATION.md, DELEGATION.md) captures org-level policies that apply across the crew

The framework loader reads these specs at agent initialization. Changes to behavior are pull requests, not code deploys. Git history becomes a full audit trail of what each agent was permitted to do and when.

## What This Bundle Demonstrates

- How TEAM.md orchestrates a multi-agent pipeline with defined handoff protocols
- Per-agent specs (SOUL.md, LIMITS.md, INPUT.md, OUTPUT.md) giving each agent its own identity, constraints, and data contracts
- Shared governance specs that apply org-level policies across the entire crew
- How non-technical stakeholders can review and approve agent behavior via Markdown files

## Specs Included

| Spec | Location | Purpose |
|------|----------|---------|
| TEAM.md | root | Crew definition, pipeline order, handoff protocol |
| SOUL.md | agents/scout/ | Scout personality and data collection philosophy |
| LIMITS.md | agents/scout/ | Scout boundaries and forbidden actions |
| INPUT.md | agents/scout/ | Scout input data contracts |
| OUTPUT.md | agents/scout/ | Scout output data contracts |
| SOUL.md | agents/analyst/ | Analyst personality and analysis approach |
| LIMITS.md | agents/analyst/ | Analyst boundaries and forbidden actions |
| INPUT.md | agents/analyst/ | Analyst input data contracts |
| OUTPUT.md | agents/analyst/ | Analyst output data contracts |
| SOUL.md | agents/scribe/ | Scribe personality and reporting style |
| LIMITS.md | agents/scribe/ | Scribe boundaries and forbidden actions |
| INPUT.md | agents/scribe/ | Scribe input data contracts |
| OUTPUT.md | agents/scribe/ | Scribe output data contracts |
| BUDGET.md | shared/ | Crew-wide compute and cost limits |
| CIRCUITBREAKER.md | shared/ | Crew-wide failure containment |
| DELEGATION.md | shared/ | Crew-wide authority chain |
| ESCALATION.md | shared/ | Crew-wide escalation paths |

## Directory Structure

```
TEAM.md                    # Crew definition and pipeline
agents/scout/              # Data collection agent
agents/analyst/            # Analysis agent
agents/scribe/             # Report generation agent
shared/                    # Crew-wide governance
```

## Quick Start

Download all specs in this bundle:
```bash
curl -LO https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/multi-agent-fleet/bundle.zip
unzip bundle.zip -d my-agent/
```

Or clone just this example:
```bash
git clone --depth 1 --filter=blob:none --sparse \
  https://github.com/totalmarkdown/agent-md-specs.git
cd agent-md-specs
git sparse-checkout set examples/multi-agent-fleet
```

Or download individual files:
```bash
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/multi-agent-fleet/TEAM.md
# Scout agent
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/multi-agent-fleet/agents/scout/INPUT.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/multi-agent-fleet/agents/scout/LIMITS.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/multi-agent-fleet/agents/scout/OUTPUT.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/multi-agent-fleet/agents/scout/SOUL.md
# Analyst agent
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/multi-agent-fleet/agents/analyst/INPUT.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/multi-agent-fleet/agents/analyst/LIMITS.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/multi-agent-fleet/agents/analyst/OUTPUT.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/multi-agent-fleet/agents/analyst/SOUL.md
# Scribe agent
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/multi-agent-fleet/agents/scribe/INPUT.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/multi-agent-fleet/agents/scribe/LIMITS.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/multi-agent-fleet/agents/scribe/OUTPUT.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/multi-agent-fleet/agents/scribe/SOUL.md
# Shared governance
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/multi-agent-fleet/shared/BUDGET.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/multi-agent-fleet/shared/CIRCUITBREAKER.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/multi-agent-fleet/shared/DELEGATION.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/multi-agent-fleet/shared/ESCALATION.md
```

## How It Works

This bundle implements a 3-agent financial data pipeline at a hedge fund:

1. **Scout** collects raw financial data from external sources, validates data quality, and passes structured output to the next stage
2. **Analyst** receives Scout's output, performs financial analysis, and produces structured findings
3. **Scribe** takes the Analyst's findings and generates human-readable reports

Every spec is a plain Markdown file that a Portfolio Manager, compliance officer, or auditor can read, review, and approve — no code knowledge required. TEAM.md defines the pipeline order and handoff protocol. Shared governance specs (BUDGET.md, ESCALATION.md, DELEGATION.md, CIRCUITBREAKER.md) apply across all three agents.

## Related Specs

Full spec definitions:
[TEAM.md](../../specs/coordination/TEAM.md) ·
[SOUL.md](../../specs/identity/SOUL.md) ·
[LIMITS.md](../../specs/governance/LIMITS.md) ·
[INPUT.md](../../specs/technical/INPUT.md) ·
[OUTPUT.md](../../specs/technical/OUTPUT.md) ·
[BUDGET.md](../../specs/governance/BUDGET.md) ·
[CIRCUITBREAKER.md](../../specs/operations/CIRCUITBREAKER.md) ·
[DELEGATION.md](../../specs/governance/DELEGATION.md) ·
[ESCALATION.md](../../specs/governance/ESCALATION.md)

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
