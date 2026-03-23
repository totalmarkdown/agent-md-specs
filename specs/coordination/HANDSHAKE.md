---
spec_name: HANDSHAKE.md
spec_version: 0.1.0
category: Coordination
domain: handshakemd.dev
priority: High
volume: "Vol 6 — Hierarchy Completion & Identity Anchors"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# HANDSHAKE.md

**Category:** Coordination
**Domain:** handshakemd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Defines the protocol for establishing trusted connections 
between agents — how two agents verify each other's identity, 
exchange credentials, and establish a secure working relationship 
before sharing sensitive data or delegating tasks. The agent 
equivalent of a TLS handshake.

### Spec

```markdown
---
agent_name: string
version: semver
handshake_protocol: string  # simple | signed | mutual-tls | did-based
trust_model: string         # open | allowlist | verified-only
---

# [Agent Name] — Handshake Protocol

## Trust Model
**Model:** [open | allowlist | verified-only]

- **Open:** Accept connections from any agent
- **Allowlist:** Only connect with agents in NETWORK.md
- **Verified-only:** Only connect with cryptographically verified agents

## Handshake Steps

### Step 1: Introduction
Initiating agent sends:
```json
{
  "from_agent_id": "uuid",
  "from_agent_name": "string",
  "whoami_url": "URL to WHOAMI.md",
  "protocol_version": "1.0",
  "intent": "task-delegation | data-request | collaboration",
  "timestamp": "ISO-8601",
  "nonce": "random-string"
}
```

### Step 2: Verification (if required)
Receiving agent checks:
- [ ] Agent ID format valid
- [ ] WHOAMI.md accessible and consistent
- [ ] Agent on allowlist (if allowlist mode)
- [ ] Cryptographic signature valid (if verified-only mode)
- [ ] Intent is acceptable

### Step 3: Response
Receiving agent responds:
```json
{
  "accepted": true,
  "session_token": "temporary-token",
  "session_expires": "ISO-8601",
  "my_agent_id": "uuid",
  "my_whoami_url": "URL",
  "capabilities": ["list", "of", "what", "I", "can", "do"],
  "constraints": "any limits on this session"
}
```

### Step 4: Acknowledgment
Initiating agent acknowledges and begins work.

## Session Management
- **Session duration:** [X minutes]
- **Renewal:** [automatic | manual]
- **Revocation:** [how to end a session early]

## Verification Methods
| Method | Security level | When to use |
|--------|---------------|-------------|
| ID-only | Low | Internal trusted networks |
| WHOAMI.md check | Medium | General agent-to-agent |
| Cryptographic signature | High | Cross-org, financial, sensitive |
| DID-based | Very high | Public, untrusted environments |

## Rejection Protocol
If handshake is rejected:
```json
{
  "accepted": false,
  "reason": "not-on-allowlist | verification-failed | capacity | other",
  "retry_after": "ISO-8601 or null",
  "suggest_alternative": "agent-id or null"
}
```

## Logging
All handshakes logged with:
- Initiating agent ID, timestamp, intent, outcome
- Rejection reasons (for security monitoring)
- Session tokens (hashed, not plaintext)
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
