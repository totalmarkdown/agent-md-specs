# Security Specs

Security specs define the protection layer for AI agents -- how they prove identity, defend against attacks, manage secrets, and isolate execution. These seven specs cover the most critical attack surfaces: identity spoofing, prompt injection, memory poisoning, and credential exposure. Every agent that handles sensitive data or operates autonomously needs this category.

## How These Specs Work Together

Security specs form a defense-in-depth stack. ATTESTATION.md proves the agent is who it claims to be, closing the identity spoofing gap that WHOAMI.md alone cannot address. PROMPTSHIELD.md defends the context window against direct and indirect prompt injection -- the most prevalent attack vector for LLM-based agents. MEMORYSAFETY.md guards persistent memory against poisoning and cross-session contamination. SECRETS.md and VAULT.md handle credential lifecycle, while ACCESS.md controls who can invoke the agent and SANDBOX.md isolates its execution environment. Start with ATTESTATION and PROMPTSHIELD as the minimum security baseline, then add the others based on threat model.

## Specs in This Category

| Spec | Tier | Purpose | Scope |
|------|------|---------|-------|
| [ACCESS.md](ACCESS.md) | core | Allowlist of authorized callers and their permission levels | Caller authorization |
| [ATTESTATION.md](ATTESTATION.md) | core | Cryptographic identity proof and credential lifecycle | Identity verification |
| [MEMORYSAFETY.md](MEMORYSAFETY.md) | core | Defenses against memory poisoning and cross-session contamination | Memory protection |
| [PROMPTSHIELD.md](PROMPTSHIELD.md) | core | Detection and defense against prompt injection attacks | Input defense |
| [SANDBOX.md](SANDBOX.md) | extended | Isolation and containment at the OS/container level | Execution isolation |
| [SECRETS.md](SECRETS.md) | core | Declaration of required secrets without exposing values | Credential inventory |
| [VAULT.md](VAULT.md) | extended | Vault system configuration for fleet-wide secret management | Secret storage |

## When to Use These Specs

- **Deploying any production agent:** Adopt ATTESTATION and PROMPTSHIELD immediately -- identity spoofing and prompt injection are the two highest-likelihood attack vectors for LLM-based agents.
- **Handling credentials or API keys:** Add SECRETS and VAULT to declare what the agent needs and centralize credential management without leaking values into config files.
- **Running agents in shared or hostile environments:** Layer in MEMORYSAFETY, ACCESS, and SANDBOX to prevent cross-agent contamination, unauthorized invocation, and container escapes.
- **Operating at fleet scale:** Combine ACCESS with VAULT for centralized credential rotation and caller authorization across hundreds of agents.

## Key Threat Model

Security specs map to the primary attack surfaces in agent systems:

| Threat | Spec | Defense |
|--------|------|---------|
| Identity spoofing | ATTESTATION.md | Cryptographic proof tied to hardware or PKI roots |
| Prompt injection | PROMPTSHIELD.md | Input validation, canary tokens, context isolation |
| Memory poisoning | MEMORYSAFETY.md | Write controls, integrity checks, contamination isolation |
| Credential theft | SECRETS.md, VAULT.md | Declarative inventory, encrypted storage, rotation |
| Unauthorized access | ACCESS.md | Caller allowlists with scoped permission levels |
| Container escape | SANDBOX.md | OS-level isolation and resource constraints |

## Related Categories

| Category | How It Relates |
|----------|---------------|
| [governance/](../governance/) | Governance defines the policies that security enforces -- PERMISSIONS declares boundaries, ENFORCEMENT verifies them, and security specs protect the mechanisms |
| [compliance/](../compliance/) | AUDITTRAIL records security events, PROVENANCE tracks data integrity, and CONSENT governs what security-relevant actions require user permission |
| [identity/](../identity/) | WHOAMI.md and ID.md declare identity; ATTESTATION.md in this category is what makes those declarations verifiable and trustworthy |

---
*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)
· [Full Index](../../INDEX.md) · [README](../../README.md)*
