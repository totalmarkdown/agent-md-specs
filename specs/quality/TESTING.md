---
spec_name: TESTING.md
spec_version: 0.1.0
category: Quality
domain: testingmd.dev
priority: High
volume: "Vol 2 — Extended Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# TESTING.md

**Category:** Quality
**Domain:** testingmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Documents the test suite for an agent — what tests exist, 
how to run them, what constitutes a passing state, and 
how to add new tests.

### Spec

````markdown
---
agent_name: string
version: semver
test_framework: string   # vitest | jest | pytest | custom
minimum_pass_rate: number  # e.g. 0.95 for 95%
created: date
updated: date
---

# [Agent Name] — Test Suite

## Test Categories

### Unit tests (fast, no external calls)
Location: [path]
Run: [command]
What they test: individual functions, parsers, validators

### Integration tests (use real MCP/API connections)
Location: [path]  
Run: [command]
Prerequisites: [required env vars, running services]
What they test: end-to-end workflows with real dependencies

### Eval tests (measure output quality)
Location: EVAL.md (see EVAL.md for evaluation dimensions and benchmarks)
Run: tmd eval --agent [name]
What they test: trigger accuracy, output quality, safety

### Regression tests
Location: [path]
Run: [command]
What they test: bugs that were fixed and must not recur

## Running All Tests
```bash
# Full test suite (run before any deployment)
[command to run all tests]

# Quick smoke test (run after deployment)
[command for fast subset]

# Eval only (weekly or after config changes)
tmd eval --agent [name] --full
```

## Passing Criteria
Before merge to main:
- [ ] Unit tests: 100% pass
- [ ] Integration tests: [X]% pass
- [ ] Eval tests: [X]% pass
- [ ] No new P1 security findings (see ENFORCEMENT.md)
- [ ] Performance: no regression > [X]% in key metrics

## Test Data
- Test fixtures: [location]
- Test database: [how to set up]
- Mock external services: [which are mocked vs real]
- PII in tests: [none | anonymized | synthetic only]

## Adding Tests
When adding a new capability or fixing a bug:
1. Write test that fails (red)
2. Implement fix/feature
3. Verify test passes (green)
4. Add to regression suite if it was a bug fix
5. Update EVAL.md with new eval cases if capability changes
````

## Example Use Cases

**Enterprise:** A fintech startup requires all agent PRs to pass TESTING.md's full suite in CI before merge, catching a regression where the tax calculation agent mishandled negative amounts.

**Multi-Agent Fleet:** A DevOps team runs TESTING.md smoke tests automatically after every fleet deployment, confirming all 30 agents are healthy within 5 minutes of rollout.

**Regulated Industry:** A medical device company references TESTING.md's regression test suite in their FDA 510(k) submission to demonstrate systematic validation of their diagnostic support agent.

## Related Specs

| Spec | Relationship |
|------|-------------|
| CV.md | Work history and track record |
| ENFORCEMENT.md | Policy verification and compliance |
| EVAL.md | Evaluation methodology |
| TESTSCORES.md | Benchmark results and quality metrics |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
