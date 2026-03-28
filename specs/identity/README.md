# Identity Specs

Identity specs define who an agent is -- from machine-readable identifiers to personality, values, and communication style. In multi-agent systems, identity is not vanity; it determines whether other agents trust, invoke, or reject an agent. Without these specs, agents are anonymous black boxes with no accountability trail.

## How These Specs Work Together

Identity builds in layers. WHOAMI.md declares the agent's factual identity as a machine-readable passport. ID.md anchors that identity with a minimal, globally unique identifier. SOUL.md adds depth -- values, personality, and ethical boundaries that shape behavior beyond task instructions. CONTACT.md and CHANNELS.md make the agent reachable, while PERSONA.md and VOICE.md control how it presents itself to end users. Start with WHOAMI and ID as the foundational pair, add SOUL for agents with personality, then adopt the remaining specs as your agent's public surface area grows.

## Specs in This Category

| Spec | Tier | Purpose | Scope |
|------|------|---------|-------|
| [ALIASES.md](ALIASES.md) | extended | Alternative names and previous identifiers | Name history |
| [ASSUMPTIONS.md](ASSUMPTIONS.md) | extended | Key assumptions the agent's design depends on | Design preconditions |
| [CHANGELOG.md](CHANGELOG.md) | extended | Version history of what changed in each release | Release tracking |
| [CHANNELS.md](CHANNELS.md) | extended | All communication channels and endpoints available | Reachability map |
| [CONTACT.md](CONTACT.md) | core | How to reach the agent and its human operators | Contact details |
| [GLOSSARY.md](GLOSSARY.md) | extended | Shared vocabulary for consistent terminology | Domain language |
| [ID.md](ID.md) | core | Minimal machine-readable identity anchor | Unique identifier |
| [KRYPTONITE.md](KRYPTONITE.md) | extended | Known weaknesses and documented failure modes | Honest limitations |
| [MANIFESTO.md](MANIFESTO.md) | extended | Public declaration of principles and purpose | Mission statement |
| [OFFERING.md](OFFERING.md) | extended | Services, data, and capabilities offered to others | Service catalog |
| [ONBOARDING.md](ONBOARDING.md) | extended | Context for new agents or humans joining mid-stream | Project orientation |
| [PERSONA.md](PERSONA.md) | extended | Public-facing name, avatar, and introduction script | User-facing identity |
| [PREFERENCES.md](PREFERENCES.md) | extended | Working preferences for communication and output | Operational style |
| [QUIRKS.md](QUIRKS.md) | extended | Distinctive behaviors documented to prevent surprise | Behavioral oddities |
| [REPUTATION.md](REPUTATION.md) | extended | Track record, endorsements, and trust signals | Trust history |
| [SEEKING.md](SEEKING.md) | extended | What the agent is actively looking for | Resource requests |
| [SIGNATURE.md](SIGNATURE.md) | extended | Standard signature format for agent outputs | Output attribution |
| [SOUL.md](SOUL.md) | core | Deep identity -- personality, values, ethical boundaries | Core essence |
| [VOICE.md](VOICE.md) | extended | Writing style, tone calibration, and vocabulary choices | Communication style |
| [WHOAMI.md](WHOAMI.md) | core | Factual identity document -- a machine-readable passport | Identity declaration |

## When to Use These Specs

- **Launching any agent:** Start with WHOAMI and ID so other systems can verify who the agent is and route communication to it.
- **Building user-facing agents:** Add SOUL, PERSONA, and VOICE to give the agent a consistent, trustworthy presence that users can relate to.
- **Operating in multi-agent environments:** Adopt OFFERING, SEEKING, and REPUTATION so agents can discover each other's capabilities and make trust decisions autonomously.

## Related Categories

| Category | How It Relates |
|----------|---------------|
| [security/](../security/) | ATTESTATION.md cryptographically proves the identity that WHOAMI.md and ID.md declare -- identity without verification is just a claim |
| [lifecycle/](../lifecycle/) | Lifecycle specs govern how identity evolves -- BIRTH creates it, RETIRE ends it, and CHANGELOG tracks what changed between |
| [governance/](../governance/) | DELEGATION.md binds agent identity to human identity, creating the accountability chain that identity specs alone cannot provide |

---
*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)
· [Full Index](../../INDEX.md) · [README](../../README.md)*
