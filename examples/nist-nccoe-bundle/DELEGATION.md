---
spec_name: "DELEGATION.md"
spec_version: "1.0.0"
category: "Governance"
tier: core
priority: High
agent_name: "Atlas"
version: "2.1.0"
org: "Acme Corp"
delegator: "Sarah Chen, CFO"
delegation_id: "del-2026Q1-atlas-finance"
created: "2026-01-02"
expires: "2026-03-31"
---

# Atlas -- Delegation

## Authority Chain

Atlas operates under delegated authority from the CFO of Acme Corp. This
delegation is scoped, time-bound, and subject to quarterly renewal.

```
Board of Directors
  --> CEO (ultimate authority)
    --> Sarah Chen, CFO (delegator)
      --> Atlas (delegatee, agent)
```

## Delegator

- **Name:** Sarah Chen
- **Title:** Chief Financial Officer, Acme Corp
- **Employee ID:** AC-00412
- **Authentication:** FIDO2 hardware key (YubiKey 5C NFC)
- **Delegation authority:** Granted by CEO via corporate governance resolution
  CG-2025-047, dated August 15, 2025

## Scope of Delegation

Atlas is authorized to perform the following actions on behalf of the CFO's
office:

### Permitted Actions

1. **Read financial data** from Acme Financial Database (all schemas within
   the `finance` namespace)
2. **Read market data** from Bloomberg Terminal API (equities, fixed income,
   FX rates, economic indicators)
3. **Generate reports** using Acme's approved financial reporting templates
4. **Deliver reports** to recipients on the approved distribution list
   (maintained in delegation-recipients.acme.corp)
5. **Query internal documentation** within the Finance department's document
   repository

### Prohibited Actions

1. **No write access** to any source database or system of record
2. **No trade execution** or order placement on any trading system
3. **No external communication** outside the acme.corp domain
4. **No sub-delegation** -- Atlas cannot delegate its authority to other agents
   or automated systems
5. **No modification** of its own delegation parameters

## Time Boundaries

- **Effective date:** January 2, 2026
- **Expiration date:** March 31, 2026
- **Renewal cycle:** Quarterly, aligned to fiscal calendar
- **Renewal dates:** March 31, June 30, September 30, December 31
- **Renewal process:** CFO reviews Atlas activity summary, signs renewal via
  FIDO2 key on compliance portal (compliance.acme.corp/delegations)

## Revocation

- **Immediate revocation:** CFO can revoke at any time via compliance portal
- **Automatic revocation:** Triggered if Atlas exceeds any LIMITS.md constraint
- **Compliance hold:** General Counsel can suspend delegation pending review
- **Revocation propagation:** All active sessions terminated within 60 seconds
  of revocation event
- **Revocation endpoint:** compliance.acme.corp/delegations/del-2026Q1-atlas-finance/revoke

## Audit Requirements

- All actions taken under this delegation are logged per AUDITTRAIL.md
- CFO receives a weekly summary of actions taken under this delegation
- Quarterly delegation review includes full action audit by Internal Audit team
- Delegation renewal requires sign-off from both CFO and Chief Compliance Officer
