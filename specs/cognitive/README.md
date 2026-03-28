# Cognitive Specs

How agents think, remember, and reason. These specs define the internal mental model of an agent -- its knowledge, beliefs, learning patterns, and reflective processes. They are what separate a stateless tool from a persistent, evolving intelligence.

## How These Specs Work Together

MEMORY is the foundational core spec -- without persistent memory, nothing else in this category functions meaningfully. EXPERTISE and TRAINING build on memory by defining what the agent knows and how it acquires new knowledge through in-context learning. BELIEFS and PHILOSOPHY shape how the agent interprets information and approaches problems. LEARNING, JOURNAL, and CONFESSION form a reflective loop where the agent tracks its growth, records observations, and honestly acknowledges mistakes. INSTINCT captures the fast heuristics that emerge from all of the above.

## Specs in This Category

| Spec | Tier | Purpose | Scope |
|------|------|---------|-------|
| [BELIEFS.md](BELIEFS.md) | Extended | Core assumptions the agent holds about its domain and work | Domain reasoning foundations |
| [CONFESSION.md](CONFESSION.md) | Extended | Honest acknowledgment of mistakes and what was learned | Error tracking and growth |
| [EXPERTISE.md](EXPERTISE.md) | Extended | Maps knowledge depth by topic for intelligent task routing | Skill and knowledge inventory |
| [INSTINCT.md](INSTINCT.md) | Extended | Fast heuristics and reflexes applied without deliberation | Automated reasoning patterns |
| [JOURNAL.md](JOURNAL.md) | Extended | Running log of reflections, observations, and surprises | Ongoing agent introspection |
| [LEARNING.md](LEARNING.md) | Extended | Active knowledge gaps being filled and skills being developed | Growth and upskilling |
| [MEMORY.md](MEMORY.md) | Core | Persistent memory across sessions and conversations | Long-term state retention |
| [PHILOSOPHY.md](PHILOSOPHY.md) | Extended | Underlying approach to problems, uncertainty, and ethics | Reasoning methodology |
| [TRAINING.md](TRAINING.md) | Extended | Few-shot examples and reference patterns for better outputs | In-context learning |

## When to Use These Specs

- **Building a stateful agent:** Start with MEMORY to give your agent persistence across sessions, then add EXPERTISE to define its knowledge boundaries.
- **Improving output quality:** Use TRAINING for few-shot examples and BELIEFS to anchor the agent's reasoning in domain-specific assumptions.
- **Creating a self-improving agent:** Combine LEARNING, JOURNAL, and CONFESSION to build a reflective loop that tracks growth over time.

## Related Categories

| Category | How It Relates |
|----------|---------------|
| [coordination/](../coordination/) | SHAREDCONTEXT extends cognitive concepts to multi-agent memory |
| [technical/](../technical/) | PROMPTS and MODEL define the technical substrate for cognition |
| [quality/](../quality/) | EVAL and FEEDBACK measure how well cognitive processes perform |

---
*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)
· [Full Index](../../INDEX.md) · [README](../../README.md)*
