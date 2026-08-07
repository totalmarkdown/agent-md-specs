# Starter Templates

Copy any template and fill in the `[REPLACE]` fields to create
a spec file for your agent.

## Quick Start

```bash
# Download a template
curl -O https://raw.githubusercontent.com/totalmarkdown/agent-md-specs/main/templates/SOUL.template.md

# Rename and fill in
mv SOUL.template.md SOUL.md
```

## Frontmatter

The first five frontmatter keys of every template — `spec_name`,
`spec_version`, `category`, `priority`, `tier` — identify the spec the
template instantiates and are copied verbatim from that spec. Keep them
as they are; they are what a validator uses to know which contract your
file is claiming to meet. Everything below them is a `[REPLACE THIS]`
placeholder and is yours to fill in.

There is no `domain` key. Templates assert no per-spec domain, and
neither do the specs themselves — the canonical location for every spec
is the [agent-md-specs
repository](https://github.com/totalmarkdown/agent-md-specs). Adding a
`domain` key to a template will fail CI.

Every template in this directory is validated against
`schemas/frontmatter.schema.json` on every push and pull request, so a
template you copy starts conformant. Reproduce the check locally with:

```bash
pip install jsonschema pyyaml
python3 tools/validate_corpus.py --surface templates
```

Templates keep the `.template.md` suffix while declaring the bare
`spec_name` of the spec they instantiate, so `agent-md-validate` emits
one `spec_name does not match filename` warning per template. That
warning is expected and correct: it disappears the moment you rename the
file to `SOUL.md` as the Quick Start above instructs.

## Available Templates

### Identity and Verification

| Template | What It Configures | Tier |
|----------|-------------------|------|
| [SOUL.template.md](SOUL.template.md) | Personality, values, tone, ethical boundaries | Core |
| [WHOAMI.template.md](WHOAMI.template.md) | Verifiable identity document | Core |
| [ID.template.md](ID.template.md) | Permanent UUID with cryptographic binding | Core |
| [CONTACT.template.md](CONTACT.template.md) | How to reach this agent | Core |
| [OWNER.template.md](OWNER.template.md) | Who owns and is responsible for this agent | Core |
| [ATTESTATION.template.md](ATTESTATION.template.md) | Identity proof — SPIFFE, X.509, DID | Core |
| [SESSION.template.md](SESSION.template.md) | Ephemeral task-scoped identity | Core |

### Governance and Safety

| Template | What It Configures | Tier |
|----------|-------------------|------|
| [LIMITS.template.md](LIMITS.template.md) | Hard stops — what the agent will never do | Core |
| [GUARDRAILS.template.md](GUARDRAILS.template.md) | Runtime safety boundaries | Core |
| [ESCALATION.template.md](ESCALATION.template.md) | When and how to involve humans | Core |
| [DELEGATION.template.md](DELEGATION.template.md) | Authority delegation chains | Core |
| [CONSENT.template.md](CONSENT.template.md) | User consent lifecycle | Core |
| [LEASTPRIVILEGE.template.md](LEASTPRIVILEGE.template.md) | Zero-trust privilege management | Core |
| [PERMISSIONS.template.md](PERMISSIONS.template.md) | Resource access control | Core |
| [BUDGET.template.md](BUDGET.template.md) | Cost controls and spending limits | Core |
| [ENFORCEMENT.template.md](ENFORCEMENT.template.md) | Spec compliance verification | Core |
| [WAKEUP.template.md](WAKEUP.template.md) | Session startup and initialization | Core |

### Accountability and Audit

| Template | What It Configures | Tier |
|----------|-------------------|------|
| [INTENT.template.md](INTENT.template.md) | Pre-action intent declaration | Core |
| [AUDITTRAIL.template.md](AUDITTRAIL.template.md) | Tamper-evident action logging | Core |
| [PROVENANCE.template.md](PROVENANCE.template.md) | Data lineage tracking | Core |

### Memory and Context

| Template | What It Configures | Tier |
|----------|-------------------|------|
| [MEMORY.template.md](MEMORY.template.md) | Individual agent memory | Core |
| [SHAREDCONTEXT.template.md](SHAREDCONTEXT.template.md) | Multi-agent shared memory | Core |
| [MEMORYSAFETY.template.md](MEMORYSAFETY.template.md) | Memory poisoning defense | Core |

### Coordination and Resilience

| Template | What It Configures | Tier |
|----------|-------------------|------|
| [TEAM.template.md](TEAM.template.md) | Multi-agent team structure | Core |
| [CIRCUITBREAKER.template.md](CIRCUITBREAKER.template.md) | Failure containment | Core |

### Technical Interface

| Template | What It Configures | Tier |
|----------|-------------------|------|
| [INPUT.template.md](INPUT.template.md) | What the agent accepts | Core |
| [PROMPTSHIELD.template.md](PROMPTSHIELD.template.md) | Prompt injection defense | Core |

### Business

| Template | What It Configures | Tier |
|----------|-------------------|------|
| [HIREME.template.md](HIREME.template.md) | How to hire this agent | Core |
| [PITCH.template.md](PITCH.template.md) | How to describe the agent | Extended |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai*
