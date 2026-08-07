---
spec_name: MEMORYSAFETY.md
spec_version: 0.1.0
category: Security
priority: Very High
tier: core
---

# [REPLACE THIS — Agent Name] — Memory Safety

<!-- Defense against memory poisoning, context manipulation, and recall attacks -->

## Threat Model
- **Memory type:** [REPLACE THIS — long-term | session | shared | all]
- **Attack vectors:** [REPLACE THIS — e.g. poisoned context injection, recall manipulation, phantom memories]
- **Trust boundary:** [REPLACE THIS — what separates trusted from untrusted memory]

## Write Protection
<!-- Controls on what gets written into agent memory -->
1. [REPLACE THIS — e.g. All memory writes must include source attribution]
2. [REPLACE THIS — e.g. No memory write from untrusted input without sanitization]
3. [REPLACE THIS — e.g. Memory entries cannot overwrite entries from higher-trust sources]

## Read Validation
<!-- How the agent validates memories before acting on them -->
- **Staleness check:** [REPLACE THIS — reject memories older than X | always check timestamp]
- **Source verification:** [REPLACE THIS — verify origin agent ID before trusting recall]
- **Consistency check:** [REPLACE THIS — cross-reference with other sources | none]

## Isolation
| Memory Zone | Accessible By | Quarantine on Suspicion |
|-------------|---------------|------------------------|
| [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS — true | false] |
| [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |

## Poisoning Response
- **On detection:** [REPLACE THIS — quarantine entry | purge entry | halt and escalate]
- **Notification:** [REPLACE THIS — who gets alerted]
- **Recovery:** [REPLACE THIS — restore from backup | rebuild from sources | manual review]

## Integrity Checks
- **Hash stored memories:** [REPLACE THIS — true | false]
- **Periodic audit:** [REPLACE THIS — frequency of memory integrity scans]
- **Diff detection:** [REPLACE THIS — how unauthorized changes are spotted]

## Related Specs
- MEMORY.md: [REPLACE THIS — path]
- SHAREDCONTEXT.md: [REPLACE THIS — path]
- PROMPTSHIELD.md: [REPLACE THIS — path]
