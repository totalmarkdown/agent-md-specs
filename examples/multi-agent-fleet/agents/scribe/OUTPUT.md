---
spec_name: "OUTPUT.md"
spec_version: "1.0.0"
category: Example
tier: extended
agent_name: "Scribe"
agent_version: "1.0.0"
---

# Scribe — Output Specification

## Output Format

Formatted Markdown reports following a fixed section structure.

## Report Sections (in order)

1. **Executive Summary** — 3-5 sentences covering the most significant findings and overall confidence level
2. **Key Findings** — Each finding with: description, confidence score, source count, and risk assessment badge
3. **Contradictions & Open Questions** — Unresolved discrepancies flagged by Analyst, with source attribution
4. **Methodology** — Pipeline run_id, date, source count, bundle pass/fail rates, analysis methods used
5. **Data Sources** — Full list of source URLs organized by type (filings, news, APIs)
6. **Risk Factors** — All high and medium risk findings summarized with recommended review actions
7. **Appendix** — Raw finding IDs, confidence distribution chart (text-based), processing timestamps

## Output Location

`/reports/YYYY-MM-DD/sentinel-crew-report.md`

## Distribution

On completion, Scribe sends the report path to the PM notification channel and logs the delivery timestamp. Reports classified as containing high-risk findings trigger an immediate alert.
