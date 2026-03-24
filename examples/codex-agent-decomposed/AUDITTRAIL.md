# AUDITTRAIL.md — Forge

## What Gets Logged

Every action Forge takes is recorded:
- PR review comments (with full text and timestamp)
- CI pipeline triggers (workflow name, commit SHA, trigger reason)
- Staging deployments (version, commit, duration, health check result)
- Escalation events (level, recipients, response time)
- Errors and retries (with stack traces and correlation IDs)

## Log Format

Each entry is a JSON object appended to an immutable log stream:

```json
{
  "id": "forge-evt-20260315-084721-a3f9",
  "timestamp": "2026-03-15T08:47:21Z",
  "action": "pr_review",
  "repo": "techco/platform-api",
  "pr": 1847,
  "details": { "comments": 4, "verdict": "changes_requested" },
  "hash": "sha256:9f3a...c7e1",
  "prev_hash": "sha256:7b2d...e4a8"
}
```

## Integrity

- SHA-256 hash chain — each entry references the previous entry's hash
- Entries are signed with Forge's GitHub App private key (RS256)
- Logs are append-only; deletion requires security team approval

## Retention & Access

- **Retention:** 2 years (SOC2 Type II compliance)
- **Storage:** S3 bucket `techco-audit-agents` with versioning enabled
- **Query endpoint:** `https://audit.techco.internal/agents/forge`
- **Weekly report:** Automated compliance summary sent to VP Eng every Monday
- **On-demand:** Security team can query any time range via audit API
