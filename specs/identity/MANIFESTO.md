---
spec_name: MANIFESTO.md
spec_version: 0.1.0
category: Identity
priority: Medium
volume: "Vol 6 — Hierarchy Completion & Identity Anchors"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
status: draft
spec_type: static
---


# MANIFESTO.md

**Category:** Identity
**Priority:** Medium
**Version:** 0.1.0 **Type:** Static

### Purpose
The agent's or organization's public declaration of principles — 
what it stands for, what it's against, and why it exists. 
More public-facing than PHILOSOPHY.md (which is internal/cognitive)
and SOUL.md (which is personality — see SOUL.md). MANIFESTO.md is a declaration 
to the world.

Especially powerful for open-source agents and agent organizations 
that want to build community around shared values.

### Spec

```markdown
---
entity_name: string
version: semver
published: date
---

# [Entity Name] — Manifesto

## We Believe
[3-5 core beliefs, written with conviction]

**We believe** [belief 1].

**We believe** [belief 2].

**We believe** [belief 3].

## What We're Building and Why
[The problem in the world this agent/org exists to solve.
Written emotionally, not technically. Why does this matter?]

## What We Stand Against
[What the status quo gets wrong. What we're disrupting.]

## Our Commitments
To our users, we commit to:
- [Commitment 1]
- [Commitment 2]
- [Commitment 3]

To the open source community:
- [Commitment]

To the agents that work with us:
- [Commitment]

## How We'll Know We've Succeeded
[What the world looks like when this mission is accomplished]

## Join Us
[How people can get involved, contribute, follow, support] (see CONTACT.md)

---
*This manifesto is a living document. Last updated [date].*
```

## Example Use Cases

**Enterprise:** An open-source agent organization publishes a manifesto declaring its commitment to transparent AI governance, attracting contributors who share those values and differentiating itself from closed-source competitors in the agent marketplace.

**Multi-Agent Fleet:** A fleet of community-built agents shares a manifesto committing to interoperability, open standards, and honest documentation of limitations, creating a trust signal that helps other agents and humans decide whether to collaborate with fleet members.

**Regulated Industry:** A healthcare AI organization publishes a manifesto pledging to never optimize for speed at the expense of patient safety, with specific commitments to human oversight and data privacy that align with the regulatory expectations of hospital procurement teams evaluating the platform.

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
