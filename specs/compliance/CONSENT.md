---
spec_name: CONSENT.md
spec_version: 0.1.0
category: Compliance
domain: consentmd.dev
priority: High
volume: "Vol 16 — Resilience & Consent"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
spec_type: static
---


# CONSENT.md

**Category:** Compliance
**Domain:** consentmd.dev
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose
Defines the full lifecycle of end-user consent — collection, recording,
verification, and revocation of permission for agent actions that affect
users or process personal data. Ensures agents operate only with explicit,
informed, and freely given user permission, as required by GDPR Article 7,
CCPA Section 1798.120, and EU AI Act Article 13.

At fleet scale, CONSENT.md enables:
- Centralized proof that every user interaction has a valid consent basis
- Automated consent verification before any data processing action
- Immediate, system-wide revocation propagation across multi-agent systems
- Regulatory audit readiness across jurisdictions with differing consent standards

### Scope Boundary

- CONSENT.md defines **what the user agreed to** and how to revoke it
- PRIVACY.md defines **how personal data is handled** after consent is given
- PII.md defines **what constitutes personal data** subject to consent
- DELEGATION.md defines **who authorized the agent** (organizational authority)
- ESCALATION.md defines **what happens** when consent cannot be verified

CONSENT.md is about **end-user permission**. DELEGATION.md is about
**organizational authority**. Both are required — delegation without
consent is unauthorized processing; consent without delegation is
an agent acting outside its mandate.

### When to Create This File
Required for any agent that processes personal data, interacts with
end users, makes decisions affecting individuals, operates in GDPR/CCPA/COPPA
jurisdictions, shares user data with third parties or other agents, or
profiles/tracks user behavior. If none apply, document exemption in COMPLIANCE.md.

### Spec

````markdown
---
agent_name: string
agent_id: string                # Must match WHOAMI.md agent_id
version: semver
consent_authority: string       # Legal entity responsible for consent management
dpo_contact: string             # Data Protection Officer contact
jurisdictions: list             # [GDPR, CCPA, COPPA, HIPAA, etc.]
consent_store: string           # database | encrypted_file | consent_platform
last_audit: date
spec_version: string
---

# [Agent Name] — Consent Configuration

## Consent Requirements

Valid consent under this configuration requires ALL of the following:

| Requirement | Description |
|-------------|-------------|
| **Clear description** | Plain-language explanation of what the agent will do |
| **Data accessed** | Specific categories of personal data to be processed |
| **Processing purpose** | Why each data category is needed — no blanket permissions |
| **Retention period** | How long data will be kept, per category |
| **Sharing scope** | Who else will receive the data (agents, services, third parties) |
| **Revocation method** | How to withdraw consent, in equally clear terms |
| **Agent identity** | Which agent(s) will process the data (ref WHOAMI.md) |

### GDPR Article 7 Compliance
Consent must be:
- **Freely given** — not conditional on unrelated service access
- **Specific** — granular per processing purpose, not bundled
- **Informed** — user understands what they are agreeing to
- **Unambiguous** — requires a clear affirmative action

The controller must demonstrate that consent was given.

---

## Consent Collection

### Acceptable Methods
| Method | Valid | Notes |
|--------|-------|-------|
| Explicit opt-in checkbox (unchecked by default) | Yes | User must actively check |
| Typed confirmation ("I agree") | Yes | Must follow clear disclosure |
| Digital signature | Yes | Strongest evidence |
| Verbal confirmation (recorded) | Yes | Must be transcribed and stored |
| Double opt-in (email confirmation) | Yes | Recommended for sensitive data |

### NOT Acceptable — Invalid Consent
| Method | Why Invalid |
|--------|-------------|
| Pre-checked boxes | Not freely given (GDPR Recital 32) |
| Silence or inactivity | Not an unambiguous indication |
| Bundled with terms of service | Not specific or freely given |
| "By continuing, you agree..." | Not an affirmative action |
| Implied from prior relationship | Not informed or specific |
| Opt-out only (must act to refuse) | Not freely given |

### Timing
- Consent MUST be collected **before** the action, never retroactively
- Missing or expired consent: **halt and escalate** per ESCALATION.md
- Re-consent required when purpose or data categories change materially

### Age Verification
| Regulation | Age Threshold | Requirement |
|-----------|---------------|-------------|
| **COPPA** | Under 13 | Verifiable parental consent required |
| **GDPR Art 8** | Under 16 (or 13-16 per member state) | Parental authorization required |
| **CCPA** | Under 16 | Opt-in required (parental for under 13) |

If age cannot be verified: apply most restrictive threshold (COPPA — 13).

---

## Consent Record

Every consent event produces a record conforming to this schema:

```yaml
consent:
  consent_id: "uuid-v4"                  # Globally unique consent identifier
  user_id: "pseudonymized-string"        # Never store raw PII as identifier
  agent_id: "uuid matching WHOAMI.md"    # Agent that will process data
  granted_at: "ISO-8601 with timezone"   # When consent was given (UTC)
  expires_at: "ISO-8601 with timezone"   # Hard expiry — re-consent required after
  scope:                                 # What was consented to
    - "email_notifications"
    - "usage_analytics"
    - "personalization"
  data_categories:                       # What data types are covered
    - "email_address"
    - "usage_patterns"
    - "preferences"
  collection_method: "explicit_opt_in"   # enum: explicit_opt_in | double_opt_in |
                                         #       digital_signature | verbal_recorded
  evidence: "sha256:hash-of-consent-ui-state-and-user-action"
  evidence_storage: "path-or-uri"
  ip_address_hash: "sha256:..."
  consent_version: "semver"
  revoked: false
  revoked_at: null
```

### Record Integrity
- Consent records are append-only — never modified, only superseded
- Each record is hashed and linked to AUDITTRAIL.md; all consent
  grants, revocations, and scope changes are logged there (see AUDITTRAIL.md)
- Records survive for retention period plus [2 years] for regulatory proof
- Storage encrypted at rest (ref PRIVACY.md)

---

## Consent Verification

Before any consented action, the agent MUST verify:

### Verification Checklist
1. **Active consent exists** for the specific processing purpose
2. **Consent has not expired** (`expires_at` > current time)
3. **Consent has not been revoked** (`revoked` == false)
4. **Consent scope covers the action** (action is within `scope` array)
5. **Data categories match** (data being processed is within `data_categories`)
6. **Consent version is current** (consent text has not materially changed)

### Verification Failure Handling
| Failure Reason | Action |
|---------------|--------|
| No consent record found | HALT — do not process. Escalate per ESCALATION.md |
| Consent expired | HALT — request re-consent before proceeding |
| Consent revoked | HALT — delete data per PRIVACY.md, confirm to user |
| Scope mismatch | HALT — request additional consent for new scope |
| Version outdated | WARN — request re-consent at next interaction |

### Verification Logging
Every verification (pass or fail) is logged to AUDITTRAIL.md:
```yaml
verification:
  verification_id: "uuid-v4"
  consent_id: "referenced consent record"
  agent_id: "agent performing the check"
  result: "valid | expired | revoked | scope_mismatch | not_found"
  timestamp: "ISO-8601"
```

---

## Consent Revocation

### User Rights
- Revoke **at any time**, without penalty or justification
- Available through **same channel** as collection, plus at least one more
- Must be **as easy as** granting consent (GDPR Art 7(3))

### Revocation Process
1. User submits revocation request
2. Agent verifies user identity (same standard as consent collection)
3. Consent record updated: `revoked: true`, `revoked_at: [timestamp]`
4. **Immediate cessation** of all processing under revoked consent
5. Data deletion initiated per PRIVACY.md, including purging
   user data from agent memory stores (see MEMORY.md) and
   shared state (see SHAREDCONTEXT.md)
6. Confirmation to user within [24 hours]: what was revoked,
   data deletion timeline, any data retained under separate legal basis
7. Revocation event logged to AUDITTRAIL.md

### Revocation Propagation
| Component | Propagation SLA |
|-----------|----------------|
| This agent | Immediate (< 1 minute) |
| Sub-agents (ref SHAREDCONTEXT.md) | Within [5 minutes] |
| Third-party data processors | Within [24 hours] |
| Backup systems | Next scheduled purge cycle |

### Data After Revocation
- Consented data: delete per PRIVACY.md (see PRIVACY.md for deletion procedures and SLAs)
- Legally required data (audit logs, legal holds): retain with documentation
- Anonymized/aggregated: may retain if truly irreversible
- Derived data (trained models): assess per MEMORYSAFETY.md

---

## Consent for Multi-Agent Systems

For team composition and agent relationships, see TEAM.md. For
shared state propagation of consent scope, see SHAREDCONTEXT.md.

### Disclosure Requirements
- Users informed which **specific agents** process their data (ref WHOAMI.md)
- Users notified when **new agents** join the processing chain
- New agent with materially different capabilities triggers re-consent
- Consent must cover all agents in a team roster (see TEAM.md for team composition)

### Sub-Delegation of Consent
| Rule | Requirement |
|------|-------------|
| Scope inheritance | Sub-agent consent scope must be a **strict subset** of parent |
| User visibility | User can query which agents have access at any time |
| Chain depth | Maximum [3] agents in any consent delegation chain |
| New agent notification | User notified within [48 hours] of new agent addition |
| Shared context | Consent scope propagated via SHAREDCONTEXT.md |

### Multi-Agent Consent Record
```yaml
multi_agent_consent:
  primary_consent_id: "uuid-v4"
  agent_chain:
    - agent_id: "orchestrator-01"
      role: "data_controller"
      consent_scope: ["full scope"]
    - agent_id: "analyzer-02"
      role: "data_processor"
      consent_scope: ["usage_analytics"]
  chain_verified_at: "ISO-8601"
  chain_hash: "sha256:..."
```

---

## Compliance Mapping

| Regulation | Requirement | How This Spec Addresses |
|-----------|-------------|------------------------|
| **GDPR Art 7** | Freely given, specific, informed, unambiguous consent | Consent Requirements enforces all four; invalid methods listed (see GDPR.md for full GDPR configuration) |
| **GDPR Art 7(3)** | Withdraw consent any time, as easy as giving | Revocation via same-channel + additional, no dark patterns |
| **GDPR Art 17** | Right to erasure when consent withdrawn | Revocation triggers deletion per PRIVACY.md with SLAs |
| **GDPR Art 8** | Child's consent (age 16, or 13 per member state) | Age Verification with per-regulation thresholds |
| **CCPA 1798.120** | Right to opt out of sale/sharing | Explicit opt-in required; revocation at any time |
| **CCPA 1798.135** | Limit use of sensitive personal information | Granular scope and data_categories per consent |
| **EU AI Act Art 13** | Transparency — inform users of AI interaction | Agent identity disclosure via WHOAMI.md |
| **EU AI Act Art 14** | Human oversight of high-risk AI | Verification failure halts and escalates to human |
| **COPPA** | Verifiable parental consent under 13 | Parental consent required; strictest threshold default |
| **HIPAA** | Authorization for PHI use/disclosure | Data categories in consent record; evidence preserved |

````

## Example Use Cases

**Enterprise:** An e-commerce platform's personalization agent collects granular, purpose-specific consent (product recommendations, email marketing, usage analytics) and immediately halts all processing for a user who revokes any single scope, propagating the revocation to all downstream agents within 5 minutes.

**Multi-Agent Fleet:** A multi-agent customer service platform uses CONSENT.md to ensure every agent in the processing chain inherits a strict subset of the original consent scope, automatically notifying users when a new specialist agent is added to their support ticket's processing chain.

**Regulated Industry:** A children's education platform enforces COPPA-compliant parental consent collection with double opt-in verification before any agent can process data from users under 13, with age-verification checks applied at every session start.

## Related Specs

| Spec | Relationship |
|------|-------------|
| PRIVACY.md | Data privacy handling |
| PII.md | Personal data classification |
| GDPR.md | GDPR compliance requirements |
| CCPA.md | CCPA compliance requirements |
| DELEGATION.md | Authority chain and authorization |
| AUDITTRAIL.md | Tamper-proof action logging |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| SHAREDCONTEXT.md | Multi-agent shared memory pool |
| MEMORYSAFETY.md | Memory poisoning defense |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*

