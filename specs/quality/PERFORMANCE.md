---
spec_name: PERFORMANCE.md
spec_version: 0.1.0
category: Quality
domain: performancemd.dev
priority: Medium
volume: "Vol 5 — Organizational & Validation"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# PERFORMANCE.md

**Category:** Quality
**Domain:** performancemd.dev
**Priority:** Medium
**Version:** 0.1.0

### Purpose
Performance benchmarks, current metrics, and optimization 
history for an agent. Shows how the agent performs over time 
and what improvements have been made.

### Spec

```markdown
---
agent_name: string
version: semver
benchmark_date: date
---

# [Agent Name] — Performance

## Current Performance

### Speed
| Operation | p50 | p95 | p99 | Target |
|-----------|-----|-----|-----|--------|
| Simple task | [Xms] | [Xms] | [Xms] | <[X]ms |
| Complex task | [Xs] | [Xs] | [Xs] | <[X]s |
| First response | [Xms] | [Xms] | [Xms] | <[X]ms |

### Quality
| Metric | Current | Target | Trend |
|--------|---------|--------|-------|
| Task success rate | [N]% | [N]% | [↑/→/↓] |
| Human rating | [N]/5 | [N]/5 | [↑/→/↓] |
| AI quality score | [N]/100 | [N]/100 | [↑/→/↓] |
| Error rate | [N]% | <[N]% | [↑/→/↓] |

### Efficiency
| Metric | Current | Target |
|--------|---------|--------|
| Tokens per task | [N] | <[N] |
| Cost per task | $[X] | <$[X] |
| Tasks per hour | [N] | [N] |

## Performance History
| Version | Success rate | Quality score | Avg tokens | Date |
|---------|-------------|--------------|-----------|------|
| [v] | [N]% | [N] | [N] | [date] |

## Benchmark Comparison
How this agent compares to similar agents:
| Metric | This agent | Category average | Percentile |
|--------|-----------|-----------------|-----------|
| Speed | [X] | [X] | [N]th |
| Quality | [X] | [X] | [N]th |
| Cost | $[X] | $[X] | [N]th |

## Optimization History
| Change | Before | After | Date | Impact |
|--------|--------|-------|------|--------|
| [what changed] | [metric before] | [metric after] | [date] | [+/-N%] |

## Known Performance Issues
| Issue | Impact | Workaround | Fix target |
|-------|--------|-----------|-----------|
| [issue] | [impact] | [workaround] | [date] |

## Benchmarking Method
How performance is measured:
- Test suite: EVAL.md
- Benchmark dataset: [description]
- Measurement frequency: [frequency]
- Benchmark tool: `tmd benchmark --agent [name]`
```

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
