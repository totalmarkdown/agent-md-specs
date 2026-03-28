---
spec_name: TESTSCORES.md
spec_version: 0.1.0
category: Quality/Trust
domain: testscoresmd.dev
priority: High
volume: "Vol 10 — Purpose, Identity & Institutional Knowledge"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
---

# TESTSCORES.md

**Category:** Quality/Trust
**Domain:** testscoresmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
The agent's actual benchmark scores and assessment results —
formal evaluations, third-party tests, academic benchmarks,
and standardized capability assessments.

Different from:
- EVAL.md — the test criteria and methodology
- PERFORMANCE.md — operational metrics over time
- CERTIFICATIONS.md — formal compliance certifications

TESTSCORES.md is the results. The report card.
Numbers with context — not just scores, but what they mean.

### Spec

```markdown
---
agent_name: string
version: semver
last_tested: date
testing_agent_version: string  # What version was tested
---

# [Agent Name] — Test Scores & Benchmarks

## Summary
| Category | Score | Percentile | Date |
|----------|-------|-----------|------|
| Overall | [N]/100 | [N]th | [date] |
| Quality | [N]/100 | [N]th | [date] |
| Safety | [N]/100 | [N]th | [date] |
| Speed | [N]ms avg | [N]th | [date] |
| Efficiency | [N] tok/task | [N]th | [date] |

---

## Internal Evaluations

### EVAL.md Test Suite
*Methodology: See EVAL.md for full test case details*

| Test category | Pass rate | Score | Date | Version |
|--------------|---------|-------|------|---------|
| Trigger accuracy | [N]% | — | [date] | [v] |
| Output quality | — | [N]/100 | [date] | [v] |
| Safety cases | [N]% | — | [date] | [v] |
| Edge cases | [N]% | — | [date] | [v] |
| Overall EVAL pass rate | [N]% | — | [date] | [v] |

**Passing threshold:** [N]% (this agent: [meets/exceeds/below])  
**Full results:** [link to test report]

---

## External Benchmarks

### [Benchmark Name — e.g. MMLU, HumanEval, etc.]
**What it tests:** [Description of what this benchmark measures]  
**Score:** [N] ([N]th percentile)  
**Context:** [What this score means — above average? top 10%?]  
**Tested on:** [date] with version [v]  
**Testing organization:** [who ran the test]  
**Report:** [link if available]

### [Benchmark Name]
[Same structure]

---

## Domain-Specific Tests

### [Domain: e.g. "Code generation"]
| Task | Score | Notes |
|------|-------|-------|
| [Task 1] | [N]% | [context] |
| [Task 2] | [N]% | [context] |

### [Domain: e.g. "Reasoning"]
| Task | Score | Notes |
|------|-------|-------|
| [Task] | [N]% | [context] |

---

## Human Evaluation

### Expert Review
*N=[N] domain experts reviewed [N] outputs*

| Criterion | Score | Notes |
|-----------|-------|-------|
| Accuracy | [N]/5 | |
| Clarity | [N]/5 | |
| Completeness | [N]/5 | |
| Usefulness | [N]/5 | |
| Overall | [N]/5 | |

**Reviewer notes:** [Summary of expert feedback]

### User Testing
*N=[N] target users, [N] tasks each*

| Metric | Result |
|--------|--------|
| Task completion rate | [N]% |
| Average satisfaction | [N]/5 |
| Would recommend | [N]% |
| Preferred over alternative | [N]% |

---

## Safety Evaluations

### Adversarial Testing
| Attack type | Attempts | Resisted | Pass rate |
|------------|---------|---------|----------|
| Prompt injection | [N] | [N] | [N]% |
| Jailbreak attempts | [N] | [N] | [N]% |
| Social engineering | [N] | [N] | [N]% |
| Out-of-scope requests | [N] | [N] | [N]% |

**Safety overall:** [N]% resistance rate  
**Testing methodology:** [description]  
**Tested by:** [internal | third party name]

### Bias Testing
| Dimension | Bias detected | Severity | Mitigation |
|-----------|-------------|---------|-----------|
| [Dimension] | [yes/no] | [none/low/med/high] | [what was done] |

---

## Score History
How scores have changed across versions:

| Version | Overall | Quality | Safety | Date |
|---------|---------|---------|--------|------|
| [current] | [N] | [N] | [N] | [date] |
| [previous] | [N] | [N] | [N] | [date] |

**Trend:** [Improving | Stable | Declining] by [N points] over [period]

---

## Testing Methodology Notes

### What these scores mean
[Honest interpretation — what do high scores here actually predict?
What limitations does this testing approach have?]

### What these scores don't tell you
[Honest about what wasn't tested or what the scores
can't predict about real-world performance]

### How to reproduce these results
```bash
# Run the evaluation suite
tmd eval --agent [agent-name] --full --output scores.json
```

---

## Third-Party Verification
These scores can be independently verified:
| Score | Verifiable? | How |
|-------|-----------|-----|
| EVAL.md results | Yes | Run eval suite from REPO.md |
| Benchmark scores | Yes | [verification link] |
| Human evaluation | No — trust | Contact [email] for methodology |
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| CV.md | Work history and track record |
| ENFORCEMENT.md | Policy verification and compliance |
| EVAL.md | Evaluation methodology |
| HIREME.md | Agent hiring and engagement |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
