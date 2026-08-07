---
spec_name: VERSIONING.md
spec_version: 0.1.0
category: Governance
priority: High
volume: "Vol 2 — Extended Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
status: draft
spec_type: static
---


# VERSIONING.md

**Category:** Governance
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose
Defines the versioning strategy for an agent's configuration files — 
how versions are numbered, what constitutes a breaking change, 
how consumers are notified, and deprecation timelines.

### Spec

```markdown
---
agent_name: string
current_version: semver
version_strategy: string   # semver | calver | custom
breaking_change_policy: string
deprecation_notice_period: string  # e.g. "30 days"
created: date
updated: date
---

# [Agent Name] — Versioning Policy

## Version Format
Using: [Semantic Versioning (MAJOR.MINOR.PATCH)]

- **MAJOR:** Breaking changes — agents/systems using this must update
- **MINOR:** New capabilities added, backward compatible
- **PATCH:** Bug fixes, clarifications, non-breaking updates

## What Counts as a Breaking Change
Breaking (requires MAJOR bump):
- Removing a required input field
- Changing the output format
- Removing a capability listed in Agent Card (see WHOAMI.md)
- Changing authentication requirements
- Renaming the agent ID

Non-breaking (MINOR or PATCH):
- Adding new optional capabilities
- Improving output quality without format change
- Adding new optional input fields
- Performance improvements
- Documentation improvements

## Change Notification
| Change type | Notice period | Channels |
|------------|---------------|---------|
| Breaking change | [30 days] | [how notified] |
| Deprecation | [60 days] | [how notified] |
| Minor change | [7 days] | [how notified] |
| Patch | Immediate | CHANGELOG.md |

## Deprecation Process
1. Mark feature as deprecated in relevant MD file
2. Add to CHANGELOG.md with removal date
3. Notify dependents via [channel]
4. Run in parallel with replacement for [N days]
5. Remove on scheduled date

## Version History
See CHANGELOG.md for full history (see CHANGELOG.md).

Current: [version]  
Previous: [version] — [still supported until date | EOL]  
LTS: [version if any] — [support until date]
```

## Example Use Cases

**Enterprise:** When an agent's output format changes from JSON to structured markdown, the change is classified as a MAJOR version bump, and all 15 downstream systems consuming the agent's output receive a 30-day deprecation notice before the old format is retired.

**Multi-Agent Fleet:** A fleet orchestrator checks each agent's version at boot time, refusing to route tasks to any agent running a deprecated configuration version and alerting the platform team when agents fall behind the minimum supported version.

**Regulated Industry:** A medical device reporting agent maintains an LTS version branch that receives only security patches for 24 months, ensuring that validated configurations used in FDA-regulated workflows remain stable while newer features are developed on the latest version.

## Related Specs

| Spec | Relationship |
|------|-------------|
| DELEGATION.md | Authority chain and authorization |
| ENFORCEMENT.md | Policy verification and compliance |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| LIMITS.md | Hard constraints and safety boundaries |
| PERMISSIONS.md | Static resource access control |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
