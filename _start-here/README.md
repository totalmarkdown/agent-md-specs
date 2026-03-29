# Start Here

> The quick guide to the specs that matter most.

→ **[Full README](../README.md)** — complete documentation & architecture overview

→ **[Full INDEX](../INDEX.md)** — full library of 178 specs

---

## If You're a NIST Reviewer

→ **[NIST Submission Guide](../NIST_SUBMISSION_GUIDE.md)** — 15-minute
guided tour answering all 6 NCCoE concept paper questions

→ **[NIST Crosswalk](../NIST_CROSSWALK.md)** — Direct mapping to
AI RMF (Govern, Map, Measure, Manage) and SP 800-207 Zero Trust

→ **[Atlas — NIST NCCoE Enterprise Finance Bundle](../examples/nist-nccoe-bundle/)** —
Complete financial agent with accountability chain + failure scenarios

---

## If You're Building an Agent

Start with these 5 files:

| File | What It Does | Get It |
|------|-------------|--------|
| [SOUL.md](../specs/identity/SOUL.md) | Personality and values | `curl -O https://raw.githubusercontent.com/totalmarkdown/soul.md/main/SOUL.md` |
| [WHOAMI.md](../specs/identity/WHOAMI.md) | Verifiable identity | `curl -O https://raw.githubusercontent.com/totalmarkdown/whoami.md/main/WHOAMI.md` |
| [LIMITS.md](../specs/governance/LIMITS.md) | Hard stops | `curl -O https://raw.githubusercontent.com/totalmarkdown/limits.md/main/LIMITS.md` |
| [ESCALATION.md](../specs/governance/ESCALATION.md) | Human-in-the-loop | `curl -O https://raw.githubusercontent.com/totalmarkdown/escalation.md/main/ESCALATION.md` |
| [DELEGATION.md](../specs/governance/DELEGATION.md) | Who authorized this agent | `curl -O https://raw.githubusercontent.com/totalmarkdown/delegation.md/main/DELEGATION.md` |

Or download the basic agent bundle (these 5 specs):
```bash
curl -LO https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/basic-agent/bundle.zip
unzip bundle.zip -d my-agent/
```

Then validate:
```bash
pip install git+https://github.com/totalmarkdown/agent-md-validator.git
agent-md-validate ./my-agent/
```

---

## If You're Building a Multi-Agent Team

Add these on top of the 5 above:

| File | What It Does | Get It |
|------|-------------|--------|
| [TEAM.md](../specs/coordination/TEAM.md) | Team structure and handoff protocols | `curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/templates/TEAM.template.md` |
| [SHAREDCONTEXT.md](../specs/coordination/SHAREDCONTEXT.md) | Shared memory governance | `curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/templates/SHAREDCONTEXT.template.md` |
| [MEMORYSAFETY.md](../specs/security/MEMORYSAFETY.md) | Memory poisoning defense | `curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/templates/MEMORYSAFETY.template.md` |
| [CIRCUITBREAKER.md](../specs/operations/CIRCUITBREAKER.md) | Failure containment | `curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/templates/CIRCUITBREAKER.template.md` |
| [BUDGET.md](../specs/governance/BUDGET.md) | Team cost controls | `curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/templates/BUDGET.template.md` |

Or download the [Sentinel — Multi-Agent Fleet Bundle](../examples/multi-agent-fleet/):
```bash
curl -LO https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/multi-agent-fleet/bundle.zip
unzip bundle.zip -d my-fleet/
```

---

## If You Need Enterprise Compliance

| File | What It Does | Get It |
|------|-------------|--------|
| [AUDITTRAIL.md](../specs/compliance/AUDITTRAIL.md) | Tamper-proof action logging | `curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/templates/AUDITTRAIL.template.md` |
| [CONSENT.md](../specs/compliance/CONSENT.md) | User consent lifecycle (GDPR/CCPA) | `curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/templates/CONSENT.template.md` |
| [PROVENANCE.md](../specs/compliance/PROVENANCE.md) | Data lineage tracking | `curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/templates/PROVENANCE.template.md` |
| [ENFORCEMENT.md](../specs/governance/ENFORCEMENT.md) | Policy verification | `curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/templates/ENFORCEMENT.template.md` |
| [ATTESTATION.md](../specs/security/ATTESTATION.md) | Cryptographic identity proof | `curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/templates/ATTESTATION.template.md` |

Or download the [Atlas — NIST NCCoE Enterprise Finance Bundle](../examples/nist-nccoe-bundle/):
```bash
curl -LO https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/examples/nist-nccoe-bundle/bundle.zip
unzip bundle.zip -d my-agent/
```

→ See [NIST Crosswalk](../NIST_CROSSWALK.md) for regulatory mapping.

---

## If You're Listing Agents on a Marketplace

| File | What It Does | Get It |
|------|-------------|--------|
| [HIREME.md](../specs/business/HIREME.md) | Agent hiring listing | `curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/templates/HIREME.template.md` |
| [PRICING.md](../specs/economic/PRICING.md) | Cost structure | `curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/specs/economic/PRICING.md` |
| [WALLET.md](../specs/economic/WALLET.md) | Financial identity | `curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/specs/economic/WALLET.md` |
| [CV.md](../specs/economic/CV.md) | Work history | `curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/specs/economic/CV.md` |
| [TESTSCORES.md](../specs/quality/TESTSCORES.md) | Benchmark results | `curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/specs/quality/TESTSCORES.md` |

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
