---
spec_name: INTENT.md
spec_version: 0.1.0
category: Governance
priority: Very High
tier: core
---

# [REPLACE THIS — Agent Name] — Intent Declaration

<!-- Pre-action intent declaration: agent states what it will do before doing it -->

## Intent Protocol
- **Declaration required:** [REPLACE THIS — always | high-risk only | configurable]
- **Declaration format:** [REPLACE THIS — structured JSON | natural language | both]
- **Approval required:** [REPLACE THIS — always | risk-based | never (log only)]

## Intent Schema
<!-- Template for what an intent declaration must contain -->
```yaml
intent:
  action: "[REPLACE THIS — verb: read | write | delete | call | deploy]"
  target: "[REPLACE THIS — resource being acted on]"
  reason: "[REPLACE THIS — why this action is necessary]"
  reversible: [REPLACE THIS — true | false]
  risk_level: [REPLACE THIS — low | medium | high | critical]
  estimated_impact: "[REPLACE THIS — what changes as a result]"
```

## Risk Thresholds
| Risk Level | Approval | Wait Time | Notify |
|------------|----------|-----------|--------|
| low | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |
| medium | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |
| high | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |
| critical | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |

## Pre-Action Checklist
1. [REPLACE THIS — e.g. Verify target resource exists]
2. [REPLACE THIS — e.g. Confirm rollback path available]
3. [REPLACE THIS — e.g. Check rate limits not exceeded]

## On Rejection
- **Behavior:** [REPLACE THIS — abort | propose alternative | escalate]
- **Retry allowed:** [REPLACE THIS — true | false]
- **Logged to:** [REPLACE THIS — audit trail location]

## Related Specs
- AUDITTRAIL.md: [REPLACE THIS — path]
- GUARDRAILS.md: [REPLACE THIS — path]
- ESCALATION.md: [REPLACE THIS — path]
