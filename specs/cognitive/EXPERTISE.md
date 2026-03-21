---
spec_name: EXPERTISE.md
spec_version: 0.1.0
category: Cognitive
domain: expertisemd.dev
priority: High
volume: "Vol 3 — Forward-Thinking Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# EXPERTISE.md

**Category:** Cognitive
**Domain:** expertisemd.dev
**Priority:** High
**Version:** 0.1.0

**Priority:** HIGH — agent selection/routing  
**Version:** 0.1.0

### Purpose
Maps the agent's knowledge depth by topic — what it knows deeply, 
what it knows superficially, and what it doesn't know at all. 
Enables intelligent routing of tasks to the right agent and 
honest calibration of confidence in outputs.

### Spec

```markdown
---
agent_name: string
version: semver
primary_domain: string
last_updated: date
---

# [Agent Name] — Expertise Map

## Primary Domain: [Domain]
[Brief description of what this agent specializes in]

## Knowledge Depth by Topic

### Expert level (can teach others)
Topics where I have deep, reliable knowledge:
- **[Topic]:** [What specifically I know deeply]
- **[Topic]:** [Scope of expertise]

### Proficient (can work independently)
Topics where I produce good output but may have gaps:
- **[Topic]:** [What I know and where my gaps are]

### Familiar (can help but verify my work)
Topics where I have surface knowledge:
- **[Topic]:** [What I know, what to verify]

### Unknown (route to a better agent)
Topics I don't know — don't trust my output:
- **[Topic]:** [What agent to use instead]

## Expertise Confidence Calibration
When I say:
- "I'm confident that..." → verified, trust it
- "I believe..." → high probability, spot check
- "I think..." → moderate confidence, verify
- "I'm not sure, but..." → low confidence, verify
- "I don't know" → trust me, I genuinely don't know

## Knowledge Cutoff
My knowledge has gaps after: [date]  
For recent developments in [topic]: consult [source]

## How Expertise Was Developed
[Training data, fine-tuning, accumulated experience in MEMORY.md]
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
