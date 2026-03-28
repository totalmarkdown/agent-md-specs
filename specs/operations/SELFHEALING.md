---
spec_name: SELFHEALING.md
spec_version: 0.1.0
category: Operations
domain: selfhealingmd.dev
priority: High
volume: "Vol 2 — Extended Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# SELFHEALING.md

**Category:** Operations
**Domain:** selfhealingmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Extends REPAIR.md with proactive self-healing behaviors — the agent 
continuously monitors its own health, predicts failures before they 
happen, and automatically corrects drift from expected behavior 
without human intervention. Where REPAIR.md is reactive, 
SELFHEALING.md is proactive.

### When to create
Long-running autonomous agents that operate overnight or over 
weekends without human supervision. Production agents where 
downtime has business cost.

### Spec

```markdown
---
agent_name: string
version: semver
monitoring_interval_seconds: number  # How often to run health checks
auto_correct: boolean                 # Allow autonomous corrections
drift_threshold: number               # % deviation before correction
created: date
updated: date
---

# [Agent Name] — Self-Healing Configuration

## Health Monitoring

### Continuous Checks (run every [N] seconds)
| Check | Expected | Threshold | Auto-fix |
|-------|----------|-----------|----------|
| Memory usage | < [X]MB | > [Y]MB | Flush cache |
| Response time | < [X]ms | > [Y]ms | Reduce batch size |
| Error rate | < [X]% | > [Y]% | Switch to fallback |
| Queue depth | < [N] items | > [N] items | Scale processing |
| [Custom check] | [expected] | [threshold] | [action] |

### Behavioral Drift Detection
Monitor these outputs over time and alert if they change significantly:
- Output length: rolling average ± [X]% triggers investigation
- Confidence scores: if average drops below [X], recalibrate
- Task completion rate: if drops below [X]%, inspect recent failures
- Token usage per task: if increases > [X]%, check for prompt bloat

## Automatic Corrections

### Allowed (no human approval needed)
- Restart stale connections
- Clear expired cache entries
- Rotate to backup model if primary exceeds latency threshold
- Reduce batch size when memory pressure detected
- Flush dead letter queue older than [X days]
- Reload config files if newer version detected

### Requires Approval (escalate first)
- Modify any CLAUDE.md, AGENTS.md, or SKILL.md file
- Change model selection for non-performance reasons
- Delete any data that isn't temporary/cache
- Modify BUDGET.md or PERMISSIONS.md

## Self-Calibration
When performance degrades, attempt these calibrations in order:
1. Check if input data format has changed → validate against DATA.md schema
2. Check if external API has changed → run API.md validation suite
3. Check if context window is polluted → run /clear and restart
4. Check if model version changed → verify model in AGENTS.md is current
5. If none resolve: escalate per ESCALATION.md

## Memory Management
- Context window target: keep below [X]% full
- When approaching limit: summarize and compress older context
- Memory consolidation: run every [N] interactions
- What to preserve: [critical context items]
- What to safely discard: [transient items]

## Heartbeat
Emit heartbeat signal every [N] minutes to [location/channel].
Heartbeat format:
```json
{
  "agent": "name",
  "status": "healthy | degraded | critical",
  "uptime_minutes": N,
  "tasks_completed": N,
  "error_rate_pct": N,
  "memory_pct": N,
  "last_correction": "ISO-8601 or null",
  "timestamp": "ISO-8601"
}
```
If heartbeat missed for [N] intervals: trigger external alert.

## Incident Log
All self-corrections logged to: [location]
Format: timestamp | check_name | detected_value | correction_applied | outcome
Review log: [daily | weekly | on alert]
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| API.md | HTTP API specification |
| BUDGET.md | Cost controls and spending limits |
| CIRCUITBREAKER.md | Failure containment and blast radius |
| ENFORCEMENT.md | Policy verification and compliance |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| HEALTHCHECK.md | Liveness and readiness checks |
| MONITOR.md | Observability and alerting |
| PERMISSIONS.md | Static resource access control |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
