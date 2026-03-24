# Sentinel Crew

**Owner:** David Park, Portfolio Manager — Equities Desk
**Created:** 2026-01-15
**Last Review:** 2026-03-01

## Members

| Agent   | Role                  | Spec Path          |
|---------|-----------------------|--------------------|
| Scout   | Data collection       | agents/scout/      |
| Analyst | Analysis & validation | agents/analyst/    |
| Scribe  | Report generation     | agents/scribe/     |

## Pipeline

Sequential execution: **Scout -> Analyst -> Scribe**

Each agent completes fully before the next begins. No parallel execution. If any agent fails, the pipeline halts and escalates per shared/ESCALATION.md.

## Handoff Protocol

Agents communicate via JSON message queue at `/queue/sentinel-crew/`. Each handoff includes a manifest with: sending_agent, timestamp, payload_path, item_count, and checksum. The receiving agent validates the manifest before accepting the payload.

## Shared Constraints

- Daily API budget: $200 (see shared/BUDGET.md)
- All agents operate under shared/DELEGATION.md scope
- Escalation follows shared/ESCALATION.md
- Pipeline runs once daily at 06:00 UTC (01:00 EST pre-market)
