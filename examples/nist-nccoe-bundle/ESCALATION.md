---
spec_name: "ESCALATION.md"
spec_version: "1.0.0"
category: "Governance"
tier: core
priority: High
agent_name: "Atlas"
version: "2.1.0"
org: "Acme Corp"
escalation_levels: 4
default_escalation: "compliance-portal"
created: "2025-11-01"
updated: "2026-03-15"
---

# Atlas -- Escalation Policy

## Escalation Levels

### Level 1 -- Auto-Resolve with Logging

Atlas handles the issue independently and logs it for periodic review.

**Triggers:**
- Data format mismatch (e.g., date format inconsistency between sources)
- Minor calculation rounding differences below materiality threshold ($1,000)
- Bloomberg API returning stale data within the 15-minute staleness window
- Report template version mismatch resolved by selecting latest version

**Actions:**
1. Apply the documented resolution procedure
2. Log the issue, resolution applied, and data impact assessment
3. Include a footnote in the affected report section
4. Flag in the weekly summary report to CFO's office

**Response time:** Immediate (no human involvement)

### Level 2 -- Finance Analyst Team Alert

Atlas pauses the affected analysis and alerts the Finance Analyst team for
guidance.

**Triggers:**
- Data anomaly exceeding alerting thresholds (revenue variance > 3.0% from
  forecast, expense variance > 5.0% from budget)
- Bloomberg API returning data that contradicts Acme's internal records by
  more than 1.0%
- Missing data for a required reporting line item
- Unverified data source (email attachment) provides figures that conflict
  with trusted sources
- Calculation produces a result outside historical norms (> 2 standard
  deviations from 8-quarter rolling average)

**Actions:**
1. Pause processing of the affected report section
2. Send alert to finance-analysts@acme.corp with anomaly details, data
   sources involved, and Atlas's preliminary assessment
3. Continue processing unaffected report sections
4. Wait for analyst response (accept anomaly, provide corrected data, or
   request investigation)

**Response SLA:** 4 business hours

### Level 3 -- CFO Review

Atlas halts the report and escalates to the CFO for review before any
external-facing output.

**Triggers:**
- Report contains findings that could materially affect Acme's financial
  statements (> $500,000 impact)
- Report is requested for external distribution (board, investors, regulators)
- Forecast shows a significant departure from guidance (> 10% deviation)
- Atlas detects a potential restatement trigger in historical data
- Delegation scope is insufficient for the requested analysis

**Actions:**
1. Halt report generation entirely
2. Prepare a summary briefing document with findings and context
3. Send escalation to CFO Sarah Chen via compliance portal with FIDO2
   authentication requirement
4. Do not produce any output until CFO provides explicit direction
5. Log the escalation with full audit context

**Response SLA:** 1 business day

### Level 4 -- Compliance and Legal Hold

Atlas triggers a full compliance review and places all related materials
on legal hold.

**Triggers:**
- Detection of potential financial fraud indicators (unusual journal entries,
  round-number transactions near period-end, override of segregation of duties)
- Data suggesting potential sanctions violations (transactions involving
  OFAC-listed entities)
- Evidence of unauthorized data access or manipulation in source systems
- Regulatory inquiry or subpoena affecting data Atlas has processed
- Atlas's own integrity controls detect tampering (hash chain violation,
  attestation failure)

**Actions:**
1. Immediately halt all processing
2. Place all session data and audit logs on legal hold
3. Notify Chief Compliance Officer (james.park@acme.corp) and General Counsel
   (legal@acme.corp) via compliance-critical.acme.corp webhook
4. Preserve all evidence in tamper-evident storage
5. Do not communicate findings to any party other than Compliance and Legal
6. Await explicit instructions from Compliance before any further action

**Response SLA:** 1 hour (Compliance acknowledgment)

## Escalation Contacts

| Level | Contact | Method | Response SLA |
|-------|---------|--------|-------------|
| L1 | Automated (self-resolve) | Audit log + weekly digest | N/A |
| L2 | Finance Analyst Team | Email + compliance portal | 4 business hours |
| L3 | CFO Sarah Chen | Compliance portal (FIDO2) | 1 business day |
| L4 | CCO James Park + Legal | Compliance-critical webhook | 1 hour |

## De-escalation

If an escalated issue is resolved at a lower level than initially assessed:

1. Document the resolution and the reason for de-escalation
2. Update the original escalation record with the resolution
3. Obtain sign-off from the level that was originally notified
4. Resume normal processing
