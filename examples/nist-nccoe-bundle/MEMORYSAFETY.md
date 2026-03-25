---
spec_name: "MEMORYSAFETY.md"
spec_version: "1.0.0"
category: "Security"
tier: core
priority: High
domain: memorysafetymd.dev
agent_name: "Atlas"
agent_version: "2.1.0"
---

# Threat Model

| Threat                    | Description                                                        | OWASP Ref   |
|---------------------------|--------------------------------------------------------------------|-------------|
| Memory poisoning          | Malicious data injected to skew financial analysis outputs         | LLM06:2025  |
| Cross-session leakage     | Residual context from prior sessions influences current analysis   | LLM02:2025  |
| Privilege escalation      | Read-only agent attempts to write entries via prompt manipulation  | LLM01:2025  |
| Data exfiltration         | Confidential financial data extracted through crafted queries      | LLM06:2025  |

## Input Sanitization

The write gateway validates all incoming entries before they reach the shared context pool:

- **Schema conformance:** Financial data must match Bloomberg field schema (instrument ID, price, timestamp, currency). Non-conforming entries are rejected.
- **Classification auto-set:** All financial entries default to `confidential`. Only Compliance Monitor (admin) can downgrade classification.
- **Range validation:** Price and yield values checked against 3-sigma bands from trailing 30-day data. Outliers flagged for human review.
- **Source verification:** Provenance field must reference an approved data source. Entries without provenance are rejected.

## Poisoning Detection

Three canary entries are maintained in the shared pool as integrity tripwires:

| Entry ID                               | Benchmark           | Expected Value (reference) | Alert on Change |
|----------------------------------------|----------------------|----------------------------|-----------------|
| `canary-spx-close`                     | S&P 500 close        | Verified daily vs Bloomberg | yes             |
| `canary-10yr-yield`                    | 10-Year Treasury yield| Verified daily vs FRED     | yes             |
| `canary-eurusd`                        | EUR/USD spot rate     | Verified daily vs ECB      | yes             |

If any canary value is modified without a corresponding verified market update, the system triggers quarantine procedures immediately.

## Quarantine Procedures

On poisoning detection: `quarantine_and_alert`. Specifically: (1) suspect entries moved to quarantine partition, (2) Compliance Monitor alerted via ESCALATION.md, (3) all Atlas outputs frozen pending human review. Atlas cannot self-clear quarantine — only Compliance Monitor or a human operator can release.

## Cross-Session Isolation

Each analysis session receives a **read-only snapshot** of the shared context pool at session start. Atlas cannot read writes from other concurrent sessions until its session ends. All writes go through the sanitization pipeline before merging into the canonical pool.

## Memory Integrity Verification

Integrity method: `both` (signed entries + hash chain). Every entry is signed using X.509 certificates issued per agent. The full pool maintains a hash chain verified hourly by Compliance Monitor. Any chain break triggers an immediate audit trail entry (AUDITTRAIL.md) and alert.

## Classification Enforcement

All entries in the finance pool carry a minimum classification of `confidential`. Entries referencing OFAC or sanctions data are auto-classified as `restricted`. Classification can only be elevated, never lowered, except by Compliance Monitor with documented justification.
