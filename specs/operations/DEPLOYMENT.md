---
spec_name: DEPLOYMENT.md
spec_version: 0.1.0
category: Operations
domain: deploymentmd.dev
priority: High
volume: "Vol 2 — Extended Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# DEPLOYMENT.md

**Category:** Operations
**Domain:** deploymentmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Documents how to deploy, configure, update, and roll back this 
agent in production environments.

### Spec

```markdown
---
agent_name: string
version: semver
environments: list     # [dev, staging, production]
deployment_method: string  # docker | k8s | serverless | bare-metal | managed
created: date
updated: date
---

# [Agent Name] — Deployment Guide

## Environments
| Environment | Purpose | URL/endpoint | Config source |
|------------|---------|--------------|---------------|
| development | Local testing | localhost | .env.local |
| staging | Pre-production testing | [URL] | Doppler/staging |
| production | Live | [URL] | Doppler/production |

## Prerequisites
Before deploying:
- [ ] All required env vars set in [secrets manager]
- [ ] MCP servers in MCP.md are accessible from deployment environment
- [ ] API endpoints in API.md are accessible
- [ ] EVAL.md test suite passing (min [X]% pass rate)
- [ ] SECURITY.md reviewed for this deployment context

## Deployment Steps
```bash
# 1. Pull latest config
doppler run -- [command to fetch config]

# 2. Run pre-deployment tests
tmd eval --agent [name] --threshold [X]

# 3. Deploy
[deployment command]

# 4. Health check
curl [health endpoint] # Expect 200 OK

# 5. Smoke test
[smoke test command]
```

## Environment Variables
| Variable | Required | Description | Source |
|----------|----------|-------------|--------|
| [VAR_NAME] | yes | [purpose] | [Doppler key] |

## Rollback Procedure
If deployment fails or causes issues:
```bash
[rollback command]
```
Rollback triggers when:
- Health check fails after deploy
- Error rate exceeds [X]% in first [N] minutes
- Any P1 alert fires within [N] minutes of deployment

## Update Process
For config-only updates (no code):
1. Update relevant MD files in workspace
2. Commit to git
3. Trigger config reload: [command]
4. Verify: run health check

For code updates:
1. Run full EVAL.md suite
2. Deploy to staging first
3. Smoke test in staging
4. Deploy to production with [N] minute monitoring window
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
