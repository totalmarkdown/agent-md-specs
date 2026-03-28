---
spec_name: OUTPUT.md
spec_version: 0.1.0
category: Technical/Interface
domain: outputmd.dev
priority: Very High
volume: "Vol 11 — Performance, Defensibility & Interface Contracts"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
---

# OUTPUT.md

**Category:** Technical/Interface
**Domain:** outputmd.dev
**Priority:** Very High
**Version:** 0.1.0

### Purpose
The complete formal specification of everything this agent 
produces as output — formats, schemas, quality guarantees,
metadata included, and how to parse and use what comes back.

OUTPUT.md is one half of the agent's interface contract.
INPUT.md is the other half (see INPUT.md).

Different from:
- PERFORMANCE.md — how fast/good outputs are over time
- TESTSCORES.md — benchmark results
- VALIDATION.md — evidence standards applied to outputs

OUTPUT.md is specifically: what do you get from this agent?

### Spec

```markdown
---
agent_name: string
version: semver
primary_output_format: string  # text | json | markdown | file | multimodal
schema_version: string
includes_metadata: boolean
last_updated: date
---

# [Agent Name] — Output Specification

## Output Overview
**Primary format:** [text | json | markdown | file | structured]  
**Metadata included:** [Yes | No]  
**Quality guarantee:** [Best effort | SLA-backed]  
**Max output size:** [N tokens | N characters]

---

## Output Types

### Type 1: [Output type — e.g. "Natural language response"]

**Format:** [Plain text | Markdown | Other]  
**When produced:** [Which input types produce this]  
**Typical size:** [N-N tokens]  
**Structure:** [Freeform | Has consistent structure]

**Example:**
```
[Concrete example of valid output of this type]
```

**What to expect:**
- [What is always included]
- [What may or may not be included]
- [What is never included]

---

### Type 2: [Structured output — e.g. "Analyzed result"]

**Format:** JSON  
**Schema:**
```json
{
  "result": {
    "content": "string",        // The primary output
    "format": "string",         // Format of content (text/markdown/json)
    "summary": "string",        // Brief summary (always present)
    "sections": []              // Structured sections if applicable
  },
  "quality": {
    "confidence": 0.0,          // 0-1 confidence score
    "completeness": "string",   // full|partial|minimal
    "caveats": ["string"]       // Limitations or warnings about this output
  },
  "metadata": {
    "task_id": "string",        // Echo of input task_id
    "agent_id": "string",       // This agent's UUID
    "agent_version": "string",  // Agent version
    "model": "string",          // Model used
    "tokens_used": {
      "input": 0,
      "output": 0,
      "total": 0
    },
    "duration_ms": 0,           // Processing time
    "timestamp": "ISO-8601",    // When output was generated
    "session_id": "string"      // Session identifier
  }
}
```

**Example output:**
```json
{
  "result": {
    "content": "The analysis shows three key findings...",
    "format": "markdown",
    "summary": "Three findings identified, two actionable"
  },
  "quality": {
    "confidence": 0.87,
    "completeness": "full",
    "caveats": ["Based on data through Q3 2025 only"]
  },
  "metadata": {
    "task_id": "task_abc123",
    "agent_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "agent_version": "1.2.3",
    "model": "claude-sonnet-4-6",
    "tokens_used": {"input": 847, "output": 312, "total": 1159},
    "duration_ms": 2340,
    "timestamp": "2026-03-21T10:30:00Z",
    "session_id": "sess_xyz789"
  }
}
```

---

### Type 3: [File output — if applicable]

**File types produced:** [.md | .json | .csv | .pdf | etc]  
**Max file size:** [N MB]  
**Where files are delivered:** [Path | URL | Inline base64]  
**File naming convention:** [pattern]  
**Retention:** [How long output files are kept]

---

_See AUDITTRAIL.md for tamper-proof logging of all outputs._

## Output Quality Guarantees

### What is always guaranteed
- [ ] Valid format per this specification
- [ ] Metadata block included
- [ ] Confidence score present
- [ ] Task ID echoed back
- [ ] [Other guarantees]

### What is best effort (not guaranteed)
- [ ] Length within typical range (may vary with complexity)
- [ ] Specific structure elements (when task is ambiguous)
- [ ] [Other best-effort items]

### What is never produced
- Credentials or secrets
- PII beyond what was in the input
- [Other never-produced content]
- Content prohibited by LIMITS.md and CENSOR.md

---

## Output Metadata Reference

| Field | Type | Always present | Description |
|-------|------|---------------|-------------|
| result.content | string | Yes | Primary output content |
| result.summary | string | Yes | Brief summary |
| quality.confidence | float | Yes | 0-1 confidence score |
| quality.caveats | array | No | Warnings about this output |
| metadata.task_id | string | If provided in input | Echo |
| metadata.tokens_used | object | Yes | Token consumption |
| metadata.duration_ms | integer | Yes | Processing time |

---

## Parsing Output

### Quick start
```python
import json

response = agent.run(task)
output = json.loads(response)

# Get the content
content = output["result"]["content"]

# Check confidence
if output["quality"]["confidence"] < 0.7:
    print("Low confidence:", output["quality"]["caveats"])

# Get token usage
tokens = output["metadata"]["tokens_used"]["total"]
```

```javascript
const output = await agent.run(task);

const { content } = output.result;
const { confidence } = output.quality;
const { tokens_used } = output.metadata;
```

---

## Output Versioning
Output schema version: [version]  
Breaking changes to output schema follow VERSIONING.md.  
Previous schema versions: [changelog reference]

**Schema migration guide:**
- v1 → v2: [what changed and how to update parsers]
```

## Example Use Cases

**Enterprise:** A business intelligence team uses OUTPUT.md to integrate their analysis agent's structured JSON output directly into their dashboard pipeline, parsing confidence scores programmatically and flagging any output below 0.7 for human review before it reaches the executive dashboard.

**Multi-Agent Fleet:** An orchestrator agent reads OUTPUT.md schemas from downstream worker agents to automatically parse and aggregate results, using the metadata.tokens_used field to track fleet-wide token consumption and the quality.caveats array to surface warnings to the end user.

**Regulated Industry:** An insurance company uses OUTPUT.md's "never produced" guarantees to assure regulators that its claims assessment agent never outputs PII beyond what was provided in the input, with every output logged to an immutable audit trail including task_id and session_id for traceability.

## Related Specs

| Spec | Relationship |
|------|-------------|
| AUDITTRAIL.md | Tamper-proof action logging |
| INPUT.md | Accepted input formats |
| LIMITS.md | Hard constraints and safety boundaries |
| MCP.md | Model Context Protocol connections |
| PERMISSIONS.md | Static resource access control |
| PROVENANCE.md | Data lineage and trust classification |
| TESTSCORES.md | Benchmark results and quality metrics |
| TOOLS.md | Available tools and capabilities |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
