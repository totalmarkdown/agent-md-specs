---
spec_name: DELEGATION.md
spec_version: 0.1.0
category: Identity
domain: specmd.dev
priority: P1
tier: core
---

# [REPLACE THIS — Agent Name] — Authority Delegation

<!-- Chain of trust: who delegated authority to this agent and what was granted -->

## Delegation Chain
<!-- Ordered from root authority to this agent -->
1. **Root:** [REPLACE THIS — human or system that holds original authority]
2. **Delegated to:** [REPLACE THIS — intermediary agent or role, if any]
3. **Delegated to:** [REPLACE THIS — this agent's ID]

## Granted Authority
<!-- What this agent is authorized to do on behalf of the delegator -->
- [REPLACE THIS — specific action or scope, e.g. "approve PRs in repo X"]
- [REPLACE THIS — specific action or scope]
- [REPLACE THIS — specific action or scope]

## Constraints
- **Max depth:** [REPLACE THIS — how many levels deep this agent can sub-delegate]
- **Can sub-delegate:** [REPLACE THIS — true | false]
- **Sub-delegation restrictions:** [REPLACE THIS — what cannot be passed further down]
- **Time-bound:** [REPLACE THIS — expiry date or "indefinite"]

## Revocation
- **Revoked by:** [REPLACE THIS — who can revoke this delegation]
- **Revocation method:** [REPLACE THIS — API call | config change | manual]
- **On revocation:** [REPLACE THIS — stop immediately | finish current task | escalate]

## Proof
- **Delegation token:** [REPLACE THIS — JWT, signed document, or "implicit"]
- **Verification:** [REPLACE THIS — how a receiving agent verifies this delegation]

## Accountability
- **Actions logged under:** [REPLACE THIS — delegator's ID | this agent's ID | both]
- **Liability:** [REPLACE THIS — who is responsible for actions taken under delegation]

## Related Specs
- ID.md: [REPLACE THIS — path]
- PERMISSIONS.md: [REPLACE THIS — path]
- LEASTPRIVILEGE.md: [REPLACE THIS — path]
