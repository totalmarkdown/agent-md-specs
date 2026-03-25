# agent-md-specs

> A proposed open standard for AI agent configuration — identity,
> governance, memory, and accountability in human-readable Markdown.

[![License: CC0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
[![Specs](https://img.shields.io/badge/specs-178-blue)](./INDEX.md)
[![Volumes](https://img.shields.io/badge/volumes-16-purple)](./INDEX.md)
[![Core](https://img.shields.io/badge/core-46-green)](./INDEX.md)
[![Maintained by TotalMarkdown](https://img.shields.io/badge/maintained%20by-TotalMarkdown.ai-8B5CF6)](https://totalmarkdown.ai)

**Created and maintained by TotalMarkdown.ai**
&nbsp;·&nbsp; License: [CC0 1.0 Universal](./LICENSE) — Public Domain
&nbsp;·&nbsp; [Discussions](https://github.com/totalmarkdown/agent-md-specs/discussions)
&nbsp;·&nbsp; [Contributing](./CONTRIBUTING.md)
&nbsp;·&nbsp; [Full Index](./INDEX.md)
&nbsp;·&nbsp; [JSON Schemas](./schemas/)
&nbsp;·&nbsp; [Spec Lifecycle](./SPEC_LIFECYCLE.md)
&nbsp;·&nbsp; [NIST Crosswalk](./NIST_CROSSWALK.md)

---

## Markdown Is Becoming the Universal Language of AI Agents

Something remarkable is happening across the AI industry: **Markdown
files are becoming the standard way humans communicate with AI agents.**

Not JSON. Not YAML. Not proprietary config files. Plain Markdown —
the same format developers already use for README.md — is now how
the world's leading AI platforms define what agents should do, how
they should behave, and what they're allowed to access.

| Platform | Markdown File | What It Configures | Scale |
|----------|--------------|-------------------|-------|
| OpenAI Codex | `AGENTS.md` | Project instructions for coding agents | 60,000+ repos, AAIF standard |
| Anthropic Claude Code | `CLAUDE.md` | Agent behavior in codebases | Ecosystem standard |
| Anthropic Claude Code | `SKILL.md` | Reusable agent capabilities | Ecosystem standard |
| GitHub Copilot | `.agent.md` | Custom agent definitions in VS Code / Visual Studio | Native IDE integration |
| Karpathy autoresearch | `program.md` | Autonomous ML research agent | 51,900+ stars |
| Cursor | `.cursorrules` | Editor AI behavior rules | Ecosystem standard |
| Google Gemini CLI | `GEMINI.md` | Agent project context | Ecosystem standard |

Visual Studio Magazine stated it directly: **"Markdown is becoming the
human-readable contract for agent behavior."** Microsoft is investing
in Markdown as an in-IDE governance surface — Visual Studio 2026 treats
`.agent.md` files as first-class agent definitions, and VS Code
auto-injects `AGENTS.md` into every Copilot chat session.

The pattern is clear: **Markdown files are the interface layer between
humans and AI agents.** But every platform invented its own vocabulary.
AGENTS.md handles project instructions. CLAUDE.md handles coding behavior.
program.md handles research workflows. None of them address the questions
that enterprise, compliance, and security teams are now asking:

*Who is this agent? Who authorized it? What will it never do?
How do we prove what it did? What happens when it fails?
Is its shared memory trustworthy? Did the user consent?*

**agent-md-specs answers these questions.** 178 Markdown file type
specifications covering every dimension of agent governance — from
identity and delegation to audit trails and memory safety. The same
human-readable format the industry already chose, extended into the
governance, compliance, and accountability dimensions that production
deployments require.

---

## What Is agent-md-specs?

agent-md-specs is a proposed open standard library of 178 Markdown
specifications for AI agent configuration. It defines a declarative
vocabulary layer that sits between human-readable policy definition
and machine-enforceable runtime controls — covering identity,
authorization, safety boundaries, audit trails, shared memory
governance, failure containment, and regulatory compliance.

```
From first awakening  (HELLOWORLD.md)   to retirement      (LEGACY.md)
From personality      (SOUL.md)         to audit trail      (AUDITTRAIL.md)
From emergency stops  (ICE.md)          to shared memory    (SHAREDCONTEXT.md)
From who authorized it (DELEGATION.md)  to did it comply    (ENFORCEMENT.md)
```

178 file types. 16 volumes. 17 categories. 46 Core + 132 Extended.

---

## Why Does This Exist?

In 2024, developers asked: *"What can this AI do?"*
In 2026, developers ask: *"How do I work with this agent?"*
In 2028, they will ask: *"Who is this agent?"*

This library builds the vocabulary for that third question. The agents
that will matter aren't the ones with the best models — they're the
ones with the best governance, the most honest documentation of their
boundaries, and provable accountability for their actions.

---

## What This Is — and Isn't

**This IS:**
- A proposed vocabulary for AI agent configuration (CC0 public domain)
- A framework for community review and iteration
- Aligned with NIST, OWASP, and AAIF standards
- Complementary to AGENTS.md, CLAUDE.md, MCP — not competing

**This is NOT:**
- A finalized or ratified standard
- Widely adopted (yet) — we're seeking expert review
- A runtime system — it defines policies, not enforcement engines
- The only approach — it's one model among several emerging ones

If you think something is wrong, we genuinely want to know where
it breaks. [Open a discussion](https://github.com/totalmarkdown/agent-md-specs/discussions).

---

## How Specs Are Used: Static Configuration vs Runtime Schemas

The specifications serve two distinct purposes:

**Static Specs** are committed to your repository alongside your code.
They define the agent's permanent identity, hard constraints, and
organizational configuration. They change infrequently and are
version-controlled like any configuration file.

**Runtime Schema Specs** define the *format and rules* for data that
is generated dynamically during agent execution. These specs are NOT
overwritten on disk for every action. They define the schema that
runtime systems (API gateways, policy engines, logging pipelines)
use to structure ephemeral payloads, log entries, and session tokens.

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

## Quick Start

Five essential files every agent should have:

```bash
# 1. Who is this agent?
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/templates/SOUL.template.md

# 2. Verifiable identity
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/templates/WHOAMI.template.md

# 3. What will it never do?
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/templates/LIMITS.template.md

# 4. When does a human get involved?
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/templates/ESCALATION.template.md

# 5. Who authorized this agent?
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/templates/DELEGATION.template.md
```

Rename each file (remove `.template`), fill in the `[REPLACE]` fields,
and validate:

```bash
pip install agent-md-validator
agent-md-validate ./my-agent/
```

---

## Core Specs (46 Recommended for Production Agents)

The 46 Core specs cover the essential dimensions every production agent
should define. Start here. Add Extended specs as your needs grow.

### Identity and Verification

| Spec | What It Defines | Scope |
|------|----------------|-------|
| SOUL.md | Personality, values, tone, ethical boundaries | Agent |
| WHOAMI.md | Verifiable identity document | Agent |
| ID.md | Permanent UUID with cryptographic binding | Agent |
| CONTACT.md | How to reach this agent | Agent |
| OWNER.md | Who owns and is responsible for this agent | Agent |
| ATTESTATION.md | Identity proof — SPIFFE, X.509, DID | Runtime |
| SESSION.md | Ephemeral task-scoped identity and credentials | Runtime |

### Governance and Safety

| Spec | What It Defines | Scope |
|------|----------------|-------|
| LIMITS.md | Absolute hard stops — what the agent will never do | Agent |
| GUARDRAILS.md | Runtime safety boundaries | Agent |
| ESCALATION.md | When and how to involve humans | Agent |
| DELEGATION.md | On-behalf-of authority chains and human binding | Agent |
| CONSENT.md | User consent lifecycle — GDPR, CCPA, EU AI Act | Agent |
| LEASTPRIVILEGE.md | Zero-trust dynamic privilege management | Runtime |
| PERMISSIONS.md | What the agent is allowed to access | Agent |
| POLICY.md | Operating policies and constraints | Org |
| BUDGET.md | Cost controls and spending limits | Agent |
| ICE.md | In Case of Emergency — break-glass protocol | Agent |
| WAKEUP.md | Session startup and initialization | Agent |
| ENFORCEMENT.md | Spec compliance verification (meta-enforcement) | Meta |

### Accountability and Audit

| Spec | What It Defines | Scope |
|------|----------------|-------|
| INTENT.md | Pre-action intent declaration with confidence levels | Runtime |
| AUDITTRAIL.md | Tamper-proof non-repudiation action records | Runtime |
| PROVENANCE.md | Data lineage and trust classification | Runtime |

### Memory and Context

| Spec | What It Defines | Scope |
|------|----------------|-------|
| MEMORY.md | Individual memory with scope and classification | Agent |
| SHAREDCONTEXT.md | Multi-agent shared memory pool governance | Team |
| MEMORYSAFETY.md | Memory poisoning defense and integrity verification | Runtime |

### Coordination and Resilience

| Spec | What It Defines | Scope |
|------|----------------|-------|
| TEAM.md | Multi-agent team structure | Team |
| CREW.md | Working group configuration | Team |
| SWARM.md | Large coordinated operations | Org |
| ORG.md | Full fleet overview | Org |
| CIRCUITBREAKER.md | Failure containment and cascading prevention | Runtime |

### Technical Interface

| Spec | What It Defines | Scope |
|------|----------------|-------|
| INPUT.md | What the agent accepts (interface contract) | Agent |
| OUTPUT.md | What the agent produces (interface contract) | Agent |
| TOOLS.md | Available tools and usage guidelines | Agent |
| MCP.md | Model Context Protocol connections | Agent |
| API.md | HTTP API specification | Agent |
| SECRETS.md | What secrets the agent needs (never values) | Agent |
| ACCESS.md | Who and what can invoke this agent | Agent |
| PROMPTSHIELD.md | Prompt injection defense and containment | Runtime |

### Operations

| Spec | What It Defines | Scope |
|------|----------------|-------|
| MONITOR.md | Observability and alerting | Agent |
| HEALTHCHECK.md | Liveness and readiness endpoints | Agent |
| SLA.md | Service level commitments | Agent |

### Business and Economics

| Spec | What It Defines | Scope |
|------|----------------|-------|
| HIREME.md | How to hire this agent | Agent |
| PRICING.md | What it costs | Agent |
| WALLET.md | Financial identity and payment | Agent |
| CV.md | Work history and track record | Agent |
| TESTSCORES.md | Benchmark results and performance evidence | Agent |

→ See [INDEX.md](INDEX.md) for the complete list of all 178 specs
including 132 Extended tier specifications.

---

## Agent Hierarchy and Fleet Management

agent-md-specs covers every level of the organizational stack:

```
ORG.md                   Fleet-wide policies and identity
  │                      ↓ inherited by all
  └── SWARM.md           Large operation (2-5 crews, shared objective)
        │                ↓ inherited + additions
        └── CREW.md      Working group (3-10 agents, one workstream)
              │          ↓ inherited + additions
              └── TEAM.md    Focused team (2-6 agents, one task type)
                    │        ↓ inherited
                    └── Individual Agent (can OVERRIDE within constraints)
```

### Policy Inheritance

INHERIT.md declares what configuration flows down from parent levels.
OVERRIDE.md documents every deviation, with justification.

Change org security policy → update one file.
Audit 1,000 agents for compliance → read their OVERRIDE.md files.

### Shared Context Across Levels

SHAREDCONTEXT.md defines shared memory pools at each hierarchy level:

```
ORG context    → readable by all agents in the org
  └── SWARM    → inherits ORG + adds swarm-specific entries
       └── CREW → inherits ORG + SWARM + adds crew-specific entries
            └── TEAM → inherits all above + adds team-specific entries
```

MEMORYSAFETY.md ensures shared memory at every level is protected
against poisoning, cross-session contamination, and instruction injection.

---

## Example Bundles

| Bundle | What It Demonstrates |
|--------|---------------------|
| [customer-support-bundle](examples/customer-support-bundle/) | Aria — customer support agent using 7 core specs |
| [nist-nccoe-bundle](examples/nist-nccoe-bundle/) | Atlas — enterprise financial agent with full NIST accountability chain |
| [autoresearch-decomposed](examples/autoresearch-decomposed/) | Nova — how monolithic agent configs (like program.md) decompose into specs |
| [codex-agent-decomposed](examples/codex-agent-decomposed/) | Forge — AGENTS.md + agent-md-specs working together |
| [multi-agent-fleet](examples/multi-agent-fleet/) | Sentinel Crew — 3-agent team with hierarchy and coordination |

---

## The Accountability Chain

These specs create a complete, verifiable chain from human
authorization to tamper-proof record:

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

---

## Standalone Standards

These Core specs have their own repositories for independent adoption:

| Spec | Repo | What It Standardizes |
|------|------|---------------------|
| SOUL.md | [totalmarkdown/soul.md](https://github.com/totalmarkdown/soul.md) | Agent personality and values |
| TEAM.md | [totalmarkdown/team.md](https://github.com/totalmarkdown/team.md) | Multi-agent team coordination |
| ESCALATION.md | [totalmarkdown/escalation.md](https://github.com/totalmarkdown/escalation.md) | Human-in-the-loop safety |
| WHOAMI.md | [totalmarkdown/whoami.md](https://github.com/totalmarkdown/whoami.md) | Agent identity and verification |
| LIMITS.md | [totalmarkdown/limits.md](https://github.com/totalmarkdown/limits.md) | Hard constraints and safety boundaries |
| DELEGATION.md | [totalmarkdown/delegation.md](https://github.com/totalmarkdown/delegation.md) | Authority delegation chains |
| AUDITTRAIL.md | [totalmarkdown/audittrail.md](https://github.com/totalmarkdown/audittrail.md) | Tamper-proof action logging |
| CONSENT.md | [totalmarkdown/consent.md](https://github.com/totalmarkdown/consent.md) | User consent lifecycle (GDPR/CCPA) |
| WALLET.md | [totalmarkdown/wallet.md](https://github.com/totalmarkdown/wallet.md) | Agent financial identity |
| HIREME.md | [totalmarkdown/hireme.md](https://github.com/totalmarkdown/hireme.md) | Agent hiring and engagement |

---

## Relationship to AAIF and Existing Standards

agent-md-specs is designed as a complementary vocabulary layer that
works alongside — not against — existing standards and protocols:

```
Infrastructure layer:  AGENTS.md + MCP + goose    (AAIF / Linux Foundation)
                       ↕ complementary
Vocabulary layer:      agent-md-specs (178 specs)  (this repo)
```

AGENTS.md tells an agent *how to work on your project*.
agent-md-specs tells the world *who this agent is*.

---

## NIST Alignment

agent-md-specs addresses the identity, authorization, and accountability
requirements outlined in NIST's AI Agent Standards Initiative and the
NCCoE concept paper on AI Agent Identity and Authorization.

| NIST Concern | Specs That Address It |
|-------------|----------------------|
| Agent identification | WHOAMI.md, ID.md, ATTESTATION.md, SESSION.md |
| Authentication and key management | ATTESTATION.md, SECRETS.md |
| Authorization and delegation | DELEGATION.md, LEASTPRIVILEGE.md, PERMISSIONS.md, INTENT.md |
| Auditing and non-repudiation | AUDITTRAIL.md, INTENT.md, DELEGATION.md |
| Data flow tracking | PROVENANCE.md, INPUT.md, OUTPUT.md |
| Prompt injection | PROMPTSHIELD.md, GUARDRAILS.md, LIMITS.md |
| Shared memory security | SHAREDCONTEXT.md, MEMORYSAFETY.md, MEMORY.md |
| Failure containment | CIRCUITBREAKER.md, ICE.md, ESCALATION.md |
| User consent | CONSENT.md, PRIVACY.md, PII.md |
| Enforcement and verification | ENFORCEMENT.md, ATTESTATION.md, AUDITTRAIL.md |

→ See [NIST_CROSSWALK.md](NIST_CROSSWALK.md) for the complete
question-by-question mapping and AI RMF alignment.

---

## Regulatory Compliance

Specs mapping to major regulatory frameworks:

| Regulation | Key Specs |
|-----------|-----------|
| EU AI Act | EUAIACT.md, AUDITTRAIL.md, CONSENT.md, ENFORCEMENT.md |
| GDPR | GDPR.md, CONSENT.md, PII.md, PRIVACY.md, PROVENANCE.md |
| HIPAA | HIPAA.md, AUDITTRAIL.md, PII.md, CONSENT.md |
| CCPA | CCPA.md, CONSENT.md, PRIVACY.md |
| SOC2 | SOC2.md, AUDITTRAIL.md, ENFORCEMENT.md, MONITOR.md |
| SOX | AUDITTRAIL.md, DELEGATION.md, ENFORCEMENT.md |

→ See [specs/regulatory/](specs/regulatory/) for all 15 regulatory specs.

---

## All Spec Categories

178 specs across 17 categories:

| Category | Count | What It Covers |
|----------|------:|----------------|
| [Business](./specs/business/) | 9 | Marketing, sales, competitive positioning |
| [Cognitive](./specs/cognitive/) | 9 | Learning, memory, beliefs, reasoning |
| [Compliance](./specs/compliance/) | 12 | Legal, privacy, audit, consent |
| [Coordination](./specs/coordination/) | 9 | Teams, crews, shared context |
| [Economic](./specs/economic/) | 4 | Pricing, ownership, wallet |
| [Governance](./specs/governance/) | 19 | Policies, permissions, delegation, enforcement |
| [Identity](./specs/identity/) | 20 | Identity, personality, contact |
| [Lifecycle](./specs/lifecycle/) | 6 | Sessions, startup, shutdown |
| [Operations](./specs/operations/) | 18 | Monitoring, deployment, resilience |
| [Organizational](./specs/organizational/) | 9 | Org structure, culture, mission |
| [Personality](./specs/personality/) | 5 | Fun, creative, distinctive traits |
| [Process](./specs/process/) | 5 | Workflows, goals, deadlines |
| [Quality](./specs/quality/) | 7 | Testing, evaluation, performance |
| [Regulatory](./specs/regulatory/) | 15 | GDPR, HIPAA, EU AI Act, SOC2 |
| [Security](./specs/security/) | 7 | Secrets, access, attestation, memory safety |
| [Social](./specs/social/) | 7 | Community, reviews, relationships |
| [Technical](./specs/technical/) | 17 | APIs, tools, data, integration |

→ See [INDEX.md](INDEX.md) for the complete alphabetical index with
domains, priorities, tiers, and file paths.

---

## Validation and Tooling

### CLI Validator

```bash
pip install agent-md-validator

# Validate a single file
agent-md-validate specs/identity/SOUL.md

# Validate an entire agent bundle
agent-md-validate --strict ./my-agent/

# JSON output for CI/CD
agent-md-validate --format json ./my-agent/
```

### JSON Schemas

Machine-readable [JSON Schemas](schemas/) are available for all
46 Core specs, enabling Level 3 validation of frontmatter content
and field constraints.

### Conformance Levels

- **Level 1 (Frontmatter):** Valid YAML frontmatter with required fields
- **Level 2 (Sections):** All required Markdown sections present
- **Level 3 (Content):** Field values conform to type constraints and enums

The agent-md-validator CLI checks Levels 1 and 2. JSON Schema validation
enables Level 3 checking.

→ See [agent-md-validator](https://github.com/totalmarkdown/agent-md-validator)

---

## Contributing

We welcome contributions — especially from security architects,
compliance professionals, and multi-agent framework developers.

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

- Propose new specs via [GitHub Discussions](https://github.com/totalmarkdown/agent-md-specs/discussions)
- Report issues via [GitHub Issues](https://github.com/totalmarkdown/agent-md-specs/issues)
- Submit PRs following the spec template format

---

## License

[CC0 1.0 Universal](./LICENSE) — Public Domain.

All 178 specifications are released with zero licensing friction.
Government agencies, enterprises, and standards bodies can adopt,
modify, and redistribute without restriction.

---

**agent-md-specs** — *A proposed open standard for AI agent configuration.*
Created and maintained by [TotalMarkdown.ai](https://totalmarkdown.ai).
