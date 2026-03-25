---
spec_name: "CIRCUITBREAKER.md"
spec_version: "1.0.0"
category: Example
tier: extended
agent_name: "Sentinel Crew"
agent_version: "1.0.0"
---

# Sentinel Crew — Circuit Breaker

## Fleet-Level Circuit Breaker

The Sentinel Crew data pipeline (Scout -> Analyst -> Scribe) uses
independent circuit breakers at each agent with crew-level coordination.

## Agent Failure Containment

| Agent | Failure Threshold | Containment | Downstream Impact |
|-------|------------------|-------------|-------------------|
| Scout | 3 consecutive API failures | Scout halts, Analyst and Scribe continue with cached data | Reports use stale data (staleness warning added) |
| Analyst | 2 consecutive analysis errors | Analyst halts, Scribe halts, Scout continues monitoring | No new reports until Analyst recovers |
| Scribe | 3 formatting failures | Scribe halts, Scout and Analyst continue | Raw analysis available, formatted reports paused |

## Crew-Level Circuit Breaker

If 2 or more agents fail simultaneously:
- Entire Sentinel Crew halts
- Alert: Portfolio Manager David Park (L3 per ESCALATION.md)
- Return last successful pipeline output with staleness warning

## Recovery

- Cooldown: 5 minutes per agent
- Backoff: exponential (5 min, 10 min, 20 min)
- Success criteria: 2 consecutive successful operations to close circuit
- Recovery order: Scout first, then Analyst, then Scribe
