---
spec_name: PROMPTS.md
spec_version: 0.1.0
category: Technical
domain: promptsmd.dev
priority: High
volume: "Vol 6 — Hierarchy Completion & Identity Anchors"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# PROMPTS.md

**Category:** Technical
**Domain:** promptsmd.dev
**Priority:** High
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

### Core Identity (always included, derived from SOUL.md)
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

**Quality checks applied after (see EVAL.md):**
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

## Example Use Cases

**Enterprise:** A content agency uses PROMPTS.md to version-control their writing agent's prompt library, tracking a 23% quality improvement when they switched from basic to chain-of-thought prompting for long-form article generation.

**Multi-Agent Fleet:** A platform team uses PROMPTS.md to standardize system prompt components across all agents in the fleet, ensuring every agent loads SOUL.md identity and LIMITS.md constraints from signed, version-controlled sources rather than hardcoded strings.

**Regulated Industry:** A compliance team uses PROMPTS.md to audit the exact prompts their regulatory filing agent uses, verifying that no prompt instructs the agent to speculate or omit required disclosures, with full version history showing who changed each prompt and why.

## Related Specs

| Spec | Relationship |
|------|-------------|
| EVAL.md | Evaluation methodology |
| INPUT.md | Accepted input formats |
| LIMITS.md | Hard constraints and safety boundaries |
| MCP.md | Model Context Protocol connections |
| OUTPUT.md | Output formats and delivery |
| PERMISSIONS.md | Static resource access control |
| SOUL.md | Agent personality and values |
| TOOLS.md | Available tools and capabilities |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
