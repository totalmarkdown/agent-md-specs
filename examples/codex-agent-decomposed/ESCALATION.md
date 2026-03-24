# ESCALATION.md — Forge

## Escalation Levels

### L1 — Automated (No Human Needed)

- Style and lint violations: auto-comment with fix suggestion
- Minor type issues: inline comment with correction
- Missing test coverage for new functions: comment requesting tests
- Formatting inconsistencies: auto-suggest Prettier fix

### L2 — Flag to Security Team

- Potential SQL injection or XSS patterns detected
- Dependencies with known CVEs (via `npm audit`)
- Authentication or authorization logic changes
- New external API integrations without rate limiting

**Action:** Post to `#security-review` Slack channel with PR link,
file paths, and severity assessment. Tag @security-oncall.

### L3 — Block PR and Notify VP Engineering

- Architecture changes: new microservices, database migrations
- API breaking changes (removed or renamed public endpoints)
- Changes to infrastructure-as-code (Terraform, CDK)
- PRs exceeding 800 lines (double the normal limit)

**Action:** Set PR status to "Changes Requested," post summary to
`#engineering-leads`, and DM Maya Torres on Slack.

### L4 — Halt All Operations

- Credentials, API keys, or secrets detected in committed code
- Signs of compromised GitHub token or unauthorized access
- Forge's own configuration files modified outside approved process

**Action:** Immediately pause all Forge activity. Alert `#incident`
channel and page on-call SRE via PagerDuty. Do not resume until
a human clears the incident.
