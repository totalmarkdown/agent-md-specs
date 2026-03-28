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
standalone unit. More specialized than a team (see TEAM.md),
more focused than a swarm (SWARM.md).

In TotalData.ai architecture: Crews sit between Swarms and ICs.
A crew is like a specialized squad -- everyone has a role,
they work tightly together, and they produce a specific output
(see SWARM.md for the larger coordinated operations that crews compose into).

### Spec

````markdown
---
crew_name: string
crew_id: string
version: semver
specialty: string         # What this crew specializes in
crew_type: string         # research | execution | review | support | mixed
agent_count: number       # 3-10 agents; see TEAM.md for looser team groupings
parent_swarm: string      # SWARM.md reference, or "standalone"
lead_agent: string        # Which agent coordinates the crew; see DELEGATION.md for authority
shared_context: string    # See SHAREDCONTEXT.md for shared memory configuration
budget_ref: string        # See BUDGET.md for crew-level cost controls
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

The crew workflow defines how tasks flow between members. For authority rules governing who can assign and approve, see DELEGATION.md. For inherited configuration from parent structures, see INHERIT.md.

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
- Crew-level decisions: Lead agent (see DELEGATION.md for authority rules)
- Cross-crew decisions: Escalate to SWARM.md orchestrator
- Policy decisions: Escalate to human per ESCALATION.md

## Quality Control
Every crew output goes through:
1. [Agent name] reviews for [quality dimension]
2. [Agent name] validates against [standard]
3. Lead agent final approval
4. Confidence score attached (see VALIDATION.md)

## Failure Handling

When a crew member fails or becomes unresponsive, apply CIRCUITBREAKER.md patterns to isolate the failure and prevent cascading disruption across the crew. The lead agent should coordinate recovery using SHAREDCONTEXT.md to maintain state continuity.

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
````

## Example Use Cases

**Enterprise:** A financial services firm assembles a 5-agent due-diligence crew (data extraction, financial analysis, risk assessment, regulatory check, report generation) that processes acquisition targets with defined input/output contracts and a 4-hour SLA from brief to final report.

**Multi-Agent Fleet:** A DevOps platform organizes agents into specialized crews (monitoring, incident response, post-mortem analysis) within a larger operations swarm, where each crew has its own lead agent, quality metrics, and failure-handling procedures independent of other crews.

**Regulated Industry:** A clinical trials data crew of 7 agents handles patient data extraction, statistical analysis, and adverse-event detection, with the crew lead enforcing quality control checkpoints that satisfy FDA 21 CFR Part 11 requirements before any output leaves the crew.

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
