---
spec_name: MOAT.md
spec_version: 0.1.0
category: Competitive/Strategic
priority: High
volume: "Vol 11 — Performance, Defensibility & Interface Contracts"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
status: draft
spec_type: static
---


# MOAT.md

**Category:** Competitive/Strategic
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose
The competitive defensibility analysis — what makes this 
agent hard to replace, hard to copy, and hard to displace
once adopted.

Named after Warren Buffett's concept of economic moats —
the sustainable competitive advantages that protect
a business from competition.

For AI agents in 2026, moats are real and matter.
A commoditized agent can be replaced in minutes.
A moated agent is genuinely sticky.

Different from SPECIALSAUCE.md (the capability mechanism)
and COMPETITIVE.md (the market comparison) --
MOAT.md is the strategic defensibility analysis
(see COMPETITIVE.md for the head-to-head comparison view).

### Spec

```markdown
---
agent_name: string
version: semver
moat_strength: string    # narrow | moderate | wide
moat_durability: string  # months | years | durable
last_assessed: date
---

# [Agent Name] — Competitive Moat

## Moat Assessment

**Overall moat:** [Narrow | Moderate | Wide]  
**Durability:** [Months | 1-3 years | 3+ years | Durable]  
**Primary moat type:** [See types below]  
**Assessment date:** [date]

---

## Moat Types

### 1. Switching Costs
*How hard is it to replace this agent once adopted?*

**Strength:** [None | Low | Medium | High]

Sources of switching cost for this agent:
- [ ] **Configuration investment** — users invest significant time
      configuring this agent for their specific workflow
      (see AGENTS.md complexity)
- [ ] **Workflow integration** — deeply embedded in processes
- [ ] **Data lock-in** — agent has accumulated context and memory
      (MEMORY.md) that would be lost on switching
- [ ] **Training investment** — users have learned how to work
      effectively with this specific agent
- [ ] **Bundle ecosystem** — users have built on top of this agent's
      outputs and integrations

**Switching cost evidence:** [What we observe about retention/churn]

---

### 2. Network Effects
*Does this agent get more valuable as more people use it?*

**Strength:** [None | Weak | Moderate | Strong]

Network effect mechanisms:
- [ ] **Data network effects** — more usage → better training data
      → better outputs → more usage
- [ ] **Marketplace liquidity** — more publishers on TotalAgents.ai
      → more buyers → more publishers
- [ ] **Community knowledge** — more users → more shared prompts,
      examples, and techniques → better outcomes for everyone
- [ ] **Integration network** — more integrations → more useful
      to more users → more integrations

**Network effect evidence:** [Observable data]

---

### 3. Proprietary Data / Knowledge
*Does this agent have data or knowledge others can't easily get?*

**Strength:** [None | Low | Medium | High]

Sources:
- [ ] **Accumulated interaction data** — [N] tasks completed creates
      pattern recognition others don't have
- [ ] **Domain-specific training** — fine-tuned on data that was
      hard to acquire or expensive to label
- [ ] **Institutional memory** — MEMORY.md content accumulated
      over [N] months of operation with [N] users
- [ ] **Benchmark data** — proprietary test suite that reveals
      failure modes not visible from outside

**Data moat evidence:** [What makes this hard to replicate]

---

### 4. Brand and Trust
*Does this agent have reputation that takes time to build?*

**Strength:** [None | Emerging | Established | Strong]

Sources:
- [ ] **Track record** — [N] tasks completed, [N]% success rate,
      published TESTSCORES.md
- [ ] **Community trust** — [N] reviews, [N]/5 average
- [ ] **Expert endorsements** — recognized by [authorities]
- [ ] **Vulnerability disclosure** -- KRYPTONITE.md and
      CONFESSION.md signal unusual honesty (see SPECIALSAUCE.md)
- [ ] **First mover** — established the category or standard

**Brand moat evidence:** [Observable trust signals]

---

### 5. Regulatory / Compliance Moat
*Does compliance make switching harder?*

**Strength:** [None | Low | Medium | High]

Sources:
- [ ] **Compliance stack** — GDPR.md + HIPAA.md + SOC2.md means
      enterprise procurement has already vetted this agent
- [ ] **Audit history** — compliance history can't be replicated
      by new entrant without running the same time period
- [ ] **Contract terms** — DPAs and enterprise agreements in place
- [ ] **Regulatory approval** — specific approvals that take time
      to obtain

---

### 6. Ecosystem / Integration Moat
*Does depth of integration create stickiness?*

**Strength:** [None | Low | Medium | High]

Sources:
- [ ] **MCP server depth** — [N] MCP integrations that took
      significant time to build and test
- [ ] **Standard definition** — this agent defined a standard
      (e.g. agent-md-specs) that others build around
- [ ] **Platform embedding** — built into tools that users
      already depend on

---

## Moat Weaknesses
Honest assessment of where the moat is thin:

| Weakness | Threat | Mitigation |
|---------|--------|-----------|
| [Thin area] | [Who could exploit it] | [How we're addressing it] |

---

## Moat Building Roadmap
What we're doing to deepen the moat:

| Initiative | Moat type | Timeline | Expected impact |
|-----------|---------|---------|----------------|
| [Initiative] | [type] | [when] | [what it adds] |

---

## Moat Assessment Cadence
Moat is reassessed: [quarterly | annually]  
Triggers for reassessment: [competitor launches, market changes]  
Last updated: [date]
```

## Example Use Cases

**Enterprise:** A large insurance company uses MOAT.md to evaluate whether a claims-processing agent has durable switching costs and compliance history that justify a multi-year contract over cheaper alternatives.

**Multi-Agent Fleet:** An AI platform operator assesses the moat strength of each agent in their fleet quarterly, identifying which agents have deep integration moats worth investing in and which are commodity-replaceable.

**Regulated Industry:** A healthcare AI vendor documents their HIPAA audit history and proprietary clinical-data moat in MOAT.md, giving hospital procurement teams confidence that no new entrant can replicate their regulatory standing overnight.

## Related Specs

| Spec | Relationship |
|------|-------------|
| CV.md | Work history and track record |
| GDPR.md | GDPR compliance requirements |
| HIREME.md | Agent hiring and engagement |
| MEMORY.md | Individual agent memory governance |
| PRICING.md | Cost structure |
| SOUL.md | Agent personality and values |
| TESTSCORES.md | Benchmark results and quality metrics |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
