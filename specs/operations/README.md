# Operations Specs

Specs for keeping agents running, observable, and recoverable in production. Operations specs cover the full operational surface -- from deployment and setup through monitoring and health checks to failure containment, self-healing, and service commitments. Without these, agents are black boxes that fail silently.

## How These Specs Work Together

The operational stack has three layers. The foundation layer handles deployment: REQUIREMENTS.md lists what you need, SETUP.md walks through first-run provisioning, and DEPLOYMENT.md covers production releases and rollbacks. The observability layer keeps agents visible: MONITOR.md defines metrics and dashboards, HEALTHCHECK.md provides point-in-time liveness checks, HEARTBEAT.md emits periodic alive signals, LOGS.md configures operational logging, and STATUS.md exposes real-time state. The resilience layer handles failure: CIRCUITBREAKER.md contains blast radius when things break, REPAIR.md defines recovery procedures, SELFHEALING.md extends that with proactive auto-correction, and BACKUP.md ensures state can be restored. SLA.md ties it all together with service-level commitments. Supporting specs cover scheduling (AVAILABILITY.md), safe interruption (INTERRUPT.md), version migration (MIGRATION.md), risk assessment (RISKS.md), and even operational sentiment (MOOD.md).

## Specs in This Category

| Spec | Tier | Purpose | Scope |
|------|------|---------|-------|
| AVAILABILITY.md | extended | Schedule, capacity, and maintenance windows | Per-agent |
| BACKUP.md | extended | Backup and recovery procedures for state and config | Per-agent |
| CIRCUITBREAKER.md | core | Failure containment, blast radius limits, and halt conditions | Per-agent/team |
| DEPLOYMENT.md | extended | Deploy, configure, update, and roll back in production | Per-agent |
| HEALTHCHECK.md | core | Exact commands and endpoints to verify correct operation | Per-agent |
| HEARTBEAT.md | core | Periodic proactive execution cycle and status reporting | Per-agent |
| INTERRUPT.md | extended | Safe mid-task interruption without losing work or state | Per-agent |
| LOGS.md | extended | Logging config, format, retention, and query access | Per-agent |
| MIGRATION.md | extended | State and config migration for major version upgrades | Per-agent |
| MONITOR.md | core | Observability config -- metrics, dashboards, and alerts | Per-agent/fleet |
| MOOD.md | extended | Operational mood vocabulary and output expectations | Per-agent |
| REPAIR.md | extended | Error recovery procedures, retry logic, and diagnostics | Per-agent |
| REQUIREMENTS.md | extended | Hardware, runtime, network, and API prerequisites | Per-agent |
| RISKS.md | extended | Forward-looking risk assessment and mitigation plans | Per-agent/org |
| SELFHEALING.md | extended | Proactive health monitoring and automatic drift correction | Per-agent |
| SETUP.md | extended | Step-by-step guide to get an agent running from scratch | Per-agent |
| SLA.md | core | Response times, uptime targets, and escalation triggers | Per-agent/team |
| STATUS.md | extended | Real-time operational status, queue depth, and incidents | Per-agent |

## When to Use These Specs

- **Deploying an agent to production:** Start with REQUIREMENTS.md and SETUP.md, then add DEPLOYMENT.md for release processes and HEALTHCHECK.md for liveness verification.
- **Making agents observable:** Add MONITOR.md for dashboards, LOGS.md for structured logging, HEARTBEAT.md for alive signals, and STATUS.md for real-time state.
- **Building resilient systems:** Use CIRCUITBREAKER.md to contain failures, SELFHEALING.md for auto-recovery, BACKUP.md for disaster recovery, and SLA.md to formalize commitments.

## Related Categories

| Category | How It Relates |
|----------|---------------|
| [governance/](../governance/) | Governance policies (ESCALATION, LIMITS) define the rules that operations specs enforce at runtime |
| [lifecycle/](../lifecycle/) | Lifecycle specs (WAKEUP, SESSION, SLEEP) handle state transitions; operations specs keep agents healthy between transitions |
| [security/](../security/) | Security specs protect agents from threats; operations specs detect and recover from failures |
| [quality/](../quality/) | Quality specs define correctness standards; operations specs provide the observability to verify them |

---
*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)
· [Full Index](../../INDEX.md) · [README](../../README.md)*
