# Start Here

> The quick guide to the specs that matter most.
> For the full library of 178 specs, see [INDEX.md](../INDEX.md).

→ **[Full README](../README.md)** — complete documentation, architecture overview, and all 178 specs

---

## If You're a NIST Reviewer

→ **[NIST Submission Guide](../NIST_SUBMISSION_GUIDE.md)** — 15-minute
guided tour answering all 6 NCCoE concept paper questions

→ **[NIST Crosswalk](../NIST_CROSSWALK.md)** — Direct mapping to
AI RMF (Govern, Map, Measure, Manage) and SP 800-207 Zero Trust

→ **[Atlas Enterprise Example](../examples/nist-nccoe-bundle/)** —
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

Then validate:
```bash
pip install git+https://github.com/totalmarkdown/agent-md-validator.git
agent-md-validate ./my-agent/
```

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

→ See the [Sentinel Crew example](../examples/multi-agent-fleet/) for
a working 3-agent fleet configuration.

---

## If You Need Enterprise Compliance

| File | What It Does |
|------|-------------|
| [AUDITTRAIL.md](../specs/compliance/AUDITTRAIL.md) | Tamper-proof action logging |
| [CONSENT.md](../specs/compliance/CONSENT.md) | User consent lifecycle (GDPR/CCPA) |
| [PROVENANCE.md](../specs/compliance/PROVENANCE.md) | Data lineage tracking |
| [ENFORCEMENT.md](../specs/governance/ENFORCEMENT.md) | Policy verification |
| [ATTESTATION.md](../specs/security/ATTESTATION.md) | Cryptographic identity proof |

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

---

## Example Bundles

| Bundle | What It Shows |
|--------|--------------|
| [Atlas (NIST)](../examples/nist-nccoe-bundle/) | Enterprise financial agent — full accountability chain |
| [Sentinel Crew](../examples/multi-agent-fleet/) | 3-agent team with hierarchy |
| [Aria](../examples/customer-support-bundle/) | Simple customer support agent |
| [Nova](../examples/autoresearch-decomposed/) | Monolithic config → decomposed specs |
| [Forge](../examples/codex-agent-decomposed/) | AGENTS.md + agent-md-specs together |

---

*[Full Index](../INDEX.md) · [README](../README.md) · [NIST Crosswalk](../NIST_CROSSWALK.md) · [Contributing](../CONTRIBUTING.md)*
