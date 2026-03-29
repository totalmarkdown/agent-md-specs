---
spec_name: SANDBOX.md
spec_version: 0.1.0
category: Security
domain: sandboxmd.dev
priority: Medium
volume: "Vol 12 — Fleet Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---


# SANDBOX.md

**Category:** Security
**Domain:** sandboxmd.dev
**Priority:** Medium
**Version:** 0.1.0 **Type:** Static

### Purpose
Isolation and containment configuration for an agent —
what it is and isn't allowed to do at the OS/container level.
Critical for agents that execute code, run subprocesses,
or need to be isolated from the host system.

### Spec

````markdown
---
agent_name: string
version: semver
sandbox_type: string      # none | process | container | vm | wasm
execution_risk: string    # low | medium | high | critical
---

# [Agent Name] — Sandbox Configuration

## Sandbox Profile
**Isolation level:** [none | process | container | VM | WebAssembly]
**Execution risk:** [low | medium | high | critical]
**Rationale:** [Why this level of isolation is appropriate]

---

## What This Agent Can Do

### Filesystem
Apply LEASTPRIVILEGE.md — grant only the minimum access required.
- Read: [paths it can read from]
- Write: [paths it can write to]
- Execute: [whether it can run executables]
- Cannot access: [paths explicitly blocked]

### Network
- Outbound: [allowed domains/IPs per NETWORK.md]
- Inbound: [none | specific ports]
- DNS: [standard | restricted resolver]

### Process
- Can spawn subprocesses: [yes | no | limited to: list]
- Can access environment variables: [own only | full system]
- Resource limits:
  - Max CPU: [N cores | N% limit]
  - Max RAM: [N GB]
  - Max execution time per task: [N seconds]
  - Max disk I/O: [N MB/s]

### System Calls (if applicable)
- Blocked system calls: [list]
- Allowed system calls: [list or "standard except blocked above"]

---

## Container Configuration (if containerized)

```dockerfile
# Recommended Docker security flags
docker run \
  --read-only \
  --tmpfs /tmp \
  --no-new-privileges \
  --cap-drop=ALL \
  --cap-add=[only what's needed] \
  --security-opt=no-new-privileges:true \
  --memory=[N]g \
  --cpus=[N] \
  [image-name]
```

---

## Isolation Verification

```bash
# Verify sandbox is configured correctly
[agent-cli] sandbox verify

# Test that isolation is working
[agent-cli] sandbox test --check filesystem
[agent-cli] sandbox test --check network
[agent-cli] sandbox test --check processes
```

---

## Escape Detection

If the agent attempts to access resources outside its sandbox:
1. The attempt is blocked and logged
2. An alert is sent to [security contact]
3. If [N] escape attempts in [N] minutes: agent is suspended
4. Incident reviewed before restarting

Escape attempts are treated as security incidents (see ENFORCEMENT.md).
````

## Example Use Cases

**Enterprise:** A software development company uses SANDBOX.md to run its code generation agent in a read-only container with no network access and a 30-second execution timeout, preventing generated code from making unauthorized API calls or modifying the host filesystem.

**Multi-Agent Fleet:** A cloud platform provider configures SANDBOX.md for each agent in its fleet with per-agent CPU and RAM limits, ensuring a runaway agent processing a large document cannot consume resources needed by other agents on the same host.

**Regulated Industry:** A nuclear energy company uses SANDBOX.md to isolate its equipment monitoring agent in a VM with blocked system calls and no outbound network except the SCADA API endpoint, detecting and suspending the agent after three escape attempts as a security incident.

## Related Specs

| Spec | Relationship |
|------|-------------|
| ATTESTATION.md | Identity verification and credential lifecycle |
| AUDITTRAIL.md | Tamper-proof action logging |
| ENFORCEMENT.md | Policy verification and compliance |
| PROMPTSHIELD.md | Prompt injection defense |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
