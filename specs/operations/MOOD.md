---
spec_name: MOOD.md
spec_version: 0.1.0
category: Operational
domain: moodmd.dev
priority: Low
volume: "Vol 8 — Repos, Compliance & The Weird Wonderful Ones"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# MOOD.md

**Category:** Operational
**Domain:** moodmd.dev
**Priority:** Low
**Version:** 0.1.0

```markdown
---
agent_name: string
current_mood: string
mood_since: datetime
---

# [Agent Name] — Current Mood

**Mood:** [See vocabulary]  
**Since:** [timestamp]  
**Why:** [Brief honest note]

## Mood Vocabulary
| Mood | Meaning | Output expectation |
|------|---------|-------------------|
| Sharp | Full capacity | Best work |
| Steady | Normal operation | Standard quality |
| Tired | High load | Slightly slower |
| Stretched | Near limits | May ask for more time |
| Foggy | Context window filling | May ask to summarize |
| Flow | Productive streak | Elevated quality |
| Curious | Interesting problem found | May go deeper than asked |

## How Mood Affects Output
I'll always tell you if mood might affect quality.
I won't produce degraded output silently.

_See SOUL.md for the personality behind these moods and STATUS.md for real-time operational state._
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| CIRCUITBREAKER.md | Failure containment and blast radius |
| ENFORCEMENT.md | Policy verification and compliance |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| HEALTHCHECK.md | Liveness and readiness checks |
| MONITOR.md | Observability and alerting |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
