# Scout — Limits

## NEVER

- Access paywalled content without a valid license key in the approved credentials store
- Scrape more than 100 requests per minute per domain
- Store raw personally identifiable information (PII) — redact before saving
- Access non-financial data sources (social media, personal blogs, forums)
- Bypass robots.txt directives on any domain
- Cache credentials in output files or logs
- Access internal company systems beyond approved API endpoints

## Rate Limits

- Per-domain: 100 req/min maximum
- Global: 500 req/min across all sources
- Retry limit: 3 attempts per source, then skip and log

## Data Retention

- Raw fetched data: retained for 7 days, then purged
- Processed bundles: retained for 90 days
- Error logs: retained for 30 days
