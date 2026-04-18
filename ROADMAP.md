# Roadmap

Living document. Last updated 2026-04-18. Comment via
[Discussions › Roadmap](https://github.com/totalmarkdown/agent-md-specs/discussions/categories/ideas).

agent-md-specs is a proposed vocabulary (draft, seeking review). This
roadmap describes what we are working on, what we are thinking about,
and what we are explicitly not doing. Items are grouped by horizon,
not priority; priority is signalled by the `milestone` on the associated
Issue.

---

## Now — Q2 2026 (April–June)

- **agent-md-validator v0.2** — multi-file bundle validation, frontmatter
  cross-reference checks, CI-friendly exit codes, `--format=json` output,
  downgrade of section-heading checks from required to recommended so
  `--strict` fails only on frontmatter issues.
- **JSON Schema coverage to 100% of Core tier** — currently 24 of 47
  Core specs have schemas in `schemas/`. Ship the remaining 23, one
  tracking issue per schema labelled `schema`.
- **Seed contributor experience** — Issue templates, PR template,
  Discussion templates, 10 `good first issue` tasks, CODE_OF_CONDUCT.md,
  SUPPORT.md. (Mostly shipped with v1.3.0 — see CHANGELOG.)
- **Public RFC #0001** — Formalize the RFC numbering scheme and the
  Draft → Proposed → Stable → Deprecated transition rules.
- **Core spec section-audit** — align the canonical specs in `specs/`
  with the section headings the validator requires in `--strict` mode
  (SOUL, WHOAMI, LIMITS, MEMORYSAFETY, INPUT, OUTPUT).
- **Reference enforcement demo** — `totalmarkdown/agent-md-opa-demo`
  companion repo: sample LIMITS.md + ~50 lines of OPA/Rego that reads
  the frontmatter and denies forbidden tool calls, with an asciinema
  recording of the full flow.

## Next — Q3 2026 (July–September)

- **Proposed → Stable promotions** — candidates: WHOAMI, LIMITS,
  DELEGATION, ESCALATION, AUDITTRAIL. Criteria: ≥2 external adopters,
  90 days in Proposed, no unresolved RFC objections.
- **Technical Steering Committee v1** — seat the first 3 external
  members. Open nominations via Issue template.
- **Reference integrations** — OPA/Rego bundle for ENFORCEMENT.md,
  SPIFFE/SPIRE mapping for ATTESTATION.md, OpenTelemetry schema for
  AUDITTRAIL.md.
- **NIST NCCoE Phase 2 engagement** — follow-up to the v1.2.0 concept
  paper submission; pilot demonstration project if invited.
- **Thin Core spec expansion** — PERMISSIONS, SLA, MONITOR, POLICY,
  BUDGET, SOUL, LIMITS — add Runtime Considerations section and
  populated YAML examples.

## Later — Q4 2026 and beyond

- **Foundation hosting evaluation** — assess neutral-governance
  candidates: LF AI & Data, OpenSSF, AAIF, CNCF Sandbox. Decision
  target: end of Q4 2026.
- **Standards body alignment** — NIST AI RMF 2.0 input, ISO/IEC JTC
  1/SC 42 liaison, IETF BoF on agent identity.
- **Extended tier v2** — 50+ additional specs identified but gated on
  contributor bandwidth; see open RFCs.
- **Tooling ecosystem** — VS Code extension, GitHub Action for bundle
  validation, pre-commit hooks, Backstage plugin, Docker image for
  `agent-md-validator`.

## Out of Scope

- **A runtime enforcement engine.** Use OPA, Cedar, or your policy
  stack. agent-md-specs defines what to enforce, not how.
- **A hosting service for `.md` specs.** They live in your repo.
- **A competing standard to AGENTS.md / CLAUDE.md / MCP.** We extend
  them — see [COMPARISON.md](./COMPARISON.md).
- **Prescriptive model choices.** Specs are model-agnostic by design.

## How to Influence the Roadmap

- Open an Issue with label `roadmap` proposing additions/removals.
- Comment on the Q3 planning discussion pinned in Discussions.
- Submit an RFC via `.github/ISSUE_TEMPLATE/new_spec_rfc.yml`.

## Contributor Onboarding Path

1. Read [`_start-here/README.md`](./_start-here/README.md) and run
   the basic-agent bundle.
2. Pick an Issue labelled `good first issue`.
3. Comment to claim it. A maintainer responds within 48h.
4. Open a PR referencing the Issue. CI runs schema + link checks.
5. After your first merged PR, you can self-assign further Issues.

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
