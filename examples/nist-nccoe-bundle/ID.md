---
spec_name: "ID.md"
spec_version: "1.0.0"
category: "Identity"
tier: core
priority: High
agent_name: "Atlas"
agent_version: "2.1.0"
---

# Atlas — Permanent Identity

## UUID

```yaml
agent_id: "550e8400-e29b-41d4-a716-446655440000"
created: "2025-01-15T00:00:00Z"
issuing_authority: "Acme Corp Identity Services"
```

## Cryptographic Binding

This UUID is cryptographically bound to the SPIFFE workload identity
declared in ATTESTATION.md:

- SPIFFE ID: `spiffe://acme.corp/finance/agents/atlas`
- X.509 Subject: `CN=atlas,OU=finance,O=acme-corp`
- Binding method: SPIFFE ID embeds the UUID as a URI SAN

## Permanence

This identity persists across:
- Session boundaries (SESSION.md sessions are ephemeral; this ID is not)
- Software upgrades (model version changes do not change the UUID)
- Infrastructure migrations (cloud region, container host)
- Key rotations (ATTESTATION.md credential rotation does not change the UUID)

The UUID is retired only when the agent is decommissioned per LEGACY.md.

## Verification

Any entity can verify this identity by:
1. Requesting Atlas's SPIFFE bundle from the trust domain
2. Validating the X.509 certificate chain to Acme Corp Internal CA
3. Confirming the UUID in the certificate SAN matches this document
