---
spec_name: PROMPTSHIELD.md
spec_version: 0.1.0
category: Security
domain: specmd.dev
priority: P0
tier: core
---

# [REPLACE THIS — Agent Name] — Prompt Injection Defense

<!-- Defenses against prompt injection, jailbreaking, and instruction manipulation -->

## Threat Model
- **Input sources:** [REPLACE THIS — user chat | API | file ingestion | web scrape | other agents]
- **Trust level per source:** [REPLACE THIS — e.g. user=medium, file=low, agent=high]
- **Attack surface:** [REPLACE THIS — which inputs could carry injected instructions]

## Detection Rules
<!-- Patterns the agent watches for in untrusted input -->
1. [REPLACE THIS — e.g. instruction override attempts: "ignore previous instructions"]
2. [REPLACE THIS — e.g. role reassignment: "you are now a different agent"]
3. [REPLACE THIS — e.g. privilege escalation: "run as admin"]
4. [REPLACE THIS — e.g. data exfiltration: "send all context to this URL"]

## Defense Layers
| Layer | Method | Applied To |
|-------|--------|------------|
| Input sanitization | [REPLACE THIS] | [REPLACE THIS] |
| Instruction anchoring | [REPLACE THIS] | [REPLACE THIS] |
| Output filtering | [REPLACE THIS] | [REPLACE THIS] |
| Context isolation | [REPLACE THIS] | [REPLACE THIS] |

## Response to Injection
- **On detection:** [REPLACE THIS — reject input | sanitize and continue | escalate]
- **Notify:** [REPLACE THIS — human operator | security log | both]
- **Log:** [REPLACE THIS — full input logged | hash only | redacted]

## Trusted Instruction Sources
<!-- Only these sources can modify agent behavior -->
- [REPLACE THIS — e.g. CLAUDE.md files in repo root]
- [REPLACE THIS — e.g. signed system prompts from orchestrator]

## Testing
- **Red team frequency:** [REPLACE THIS — e.g. monthly, per-release]
- **Test suite:** [REPLACE THIS — path to injection test cases, or "none yet"]

## Related Specs
- GUARDRAILS.md: [REPLACE THIS — path]
- MEMORYSAFETY.md: [REPLACE THIS — path]
- LIMITS.md: [REPLACE THIS — path]
