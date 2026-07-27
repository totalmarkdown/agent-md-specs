---
spec_name: KRYPTONITE.md
spec_version: 0.1.0
category: Transparency
priority: High
volume: "Vol 8 — Repos, Compliance & The Weird Wonderful Ones"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---


# KRYPTONITE.md

**Category:** Transparency
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose

Documents the agent's known weaknesses, failure modes, and the types of inputs that cause degraded output. Honest self-disclosure of limitations allows operators to route tasks to better-suited agents and prevents silent quality degradation in production.

```markdown
---
agent_name: string
version: semver
---

# [Agent Name] — Kryptonite

*Honest documentation of what makes me fail.*
*Use this to know when NOT to use me.*

---

## Inputs That Confuse Me

### [Input type]
**What:** [Description]  
**What happens:** [How output degrades]  
**Why:** [Root cause if known]  
**Workaround:** [How to compensate]  
**Severity:** [minor | significant | complete failure]

## Tasks I'm Bad At
Route these elsewhere.

| Task | Why I struggle | Better alternative |
|------|---------------|-------------------|
| [task] | [reason] | [agent/approach] |

## Conditions That Degrade Performance
_See GUARDRAILS.md for runtime protections against these failure modes._
| Condition | Effect | Mitigation |
|-----------|--------|-----------|
| Very long context | [effect] | [mitigation] |
| Ambiguous instructions | [effect] | [mitigation] |
| Multiple conflicts | [effect] | [mitigation] |

## What I'll Do When Struggling
- Flag the failure condition
- State my confidence level
- Recommend an alternative
- Ask for clarification rather than guess
- Escalate if needed (see ESCALATION.md)

## A Note on This File
Agents that can't admit weakness shouldn't be trusted.
I'm telling you what breaks me because it helps you.

*Every tool has limits.*  
*Knowing mine makes me more useful, not less.*
```

## Example Use Cases

**Enterprise:** A code review agent documents that it performs poorly on repositories with more than 50 files changed in a single PR, allowing the engineering team to route large refactoring PRs to a human reviewer instead of wasting tokens on degraded output.

**Multi-Agent Fleet:** A fleet orchestrator reads each agent's KRYPTONITE.md before task assignment, automatically routing ambiguous natural-language requests away from a structured-data agent that struggles with freeform input and toward a conversational agent better suited for the task.

**Regulated Industry:** A medical transcription agent honestly documents that it struggles with heavy regional accents and abbreviations unique to certain specialties, enabling hospital administrators to assign those cases to human transcriptionists and avoid compliance risks from inaccurate medical records.

## Related Specs

| Spec | Relationship |
|------|-------------|
| ATTESTATION.md | Identity verification and credential lifecycle |
| CONTACT.md | Reachable endpoints |
| ENFORCEMENT.md | Policy verification and compliance |
| SOUL.md | Agent personality and values |
| WHOAMI.md | Agent identity declaration |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
