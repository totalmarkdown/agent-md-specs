---
spec_name: TRAINING.md
spec_version: 0.1.0
category: Cognitive
domain: trainingmd.dev
priority: High
volume: "Vol 1 — Core Agent Specs"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
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
See LEARNING.md for the agent's forward-looking learning agenda.

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
[Known edge cases and how to handle them — see EVAL.md for how these are tested]

## Terminology
| Term | Definition | How to use |
|------|-----------|-----------|
| [Term] | [Definition] | [Usage note] |
```

## Example Use Cases

**Enterprise:** An e-commerce product-description agent loads TRAINING.md with 15 curated input/output examples in the brand's voice before each batch run, ensuring consistent tone and format across thousands of SKU descriptions.

**Multi-Agent Fleet:** A platform operator maintains domain-specific TRAINING.md files for each vertical (healthcare, legal, finance) and loads the appropriate one when spinning up a general-purpose agent for a specialized task, achieving domain quality without maintaining separate models.

**Regulated Industry:** A regulatory filing agent's TRAINING.md includes counter-examples of common SEC formatting errors and explains why each is wrong, reducing submission rejection rates by teaching the agent to recognize and avoid known compliance pitfalls.

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
