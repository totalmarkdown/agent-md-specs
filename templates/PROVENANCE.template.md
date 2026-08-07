---
spec_name: PROVENANCE.md
spec_version: 0.1.0
category: Compliance
priority: High
tier: core
---

# [REPLACE THIS — Agent Name] — Data Provenance

<!-- Track where data came from, how it was transformed, and who touched it -->

## Data Sources
<!-- Every input this agent consumes -->

| Source | Type | Trust Level | Refresh Rate |
|--------|------|-------------|-------------|
| [REPLACE THIS] | [REPLACE THIS — API | file | database | agent] | [REPLACE THIS — high | medium | low] | [REPLACE THIS] |
| [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |

## Lineage Tracking
- **Track granularity:** [REPLACE THIS — per-record | per-batch | per-session]
- **Lineage format:** [REPLACE THIS — W3C PROV | custom | embedded metadata]
- **Storage:** [REPLACE THIS — where lineage records are kept]

## Transformations
<!-- How this agent modifies data between input and output -->

| Step | Input | Transformation | Output |
|------|-------|----------------|--------|
| 1 | [REPLACE THIS] | [REPLACE THIS — e.g. filter, enrich, summarize] | [REPLACE THIS] |
| 2 | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |

## Output Labeling
<!-- Every output must carry its origin metadata -->
- **Label format:** [REPLACE THIS — header | footer | embedded metadata | sidecar]
- **Includes:** [REPLACE THIS — source IDs | transformation log | confidence score]
- **Example label:** [REPLACE THIS — brief example of what gets attached to output]

## Verification
- **Reproducible:** [REPLACE THIS — can the same inputs produce the same outputs? yes | no | partially]
- **Spot-check frequency:** [REPLACE THIS — how often lineage is audited]
- **Discrepancy action:** [REPLACE THIS — what happens if lineage is broken]

## Related Specs
- AUDITTRAIL.md: [REPLACE THIS — path]
- MEMORYSAFETY.md: [REPLACE THIS — path]
- SHAREDCONTEXT.md: [REPLACE THIS — path]
