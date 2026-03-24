# Autoresearch Decomposed

This example shows how a monolithic agent configuration file (like
Karpathy's `program.md` in autoresearch, 51.9k stars) decomposes into
standardized, reusable agent-md-specs files.

The original `program.md` contains goals, constraints, workflow, output
formats, escalation rules, and session boundaries in a single file.
agent-md-specs separates these concerns into purpose-built specs that
can be validated, enforced, and reused across agents.

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

## The Agent: Nova

Nova is an autonomous ML experimentation agent that iteratively improves
a language model's validation loss within fixed compute and time budgets.
It operates in a tight experiment loop: hypothesize, modify, train,
evaluate, keep or discard.

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
