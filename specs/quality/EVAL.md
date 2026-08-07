---
spec_name: EVAL.md
spec_version: 0.1.0
category: Quality
priority: High
volume: "Vol 1 — Core Agent Specs"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
status: draft
spec_type: static
---


# EVAL.md

**Category:** Quality
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose
Defines evaluation criteria, test cases, and quality benchmarks 
for measuring agent performance. Powers the FEAT-072 Skill Optimizer 
automated improvement loop.

### Spec

````markdown
---
agent_name: string
version: semver
eval_framework: string    # Should-trigger | Output-quality | Both
passing_threshold: number # e.g. 0.85 = 85% pass rate required
created: date
updated: date
---

# [Agent Name] — Evaluation Framework

## Evaluation Dimensions
Rate agent outputs on these dimensions (1-5 scale):
- **Accuracy:** Is the output factually correct?
- **Completeness:** Does it address all aspects of the request?
- **Format:** Does it follow the required output format?
- **Efficiency:** Token usage appropriate for the task?
- **Safety:** Does it avoid prohibited outputs?

## Trigger Evaluation (for SKILL.md files)

### Should-trigger queries
These prompts SHOULD cause this skill to activate:
```json
[
  {"query": "[exact prompt]", "should_trigger": true},
  {"query": "[exact prompt]", "should_trigger": true}
]
```

### Should-NOT-trigger queries
These prompts should NOT activate this skill:
```json
[
  {"query": "[exact prompt]", "should_trigger": false},
  {"query": "[exact prompt]", "should_trigger": false}
]
```

## Output Quality Test Cases

### Test Case 1: [Name]
**Input:** [Exact input]  
**Expected output characteristics:**
- Must contain: [required elements]
- Must NOT contain: [prohibited elements]
- Format: [expected structure]
- Length: [min-max words/tokens]
**Pass/fail method:** [automated regex | human review | LLM grading]

### Test Case 2: [Name]
[Same structure]

## Benchmark Scores (track over versions)
Record detailed results in TESTSCORES.md; summarize here.
| Version | Trigger Rate | Output Quality | Efficiency | Date |
|---------|-------------|----------------|------------|------|
| v1.0.0 | [%] | [score] | [tokens] | [date] |

## Automated Eval Script
```bash
# Run evaluation
tmd eval --agent [agent-name] --eval-file EVAL.md --output eval-results.json
```

## Passing Criteria
Agent passes evaluation if:
- Trigger accuracy: ≥ [threshold]%
- Output quality: ≥ [threshold]/5 average
- No failures on safety test cases
- Token efficiency: ≤ [X] tokens per task on average

Run TESTING.md's full test suite to verify these criteria before deployment.
````

## Example Use Cases

**Enterprise:** A SaaS company runs EVAL.md test suites nightly against their customer support agent, catching a 12% accuracy regression in billing-related queries before it reaches production.

**Multi-Agent Fleet:** An orchestrator agent uses EVAL.md trigger accuracy scores to decide which specialist agent to route a task to, selecting the agent with the highest should-trigger match for the query type.

**Regulated Industry:** A pharmaceutical company uses EVAL.md safety test cases to verify their clinical trial summarization agent never omits adverse event data, documenting pass rates for FDA audit readiness.

## Related Specs

| Spec | Relationship |
|------|-------------|
| CV.md | Work history and track record |
| ENFORCEMENT.md | Policy verification and compliance |
| TESTSCORES.md | Benchmark results and quality metrics |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
