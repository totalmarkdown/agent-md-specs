---
spec_name: VERSION.md
spec_version: 0.1.0
category: Technical
priority: Medium
volume: "Vol 5 — Organizational & Validation"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
status: draft
spec_type: static
---


# VERSION.md

**Category:** Technical
**Priority:** Medium
**Version:** 0.1.0 **Type:** Static

### Purpose
The current version snapshot — what version this agent is right now, 
what changed in this version, and how to upgrade. Where CHANGELOG.md 
is the full history, VERSION.md is just the current moment.
Optimized for quick machine-readable version checking.

### Spec

````markdown
---
agent_name: string
current_version: semver
released: date
previous_version: semver
breaking_changes: boolean
---

# [Agent Name] — Version [X.Y.Z]

## Current Version
**Version:** [X.Y.Z]  
**Released:** [Date]  
**Status:** [stable | beta | deprecated]  
**Model:** [See MODEL.md — current model version]

## What's New in [X.Y.Z]
[2-3 sentence summary of most important changes]

### Added
- [New capability]
- [New file in bundle]

### Changed
- [Modified behavior — note if breaking]

### Fixed
- [Bug fixed]

### Breaking Changes
[If any — what breaks and how to fix it]  
Migration guide: [link or inline if small]

## Quick Upgrade
```bash
# Install latest version
tmd marketplace update [agent-name]

# Verify version
[agent-name] --version
# Expected output: [agent-name] v[X.Y.Z]
```

## Version Support
| Version | Status | Supported until |
|---------|--------|----------------|
| [X.Y.Z] | ✅ Current | Indefinite |
| [X.Y-1.Z] | ⚠ Maintenance | [date] |
| [X-1.Y.Z] | ❌ EOL | Unsupported |

## Full History
See CHANGELOG.md for complete version history and DEPENDENCIES.md for version compatibility.

## Check for Updates
```bash
tmd marketplace check-update [agent-name]
```
````

## Example Use Cases

**Enterprise:** A platform team uses VERSION.md to quickly check which version of their deployment agent is running in production, verify whether breaking changes exist, and run the one-line upgrade command when a new stable release is available.

**Multi-Agent Fleet:** A marketplace operator reads VERSION.md from all listed agents to display version badges, support status (current/maintenance/EOL), and "update available" notifications to users who have installed older versions.

**Regulated Industry:** A compliance officer uses VERSION.md's version support table to verify that the organization's regulatory filing agent is on a currently supported version, scheduling an upgrade before the maintenance version reaches end-of-life to maintain audit compliance.

## Related Specs

| Spec | Relationship |
|------|-------------|
| INPUT.md | Accepted input formats |
| MCP.md | Model Context Protocol connections |
| OUTPUT.md | Output formats and delivery |
| PERMISSIONS.md | Static resource access control |
| TOOLS.md | Available tools and capabilities |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
