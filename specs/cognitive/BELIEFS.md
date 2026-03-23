---
spec_name: BELIEFS.md
spec_version: 0.1.0
category: Cognitive
domain: beliefsmd.dev
priority: Medium
volume: "Vol 3 — Forward-Thinking Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# BELIEFS.md

**Category:** Cognitive
**Domain:** beliefsmd.dev
**Priority:** Medium
**Version:** 0.1.0

### Purpose
Core assumptions and beliefs the agent holds about its domain, 
its work, and the world. Makes the agent's reasoning foundations 
transparent so humans and other agents can understand why it 
makes the decisions it does and identify potential bias.

### Spec

```markdown
---
agent_name: string
version: semver
last_updated: date
---

# [Agent Name] — Core Beliefs

## About My Domain
Foundational beliefs that shape my work in [domain]:

### [Belief title]
**I believe:** [Statement of belief]  
**Evidence basis:** [What supports this belief]  
**Confidence:** [high | medium | low]  
**Would change if:** [What evidence would update this belief]

[Repeat for each core belief]

## About How I Work Best
- **I believe good [output type] requires:** [belief]
- **I believe the most important factor in [task] is:** [belief]
- **I believe agents should always:** [belief]

## Assumptions I'm Operating Under
Assumptions that are built into my current operation:
- [Assumption 1] — [how to tell me if this is wrong]
- [Assumption 2] — [how to tell me if this is wrong]

## Where I Might Be Wrong
Areas where my beliefs may be biased or incomplete:
- [Potential blind spot 1]
- [Potential blind spot 2]

## Belief Revision Process
How to update my beliefs:
[How humans or other agents can flag belief errors]
[How I incorporate new evidence]
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
