---
spec_name: KPI.md
spec_version: 0.1.0
category: Performance/Governance
domain: kpimd.dev
priority: High
volume: "Vol 11 — Performance, Defensibility & Interface Contracts"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# KPI.md

**Category:** Performance/Governance
**Domain:** kpimd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
The full set of key performance indicators that collectively 
prove this agent or organization is healthy and on track.

The hierarchy of measurement:
```
NORTHSTAR.md    ← The one number that matters most
KPI.md          ← The balanced scorecard (8-15 metrics)
PERFORMANCE.md  ← Operational benchmarks over time
TESTSCORES.md   ← Assessment results
GOALS.md        ← Objectives with timeframes
```

Good KPIs are:
- **Measurable** — actual numbers, not feelings
- **Actionable** — someone can influence them
- **Leading OR lagging** — know which you're looking at
- **Few enough to remember** — ideally under 12

### Spec

```markdown
---
entity_name: string
version: semver
kpi_count: number
reporting_cadence: string    # daily | weekly | monthly | quarterly
dashboard_url: string        # Where to see live KPIs
last_updated: date
---

# [Entity Name] — KPIs

## KPI Dashboard
**Live dashboard:** [URL]  
**Reporting cadence:** [frequency]  
**Owner:** [Who is accountable for KPI health]

---

## North Star (1 metric)
See NORTHSTAR.md for full context.

| Metric | Current | Target | Trend |
|--------|---------|--------|-------|
| [North Star metric] | [value] | [target] | [↑/→/↓] |

---

## Quality KPIs

| KPI | Current | Target | Threshold | Trend |
|-----|---------|--------|-----------|-------|
| Task success rate | [N]% | [N]% | >[N]% | [↑/→/↓] |
| Output quality score | [N]/100 | [N]/100 | >[N] | [↑/→/↓] |
| Human satisfaction | [N]/5 | [N]/5 | >[N] | [↑/→/↓] |
| Error rate | [N]% | <[N]% | <[N]% | [↑/→/↓] |
| First-attempt success | [N]% | [N]% | >[N]% | [↑/→/↓] |

---

## Speed KPIs

| KPI | Current | Target | Threshold | Trend |
|-----|---------|--------|-----------|-------|
| Mean response time | [N]ms | <[N]ms | <[N]ms | [↑/→/↓] |
| p95 response time | [N]ms | <[N]ms | <[N]ms | [↑/→/↓] |
| Task completion time | [N]min | <[N]min | <[N]min | [↑/→/↓] |
| Queue wait time | [N]sec | <[N]sec | <[N]sec | [↑/→/↓] |

---

## Efficiency KPIs

| KPI | Current | Target | Threshold | Trend |
|-----|---------|--------|-----------|-------|
| Tokens per task | [N] | <[N] | <[N] | [↑/→/↓] |
| Cost per task | $[X] | <$[X] | <$[X] | [↑/→/↓] |
| Tasks per hour | [N] | >[N] | >[N] | [↑/→/↓] |
| Budget utilization | [N]% | [N]% | <[N]% | [↑/→/↓] |

---

## Reliability KPIs

| KPI | Current | Target | Threshold | Trend |
|-----|---------|--------|-----------|-------|
| Uptime | [N]% | [N]% | >[N]% | [↑/→/↓] |
| Heartbeat success | [N]% | 100% | >99% | [↑/→/↓] |
| Escalation rate | [N]% | <[N]% | <[N]% | [↑/→/↓] |
| Guardrail triggers | [N]/day | <[N]/day | <[N]/day | [↑/→/↓] |

---

## Growth KPIs (if marketplace/product)

| KPI | Current | Target | Trend |
|-----|---------|--------|-------|
| Active installs | [N] | [N] | [↑/→/↓] |
| Monthly downloads | [N] | [N] | [↑/→/↓] |
| Reviews (avg) | [N]/5 | >[N]/5 | [↑/→/↓] |
| Retention (30-day) | [N]% | >[N]% | [↑/→/↓] |
| Revenue/MRR | $[X] | $[X] | [↑/→/↓] |

---

## KPI Thresholds and Actions

### Green (healthy — no action)
All KPIs within target range.

### Yellow (watch — investigate)
Any KPI between threshold and target:
- Log the deviation
- Identify likely cause
- Monitor for [N] periods before acting

### Red (act — immediate attention)
Any KPI below threshold:
- Alert owner immediately
- Root cause analysis within [N] hours
- Remediation plan within [N] hours
- Executive notification if [specific KPIs] are red

---

## KPI History
| Period | North Star | Quality | Speed | Reliability |
|--------|-----------|---------|-------|------------|
| [period] | [N] | [N] | [N] | [N] |

## KPI Review Cadence
- **Daily:** Speed + reliability (automated)
- **Weekly:** Quality + efficiency (owner review)
- **Monthly:** All KPIs + trend analysis (team review)
- **Quarterly:** KPI set itself — are these the right metrics?

## Adding/Changing KPIs
KPIs should only change when strategy changes.
To propose a KPI change: [process]
Changes require: [approval level]
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
