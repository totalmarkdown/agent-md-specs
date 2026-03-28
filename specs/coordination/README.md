# Coordination Specs

Specs for multi-agent collaboration -- how agents find each other, form teams, communicate, and share state. Without coordination specs, multi-agent systems devolve into isolated processes that duplicate work, contradict each other, or deadlock waiting on responses that never come.

## How These Specs Work Together

TEAM.md is the foundational spec: it defines a group of agents, their roles, and how they hand off work. CREW.md and SWARM.md extend the hierarchy -- crews are specialized squads of 3-10 agents, and swarms coordinate multiple crews toward a shared objective. Before agents can collaborate, they establish trust via HANDSHAKE.md, then communicate using the message format defined in PROTOCOL.md. SHAREDCONTEXT.md governs the persistent shared memory pool that team members read and write to, preventing stale references and conflicting facts. ROSTER.md is the team directory, COLLABORATE.md sets collaboration norms for mixed human-agent teams, and SHARE.md controls who can share resources and under what conditions.

## Specs in This Category

| Spec | Tier | Purpose | Scope |
|------|------|---------|-------|
| COLLABORATE.md | extended | Collaboration rules for mixed human-agent projects | Per-project |
| CREW.md | core | Specialized working group of 3-10 agents within a swarm | Per-crew |
| HANDSHAKE.md | extended | Trust establishment and credential exchange between agents | Per-connection |
| PROTOCOL.md | extended | Message format and communication rules between agents | Per-team |
| ROSTER.md | extended | Registry of all agents in a team or fleet | Per-team |
| SHARE.md | extended | Access control and sharing rules for resources | Per-resource |
| SHAREDCONTEXT.md | core | Governed shared memory pool for multi-agent state | Per-team/crew |
| SWARM.md | core | Large-scale coordination of multiple crews | Per-swarm |
| TEAM.md | core | Team structure, roles, and orchestration pattern | Per-team |

## When to Use These Specs

- **Two or more agents working on related tasks:** Start with TEAM.md to define roles and orchestration, add PROTOCOL.md for message format.
- **Agents that need shared memory:** Add SHAREDCONTEXT.md to govern what gets stored, who can write, and how long entries persist.
- **Scaling beyond a single team:** Use CREW.md and SWARM.md to organize agents into specialized squads and coordinate across them.
- **Onboarding a new agent into an existing fleet:** Use ROSTER.md for discovery, HANDSHAKE.md for trust, and SHARE.md for resource access.

## Related Categories

| Category | How It Relates |
|----------|---------------|
| [organizational/](../organizational/) | Defines the fleet hierarchy (ORG, reporting chains) that coordination specs operate within |
| [governance/](../governance/) | Sets the rules and policies that constrain how coordinated agents behave |
| [security/](../security/) | Provides the trust and authentication foundations that HANDSHAKE.md builds on |

---
*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)
· [Full Index](../../INDEX.md) · [README](../../README.md)*
