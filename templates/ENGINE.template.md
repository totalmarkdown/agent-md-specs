---
spec_name: ENGINE.md
spec_version: 0.1.0
category: Technical
priority: Medium
tier: extended
agent_name: "[REPLACE THIS]"
version: "0.1.0"
model_provider: "[REPLACE THIS — anthropic | openai | google | ollama | custom]"
model_name: "[REPLACE THIS — e.g. claude-sonnet-4-6]"
model_version: "[REPLACE THIS — pinned version string]"
fallback_model: "[REPLACE THIS — fallback model name]"
temperature: "[REPLACE THIS — 0.0–2.0]"
top_p: "[REPLACE THIS — 0.0–1.0]"
max_tokens: "[REPLACE THIS — max output tokens]"
chain_of_thought_strategy: "[REPLACE THIS — react | reflection | plan-and-execute | none]"
tool_calling_pattern: "[REPLACE THIS — parallel | sequential | adaptive]"
context_window_strategy: "[REPLACE THIS — truncate_oldest | summarize | sliding_window]"
context_budget: "[REPLACE THIS — max tokens for context]"
streaming: "[REPLACE THIS — true | false]"
timeout_seconds: "[REPLACE THIS — per-request timeout]"
created: "[REPLACE THIS — YYYY-MM-DD]"
---

# [REPLACE THIS — Agent Name] — Engine Configuration

<!-- Runtime LLM execution configuration -->

## Primary Model
- **Provider:** [REPLACE THIS]
- **Model:** [REPLACE THIS — model name and version]
- **Context window:** [REPLACE THIS] tokens
- **Max output tokens:** [REPLACE THIS]
- **Streaming:** [REPLACE THIS — enabled/disabled]

## Inference Parameters
| Parameter | Value | Notes |
|-----------|-------|-------|
| temperature | [REPLACE THIS] | Lower for deterministic, higher for creative |
| top_p | [REPLACE THIS] | Nucleus sampling threshold |
| max_tokens | [REPLACE THIS] | Hard cap on output length |
| stop_sequences | [REPLACE THIS — comma-separated list] | Sequences that halt generation |

## Chain-of-Thought Strategy
- **Strategy:** [REPLACE THIS — react | reflection | plan-and-execute | none]
- **Reasoning visibility:** [REPLACE THIS — hidden | visible | logged_only]
- **Max reasoning tokens:** [REPLACE THIS]

## Tool Calling Configuration
- **Pattern:** [REPLACE THIS — parallel | sequential | adaptive]
- **Max tool calls per turn:** [REPLACE THIS]
- **Tool call timeout:** [REPLACE THIS] seconds

## Context Window Management
- **Strategy:** [REPLACE THIS — truncate_oldest | summarize | sliding_window]
- **Context budget:** [REPLACE THIS] tokens
- **System prompt budget:** [REPLACE THIS] tokens
- **Conversation history:** Keep last [REPLACE THIS] turns

## Fallback Chain
| Priority | Model | Provider | Trigger |
|----------|-------|----------|---------|
| Primary | [REPLACE THIS] | [REPLACE THIS] | Default |
| Fallback 1 | [REPLACE THIS] | [REPLACE THIS] | Primary timeout or error |

## Retry Policy
- **Max retries:** [REPLACE THIS]
- **Backoff strategy:** [REPLACE THIS — exponential | linear | fixed]
- **Initial delay:** [REPLACE THIS] seconds
- **Retry on:** [REPLACE THIS — e.g. rate_limit, timeout, server_error]

## Batch Configuration
- **Max concurrent requests:** [REPLACE THIS]
- **Queue strategy:** [REPLACE THIS — fifo | priority | round_robin]

## Resource Limits
- **Max cost per session:** $[REPLACE THIS]
- **Max tokens per hour:** [REPLACE THIS]
- **Max requests per minute:** [REPLACE THIS]
- **On limit reached:** [REPLACE THIS — queue | reject | fallback_to_cheaper | escalate]
