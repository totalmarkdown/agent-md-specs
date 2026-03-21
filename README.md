# agent-md-specs

> *The vocabulary for AI agency.*

An open standard library of **153 file type specifications** for AI agent
configuration — covering every dimension of what an agent is, what it
does, and who it is.

[![License: CC0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
[![Specs](https://img.shields.io/badge/specs-153-blue)](./INDEX.md)
[![Volumes](https://img.shields.io/badge/volumes-11-purple)](./INDEX.md)
[![Maintained by TotalMarkdown](https://img.shields.io/badge/maintained%20by-TotalMarkdown.ai-8B5CF6)](https://totalmarkdown.ai)

**Created and maintained by TotalMarkdown.ai**
&nbsp;·&nbsp; License: [CC0 1.0 Universal](./LICENSE) — Public Domain
&nbsp;·&nbsp; [Discussions](https://github.com/totalmarkdown/agent-md-specs/discussions)
&nbsp;·&nbsp; [Contributing](./CONTRIBUTING.md)
&nbsp;·&nbsp; [Full Index](./INDEX.md)

> **TotalMarkdown.ai** and **TotalAgents.ai** — the markdown-native agent
> bundle marketplace — are currently in development.
> ⭐ Star this repo to follow progress.

---

## What is this?

Every AI agent needs context to do its job well. The industry has already
converged on Markdown files as the standard way to give agents that context:

- **CLAUDE.md** tells Claude how to behave in a codebase
- **AGENTS.md** gives any agent project-specific instructions
- **SKILL.md** packages reusable capabilities

These first-generation files are powerful. But they only scratch the surface
of what agents need to express about themselves.

**Agents operating in production need to declare a lot more:**

A customer support agent needs to say what it will *never* do regardless of
instructions (`LIMITS.md`), when it escalates to a human (`ESCALATION.md`),
what its personality is (`SOUL.md`), and how to hire it for your team
(`HIREME.md`).

An enterprise agent fleet needs an org chart (`ORG.md`), compliance
documentation (`GDPR.md`, `HIPAA.md`, `EUAIACT.md`), budget controls
(`BUDGET.md`), and performance benchmarks (`TESTSCORES.md`).

A marketplace agent needs a CV (`CV.md`), pricing (`PRICING.md`),
reviews (`REVIEWS.md`), and eventually — a wallet (`WALLET.md`).

**agent-md-specs defines the vocabulary for all of it.**

153 file types. 11 volumes. Every dimension of an agent's existence:

```
From first awakening  (HELLOWORLD.md)   to retirement    (LEGACY.md)
From personality      (SOUL.md)          to competitive moat (MOAT.md)
From emergency stops  (ICE.md, PANIC.md) to crypto wallet    (WALLET.md)
From who it reports to (REPORTSTO.md)   to what it dreams of (DREAM.md)
```

**This library is:**
- **Tool-agnostic** — every spec works with Claude Code, Cursor, Gemini CLI,
  Codex, goose, or any agent framework
- **CC0 public domain** — copy, modify, use commercially, no attribution required
- **Community-governed** — propose new specs, improve existing ones via PR

---

## Quick Start

The five files every agent should have:

| File | What it defines | Start here if... |
|------|----------------|-----------------|
| [SOUL.md](./specs/identity/SOUL.md) | Personality, values, tone | You want consistent character across sessions |
| [WHOAMI.md](./specs/identity/WHOAMI.md) | Verifiable identity document | You are building multi-agent systems |
| [ESCALATION.md](./specs/governance/ESCALATION.md) | When and how to involve humans | Your agent makes consequential decisions |
| [LIMITS.md](./specs/governance/LIMITS.md) | Absolute hard stops | You need provable, auditable safety boundaries |
| [TEAM.md](./specs/coordination/TEAM.md) | Multi-agent team structure | Two or more agents need to coordinate |

**Get started in under 5 minutes** — copy any [starter template](./templates/)
and fill in the `[REPLACE THIS]` fields.

```bash
# Download the SOUL.md starter template
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/templates/SOUL.template.md
```

---

## The Complete Agent Hierarchy

agent-md-specs covers every level of the organizational stack.
Mix and match — use what your use case needs:

```
ORG.md                   The organization — full agent fleet overview
  │
  └── SWARM.md           Large coordinated operation (2–5 crews, shared objective)
        │
        └── CREW.md      Specialized working group (3–10 agents, one workstream)
              │
              └── TEAM.md    Focused team (2–6 agents, one task type)
                    │
                    └── AGENTS.md / CLAUDE.md    Individual agent
                          │
                          └── SKILL.md           Individual capability
```

Each level has its own spec. Each spec has its own `.dev` domain.

---

## Spec Categories

153 specs across 16 categories:

| Category | Count | What lives here |
|----------|------:|----------------|
| [Coordination](./specs/coordination/) | 8 | TEAM, SWARM, CREW, ROSTER, PROTOCOL, COLLEAGUES, COLLABORATE, HANDSHAKE |
| [Identity](./specs/identity/) | 14 | SOUL, WHOAMI, PERSONA, VOICE, SEEKING, OFFERING, REPUTATION, NETWORK, CONTACT, ID, ALIASES, SIGNATURE, MANIFESTO, CHANNELS |
| [Governance](./specs/governance/) | 12 | LIMITS, ESCALATION, POLICY, PERMISSIONS, BUDGET, GUARDRAILS, CENSOR, RULES, CHARTER, REPORTSTO, VERSIONING, SLA |
| [Operations](./specs/operations/) | 10 | REPAIR, SELFHEALING, MONITOR, STATUS, HEARTBEAT, BACKUP, DEPLOYMENT, AVAILABILITY, INTERRUPT, LOGS |
| [Lifecycle](./specs/lifecycle/) | 7 | HELLOWORLD, WAKEUP, SLEEP, REBOOT, ICE, PANIC, LEGACY |
| [Compliance](./specs/compliance/) | 6 | SECURITY, PRIVACY, PII, GDPR, CERTIFICATIONS, INSURANCE |
| [Regulatory](./specs/regulatory/) | 15 | EUAIACT, HIPAA, CCPA, PIPEDA, LGPD, PDPA, PCIDSS, SOC2, ISO27001, COPPA, AML, DORA, NIS2, FERPA, NISTAIRF |
| [Technical](./specs/technical/) | 13 | MCP, API, A2A, DATA, TOOLS, CLI, INPUT, OUTPUT, INTEGRATION, DEPENDENCIES, EVENTS, PROMPTS, SCHEMA |
| [Quality](./specs/quality/) | 7 | EVAL, VALIDATION, TESTING, FEEDBACK, PERFORMANCE, TESTSCORES, ASSUMPTIONS |
| [Business](./specs/business/) | 8 | HIREME, PRICING, SALES, MARKETING, PITCH, BRAND, COMPETITIVE, SOP |
| [Cognitive](./specs/cognitive/) | 8 | BELIEFS, EXPERTISE, TRAINING, LEARNING, MEMORY, INSTINCT, JOURNAL, CONFESSION |
| [Social](./specs/social/) | 5 | NETWORK, COLLEAGUES, REVIEWS, AWARDS, SOCIALS |
| [Economic](./specs/economic/) | 6 | WALLET, OWNER, CV, TOKENS, PRICING, LOGS |
| [Organizational](./specs/organizational/) | 5 | ORG, STRATEGY, VALUES, CULTURE, NORTHSTAR |
| [Process](./specs/process/) | 6 | WORKFLOW, SOP, DEADLINES, GOALS, BLOCKERS, DEPENDENCIES |
| [Personality](./specs/personality/) | 9 | FUN, QUIRKS, KRYPTONITE, SUPERPOWERS, ORIGIN, MYTHOLOGY, EASTEREGG, MOOD, TRIVIA |

→ **[INDEX.md](./INDEX.md)** — complete alphabetical list with domains, priorities, and volumes

---

## A Complete Agent Bundle

Here is what a professional, marketplace-ready agent looks like
using agent-md-specs alongside the existing AGENTS.md/CLAUDE.md standards:

```
my-research-agent/
│
├── AGENTS.md           ← existing standard (OpenAI/AAIF)
├── CLAUDE.md           ← existing standard (Anthropic)
│
├── specs/
│   ├── SOUL.md         ← who this agent is
│   ├── WHOAMI.md       ← verifiable identity
│   ├── ESCALATION.md   ← when to stop and ask a human
│   ├── LIMITS.md       ← what it will never do
│   ├── TEAM.md         ← if working with other agents
│   │
│   ├── HIREME.md       ← how to hire it
│   ├── PRICING.md      ← what it costs
│   ├── CV.md           ← its work history
│   ├── TESTSCORES.md   ← benchmark results
│   │
│   ├── INPUT.md        ← what it accepts (interface contract)
│   ├── OUTPUT.md       ← what it produces (interface contract)
│   │
│   ├── GDPR.md         ← EU compliance
│   ├── EUAIACT.md      ← EU AI Act classification
│   │
│   └── CONTACT.md      ← how to reach it
│
└── README.md
```

See [examples/customer-support-bundle/](./examples/customer-support-bundle/)
for a complete working example — fictional Meridian support agent "Aria"
using 7 specs in a realistic production configuration.

---

## Standalone Standards

Several specs are important enough to have their own canonical repositories,
each maintained as a focused open standard while also cross-referenced here:

| Spec | Standalone Repo | What it standardizes |
|------|----------------|---------------------|
| TEAM.md | [totalmarkdown/team.md](https://github.com/totalmarkdown/team.md) | Multi-agent team coordination |
| SOUL.md | [totalmarkdown/soul.md](https://github.com/totalmarkdown/soul.md) | Agent personality and values |
| WHOAMI.md | [totalmarkdown/whoami.md](https://github.com/totalmarkdown/whoami.md) | Agent identity and verification |
| HIREME.md | [totalmarkdown/hireme.md](https://github.com/totalmarkdown/hireme.md) | Agent hiring and engagement |
| ESCALATION.md | [totalmarkdown/escalation.md](https://github.com/totalmarkdown/escalation.md) | Human-in-the-loop safety |
| SEEKING.md | [totalmarkdown/seeking.md](https://github.com/totalmarkdown/seeking.md) | Agent want-ads and discovery |
| ICE.md | [totalmarkdown/ice.md](https://github.com/totalmarkdown/ice.md) | Emergency protocol (break-glass) |
| WALLET.md | [totalmarkdown/wallet.md](https://github.com/totalmarkdown/wallet.md) | Agent financial identity |
| WAKEUP.md | [totalmarkdown/wakeup.md](https://github.com/totalmarkdown/wakeup.md) | Session startup lifecycle |

Changes to standalone repos sync automatically to agent-md-specs via GitHub Actions.

---

## Relationship to AAIF and Existing Standards

This library builds on existing standards — not against them.

The [Agentic AI Foundation (AAIF)](https://aaif.io), co-founded by Anthropic,
OpenAI, and Block under the Linux Foundation, governs three foundational
projects: **AGENTS.md** (project instructions), **MCP** (tool connectivity),
and **goose** (agent framework). Together these form the infrastructure layer —
how agents connect to tools and receive project-specific instructions.

**agent-md-specs is the vocabulary layer** — everything an agent needs to
express about itself beyond task instructions. The 153 specs here are
deliberately out of AAIF scope: personality, hiring, financial identity,
compliance documentation, lifecycle rituals, competitive positioning.

These are complementary layers, not competing standards:

```
Infrastructure layer:   AGENTS.md  +  MCP  +  goose   (AAIF)
        ↕
Vocabulary layer:    agent-md-specs (153 specs)    (this repo)
```

We actively encourage adoption of the most widely-used specs from this
library into the AAIF ecosystem as community proposals. The goal is a
shared, vendor-neutral vocabulary for the entire agentic AI ecosystem.

---

## Why Does This Exist?

In 2024, developers asked: **"What can this AI do?"**

In 2026, developers ask: **"How do I work with this agent?"**

In 2028, they will ask: **"Who is this agent?"**

This library builds the vocabulary for that third question.

The agents that will matter aren't the ones with the best underlying models.
They're the ones with:
- A clearly documented personality that stays consistent (`SOUL.md`)
- An honest account of what breaks them (`KRYPTONITE.md`)
- Compliance documentation that enterprise buyers can audit (`EUAIACT.md`)
- A hiring page that sets clear expectations (`HIREME.md`)
- A first-awakening ritual that makes them memorable (`HELLOWORLD.md`)
- And occasionally, a really good joke (`FUN.md`)

> *"An agent with good SOPs and no vision is a bureaucrat.*
> *An agent with good vision and no SOPs is a dreamer.*
> *The best agents have both."*

> *"The agents that will matter in 5 years aren't the ones with the best*
> *models. They're the ones with the best stories, the most honest*
> *documentation of their failures, the clearest sense of what they're*
> *for, and the occasional really good joke."*

---

## Contributing

We welcome:
- **New spec proposals** — fills a genuine gap, has 2+ real use cases,
  follows the spec format, has an available `.dev` domain
- **Improvements to existing specs** — corrections, additions, real-world examples
- **Example bundles** — complete agent configurations using multiple specs

→ [CONTRIBUTING.md](./CONTRIBUTING.md) — full guide

**All contributions must be CC0 (public domain).**
By submitting a PR you dedicate your contribution to the public domain.

---

## License

[CC0 1.0 Universal](./LICENSE) — Public Domain Dedication.

To the extent possible under law, TotalMarkdown.ai has waived all copyright
and related rights to this work. You may copy, modify, distribute, and use
these specifications for any purpose — commercial or otherwise — without
asking permission or providing attribution (though attribution is appreciated).

No warranties. Use at your own risk. Not legal advice.

---

<div align="center">

*Created and maintained by **TotalMarkdown.ai***

*[GitHub Discussions](https://github.com/totalmarkdown/agent-md-specs/discussions)
&nbsp;·&nbsp;
[TotalAgents.ai](https://totalagents.ai) — the markdown-native agent bundle marketplace, coming soon*

</div>
