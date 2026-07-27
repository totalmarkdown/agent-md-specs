---
spec_name: "CIRCUITBREAKER.md"
spec_version: "1.0.0"
category: "Operations"
tier: core
priority: High
agent_name: "Atlas"
agent_version: "2.1.0"
---

# Circuit Breaker States

Atlas operates with three circuit breaker states: **closed** (normal operation), **open** (all requests blocked, fallback only), and **half_open** (limited probe requests to test recovery).

# Failure Thresholds

- **3 consecutive Bloomberg API failures** triggers circuit open for Atlas financial data ingestion.
- **2 consecutive Acme Corp financial database errors** triggers circuit open for internal data queries.
- **30-second timeout** on any single external API call is treated as a failure.
- Error rate exceeding 50% within a 60-second sliding window also triggers circuit open.

# Blast Radius Boundaries

- **Agent level:** Atlas halts all new report generation individually. No other agent is affected by Atlas entering open state.
- **Team level:** The Finance Team continues operating in degraded mode — existing reports remain accessible, but no new reports are generated until Atlas recovers.
- **Org level:** Atlas cannot propagate failure to downstream compliance monitoring agents or any agent outside the Finance Team.

# Fallback Behaviors

When the circuit is open, Atlas returns the **most recent cached financial report** with a staleness warning banner indicating the cache timestamp. The Finance Analyst team is alerted via Slack within 60 seconds of circuit opening.

# Retry Policy

- **Backoff strategy:** Exponential backoff starting at 30 seconds.
- **Cooldown:** 5-minute cooldown period before entering half_open state.
- **Half-open probes:** Atlas sends a single lightweight health-check request to the failed dependency.
- **Successes to close:** 2 consecutive successful probe responses required to return to closed state.
- **Max retries per request:** 3 before marking the request as failed.

# Cascading Prevention

- Atlas is **bulkheaded** from downstream agents — its failure cannot trigger circuit breakers in the compliance monitoring agent or any other downstream consumer.
- Fan-out limit: Atlas may call a maximum of 3 external services concurrently.
- Poison pill detection is enabled — if a specific input consistently causes failures, that input is quarantined and flagged for human review.

# Monitoring and Alerting

- Circuit state changes are logged to the audit trail and published to the `#finance-ops` Slack channel.
- Open circuit duration exceeding 15 minutes triggers escalation to the Finance Team lead.
- All failure events include correlation IDs for traceability.

# Recovery Procedures

1. Automated recovery via half_open probing (default path).
2. Manual override available to Finance Team lead to force-close the circuit after verifying upstream service health.
3. Post-incident review required for any circuit open event lasting longer than 30 minutes.
