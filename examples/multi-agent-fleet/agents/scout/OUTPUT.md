# Scout — Output Specification

## Output Format

Structured JSON data bundles. One file per source, plus a manifest file for the full run.

## Schema (per source)

```json
{
  "source_url": "https://example.com/filing/10-K",
  "source_type": "sec_filing",
  "timestamp": "2026-03-24T06:12:43Z",
  "raw_text": "Full extracted text content...",
  "extracted_metrics": [
    {"metric": "revenue_q4", "value": 4200000000, "unit": "USD"},
    {"metric": "eps", "value": 3.42, "unit": "USD"}
  ],
  "confidence_score": 0.92,
  "data_classification": "public"
}
```

## Output Location

`/data/scout/YYYY-MM-DD/` — one directory per run date.

## Manifest

Each run produces `manifest.json` containing: run_id, timestamp, source_count, success_count, failure_count, total_metrics_extracted, and file listing with checksums.

## Handoff

On completion, Scout writes a handoff message to `/queue/sentinel-crew/` for Analyst pickup.
