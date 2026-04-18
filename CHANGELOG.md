# Changelog

All notable changes to agent-md-specs are documented here.

## [1.3.1] — 2026-04-18

This release addresses findings from two independent pre-launch
reviews. No Core specs change semantically; all changes are corrections,
community-file additions, governance formalization, and five spec
promotions from Draft to Proposed stage.

### Added

- **CODE_OF_CONDUCT.md** (Contributor Covenant v2.1).
- **ROADMAP.md** (Now / Next / Later / Out of Scope + contributor
  onboarding path).
- **SUPPORT.md** (routes for questions, bugs, security, governance).
- **CITATION.cff** (academic citation metadata).
- **COMPARISON.md** (side-by-side vs AGENTS.md, CLAUDE.md, SKILL.md,
  .cursorrules, program.md, MCP, Markform).
- **CRITICISM.md** (pre-emptive answers to 5 predictable objections).
- **Issue templates** (`.github/ISSUE_TEMPLATE/{bug_report,spec_proposal,new_spec_rfc,config}.yml`)
  and PR template (`.github/PULL_REQUEST_TEMPLATE.md`) with CC0 ack
  and validator checkbox.
- **CODEOWNERS** at `.github/CODEOWNERS`.
- **"Project Status and Timeline"** section in README — honest framing
  of the 8-day v0.1.0 → v1.2.0-nist-submission cadence and the Draft
  stage of all specs.
- **"About This Draft"** section in README — one-person-24-days origin
  disclosure, explicit ask for reviewers and pilot adopters.
- **Proposed stage** for 5 Core specs (14-day public comment windows
  opened): AUDITTRAIL, DELEGATION, ATTESTATION, INTENT, LEASTPRIVILEGE.
  Frontmatter now carries `status: proposed` and `proposed_on: 2026-04-18`.
- **Custom GitHub labels** (`rfc`, `rfc:core`, `spec:new`, `spec:amendment`,
  `schema`, `tier:core`, `tier:extended`, `roadmap`, `validator`).
- **Companion repo**
  [totalmarkdown/agent-md-opa-demo](https://github.com/totalmarkdown/agent-md-opa-demo)
  — working OPA/Rego reference integration that enforces `LIMITS.md`
  frontmatter at runtime; linked from README "See it enforce" section.

### Changed

- **agent-md-validator v0.2.0** — `--strict` mode no longer fails on
  missing recommended section headings or absent cross-references.
  These are now `info`-level notices. `--strict` still fails on
  frontmatter errors, missing required fields, and invalid tier values.
  Result: `agent-md-validate --strict specs/` and all 7 example bundles
  now PASS.
- **GOVERNANCE.md** expanded from 40 → 200 lines. Adds RFC specifics
  (2 approvals + 14-day window), TSC scoping (1 seat → 5 target by
  Q4 2026, nomination process), DCO policy, succession / bus-factor
  clause, naming policy, decision-log pointer, multi-contact security
  reviewer plan.
- **SPEC_LIFECYCLE.md** — stale references updated (`v1.1.0` → `v1.3.0`,
  Core count `39` → `47`).
- **INDEX.md** — Extended count corrected (`133` → `132`).
- **README.md** — Technical category count corrected (`17` → `18`);
  "Standalone Standards" section renamed to "Standalone Companion
  Repositories"; "NIST Alignment" renamed to "Mapping to NIST
  Publications" with explicit non-endorsement language; opening prose
  tightened (removed AI-prose "Something remarkable…", 7-question
  barrage reduced to 3, fabricated 2028 tense cut); "5 files to start,
  47 Core for production, 132 Extended when you need them" framing
  added.
- **schemas/README.md** — "agent-md-specs standard" → "agent-md-specs
  specification"; added missing HEARTBEAT.md row.
- **_start-here/README.md** — reordered: "Building an Agent" now first,
  "Evaluating the Framework" second, "Reviewing the NCCoE Submission"
  third; 4-command TL;DR added to top; expected-output line added
  after `agent-md-validate`; 5 individual curl commands collapsed into
  `<details>` fallback.
- **NIST_SUBMISSION_GUIDE.md** — title changed from "NIST NCCoE
  Reviewer Guide" to "Reviewer Guide for the NCCoE Submission".
- **nist-nccoe-response-content.md** — JSON Schema overclaim corrected
  (3 instances: "every Core spec has a schema" → truth: 24 of 47,
  remaining 23 planned); AI-prose rewrite on lines 16 and 93.
- **GitHub repo description** updated to include "draft, seeking review"
  and correct spec count (179, was 178).

### Fixed

- **10 broken relative links** in `examples/basic-agent/README.md` and
  `examples/marketplace-agent/README.md` — used `../specs/` but the
  correct path is `../../specs/`.
- **Duplicate CHANGELOG [1.1.0] entry** — the 2026-03-26 entry is now
  correctly labelled `[1.0.1]`.
- **`.github/workflows/check-links.yml`** — rewritten in Python so
  relative `..` segments are normalized and fenced code blocks are
  skipped. The previous script hardcoded a file list and missed the
  `../specs/` bugs.

### Seeded

- 11 Issues (10 `good first issue` + 1 tracking Issue for the C1
  proper fix).
- 5 RFC Issues (one per Draft → Proposed promotion, `rfc:core` label).
- 3 substantive Discussions in Ideas category (Core/Extended boundary,
  Markdown format rationale, AGENTS.md complementarity).

## [1.3.0] — 2026-04-03

### Added
- HEARTBEAT.md promoted to Core tier — periodic proactive execution cycles, status reporting, cost controls, and delivery routing
- HEARTBEAT.template.md template for quick adoption
- heartbeat.schema.json JSON Schema for validation
- Domain column added to Standalone Companion Repositories table in README.md

### Changed
- Spec counts updated: 47 Core, 132 Extended, 179 total
- Cross-references added to HEALTHCHECK.md, MONITOR.md, SLA.md, CIRCUITBREAKER.md, WAKEUP.md, SESSION.md, BUDGET.md

## [1.2.0-nist-submission] — 2026-03-29

### Added
- 2 new example bundles: Basic Agent (5 starter specs), Marketplace Agent (5 listing specs)
- bundle.zip downloads for all 7 example bundles
- curl download commands in every _start-here section (multi-agent team, enterprise compliance, marketplace)
- Team/fleet context added to README intro and "Why Does This Exist?" section
- Mermaid diagram replaced: individual nodes → block-level cluster view (9 functional clusters)
- spec_type field (static/runtime_schema) added to all 179 specs

### Fixed
- Missing required frontmatter in basic-agent and marketplace-agent template files
- Validation errors: 16 errors → 0 errors in basic-agent bundle

### Changed
- All example bundle display names aligned to folder names (e.g., "Aria — Customer Support Bundle", "Atlas — NIST NCCoE Enterprise Finance Bundle")
- Example READMEs standardized to consistent structure across all 7 bundles
- Metadata display refactored from banner to inline format across all specs
- NIST Submission Guide and Crosswalk references updated with consistent naming

## [1.1.0] — 2026-03-28

### Added
- _start-here/ directory — curated entry point for 5 audiences
- Inline cross-references across all 179 specs (~500+ references)
- Example Use Cases section added to all 179 specs
- Related Specs navigation tables on all 179 specs
- Category READMEs enriched with descriptions, relationships, and use cases
- CI workflows: validate-specs.yml and check-links.yml
- Canonical source notices on all 10 standalone repos
- Issue template redirects on all standalone repos
- NIST alignment callout in README

### Fixed
- PyPI install claim → git+https install from GitHub
- Schema count claim corrected (24, not 46)
- OWASP/NIST peer-review language softened
- Ghost references (AGENTCARD.md, HANDOFF.md) removed
- Stale counts in SPEC_LIFECYCLE.md and GOVERNANCE.md
- Domain typos (HIREME.md, NISTAIRF.md)
- Duplicate Example Use Cases sections renamed
- ASCII diagram rendering in 6 specs (4-backtick fences)
- Standalone repo READMEs standardized to consistent structure
- All 10 standalone repos synced with latest spec files

### Changed
- README subtitle tightened with Zero Trust positioning
- README leads with "46 Core specs" instead of "179 specs"
- Core Specs tables now have clickable links to spec files
- README framing: "proposed standard" throughout

## [1.0.1] — 2026-03-26

### Added
- Vol 15: Shared Context & Memory Governance
  - SHAREDCONTEXT.md — multi-agent shared memory pool governance
  - MEMORYSAFETY.md — memory poisoning defense and integrity verification
  - MEMORY.md upgraded to Core tier with scope declaration
- Vol 16: Resilience & Consent
  - CIRCUITBREAKER.md — failure containment and cascading prevention
  - CONSENT.md — user consent lifecycle (GDPR, CCPA, EU AI Act)
- JSON Schemas for all Vol 15-16 specs + expanded schema coverage
- Templates for top 23 specs
- Atlas example bundle updated with Vol 15-16 specs
- Static vs Runtime distinction in README and NIST_CROSSWALK.md
- Scope Boundary sections in Vol 14 governance specs
- SPEC_LIFECYCLE.md — formal Draft → Stable progression
- SECURITY.md — vulnerability reporting policy
- READMEs added to all spec category directories
- READMEs added to all example bundles
- Standalone repos restructured (10 repos aligned to top specs)

### Fixed
- All broken cross-references resolved
- Frontmatter consistency across all 179 specs
- Schema category enum expanded to match all specs
- All 5 example bundles pass validator with 0 errors
- Standalone repos updated to 179 count
- README softened to "proposed standard"
- NIST_CROSSWALK.md enforcement mapping expanded with ZTA references

## [1.0.0] — 2026-03-25

### Added
- Vol 14: Agent Identity & Accountability (9 NIST-aligned specs)
  - DELEGATION.md, INTENT.md, LEASTPRIVILEGE.md, ENFORCEMENT.md
  - ATTESTATION.md, PROMPTSHIELD.md
  - AUDITTRAIL.md, PROVENANCE.md
  - SESSION.md
- NIST_CROSSWALK.md mapping to AI RMF and NCCoE concept paper
- GOVERNANCE.md with spec management process
- Core/Extended tiering (39 core, 135 extended)
- 5 example bundles (Aria, Atlas, Nova, Forge, Sentinel Crew)
- agent-md-validator v0.1.0 (separate repo)

### Fixed
- Spec count consistency (all references now 174)
- Ghost spec references removed (SCHEMA, TOKENS)
- NETWORK.md duplicate resolved (social → CONNECTIONS.md)
- Duplicated metadata removed from 96+ spec files
- Category misplacements corrected in README

## [0.1.0] — 2026-03-21

### Added
- Initial release: 165 specs across 13 volumes
- 9 standalone repos (team.md, soul.md, etc.)
- CC0 public domain license
