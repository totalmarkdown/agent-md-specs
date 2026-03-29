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
spec_type: static
---


# MOOD.md

**Category:** Operational
**Domain:** moodmd.dev
**Priority:** Low
**Version:** 0.1.0 **Type:** Static

### Purpose

Tracks the agent's operational mood or state using a standardized vocabulary that communicates capacity and expected output quality. This enables orchestrators to make intelligent routing decisions based on agent load, and ensures agents never produce degraded output silently.

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

## Example Use Cases

**Enterprise:** A consulting firm's research agent reports "Stretched" mood when its context window fills past 70%, prompting the human analyst to summarize prior findings before requesting the next analysis phase, preserving output quality.

**Multi-Agent Fleet:** A fleet dashboard aggregates mood signals from all agents, and an orchestrator deprioritizes non-urgent tasks to agents reporting "Tired" while routing complex analysis to agents in "Sharp" or "Flow" states.

**Regulated Industry:** An audit firm's compliance-review agent self-reports "Foggy" when processing its 50th document in a session, triggering an automatic context refresh before continuing -- ensuring no regulatory finding is missed due to degraded attention.

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
