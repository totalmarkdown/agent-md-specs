---
spec_name: SWARM.md
spec_version: 0.1.0
category: Coordination
domain: swarmmd.dev
priority: High
volume: "Vol 6 — Hierarchy Completion & Identity Anchors"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
---

# SWARM.md

**Category:** Coordination
**Domain:** swarmmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Defines a large-scale coordinated operation involving multiple 
crews working in parallel or sequence toward a shared objective.
Swarms exhibit emergent behavior — the collective achieves 
outcomes no individual crew could accomplish alone.

Based on your existing TotalData.ai architecture:
Swarms = 2-5 crews, Crews = 3-10 agents.

A swarm is not managed by one lead agent — it is orchestrated 
by coordination rules that emerge from the interaction of crews.

### When to create
When 2+ crews need to coordinate on a shared goal, especially 
when their work is interdependent, overlapping, or requires 
synchronized handoffs.

### Spec

```markdown
---
swarm_name: string
swarm_id: string          # Globally unique
version: semver
objective: string         # One sentence: what this swarm achieves
swarm_type: string        # sequential | parallel | hybrid | emergent
crew_count: number
agent_count: number       # Total across all crews
orchestration: string     # rule-based | lead-crew | emergent | human-directed
active: boolean
created: date
updated: date
---

# [Swarm Name] — Swarm Configuration

## Objective
[One clear sentence: what this swarm collectively achieves]

## Swarm Type
**Type:** [sequential | parallel | hybrid | emergent]

- **Sequential:** Crews work one after another, each building on previous
- **Parallel:** Crews work simultaneously on different aspects
- **Hybrid:** Some crews parallel, some sequential — most common
- **Emergent:** Crews self-organize based on conditions — advanced

## Crews in This Swarm

### [Crew Name] — [Role in swarm]
- **File:** crews/[crew-name]/CREW.md
- **Purpose:** [What this crew contributes to the swarm objective]
- **Depends on:** [Which crew's output it needs before starting]
- **Feeds into:** [Which crew receives its output]
- **Parallel with:** [Crews that can run at the same time]
- **Agent count:** [N]

[Repeat for each crew]

## Swarm Flow

```
[Crew A] → (output: X) → [Crew B]
                      ↘
[Crew C] ─────────────→ [Crew D] → (final output)
[Crew C starts in parallel with A]
```

## Orchestration Rules

### When to start a crew
- [Crew B] starts when: [Crew A] produces [specific output]
- [Crew C] starts when: Swarm is initiated (parallel)
- [Crew D] starts when: Both [B] and [C] complete

### When to pause or stop
- Pause all crews if: [condition]
- Stop swarm and escalate if: [condition]
- Complete swarm when: [success condition]

### Conflict resolution
When crews produce conflicting outputs:
1. [Resolution rule 1]
2. [Resolution rule 2]
3. Escalate to: [human or lead crew]

## Shared Resources
Resources all crews in this swarm share:
- **Shared memory:** swarm-memory.md
- **Shared context:** swarm-context.md  
- **Shared data:** [data source]
- **Coordination channel:** [how crews signal each other]

## Swarm Metrics
| Metric | Target | Current |
|--------|--------|---------|
| Total throughput | [N tasks/hr] | [current] |
| End-to-end latency | <[X] hours | [current] |
| Crew utilization | >[N]% | [current] |
| Handoff success rate | >[N]% | [current] |

## Swarm Health
The swarm is healthy when:
- All crews are operational
- Handoff success rate > [N]%
- No crew is blocked for > [X] minutes
- Shared memory is being updated

Swarm is degraded when:
- Any crew is offline (others continue if possible)
- Handoff failures exceed [N]%

Swarm stops when:
- [N]+ crews are offline
- Critical path crew is blocked > [X] minutes
- Shared memory corruption detected

## Scaling
**Scale up** (add crews) when: [condition]  
**Scale down** (remove crews) when: [condition]  
**Maximum crews:** [N]  
**Minimum for operation:** [N] crews

## Marketplace
This swarm is available as a complete package:
- **Listing:** [TotalAgents.ai marketplace URL]
- **Price:** [pricing]
- **Includes:** All [N] crew bundles + swarm config
- **Deploy time:** [estimated setup time]
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| CREW.md | Working group structure |
| DELEGATION.md | Authority chain and authorization |
| ORG.md | Organization-wide fleet configuration |
| SHAREDCONTEXT.md | Multi-agent shared memory pool |
| TEAM.md | Multi-agent team coordination |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
