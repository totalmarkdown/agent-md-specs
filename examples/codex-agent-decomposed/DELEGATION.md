---
spec_name: "DELEGATION.md"
spec_version: "1.0.0"
category: Example
tier: extended
agent_name: "Forge"
agent_version: "3.2.0"
---

# DELEGATION.md — Forge

## Delegating Authority

- **Delegated by:** Maya Torres, VP Engineering, TechCo Inc.
- **Delegation date:** 2026-01-15
- **Expires:** 2026-12-31 (must be renewed annually)

## Granted Permissions

- Read access to all repositories in the TechCo GitHub org
- Comment on pull requests (review comments and inline suggestions)
- Request changes or approve PRs on behalf of the Forge bot account
- Trigger CI pipelines via GitHub Actions workflow_dispatch
- Deploy to staging environment via `npm run deploy:staging`
- Read CI logs and test results

## Explicitly NOT Delegated

- Deploy to production (requires human release manager)
- Modify CI/CD pipeline configuration (`.github/workflows/`)
- Access secrets or environment variables directly
- Approve PRs authored by Forge itself (self-approval loop)
- Create or delete repositories
- Modify branch protection rules
- Access customer data or production databases

## Revocation

Delegation can be revoked immediately via:
- TechCo admin portal → Agents → Forge → Revoke
- Emergency: disable GitHub App installation in org settings
- Contact: security@techco.com for urgent revocation
