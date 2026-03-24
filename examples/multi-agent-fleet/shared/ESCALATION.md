# Sentinel Crew — Escalation Policy

## Level 1 — Automatic (No Human)

- **Triggers:** Data format errors, API timeouts, schema validation failures
- **Action:** Retry twice with exponential backoff (5s, 30s). Log the error. If resolved, continue pipeline.
- **If unresolved:** Escalate to L2.

## Level 2 — Analyst Review

- **Triggers:** Data anomalies (values >3 standard deviations from historical), contradictory sources on same metric, >20% of Scout bundles failing validation
- **Action:** Analyst flags the issue in its output with `risk_assessment: medium`. PM reviews in daily report.
- **Response time:** Same pipeline run. No human intervention required unless pattern persists 3+ days.

## Level 3 — Portfolio Manager (David Park)

- **Triggers:** Any finding with `risk_assessment: high`, daily budget overage exceeding 10%, pipeline failure after L1 retries exhausted, 3+ consecutive days of L2 flags
- **Action:** Pipeline pauses. PM notified via Slack (#sentinel-crew-alerts). PM must acknowledge and either approve continuation or modify parameters.
- **Response time:** 4 hours during market hours (09:00-16:00 EST).

## Level 4 — Chief Investment Officer

- **Triggers:** Regulatory data detected in non-public classification, potential market-moving findings before public disclosure, system compromise indicators, unauthorized access attempts
- **Action:** Pipeline halts immediately. All data quarantined. CIO and Compliance notified. No data leaves the system until cleared.
- **Response time:** 1 hour, any time.
