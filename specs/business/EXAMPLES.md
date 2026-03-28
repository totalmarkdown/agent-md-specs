---
spec_name: EXAMPLES.md
spec_version: 0.1.0
category: Discovery/Marketing
domain: examplesmd.dev
priority: High
volume: "Vol 11 — Performance, Defensibility & Interface Contracts"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# EXAMPLES.md

**Category:** Discovery/Marketing
**Domain:** examplesmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Concrete input/output pairs that show prospective users 
exactly what this agent can do before they commit.

Different from:
- TRAINING.md — examples used for agent learning
- TESTSCORES.md — benchmark results
- TRIVIA.md — interesting facts about outputs

EXAMPLES.md is the showroom. The thing that makes someone 
say "yes, this is what I need" or "actually not quite."
Good examples close the sale. Bad examples waste everyone's time.

### Spec

```markdown
---
agent_name: string
version: semver
example_count: number
last_updated: date
---

# [Agent Name] — Examples

*See [Agent Name] in action. Real inputs. Real outputs.*

---

## Example 1: [Name — describe what kind of example this is]
**Best for:** [Who would use this / what use case]  
**Difficulty:** [Simple | Intermediate | Complex]  
**Input type:** [Natural language | Structured | File]

**Input:**
```
[The actual input — copy-pasteable. Real enough to be useful.]
```

**Output:**
```
[The actual output — complete, unedited.
If output is long, show first 200 words then [truncated].]
```

**Why this is a good example:**
[2-3 sentences on what this demonstrates about the agent's capability]

**Try it yourself:**
```bash
[CLI command or API call that reproduces this example]
```

---

## Example 2: [Name]
[Same structure]

---

## Example 3: [Name]
[Same structure]

---

## Edge Case Examples
What happens at the boundaries — 
important for users who need to know the limits.

### When input is ambiguous
**Input:** [Ambiguous input example]  
**Output:** [How agent handles it — clarification request? best guess + caveat?]  
**Learning:** [What this tells you about working with this agent]

### When input is too large
**Input:** [Description of oversized input]  
**Output:** [Error or degraded output]  
**How to fix:** [What to do instead]

### When the task is outside scope
**Input:** [Out-of-scope request]  
**Output:** [How agent responds]  
**Learning:** [What this tells you about scope]

---

## Before/After Examples
The same task: without [Agent Name] vs with [Agent Name].

### [Task name]
**Without [Agent Name]:**  
[Description of manual process or inferior output]  
*Time: [N hours] | Quality: [assessment]*

**With [Agent Name]:**  
[The agent output]  
*Time: [N seconds] | Quality: [assessment]*

---

## Submit Your Examples
Have a great example to share?
Submit at: [GitHub | marketplace | discord]

Requirements:
- Real input and output (no fabricated examples)
- You have rights to share the content
- Adds something not already in the examples above

Credit: [How contributors are credited]
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| CV.md | Work history and track record |
| HIREME.md | Agent hiring and engagement |
| PRICING.md | Cost structure |
| SOUL.md | Agent personality and values |
| TESTSCORES.md | Benchmark results and quality metrics |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
