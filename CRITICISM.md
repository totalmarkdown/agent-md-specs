# Criticism — Objections We Expect and Our Honest Answers

agent-md-specs is a first draft. It has predictable weaknesses, and
people will point them out. Rather than wait to be critiqued, we're
writing down the top 5 objections we expect — and answering them
honestly.

If you have an objection that isn't on this list, please open a
[Discussion in the Q&A category](https://github.com/totalmarkdown/agent-md-specs/discussions/categories/q-a)
and we'll add it.

---

## 1. "Isn't this just documentation?"

Partly, yes. But the YAML frontmatter in every spec is machine-readable.
A policy engine (OPA/Rego, Cedar), API gateway, or logging pipeline can
consume the same file a compliance officer reads and approves. There is
no drift between the policy humans sign off on and the configuration
machines enforce — because it's the same file.

That said, until there's a working reference integration, "just
documentation" is a fair critique. We acknowledge the gap: building a
reference OPA/Rego demo that reads `LIMITS.md` frontmatter and denies
forbidden tool calls is on the
[ROADMAP](./ROADMAP.md#now--q2-2026-aprilspec-june).

---

## 2. "Why 179 specs? That's absurd."

It looks overwhelming. It isn't meant to be consumed all at once.

The right mental model: **5 files to start (Basic Agent bundle), 47
Core for production-grade agents, 132 Extended when you need them.**
Most agents will never use more than 10-20 specs. A financial-services
agent might use 25; a personal productivity bot might use 5.

The 132 Extended tier exists because different audiences need different
specs: `GDPR.md` matters to a European SaaS team; `HIPAA.md` matters to
a telemedicine agent; `KRYPTONITE.md` (known failure modes) matters to
a safety researcher. Having a named, documented slot for each dimension
is better than an undocumented free-for-all.

If a spec genuinely has no real use cases, it should be demoted or
retired. [Open a Discussion](https://github.com/totalmarkdown/agent-md-specs/discussions/categories/ideas)
proposing removal.

---

## 3. "Why not PR this into AGENTS.md?"

AGENTS.md is deliberately a single file with a small surface area
(build / test / style / project conventions). Pushing identity,
delegation, audit trails, memory safety, and 15 regulatory frameworks
into it would break the format for its 67,000+ current users.

agent-md-specs is a separate, composable vocabulary. AGENTS.md users
can adopt it incrementally — add `LIMITS.md` first, then `DELEGATION.md`,
then `AUDITTRAIL.md` — without changing anything about their existing
AGENTS.md file. The [Forge bundle](./examples/codex-agent-decomposed/)
shows AGENTS.md and agent-md-specs coexisting in one repo.

See [COMPARISON.md](./COMPARISON.md) for the detailed side-by-side.

---

## 4. "Where's the runtime enforcement? These are just Markdown files."

Correct — and that is a deliberate design choice. agent-md-specs
defines **what** should be enforced. Your runtime (OPA/Rego, Cedar,
API gateways, orchestration platforms, CI/CD pipelines) defines **how**
it is enforced.

This separation of concerns is why AGENTS.md and MCP work. You don't
want your governance vocabulary tied to one runtime.

**The honest gap:** no reference integration ships in this repo yet.
We haven't proven the "YAML frontmatter is the bridge" claim with a
working demo. That demo — `totalmarkdown/agent-md-opa-demo` — is the
highest-priority item on the [roadmap](./ROADMAP.md#now--q2-2026-aprilspec-june).
Until it ships, this objection lands.

---

## 5. "Who's actually using this?"

Nobody yet. That's what the Draft stage means.

agent-md-specs was written by one person over 24 days (March 5–29,
2026) and submitted as a public comment on the NIST NCCoE concept
paper on 2026-03-29. It is genuinely a first draft seeking expert
review.

We're asking for:
- **10 reviewers** who will read 2-3 specs closely and tell us where
  we're wrong
- **3 pilot adopters** willing to try the Basic Agent bundle in a real
  project
- **1-2 external maintainers** willing to help run the RFC process

Adoption comes from expert review → improvement → real use cases →
reference integrations → word of mouth. We're at step 1.

If this matters to you, [open a Discussion](https://github.com/totalmarkdown/agent-md-specs/discussions)
or [file an RFC](https://github.com/totalmarkdown/agent-md-specs/issues/new/choose).
Constructive critique is the single highest-leverage contribution
possible at this stage.

---

## Bonus: "Why all the AI-generated-sounding marketing copy?"

The v0.1.0–v1.2.0-nist-submission cadence (8 days end-to-end) left
some rough prose that reads as LLM-assisted. We're editing that out
across v1.3.x; the README has been tightened, and the
`nist-nccoe-response-content.md` schema overclaim was corrected in
v1.3.1. If you find more, open an issue with the "docs" label.

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
