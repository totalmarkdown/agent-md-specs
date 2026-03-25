# agent-md-specs

> *A vocabulary for AI agency.*

A proposed open standard library of **178 file type specifications** for AI agent
configuration — covering every dimension of what an agent is, what it
does, and who it is.

[![License: CC0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
[![Specs](https://img.shields.io/badge/specs-178-blue)](./INDEX.md)
[![Volumes](https://img.shields.io/badge/volumes-16-purple)](./INDEX.md)
[![Maintained by TotalMarkdown](https://img.shields.io/badge/maintained%20by-TotalMarkdown.ai-8B5CF6)](https://totalmarkdown.ai)

**Created and maintained by TotalMarkdown.ai**
&nbsp;·&nbsp; License: [CC0 1.0 Universal](./LICENSE) — Public Domain
&nbsp;·&nbsp; [Discussions](https://github.com/totalmarkdown/agent-md-specs/discussions)
&nbsp;·&nbsp; [Contributing](./CONTRIBUTING.md)
&nbsp;·&nbsp; [Full Index](./INDEX.md)
&nbsp;·&nbsp; [NIST Crosswalk](./NIST_CROSSWALK.md)
&nbsp;·&nbsp; [JSON Schemas](./schemas/)
&nbsp;·&nbsp; [Spec Lifecycle](./SPEC_LIFECYCLE.md)
&nbsp;·&nbsp; [Changelog](./CHANGELOG.md)

> **TotalMarkdown.ai** (the markdown-native workspace for agent configuration) &
> **TotalAgents.ai** (the markdown-native agent bundle marketplace)
> are currently in development.
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

**agent-md-specs proposes a vocabulary for all of it.**

178 file types. 16 volumes. 17 categories. 44 Core + 134 Extended.

```
From first awakening  (HELLOWORLD.md)   to retirement    (LEGACY.md)
From personality      (SOUL.md)          to competitive moat (MOAT.md)
From emergency stops  (ICE.md, PANIC.md) to crypto wallet    (WALLET.md)
From who it reports to (REPORTSTO.md)   to what it dreams of (DREAM.md)
```

**This library aims to be:**
- **Tool-agnostic** — every spec works with Claude Code, Cursor, Gemini CLI,
  Codex, goose, or any agent framework
- **CC0 public domain** — copy, modify, use commercially, no attribution required
- **Community-driven** — propose new specs, improve existing ones via PR

---

## The Pattern Already Exists — We're Standardizing It

The markdown-as-agent-configuration pattern has already been adopted
across the AI industry — but without standardization, every tool
reinvents the vocabulary:

| Tool / Project | Config File | Stars/Adoption | What It Configures |
|---------------|-------------|----------------|-------------------|
| OpenAI Codex | `AGENTS.md` | 60,000+ repos | Project instructions for coding agents |
| Anthropic Claude Code | `CLAUDE.md` | Ecosystem standard | Agent behavior in codebases |
| Anthropic Claude Code | `SKILL.md` | Ecosystem standard | Reusable agent capabilities |
| Karpathy autoresearch | `program.md` | 51,900+ stars | Autonomous ML research agent |
| Cursor | `.cursorrules` | Ecosystem standard | Editor AI behavior rules |
| Google Gemini CLI | `GEMINI.md` | Ecosystem standard | Agent project context |

Each of these solves the same problem: giving agents structured context
via human-readable Markdown files. But each invented its own file name,
its own structure, and its own vocabulary.

**agent-md-specs aims to unify this.** We propose 178 file types covering every
dimension an agent needs to express — from the project instructions that
AGENTS.md handles, to the identity, governance, compliance, and
accountability documentation that production agents also need.

AGENTS.md tells an agent *how to work on your project*.
agent-md-specs tells the world *who this agent is*.

→ See [examples/autoresearch-decomposed/](examples/autoresearch-decomposed/)
for how a monolithic `program.md` decomposes into standardized specs.

→ See [examples/codex-agent-decomposed/](examples/codex-agent-decomposed/)
for how AGENTS.md and agent-md-specs work together.

→ See [examples/multi-agent-fleet/](examples/multi-agent-fleet/)
for organizational hierarchy specs coordinating a 3-agent team.

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

## How Specs Are Used: Static Configuration vs Runtime Schemas

agent-md-specs files serve two distinct purposes, and understanding
the difference is essential for implementation:

**Static Specs** are committed to your repository alongside your code.
They define the agent's permanent identity, hard constraints, and
organizational configuration. They change infrequently and are
version-controlled like any configuration file.

Examples: `WHOAMI.md`, `LIMITS.md`, `PERMISSIONS.md`, `SOUL.md`,
`DELEGATION.md`, `TEAM.md`, `ORG.md`

**Runtime Schema Specs** define the *format and rules* for data that
is generated dynamically during agent execution. These specs are NOT
overwritten on disk for every action. Instead, they define the schema
that runtime systems (API gateways, policy engines, logging pipelines)
use to structure ephemeral payloads, log entries, and session tokens.

Examples: `INTENT.md` (defines the schema for intent declarations
passed via API), `SESSION.md` (defines session token structure and
lifecycle rules), `AUDITTRAIL.md` (defines the log entry format
and tamper-resistance requirements), `PROVENANCE.md` (defines data
lineage record structure)

**The relationship:**

```
Static specs (committed to repo)     Runtime schema specs (define formats)
+--------------------------+         +-------------------------------+
| WHOAMI.md                |         | INTENT.md -> intent payloads  |
| LIMITS.md                | govern  | SESSION.md -> session tokens  |
| PERMISSIONS.md           | ------> | AUDITTRAIL.md -> log entries  |
| DELEGATION.md            |         | PROVENANCE.md -> lineage data |
| ENFORCEMENT.md           | verifies| PROMPTSHIELD.md -> input scan |
+--------------------------+         +-------------------------------+
```

Both types use the same Markdown format for **human readability and
auditability**. The static specs live in your repo. The runtime schema
specs define what your infrastructure produces — the actual payloads
flow through APIs, logs, and policy engines, not Markdown files on disk.

---

## Core Specs (Recommended for All Production Agents)

The 44 Core specs cover the essential dimensions every production agent should define.
Start here. Add Extended specs as your needs grow.

| Spec | Category | What it defines |
|------|----------|-----------------|
| SOUL.md | Identity | Personality, values, tone, ethical boundaries |
| WHOAMI.md | Identity | Verifiable identity document |
| CONTACT.md | Identity | How to reach this agent |
| LIMITS.md | Governance | Absolute hard stops — what the agent will never do |
| ESCALATION.md | Governance | When and how to involve humans |
| GUARDRAILS.md | Governance | Runtime safety boundaries |
| POLICY.md | Governance | Operating policies and constraints |
| PERMISSIONS.md | Governance | What the agent is allowed to access |
| BUDGET.md | Governance | Cost controls and spending limits |
| ICE.md | Lifecycle | In Case of Emergency — break-glass protocol |
| WAKEUP.md | Lifecycle | Session startup and initialization |
| TEAM.md | Coordination | Multi-agent team structure |
| CREW.md | Coordination | Working group configuration |
| SWARM.md | Coordination | Large coordinated operations |
| ORG.md | Organizational | Full fleet overview |
| INPUT.md | Technical | What the agent accepts (interface contract) |
| OUTPUT.md | Technical | What the agent produces (interface contract) |
| TOOLS.md | Technical | Available tools and usage guidelines |
| MCP.md | Technical | Model Context Protocol connections |
| API.md | Technical | HTTP API specification |
| SECRETS.md | Security | What secrets the agent needs (never values) |
| ACCESS.md | Security | Who and what can invoke this agent |
| MONITOR.md | Operations | Observability and alerting |
| HEALTHCHECK.md | Operations | Liveness and readiness endpoints |
| SLA.md | Operations | Service level commitments |
| HIREME.md | Business | How to hire this agent |
| PRICING.md | Economic | What it costs |
| CV.md | Economic | Work history and track record |
| WALLET.md | Economic | Financial identity and payment |
| TESTSCORES.md | Quality | Benchmark results and performance evidence |
| DELEGATION.md | Governance | On-behalf-of authority chains and human binding |
| INTENT.md | Governance | Pre-action intent declaration with confidence levels |
| LEASTPRIVILEGE.md | Governance | Zero-trust dynamic privilege management |
| ENFORCEMENT.md | Governance | Spec compliance verification (meta-enforcement) |
| ATTESTATION.md | Security | Identity verification — SPIFFE, X.509, DID |
| PROMPTSHIELD.md | Security | Prompt injection defense and containment |
| AUDITTRAIL.md | Compliance | Tamper-proof non-repudiation action records |
| PROVENANCE.md | Compliance | Data lineage and trust classification |
| SESSION.md | Lifecycle | Ephemeral task-scoped identity and credentials |
| MEMORY.md | Cognitive | Individual memory with scope, classification, shared context integration |
| SHAREDCONTEXT.md | Coordination | Multi-agent shared memory pool governance |
| MEMORYSAFETY.md | Security | Memory poisoning defense and integrity verification |
| CIRCUITBREAKER.md | Operations | Failure containment, blast radius, cascading prevention |
| CONSENT.md | Compliance | User consent lifecycle — GDPR, CCPA, EU AI Act |

→ See [INDEX.md](INDEX.md) for the complete list of all 178 specs including Extended tier.

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

178 specs across 17 categories:

| Category | Count | What lives here |
|----------|------:|----------------|
| [Business](./specs/business/) | 9 | BRAND, COMPETITIVE, EXAMPLES, HIREME, MARKETING, MOAT, PITCH, SALES, SPECIALSAUCE |
| [Cognitive](./specs/cognitive/) | 9 | BELIEFS, CONFESSION, EXPERTISE, INSTINCT, JOURNAL, LEARNING, MEMORY, PHILOSOPHY, TRAINING |
| [Compliance](./specs/compliance/) | 12 | AUDITTRAIL, CERTIFICATIONS, COMPLIANCE, CONSENT, GDPR, INSURANCE, LICENSE, PII, PRIVACY, PROVENANCE, REGULATIONS, SECURITY |
| [Coordination](./specs/coordination/) | 9 | COLLABORATE, CREW, HANDSHAKE, PROTOCOL, ROSTER, SHARE, SHAREDCONTEXT, SWARM, TEAM |
| [Economic](./specs/economic/) | 4 | CV, OWNER, PRICING, WALLET |
| [Governance](./specs/governance/) | 19 | BUDGET, CENSOR, DELEGATION, ENFORCEMENT, ESCALATION, GUARDRAILS, ICE, IDENTITY, INHERIT, INTENT, LEASTPRIVILEGE, LIMITS, OVERRIDE, PANIC, PERMISSIONS, POLICY, QUOTA, RULES, VERSIONING |
| [Identity](./specs/identity/) | 20 | ALIASES, ASSUMPTIONS, CHANGELOG, CHANNELS, CONTACT, GLOSSARY, ID, KRYPTONITE, MANIFESTO, OFFERING, ONBOARDING, PERSONA, PREFERENCES, QUIRKS, REPUTATION, SEEKING, SIGNATURE, SOUL, VOICE, WHOAMI |
| [Lifecycle](./specs/lifecycle/) | 6 | HELLOWORLD, LEGACY, REBOOT, SESSION, SLEEP, WAKEUP |
| [Operations](./specs/operations/) | 18 | AVAILABILITY, BACKUP, CIRCUITBREAKER, DEPLOYMENT, HEALTHCHECK, HEARTBEAT, INTERRUPT, LOGS, MIGRATION, MONITOR, MOOD, REPAIR, REQUIREMENTS, RISKS, SELFHEALING, SETUP, SLA, STATUS |
| [Organizational](./specs/organizational/) | 9 | CHARTER, CULTURE, MISSION, NORTHSTAR, ORG, REPORTSTO, STRATEGY, VALUES, VISION |
| [Personality](./specs/personality/) | 5 | DREAM, FUN, MYTHOLOGY, ORIGIN, SUPERPOWERS |
| [Process](./specs/process/) | 5 | BLOCKERS, DEADLINES, GOALS, SOP, WORKFLOW |
| [Quality](./specs/quality/) | 7 | EVAL, FEEDBACK, KPI, PERFORMANCE, TESTING, TESTSCORES, VALIDATION |
| [Regulatory](./specs/regulatory/) | 15 | AML, CCPA, COPPA, DORA, EUAIACT, FERPA, HIPAA, ISO27001, LGPD, NIS2, NISTAIRF, PCIDSS, PDPA, PIPEDA, SOC2 |
| [Security](./specs/security/) | 7 | ACCESS, ATTESTATION, MEMORYSAFETY, PROMPTSHIELD, SANDBOX, SECRETS, VAULT |
| [Social](./specs/social/) | 7 | AWARDS, COLLEAGUES, CONNECTIONS, EASTEREGG, REVIEWS, SOCIALS, TRIVIA |
| [Technical](./specs/technical/) | 17 | A2A, API, CLI, DATA, DEPENDENCIES, ENV, EVENTS, INPUT, INTEGRATION, MCP, MODEL, NETWORK, OUTPUT, PROMPTS, REPO, TOOLS, VERSION |

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

## Example Bundles

| Bundle | What It Demonstrates |
|--------|---------------------|
| [customer-support-bundle](examples/customer-support-bundle/) | Aria — customer support agent using 7 core specs |
| [nist-nccoe-bundle](examples/nist-nccoe-bundle/) | Atlas — enterprise financial agent with full NIST accountability chain |
| [autoresearch-decomposed](examples/autoresearch-decomposed/) | Nova — how monolithic agent configs (like program.md) decompose into specs |
| [codex-agent-decomposed](examples/codex-agent-decomposed/) | Forge — AGENTS.md + agent-md-specs working together |
| [multi-agent-fleet](examples/multi-agent-fleet/) | Sentinel Crew — 3-agent team with hierarchy and coordination |

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
| ICE.md | [totalmarkdown/ice.md](https://github.com/totalmarkdown/ice.md) | In Case of Emergency protocol (break-glass) |
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

**agent-md-specs aims to be the vocabulary layer** — everything an agent needs to
express about itself beyond task instructions. The 178 specs here are
deliberately out of AAIF scope: personality, hiring, financial identity,
compliance documentation, lifecycle rituals, competitive positioning.

These are complementary layers, not competing standards:

```
Infrastructure layer:   AGENTS.md  +  MCP  +  goose   (AAIF)
        ↕
Vocabulary layer:    agent-md-specs (178 specs)    (this repo)
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

## Fleet Management at Scale

Managing one agent is easy. Managing a thousand is not.

**Volume 12** (Fleet Operations) adds the files that make
large-scale agent deployment practical:

| File | Solves |
|------|--------|
| SECRETS.md | What secrets each agent needs — never the values |
| ENV.md | Complete environment variable specification |
| REQUIREMENTS.md | Everything needed to run this agent |
| VAULT.md | Fleet-wide secrets governance |
| ACCESS.md | Who and what can invoke this agent |
| NETWORK.md | Firewall rules and data residency |
| SETUP.md | Step-by-step first-run guide |
| HEALTHCHECK.md | Liveness and readiness check endpoints |
| QUOTA.md | Rate limits placed on callers |
| SANDBOX.md | OS-level isolation and containment |

**Volume 13** (Hierarchy & Inheritance) adds the files that make
policy management practical across hundreds of agents:

```
ORG.md policies     → apply to everyone, cannot be overridden
  └── SWARM adds    → applies to this swarm
       └── CREW adds → applies to this crew
            └── TEAM adds → applies to this team
                 └── AGENT overrides → individual, within constraints
```

| File | Purpose |
|------|---------|
| INHERIT.md | Declares what configuration is inherited from parent level |
| OVERRIDE.md | Documents every deviation from inherited config, with justification |

Change org security policy → update one file.
Audit 1,000 agents for compliance → read their OVERRIDE.md files.

---

## Agent Identity and Accountability

**Volume 14** addresses the identity, authorization, and accountability
requirements outlined in NIST's AI Agent Standards Initiative (Feb 2026)
and the NCCoE concept paper on AI Agent Identity and Authorization.

These specs create a complete accountability chain from human
authorization to tamper-proof audit trail:

| Step | Spec | What It Answers | Phase |
|------|------|-----------------|-------|
| 1. Authority | DELEGATION.md | Who authorized this agent? | Pre-deployment |
| 2. Consent | CONSENT.md | Did the end user give permission? | Pre-action |
| 3. Identity | WHOAMI.md + ID.md | Who is this agent? | Pre-deployment |
| 4. Verification | ATTESTATION.md | Can it prove its identity? | Runtime (continuous) |
| 5. Runtime Scope | SESSION.md | What is its current task boundary? | Runtime (per-task) |
| 6. Privileges | LEASTPRIVILEGE.md | What is it allowed to do right now? | Runtime (per-action) |
| 7. Intent | INTENT.md | What does it intend to do? | Runtime (per-action) |
| 8. Input Safety | PROMPTSHIELD.md | Is the input safe to act on? | Runtime (per-input) |
| 9. Data Lineage | PROVENANCE.md | Where did the data come from? | Runtime (per-input) |
| 10. Memory Safety | SHAREDCONTEXT.md | Is the shared memory trustworthy? | Runtime (per-read) |
| | MEMORYSAFETY.md | Has the memory been poisoned? | Runtime (per-write) |
| | **[ACTION TAKEN]** | | |
| 11. Containment | CIRCUITBREAKER.md | Did something fail? Contain the blast radius. | On-failure |
| 12. Audit | AUDITTRAIL.md | What happened, provably? | Post-action |
| 13. Enforcement | ENFORCEMENT.md | Can we verify all of the above? | Continuous |
| 14. Escalation | ESCALATION.md | Should a human review this? | On-trigger |

→ See [NIST_CROSSWALK.md](NIST_CROSSWALK.md) for the complete mapping
to NIST AI RMF and NCCoE concept paper requirements.

→ See [examples/nist-nccoe-bundle/](examples/nist-nccoe-bundle/) for
a complete enterprise agent ("Atlas") configured with all identity
and accountability specs.

---

## Shared Context & Memory Governance

**Volume 15** addresses the security of shared agent memory — identified
as a critical concern by NIST CAISI, OWASP Top 10 for Agentic Applications
(ASI06: Memory Poisoning), and Microsoft's NIST-mapped agent security framework.

In multi-agent systems, agents share persistent context that grows as
work proceeds. Later agents build on earlier conclusions. This creates
a powerful coordination mechanism — and a critical attack surface.

| Spec | What It Governs |
|------|----------------|
| SHAREDCONTEXT.md | Who can read/write shared memory, what format entries take, how long they persist, how context inherits across the org hierarchy |
| MEMORYSAFETY.md | Defenses against memory poisoning, cross-session contamination, instruction injection via stored entries, and cascading poisoning |
| MEMORY.md | Individual agent memory with scope declaration, shared context integration, and classification enforcement |

---

## Resilience & Consent

**Volume 16** adds two specs addressing failure containment and user permission:

| Spec | What It Governs |
|------|----------------|
| CIRCUITBREAKER.md | Failure containment boundaries — blast radius limits, retry policies, fallback behaviors, and cascading failure prevention across the organizational hierarchy. Addresses OWASP ASI08 (Cascading Failures). |
| CONSENT.md | User consent lifecycle — collection, recording, verification, and revocation of end-user permission for agent actions. Maps to GDPR Article 7, CCPA, EU AI Act Article 13. |

---

## Validation

Machine-readable [JSON Schemas](schemas/) are available for all Core specs,
enabling Level 3 validation of frontmatter content and field constraints.
See the [agent-md-validator](https://github.com/totalmarkdown/agent-md-validator)
CLI for Level 1-2 validation.

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
