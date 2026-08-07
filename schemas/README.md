# JSON Schemas for agent-md-specs

Machine-readable schemas for validating agent-md-specs configuration files.

## Why JSON Schemas for Markdown Files?

The YAML frontmatter in every agent-md-specs file IS the machine-
readable format. These schemas validate that frontmatter — ensuring
field types, allowed values, and structural constraints are correct.
The Markdown body provides the human-readable context that compliance
officers need to understand and approve the policies. The schemas
ensure the machine-readable portion is trustworthy and consistent.

## Usage

These schemas define the expected structure for each spec type's YAML
frontmatter and content fields. They can be used with any JSON Schema
validator to verify that agent configuration files conform to the
agent-md-specs specification.

### Validation Example

```bash
# Using Python jsonschema
pip install jsonschema pyyaml

# Validate a DELEGATION.md file's frontmatter
python -c "
import yaml, json, jsonschema
with open('my-agent/DELEGATION.md') as f:
    content = f.read().split('---')[1]
    data = yaml.safe_load(content)
with open('schemas/delegation.schema.json') as f:
    schema = json.load(f)
jsonschema.validate(data, schema)
print('Valid!')
"
```

## Schema Files

| Schema | Validates | Spec Tier |
|--------|----------|-----------|
| frontmatter.schema.json | All documents (shared fields) | All |
| spec-document.schema.json | The specification documents in `specs/` | All |
| attestation.schema.json | ATTESTATION.md | Core |
| audittrail.schema.json | AUDITTRAIL.md | Core |
| circuitbreaker.schema.json | CIRCUITBREAKER.md | Core |
| consent.schema.json | CONSENT.md | Core |
| contact.schema.json | CONTACT.md | Core |
| delegation.schema.json | DELEGATION.md | Core |
| enforcement.schema.json | ENFORCEMENT.md | Core |
| escalation.schema.json | ESCALATION.md | Core |
| guardrails.schema.json | GUARDRAILS.md | Core |
| heartbeat.schema.json | HEARTBEAT.md | Core |
| id.schema.json | ID.md | Core |
| intent.schema.json | INTENT.md | Core |
| leastprivilege.schema.json | LEASTPRIVILEGE.md | Core |
| limits.schema.json | LIMITS.md | Core |
| memory.schema.json | MEMORY.md | Core |
| memorysafety.schema.json | MEMORYSAFETY.md | Core |
| owner.schema.json | OWNER.md | Core |
| permissions.schema.json | PERMISSIONS.md | Core |
| promptshield.schema.json | PROMPTSHIELD.md | Core |
| provenance.schema.json | PROVENANCE.md | Core |
| session.schema.json | SESSION.md | Core |
| sharedcontext.schema.json | SHAREDCONTEXT.md | Core |
| team.schema.json | TEAM.md | Core |
| whoami.schema.json | WHOAMI.md | Core |

## What Each Schema Is For

The corpus contains three kinds of Markdown file, and they do not share
one contract. Reading a schema without knowing which layer it describes is
the fastest way to misread it.

| Layer | Where | Contract |
|-------|-------|----------|
| Specification document | `specs/**` | `spec-document.schema.json` — the shared frontmatter fields plus the required lifecycle `status:` marker. This is the spec *text*, not a deployed configuration. |
| Starter template | `templates/*.template.md` | `frontmatter.schema.json`. Templates carry their spec's identity block and `[REPLACE THIS — ...]` placeholders everywhere else, so by construction they cannot satisfy per-spec value constraints. |
| Instance document | `examples/**`, and adopter files in the wild | The per-spec schema bound by filename — `WHOAMI.md` → `whoami.schema.json` — falling back to `frontmatter.schema.json` where no per-spec schema exists. This is where Level 3 applies. |

The per-spec schemas model a deployed agent's file, which is why the
`Validation Example` above points at `my-agent/DELEGATION.md` rather than
at `specs/governance/DELEGATION.md`.

## Conformance Levels

- **Level 1 (Frontmatter):** Valid YAML frontmatter with all required fields
- **Level 2 (Sections):** All required Markdown sections present
- **Level 3 (Content):** Field values conform to type constraints and enums

The agent-md-validator CLI checks Levels 1 and 2. JSON Schema validation
enables Level 3 checking for structured frontmatter content.

Level 3 is executed by [`tools/validate_corpus.py`](../tools/validate_corpus.py),
which the `Validate Specs` workflow runs on every push and pull request
that touches `specs/`, `examples/`, `schemas/`, `templates/`, `tools/` or
`tests/`. Run it yourself with:

```bash
pip install jsonschema pyyaml
python3 tools/validate_corpus.py                 # validate the whole corpus
python3 tools/validate_corpus.py --stable-gate   # per-spec Level 3 readiness
```

All `$ref`s resolve against this directory. The script builds its schema
registry with a retriever that refuses every URI it was not given, so a
schema that grew a remote `$ref` fails the run rather than silently
fetching from the network in CI.

`SPEC_LIFECYCLE.md` makes "passes Level 3" a precondition for promoting a
spec to Stable. `--stable-gate` reports the repository-checkable part of
that criterion for every spec: does the spec publish a schema, does at
least one example bundle ship an instance document for it, and do all
those documents validate with no known deviation registered against any of
them.

## Known Deviations

[`known-deviations.json`](./known-deviations.json) lists validation
failures that are known, named, and deliberately not fixed in the current
release. Each entry carries the owning defect id, the governance track
that owns the fix, and the reason.

The validator reports every entry on each run and does not fail on it.
Three properties keep that from being a suppression list:

1. **A listed entry that stops reproducing fails the run.** A deviation
   cannot outlive the failure it describes.
2. **Each entry is bound to one exact error.** The `error_signature` field
   is a SHA-256 over the error's structural shape — its absolute schema
   path, the failing keyword, that keyword's schema value, and recursively
   the same for every sub-error a composite keyword such as `anyOf`
   collected. A materially different failure at the same path, schema,
   JSON path and keyword produces a different signature and is reported as
   an unregistered failure, so it cannot inherit an existing entry's
   excuse. Read a signature off a real run with
   `python3 tools/validate_corpus.py --signatures`.
3. **A listed document has not passed.** The summary table counts it under
   `known`, never under `passed`, and a listed *instance* document supplies
   no Level-3 evidence for promoting its spec to Stable. Registering a
   deviation records a decision; it does not manufacture conformance.

Adding an entry is a governance statement, not a way to make CI green.

## A Note on `status`

`status` means two different things in this corpus. On a specification
document it is the lifecycle stage (`draft | proposed | stable |
deprecated | retired`). On a HIREME instance document it is the agent's
availability (`available | busy | unavailable`).

That is why the lifecycle enum lives in `spec-document.schema.json` and
not in `frontmatter.schema.json`: defining it in the shared schema would
invalidate adopter documents that are using the field correctly under the
other meaning. Resolving the overload is a vocabulary change to published
specs and needs an RFC.

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai*
