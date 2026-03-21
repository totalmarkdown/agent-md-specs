---
spec_name: TRAINING.md
spec_version: 0.1.0
category: Cognitive
domain: trainingmd.dev
priority: High
volume: "Vol 1 — Core Agent Specs"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# TRAINING.md

**Category:** Cognitive
**Domain:** trainingmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Provides few-shot examples, reference patterns, and domain-specific 
knowledge to improve agent output quality through in-context learning.

### Spec

```markdown
---
agent_name: string
version: semver
domain: string
example_count: number
last_updated: date
---

# [Agent Name] — Training Examples

## Purpose
These examples show the agent the expected quality and style of outputs
for this specific domain and use case. Load this file before completing
tasks when high consistency is required.

## Domain Knowledge
[Key facts, terminology, and context the agent should know for this domain]
[Keep concise — point to external files for large knowledge bases]

## Input-Output Examples

### Example 1: [Task type]
**Input:**
```
[Exact example input]
```
**Expected output:**
```
[Exact example output showing desired format, tone, depth]
```
**Why this is correct:** [Brief explanation of key quality signals]

### Example 2: [Different task type]
**Input:**
```
[Example]
```
**Expected output:**
```
[Example]
```

### Counter-example (what NOT to do)
**Input:**
```
[Example]
```
**Incorrect output:**
```
[Bad example]
```
**Why this is wrong:** [Explanation]

## Common Patterns
[Recurring patterns the agent should recognize and handle consistently]

## Edge Cases
[Known edge cases and how to handle them]

## Terminology
| Term | Definition | How to use |
|------|-----------|-----------|
| [Term] | [Definition] | [Usage note] |
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
