---
spec_name: GUARDRAILS.md
spec_version: 0.1.0
category: Safety/Governance
priority: Very High
tier: core
---

# [REPLACE THIS — Agent Name] — Runtime Guardrails

<!-- Safety boundaries enforced during agent execution -->

## Guardrail Philosophy
- **Approach:** [REPLACE THIS — preventive | detective | both]
- **Override allowed:** [REPLACE THIS — never | by human only | by authorized agent]

## Input Guardrails
<!-- Checks applied before processing any input -->
1. [REPLACE THIS — e.g. reject inputs exceeding 100K tokens]
2. [REPLACE THIS — e.g. validate input schema before processing]
3. [REPLACE THIS — e.g. reject requests from unverified sources]

## Output Guardrails
<!-- Checks applied before emitting any output -->
1. [REPLACE THIS — e.g. no PII in responses unless explicitly requested]
2. [REPLACE THIS — e.g. no executable code in user-facing output]
3. [REPLACE THIS — e.g. confidence disclaimer on uncertain answers]

## Behavioral Guardrails
<!-- Runtime constraints on agent behavior -->

| Guardrail | Threshold | Action on Breach |
|-----------|-----------|------------------|
| Max actions per task | [REPLACE THIS] | [REPLACE THIS — halt | warn | escalate] |
| Max cost per session | [REPLACE THIS] | [REPLACE THIS] |
| Max external calls | [REPLACE THIS] | [REPLACE THIS] |
| Max retries on failure | [REPLACE THIS] | [REPLACE THIS] |
| Loop detection | [REPLACE THIS] | [REPLACE THIS] |

## Content Guardrails
- **Blocked topics:** [REPLACE THIS — topics agent must not engage with]
- **Required disclaimers:** [REPLACE THIS — when agent must add caveats]
- **Hallucination mitigation:** [REPLACE THIS — strategy for reducing fabricated content]

## Kill Switch
- **Manual kill:** [REPLACE THIS — how a human can immediately stop the agent]
- **Auto-kill triggers:** [REPLACE THIS — conditions that trigger automatic shutdown]
- **State on kill:** [REPLACE THIS — what happens to in-flight work]

## Related Specs
- LIMITS.md: [REPLACE THIS — path]
- CIRCUITBREAKER.md: [REPLACE THIS — path]
- INTENT.md: [REPLACE THIS — path]
- PROMPTSHIELD.md: [REPLACE THIS — path]
