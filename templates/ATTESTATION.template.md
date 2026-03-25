---
spec_name: ATTESTATION.md
spec_version: 0.1.0
category: Identity
domain: specmd.dev
priority: P0
tier: core
---

# [REPLACE THIS — Agent Name] — Identity Attestation

<!-- Cryptographic proof of agent identity using SPIFFE, X.509, or DID -->

## Attestation Method
- **Type:** [REPLACE THIS — SPIFFE | X.509 | DID | HMAC | none]
- **Standard:** [REPLACE THIS — e.g. SPIFFE v1.0, X.509v3, did:web]
- **Issuer:** [REPLACE THIS — CA or identity provider]

## SPIFFE ID
<!-- Only if using SPIFFE; remove section otherwise -->
- **SPIFFE ID:** [REPLACE THIS — e.g. spiffe://example.org/agent/researcher]
- **Trust domain:** [REPLACE THIS — e.g. example.org]
- **Workload selector:** [REPLACE THIS — how the runtime identifies this workload]

## Certificate Details
<!-- Only if using X.509; remove section otherwise -->
- **Subject:** [REPLACE THIS — CN and O fields]
- **Serial:** [REPLACE THIS — certificate serial number]
- **Expires:** [REPLACE THIS — YYYY-MM-DD]
- **CA chain:** [REPLACE THIS — path to CA bundle or "system trust store"]

## DID Document
<!-- Only if using DID; remove section otherwise -->
- **DID:** [REPLACE THIS — e.g. did:web:example.com:agents:researcher]
- **Verification method:** [REPLACE THIS — key type and ID]
- **Service endpoint:** [REPLACE THIS — URL for resolution]

## Rotation Policy
- **Auto-rotate:** [REPLACE THIS — true | false]
- **Rotation interval:** [REPLACE THIS — e.g. 24h, 7d, 90d]
- **On compromise:** [REPLACE THIS — action to take if key is compromised]

## Verification Steps
1. [REPLACE THIS — step to retrieve credential]
2. [REPLACE THIS — step to validate against trust anchor]
3. [REPLACE THIS — step to check revocation status]

## Related Specs
- ID.md: [REPLACE THIS — path]
- PERMISSIONS.md: [REPLACE THIS — path]
