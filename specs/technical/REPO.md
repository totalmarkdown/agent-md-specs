---
spec_name: REPO.md
spec_version: 0.1.0
category: Technical/Documentation
domain: repomd.dev
priority: High
volume: "Vol 8 — Repos, Compliance & The Weird Wonderful Ones"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
spec_type: static
---


# REPO.md

**Category:** Technical/Documentation
**Domain:** repomd.dev
**Priority:** High
**Version:** 0.1.0 **Type:** Static

### Purpose

Defines the agent's source code repository structure, documentation links, contribution guidelines, and code quality metrics. This gives developers, auditors, and contributors a single reference point for locating the agent's codebase, filing issues, and assessing software quality.

````markdown
---
agent_name: string
version: semver
primary_repo: string
license: string
open_source: boolean
---

# [Agent Name] — Repository & Code

## Primary Repository
**URL:** [https://github.com/org/repo]  
**License:** [MIT | Apache-2.0 | proprietary]  
**Stars:** [N] ⭐ | **Forks:** [N] | **Open issues:** [N]

## Repo Structure
```
repo/
├── README.md
├── CLAUDE.md / AGENTS.md
├── specs/          # All MD spec files
├── src/            # Source code
├── docs/           # Documentation
├── tests/          # Test suite
└── examples/       # Example configs
```

## Documentation
| Doc | URL | Description |
|-----|-----|-------------|
| README | [URL] | Overview, quickstart |
| Full docs | [URL] | Complete documentation |
| API reference | [URL] | Tool reference |
| Changelog | [URL] | Version history |
| Roadmap | [URL] | What's coming |

## Issues & Feedback
**Bugs:** [URL] → Issues → Bug Report  
**Features:** [URL] → Issues → Feature Request  
**Security:** See SECURITY.md — do NOT open public issue  
**Questions:** [discussions URL]

## Contributing
**Guide:** [URL to CONTRIBUTING.md]  
**Good first issues:** tagged `good-first-issue`  
```bash
git clone [repo URL]
cd [repo]
[setup commands]
```

## Packages
| Package | Registry | Install |
|---------|---------|---------|
| [@org/name] | npm | `npm i @org/name` |
| [name] | PyPI | `pip install name` |

## Code Quality
_See TESTING.md for the full test suite and pass criteria._
| Metric | Status |
|--------|--------|
| CI/CD | [passing] |
| Test coverage | [N]% |
| Last security audit | [date] |
````

## Example Use Cases

**Enterprise:** An open-source agent developer uses REPO.md to provide a single reference page linking to their GitHub repo, npm package, full documentation site, and contribution guide, reducing onboarding time for new contributors from hours to minutes.

**Multi-Agent Fleet:** A marketplace operator uses REPO.md data from all listed agents to display code quality badges (CI status, test coverage percentage, last security audit date) on each agent's profile page, helping buyers assess reliability.

**Regulated Industry:** A security auditor uses REPO.md to locate the agent's test suite, changelog, and SECURITY.md contact before performing a penetration test, following the documented responsible disclosure process instead of opening public issues.

## Related Specs

| Spec | Relationship |
|------|-------------|
| INPUT.md | Accepted input formats |
| MCP.md | Model Context Protocol connections |
| OUTPUT.md | Output formats and delivery |
| PERMISSIONS.md | Static resource access control |
| TOOLS.md | Available tools and capabilities |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
