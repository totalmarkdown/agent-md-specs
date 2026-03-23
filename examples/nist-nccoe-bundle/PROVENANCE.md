---
agent_name: "Atlas"
version: "2.1.0"
org: "Acme Corp"
provenance_model: "source-classification"
trust_levels:
  - "trusted"
  - "verified"
  - "unverified"
  - "untrusted"
created: "2025-11-01"
updated: "2026-03-15"
---

# Atlas -- Data Provenance

## Provenance Model

Every piece of data Atlas consumes is classified by source, trust level, and
authentication method. This classification determines how Atlas treats the
data in its analysis and what caveats it attaches to outputs derived from
each source.

## Source Registry

### Trusted Sources

Trusted sources are operated by Acme Corp, authenticated via mTLS with SPIFFE
SVIDs, and subject to Acme's internal data governance controls.

#### Acme Financial Database

- **Endpoint:** financial-db.acme.corp:5432
- **Trust level:** Trusted
- **Authentication:** mTLS with SPIFFE SVID
- **Data types:** General ledger, accounts receivable, accounts payable,
  revenue recognition, cost center allocations, budget data
- **Data owner:** Controller's Office
- **Refresh frequency:** Real-time (transactional), nightly batch for
  aggregated views
- **Data quality SLA:** 99.9% accuracy per quarterly reconciliation
- **Lineage:** ERP system (SAP S/4HANA) --> ETL pipeline --> Financial DB

#### Acme Internal Document Repository

- **Endpoint:** docs.acme.corp/finance/
- **Trust level:** Trusted
- **Authentication:** mTLS with SPIFFE SVID
- **Data types:** Report templates, financial policies, methodology documents,
  prior-period reports
- **Data owner:** CFO's Office
- **Version control:** Git-backed, all changes require Finance team approval

### Verified Sources

Verified sources are external to Acme but authenticated via strong credentials
and covered by contractual data quality agreements.

#### Bloomberg Terminal API

- **Endpoint:** bloomberg-api.acme.corp:8443 (via Acme API gateway)
- **Trust level:** Verified
- **Authentication:** OAuth 2.0 + API key, proxied through Acme gateway
- **Data types:** Equity prices, fixed income yields, FX rates, economic
  indicators, sector benchmarks
- **Data quality:** Bloomberg's standard data accuracy SLA per enterprise
  license agreement
- **Caveats in output:** All Bloomberg-sourced data is labeled with retrieval
  timestamp and marked as "market data, Bloomberg Terminal" in report footnotes
- **Staleness threshold:** Market data older than 15 minutes is flagged;
  data older than 24 hours triggers a warning in the report

### Unverified Sources

Unverified sources are internal but lack strong authentication or data quality
guarantees.

#### Email Attachments

- **Trust level:** Unverified
- **Authentication:** Sender identity via Acme email (SPF/DKIM/DMARC validated)
  but attachment content is not authenticated
- **Processing:** All email attachments are processed in a sandboxed
  environment. Data extracted from attachments is tagged as "unverified,
  email attachment" throughout the analysis pipeline.
- **Restrictions:** Atlas will not use unverified data as the sole basis for
  any financial figure. Unverified data is used only for cross-reference
  and flagged in report footnotes.

### Untrusted Sources

Untrusted sources are external, unauthenticated, and used only for
supplementary context.

#### Web Search Results

- **Trust level:** Untrusted
- **Authentication:** None
- **Access:** Read-only, via Acme's web proxy with content filtering
- **Restrictions:** Atlas does not incorporate web search data into financial
  calculations. Web data is used only for qualitative context (e.g., industry
  news references in report narratives) and is always attributed with URL
  and retrieval timestamp.

## Aggregation Escalation

When Atlas combines data from multiple sources, the resulting aggregate may
have a higher sensitivity classification than any individual source.

| Combination | Escalated Classification | Reason |
|-------------|------------------------|--------|
| Revenue by department + headcount by department | PII-adjacent | Could derive per-capita revenue, identifying small teams |
| Compensation expense + department roster | PII | Direct link to individual compensation |
| Customer revenue + customer contact list | Confidential-PII | Links financial data to identifiable individuals |

When an aggregation triggers escalation, Atlas:

1. Applies the higher classification to the output
2. Restricts the output distribution list to recipients authorized for that
   classification level
3. Logs the aggregation escalation event in the audit trail
4. Adds a classification banner to the report header
