---
spec_name: HEALTHCHECK.md
spec_version: 0.1.0
category: Operations
domain: healthcheckmd.dev
priority: High
volume: "Vol 12 — Fleet Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
spec_type: static
---


# HEALTHCHECK.md

**Category:** Operations
**Domain:** healthcheckmd.dev
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose
Exact commands and endpoints to verify this agent is running
correctly. Different from MONITOR.md (ongoing observability)
and SELFHEALING.md (proactive health) — HEALTHCHECK.md is
the specific checks a deployment system, load balancer, or
human uses to verify liveness and readiness. When checks fail
repeatedly, CIRCUITBREAKER.md governs containment.

### Spec

````markdown
---
agent_name: string
version: semver
liveness_endpoint: string    # HTTP endpoint or command
readiness_endpoint: string   # HTTP endpoint or command
check_interval_seconds: number
---

# [Agent Name] — Health Checks

## Quick Check

```bash
# Is the agent alive?
curl -f http://localhost:[PORT]/health

# Is it ready to accept work?
curl -f http://localhost:[PORT]/ready

# Full status
curl http://localhost:[PORT]/status | jq .
```

---

## Health Check Endpoints

### GET /health (liveness)
The agent is running and not crashed.

**Healthy response (200):**
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "uptime_seconds": 3600
}
```

**Unhealthy response (503):**
```json
{
  "status": "unhealthy",
  "reason": "database connection failed"
}
```

### GET /ready (readiness)
The agent is ready to accept tasks.

**Ready response (200):**
```json
{
  "status": "ready",
  "queue_depth": 0,
  "connections": {
    "database": "ok",
    "llm_api": "ok",
    "mcp_servers": "ok"
  }
}
```

**Not ready response (503):**
```json
{
  "status": "not_ready",
  "reason": "warming up",
  "retry_after": 10
}
```

### GET /status (detailed)
Full operational status. See STATUS.md for format.

---

## CLI Health Checks

If not running as HTTP server:

```bash
# Basic liveness
[agent-cli] health

# Full readiness check
[agent-cli] health --full

# Check specific component
[agent-cli] health --check database
[agent-cli] health --check llm
[agent-cli] health --check mcp
```

---

## Kubernetes / Docker Health Check Config

```yaml
# Kubernetes
livenessProbe:
  httpGet:
    path: /health
    port: [PORT]
  initialDelaySeconds: 10
  periodSeconds: 30
  failureThreshold: 3

readinessProbe:
  httpGet:
    path: /ready
    port: [PORT]
  initialDelaySeconds: 5
  periodSeconds: 10
  failureThreshold: 3
```

```dockerfile
# Docker
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
  CMD curl -f http://localhost:[PORT]/health || exit 1
```

---

## What Each Check Verifies

| Check | Verifies | Failure means |
|-------|---------|--------------|
| /health | Process running, not crashed | Restart needed |
| /ready | All deps available, queue healthy | Don't send traffic |
| database | DB connection active | Data ops will fail |
| llm_api | LLM API reachable + authenticated | Tasks will fail |
| mcp_servers | All required MCP servers responding | Tools unavailable |

---

## Automated Health Monitoring

Configure your monitoring system to:
- Check /health every [N] seconds
- Alert if [N] consecutive failures
- Check /ready before routing traffic
- See MONITOR.md for full alerting configuration

_See MONITOR.md for ongoing observability beyond point-in-time checks._
````

## Example Use Cases

**Enterprise:** A retail company's inventory-management agent exposes /health and /ready endpoints behind a Kubernetes load balancer, which automatically stops routing traffic to unhealthy instances during peak Black Friday traffic.

**Multi-Agent Fleet:** An orchestrator polls HEALTHCHECK.md endpoints for all 80 agents in a data-pipeline fleet every 30 seconds, displaying a real-time fleet health dashboard and automatically rerouting tasks away from agents with failing readiness checks.

**Regulated Industry:** A telehealth platform's appointment-scheduling agent runs extended health checks that verify HIPAA-compliant encryption is active on all database connections before reporting readiness, preventing unencrypted patient data handling.

## Related Specs

| Spec | Relationship |
|------|-------------|
| CIRCUITBREAKER.md | Failure containment and blast radius |
| ENGINE.md | Runtime execution configuration |
| ENFORCEMENT.md | Policy verification and compliance |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| HEARTBEAT.md | Periodic proactive execution cycle |
| MONITOR.md | Observability and alerting |
| SLA.md | Service level commitments |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
