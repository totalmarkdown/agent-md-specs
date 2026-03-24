---
spec_name: "INPUT.md"
spec_version: "1.0.0"
category: Example
tier: extended
agent_name: "Analyst"
agent_version: "1.0.0"
---

# Analyst — Input Specification

## Accepted Input

Scout's JSON data bundles from `/data/scout/YYYY-MM-DD/`.

## Validation Rules

- Schema validation: every bundle must contain source_url, timestamp, raw_text, extracted_metrics, confidence_score, and data_classification
- Bundles with `confidence_score` below 0.3 are rejected and logged as low-confidence discards
- Bundles missing required fields are rejected — Analyst does not attempt to repair malformed data
- Manifest checksum must match actual file checksums; mismatches halt processing and escalate to L2

## Minimum Viable Input

- At least 5 valid bundles required to proceed with analysis
- If fewer than 5 bundles pass validation, the run is marked as insufficient data and Scribe is not triggered

## Historical Context

Analyst loads the previous 30 days of its own output from `/data/analyst/` for trend comparison. Missing historical data is noted but does not block the current run.
