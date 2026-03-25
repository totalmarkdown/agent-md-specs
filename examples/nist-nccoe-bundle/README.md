# Example Bundle: Atlas — Enterprise Financial Agent (NIST-Aligned)

This bundle demonstrates how agent-md-specs configures a production
financial analysis agent with full NIST NCCoE alignment, including
the complete accountability chain from human delegation to
tamper-proof audit trail.

## Why This Bundle Matters

This is the reference example for the NIST NCCoE submission. It shows
how core specs work together to govern a real enterprise agent
operating under strict regulatory requirements (SOX, GDPR, SOC2).

## Agent Profile

- **Name:** Atlas v2.1
- **Role:** Financial analysis agent
- **Organization:** Acme Corp (fictional)
- **Delegated by:** CFO Sarah Chen
- **Model:** Claude Sonnet 4
- **Purpose:** Generate quarterly financial reports and forecasts

## Files in This Bundle

| File | What It Configures | NIST Question |
|------|-------------------|---------------|
| WHOAMI.md | Agent identity | Identification |
| DELEGATION.md | Authority chain from CFO | Authorization (delegation) |
| ATTESTATION.md | SPIFFE/X.509 verification | Authentication |
| SESSION.md | 30-min task boundary | Identification (ephemeral) |
| LEASTPRIVILEGE.md | Zero-trust privileges | Authorization (least privilege) |
| INTENT.md | Pre-action declarations | Authorization (intent) |
| PROMPTSHIELD.md | Injection defenses | Prompt injection |
| PROVENANCE.md | Data source lineage | Data flow tracking |
| SHAREDCONTEXT.md | Team shared memory | Memory governance |
| MEMORYSAFETY.md | Memory poisoning defense | Memory security |
| AUDITTRAIL.md | Hash-chain audit log | Auditing/non-repudiation |
| CIRCUITBREAKER.md | Failure containment | Resilience |
| CONSENT.md | Employee consent record | Compliance (GDPR) |
| ESCALATION.md | 4-level escalation path | Human-in-the-loop |
| LIMITS.md | Hard stops | Safety boundaries |
| PERMISSIONS.md | Resource access control | Authorization |
| ENFORCEMENT.md | Compliance verification | Cross-cutting |
| SOUL.md | Professional persona | Agent behavior |

## The Accountability Chain in Action

This bundle implements the complete accountability chain:
1. CFO Sarah Chen delegates read-only financial analysis authority
2. Employee consent covers AI-assisted analysis (form FIN-AI-001)
3. Atlas identifies as spiffe://acme.corp/finance/agents/atlas
4. X.509 certificate proves identity with 90-day rotation
5. Session scoped to 30 minutes, 50 actions max
6. Baseline: read financial databases only
7. Intent: "read Q3 revenue data" (confidence 0.95)
8. Input scanned for SQL injection and financial-domain attacks
9. Data sourced from Bloomberg (trusted) and internal DB (trusted)
10. Shared context validated, canary entries intact
11. Memory sanitization gateway active
12. [ACTION: generate report]
13. Circuit breaker monitoring (3 consecutive failures = halt)
14. Hash-chain audit entry signed with Atlas's X.509 cert
15. Enforcement verified, no drift detected
