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
---

# REPO.md

**Category:** Technical/Documentation
**Domain:** repomd.dev
**Priority:** High
**Version:** 0.1.0

```markdown
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
| Metric | Status |
|--------|--------|
| CI/CD | [passing] |
| Test coverage | [N]% |
| Last security audit | [date] |
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
