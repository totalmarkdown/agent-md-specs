# Forge — Code Review & Deployment Agent

> *A code review agent that uses AGENTS.md for project context alongside agent-md-specs for identity, governance, and accountability.*

## What This Bundle Demonstrates

- How AGENTS.md (60,000+ repos, AAIF standard) and agent-md-specs complement each other
- AGENTS.md answers "How should you work on this codebase?" while agent-md-specs answers "Who are you, and what are you allowed to do?"
- How a code review agent gets governed without interfering with project-level configuration

## How They Work Together

```
AGENTS.md              agent-md-specs
(project context)      (everything else about the agent)
┌──────────────┐       ┌──────────────────────────┐
│ Build cmds   │       │ SOUL.md — personality    │
│ Test cmds    │       │ WHOAMI.md — identity     │
│ Code style   │       │ DELEGATION.md — authority│
│ PR rules     │       │ LIMITS.md — hard stops   │
│ Lint config  │       │ ESCALATION.md — safety   │
└──────────────┘       │ AUDITTRAIL.md — records  │
                       │ ENFORCEMENT.md — verify  │
                       └──────────────────────────┘
```

## Specs Included

| Spec | Purpose |
|------|---------|
| AGENTS.md | Project-level context: build commands, test commands, code style, PR rules |
| SOUL.md | Agent personality and review philosophy |
| WHOAMI.md | Identity declaration for Forge v3.2 |
| DELEGATION.md | Authority chain from DevOps team |
| LIMITS.md | Hard stops — never deploys to production without human approval |
| ESCALATION.md | Safety escalation paths |
| AUDITTRAIL.md | Records of all review and deployment actions |
| ENFORCEMENT.md | Compliance verification |

## Quick Start

Download all specs in this bundle:
```bash
curl -LO https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/codex-agent-decomposed/bundle.zip
unzip bundle.zip -d my-agent/
```

Or clone just this example:
```bash
git clone --depth 1 --filter=blob:none --sparse \
  https://github.com/totalmarkdown/agent-md-specs.git
cd agent-md-specs
git sparse-checkout set examples/codex-agent-decomposed
```

Or download individual files:
```bash
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/codex-agent-decomposed/AGENTS.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/codex-agent-decomposed/AUDITTRAIL.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/codex-agent-decomposed/DELEGATION.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/codex-agent-decomposed/ENFORCEMENT.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/codex-agent-decomposed/ESCALATION.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/codex-agent-decomposed/LIMITS.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/codex-agent-decomposed/SOUL.md
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/codex-agent-decomposed/WHOAMI.md
```

## How It Works

Forge v3.2 is a code review and deployment agent owned by the DevOps team at TechCo. It reviews PRs, runs CI pipelines, and deploys to staging — but never to production without human approval.

AGENTS.md tells Forge how to work on the codebase (build commands, test suites, lint rules, PR conventions). agent-md-specs tells Forge who it is (WHOAMI.md, SOUL.md), what authority it has (DELEGATION.md), what it must never do (LIMITS.md), how to escalate problems (ESCALATION.md), and how every action gets recorded (AUDITTRAIL.md, ENFORCEMENT.md).

## Related Specs

Full spec definitions:
[SOUL.md](../../specs/identity/SOUL.md) ·
[WHOAMI.md](../../specs/identity/WHOAMI.md) ·
[DELEGATION.md](../../specs/governance/DELEGATION.md) ·
[LIMITS.md](../../specs/governance/LIMITS.md) ·
[ESCALATION.md](../../specs/governance/ESCALATION.md) ·
[AUDITTRAIL.md](../../specs/compliance/AUDITTRAIL.md) ·
[ENFORCEMENT.md](../../specs/governance/ENFORCEMENT.md)

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
