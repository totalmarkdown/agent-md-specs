# Changelog

All notable changes to agent-md-specs are documented here.

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
- Frontmatter consistency across all 178 specs
- Schema category enum expanded to match all specs
- All 5 example bundles pass validator with 0 errors
- Standalone repos updated to 178 count
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
