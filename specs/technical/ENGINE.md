---
spec_name: ENGINE.md
spec_version: 0.1.0
category: Technical
domain: enginemd.dev
priority: Medium
volume: "Vol 8 — Technical"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---


# ENGINE.md

**Category:** Technical
**Domain:** enginemd.dev
**Priority:** Medium
**Version:** 0.1.0 **Type:** Static

### Purpose
Runtime execution configuration for the LLM engine powering an agent —
model selection, inference parameters, retry policies, concurrency
controls, and resource limits. Different from MODEL.md (which model
and its capabilities) — ENGINE.md defines *how* the model is invoked
at runtime: temperature, token budgets, fallback chains, batching,
and cost guardrails. Connects to BUDGET.md for spending limits,
LIMITS.md for hard constraints, and MONITOR.md for observability
of engine performance.

### When to create
Any agent that calls an LLM at runtime. Especially important for
production agents where inference cost, latency, and reliability
directly impact SLAs. Required when agents use fallback chains,
multi-model routing, or cost-constrained execution.

### Spec

```markdown
---
agent_name: string
version: semver
model_provider: string           # anthropic | openai | google | ollama | custom
model_name: string               # claude-sonnet-4-6 | gpt-4o | gemini-2.0-flash
model_version: string            # Pinned version string
fallback_model: string           # Model to use if primary is unavailable
temperature: number              # 0.0–2.0
top_p: number                    # 0.0–1.0
max_tokens: number               # Max output tokens per call
chain_of_thought_strategy: string  # react | reflection | plan-and-execute | none
tool_calling_pattern: string     # parallel | sequential | adaptive
context_window_strategy: string  # truncate_oldest | summarize | sliding_window
context_budget: number           # Max tokens reserved for context
streaming: boolean               # true | false
timeout_seconds: number
created: date
updated: date
---

# [Agent Name] — Engine Configuration

## Primary Model
- **Provider:** [provider name]
- **Model:** [model name and version]
- **Context window:** [N] tokens
- **Max output tokens:** [N]
- **Streaming:** [enabled/disabled]

## Inference Parameters
| Parameter | Value | Notes |
|-----------|-------|-------|
| temperature | [0.0–2.0] | Lower for deterministic, higher for creative |
| top_p | [0.0–1.0] | Nucleus sampling threshold |
| max_tokens | [N] | Hard cap on output length |
| stop_sequences | [list] | Sequences that halt generation |
| frequency_penalty | [0.0–2.0] | Reduce repetition (if supported) |
| presence_penalty | [0.0–2.0] | Encourage topic diversity (if supported) |

## Chain-of-Thought Strategy
- **Strategy:** [react | reflection | plan-and-execute | none]
- **Reasoning visibility:** [hidden | visible | logged_only]
- **Max reasoning tokens:** [N] (if applicable)

## Tool Calling Configuration
- **Pattern:** [parallel | sequential | adaptive]
- **Max tool calls per turn:** [N]
- **Tool call timeout:** [N] seconds
- See TOOLS.md for full tool inventory and permissions.

## Context Window Management
- **Strategy:** [truncate_oldest | summarize | sliding_window]
- **Context budget:** [N] tokens reserved for context
- **System prompt budget:** [N] tokens reserved for system prompt
- **Conversation history:** Keep last [N] turns or [N] tokens
- **Summarization trigger:** When context exceeds [N]% of window

## Fallback Chain
| Priority | Model | Provider | Trigger |
|----------|-------|----------|---------|
| Primary | [model] | [provider] | Default |
| Fallback 1 | [model] | [provider] | Primary timeout or error |
| Fallback 2 | [model] | [provider] | All above unavailable |
| Emergency | [model] | [provider] | All above unavailable |

## Retry Policy
- **Max retries:** [N]
- **Backoff strategy:** [exponential | linear | fixed]
- **Initial delay:** [N] seconds
- **Max delay:** [N] seconds
- **Retry on:** [rate_limit | timeout | server_error]
- **Do not retry on:** [auth_error | invalid_request | content_filter]
- **Fallback chain:** After [N] retries, switch to fallback model

## Batch Configuration
- **Max concurrent requests:** [N]
- **Queue strategy:** [fifo | priority | round_robin]
- **Queue max depth:** [N]
- **Batch window:** [N] seconds (group requests within window)

## Timeout Configuration
- **Per-request timeout:** [N] seconds
- **Per-task timeout:** [N] seconds (across multiple LLM calls)
- **Streaming first-token timeout:** [N] seconds
- **On timeout:** [retry | fallback | escalate]

## Resource Limits
- **Max cost per session:** $[amount] (see BUDGET.md)
- **Max tokens per hour:** [N] tokens
- **Max requests per minute:** [N]
- **Daily cost ceiling:** $[amount]
- **On limit reached:** [queue | reject | fallback_to_cheaper | escalate]

_See BUDGET.md for spending controls, LIMITS.md for hard constraints,
and MONITOR.md for engine performance observability._
```

## Example Use Cases

**Enterprise:** A financial analysis firm configures ENGINE.md for its portfolio-review agent with temperature 0.1 for deterministic outputs, a three-model fallback chain (Claude Sonnet primary, GPT-4o fallback, Gemini emergency), exponential retry backoff, and a $50/session cost ceiling that automatically switches to cheaper models when 80% of the budget is consumed.

**Multi-Agent Fleet:** A platform team standardizes ENGINE.md across 60 agents, using adaptive tool-calling patterns for complex orchestration agents and sequential patterns for compliance-checking agents, with fleet-wide concurrency limits that prevent any single agent from consuming more than 20% of the shared API rate limit during peak hours.

**Regulated Industry:** A pharmaceutical company's clinical-trial analysis agent uses ENGINE.md to enforce deterministic inference (temperature 0, fixed seed), pin exact model versions for reproducibility, disable streaming to ensure complete audit trails, and cap context windows to prevent PHI from leaking into summarization — all requirements from their FDA 21 CFR Part 11 compliance program. See SOP.md for the associated standard operating procedures.

## Related Specs

| Spec | Relationship |
|------|-------------|
| [BUDGET.md](../governance/BUDGET.md) | Spending controls and cost thresholds |
| [HEALTHCHECK.md](../operations/HEALTHCHECK.md) | Liveness and readiness checks for engine |
| [LIMITS.md](../governance/LIMITS.md) | Hard constraints and safety boundaries |
| [MODEL.md](MODEL.md) | Underlying AI model identity and capabilities |
| [MONITOR.md](../operations/MONITOR.md) | Observability and engine performance metrics |
| [PERMISSIONS.md](../governance/PERMISSIONS.md) | Resource access control for engine operations |
| [SOP.md](../process/SOP.md) | Standard operating procedures for engine changes |
| [TOOLS.md](TOOLS.md) | Tool inventory configured via engine |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
