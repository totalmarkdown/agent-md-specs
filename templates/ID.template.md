---
spec_name: ID.md
spec_version: 0.1.0
category: Identity
priority: High
tier: core
---

# [REPLACE THIS — Agent Name] — Permanent Identity

<!-- Immutable UUID anchor that persists across sessions, deployments, and migrations -->

## Identity Anchor
- **UUID:** [REPLACE THIS — UUID v4, e.g. 550e8400-e29b-41d4-a716-446655440000]
- **Created:** [REPLACE THIS — YYYY-MM-DD]
- **Created by:** [REPLACE THIS — person or system that minted the ID]
- **Immutable:** true

## Naming
- **Canonical name:** [REPLACE THIS — the official agent name]
- **Aliases:** [REPLACE THIS — alternative names, or "none"]
- **Namespace:** [REPLACE THIS — org prefix, e.g. acme.agents.researcher]

## Lifecycle
- **Status:** [REPLACE THIS — active | suspended | decommissioned]
- **Successor:** [REPLACE THIS — UUID of replacement agent, or "none"]
- **Predecessor:** [REPLACE THIS — UUID of previous version, or "none"]

## Binding
<!-- What this ID is bound to — prevents identity spoofing -->
- **Bound to bundle:** [REPLACE THIS — path to agent bundle root]
- **Signing key:** [REPLACE THIS — public key fingerprint, or "none"]
- **Registry entry:** [REPLACE THIS — URL or path to registry record]

## Verification
<!-- How another agent or system confirms this identity -->
- **Method:** [REPLACE THIS — key lookup | registry query | attestation chain]
- **Endpoint:** [REPLACE THIS — URL or path to verify against]

## Related Specs
- WHOAMI.md: [REPLACE THIS — path]
- ATTESTATION.md: [REPLACE THIS — path]
- OWNER.md: [REPLACE THIS — path]
