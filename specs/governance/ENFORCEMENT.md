---
spec_name: ENFORCEMENT.md
spec_version: 0.1.0
category: Governance
domain: enforcementmd.dev
priority: Very High
volume: "Vol 14 — Agent Identity, Accountability & Compliance"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
spec_type: static
---


# ENFORCEMENT.md

**Category:** Governance
**Domain:** enforcementmd.dev
**Priority:** Very High
**Version:** 0.1.0 **Type:** Static

### Purpose
Defines how an agent's configuration specs are verified at build
time, runtime, and post-hoc. The meta-spec that answers: "How do
we know this agent actually follows its own documentation?"

Without ENFORCEMENT.md, agent specs are aspirational — they describe
intended behavior but provide no mechanism to verify compliance.
This spec closes the gap between declaration and reality by defining
validation rules, drift detection, and compliance attestation.

### Scope Boundary

This spec is a **meta-specification** that defines how all other specs
are verified. It does not define policies itself — it defines the
verification framework.

- ENFORCEMENT.md defines **how specs are validated and enforced** (the "how")
- LIMITS.md, PERMISSIONS.md, DELEGATION.md define **what is enforced** (the "what")
- AUDITTRAIL.md defines **the record of enforcement actions** (the "proof")

Note: ENFORCEMENT.md describes a declarative verification framework.
Actual enforcement requires a compliant runtime — such as an API gateway,
policy engine (e.g., OPA/Rego), or agent orchestration platform — that
reads these specs and implements the enforcement matrix.

### When to Create This File
Required for any agent operating in production or handling sensitive
tasks. Critical in regulated environments where compliance must be
demonstrable. Essential in multi-agent systems where trust between
agents depends on verified configuration. Should be one of the first
governance specs created after PERMISSIONS.md and LIMITS.md.

### Spec

````markdown
---
agent_name: string
version: semver
enforcement_mode: strict | advisory | disabled
validator_tool: string              # Tool or script that runs validation
last_validation: datetime           # ISO-8601
last_validation_result: pass | fail
drift_detection_frequency: string   # cron expression or interval
compliance_attestation_frequency: string
created: date
updated: date
---

# [Agent Name] — Enforcement Protocol

## Pre-Deployment Validation

Before this agent is deployed or updated, the following
validation MUST pass. A reference implementation is available
at [agent-md-validator](https://github.com/totalmarkdown/agent-md-validator).

### Validation Run
```yaml
validation:
  tool: [validator CLI / CI script / policy engine]
  run_at: [ISO-8601]
  run_by: [CI/CD pipeline / human / orchestrator]
  agent_version: [semver being validated]
  results:
    total_specs: [number]
    passed: [number]
    failed: [number]
    skipped: [number]
    warnings: [number]
```

### Spec Validation Matrix

| Spec | Required | Validation Method | Result |
|------|----------|-------------------|--------|
| ID.md | Yes | UUID format valid, unique | [pass/fail/skip] |
| WHOAMI.md | Yes | All required fields present | [pass/fail/skip] |
| PERMISSIONS.md | Yes | No contradictions with LIMITS.md | [pass/fail/skip] |
| LIMITS.md | Yes | At least [N] limits defined | [pass/fail/skip] |
| ESCALATION.md | Yes | All levels defined, contacts valid | [pass/fail/skip] |
| DELEGATION.md | If delegated | Principal exists, scope defined | [pass/fail/skip] |
| BUDGET.md | If financial | Limits set, currency valid | [pass/fail/skip] |
| INTENT.md | If autonomous | Thresholds defined, categories set | [pass/fail/skip] |
| LEASTPRIVILEGE.md | If privileged | Baseline defined, de-escalation set | [pass/fail/skip] |
| SESSION.md | If ephemeral | Destruction policy defined | [pass/fail/skip] |
| [Additional specs] | [Yes/No/If] | [method] | [result] |

### Minimum Requirements for Deployment
- All `Required: Yes` specs must pass validation
- Zero `fail` results on required specs
- All `Required: If [condition]` specs validated when condition is true
- Validation timestamp < [N hours] old at deployment time
- Validator tool version matches expected version

### CI/CD Integration
```yaml
pipeline_stage: pre-deploy
validation_command: [command to run validator]
blocking: true                   # Deployment halts on failure
artifact: validation-report.json # Stored with deployment artifact
notification_on_failure: [contact / channel]
```

## Runtime Enforcement Matrix

How each core spec is enforced during agent operation.
The specs below define the policies that this matrix enforces
(see LIMITS.md for hard boundaries, BUDGET.md for financial constraints).

| Spec | Enforcement Method | Violation Action |
|------|-------------------|-----------------|
| PERMISSIONS.md | Policy engine intercepts every action | Block action, log violation |
| LIMITS.md | Hard-coded checks, cannot be bypassed | Refuse + escalate immediately |
| BUDGET.md | Running counter, checked pre-action | Block action exceeding budget |
| ESCALATION.md | Trigger conditions monitored continuously | Auto-escalate on match |
| DELEGATION.md | Delegation ID verified per action | Block if expired/revoked |
| LEASTPRIVILEGE.md | Privilege state checked pre-action (see LEASTPRIVILEGE.md) | Deny if insufficient privilege |
| INTENT.md | Intent declaration required pre-action | Block action without intent |
| PROMPTSHIELD.md | Prompt injection detection pre-action (see PROMPTSHIELD.md) | Block + quarantine on detection |
| QUOTA.md | Rate counters, checked pre-action | Throttle or block at limit |

### Enforcement Levels

| Level | Behavior | When |
|-------|----------|------|
| `block` | Action prevented, error returned | Clear violation, high risk |
| `warn_and_proceed` | Action allowed, warning logged | Minor violation, low risk |
| `log_only` | Action allowed, violation recorded | Advisory mode, monitoring |
| `quarantine` | Action halted, agent paused | Repeated violations, pattern detected |

### Active Enforcement Level: `[block]`

## Declaration-Only Specs

Some specs are descriptive rather than enforceable at runtime.
These require alternative verification:

| Spec | Verification Method | Frequency |
|------|-------------------|-----------|
| SOUL.md | Human review of agent outputs | [quarterly] |
| VOICE.md | Tone analysis of communications | [monthly] |
| VALUES.md | Behavioral pattern review | [quarterly] |
| PERSONA.md | Consistency scoring | [monthly] |
| ORIGIN.md | Static — validated once at creation | Once |

### Alternative Verification Methods
- **Human review:** Designated reviewer samples agent outputs
- **Behavioral analysis:** Automated analysis of action patterns
- **Peer review:** Other agents assess consistency (if multi-agent)
- **User feedback:** Satisfaction signals correlated with spec claims

## Behavioral Drift Detection

Monitoring for divergence between declared configuration and
actual behavior over time.

Drift detection integrates with MONITOR.md for continuous
runtime observation and CIRCUITBREAKER.md for automated
response when drift exceeds safe thresholds.

### Monitoring Configuration
```yaml
drift_detection:
  frequency: [cron expression — e.g., "0 */6 * * *"]
  lookback_window: [hours — e.g., 24]
  alert_threshold: [percentage — e.g., 5% deviation triggers alert]
  auto_remediation: [enabled / disabled]
```

### What Constitutes Drift

| Category | Drift Example | Severity |
|----------|--------------|----------|
| Permission drift | Agent accessing resources not in PERMISSIONS.md | Critical |
| Budget drift | Spending rate exceeding BUDGET.md projections | High |
| Escalation drift | Agent handling situations it should escalate | Critical |
| Behavioral drift | Response patterns diverging from VOICE.md | Medium |
| Privilege drift | Elevated privileges held longer than specified | High |
| Scope drift | Agent taking actions outside declared scope | Critical |

### Drift Response Protocol
1. **Detect:** Automated monitoring flags drift pattern
2. **Classify:** Severity assigned based on category
3. **Alert:** Notification sent per severity level
   - Critical: Immediate alert to security + agent pause
   - High: Alert to ops team within [N minutes]
   - Medium: Queued for next review cycle
4. **Investigate:** Root cause analysis
5. **Remediate:** Apply correction
   - Auto-remediation (if enabled): Reset to declared config
   - Manual remediation: Human reviews and adjusts
6. **Document:** Drift incident logged to AUDITTRAIL.md

### Auto-Remediation Policy
```yaml
auto_remediation:
  enabled: [true / false]
  allowed_actions:
    - revoke_excess_privileges     # Return to LEASTPRIVILEGE.md baseline
    - reset_budget_counters        # Recount from AUDITTRAIL.md
    - force_deescalation           # Drop to baseline privilege
  prohibited_actions:
    - modify_spec_files            # Never self-modify declared config
    - override_limits              # Never relax LIMITS.md
    - suppress_alerts              # Never silence drift alerts
```

## Audit Verification

Ensuring the audit trail itself has not been tampered with
(see AUDITTRAIL.md for the event schema and tamper-resistance mechanisms):

### External Anchor
```yaml
audit_anchor:
  type: [blockchain / external hash store / signed ledger]
  endpoint: [URL or service reference]
  anchor_frequency: [every N entries / hourly / daily]
  last_anchor: [ISO-8601]
  last_anchor_hash: [SHA-256 of anchored state]
```

### Third-Party Verification
```yaml
verification:
  endpoint: [URL for external verification service]
  api_key_ref: [reference in SECRETS.md — not the actual key]
  verification_frequency: [daily / weekly]
  last_verified: [ISO-8601]
  last_result: [verified / tampered / unreachable]
```

### Tamper Detection
- Audit entries include hash chain (each entry hashes previous)
- Hash chain verified at `anchor_frequency`
- Break in hash chain triggers:
  1. Immediate alert to security team
  2. Agent operations suspended
  3. Full audit reconstruction from external anchor
  4. Incident response per ESCALATION.md Level 3

### Chain Integrity Check
```yaml
chain_integrity:
  frequency: [hourly / daily]
  last_check: [ISO-8601]
  entries_verified: [count]
  result: [intact / broken_at_entry_N / pending]
```

## Compliance Attestation Report

Periodic report summarizing enforcement status:

### Report Configuration
```yaml
attestation_report:
  generation_frequency: [daily / weekly / monthly]
  format: [json + markdown]
  signed_by: [ATTESTATION.md credential reference]  # See ATTESTATION.md for signing credentials
  distribution: [who receives the report]
  retention: [how long reports are kept]
```

### Report Contents
```yaml
attestation:
  report_id: [UUID]
  generated_at: [ISO-8601]
  period: [start — end ISO-8601]
  agent_id: [from ID.md]
  agent_version: [semver]

  validation_summary:
    last_pre_deploy_validation: [ISO-8601]
    result: [pass / fail]
    specs_validated: [count]

  runtime_enforcement:
    total_actions: [count]
    actions_blocked: [count]
    actions_warned: [count]
    violations_by_spec:
      PERMISSIONS.md: [count]
      LIMITS.md: [count]
      BUDGET.md: [count]

  drift_detection:
    checks_performed: [count]
    drift_incidents: [count]
    drift_incidents_resolved: [count]
    drift_incidents_open: [count]

  audit_integrity:
    chain_checks_performed: [count]
    chain_intact: [true / false]
    external_anchors_verified: [count]

  overall_compliance: [compliant / non-compliant / degraded]
  attestation_signature: [cryptographic signature]
```

## Enforcement Exceptions

Documented exceptions to standard enforcement:

| Exception | Justification | Approved By | Expires |
|-----------|--------------|------------|---------|
| [spec:rule] | [why exception is needed] | [human approver] | [date] |

Exceptions are:
- Always time-bound (no permanent exceptions)
- Always approved by a human (never self-approved)
- Always logged to AUDITTRAIL.md
- Reviewed at each compliance attestation
````

## Example Use Cases

**Enterprise:** A CI/CD pipeline runs the agent-md-validator against every agent configuration before deployment, blocking any release where required specs like PERMISSIONS.md or LIMITS.md fail validation checks.

**Multi-Agent Fleet:** A fleet management platform performs drift detection every six hours across 200 agents, automatically revoking excess privileges from any agent whose runtime behavior diverges from its declared PERMISSIONS.md and generating a weekly compliance attestation report for the security team.

**Regulated Industry:** A HIPAA-compliant healthcare platform generates tamper-evident compliance attestation reports with cryptographic signatures, anchoring audit hashes to an external ledger so regulators can independently verify that patient data access patterns match declared policies.

## Related Specs

| Spec | Relationship |
|------|-------------|
| AUDITTRAIL.md | Tamper-evident action logging |
| ATTESTATION.md | Identity verification and credential lifecycle |
| MONITOR.md | Observability and alerting |
| HEALTHCHECK.md | Liveness and readiness checks |
| LIMITS.md | Hard constraints and safety boundaries |
| PERMISSIONS.md | Static resource access control |
| BUDGET.md | Cost controls and spending limits |
| DELEGATION.md | Authority chain and authorization |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
