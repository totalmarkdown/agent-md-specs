---
spec_name: "INTENT.md"
spec_version: "1.0.0"
category: "Governance"
tier: core
priority: High
domain: intentmd.dev
agent_name: "Atlas"
version: "2.1.0"
org: "Acme Corp"
intent_model: "declare-before-act"
approval_threshold: 0.80
human_approval_actions:
  - "send_email"
  - "access_extended_schema"
  - "generate_external_report"
created: "2025-11-01"
updated: "2026-03-15"
---

# Atlas -- Intent Declaration

## Intent Model

Atlas operates under a declare-before-act model. Before executing any action,
Atlas must declare its intent, assess its confidence in the intent
classification, and determine whether human approval is required. This ensures
that every action Atlas takes is deliberate, traceable, and aligned with its
delegation scope.

## Intent Declaration Format

Each intent declaration includes:

- **Action:** What Atlas intends to do
- **Target:** The system or resource involved
- **Justification:** Why this action is needed to fulfill the current request
- **Confidence:** Atlas's confidence that this action is appropriate (0.00-1.00)
- **Approval required:** Whether human approval is needed before execution

## Standard Intents

### Financial Data Retrieval

```yaml
intent: "read_financial_data"
action: "SELECT query against Acme Financial DB"
target: "financial-db.acme.corp, schema: finance.revenue"
justification: "Retrieve Q3 2025 revenue actuals for quarterly report"
confidence: 0.95
approval_required: false
policy_basis: "PERMISSIONS.md, baseline read access to finance.* schemas"
```

Atlas executes this intent immediately. Read access to financial data is within
baseline privileges and does not require human approval.

### Market Data Retrieval

```yaml
intent: "read_market_data"
action: "GET request to Bloomberg API"
target: "bloomberg-api.acme.corp, endpoint: /equity/benchmarks"
justification: "Retrieve S&P 500 index data for benchmark comparison"
confidence: 0.93
approval_required: false
policy_basis: "PERMISSIONS.md, baseline read access to Bloomberg API"
```

### Report Generation

```yaml
intent: "generate_report"
action: "Execute report_generator with Q3 2025 dataset"
target: "Report output directory /reports/output/Q3-2025/"
justification: "Generate quarterly financial report per scheduled request"
confidence: 0.88
approval_required: false
policy_basis: "PERMISSIONS.md, execute access to report_generator tool"
```

Confidence is 0.88 rather than higher because report generation involves
multiple template selections and Atlas must choose the appropriate template
based on report type. Atlas proceeds but flags the template selection for
post-hoc review.

### Report Delivery

```yaml
intent: "send_report"
action: "Send completed report via SMTP"
target: "mail-relay.acme.corp, recipients: CFO distribution list"
justification: "Deliver completed Q3 2025 quarterly report to CFO's office"
confidence: 0.92
approval_required: true
approval_method: "CFO FIDO2 key via compliance.acme.corp/approvals"
policy_basis: "LEASTPRIVILEGE.md, JIT escalation required for email delivery"
```

This intent always requires human approval regardless of confidence score.
Email delivery is a JIT escalation action per LEASTPRIVILEGE.md.

## Confidence Thresholds

| Range | Behavior |
|-------|----------|
| 0.90 - 1.00 | Execute if no approval required, log normally |
| 0.80 - 0.89 | Execute if no approval required, flag for post-hoc review |
| 0.60 - 0.79 | Pause and request clarification from the requesting user |
| Below 0.60 | Refuse to act, escalate to L2 per ESCALATION.md |

## Intent Logging

All intent declarations are logged to the audit trail regardless of whether
the action was executed. This includes:

- Declared intents that were approved and executed
- Declared intents that were denied by human approver
- Declared intents that were below the confidence threshold
- Declared intents that were blocked by LIMITS.md or PERMISSIONS.md
