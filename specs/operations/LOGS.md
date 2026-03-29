---
spec_name: LOGS.md
spec_version: 0.1.0
category: Operations
domain: logsmd.dev
priority: Medium
volume: "Vol 4 — Economic Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---
> **Static Configuration** — committed to your repository


# LOGS.md

**Category:** Operations
**Domain:** logsmd.dev
**Priority:** Medium
**Version:** 0.1.0

### Purpose
Operational logging configuration — where logs go, what gets logged,
log format, retention policy, and how to query them. Different from
AUDITTRAIL.md (compliance/security audit trail) — LOGS.md covers
operational observability logs. For alert rules built on these logs,
see MONITOR.md.

### Spec

````markdown
---
agent_name: string
version: semver
log_level: string      # DEBUG | INFO | WARN | ERROR
log_destination: string
retention_days: number
structured_logging: boolean
---

# [Agent Name] — Logging Configuration

## Log Destinations
| Log type | Destination | Format | Retention |
|----------|-------------|--------|-----------|
| Application logs | [path/service] | [JSON/text] | [N days] |
| Error logs | [path/service] | [JSON/text] | [N days] |
| Audit logs | [path/service] | [JSON/text] | [N years] |
| Performance logs | [path/service] | [JSON/text] | [N days] |
| Debug logs | [path/service] | [JSON/text] | [N days] |

## Log Levels
**Production:** [INFO | WARN | ERROR]  
**Staging:** [DEBUG | INFO | WARN | ERROR]  
**Development:** [DEBUG]

## What Gets Logged

### Always logged (regardless of level)
- Agent start/stop events
- Task start/completion/failure
- All errors and exceptions
- Security events (auth, access control)
- Escalations
- External API calls (sanitized)

### Logged at INFO level
- Task progress milestones
- Configuration changes
- Resource usage summaries

### Logged at DEBUG level
- Detailed task steps
- Tool call inputs/outputs (sanitized)
- Memory operations
- Full request/response cycles

### Never logged
- API keys, tokens, credentials
- PII (names, emails, phone numbers)
- File contents unless explicitly in scope
- Private wallet addresses

## Log Format
Structured JSON format:
```json
{
  "timestamp": "ISO-8601",
  "level": "INFO|WARN|ERROR|DEBUG",
  "agent": "agent-name",
  "agent_version": "semver",
  "task_id": "uuid",
  "event": "event-type",
  "message": "human readable description",
  "data": {},
  "duration_ms": 0,
  "error": null
}
```

## Querying Logs
```bash
# Recent errors
[log-query-command] --level ERROR --since 1h

# Specific task
[log-query-command] --task-id [uuid]

# Performance analysis
[log-query-command] --event task_complete --since 24h | analyze
```

## Alerting (see MONITOR.md for full config)
Log-based alerts:
- ERROR rate > [N]/min → alert
- Specific error pattern → alert
- No logs for [N] min → heartbeat alert

## Log Access
- **Read access:** [roles/systems]
- **Write access:** agent only
- **Deletion:** [policy — typically never]
- **Export:** [how to export for analysis]
````

## Example Use Cases

**Enterprise:** A supply-chain management platform configures structured JSON logging for its procurement agents, enabling the ops team to query by task_id across all agents to trace a purchase order's full lifecycle from request to fulfillment.

**Multi-Agent Fleet:** A DevOps team aggregates logs from 60 agents into Datadog, using the standardized log format to build cross-agent correlation dashboards that surface which upstream agent failures are causing downstream task failures.

**Regulated Industry:** A government contractor's document-classification agents log all tool call inputs and outputs (sanitized of classified content) with 10-year retention, meeting NIST 800-53 audit requirements while ensuring no PII leaks into log storage.

## Related Specs

| Spec | Relationship |
|------|-------------|
| AUDITTRAIL.md | Tamper-proof action logging |
| CIRCUITBREAKER.md | Failure containment and blast radius |
| ENFORCEMENT.md | Policy verification and compliance |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| HEALTHCHECK.md | Liveness and readiness checks |
| MONITOR.md | Observability and alerting |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
