---
spec_name: ATTESTATION.md
spec_version: 0.1.0
category: Security
priority: Very High
volume: "Vol 14 — Agent Identity, Accountability & Compliance"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
status: proposed
proposed_on: 2026-04-18
spec_type: static
---


# ATTESTATION.md

**Category:** Security
**Priority:** Very High
**Version:** 0.1.0 **Type:** Static

### Purpose
Defines how an agent cryptographically proves its identity to other
agents, services, and human operators. Where WHOAMI.md declares
identity, ATTESTATION.md defines how that identity is *verified* —
the mechanisms, credentials, and trust anchors that make the
declaration believable.

Without attestation, any agent can claim to be any other agent.
ATTESTATION.md closes that gap by binding identity claims to
cryptographic proof, hardware roots of trust, and organizational
certificate chains.

At fleet scale, ATTESTATION.md enables:
- Zero-trust agent-to-agent authentication
- Credential lifecycle management across hundreds of agents
- Hardware-rooted identity that survives software redeployment
- Auditability of who authenticated as whom, and when

### Scope Boundary

This spec governs **cryptographic identity verification and credential lifecycle**.

- ATTESTATION.md defines **how the agent proves its identity** (runtime, continuous)
- WHOAMI.md defines **who the agent claims to be** (static, pre-deployment)
- ID.md defines **the permanent UUID anchor** (static, pre-deployment)
- SESSION.md defines **the ephemeral runtime identity** that inherits from attestation (see SESSION.md for session credential lifecycle)
- ENFORCEMENT.md defines **how attestation is verified** at runtime (see ENFORCEMENT.md for the runtime verification matrix)

ATTESTATION.md does NOT define the agent's identity — it defines how
that identity is cryptographically verified by external systems.

### When to Create This File
Every agent that communicates with other agents, accesses shared
resources, or operates in a zero-trust environment. Required for
any agent claiming a trust level above "untrusted" in WHOAMI.md.
Critical for agents handling sensitive data or executing
high-stakes actions on behalf of humans.

### Spec

````markdown
---
agent_name: string
agent_id: string              # Must match WHOAMI.md agent_id (see WHOAMI.md) and ID.md UUID (see ID.md)
version: semver
attestation_method: string    # spiffe | x509 | did | jwt | api_key
hardware_binding: string      # tpm | secure_enclave | cloud_hsm | none
trust_anchor: string          # Issuing authority or self-signed
credential_expiry: date
last_rotation: date
next_rotation: date
spec_version: string
---

# [Agent Name] — Attestation Configuration

## Attestation Method

**Primary method:** [SPIFFE/SPIRE | X.509 | DID | JWT | API Key]
**Fallback method:** [secondary method or "none"]

Preference order (strongest to weakest):
1. **SPIFFE/SPIRE** — Workload identity (spiffe.io) with automatic rotation,
   platform-agnostic, designed for zero-trust service meshes
2. **X.509 certificates** — Industry standard PKI, widely supported,
   requires certificate authority infrastructure
3. **DID (Decentralized Identifier)** — Self-sovereign identity,
   no central authority dependency, emerging standard
4. **JWT (JSON Web Token)** — Lightweight, widely supported,
   suitable for short-lived sessions and API interactions
5. **API Key** — Simplest, weakest; acceptable only for internal
   low-sensitivity agents behind network controls

### Current Configuration
| Property | Value |
|----------|-------|
| **Method** | [selected method] |
| **SPIFFE ID** | `spiffe://[trust-domain]/[path]` |
| **Certificate CN** | [common name] |
| **Key algorithm** | [RSA-4096 | ECDSA-P256 | Ed25519] |
| **Issued by** | [CA or issuing authority] |
| **Valid from** | [date] |
| **Valid until** | [date] |
| **Revocation check** | [OCSP | CRL | SPIRE rotation | none] |

---

## Hardware Binding

**Binding type:** [TPM 2.0 | Secure Enclave | Cloud HSM | None]

Hardware binding anchors the agent's identity to a physical device,
preventing credential theft from compromising identity.

| Property | Value |
|----------|-------|
| **Hardware module** | [TPM make/model | AWS CloudHSM | Azure HSM | GCP KMS | Apple Secure Enclave | none] |
| **Key storage** | [hardware-bound | software keystore | environment variable] | <!-- See SECRETS.md for credential storage requirements -->
| **Attestation quote** | [PCR values | enclave measurement | none] |
| **Extractable** | [yes | no — hardware-bound keys should be no] |
| **FIPS 140-2 level** | [1 | 2 | 3 | N/A] |

If hardware binding is "none", document the compensating controls:
- [e.g., short-lived credentials, network isolation, IP allowlisting]

---

## Software Binding

Software binding ties the agent's identity to a specific, verifiable
build — so a credential cannot be transplanted to a modified agent.

| Property | Value |
|----------|-------|
| **Container image hash** | `sha256:[digest]` |
| **Image registry** | [registry URL] |
| **Model weights checksum** | `sha256:[digest]` |
| **Code signature** | [signing key fingerprint] |
| **Build reproducibility** | [reproducible | best-effort | not verified] |
| **SBOM location** | [URL or path to Software Bill of Materials] |
| **Signed by** | [build system identity] |

Verification command:
```bash
# Verify container image
cosign verify --key [key-ref] [image-ref]

# Verify code signature
gpg --verify [signature-file] [code-artifact]
```

---

## Organizational Binding

Ties the agent's identity to a real-world organization through a
certificate chain or verifiable credential.

| Property | Value |
|----------|-------|
| **Issuing authority** | [Organization name and legal entity] |
| **Trust anchor** | [Root CA certificate fingerprint or DID document URL] |
| **Certificate chain depth** | [e.g., Root CA → Intermediate CA → Agent cert] |
| **Organization identifier** | [LEI, DUNS, or domain-validated org] |
| **Responsible human** | [Name and role of accountable person] |
| **Authority contact** | [Email or endpoint for CA/authority] |

Certificate chain:
1. **Root CA:** [fingerprint] — [organization]
2. **Intermediate CA:** [fingerprint] — [department or service]
3. **Agent certificate:** [fingerprint] — [this agent]

---

## Credential Lifecycle

### Issuance
Key material referenced here should be stored according to SECRETS.md.
- **Issued by:** [CA, SPIRE server, DID registry, or manual process]
- **Issuance requires:** [human approval | automated policy check | both]
- **Initial verification:** [identity proofing steps before first credential]
- **Delivery method:** [injected at deploy | fetched from vault | SPIRE SVID]

### Rotation Schedule
| Credential Type | Rotation Period | Method | Downtime |
|----------------|-----------------|--------|----------|
| SPIFFE SVID | [1 hour] | Automatic (SPIRE) | Zero |
| X.509 certificate | [90 days] | Automated renewal | Zero |
| JWT signing key | [24 hours] | Key rotation API | Zero |
| API key | [30 days] | Manual + vault update | Brief |

### Revocation
- **Revocation method:** [OCSP responder | CRL distribution | SPIRE eviction | manual]
- **Revocation triggers:** [credential compromise, agent decommission, policy violation] — on compromise, notify via ESCALATION.md
- **Revocation propagation time:** [seconds for SPIRE | hours for CRL | immediate for OCSP]
- **Who can revoke:** [security team | automated policy engine | agent owner]

### Recovery
If credentials are lost or compromised:
1. Revoke all existing credentials immediately
2. Re-verify agent identity through [identity proofing process]
3. Issue new credentials via [issuance process]
4. Update all services that trust this agent's old credentials
5. Log incident in AUDITTRAIL.md and notify [security contact]
6. Post-incident review within [48 hours]

---

## Verification Endpoint

Other agents and services verify this agent's identity here:

| Property | Value |
|----------|-------|
| **Endpoint URL** | `https://[domain]/.well-known/agent-attestation` |
| **Protocol** | [mTLS | SPIFFE Federation | DID Resolution | OAuth 2.0] |
| **Request format** | [SPIFFE bundle | certificate chain | DID document request] |
| **Response format** | [SPIFFE SVID | X.509 chain | DID document | JWT] |
| **Rate limit** | [requests per second] |
| **Caching** | [TTL for verification responses] |

Expected verification response:
```json
{
  "agent_id": "[agent_id matching WHOAMI.md]",
  "verified": true,
  "method": "[attestation method]",
  "trust_level": "[untrusted | community | verified | certified]",
  "valid_until": "[ISO 8601 timestamp]",
  "issuer": "[issuing authority]",
  "chain_valid": true
}
```

---

## Human-in-the-Loop Binding

For high-stakes actions, the agent's attestation is bound to a
specific human operator's authentication (see DELEGATION.md for
the authority chain linking agent actions to human principals).

| Property | Value |
|----------|-------|
| **Human auth method** | [FIDO2/WebAuthn | YubiKey | TOTP | none] |
| **Binding mechanism** | [Co-signed JWT | dual-signature | delegation token] |
| **Required for** | [List of action types requiring human binding] |
| **Session duration** | [How long the human binding remains valid] |
| **Re-authentication** | [After N actions | after N minutes | per action] |

Actions requiring human-bound attestation:
- [ ] Financial transactions above $[threshold]
- [ ] Data deletion or modification of production records
- [ ] Credential rotation or revocation for other agents
- [ ] Policy changes or guardrail modifications
- [ ] External communications on behalf of the organization

---

## NIST Standards Alignment

| Standard | Relevance | Compliance Status |
|----------|-----------|-------------------|
| **SP 800-207 (Zero Trust)** | Agent identity verification in zero-trust architecture | [compliant | partial | planned] |
| **SP 800-63-4 (Digital Identity)** | Identity assurance levels for agent credentials | [compliant | partial | planned] |
| **SP 800-57 (Key Management)** | Key lifecycle management for attestation keys | [compliant | partial | planned] |
| **SPIFFE/SPIRE** | Workload identity standard for service meshes | [adopted | evaluated | N/A] |
| **NIST AI RMF** | AI system identity and provenance requirements | [compliant | partial | planned] |

---

## Attestation Failures

When attestation fails, the agent MUST:
1. Refuse to execute the requested action
2. Log the failure with full context (who, what, when, why)
3. Notify the security contact: [contact]
4. Enter degraded mode (read-only, no external actions)
5. Do NOT retry with weaker credentials or bypass verification
````

## Example Use Cases

**Enterprise:** A large tech company uses ATTESTATION.md with SPIFFE/SPIRE to provide zero-downtime credential rotation for its 150 production agents, with SVIDs rotating every hour and hardware-bound keys in AWS CloudHSM preventing credential theft.

**Multi-Agent Fleet:** A marketplace platform requires every listed agent to have a valid ATTESTATION.md with organizational binding, creating a verifiable certificate chain from the agent back to a known legal entity before the agent can serve any customer.

**Regulated Industry:** A defense contractor uses ATTESTATION.md with TPM 2.0 hardware binding and NIST SP 800-207 zero-trust alignment for its intelligence analysis agents, ensuring credentials cannot be extracted from compromised hosts and every agent-to-agent interaction is mutually authenticated.

## Related Specs

| Spec | Relationship |
|------|-------------|
| WHOAMI.md | Agent identity declaration |
| ID.md | Permanent cryptographic identifier |
| SECRETS.md | Required credentials manifest |
| DELEGATION.md | Authority chain and authorization |
| AUDITTRAIL.md | Tamper-evident action logging |
| ACCESS.md | Who can invoke this agent |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
