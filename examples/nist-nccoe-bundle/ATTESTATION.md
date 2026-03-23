---
agent_name: "Atlas"
version: "2.1.0"
org: "Acme Corp"
ca_issuer: "Acme Corp Internal CA"
spiffe_id: "spiffe://acme.corp/finance/agents/atlas"
key_rotation_days: 90
created: "2025-11-01"
updated: "2026-03-15"
---

# Atlas -- Attestation

## Cryptographic Identity

Atlas's identity is bound to a cryptographic certificate chain rooted in Acme
Corp's internal certificate authority. This binding ensures that any system
communicating with Atlas can verify it is the authentic agent and not an
impersonator.

### X.509 Certificate

- **Subject:** CN=atlas.finance.agents.acme.corp
- **Issuer:** CN=Acme Corp Internal CA, O=Acme Corp, C=US
- **Serial:** 7A:3F:B2:C1:9E:4D:8A:6F
- **Algorithm:** ECDSA P-384
- **Key size:** 384-bit elliptic curve
- **Valid from:** January 2, 2026
- **Valid until:** April 2, 2026 (90-day lifecycle)
- **CRL:** http://crl.pki.acme.corp/intermediate.crl
- **OCSP:** http://ocsp.pki.acme.corp/

### SPIFFE Identity

- **Trust domain:** acme.corp
- **SPIFFE ID:** spiffe://acme.corp/finance/agents/atlas
- **SVID type:** X.509-SVID
- **Workload registrar:** Kubernetes PSAT (projected service account token)
- **SPIRE server:** spire-server.infra.acme.corp:8081

## Key Rotation

- **Rotation interval:** 90 days
- **Next rotation:** April 2, 2026
- **Rotation method:** Automated via SPIRE agent. New SVID issued 24 hours
  before current SVID expiration. Old key revoked immediately upon new key
  activation.
- **Emergency rotation:** InfoSec team can trigger immediate rotation via
  pki.acme.corp/emergency-rotate. Requires two-person authorization.
- **Rotation log:** All rotation events logged to AUDITTRAIL.md and
  pki-events.acme.corp

## Container Binding

Atlas runs in an immutable container image. The attestation binds the
cryptographic identity to the specific container hash to prevent identity
theft via container replacement.

- **Container registry:** registry.acme.corp/finance/atlas
- **Image tag:** v2.1.0-prod
- **Image digest:** sha256:a3f7b2c19e4d4a8bb5f62d1e8c7a4f9e1b3d5a7c9e2f4b6d8a0c2e4f6a8b0d2
- **Runtime:** Kubernetes 1.29, isolated namespace `finance-agents`
- **Node attestation:** TPM 2.0 measured boot chain
- **Pod security:** Restricted PSS, read-only root filesystem, no privilege
  escalation, dropped all capabilities except NET_BIND_SERVICE

## Verification

Any service within Acme's infrastructure can verify Atlas's identity before
accepting its requests or providing it with data.

- **Verification endpoint:** https://verify.acme.corp/agents/atlas
- **Verification method:** Present Atlas's X.509-SVID. Endpoint returns JSON
  with identity confirmation, delegation status, and current permissions hash.
- **mTLS requirement:** All connections to and from Atlas require mutual TLS.
  One-way TLS connections are rejected.
- **Certificate pinning:** Bloomberg API integration uses certificate pinning
  with backup pins rotated quarterly.

## Trust Chain

```
Acme Corp Root CA (offline, HSM-stored)
  --> Acme Corp Intermediate CA (online, HSM-backed)
    --> SPIRE Server CA (short-lived, automated)
      --> Atlas X.509-SVID (90-day, container-bound)
```

## Incident Response

If Atlas's cryptographic identity is compromised:

1. InfoSec triggers emergency key rotation
2. All active sessions are terminated immediately
3. Delegation is suspended pending investigation
4. Compromised certificate is added to CRL within 5 minutes
5. Post-incident review determines root cause before re-attestation
