# Start Here

> From curious to validated bundle in under 5 minutes. 4 commands, no signup, CC0.

→ **[Full README](../README.md)** — complete documentation & architecture overview

→ **[Full INDEX](../INDEX.md)** — full library of 179 specs

**TL;DR — run this:**

```bash
curl -LO https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/basic-agent/bundle.zip
unzip bundle.zip -d my-agent/
pip install git+https://github.com/totalmarkdown/agent-md-validator.git
agent-md-validate ./my-agent/
```

Expected output: `PASSED (with warnings)` — the bundle's `[REPLACE]` placeholders generate cross-reference warnings but no errors.

---

## If You're Building an Agent

The 5 files every agent should have:

| File | What It Does |
|------|-------------|
| [SOUL.md](../specs/identity/SOUL.md) | Personality and values |
| [WHOAMI.md](../specs/identity/WHOAMI.md) | Verifiable identity |
| [LIMITS.md](../specs/governance/LIMITS.md) | Hard stops |
| [ESCALATION.md](../specs/governance/ESCALATION.md) | Human-in-the-loop |
| [DELEGATION.md](../specs/governance/DELEGATION.md) | Who authorized this agent |

Download the [Basic Agent — Starter Bundle](../examples/basic-agent/) (the 5 specs above pre-filled with placeholders):

```bash
curl -LO https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/basic-agent/bundle.zip
unzip bundle.zip -d my-agent/
```

Then validate:

```bash
pip install git+https://github.com/totalmarkdown/agent-md-validator.git
agent-md-validate ./my-agent/
```

Expected output: `PASSED (with warnings)` — fill in the `[REPLACE]` fields and the warnings disappear.

<details>
<summary>Prefer individual files? (5 separate curls)</summary>

```bash
curl -O https://raw.githubusercontent.com/totalmarkdown/soul.md/main/SOUL.md
curl -O https://raw.githubusercontent.com/totalmarkdown/whoami.md/main/WHOAMI.md
curl -O https://raw.githubusercontent.com/totalmarkdown/limits.md/main/LIMITS.md
curl -O https://raw.githubusercontent.com/totalmarkdown/escalation.md/main/ESCALATION.md
curl -O https://raw.githubusercontent.com/totalmarkdown/delegation.md/main/DELEGATION.md
```

</details>

---

## If You're Evaluating the Framework

- [COMPARISON.md](../COMPARISON.md) — how this relates to AGENTS.md, CLAUDE.md, MCP, program.md, Markform.
- [CRITICISM.md](../CRITICISM.md) — pre-emptive answers to the objections we expect.
- [SPEC_LIFECYCLE.md](../SPEC_LIFECYCLE.md) — how specs move Draft → Proposed → Stable.
- [ROADMAP.md](../ROADMAP.md) — what's coming, what's deferred, what's out of scope.
- [GOVERNANCE.md](../GOVERNANCE.md) — RFC process, TSC scoping, decision log.

---

## If You're Reviewing the NCCoE Submission

→ **[Guide for NCCoE Submission Reviewers](../NIST_SUBMISSION_GUIDE.md)** — 15-minute
guided tour answering all 6 NCCoE concept paper questions

→ **[NIST Crosswalk](../NIST_CROSSWALK.md)** — Direct mapping to
AI RMF (Govern, Map, Measure, Manage) and SP 800-207 Zero Trust

→ **[Atlas — NIST NCCoE Enterprise Finance Bundle](../examples/nist-nccoe-bundle/)** —
Complete financial agent with accountability chain + failure scenarios

---

## If You're Building a Multi-Agent Team

Add these on top of the 5 above:

| File | What It Does |
|------|-------------|
| [TEAM.md](../specs/coordination/TEAM.md) | Team structure and handoff protocols |
| [SHAREDCONTEXT.md](../specs/coordination/SHAREDCONTEXT.md) | Shared memory governance |
| [MEMORYSAFETY.md](../specs/security/MEMORYSAFETY.md) | Memory poisoning defense |
| [CIRCUITBREAKER.md](../specs/operations/CIRCUITBREAKER.md) | Failure containment |
| [BUDGET.md](../specs/governance/BUDGET.md) | Team cost controls |

Or download the [Sentinel — Multi-Agent Fleet Bundle](../examples/multi-agent-fleet/):

```bash
curl -LO https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/multi-agent-fleet/bundle.zip
unzip bundle.zip -d my-fleet/
```

---

## If You Need Enterprise Compliance

| File | What It Does |
|------|-------------|
| [AUDITTRAIL.md](../specs/compliance/AUDITTRAIL.md) | Tamper-proof action logging |
| [CONSENT.md](../specs/compliance/CONSENT.md) | User consent lifecycle (GDPR/CCPA) |
| [PROVENANCE.md](../specs/compliance/PROVENANCE.md) | Data lineage tracking |
| [ENFORCEMENT.md](../specs/governance/ENFORCEMENT.md) | Policy verification |
| [ATTESTATION.md](../specs/security/ATTESTATION.md) | Cryptographic identity proof |

Or download the [Atlas — NIST NCCoE Enterprise Finance Bundle](../examples/nist-nccoe-bundle/):

```bash
curl -LO https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/nist-nccoe-bundle/bundle.zip
unzip bundle.zip -d my-agent/
```

→ See [NIST Crosswalk](../NIST_CROSSWALK.md) for regulatory mapping.

---

## If You're Listing Agents on a Marketplace

| File | What It Does |
|------|-------------|
| [HIREME.md](../specs/business/HIREME.md) | Agent hiring listing |
| [PRICING.md](../specs/economic/PRICING.md) | Cost structure |
| [WALLET.md](../specs/economic/WALLET.md) | Financial identity |
| [CV.md](../specs/economic/CV.md) | Work history |
| [TESTSCORES.md](../specs/quality/TESTSCORES.md) | Benchmark results |

Or download the [Vex — Marketplace Listing Bundle](../examples/marketplace-agent/):

```bash
curl -LO https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/marketplace-agent/bundle.zip
unzip bundle.zip -d my-agent/
```

---

## Example Bundles

| Bundle | What It Shows |
|--------|--------------|
| [Basic Agent — Starter Bundle](../examples/basic-agent/) | The 5 essential specs every agent needs |
| [Aria — Customer Support Bundle](../examples/customer-support-bundle/) | Simple customer support agent |
| [Atlas — NIST NCCoE Enterprise Finance Bundle](../examples/nist-nccoe-bundle/) | Enterprise financial agent — full accountability chain |
| [Nova — Autoresearch Decomposed Bundle](../examples/autoresearch-decomposed/) | Monolithic config → decomposed specs |
| [Forge — Codex Agent Decomposed Bundle](../examples/codex-agent-decomposed/) | AGENTS.md + agent-md-specs together |
| [Sentinel — Multi-Agent Fleet Bundle](../examples/multi-agent-fleet/) | 3-agent financial pipeline with hierarchy |
| [Vex — Marketplace Listing Bundle](../examples/marketplace-agent/) | Agent hiring, pricing, and benchmarks |

---

*[Full Index](../INDEX.md) · [README](../README.md) · [NIST Crosswalk](../NIST_CROSSWALK.md) · [Contributing](../CONTRIBUTING.md)*
