# Contributing to agent-md-specs

agent-md-specs is an open standard maintained by TotalMarkdown.ai
and governed by the community. All contributions are CC0 — public domain.

## How to propose a new spec

Open a GitHub issue with:
- **Spec name** — the filename (e.g. MYSPEC.md)
- **Category** — which subdirectory it belongs in
- **Purpose** — one paragraph on what problem it solves
- **Use cases** — at least 2 concrete, specific use cases
- **Draft spec** — a first attempt at the spec content

We review proposals based on:
- Does this fill a genuine gap not covered by existing specs?
- Are the use cases real and specific?
- Does it follow the spec format?

## How to improve an existing spec

1. Fork this repository
2. Edit the spec file in the appropriate `specs/` subdirectory
3. Open a pull request with a clear description of what changed and why
4. If the spec has a standalone canonical repo, open a PR there instead

## Spec format requirements

Every spec must have:
- YAML frontmatter with spec_name, spec_version, category,
  priority, maintained_by, and license fields
- A clear Purpose section
- A When to create section
- A complete Spec section with the full specification

The authoritative machine contract is `schemas/frontmatter.schema.json`.
If this list and that schema ever disagree, the schema wins — and CI
enforces the schema, so a disagreement is a bug in this list. Specs
carry no `domain` field; see below.

## Canonical location

Specs do not assert a per-spec domain. There is no `domain` frontmatter
field, and adding one to a spec, template or example will fail CI.

The canonical location for every spec in this repository is this
repository:

    https://github.com/totalmarkdown/agent-md-specs

A handful of specs also have a standalone companion repo, listed in the
README. Those are mirrors of the spec published here, not a competing
source of truth.

## License requirement

All contributions to agent-md-specs must be CC0 1.0 Universal.
By submitting a pull request you dedicate your contribution
to the public domain under CC0. No exceptions.

## Code of conduct

- Be direct and specific — vague proposals don't get merged
- Be honest about limitations and overlaps with existing specs
- Do not disparage existing standards or competing tools
- Welcome all agent frameworks — this library is tool-agnostic
