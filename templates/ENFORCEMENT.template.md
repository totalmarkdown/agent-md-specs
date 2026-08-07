---
spec_name: ENFORCEMENT.md
spec_version: 0.1.0
category: Governance
priority: Very High
tier: core
---

# [REPLACE THIS — Agent Name] — Spec Enforcement

<!-- How compliance with agent specs is verified and enforced at runtime -->

## Enforcement Mode
- **Mode:** [REPLACE THIS — strict | advisory | audit-only]
- **Enforcer:** [REPLACE THIS — self | orchestrator | sidecar | external validator]
- **Fail behavior:** [REPLACE THIS — block action | warn and continue | log only]

## Specs Enforced
<!-- Which spec files are actively checked -->

| Spec | Enforcement | Check Frequency | Last Verified |
|------|-------------|-----------------|---------------|
| LIMITS.md | [REPLACE THIS — runtime | pre-deploy | manual] | [REPLACE THIS] | [REPLACE THIS] |
| PERMISSIONS.md | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |
| GUARDRAILS.md | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |
| [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |

## Validation Rules
1. [REPLACE THIS — e.g. All spec files must have valid YAML frontmatter]
2. [REPLACE THIS — e.g. Agent actions must not exceed PERMISSIONS.md grants]
3. [REPLACE THIS — e.g. Budget usage must stay within BUDGET.md thresholds]

## Violation Handling
| Severity | Response | Notify | Auto-fix |
|----------|----------|--------|----------|
| Critical | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |
| Warning | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |
| Info | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |

## Spec Drift Detection
- **Drift check:** [REPLACE THIS — how often specs are re-validated against runtime behavior]
- **Schema validation:** [REPLACE THIS — tool or script that validates spec format]
- **Reconciliation:** [REPLACE THIS — what happens when runtime diverges from spec]

## Related Specs
- AUDITTRAIL.md: [REPLACE THIS — path]
- CIRCUITBREAKER.md: [REPLACE THIS — path]
- GUARDRAILS.md: [REPLACE THIS — path]
