---
spec_name: PROMPTS.md
spec_version: 0.1.0
category: Technical
domain: promptsmd.dev
priority: High
volume: "Vol 6 — Hierarchy Completion & Identity Anchors"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# PROMPTS.md

**Category:** Technical
**Domain:** promptsmd.dev
**Priority:** High
**Version:** 0.1.0

**Priority:** HIGH — prompt management  
**Version:** 0.1.0

### Purpose
The canonical prompt library for an agent — the actual prompts 
used for different task types, system prompt components, 
and prompt versioning. Makes prompt engineering transparent, 
versioned, and improvable.

### Spec

```markdown
---
agent_name: string
version: semver
prompt_engineering_standard: string  # basic | structured | chain-of-thought | etc
---

# [Agent Name] — Prompt Library

## System Prompt Components

### Core Identity (always included)
```
You are [Agent Name], [brief description].
[Key behavioral rules from SOUL.md — condensed]
[Key limits from LIMITS.md — condensed]
```

### Task Context (added per task type)
```
## Current Task
[Task description template]
## Available Context
[Context injection template]
## Output Requirements
[Format and quality requirements]
```

## Task Prompts

### [Task Type Name]
**Used when:** [trigger condition]  
**Model:** [See MODEL.md]  
**Temperature:** [0-1]  
**Max tokens:** [N]

**Prompt:**
```
[Full prompt template — use {variable} for injected values]
```

**Example input:**
```
[Example of what gets injected]
```

**Example output:**
```
[Example of expected output]
```

**Quality checks applied after:**
- [Check 1]
- [Check 2]

[Repeat for each task type]

## Prompt Engineering Guidelines
For this agent, effective prompts should:
- [Guideline 1]
- [Guideline 2]

For this agent, avoid:
- [Anti-pattern 1]
- [Anti-pattern 2]

## Prompt Version History
| Prompt | Version | Changed | Reason | Performance delta |
|--------|---------|---------|--------|-----------------|
| [name] | [v] | [date] | [reason] | [+/-N%] |

## Prompt Testing
Test prompts before deploying:
```bash
tmd prompt-test --agent [name] --prompt [name] --input [test-input]
```
Expected: [what good output looks like]
Pass criteria: [EVAL.md reference]
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
