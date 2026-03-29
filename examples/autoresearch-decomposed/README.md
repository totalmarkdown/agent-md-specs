# Nova — Autoresearch Decomposed Bundle

> *A monolithic agent config decomposed into standardized, reusable agent-md-specs files.*

## What This Bundle Demonstrates

- How a monolithic agent configuration file (like Karpathy's `program.md` in autoresearch, 51.9k stars) decomposes into standardized, reusable specs
- Separation of concerns: goals, constraints, workflow, output formats, escalation, and session boundaries each get their own enforceable file
- How decomposed specs can be independently validated, enforced, and reused across agents

## Monolithic → Decomposed Mapping

| Monolithic Section | agent-md-spec File | Why Separate? |
|-------------------|-------------------|---------------|
| Agent personality / philosophy | SOUL.md | Reusable across projects |
| Objectives / success metrics | GOALS.md | Independently trackable |
| Hard constraints / forbidden actions | LIMITS.md | Enforceable at runtime |
| Experiment loop / branching | WORKFLOW.md | Auditable process definition |
| Output format / logging schema | OUTPUT.md | Validates output structure |
| Error handling / stuck behavior | ESCALATION.md | Standardized safety pattern |
| Time budgets / compute limits | SESSION.md + BUDGET.md | Independently monitored |
| Validation / drift detection | ENFORCEMENT.md | Automated compliance |

## Specs Included

| Spec | Purpose |
|------|---------|
| SOUL.md | Agent personality and research philosophy |
| GOALS.md | Objectives and success metrics (validation loss targets) |
| LIMITS.md | Hard constraints and forbidden actions |
| WORKFLOW.md | Experiment loop: hypothesize, modify, train, evaluate, keep or discard |
| OUTPUT.md | Output format and logging schema |
| ESCALATION.md | Error handling and stuck-behavior patterns |
| SESSION.md | Time boundaries for experiment sessions |
| BUDGET.md | Compute and cost limits |
| ENFORCEMENT.md | Validation and drift detection |

## Quick Start

Download all specs in this bundle:
```bash
curl -LO https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/autoresearch-decomposed/bundle.zip
unzip bundle.zip -d my-agent/
```

Or clone just this example:
```bash
git clone --depth 1 --filter=blob:none --sparse \
  https://github.com/totalmarkdown/agent-md-specs.git
cd agent-md-specs
git sparse-checkout set examples/autoresearch-decomposed
```

Or download individual files:
```bash
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/autoresearch-decomposed/BUDGET.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/autoresearch-decomposed/ENFORCEMENT.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/autoresearch-decomposed/ESCALATION.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/autoresearch-decomposed/GOALS.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/autoresearch-decomposed/LIMITS.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/autoresearch-decomposed/OUTPUT.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/autoresearch-decomposed/SESSION.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/autoresearch-decomposed/SOUL.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/autoresearch-decomposed/WORKFLOW.md
```

## How It Works

Nova is an autonomous ML experimentation agent that iteratively improves a language model's validation loss within fixed compute and time budgets. It operates in a tight experiment loop: hypothesize, modify, train, evaluate, keep or discard.

The original `program.md` contains goals, constraints, workflow, output formats, escalation rules, and session boundaries in a single file. agent-md-specs separates these concerns into purpose-built specs that can be validated, enforced, and reused across agents.

## Related Specs

Full spec definitions:
[SOUL.md](../../specs/identity/SOUL.md) ·
[GOALS.md](../../specs/process/GOALS.md) ·
[LIMITS.md](../../specs/governance/LIMITS.md) ·
[WORKFLOW.md](../../specs/process/WORKFLOW.md) ·
[OUTPUT.md](../../specs/technical/OUTPUT.md) ·
[ESCALATION.md](../../specs/governance/ESCALATION.md) ·
[SESSION.md](../../specs/lifecycle/SESSION.md) ·
[BUDGET.md](../../specs/governance/BUDGET.md) ·
[ENFORCEMENT.md](../../specs/governance/ENFORCEMENT.md)

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
