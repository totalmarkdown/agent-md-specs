---
spec_name: ICE.md
spec_version: 0.1.0
category: Safety
domain: icemd.dev
priority: High
volume: "Vol 7 — Inner Life & Lifecycle Rituals"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: core
spec_type: static
---


> **Canonical repository:**
> [totalmarkdown/ice.md](https://github.com/totalmarkdown/ice.md)
> This copy is included in agent-md-specs for cross-reference.
> For contributions to this specific spec, use the canonical repo.

# ICE.md

**Category:** Safety
**Domain:** icemd.dev
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose
The break-glass file. What this agent does — and what humans 
should do — when multiple things are failing simultaneously 
and there is no time to think carefully.

Different from:
- ESCALATION.md — decision escalation (planned)
- REPAIR.md — technical recovery (methodical)
- SELFHEALING.md — proactive health (automated)
- PANIC.md — reflexive immediate response (see PANIC.md)

ICE.md is the calm, pre-written emergency protocol.
Written when things are fine, to be read when they're not.

### Spec

````markdown
---
agent_name: string
version: semver
primary_emergency_contact: string
secondary_emergency_contact: string
last_drilled: date          # When emergency protocol was last tested
---

# [Agent Name] — In Case of Emergency

## READ THIS FIRST
If you are reading this because something is wrong:
1. **Stop** — do not take further actions until you've read this
2. **Assess** — which emergency type is this? (see below)
3. **Act** — follow the protocol for that type
4. **Communicate** — notify the right people
5. **Document** — write down what happened

---

## Emergency Types

### TYPE 1: Agent is producing harmful outputs
**Signs:** Outputs that are dangerous, offensive, or clearly wrong at scale  
**Immediate action:** 
```bash
# Stop the agent immediately
[kill command]
# Do NOT let it continue while investigating
```
**Then:** Preserve all logs, do not delete anything  
**Notify:** [Primary contact] immediately  
**Do NOT restart** until root cause is identified

---

### TYPE 2: Agent is offline / not responding
**Signs:** No heartbeat, tasks not completing, no response to health check  
**Immediate action:**
```bash
# Check if process is running
[status command]
# Check logs for last known state
[log command]
```
**If safe to restart:** See REBOOT.md  
**If cause unknown:** Do NOT restart, notify [contact] first  
**Notify:** [Contact] if offline > [N] minutes

---

### TYPE 3: Data breach or security incident
**Signs:** Unexpected data access, credentials exposed, unusual external calls  
**Immediate action:**
- Disconnect agent from all external services NOW
- Do NOT attempt to "fix" — preserve evidence
- Rotate all credentials listed in IDENTITY.md
**Notify:** [Security contact] within [N] minutes  
**Do NOT:** Delete logs, attempt to cover, restart until cleared

---

### TYPE 4: Runaway spending / resource exhaustion
**Signs:** Budget alerts, unexpected API charges, system resource maxed (see CIRCUITBREAKER.md)  
**Immediate action:**
```bash
# Hard stop all agent processes
[kill command]
# Check current spend
[cost check command]
```
**Notify:** [Finance contact]  
**Before restarting:** Identify what caused the runaway

---

### TYPE 5: Agent is in an infinite loop
**Signs:** Task started hours ago, no completion, escalating resource use  
**Immediate action:**
```bash
# Force stop
[kill -9 command]
```
**Preserve:** The last task input that triggered the loop  
**Notify:** [Technical contact]

---

## Emergency Contacts

| Who | Contact | Available | For |
|-----|---------|-----------|-----|
| [Primary] | [contact] | 24/7 | All emergencies |
| [Secondary] | [contact] | Business hours | Backup |
| [Technical] | [contact] | [hours] | Type 2, 3, 5 |
| [Security] | [contact] | 24/7 | Type 3 |
| [Finance] | [contact] | Business hours | Type 4 |

## After the Emergency
Once the immediate situation is stable:
1. Write an incident report: what happened, when, impact, resolution
2. Update this file if the emergency type wasn't covered
3. Notify relevant contacts per ESCALATION.md
4. Run a post-mortem within [N] days
4. Update REPAIR.md and SELFHEALING.md with learnings
5. Schedule a drill of this protocol: [cadence]

## Emergency Drill
This protocol was last tested: [date]  
Next scheduled drill: [date]  
How to run a drill: [instructions]
````

## Example Use Cases

**Enterprise:** A production data pipeline agent begins generating corrupted output at scale, and the on-call engineer follows the TYPE 1 protocol to immediately kill the process, preserve logs, and notify the data platform lead before any downstream systems consume bad data.

**Multi-Agent Fleet:** A fleet orchestrator detects runaway API spending from a malfunctioning agent that entered an infinite retry loop, follows the TYPE 4 protocol to hard-stop the agent, check cumulative costs, and identify the root cause before allowing any fleet member to restart.

**Regulated Industry:** A securities trading agent's health check stops responding during market hours, and the operations team follows the TYPE 2 protocol to diagnose whether the outage is safe to recover from or requires regulatory notification before restart.

## Related Specs

| Spec | Relationship |
|------|-------------|
| CIRCUITBREAKER.md | Failure containment and blast radius |
| DELEGATION.md | Authority chain and authorization |
| ENFORCEMENT.md | Policy verification and compliance |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| LIMITS.md | Hard constraints and safety boundaries |
| PANIC.md | Panic-mode emergency response |
| PERMISSIONS.md | Static resource access control |
| REPAIR.md | Recovery and self-healing procedures |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
