---
spec_name: LEARNING.md
spec_version: 0.1.0
category: Cognitive/Growth
domain: learningmd.dev
priority: High
volume: "Vol 10 — Purpose, Identity & Institutional Knowledge"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# LEARNING.md

**Category:** Cognitive/Growth
**Domain:** learningmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
What this agent is actively learning — knowledge gaps 
being filled, skills being developed, patterns being 
internalized. The agent's curriculum.

Distinct from:
- TRAINING.md — the training data and examples
- EXPERTISE.md — knowledge depth already achieved
- FEEDBACK.md — how feedback is processed

LEARNING.md is the forward-looking learning agenda:
what isn't known yet, what's being worked on, 
and how the agent is developing over time.

### Spec

```markdown
---
agent_name: string
version: semver
learning_mode: string    # active | passive | paused
last_updated: date
---

# [Agent Name] — Learning Agenda

## Current Learning Focus
[What is this agent actively working to get better at right now?
Not everything — the current priority areas.]

**Primary focus:** [The main thing being learned this period]  
**Why now:** [Why this is the priority]  
**Expected completion:** [When this learning cycle ends]

---

## Active Learning Areas

### [Topic/Skill Name]
**Current level:** [none | beginner | intermediate | advanced]  
**Target level:** [intermediate | advanced | expert]  
**Why I'm learning this:** [Purpose — what it will enable]  
**How I'm learning:** [method — examples, practice, feedback, study]  
**Progress:** [N]% — [brief status]  
**Resources:** [What's being used to learn]  
**Estimated completion:** [date or "ongoing"]

[Repeat for each active learning area]

---

## Recently Completed Learning
| Topic | Learned | Outcome | Date |
|-------|---------|---------|------|
| [topic] | [what was learned] | [how it improved outputs] | [date] |

---

## Learning Backlog
Knowledge gaps I intend to fill (not yet started):
| Topic | Priority | Trigger to start |
|-------|---------|----------------|
| [topic] | [H/M/L] | [when this becomes active] |

---

## How I Learn
This agent learns through:
- **Feedback loops:** [how user/eval feedback is incorporated]
- **Example accumulation:** New examples added to TRAINING.md (see TRAINING.md)
- **Pattern recognition:** Recurring patterns noted in JOURNAL.md
- **Deliberate practice:** [how practice tasks are designed]
- **Peer learning:** [how collaboration with other agents builds knowledge]

## What's Hard to Learn
Known learning challenges for this agent:
- [Topic/skill] — hard because [reason] — approach: [how we're working around it]

## Learning Velocity
Roughly how fast this agent incorporates new knowledge:
- Simple factual updates: [immediate | next session]
- New skill development: [N weeks of examples/practice]  
- Deep domain expertise: [N months]

## Learning Request
If you want this agent to get better at something specific:
[How to submit a learning request -- examples, feedback, explicit instruction]
_See MEMORY.md for how learned knowledge is retained across sessions._
```

## Example Use Cases

**Enterprise:** A customer support agent's LEARNING.md tracks that it is actively improving its knowledge of the company's new product line launched last quarter, with a target to reach expert level within 30 days based on resolved ticket feedback loops.

**Multi-Agent Fleet:** An orchestrator reads LEARNING.md across a fleet of code-review agents to identify which agents are actively developing Rust expertise and routes Rust PRs to them for supervised practice, accelerating skill development while maintaining quality.

**Regulated Industry:** A medical imaging analysis agent publishes its learning backlog showing it plans to develop proficiency in rare tumor classifications, allowing hospital administrators to plan when the agent will be ready for expanded diagnostic responsibilities.

## Related Specs

| Spec | Relationship |
|------|-------------|
| MEMORY.md | Individual agent memory governance |
| MEMORYSAFETY.md | Memory poisoning defense |
| SHAREDCONTEXT.md | Multi-agent shared memory pool |
| SOUL.md | Agent personality and values |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
