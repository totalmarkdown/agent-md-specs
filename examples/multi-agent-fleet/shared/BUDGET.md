# Sentinel Crew — Budget

**Effective:** 2026-01-15
**Approved by:** David Park, Portfolio Manager

## Daily Budget: $200

| Agent   | Allocation | Amount | Rationale                           |
|---------|-----------|--------|-------------------------------------|
| Scout   | 60%       | $120   | Highest API call volume (data APIs, web fetching) |
| Analyst | 30%       | $60    | Computation-heavy analysis, LLM calls for NLP     |
| Scribe  | 10%       | $20    | Minimal API usage, primarily formatting            |

## Monthly Cap

$4,500 hard cap. Pipeline halts automatically when 90% ($4,050) is reached and alerts PM for review. Unused daily budget does not roll over.

## Overage Policy

- **0-10% daily overage:** Logged, no action. Reviewed in weekly digest.
- **>10% daily overage:** Pipeline halts immediately. PM alerted. Requires manual restart.
- **Monthly cap hit:** All runs suspended until next billing cycle or PM override.

## Tracking

Each agent logs API costs per call to `/logs/sentinel-crew/costs/YYYY-MM-DD.json`. Daily totals reconciled against billing dashboard at end of day.
