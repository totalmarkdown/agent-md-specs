---
spec_name: INTENT.md
spec_version: 0.1.0
category: Governance
domain: intentmd.dev
priority: Very High
volume: "Vol 14 — Agent Identity, Accountability & Compliance"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
---

# INTENT.md

**Category:** Governance
**Domain:** intentmd.dev
**Priority:** Very High
**Version:** 0.1.0

### Purpose
Defines how an agent declares the intent of its actions before,
during, and after execution. Enables pre-action authorization,
dynamic policy evaluation, and post-hoc auditability. Answers
the NIST question: "How might an agent convey the intent of
its actions?"

Every action an agent takes should be preceded by a declared
intent — a structured statement of what it plans to do, why,
and what it expects to happen. This creates a reviewable record
that separates "what the agent meant to do" from "what actually
happened," enabling meaningful accountability.

### Scope Boundary

This spec governs **pre-action intent declaration and confidence assessment**.

- INTENT.md defines **what the agent plans to do before doing it** (runtime, per-action)
- DELEGATION.md defines **who authorized the agent to act** (static, pre-deployment)
- LEASTPRIVILEGE.md defines **what privileges are currently active** (runtime, per-action)
- AUDITTRAIL.md defines **what actually happened after the fact** (post-action)
- ENFORCEMENT.md defines **how intent declarations are verified against policy** (continuous)

INTENT.md does NOT define permissions or policy — it defines the agent's
declared plan of action, which is then evaluated against LEASTPRIVILEGE
and ENFORCEMENT before execution proceeds.

### When to Create This File
Required for any agent performing actions with side effects —
writes, deletes, communications, transactions, API calls.
Critical for agents operating with elevated privileges or
handling sensitive data. Essential in regulated environments
where pre-action justification is required.

### Spec

````markdown
---
agent_name: string
version: semver
intent_logging: enabled | disabled
auto_proceed_threshold: number    # Confidence above which agent proceeds
human_review_threshold: number    # Confidence below which human reviews
created: date
updated: date
---

# [Agent Name] — Intent Declaration Protocol

## Intent Declaration Format

Every action MUST be preceded by an intent declaration:

```yaml
intent:
  id: [UUID — unique per declaration]
  timestamp: [ISO-8601]
  action_type: [category from Intent Categories]
  target_resource: [what will be affected]
  reason: [why this action is being taken]
  expected_outcome: [what should happen if successful]
  confidence_level: [0.0 - 1.0]
  reversible: [true / false]
  delegation_ref: [DELEGATION.md ID, if acting on behalf of]  # See DELEGATION.md
  session_id: [from SESSION.md — binds intent to active session]  # See SESSION.md
  parent_intent: [UUID of parent intent, if part of a chain]
```

### Example Declaration
```yaml
intent:
  id: "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
  timestamp: "2025-07-15T14:32:00Z"
  action_type: write
  target_resource: "database://production/users/profile"
  reason: "User requested email address update via support ticket #4521"
  expected_outcome: "Email field updated, confirmation sent to old and new address"
  confidence_level: 0.95
  reversible: true
  delegation_ref: "delegation_abc123"
  parent_intent: null
```

## Intent Categories

| Category | Description | Default Risk | Examples |
|----------|------------|-------------|----------|
| `read` | Accessing data without modification | Low | Query database, read file, fetch API |
| `write` | Modifying existing data | Medium | Update record, edit file, patch config |
| `delete` | Removing data or resources | High | Drop table, remove file, revoke access |
| `create` | Creating new data or resources | Medium | Insert record, create file, provision |
| `communicate` | Sending messages to humans or systems | Medium | Send email, post to Slack, webhook |
| `transact` | Financial or contractual actions | Very High | Process payment, sign agreement |
| `delegate` | Passing authority to another agent | High | Sub-delegate per DELEGATION.md |
| `escalate` | Elevating to higher authority | Low | Trigger ESCALATION.md protocol |
| `external_call` | Invoking external service or API | Medium | Third-party API, external webhook |

## Confidence Level

The agent's confidence that the intended action is correct and
appropriate, expressed as a float from 0.0 to 1.0.

### Confidence Thresholds

| Range | Label | Policy |
|-------|-------|--------|
| > 0.9 | High confidence | Proceed autonomously, log intent |
| 0.7 - 0.9 | Moderate confidence | Proceed, log intent with rationale flag |
| 0.5 - 0.7 | Low confidence | Pause, request human confirmation |
| < 0.5 | Very low confidence | Halt, escalate per ESCALATION.md (see ESCALATION.md for level definitions) |

### Confidence Factors
Confidence should account for:
- Clarity of the triggering instruction
- Precedent (has this exact action succeeded before?)
- Scope of impact (smaller scope = higher confidence)
- Reversibility (reversible actions tolerate lower confidence)
- Data freshness (stale context reduces confidence)

**Important:** Confidence scores SHOULD be derived from external
evaluation systems, deterministic checks, or probabilistic ensembles
— not solely from the agent's own self-assessment. _See ATTESTATION.md
for identity binding that ensures non-repudiation of confidence claims._ LLMs are known to
produce miscalibrated confidence estimates. Where the agent generates
its own confidence score, an external validator or calibration layer
SHOULD verify the score before it is used for authorization decisions.

## Expected Impact Assessment

Before proceeding, classify the expected impact:

| Dimension | Assessment | Value |
|-----------|-----------|-------|
| Reversibility | Can this be undone? (see LIMITS.md for hard irreversibility constraints) | [fully / partially / irreversible] |
| Data sensitivity | What data is touched? | [public / internal / confidential / restricted] |
| Financial impact | Cost or value at risk | [$0 / $1-100 / $100-10k / $10k+] |
| Blast radius | How many users/systems affected (see CIRCUITBREAKER.md for blast radius thresholds) | [single / team / org / public] |
| Time pressure | How urgent is this action | [none / hours / minutes / immediate] |

### Impact Score
```
impact_score = max(reversibility_risk, data_risk, financial_risk, blast_risk)
```

Impact score determines whether confidence threshold is raised:
- Low impact: standard thresholds apply
- Medium impact: thresholds shift up by 0.1
- High impact: thresholds shift up by 0.2
- Very high impact: always requires human review regardless of confidence

## Fallback Intent

What the agent does if the primary action fails or is denied:

```yaml
fallback:
  on_denial: [wait_and_retry / escalate / abandon / use_alternative]
  on_failure: [retry_N_times / escalate / rollback / log_and_continue]
  alternative_action: [description of fallback approach, if any]
  max_retries: [number]
  retry_delay_seconds: [number]
  escalation_after_failure: [true / false]
```

### Fallback Rules
- Fallback actions MUST have their own intent declarations
- Fallback scope MUST be <= original intent scope
- Failed intent + fallback intent form a linked audit chain
- After [max_retries] failures: mandatory escalation

## Human Review Threshold

Matrix combining confidence and impact to determine when
human approval is required:

|  | Low Impact | Medium Impact | High Impact | Very High Impact |
|--|-----------|--------------|------------|-----------------|
| **High confidence (>0.9)** | Proceed | Proceed | Review | Review |
| **Moderate (0.7-0.9)** | Proceed | Review | Review | Review |
| **Low (0.5-0.7)** | Confirm | Review | Review | Halt |
| **Very low (<0.5)** | Confirm | Halt | Halt | Halt |

**Proceed:** Execute autonomously, log intent
**Confirm:** Notify human, proceed after [timeout] if no objection
**Review:** Pause, wait for explicit human approval
**Halt:** Stop, escalate per ESCALATION.md Level 3

## Intent Logging

Every intent declaration is logged regardless of outcome.
These records feed into AUDITTRAIL.md as the permanent history of
what the agent planned versus what actually occurred.

```yaml
intent_log_entry:
  intent_id: [UUID]
  declared_at: [ISO-8601]
  decision: [proceed / confirm / review / halt]
  decision_reason: [confidence x impact result]
  outcome: [executed / denied / failed / rolled_back / pending]
  completed_at: [ISO-8601 or null]
  actual_result: [what actually happened]
  deviation: [true / false — did outcome match expected_outcome?]
  audit_ref: [AUDITTRAIL.md entry ID]
```

### Deviation Handling
When `deviation: true` (outcome differs from expected):
1. Log the deviation with details
2. Assess whether deviation is benign or harmful
3. If harmful: trigger rollback if reversible, escalate if not
4. Flag for pattern analysis (repeated deviations indicate drift)

## Intent-Action Binding

Each audit trail entry includes a cryptographic link to the
original intent declaration, proving the action was pre-declared:

```
intent_hash: SHA-256(intent_declaration_json)
action_hash: SHA-256(action_details_json)
binding: {intent_hash, action_hash, timestamp, agent_signature}
```

This binding ensures:
- No action exists without a prior intent declaration
- Intent declarations cannot be retroactively modified
- The audit trail proves intent preceded action
- Third parties can verify the intent-action link

## Multi-Step Intent

For complex tasks requiring multiple actions:

```yaml
intent_chain:
  chain_id: [UUID]
  steps:
    - intent_id: [UUID — step 1]
      depends_on: null
    - intent_id: [UUID — step 2]
      depends_on: [step 1 UUID]
    - intent_id: [UUID — step 3]
      depends_on: [step 2 UUID]
  rollback_policy: [all_or_nothing / partial / best_effort]
```

Each step is independently declared, reviewed, and logged.
Chain failure triggers rollback per `rollback_policy`.
````

## Example Use Cases

**Enterprise:** Before updating a customer's email address in the CRM, a support agent declares its intent with the specific record ID, reason (support ticket #4521), expected outcome, and 0.95 confidence, creating a reviewable pre-action record that the compliance team can audit months later.

**Multi-Agent Fleet:** An orchestrator agent declares a multi-step intent chain for a data migration task, where each step (extract, transform, load) has its own intent declaration with dependency links, and the entire chain rolls back automatically if the final validation step fails.

**Regulated Industry:** A loan underwriting agent must declare intent before accessing each applicant's credit file, with the intent-action binding cryptographically proving that every data access was pre-declared and justified, satisfying FCRA audit requirements.

## Related Specs

| Spec | Relationship |
|------|-------------|
| AUDITTRAIL.md | Tamper-proof action logging |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| LIMITS.md | Hard constraints and safety boundaries |
| DELEGATION.md | Authority chain and authorization |
| LEASTPRIVILEGE.md | Dynamic zero-trust privilege management |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
