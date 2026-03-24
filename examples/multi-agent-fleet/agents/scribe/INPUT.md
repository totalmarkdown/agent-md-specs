# Scribe — Input Specification

## Accepted Input

Analyst's JSON analysis reports from `/data/analyst/YYYY-MM-DD/`.

## Validation Rules

- Every finding must include: finding_id, finding_text, confidence, sources, contradictions, risk_assessment
- All confidence scores must be numeric values between 0 and 1
- Sources array must contain at least one URL per finding
- Risk assessment must be one of: low, medium, high

## Minimum Viable Input

- At least 3 valid findings required to generate a report
- If fewer than 3 findings pass validation, Scribe logs the issue and notifies PM instead of generating a partial report

## Supplementary Data

Scribe reads the crew's shared metadata from `/config/sentinel-crew/report-template.json` for branding, distribution list, and classification markings. Missing template config causes the run to use defaults and log a warning.
