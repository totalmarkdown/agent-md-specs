---
spec_name: INHERIT.md
spec_version: 0.1.0
category: Governance
domain: inheritmd.dev
priority: High
volume: "Vol 13 — Hierarchy & Inheritance"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# INHERIT.md

**Category:** Governance
**Domain:** inheritmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Declares what configuration this entity inherits from its
parent level in the hierarchy. Makes the inheritance chain
explicit, machine-readable, and auditable.

INHERIT.md is read at startup. The agent or team loads
all parent configuration first, then applies its own
additions and overrides (see OVERRIDE.md).

Think of INHERIT.md as the `extends` declaration in a
class hierarchy, or the `@import` in CSS.

### Spec

```markdown
---
entity_name: string
entity_type: string      # agent | team | crew | swarm | org
entity_level: number     # 0=org, 1=swarm, 2=crew, 3=team, 4=agent
parent_entity: string    # name of parent (null if org-level)
parent_path: string      # path to parent config files
version: semver
inheritance_mode: string # strict | permissive | selective
last_validated: date
---

# [Entity Name] — Inheritance Declaration

## Parent
**Inherits from:** [Parent entity name]
**Parent type:** [org | swarm | crew | team]
**Parent config path:** [relative or absolute path to parent MD files]
**Inheritance mode:** [strict | permissive | selective]

### Inheritance Modes
- **strict:** All parent config applies unless explicitly overridden
- **permissive:** Parent config applies as defaults, child can freely extend
- **selective:** Only explicitly listed parent files are inherited

---

## What This Entity Inherits

### Inherited in full (no changes)
These parent files apply exactly as written:

| File | From | Applies to | Override allowed |
|------|------|-----------|-----------------|
| POLICY.md | [parent] | This entity | No — org policy is absolute |
| LIMITS.md | [parent] | This entity | No — hard stops are absolute |
| SECURITY.md | [parent] | This entity | Additive only |
| COMPLIANCE.md | [parent] | This entity | Additive only |
| BUDGET.md | [parent] | This entity | Can restrict further, not expand |

### Inherited with additions
These parent files apply, with this entity adding its own content:

| File | From | This entity adds |
|------|------|-----------------|
| RULES.md | [parent] | [additional rules specific to this entity] |
| ESCALATION.md | [parent] | [additional escalation paths] |
| TOOLS.md | [parent] | [additional tools available at this level] |
| GLOSSARY.md | [parent] | [domain-specific terminology] |

### Overridden
These parent files are partially or fully replaced.
See OVERRIDE.md for justification of each override.

| File | From | Override type | Justification ref |
|------|------|--------------|------------------|
| VOICE.md | [parent] | Full | OVERRIDE.md #3 |
| BUDGET.md | [parent] | Partial | OVERRIDE.md #1 |

### Not inherited
These files are defined fresh at this level, not inherited:

| File | Reason |
|------|--------|
| SOUL.md | Individual agent personality — always local |
| WHOAMI.md | Identity — always local |
| MEMORY.md | Memory — always local |
| HIREME.md | Hiring — individual or team level |

---

## Inheritance Resolution Order

When the same rule appears at multiple levels,
this is how conflicts are resolved:

1. **ORG level** — highest authority, never overridden for absolute policies
2. **SWARM level** — overrides team/crew/agent for swarm-specific rules
3. **CREW level** — overrides team/agent for crew-specific rules
4. **TEAM level** — overrides agent for team-specific rules
5. **AGENT level** — lowest authority, can only override what parents permit

For non-absolute rules, lower levels take precedence
(agent-level overrides team-level overrides crew-level etc.)

---

## Validating Inheritance

```bash
# Verify this entity's inheritance chain is valid
tmd inherit validate --entity [name]

# Show the full resolved configuration (all levels merged)
tmd inherit resolve --entity [name] --file RULES.md

# Check for conflicts between levels
tmd inherit check --entity [name]

# Show diff between parent and child for a specific file
tmd inherit diff --entity [name] --file BUDGET.md
```

---

## For Tools and Orchestrators

When an orchestrator loads this agent or team,
it should resolve the full configuration by:

1. Starting with ORG-level config files
2. Applying SWARM-level additions/overrides (if applicable)
3. Applying CREW-level additions/overrides (if applicable)
4. Applying TEAM-level additions/overrides (if applicable)
5. Applying AGENT-level additions/overrides
6. Validating no ORG-level absolute policies were violated

The resolved configuration is the effective configuration.
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
