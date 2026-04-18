# How agent-md-specs compares to AGENTS.md, CLAUDE.md, MCP, and other formats

> These are orthogonal, not competing. Use `AGENTS.md` to tell the
> agent how to work on your repo. Use `agent-md-specs` to tell the
> world who the agent is, what it will never do, who authorized it,
> and what it did.

agent-md-specs is a proposed vocabulary for the governance,
accountability, and identity dimensions of AI agent configuration. It
is intentionally designed to layer on top of — not replace — the
existing ecosystem of agent configuration formats.

This document exists because the most common objection we hear is
"isn't this just AGENTS.md?" It isn't. Here's how they compare.

## One-line summaries

| Format | One-line summary |
|--------|------------------|
| **agent-md-specs** | 179 Markdown spec types covering identity, governance, accountability, and compliance — the "who / what / why / who approved / what happened" layer. |
| **AGENTS.md** (AAIF / Linux Foundation) | A single `AGENTS.md` file in your repo telling coding agents how to build, test, and style your code. |
| **CLAUDE.md** (Anthropic) | Like AGENTS.md but for Claude Code specifically — project instructions a coding agent reads at session start. |
| **SKILL.md** (Anthropic) | Reusable, composable agent capability definitions — a skill library for Claude. |
| **.cursorrules** (Cursor) | In-IDE behavior rules for the Cursor editor's AI assistant. |
| **program.md** (Karpathy autoresearch) | A single Markdown file specifying an autonomous ML research workflow. |
| **MCP** (Anthropic Model Context Protocol) | A wire protocol (JSON-RPC over stdio/HTTP) for agents to call tools and read resources. Not a file format. |
| **Markform** | Markdown-native form specification format (separate project, related ecosystem). |

## Comparison matrix

| Dimension | agent-md-specs | AGENTS.md | CLAUDE.md | .cursorrules | program.md | MCP |
|-----------|:--------------:|:---------:|:---------:|:------------:|:----------:|:---:|
| **Primary purpose** | Identity, governance, accountability | Project instructions for coding agents | Same as AGENTS.md (Claude-specific) | IDE AI behavior | Autonomous research workflow | Tool + resource protocol |
| **Audience** | Compliance, security, ops, agent authors | Coding agents | Claude Code | Cursor AI | Autonomous agents | Any agent + any tool |
| **Scope** | Cross-repo (per agent) | Per-repo | Per-repo | Per-repo | Per-workflow | Runtime connection |
| **Lifecycle** | Formal Draft → Proposed → Stable | Single spec, AAIF-governed | Single convention | Single convention | Single file | Versioned protocol |
| **Format** | 179 Markdown file types + YAML frontmatter + JSON Schemas | Single Markdown file | Single Markdown file | Single Markdown file | Single Markdown file | JSON-RPC |
| **What it covers** | Who / authority / limits / consent / audit / memory safety / coordination / compliance | Build / test / style / dependencies | Same as AGENTS.md | IDE prompts | Research steps | Tool calls, resources, prompts |
| **What it doesn't cover** | Build commands, runtime tool calls, model choice | Agent identity, delegation, audit | Same as AGENTS.md | Agent lifecycle | Governance | File conventions, identity |
| **License** | CC0 | MIT / open | Anthropic docs | Cursor docs | MIT | MIT |
| **Maturity** | Draft (seeking review) | AAIF standard, 67,000+ repos | Ecosystem standard | Ecosystem standard | 59,000+ stars (educational) | Anthropic standard |

## When to use each

**Use AGENTS.md / CLAUDE.md** when you want a coding agent working in
your repo to know: how to build, how to run tests, what style to
follow, what files matter, which commands are safe to run.

**Use .cursorrules** when the only environment the agent runs in is
the Cursor editor, and you want local behavior tweaks.

**Use program.md** when you want to describe an autonomous research
workflow to an ML research agent as an inline instruction set.

**Use MCP** when you want the agent to call tools or read resources
from external systems at runtime — this is a protocol, not a file
format, and it sits underneath any of the above.

**Use agent-md-specs** when you want to:
- Declare who an agent is, in a way that's auditable and verifiable
- Document what it will never do (hard limits, guardrails)
- Trace the authority chain back to a human (delegation)
- Log every consequential action provably (audit trail)
- Define failure containment boundaries (circuit breakers)
- Govern shared memory across multiple agents (shared context +
  memory safety)
- Map the agent's posture to regulatory frameworks (GDPR, HIPAA, EU
  AI Act, SOC 2)

## Can I use AGENTS.md and agent-md-specs together?

Yes. In fact, the [Forge — Codex Agent Decomposed
Bundle](./examples/codex-agent-decomposed/) shows exactly this pattern:
a single project has `AGENTS.md` (for Codex to know how to build the
code) **and** `WHOAMI.md`, `SOUL.md`, `LIMITS.md`, `DELEGATION.md`,
`AUDITTRAIL.md`, `ENFORCEMENT.md`, `ESCALATION.md` (for the governance,
identity, and accountability layer). The files answer different
questions and live side by side.

## Stack diagram

```
                     ┌────────────────────────────────┐
Identity +    ┌──►  │  agent-md-specs (179 spec types) │   ← this repo
accountability │     │  "who / what won't / audit / …"  │      Markdown + YAML
layer          │     └────────────────────────────────┘      + JSON Schemas
               │                   ▲
               │                   │  can coexist with
               │                   ▼
Project-       │     ┌────────────────────────────────┐
instruction    ├──►  │  AGENTS.md / CLAUDE.md /        │      Markdown only
layer          │     │  .cursorrules / program.md     │
               │     │  "how to build / style / test"  │
               │     └────────────────────────────────┘
               │                   ▲
               │                   │  runtime calls via
               │                   ▼
Runtime        │     ┌────────────────────────────────┐
protocol       └──►  │  MCP (JSON-RPC)                 │      protocol, not files
                     │  "invoke tools + read resources" │
                     └────────────────────────────────┘
```

## FAQ

**"Why not just PR all this into AGENTS.md?"**
AGENTS.md is a single file with a deliberately small surface area
(build/test/style). Pushing 179 governance dimensions into it would
break the format for its current users. agent-md-specs is a separate,
composable vocabulary that AGENTS.md users can adopt incrementally.

**"Why so many files? Couldn't this be one big spec?"**
It could — and in single-agent cases, a monolithic `program.md` works
fine. The reason for decomposition is that different audiences read
different files: compliance reads `AUDITTRAIL.md` and `CONSENT.md`,
security reads `LIMITS.md` and `ATTESTATION.md`, ops reads `MONITOR.md`
and `CIRCUITBREAKER.md`. Separating them means each spec can be
reviewed and approved by the right owner.

**"Isn't this just documentation?"**
The YAML frontmatter in every spec is machine-readable. Policy engines
(OPA/Rego), API gateways, and logging pipelines consume the same file
compliance officers approve. There is no drift between what humans
signed off on and what machines enforce — because it's the same file.

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
