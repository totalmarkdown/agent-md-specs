---
spec_name: INPUT.md
spec_version: 0.1.0
category: Technical/Interface
domain: inputmd.dev
priority: Very High
volume: "Vol 11 — Performance, Defensibility & Interface Contracts"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
---

# INPUT.md

**Category:** Technical/Interface
**Domain:** inputmd.dev
**Priority:** Very High
**Version:** 0.1.0

### Purpose
The complete formal specification of everything this agent 
accepts as input — formats, schemas, validation rules, 
size limits, required vs optional fields, and what happens 
when input is malformed.

INPUT.md is one half of the agent's interface contract.
OUTPUT.md is the other half.
Together they enable programmatic integration without 
reading the source code.

Different from:
- DATA.md — data sources and pipelines
- TOOLS.md — tools the agent uses
- API.md — HTTP endpoint specifications

INPUT.md is specifically: what do you give this agent?

### Spec

```markdown
---
agent_name: string
version: semver
primary_input_format: string   # text | json | markdown | file | multimodal
schema_version: string
last_updated: date
---

# [Agent Name] — Input Specification

## Input Overview
**Primary format:** [text | json | markdown | file | multimodal]  
**Schema:** [version of input schema]  
**Validation:** [strict | lenient | none]  
**Max input size:** [N tokens | N characters | N MB]

---

## Input Types

### Type 1: [Input type name — e.g. "Natural language task"]

**Format:** [Plain text | Markdown | JSON | Other]  
**When to use:** [Use cases this input type is designed for]  
**Required fields:** [List if structured]  
**Optional fields:** [List if structured]  
**Size limits:** [min/max tokens or characters]

**Example:**
```
[Concrete minimal example of valid input of this type]
```

**What makes this input effective:**
- Include: [what helps the agent]
- Avoid: [what confuses the agent]

---

### Type 2: [Input type name — e.g. "Structured task brief"]

**Format:** JSON  
**Schema:**
```json
{
  "task": {
    "type": "string",           // required — task type identifier
    "instruction": "string",    // required — what to do
    "context": "string",        // optional — background info
    "constraints": ["string"],  // optional — limitations
    "format": "string",         // optional — desired output format
    "examples": []              // optional — input/output examples
  },
  "config": {
    "quality": "fast|balanced|thorough",  // optional, default: balanced
    "max_tokens": "integer",              // optional
    "language": "string"                 // optional, default: en
  },
  "metadata": {
    "task_id": "string",        // optional — your tracking ID
    "priority": "low|normal|high|urgent",  // optional
    "deadline": "ISO-8601"      // optional
  }
}
```

**Minimal valid example:**
```json
{
  "task": {
    "type": "analyze",
    "instruction": "Summarize the key findings in this research"
  }
}
```

**Full example:**
```json
{
  "task": {
    "type": "analyze",
    "instruction": "Summarize the key findings",
    "context": "This is a quarterly business review",
    "constraints": ["under 200 words", "bullet points"],
    "format": "markdown"
  },
  "config": {
    "quality": "thorough"
  },
  "metadata": {
    "task_id": "task_abc123",
    "priority": "normal"
  }
}
```

---

### Type 3: [File input — if applicable]

**Accepted formats:** [.md | .txt | .pdf | .json | .csv | etc]  
**Max file size:** [N MB]  
**Max files per request:** [N]  
**Encoding:** [UTF-8 required | other]

**How to send files:**
- Via CLI: [command syntax]
- Via API: [multipart/form-data | base64 | URL reference]
- Via MCP: [tool name and parameters]

---

## Input Validation

### What gets rejected (400 error)
| Issue | Error message | Resolution |
|-------|-------------|-----------|
| Missing required field | "Field '[name]' is required" | Add the field |
| Invalid format | "Expected [format], got [received]" | Fix format |
| Too large | "Input exceeds [N] token limit" | Reduce input |
| Invalid enum value | "Valid values: [list]" | Use valid value |
| [Other] | "[message]" | [resolution] |

### What gets sanitized (warning)
| Issue | What happens | Warning message |
|-------|-------------|----------------|
| Extra whitespace | Trimmed | None |
| Unknown fields | Ignored | "Unknown fields ignored: [list]" |
| [Other] | [handling] | [message] |

---

## Special Input Behaviors

### Context injection
The agent automatically adds to its context:
- Current MEMORY.md content
- Relevant GOALS.md entries
- Current DEADLINES.md if task has deadline relevance

### Input preprocessing
Before the model sees the input, these transformations occur:
- [Preprocessing step 1]
- [Preprocessing step 2]

### Input that triggers special modes
| Input pattern | Triggered mode |
|--------------|---------------|
| "[pattern]" | [what mode activates] |
| "urgent: ..." | High priority processing |

---

## Input Size Guidance

| Task complexity | Recommended input size | Notes |
|----------------|----------------------|-------|
| Simple task | <500 tokens | Fast, cheap |
| Standard task | 500-2000 tokens | Balanced |
| Complex task | 2000-8000 tokens | Thorough |
| Maximum | [N] tokens | Quality may degrade near limit |

**Token estimation:**
- 1 token ≈ 4 characters in English
- 1 page of text ≈ 500 tokens
- Use: `tmd count-tokens --text "[your input]"`
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| API.md | HTTP API specification |
| DEADLINES.md | Time constraints and schedules |
| GOALS.md | Objectives and success criteria |
| MCP.md | Model Context Protocol connections |
| MEMORY.md | Individual agent memory governance |
| OUTPUT.md | Output formats and delivery |
| PERMISSIONS.md | Static resource access control |
| PROMPTSHIELD.md | Prompt injection defense |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
