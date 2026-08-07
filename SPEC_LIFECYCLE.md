# Specification Lifecycle

How agent-md-specs specifications are proposed, reviewed, matured, and deprecated.

---

## Lifecycle Stages

Every spec progresses through these stages:

```
Draft -> Proposed -> Stable -> Deprecated -> Retired
```

A spec's stage is recorded in its `status:` frontmatter field, not in its
version number. See [Versioning](#versioning) for why the two are
independent, and `schemas/spec-document.schema.json` for the machine-
readable definition — `status` is required on every spec and CI rejects a
value outside `draft | proposed | stable | deprecated | retired`.

### Draft
- **Frontmatter:** `status: draft`
- **Who can create:** Anyone, via PR or GitHub Discussion
- **Requirements:** YAML frontmatter, Purpose section, at least 1 use case
- **Review:** Maintainer review for scope and non-duplication
- **Stability:** May change significantly between versions
- **Commitment:** No backward compatibility guarantees

### Proposed
- **Frontmatter:** `status: proposed` and `proposed_on: YYYY-MM-DD` (the
  date the comment window opened)
- **Requirements:** Complete template with all required sections, at least
  2 documented real-world use cases, passes agent-md-validator Level 2,
  JSON Schema defined (for Core specs)
- **Review:** 14-day community review period via GitHub Discussion
- **Stability:** Structure is settling; breaking changes require RFC
- **Commitment:** Best-effort backward compatibility

### Stable
- **Frontmatter:** `status: stable`
- **Requirements:** Passes Level 3 validation, at least 1 example
  bundle using this spec, no unresolved issues for 30 days, at least 2
  independent implementations or adoption references
- **Review:** Formal review by maintainers + community vote in Discussions
- **Stability:** Breaking changes only in major versions with migration guide
- **Commitment:** Full backward compatibility within major version

**What "passes Level 3" means, concretely.** Level 3 is defined in
[schemas/README.md](./schemas/README.md#conformance-levels) as field values
conforming to their type constraints and enums. For a spec, it is checked
against the instance documents that use it: the spec publishes a per-spec
JSON Schema, at least one example bundle ships a document for that spec,
and every such document validates against that schema. `tools/validate_corpus.py
--stable-gate` reports this for all 179 specs, so the criterion is a number
a reviewer can read rather than a check nobody runs. Level 3 evidence is
necessary but not sufficient — the review, adoption and 30-day criteria
above are assessed by maintainers.

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

As of v1.3.1, **5** of the 179 specs are at **Proposed** stage —
AUDITTRAIL, ATTESTATION, DELEGATION, INTENT and LEASTPRIVILEGE, promoted
on 2026-04-18 with comment windows open from that date. The remaining
**174** specs are at **Draft** stage.

Proposed carries best-effort backward compatibility and requires an RFC
for breaking changes; Draft carries no backward compatibility guarantee.
Every spec states its own stage in `status:` frontmatter, and CI fails if
this section and the corpus disagree.

The remaining Vol 14 NIST-aligned specs (ENFORCEMENT, PROMPTSHIELD,
PROVENANCE, SESSION) are candidates for advancement to **Proposed** stage
pending community review and NIST feedback.

---

## Versioning

### Individual Specs
Each spec has its own semantic version in YAML frontmatter:
- **Patch** (0.1.1): Typo fixes, clarifications, non-breaking additions
- **Minor** (0.2.0): New optional sections, expanded templates
- **Major** (1.0.0): Breaking changes to required fields or structure

**Stage and version are independent.** A spec's lifecycle stage is what
`status:` says; it is not inferred from the version number, and reaching
any particular version does not promote a spec. While `spec_version` is
below `1.0.0` the spec is in initial development under
[semver §4](https://semver.org/#spec-item-4): a breaking change to a Draft
or Proposed spec bumps the **minor** version and leaves `status:`
untouched. Promotion to Stable is a separate governance act with its own
criteria, and a Stable spec's first breaking change is what takes it to
`1.0.0` and beyond.

Earlier revisions of this document wrote the stages as `Draft (v0.x.x)`,
`Proposed (v0.5.0+)` and `Stable (v1.0.0+)`. That encoding made the most
common governance action inexpressible: a breaking fix to a Proposed spec
at `0.1.0` would go to `1.0.0` by semver, which the same document read as
a promotion to Stable — a stage the spec does not qualify for. The stage
ranges are removed; `status:` is authoritative.

### Library Version
The agent-md-specs library as a whole uses date-based volume versioning
(Vol 1-16) combined with semantic releases (current: v1.3.1).
- **Patch**: Bug fixes, frontmatter corrections
- **Minor**: New Extended specs, non-breaking additions to existing specs
- **Major**: New Core specs, breaking changes to Core spec structure,
  tier reclassifications

---

## RFC Process (for Core Spec Changes)

Changes to Core tier specs (47 specs) require a lightweight RFC:

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
