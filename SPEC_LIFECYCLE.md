# Specification Lifecycle

How agent-md-specs specifications are proposed, reviewed, matured, and deprecated.

---

## Lifecycle Stages

Every spec progresses through these stages:

```
Draft -> Proposed -> Stable -> Deprecated -> Retired
```

### Draft (v0.x.x)
- **Who can create:** Anyone, via PR or GitHub Discussion
- **Requirements:** YAML frontmatter, Purpose section, at least 1 use case
- **Review:** Maintainer review for scope and non-duplication
- **Stability:** May change significantly between versions
- **Commitment:** No backward compatibility guarantees

### Proposed (v0.5.0+)
- **Requirements:** Complete template with all required sections, at least
  2 documented real-world use cases, passes agent-md-validator Level 2,
  JSON Schema defined (for Core specs)
- **Review:** 14-day community review period via GitHub Discussion
- **Stability:** Structure is settling; breaking changes require RFC
- **Commitment:** Best-effort backward compatibility

### Stable (v1.0.0+)
- **Requirements:** Passes agent-md-validator Level 3, at least 1 example
  bundle using this spec, no unresolved issues for 30 days, at least 2
  independent implementations or adoption references
- **Review:** Formal review by maintainers + community vote in Discussions
- **Stability:** Breaking changes only in major versions with migration guide
- **Commitment:** Full backward compatibility within major version

### Deprecated
- **Trigger:** Superseded by another spec, or no longer relevant
- **Process:** 90-day deprecation notice, migration guide to replacement
- **Stability:** No new features; security fixes only
- **Frontmatter:** Add `status: deprecated` and `superseded_by: [SPEC.md]`

### Retired
- **Trigger:** 90 days after deprecation with no objections
- **Process:** Moved to archive/ directory, removed from INDEX.md
- **Stability:** No changes
- **Frontmatter:** Add `status: retired`

---

## Current Status

All 178 specs in agent-md-specs v1.1.0 are at **Draft** stage.

The Vol 14 NIST-aligned specs (DELEGATION, INTENT, LEASTPRIVILEGE,
ENFORCEMENT, ATTESTATION, PROMPTSHIELD, AUDITTRAIL, PROVENANCE,
SESSION) are candidates for advancement to **Proposed** stage pending
community review and NIST feedback.

---

## Versioning

### Individual Specs
Each spec has its own semantic version in YAML frontmatter:
- **Patch** (0.1.1): Typo fixes, clarifications, non-breaking additions
- **Minor** (0.2.0): New optional sections, expanded templates
- **Major** (1.0.0): Breaking changes to required fields or structure

### Library Version
The agent-md-specs library as a whole uses date-based volume versioning
(Vol 1-16) combined with semantic releases (v1.0.0).
- **Patch**: Bug fixes, frontmatter corrections
- **Minor**: New Extended specs, non-breaking additions to existing specs
- **Major**: New Core specs, breaking changes to Core spec structure,
  tier reclassifications

---

## RFC Process (for Core Spec Changes)

Changes to Core tier specs (39 specs) require a lightweight RFC:

1. **Open a GitHub Discussion** in the "Ideas" category
2. **Title format:** `RFC: [Change description] for [SPEC.md]`
3. **Include:** Motivation, proposed change, backward compatibility impact,
   migration guide if breaking
4. **Review period:** 14 days minimum for Proposed specs, 30 days for Stable
5. **Approval:** Maintainer approval + no unresolved blocking objections
6. **Implementation:** Submit PR referencing the RFC discussion

Extended tier specs follow a lighter process (PR + maintainer review).

---

## Tier Promotion

Specs can move between tiers:

### Extended -> Core
- **Criteria:** Demonstrated adoption, addresses a widely-needed capability,
  passes Level 3 validation, has JSON Schema, has example bundle usage
- **Process:** RFC with 30-day review period + community vote

### Core -> Extended (demotion)
- **Criteria:** Low adoption, superseded by better approach, or scope too narrow
- **Process:** RFC with 30-day review period + migration guide

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
