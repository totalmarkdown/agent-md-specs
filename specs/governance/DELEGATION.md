---
spec_name: DELEGATION.md
spec_version: 0.1.0
category: Governance
domain: delegationmd.dev
priority: Very High
volume: "Vol 14 — Agent Identity, Accountability & Compliance"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
---

# DELEGATION.md

**Category:** Governance
**Domain:** delegationmd.dev
**Priority:** Very High
**Version:** 0.1.0

### Purpose
Defines the chain of delegated authority from a human principal to
this agent, including scope constraints, time limits, and revocation.
Ensures every autonomous action can be traced back to a specific
human authorization, answering the NIST questions: "How do we handle
delegation of authority for 'on behalf of' scenarios?" and "How do
we bind agent identity with human identity?"

Without DELEGATION.md, an agent operating autonomously has no
provable link between its actions and the human who authorized them.
This spec creates that link — scoped, time-bound, and revocable.

### Scope Boundary

This spec governs **who authorized this agent and with what constraints**.
It defines the authority chain from human to agent.

- DELEGATION.md defines **who granted what authority** (static, pre-deployment)
- LEASTPRIVILEGE.md defines **what privileges are active right now** (dynamic, runtime)
- PERMISSIONS.md defines **what resources can be accessed** (static, pre-deployment)
- ENFORCEMENT.md defines **how all of the above are verified** (meta, continuous)
- SESSION.md defines **the ephemeral runtime boundary** for a single task

### When to Create This File
Required for any agent that acts on behalf of a human or organization.
Critical when agents send communications, make purchases, modify data,
or interact with external systems using delegated credentials.
Mandatory in multi-agent systems where sub-delegation may occur.

### Spec

```markdown
---
agent_name: string
version: semver
delegation_id: string           # Unique ID for this delegation grant
delegating_principal: string    # Human who grants authority
delegation_granted: datetime    # ISO-8601
delegation_expires: datetime    # ISO-8601 — hard expiry
delegation_status: active | suspended | revoked | expired
---

# [Agent Name] — Delegation of Authority

## Delegating Principal

| Field | Value |
|-------|-------|
| Name | [Human full name] |
| Role | [Title / organizational role] |
| Organization | [Org name] |
| Auth method | [OAuth 2.0 / SSO / manual approval / signed cert] |
| Identity anchor | [email / employee ID / DID] |
| WHOAMI.md ref | [path or URL to principal's identity record] |

The delegating principal is the human ultimately accountable for
all actions this agent performs under this delegation grant.

## Delegation Scope

Explicit allow-list of delegated actions. Anything not listed
here is NOT delegated and must be escalated per ESCALATION.md.

### Allowed Actions
- [ ] [Action category]: [specific scope]
  - Example: `send_email`: only to @[domain], max [N] per day
- [ ] [Action category]: [specific scope]
  - Example: `create_ticket`: only in [project], priority <= medium
- [ ] [Action category]: [specific scope]
  - Example: `read_database`: [schema].[table], SELECT only

### Explicitly Denied Actions
Even if technically possible, these are never delegated:
- [Action]: [reason]
- [Action]: [reason]

## Delegation Constraints

| Constraint | Type | Value | Enforcement |
|-----------|------|-------|-------------|
| Time bound | expires_at | [ISO-8601 datetime] | Hard cutoff — all actions halt |
| Action count | max_actions | [number] | Counter resets: [never / daily / per-session] |
| Budget cap | max_spend | $[amount] [currency] | Cumulative across delegation lifetime |
| Rate limit | max_actions_per_hour | [number] | Rolling window |
| Geographic | allowed_regions | [region list] | IP / locale enforcement |
| Data scope | allowed_data | [classification level] | Max sensitivity: [public / internal / confidential] |

### Constraint Violation Behavior
When any constraint is hit:
1. Current action is halted (not rolled back unless irreversible)
2. Violation logged to AUDITTRAIL.md with constraint details
3. Agent enters reduced-privilege mode (LEASTPRIVILEGE.md baseline)
4. Escalation triggered per ESCALATION.md Level 3
5. Delegation status set to `suspended` pending review

## Sub-Delegation Policy

| Field | Value |
|-------|-------|
| Sub-delegation allowed | [yes / no] |
| Maximum depth | [number — e.g., 2 means agent can delegate to one sub-agent] |
| Scope narrowing | [strict — sub-delegation must be strictly narrower] |
| Sub-delegate approval | [automatic / requires principal approval] |
| Sub-delegate registry | [path to registry of active sub-delegations] |

### Sub-Delegation Rules
- Sub-delegated scope MUST be a strict subset of parent scope
- Sub-delegated expiry MUST be <= parent delegation expiry
- Sub-delegated budget MUST be <= remaining parent budget
- Each sub-delegation creates its own DELEGATION.md
- Sub-delegation chain logged to AUDITTRAIL.md

## Consent Record

How the delegating principal authorized this delegation:

| Field | Value |
|-------|-------|
| Consent type | [OAuth token / signed document / MCP authorization / manual approval] |
| Consent reference | [token ID / document hash / approval ticket] |
| Consent timestamp | [ISO-8601] |
| Consent expiry | [ISO-8601 — may differ from delegation expiry] |
| Consent revocation URL | [endpoint to revoke consent] |
| Consent witness | [system or person that recorded consent] |

### OAuth 2.0 On-Behalf-Of (if applicable)
```
token_type: Bearer
scope: [granted OAuth scopes]
resource: [target resource server]
assertion: [original user token reference]
```

### MCP Authorization (if applicable)
```
mcp_server: [server identifier]
granted_tools: [list of MCP tools delegated]
context_scope: [conversation / session / persistent]
```

## Revocation

### Automatic Expiry
Delegation expires automatically at `delegation_expires`.
No action required — agent loses all delegated privileges.
In-flight actions at expiry: [complete-current / halt-immediately]

### Manual Revocation
| Field | Value |
|-------|-------|
| Revocation endpoint | [URL or mechanism] |
| Who can revoke | [principal / principal's manager / security team] |
| Revocation latency | [max time from revocation request to enforcement] |
| Notification on revoke | [who is notified — agent, principal, security] |

### In-Flight Action Handling on Revocation
- **Reversible actions:** Roll back if possible, log rollback
- **Irreversible actions:** Complete if safe, flag for review
- **Long-running tasks:** Checkpoint and halt, preserve state
- **Sub-delegations:** Cascade revocation to all sub-delegates

## Accountability Binding

How actions are traced back through the delegation chain
to the authorizing human:

1. Every action includes `delegation_id` in its audit entry
2. Audit entry references `delegating_principal` identity
3. If sub-delegated: full chain recorded
   `human → agent_A (delegation_123) → agent_B (delegation_456)`
4. AUDITTRAIL.md entries are append-only and tamper-evident
5. Accountability chain is verifiable by third parties

### Attribution Format
```
action_by: [agent UUID from ID.md]
on_behalf_of: [delegating principal identity]
delegation_id: [this delegation's unique ID]
delegation_chain: [ordered list if sub-delegated]
timestamp: [ISO-8601]
action_hash: [SHA-256 of action details]
```

## On-Behalf-Of Protocol Reference

| Protocol | Used | Reference |
|----------|------|-----------|
| OAuth 2.0 Token Exchange (RFC 8693) | [yes/no] | [config location] |
| OAuth 2.0 On-Behalf-Of | [yes/no] | [config location] |
| MCP Delegation | [yes/no] | [MCP server config] |
| SPIFFE/SPIRE | [yes/no] | [trust domain] |
| Custom delegation protocol | [yes/no] | [documentation URL] |

## Delegation Review Schedule

| Review type | Frequency | Reviewer |
|------------|-----------|----------|
| Scope appropriateness | [weekly / monthly] | [role] |
| Constraint adequacy | [monthly / quarterly] | [role] |
| Usage audit | [daily / weekly] | [automated + role] |
| Full delegation renewal | [at expiry] | [delegating principal] |
```

### Cross-References
- **WHOAMI.md** — Identity of the agent receiving delegation
- **PERMISSIONS.md** — Static permission boundaries (delegation operates within these)
- **ESCALATION.md** — What happens when delegation scope is exceeded
- **AUDITTRAIL.md** — Where delegation chain and actions are logged
- **ACCESS.md** — Technical access controls that implement delegation scope
- **REPORTSTO.md** — Organizational hierarchy context for delegation authority

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
