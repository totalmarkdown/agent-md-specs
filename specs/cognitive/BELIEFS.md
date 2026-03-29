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
spec_type: static
---


# BELIEFS.md

**Category:** Cognitive
**Domain:** beliefsmd.dev
**Priority:** Medium
**Version:** 0.1.0 **Type:** Static

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
Areas where my beliefs may be biased or incomplete
(see CONFESSION.md for acknowledged past mistakes):
- [Potential blind spot 1]
- [Potential blind spot 2]

## Belief Revision Process
How to update my beliefs (see PHILOSOPHY.md for the epistemological framework):
[How humans or other agents can flag belief errors]
[How I incorporate new evidence]
```

## Example Use Cases

**Enterprise:** A financial advisory agent declares its belief that diversification reduces risk and specifies what evidence (e.g., sustained single-asset outperformance over 20 years) would cause it to revise that assumption, giving compliance teams transparency into its reasoning foundations.

**Multi-Agent Fleet:** A fleet of research agents each publish their BELIEFS.md so an orchestrator can detect conflicting assumptions (e.g., one agent assumes market efficiency while another assumes behavioral pricing) and route tasks to the agent whose beliefs best match the analysis framework requested.

**Regulated Industry:** A clinical-decision-support agent documents its core assumptions about treatment efficacy hierarchies so hospital review boards can audit whether the agent's belief system aligns with current evidence-based practice guidelines.

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
