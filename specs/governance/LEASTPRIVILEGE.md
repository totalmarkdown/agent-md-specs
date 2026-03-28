---
spec_name: LEASTPRIVILEGE.md
spec_version: 0.1.0
category: Governance
domain: leastprivilegemd.dev
priority: Very High
volume: "Vol 14 — Agent Identity, Accountability & Compliance"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
---

# LEASTPRIVILEGE.md

**Category:** Governance
**Domain:** leastprivilegemd.dev
**Priority:** Very High
**Version:** 0.1.0

### Purpose
Defines the agent's privilege management following zero-trust
principles. Privileges are granted just-in-time, scoped to
specific tasks, and automatically revoked after use. Answers
the NIST questions: "How do we establish 'least privilege' for
an agent?" and "How can zero-trust principles be applied?"

Traditional access control grants persistent privileges.
LEASTPRIVILEGE.md inverts this — the agent starts with minimal
permissions and temporarily escalates only when a specific task
requires it, with automatic de-escalation when the task completes.

### Scope Boundary

This spec governs **dynamic privilege management at runtime** using
zero-trust principles.

- LEASTPRIVILEGE.md defines **runtime privilege escalation and de-escalation**
- DELEGATION.md defines **the authority chain that grants baseline privileges**
- PERMISSIONS.md defines **the static resource access list**
- ENFORCEMENT.md defines **how privilege policies are enforced and drift is detected**

### When to Create This File
Required for any agent with access to resources beyond its
minimum operational needs. Critical for agents operating in
production environments, handling sensitive data, or interacting
with external systems. Essential in multi-agent architectures
where privilege boundaries prevent lateral movement.

### Spec

```markdown
---
agent_name: string
version: semver
zero_trust_mode: enabled | advisory
baseline_privilege_level: minimal | reduced | standard
auto_deescalation: enabled | disabled
privilege_audit_frequency: per_action | per_task | hourly
created: date
updated: date
---

# [Agent Name] — Least Privilege Policy

## Zero Trust Posture Statement

This agent assumes no implicit trust. Every action, every
resource access, and every inter-agent communication is
verified independently. Trust is:
- Never inherited from context or environment
- Never assumed from prior successful interactions
- Never granted permanently — always time-bound
- Never broader than the specific task requires

## Privilege Baseline

Minimum permissions when the agent is idle (no active task).
These map to the static resource grants declared in PERMISSIONS.md
(see PERMISSIONS.md for the full resource access list that defines
baseline boundaries).

| Resource | Idle Permission | Justification |
|----------|----------------|---------------|
| Own configuration files | read-only | Self-awareness |
| WAKEUP.md / SLEEP.md | read + execute | Lifecycle management |
| MEMORY.md | read-only | Context loading |
| ESCALATION.md | read + execute | Always able to escalate |
| AUDITTRAIL.md | append-only | Always able to log |
| HEALTHCHECK.md | read + execute | Self-monitoring |
| All other resources | no access | Denied until escalated |

### What the Agent CANNOT Do at Baseline
- Read or write any external data store
- Send any external communication
- Access any API or tool
- Modify any configuration
- Create, update, or delete any resource
- Communicate with other agents (except escalation)

## Just-In-Time Escalation

When a task requires privileges beyond baseline, the agent
requests temporary escalation. The authority to grant these
privileges flows from DELEGATION.md.

### Escalation Request Format
```yaml
privilege_request:
  request_id: [UUID]
  agent_id: [from ID.md]
  timestamp: [ISO-8601]
  task_ref: [task or intent ID that requires this privilege]  # See INTENT.md — intent must be declared before requesting escalation
  requested_privileges:
    - resource: [target resource]
      permission: [read / write / delete / execute / admin]
      justification: [why this specific privilege is needed]
  requested_duration: [seconds — max allowed for this privilege]
  requested_scope: [narrow description of what will be accessed]
  fallback_if_denied: [what agent does if escalation is refused]
```

### Approval Authority

| Privilege Level | Approver | Latency |
|----------------|----------|---------|
| Read non-sensitive | Automatic (policy engine) | < 1 second |
| Read sensitive | Automatic with logging | < 1 second |
| Write non-sensitive | Automatic (policy engine) | < 1 second |
| Write sensitive | Human review required | [timeout period] |
| Delete any | Human review required | [timeout period] |
| External communication | Policy engine + logging | < 5 seconds |
| Financial transaction | Human review required | [timeout period] |
| Admin / elevated | Human review required | [timeout period] |

### Escalation Grant Format
```yaml
privilege_grant:
  grant_id: [UUID]
  request_id: [reference to request]
  granted_at: [ISO-8601]
  expires_at: [ISO-8601 — hard expiry]
  granted_privileges:
    - resource: [target resource]
      permission: [what was granted — may be narrower than requested]
      scope: [exact scope — may be narrower than requested]
  approved_by: [policy engine / human identity]
  conditions: [any additional constraints]
```

## Automatic De-escalation

Privileges are revoked automatically. The agent does not
retain elevated permissions between tasks.

### De-escalation Triggers

| Trigger | Behavior | Timing |
|---------|----------|--------|
| Action completed | Revoke privilege for that action | Immediate |
| Time-to-live expired | Revoke regardless of task state | At `expires_at` |
| Task completed | Revoke all task-scoped privileges | Immediate |
| Error or failure | Revoke and log failure context | Immediate |
| Session end | Revoke everything to baseline | At SLEEP.md | <!-- Session-scoped privileges expire with the session; see SESSION.md -->
| Anomaly detected | Revoke to baseline + escalate | Immediate |

### De-escalation Procedure
1. Privilege grant marked as `revoked` with revocation timestamp
2. Resource access physically removed (not just policy-flagged)
3. Any cached credentials or tokens for that resource destroyed
4. De-escalation logged to AUDITTRAIL.md
5. Agent returns to baseline privilege set

### Failure to De-escalate
If automatic de-escalation fails (see MONITOR.md for drift
detection that catches stale elevated privileges):
1. Alert sent to MONITOR.md
2. Agent enters degraded mode (all actions paused)
3. Human intervention required to reset privilege state
4. Incident logged for post-mortem review

## Unknown Action Policy

When the agent encounters an action it has no explicit
policy for (see INTENT.md for how the agent declares
what it plans to do before acting):

| Policy | Behavior | When to Use |
|--------|----------|-------------|
| `deny_and_log` | Refuse action, log to AUDITTRAIL.md (see AUDITTRAIL.md) | Default — production |
| `request_escalation` | Pause and ask for guidance | When human is available |
| `attempt_with_sandbox` | Try in isolated sandbox first | Testing / non-production only |

**Active policy:** `[deny_and_log]`

### Unknown Action Handling
```
1. Action not found in allowed actions list
2. Log: {action, context, agent_state, timestamp}
3. Apply active unknown action policy
4. If deny_and_log: return "action not permitted" to caller
5. If request_escalation: trigger ESCALATION.md Level 2
6. Record for policy review (should this action be explicitly allowed or denied?)
```

## Privilege Audit

Every privilege grant, use, and revocation is logged:

```yaml
privilege_audit_entry:
  entry_id: [UUID]
  timestamp: [ISO-8601]
  event_type: [request / grant / use / deny / revoke / expire]
  grant_id: [reference to privilege grant]
  resource: [what resource was involved]
  permission: [what permission level]
  outcome: [success / failure / denied]
  duration_seconds: [how long the privilege was active]
  actions_taken: [count of actions performed with this privilege]
  audit_ref: [AUDITTRAIL.md entry ID]
```

### Audit Alerts

| Pattern | Alert Level | Action |
|---------|------------|--------|
| Privilege used but no action taken | Warning | Review for unnecessary grants |
| Privilege used beyond original justification | Critical | Revoke + escalate |
| Repeated escalation requests for same resource | Info | Consider baseline adjustment |
| Privilege active longer than [threshold] | Warning | Force de-escalation |
| Denied request followed by alternative approach | Critical | Review for circumvention |

## Privilege Profiles

Pre-defined privilege sets for common task types:

### Profile: Read-Only Research
```yaml
profile: read_only_research
privileges:
  - resource: "[data sources]"
    permission: read
    duration: 3600
restrictions:
  - no write access to any resource
  - no external communication
  - no tool execution
```

### Profile: Content Creation
```yaml
profile: content_creation
privileges:
  - resource: "[content workspace]"
    permission: read-write
    duration: 7200
  - resource: "[reference materials]"
    permission: read
    duration: 7200
restrictions:
  - write only to designated workspace
  - no delete permissions
  - no external API calls
```

### Profile: External Integration
```yaml
profile: external_integration
privileges:
  - resource: "[specific external API]"
    permission: execute
    duration: 1800
  - resource: "[credentials vault]"
    permission: read
    duration: 300
restrictions:
  - only specified API endpoints
  - credentials read once then discarded from memory
  - all requests logged with full payload
```

## Review and Adjustment

| Review Type | Frequency | Reviewer | Purpose |
|------------|-----------|----------|---------|
| Baseline adequacy | Monthly | [security role] | Is baseline too broad or too narrow? |
| Escalation patterns | Weekly | [automated] | Are the same privileges requested repeatedly? |
| De-escalation compliance | Daily | [automated] | Are privileges being properly revoked? |
| Profile accuracy | Quarterly | [security role] | Do profiles match actual usage? |
```


```
## Example Use Cases

**Enterprise:** A report generation agent starts each session with read-only access to its own config files, requests just-in-time write access to the analytics database only for the duration of the report task, and has that privilege automatically revoked the moment the report is saved.

**Multi-Agent Fleet:** When an agent in a fleet is compromised by a prompt injection attempt, zero-trust privilege boundaries prevent lateral movement because each agent holds only baseline permissions and cannot access resources belonging to peer agents without a fresh, scoped privilege grant.

**Regulated Industry:** A PCI-DSS compliant payment processing agent receives read access to the credentials vault for exactly 300 seconds to retrieve a payment gateway token, after which the privilege is physically revoked and any cached credentials are destroyed from memory.

## Related Specs

| Spec | Relationship |
|------|-------------|
| PERMISSIONS.md | Static resource access control |
| ACCESS.md | Who can invoke this agent |
| DELEGATION.md | Authority chain and authorization |
| AUDITTRAIL.md | Tamper-proof action logging |
| INTENT.md | Pre-action declaration and confidence scoring |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
