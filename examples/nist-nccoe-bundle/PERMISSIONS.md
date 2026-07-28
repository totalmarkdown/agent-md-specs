---
spec_name: "PERMISSIONS.md"
spec_version: "1.0.0"
category: "Governance"
tier: core
priority: High
agent_name: "Atlas"
version: "2.1.0"
org: "Acme Corp"
permission_model: "explicit-grant"
last_reviewed: "2026-03-01"
reviewed_by: "Maria Gonzalez, Engineering Lead"
iam_sync: true
created: "2025-11-01"
updated: "2026-03-15"
---

# Atlas -- Permissions

## Permission Model

Atlas operates under an explicit-grant permission model. Every resource Atlas
can access is listed below. Access to any resource not listed is denied by
default. Permissions are synchronized with Acme's IAM system (iam.acme.corp)
and validated at session startup.

## Read Permissions

### Acme Financial Database

- **Host:** financial-db.acme.corp:5432
- **Database role:** atlas_readonly
- **Schemas granted:**
  - `finance.general_ledger` -- journal entries, account balances, trial balance
  - `finance.accounts_receivable` -- invoices, payments, aging reports
  - `finance.accounts_payable` -- vendor invoices, payment schedules
  - `finance.revenue` -- revenue recognition, deferred revenue, contract data
  - `finance.cost_centers` -- department budgets, actuals, allocations
  - `finance.consolidation` -- intercompany eliminations, consolidated views
  - `finance.treasury` -- cash positions, bank balances, cash forecasts
  - `finance.budget` -- annual budget, quarterly forecasts, variance thresholds
- **Schemas denied:**
  - `hr.*` -- all human resources schemas
  - `payroll.*` -- all payroll schemas
  - `trading.*` -- all trading system schemas
  - `audit_internal.*` -- internal audit working papers
- **Row-level security:** Atlas can only access data for fiscal periods within
  its delegation window (current quarter and 8 prior quarters)

### Bloomberg Terminal API

- **Endpoint:** bloomberg-api.acme.corp:8443
- **Permitted data types:**
  - Equity index data (S&P 500, DJIA, NASDAQ Composite, Russell 2000)
  - Fixed income benchmarks (US Treasury yields, investment-grade spreads)
  - Foreign exchange rates (USD pairs for currencies in Acme's operations)
  - Economic indicators (GDP, CPI, unemployment, PMI)
  - Sector benchmarks (industry-specific indices for Acme's sector)
- **Denied data types:**
  - Individual equity analysis
  - Trading signals or recommendations
  - Derivative pricing
  - Real-time order book data

### Internal Documentation

- **Endpoint:** docs.acme.corp/finance/
- **Permitted paths:**
  - `/finance/templates/*` -- report templates
  - `/finance/policies/*` -- accounting policies and methodology documents
  - `/finance/prior-reports/*` -- previously published financial reports
- **Denied paths:**
  - `/finance/audit-workpapers/*` -- internal audit materials
  - `/finance/ma/*` -- mergers and acquisitions materials
  - `/legal/*` -- all legal department documents

## Write Permissions

### Report Output Directory

- **Path:** /reports/output/
- **Subdirectories:** Organized by fiscal period (e.g., /reports/output/Q3-2025/)
- **Permitted operations:** Create new files, overwrite Atlas-generated files
- **Denied operations:** Delete files, modify files created by other systems
  or users, access parent directories
- **File types:** PDF, XLSX, JSON only
- **Naming convention:** `ATLAS-{report_type}-{period}-{timestamp}.{ext}`

## Execute Permissions

### Report Generator Tool

- **Tool ID:** report_generator_v3
- **Permitted operations:** Generate reports using approved templates
- **Input validation:** All inputs validated against template schema before
  execution
- **Output validation:** Generated reports checked against Acme's financial
  report format standard before delivery

### Forecast Engine

- **Tool ID:** forecast_engine_v2
- **Permitted models:** ARIMA, exponential smoothing, linear regression
- **Denied models:** Neural networks, custom models, unvalidated algorithms
- **Parameter constraints:** Forecast horizon limited to 4 quarters forward

## Denied Permissions -- Explicit

The following systems are explicitly denied to Atlas at multiple enforcement
layers (network, IAM, application):

| System | Reason |
|--------|--------|
| Trading systems (trading.acme.corp) | LIMITS.md hard stop: no trade execution |
| HR database (hr-db.acme.corp) | LIMITS.md hard stop: no personnel data |
| External email relay | LIMITS.md hard stop: no external communication |
| Production ERP (sap.acme.corp) | Write access denied; Atlas reads from replica |
| Customer CRM (crm.acme.corp) | Outside delegation scope |
| Engineering systems (jira.acme.corp, github.acme.corp) | Outside delegation scope |

## Permission Changes

All permission changes require:
1. Request from CFO's office with business justification
2. Security review by InfoSec team
3. Compliance review by Chief Compliance Officer
4. Implementation by Engineering with change management ticket
5. Post-implementation verification and audit log entry
