# Codex Agent Decomposed

AGENTS.md (60,000+ repos, AAIF standard) tells agents how to work on
a specific project. But production agents need to express much more:
who they are, what they're authorized to do, how they prove their
identity, and how their actions are audited.

This example shows a code review agent ("Forge") that uses AGENTS.md
for project context alongside agent-md-specs for identity, governance,
and accountability.

## How They Work Together

```
AGENTS.md              agent-md-specs
(project context)      (everything else about the agent)
┌──────────────┐       ┌────────────────────────┐
│ Build cmds   │       │ SOUL.md — personality   │
│ Test cmds    │       │ WHOAMI.md — identity     │
│ Code style   │       │ DELEGATION.md — authority│
│ PR rules     │       │ LIMITS.md — hard stops   │
│ Lint config  │       │ ESCALATION.md — safety   │
└──────────────┘       │ AUDITTRAIL.md — records  │
                       │ ENFORCEMENT.md — verify  │
                       └────────────────────────┘
```

AGENTS.md answers: "How should you work on this codebase?"
agent-md-specs answers: "Who are you, and what are you allowed to do?"

## The Agent: Forge

Forge v3.2 is a code review and deployment agent owned by the DevOps
team at TechCo. It reviews PRs, runs CI pipelines, and deploys to
staging — but never to production without human approval.

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
