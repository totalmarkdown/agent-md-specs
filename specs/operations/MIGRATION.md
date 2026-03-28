---
spec_name: MIGRATION.md
spec_version: 0.1.0
category: Operations
domain: migrationmd.dev
priority: Medium
volume: "Vol 2 — Extended Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# MIGRATION.md

**Category:** Operations
**Domain:** migrationmd.dev
**Priority:** Medium
**Version:** 0.1.0

### Purpose
Documents how to migrate data, configuration, and state when 
upgrading an agent to a new major version or moving between 
environments.

### Spec

````markdown
---
from_version: semver
to_version: semver
migration_type: string    # config | data | full
reversible: boolean
estimated_duration: string
created: date
---

# Migration Guide: v[X] → v[Y]

## Overview
**Type:** [config-only | data migration | full migration]  
**Reversible:** [yes | no — read carefully before proceeding]  
**Estimated time:** [duration]  
**Requires downtime:** [yes — [duration] | no]

## What's Changing
| Component | Old behavior | New behavior | Migration needed |
|-----------|-------------|-------------|-----------------|
| [config field] | [old] | [new] | [yes/no + how] |

## Pre-Migration Checklist
- [ ] Backup current state: [backup command] (see BACKUP.md)
- [ ] Verify backups are accessible
- [ ] Notify dependent agents/teams [N hours] in advance
- [ ] Run current test suite — all passing
- [ ] Read full migration guide before starting

## Migration Steps
```bash
# Step 1: [description]
[command]

# Step 2: [description]  
[command]

# Verify: [what to check]
[verification command]
```

## Post-Migration Verification
- [ ] All tests passing with new version
- [ ] Key workflows functioning: [list]
- [ ] Monitor for [X hours] for unexpected behavior (see HEALTHCHECK.md)
- [ ] Update handoff notes and MEMORY.md if needed

## Rollback Procedure
If migration fails:
```bash
[rollback commands]
```
Rollback restores to pre-migration state from backup.
Note: [any data loss risks if rolling back]
````

## Example Use Cases

**Enterprise:** An advertising platform migrates its campaign-optimization agents from GPT-4 to Claude, using MIGRATION.md to document prompt format changes, MEMORY.md schema updates, and a 48-hour parallel-run verification period before cutting over.

**Multi-Agent Fleet:** A fleet-wide migration from v2 to v3 of the agent framework rolls out team-by-team over two weeks, with each team's MIGRATION.md documenting its specific config changes, rollback commands, and post-migration health monitoring windows.

**Regulated Industry:** A banking compliance agent migrating to a new transaction-monitoring schema documents the exact field mappings, data validation steps, and regulatory sign-off requirements, ensuring no gap in suspicious-activity detection during the transition.

## Related Specs

| Spec | Relationship |
|------|-------------|
| CIRCUITBREAKER.md | Failure containment and blast radius |
| ENFORCEMENT.md | Policy verification and compliance |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| HEALTHCHECK.md | Liveness and readiness checks |
| MEMORY.md | Individual agent memory governance |
| MONITOR.md | Observability and alerting |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
