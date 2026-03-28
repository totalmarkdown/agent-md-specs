---
spec_name: REPAIR.md
spec_version: 0.1.0
category: Operations
domain: repairmd.dev
priority: High
volume: "Vol 1 — Core Agent Specs"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# REPAIR.md

**Category:** Operations
**Domain:** repairmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Defines error recovery procedures, retry logic, self-healing 
behaviors, and diagnostic steps for an agent that encounters 
failures during operation.

### When to create
Any production agent that runs autonomously and must continue 
operating through transient failures without human intervention 
for routine errors.

### Spec

```markdown
---
agent_name: string
version: semver
max_retries: number      # Default retry limit
retry_backoff: string    # linear | exponential | fixed
alert_on_failure: boolean
created: date
updated: date
---

# [Agent Name] — Repair and Recovery

## Recovery Philosophy
[Fail fast | retry aggressively | degrade gracefully | other approach]

## Error Classification

### Transient (retry automatically)
Errors that are likely to resolve without intervention:
- Network timeout
- Rate limit (429) — wait and retry
- Temporary unavailability (503)
- Lock contention on database
- [Agent-specific transient errors]

### Recoverable (attempt repair)
Errors that require corrective action before retrying:
- Invalid data format — apply data cleaning, retry
- Missing expected file — regenerate from source, retry
- Stale credentials — refresh token, retry
- Disk space — clean temp files, retry

### Fatal (stop and escalate)
Errors that cannot be resolved autonomously (see ESCALATION.md for routing):
- Authentication failure (invalid credentials)
- Permission denied
- Data corruption detected
- Schema mismatch
- Any error that repeats more than [N] times — triggers CIRCUITBREAKER.md
- [Agent-specific fatal errors]

## Retry Configuration
| Error Type | Max Retries | Backoff | Max Wait |
|------------|-------------|---------|----------|
| Network timeout | 3 | exponential | 60s |
| Rate limit | 5 | fixed 60s | 5min |
| Database lock | 3 | linear 5s | 15s |
| [Custom] | [N] | [type] | [max] |

## Recovery Procedures

### On network failure:
1. Log error with timestamp and error message
2. Wait [backoff period]
3. Test connectivity with lightweight ping
4. If connectivity restored: retry original request
5. If still failing after [N] attempts: escalate Level 2

### On data validation failure:
1. Log the invalid record with full details
2. Apply cleaning rules from DATA.md
3. Retry with cleaned data
4. If still invalid: move to dead letter queue at [location]
5. Continue processing remaining records

### On out-of-memory / resource exhaustion:
1. Stop processing new items
2. Complete current item if safe to do so
3. Release resources
4. Log resource usage at time of failure
5. Restart with reduced batch size: [original size / 2]

### On unexpected exception (catch-all):
1. Log full stack trace to [location]
2. Capture current state snapshot to [location]
3. Escalate Level 3 per ESCALATION.md
4. Do not retry — wait for human intervention

## Health Checks
Run these checks at startup and every [X minutes]:
- [ ] [Dependency name] reachable: [test method]
- [ ] [Data source] accessible: [test method]
- [ ] Disk space available: minimum [X GB]
- [ ] Memory available: minimum [X MB]

If any health check fails at startup: do not proceed, log failure, alert.

## Diagnostic Information to Capture on Failure
Always include in error reports:
- Timestamp (UTC)
- Agent name and version
- Task being executed
- Input that triggered the error
- Full error message and stack trace
- System state (memory, disk, CPU if available)
- Last 10 actions taken before failure
- Relevant environment variables (names only, never values)

## Dead Letter Queue
Failed records that cannot be processed go to: [location]  
Format: [original record] + [error details] + [timestamp]  
Review dead letter queue: [daily | weekly | on alert]  
Retry dead letter queue: [manually | automated after fix]
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| CIRCUITBREAKER.md | Failure containment and blast radius |
| ENFORCEMENT.md | Policy verification and compliance |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| HEALTHCHECK.md | Liveness and readiness checks |
| MONITOR.md | Observability and alerting |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
