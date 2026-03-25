# JSON Schemas for agent-md-specs

Machine-readable schemas for validating agent-md-specs configuration files.

## Usage

These schemas define the expected structure for each spec type's YAML
frontmatter and content fields. They can be used with any JSON Schema
validator to verify that agent configuration files conform to the
agent-md-specs standard.

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
| frontmatter.schema.json | All specs (shared fields) | All |
| attestation.schema.json | ATTESTATION.md | Core |
| audittrail.schema.json | AUDITTRAIL.md | Core |
| circuitbreaker.schema.json | CIRCUITBREAKER.md | Core |
| consent.schema.json | CONSENT.md | Core |
| contact.schema.json | CONTACT.md | Core |
| delegation.schema.json | DELEGATION.md | Core |
| enforcement.schema.json | ENFORCEMENT.md | Core |
| escalation.schema.json | ESCALATION.md | Core |
| guardrails.schema.json | GUARDRAILS.md | Core |
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

## Conformance Levels

- **Level 1 (Frontmatter):** Valid YAML frontmatter with all required fields
- **Level 2 (Sections):** All required Markdown sections present
- **Level 3 (Content):** Field values conform to type constraints and enums

The agent-md-validator CLI checks Levels 1 and 2. JSON Schema validation
enables Level 3 checking for structured frontmatter content.

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai*
