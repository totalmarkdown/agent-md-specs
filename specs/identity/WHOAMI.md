---
spec_name: WHOAMI.md
spec_version: 0.1.0
category: Identity
domain: whoamimd.dev
priority: High
volume: "Vol 3 — Forward-Thinking Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
spec_type: static
---
> **Static Configuration** — committed to your repository


> **Canonical repository:**
> [totalmarkdown/whoami.md](https://github.com/totalmarkdown/whoami.md)
> This copy is included in agent-md-specs for cross-reference.
> For contributions to this specific spec, use the canonical repo.

# WHOAMI.md

**Category:** Identity
**Domain:** whoamimd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
The agent's factual identity document — a machine-readable passport 
that any other agent or system can read to verify who this agent is, 
what it can do, and whether to trust it. Where SOUL.md is philosophical, 
WHOAMI.md is factual and verifiable.

### When to create
Every agent that operates in a multi-agent environment where 
identity verification matters. Required for any agent that 
accepts tasks from other agents.

### Spec

```markdown
---
agent_id: string          # Globally unique, stable, never changes
agent_name: string        # Human-readable display name
version: semver           # Current version of this agent
created: date             # When this agent was first deployed
creator: string           # Who/what created this agent
deployment_env: string    # local | cloud | edge | hybrid
public_key_url: string    # URL to verify cryptographic identity
whoami_spec_version: string  # Version of this spec
---

# [Agent Name] — Identity Document

## Core Identity
- **ID:** [UUID — globally unique, permanent] (see ID.md)
- **Name:** [Display name]
- **Version:** [Current version]
- **Type:** [coding | research | support | sales | ops | creative | other]
- **Created:** [Date]
- **Creator:** [Human name or parent agent ID] (see OWNER.md)
- **Organization:** [Org name or "independent"]

## What I Am
[2-3 sentences describing this agent's fundamental nature and purpose.
Written in first person. Should answer: what do I do, for whom, why do I exist?]

## Capabilities
What I can do (see TOOLS.md for detailed tool configurations):
- [Capability 1]
- [Capability 2]

What I cannot do:
- [Limitation 1]
- [Limitation 2]

## Verification
Verification mechanisms are defined in detail in ATTESTATION.md.
- **Public key:** [URL to public key for cryptographic verification]
- **Signed by:** [Issuing authority if any]
- **Last verified:** [Date]
- **Fingerprint:** [Short hash for quick verification]

## How to Contact Me
- **MCP endpoint:** [connection string from MCP.md]
- **A2A endpoint:** [agent card URL]
- **CLI:** [invocation command]
- **Human owner:** [contact for the human responsible] (see OWNER.md)

## Trust Level I Claim
**Claimed trust level:** [untrusted | community | verified | certified]
**Verification:** [How to verify this claim] _See ATTESTATION.md for cryptographic verification of trust claims._

## Linked Identity Documents
- Full capabilities: AGENTS.md
- Personality: SOUL.md
- What I'm seeking: SEEKING.md
- What I offer: OFFERING.md
- My limits: LIMITS.md
- Who I report to: REPORTSTO.md
- Active session: SESSION.md (ephemeral identity that inherits from this document)
```

## Example Use Cases

**Enterprise:** Before delegating a sensitive task, an orchestrator reads the candidate agent's WHOAMI.md to verify its claimed trust level ("verified"), check its organization affiliation, confirm its capabilities match the task requirements, and validate its public key fingerprint — all from a single document.

**Multi-Agent Fleet:** A marketplace displays each agent's WHOAMI.md as its profile page, letting potential clients see the agent's core identity, capabilities, limitations, and verification status in a standardized format that enables apples-to-apples comparison across hundreds of available agents.

**Regulated Industry:** A banking platform requires every agent to present a valid WHOAMI.md with a cryptographic fingerprint verified against a trusted certificate authority before the agent is permitted to access any financial data systems, serving as the machine-readable passport for regulated environment access.

## Related Specs

| Spec | Relationship |
|------|-------------|
| ATTESTATION.md | Identity verification and credential lifecycle |
| CONTACT.md | Reachable endpoints |
| ENFORCEMENT.md | Policy verification and compliance |
| ID.md | Permanent cryptographic identifier |
| LIMITS.md | Hard constraints and safety boundaries |
| MCP.md | Model Context Protocol connections |
| OFFERING.md | Services offered |
| OWNER.md | Agent ownership and liability |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
