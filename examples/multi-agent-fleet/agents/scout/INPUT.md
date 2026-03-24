# Scout — Input Specification

## Accepted Input Types

- **URLs** — Direct links to financial data pages, SEC filings, earnings transcripts
- **RSS feed URLs** — Financial news feeds, regulatory announcement feeds
- **API endpoint configs** — JSON objects with fields: endpoint_url, auth_type, headers, params
- **Search queries** — Plain text queries for financial data aggregator APIs

## Constraints

- Maximum 50 sources per run
- Each source must include a `source_type` field (url, rss, api, query)
- API configs must reference credentials by alias, never inline secrets
- URLs must use HTTPS — plain HTTP sources are rejected

## Input Location

Scout reads its source list from `/config/scout/sources.json` at pipeline start. The Portfolio Manager or a delegated team member maintains this file. Changes require a pull request with PM approval.

## Validation

Scout validates all inputs before processing. Malformed entries are logged and skipped. If more than 20% of sources fail validation, the run halts and escalates to L2.
