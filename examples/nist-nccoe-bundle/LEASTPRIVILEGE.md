---
agent_name: "Atlas"
version: "2.1.0"
org: "Acme Corp"
privilege_model: "deny-by-default"
jit_enabled: true
created: "2025-11-01"
updated: "2026-03-15"
---

# Atlas -- Least Privilege

## Privilege Model

Atlas operates under a deny-by-default privilege model. Every action Atlas
can take must be explicitly authorized. Any action not listed in the baseline
grants is denied and logged as a policy violation.

## Baseline Privileges

These privileges are active for every Atlas session without additional
approval. They represent the minimum required to perform routine financial
analysis work.

### Data Read Access

| System | Scope | Authentication | Purpose |
|--------|-------|----------------|---------|
| Acme Financial DB | `finance.*` schemas, read-only | mTLS + SPIFFE SVID | Historical and current-period financial data |
| Bloomberg API | Equities, fixed income, FX, economic indicators | OAuth 2.0 + API key | Market data for forecasts and benchmarks |
| Finance Document Repository | `/finance/templates/*`, `/finance/policies/*` | mTLS + SPIFFE SVID | Report templates and methodology docs |

### Compute Access

| Resource | Scope | Purpose |
|----------|-------|---------|
| Report generator | Execute only | Format data into Acme reporting templates |
| Forecast engine | Execute only | Run ARIMA and exponential smoothing models |
| tmpfs scratch volume | Read/write, 512 MB max | Intermediate calculations during session |

### Network Access

| Destination | Protocol | Purpose |
|-------------|----------|---------|
| financial-db.acme.corp:5432 | PostgreSQL over mTLS | Database queries |
| bloomberg-api.acme.corp:8443 | HTTPS (proxy) | Market data retrieval |
| mail-relay.acme.corp:587 | SMTP over TLS | Report delivery (JIT only) |

## Just-in-Time Escalation

Certain actions require temporary privilege escalation. These privileges are
not active by default and must be explicitly requested and approved before use.

### Email Delivery

- **Trigger:** Atlas needs to send a completed report to the distribution list
- **Approval required:** CFO Sarah Chen via FIDO2 key on compliance portal
- **Approval latency:** Synchronous, blocks until approved or denied
- **Privilege granted:** SMTP send to addresses on approved distribution list
- **Duration:** Single use. Privilege revoked immediately after the email is sent.
- **Audit:** Approval event, send event, and de-escalation event all logged

### Extended Data Access

- **Trigger:** Ad-hoc analysis request requires data outside `finance.*` schemas
- **Approval required:** CFO + Chief Compliance Officer dual approval
- **Privilege granted:** Read-only access to specified additional schema
- **Duration:** Single session only. Privilege does not persist across sessions.
- **Restrictions:** PII-containing tables are excluded even under escalation

## De-escalation

Escalated privileges are revoked under the following conditions:

1. **Single-use completion:** Privilege used once, then immediately revoked
2. **Session end:** All escalated privileges revoked at session termination
3. **Timeout:** If an escalated privilege is not used within 5 minutes of
   grant, it is automatically revoked
4. **Manual revocation:** CFO or compliance officer can revoke at any time

## Unknown Actions

If Atlas encounters a situation requiring an action not covered by baseline
or JIT escalation grants:

1. The action is denied
2. The denial is logged with full context (what was attempted and why)
3. Atlas informs the requesting user that the action is outside its authority
4. Atlas suggests the appropriate human contact for the requested action
5. The session continues for remaining authorized work
