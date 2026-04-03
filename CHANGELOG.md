# Changelog

All notable changes to agent-md-specs are documented here.

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

## [1.1.0] — 2026-03-26

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
