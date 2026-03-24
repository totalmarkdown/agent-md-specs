# ENFORCEMENT.md — Forge

## Pre-Review Checks

Before Forge reviews any PR, these conditions are verified:
- PR author is not Forge itself (prevents self-approval loops)
- PR is within the TechCo GitHub org (rejects external webhooks)
- PR is less than 30 days old (stale PRs require human triage)
- Forge's delegation has not expired (checked against DELEGATION.md expiry)

## Runtime Enforcement

- GitHub Actions OIDC permissions enforce read-only access to production
- Forge's GitHub App token is scoped per-repository at installation time
- AWS IAM role `forge-lambda-execution` has no write access to prod resources
- All outbound network calls are restricted to TechCo internal services
  and GitHub API (enforced via Lambda VPC security groups)

## Pre-Deploy Gates

Before triggering any staging deployment:
- All CI checks must pass (unit, integration, e2e, lint, typecheck)
- No open security findings from `npm audit` at severity high or critical
- PR has at least 1 human approval
- No LIMITS.md violations detected in the changeset

## Post-Deploy Verification

- Health check: `GET https://staging.techco.com/health` must return 200
  within 5 minutes of deploy completion
- If health check fails: auto-rollback to previous version, post to
  `#deploys` Slack channel with failure details
- Smoke tests: run `npm run test:smoke` against staging after deploy

## Drift Detection

- If Forge's review comments are overridden (dismissed) more than 5 times
  in a 7-day window, alert VP Eng — possible LIMITS misconfiguration or
  team friction that needs human attention
- If Forge's deployment success rate drops below 90% over 30 days, flag
  for DevOps review of pipeline health
