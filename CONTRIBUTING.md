# Contributing to agent-md-specs

agent-md-specs is an open standard maintained by TotalMarkdown.ai
and governed by the community. All contributions are CC0 — public domain.

## How to propose a new spec

Open a GitHub issue with:
- **Spec name** — the filename (e.g. MYSPEC.md)
- **Category** — which subdirectory it belongs in
- **Domain** — the .dev domain for this spec (e.g. myspecmd.dev)
- **Purpose** — one paragraph on what problem it solves
- **Use cases** — at least 2 concrete, specific use cases
- **Draft spec** — a first attempt at the spec content

We review proposals based on:
- Does this fill a genuine gap not covered by existing specs?
- Are the use cases real and specific?
- Does it follow the spec format?
- Is the .dev domain available?

## How to improve an existing spec

1. Fork this repository
2. Edit the spec file in the appropriate `specs/` subdirectory
3. Open a pull request with a clear description of what changed and why
4. If the spec has a standalone canonical repo, open a PR there instead

## Spec format requirements

Every spec must have:
- YAML frontmatter with spec_name, spec_version, category, domain,
  priority, maintained_by, and license fields
- A clear Purpose section
- A When to create section
- A complete Spec section with the full specification

## Domain convention

Each spec has a dedicated .dev domain (e.g. soulmd.dev, teammd.dev).
When proposing a new spec, verify the .dev domain is available
before submitting. The domain establishes the spec as a
first-class standard rather than a loose convention.

## License requirement

All contributions to agent-md-specs must be CC0 1.0 Universal.
By submitting a pull request you dedicate your contribution
to the public domain under CC0. No exceptions.

## Code of conduct

- Be direct and specific — vague proposals don't get merged
- Be honest about limitations and overlaps with existing specs
- Do not disparage existing standards or competing tools
- Welcome all agent frameworks — this library is tool-agnostic
