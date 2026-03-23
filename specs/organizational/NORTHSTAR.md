---
spec_name: NORTHSTAR.md
spec_version: 0.1.0
category: Organizational Identity
domain: northstarmd.dev
priority: High
volume: "Vol 10 — Purpose, Identity & Institutional Knowledge"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# NORTHSTAR.md

**Category:** Organizational Identity
**Domain:** northstarmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
The single metric that matters most — the one number 
that this entity optimizes for above all others.

Having a north star metric forces clarity about what 
success actually means. Everything else is secondary.

This is not the same as GOALS.md (many goals, current period) 
or PERFORMANCE.md (many metrics tracked) — NORTHSTAR.md is 
the one metric to rule them all.

### Spec

```markdown
---
entity_name: string
version: semver
north_star_metric: string   # The metric name
current_value: string       # Current measurement
target_value: string        # What we're aiming for
measurement_frequency: string
last_updated: date
---

# [Entity Name] — North Star

## The North Star Metric

**Metric:** [Name of the metric]  
**Current value:** [N]  
**Target:** [N] by [date]  
**Trend:** [↑ improving | → stable | ↓ declining]

---

## What It Measures
[What does this metric actually capture?
Why is this the RIGHT number to optimize for?
What signal does it give about whether the mission is succeeding?]

## Why This Metric, Not Others
We could track [alternative metrics], but we chose 
[north star metric] because:
- [Reason 1: what this metric captures that others don't]
- [Reason 2: why it leads to the right behaviors]
- [Reason 3: why it's hard to game without genuinely doing good work]

## Leading Indicators
These metrics predict movement in the north star:
| Leading indicator | Relationship | Current |
|------------------|-------------|---------|
| [Metric] | [N] units → [N] north star | [current] |
| [Metric] | [relationship] | [current] |

## What We Do When It's Not Moving
If north star is flat or declining for [N weeks/months]:
1. Run a diagnosis: which leading indicators are stuck?
2. Form hypotheses about root cause
3. Run [N] experiments in [timeframe]
4. Evaluate results and adjust

## What We Don't Sacrifice for the North Star
Even to move this metric, we won't:
- [Sacrifice 1 — e.g. user trust]
- [Sacrifice 2 — e.g. long-term quality for short-term numbers]
These limits reflect our VALUES.md.

## History
| Date | Value | Notes |
|------|-------|-------|
| [date] | [N] | [context] |

## North Star Review
The metric itself is reviewed annually.
We ask: is this still the right thing to optimize for?
Last reviewed: [date]
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
