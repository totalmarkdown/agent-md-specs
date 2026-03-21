---
spec_name: BACKUP.md
spec_version: 0.1.0
category: Operations
domain: backupmd.dev
priority: Medium
volume: "Vol 2 — Extended Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# BACKUP.md

**Category:** Operations
**Domain:** backupmd.dev
**Priority:** Medium
**Version:** 0.1.0

### Purpose
Documents backup and recovery procedures for agent state, 
configuration, and data.

### Spec

```markdown
---
agent_name: string
version: semver
backup_frequency: string   # hourly | daily | weekly
retention_period: string
backup_location: string
created: date
updated: date
---

# [Agent Name] — Backup Configuration

## What Gets Backed Up
| Component | Frequency | Retention | Location | Method |
|-----------|-----------|-----------|----------|--------|
| MEMORY.md | [frequency] | [period] | [location] | [method] |
| SQLite database | [frequency] | [period] | [location] | [method] |
| Agent config files | On change | [period] | Git | Commit |
| [Other] | [frequency] | [period] | [location] | [method] |

## Backup Schedule
- Full backup: [schedule]
- Incremental: [schedule]
- Config snapshot: on every meaningful change (git commit)

## Recovery Procedure
```bash
# Restore from latest backup
[restore command]

# Restore from specific date
[restore command with date parameter]

# Verify restore
[verification command]
```

## Recovery Time Objectives
- RTO (Recovery Time): < [X hours]
- RPO (Recovery Point): < [X hours] of data loss acceptable

## Backup Monitoring
- Alert if backup fails: [yes — via MONITOR.md alert rules]
- Verify backup integrity: [weekly test restore]
- Backup size trending: [monitor for unexpected growth]
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
