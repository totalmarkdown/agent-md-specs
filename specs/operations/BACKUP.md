---
spec_name: BACKUP.md
spec_version: 0.1.0
category: Operations
domain: backupmd.dev
priority: Medium
volume: "Vol 2 — Extended Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
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

_See AUDITTRAIL.md for compliance records that must survive restores._

## Backup Monitoring
- Alert if backup fails: [yes — via MONITOR.md alert rules]
- Verify backup integrity: [weekly test restore]
- Backup size trending: [monitor for unexpected growth]
- For migrating backups between environments, see LEGACY.md
```


```
## Example Use Cases

**Enterprise:** An e-commerce company backs up its product-recommendation agent's learned preferences and MEMORY.md every hour to S3, with a 4-hour RPO, so that a corrupted model state can be rolled back without losing an entire day of customer interaction data.

**Multi-Agent Fleet:** A 50-agent content moderation fleet uses BACKUP.md to coordinate staggered backup windows, ensuring no more than 10% of agents are performing full state snapshots simultaneously to avoid fleet-wide performance degradation.

**Regulated Industry:** A pharmaceutical company's clinical-trial data agent retains backups for 7 years per FDA 21 CFR Part 11 requirements, with documented integrity verification and chain-of-custody logging for every restore operation.

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
