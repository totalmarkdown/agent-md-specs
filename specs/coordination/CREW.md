---
spec_name: CREW.md
spec_version: 0.1.0
category: Coordination
domain: crewmd.dev
priority: High
volume: "Vol 6 — Hierarchy Completion & Identity Anchors"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
---

# CREW.md

**Category:** Coordination
**Domain:** crewmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Defines a crew — a specialized working group of 3-10 agents 
that handles a specific workstream within a swarm or as a 
standalone unit. More specialized than a team (TEAM.md), 
more focused than a swarm (SWARM.md).

In TotalData.ai architecture: Crews sit between Swarms and ICs.
A crew is like a specialized squad — everyone has a role,
they work tightly together, and they produce a specific output.

### Spec

```markdown
---
crew_name: string
crew_id: string
version: semver
specialty: string         # What this crew specializes in
crew_type: string         # research | execution | review | support | mixed
agent_count: number       # 3-10 agents
parent_swarm: string      # SWARM.md reference, or "standalone"
lead_agent: string        # Which agent coordinates the crew
created: date
updated: date
---

# [Crew Name] — Crew Configuration

## Specialty
**[One sentence: what this crew specializes in and delivers]**

## Crew Composition

### [Lead Agent Name] — Crew Lead
- **File:** [path to agent's CLAUDE.md or AGENTS.md]
- **Role:** Coordinates crew, makes final decisions, handles escalations
- **Strengths:** [Key strengths]

### [Agent Name] — [Role]
- **File:** [path]
- **Role:** [What this agent does in the crew]
- **Inputs from:** [Which crew member feeds them]
- **Outputs to:** [Which crew member receives their work]

[Repeat for each crew member — max 10]

## Crew Workflow

```
[Lead Agent] assigns task
      ↓
[Agent A] processes → [Agent B] reviews → [Agent C] finalizes
                    ↗ (parallel)
[Agent D] researches
      ↓
[Lead Agent] approves and delivers output
```

## Input / Output Contract

### What this crew accepts
- **Input format:** [format]
- **Required fields:** [list]
- **Optional context:** [list]
- **Maximum input size:** [limit]

### What this crew delivers
- **Output format:** [format]
- **Guaranteed fields:** [list]
- **Quality standard:** [threshold]
- **Delivery time:** [SLA]

## Decision Making
- Day-to-day decisions: Individual agents autonomously
- Crew-level decisions: Lead agent
- Cross-crew decisions: Escalate to SWARM.md orchestrator
- Policy decisions: Escalate to human per ESCALATION.md

## Quality Control
Every crew output goes through:
1. [Agent name] reviews for [quality dimension]
2. [Agent name] validates against [standard]
3. Lead agent final approval
4. Confidence score attached (see VALIDATION.md)

## Crew Metrics
| Metric | Target | Current |
|--------|--------|---------|
| Output quality | >[N]/100 | [current] |
| Throughput | [N]/day | [current] |
| Internal error rate | <[N]% | [current] |
| Lead time | <[X] hours | [current] |

## Marketplace
Available as a standalone crew bundle:
- **Listing:** [TotalAgents.ai URL]
- **Price:** [pricing]
- **Works with:** Any compatible swarm or standalone
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| DELEGATION.md | Authority chain and authorization |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| ORG.md | Organization-wide fleet configuration |
| SHAREDCONTEXT.md | Multi-agent shared memory pool |
| SWARM.md | Large operation structure |
| TEAM.md | Multi-agent team coordination |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
