---
spec_name: DATA.md
spec_version: 0.1.0
category: Technical
domain: datamd.dev
priority: High
volume: "Vol 1 — Core Agent Specs"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---


# DATA.md

**Category:** Technical
**Domain:** datamd.dev
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose
Defines data sources, schemas, access credentials locations, 
data quality rules, and data handling procedures for an agent 
that reads, writes, or transforms data.

### When to create
Any agent that queries databases, reads APIs, processes files, 
writes to data stores, or makes decisions based on data.

### Spec

````markdown
---
agent_name: string
version: semver
data_classification: string  # public | internal | confidential | restricted
pii_handled: boolean
created: date
updated: date
---

# [Agent Name] — Data Configuration

## Data Sources

### [Source Name]
- **Type:** database | API | file | stream | warehouse
- **Location:** [connection string pattern — never actual credentials]
- **Credentials:** Stored in [env var name | keychain key | vault path]
- **Access level:** read-only | read-write | admin
- **Rate limits:** [requests per minute/hour]
- **Documentation:** [link]
- **Schema:** See [schema file path] or below

### Schema (inline for small schemas)
```sql
-- Table: [table_name]
-- Description: [what this table contains]
id          UUID    PRIMARY KEY
field_name  TYPE    -- [description]
```

## Data Quality Rules
_See PROVENANCE.md for data lineage and trust classification._
- Required fields: [list fields that must never be null]
- Valid value ranges: [field]: [min] to [max]
- Date format: [ISO 8601 | other]
- Encoding: [UTF-8 | other]
- Deduplication: [field(s) that define a unique record]

## Data Handling Rules

### PII (Personal Identifiable Information)
Classify fields according to PII.md.
- PII fields in this dataset: [list]
- PII handling: [mask | encrypt | avoid logging | other]
- Retention: [how long data can be kept]
- Deletion: [how to handle deletion requests]

### Data Transformations
- Bronze → Silver rules: [cleaning and normalization]
- Silver → Gold rules: [enrichment and aggregation]
- Null handling: [replace with X | skip | error]
- Encoding errors: [skip | replace | error]

## Output Formats
When writing data, use these formats:
- Default format: [JSON | CSV | Parquet | other]
- Date format: [ISO 8601]
- Numeric precision: [X decimal places]
- Encoding: UTF-8

## Monitoring and Alerts
- Alert if row count drops below: [threshold]
- Alert if null rate exceeds: [%] for field [name]
- Alert if processing time exceeds: [minutes]
- Alert destination: [log file | Slack | email]
````

## Example Use Cases

**Enterprise:** A retail analytics company uses DATA.md to document its inventory agent's three data sources (PostgreSQL warehouse, Shopify API, CSV uploads), defining Bronze-to-Gold transformation rules and PII masking for customer email addresses.

**Multi-Agent Fleet:** A data platform team uses DATA.md across all ETL agents to map which agents read from which sources and write to which destinations, enabling impact analysis when a database schema change affects multiple agents.

**Regulated Industry:** A clinical research organization uses DATA.md to define data quality rules for its trial data agent, requiring ISO 8601 date formats, non-null patient IDs, and 90-day retention limits with automated deletion for de-identified datasets.

## Related Specs

| Spec | Relationship |
|------|-------------|
| INPUT.md | Accepted input formats |
| MCP.md | Model Context Protocol connections |
| OUTPUT.md | Output formats and delivery |
| PERMISSIONS.md | Static resource access control |
| TOOLS.md | Available tools and capabilities |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
