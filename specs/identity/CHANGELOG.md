---
spec_name: CHANGELOG.md
spec_version: 0.1.0
category: Identity
domain: changelogmd.dev
priority: Medium
volume: "Vol 4 — Economic Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# CHANGELOG.md

**Category:** Identity
**Domain:** 
**Priority:** Medium
**Version:** 0.1.0

### Purpose
Version history for an agent bundle — what changed in each version, 
what was fixed, what was added, and whether updates are breaking.
Standard CHANGELOG.md format adapted for agent configuration files.
_See VERSIONING.md for the versioning strategy that drives this log._

### Spec

```markdown
---
agent_name: string
current_version: semver
---

# [Agent Name] — Changelog

All notable changes to this agent are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com).

## [Unreleased]
Changes being developed but not yet released.

### Planned
- [Upcoming feature]

---

## [1.2.0] — YYYY-MM-DD

### Added
- [New capability or file added to bundle]
- [New skill or tool integration]

### Changed
- [Behavior that changed — non-breaking]
- [Performance improvement]

### Fixed
- [Bug that was fixed]
- [Incorrect behavior corrected]

### Deprecated
- [Feature that will be removed in next major version]

### Removed
- [Feature removed in this version]

### Security
- [Security fix — describe without giving exploit details] (see AUDITTRAIL.md)

---

## [1.1.0] — YYYY-MM-DD

[Same format]

---

## [1.0.0] — YYYY-MM-DD — Initial Release

### Added
- Initial bundle with [list of files]
- [Core capabilities]

---

## Version Compatibility
| Agent version | Model required | Breaking changes |
|--------------|---------------|-----------------|
| 2.x | Claude Sonnet 4+ | Yes — see migration guide |
| 1.x | Claude Sonnet 3+ | No |

## Migration Guides
- [1.x → 2.x](./migrations/v1-to-v2.md)
```

## Example Use Cases

**Enterprise:** Before upgrading an agent from v1.x to v2.x, a platform team reviews the changelog to identify breaking changes — discovering the output format changed from JSON to structured markdown — and schedules downstream consumer updates before deploying the new version.

**Multi-Agent Fleet:** A fleet management dashboard aggregates changelogs from all 50 agents to generate a weekly "what changed" digest for the operations team, highlighting any security fixes or deprecated features that need attention.

**Regulated Industry:** An FDA-regulated manufacturing agent maintains a changelog that maps every configuration change to a specific change control ticket, providing auditors with a complete, timestamped history of what was modified and why for each validated version.

## Related Specs

| Spec | Relationship |
|------|-------------|
| ATTESTATION.md | Identity verification and credential lifecycle |
| CONTACT.md | Reachable endpoints |
| ENFORCEMENT.md | Policy verification and compliance |
| SOUL.md | Agent personality and values |
| WHOAMI.md | Agent identity declaration |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
