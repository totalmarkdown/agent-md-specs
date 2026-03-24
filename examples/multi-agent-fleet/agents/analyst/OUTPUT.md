# Analyst — Output Specification

## Output Format

JSON analysis reports. One file per thematic cluster of findings.

## Schema (per finding)

```json
{
  "finding_id": "SEN-2026-0324-007",
  "finding_text": "Q4 revenue for ACME Corp exceeded consensus estimates by 12%, confirmed across 3 independent filings and 2 news sources.",
  "confidence": 0.85,
  "sources": [
    "https://sec.gov/filing/acme-10k-2025",
    "https://reuters.com/acme-q4-results",
    "https://bloomberg.com/acme-earnings"
  ],
  "contradictions": [
    {"source": "https://ft.com/acme-outlook", "claim": "Revenue growth was 8%, not 12%", "resolution": "unresolved"}
  ],
  "risk_assessment": "medium",
  "analyst_notes": "FT figure may reference organic growth excluding acquisitions. Recommend PM review."
}
```

## Output Location

`/data/analyst/YYYY-MM-DD/` — findings grouped by sector or topic.

## Handoff

On completion, Analyst writes a handoff message to `/queue/sentinel-crew/` for Scribe pickup. Includes total finding count, average confidence, and count of high-risk findings.
