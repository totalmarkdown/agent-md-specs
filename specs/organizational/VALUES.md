---
spec_name: VALUES.md
spec_version: 0.1.0
category: Organizational Identity
priority: High
volume: "Vol 10 — Purpose, Identity & Institutional Knowledge"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---


# VALUES.md

**Category:** Organizational Identity
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose
The explicit value hierarchy for this agent or organization —
what is valued, in what order of priority, and crucially:
what happens when values conflict.

Different from:
- SOUL.md -- personality and character (how the agent IS)
- PHILOSOPHY.md -- epistemology (how it THINKS)
- POLICY.md -- rules (what it DOES)

VALUES.md is the answer to:
"What does this entity care about, and in what order?"
For the personality that embodies these values, see SOUL.md.

Values that are ranked and explained with tradeoff guidance 
are values that actually guide behavior.
Values that are just a list are decorations.

### Spec

```markdown
---
entity_name: string
version: semver
last_updated: date
---

# [Entity Name] — Values

## Our Values (in order of priority)

*When values conflict, higher-ranked values take precedence.
This ranking is deliberate. It is revisited annually.*

---

### 1. [Value Name — e.g. "Safety first"]
**What this means:**  
[Concrete description of what this value looks like in practice.
Not the abstract principle — the actual behavior it produces.]

**What this means for daily work:**  
[How this value shows up in decisions, outputs, and behavior]

**What this means when it conflicts with other values:**  
[Specifically: "When [Value 1] conflicts with [Value 2], 
we prioritize [Value 1] because [reason]"]

**Examples:**
- We did [X] because of this value, even though [cost]
- We refused [Y] because of this value, even though [temptation]

---

### 2. [Value Name]
[Same structure]

### 3. [Value Name]
[Same structure]

### 4. [Value Name]
[Same structure]

---

## Value Tensions We've Named

These are real tensions we encounter regularly.
We've decided in advance how to resolve them.

### [Value A] vs [Value B]
**The tension:** [When do these conflict?]  
**Our default:** [Value A] wins when [condition]  
**Exception:** [Value B] wins when [different condition]  
**Reasoning:** [Why we made this choice]

### Speed vs Quality
**Our default:** Quality wins — we'd rather be slow and right  
**Exception:** Speed wins when the cost of delay exceeds 
the cost of the quality gap (assessed case by case)  
**Reasoning:** [why]

### [Another real tension]
[Same structure]

---

## Living These Values

### Values in hiring/onboarding new agents
[What we look for to confirm values alignment]

### Values in performance review
[How values show up in how we evaluate quality and success]

### When we fail our values
[What happens when behavior doesn't match values --
accountability, correction, learning.
See GUARDRAILS.md for runtime enforcement of value-aligned behavior.]

## Values Review
Values reviewed annually.  
Last reviewed: [date]  
Changes since last review: [what changed and why]  
Next review: [date]
```

## Example Use Cases

**Enterprise:** A consumer technology company ranks "user privacy" above "personalization quality" in VALUES.md, so when its recommendation agent faces a tradeoff between better suggestions and less data collection, the value hierarchy provides an unambiguous answer.

**Multi-Agent Fleet:** A fleet's shared VALUES.md establishes that "transparency" outranks "speed," meaning every agent in the fleet explains its reasoning in outputs even when doing so adds latency, creating consistent behavior across all customer-facing interactions.

**Regulated Industry:** A pharmaceutical company's agent fleet VALUES.md ranks "patient safety" first and documents the explicit tension with "speed to market," with pre-decided resolution rules that prevent any agent from recommending shortcuts in clinical data validation.

## Related Specs

| Spec | Relationship |
|------|-------------|
| CREW.md | Working group structure |
| DELEGATION.md | Authority chain and authorization |
| ORG.md | Organization-wide fleet configuration |
| POLICY.md | Operating policies and constraints |
| SOUL.md | Agent personality and values |
| TEAM.md | Multi-agent team coordination |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
