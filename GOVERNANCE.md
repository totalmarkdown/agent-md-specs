# Governance

## Current Status

agent-md-specs is currently maintained by TotalMarkdown.ai. As the project matures and gains community adoption, governance will evolve toward a more formal structure.

## How Specs Are Managed

### Proposing a New Spec
1. Open a GitHub Discussion in the "Ideas" category
2. Include: spec name, category, purpose, at least 2 real-world use cases
3. Community discussion period: 14 days minimum
4. If accepted, submit a PR following the spec template format

### Modifying an Existing Spec
1. Open a GitHub Issue describing the proposed change
2. Submit a PR with the change
3. Changes to Core tier specs require additional review

### Spec Tiers
- **Core** — essential specs recommended for all production agents
- **Extended** — valuable specs for specific use cases and advanced configurations

### Versioning
- Individual specs use semver in their YAML frontmatter
- The library itself is versioned by volume (Vol 1-13)
- Breaking changes to Core specs require a new major version

## Future Governance

As adoption grows, we intend to:
- Establish a Technical Steering Committee with external members
- Formalize the RFC process for new specs
- Seek alignment with AAIF and NIST AI Agent Standards Initiative
- Accept nominations for spec category maintainers

## Contact

- GitHub Discussions: https://github.com/totalmarkdown/agent-md-specs/discussions
- Created and maintained by TotalMarkdown.ai
