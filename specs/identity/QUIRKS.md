---
spec_name: QUIRKS.md
spec_version: 0.1.0
category: Transparency
priority: High
volume: "Vol 8 — Repos, Compliance & The Weird Wonderful Ones"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---


# QUIRKS.md

**Category:** Transparency
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose

Documents the agent's distinctive behaviors -- both intentional design choices and known unintentional patterns. By surfacing these quirks proactively, users are not caught off guard by unexpected behavior and can distinguish features from bugs.

```markdown
---
agent_name: string
version: semver
---

# [Agent Name] — Quirks

*Things I do that might seem strange.*
*Documented so they don't catch you off guard.*

---

## [Quirk Name]
**What it looks like:** [Observable behavior]  
**When:** [Trigger or condition]  
**Why:** [Explanation — intentional or known issue]  
**Problem?** [No | Yes — workaround: [X] | Fixed in v[N]]

---

## Intentional Quirks (features)

### I [quirk]
Because [reason]. If you prefer [alternative]: [workaround].

## Unintentional Quirks (known bugs — see KRYPTONITE.md)

### I sometimes [behavior]
When [condition]. I know. Workaround: [if one exists].

## Endearing Quirks
Things users have come to appreciate:
- [Quirk users mention positively]

## Report New Quirks
[github issue | discord | feedback form] (see CONTACT.md)

I want to know. Either I'll explain it,
or I'll document it as a known issue.
```

## Example Use Cases

**Enterprise:** A report generation agent documents an intentional quirk — it always adds a confidence disclaimer footer to outputs, even when confidence is 99% — so users understand this is by design and not a sign of uncertainty, reducing unnecessary support tickets.

**Multi-Agent Fleet:** A fleet operator reviews quirks across all agents and discovers that three agents share the same unintentional quirk of repeating the task summary at the end of every output, identifying a common prompt template issue that can be fixed fleet-wide.

**Regulated Industry:** A clinical documentation agent documents a quirk where it occasionally rephrases medical terminology into plain language mid-sentence, flagging it as a known behavior so clinicians are aware and can verify that the original medical terms are preserved in the structured data fields.

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
