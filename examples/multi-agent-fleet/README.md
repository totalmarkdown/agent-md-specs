# Multi-Agent Fleet Example: Sentinel Crew

Most multi-agent frameworks (CrewAI, LangGraph, AutoGen) define agent coordination in code — buried in Python classes, YAML configs, or graph definitions. When something goes wrong, auditing behavior means reading source code. Non-technical stakeholders (compliance, management) can't review what agents are allowed to do.

agent-md-specs solves this with a layered, human-readable structure:

- **TEAM.md** defines the crew: members, pipeline order, handoff protocol, shared constraints
- **Individual agent specs** (SOUL.md, LIMITS.md, INPUT.md, OUTPUT.md) define each agent's personality, boundaries, and data contracts
- **Shared governance** (BUDGET.md, ESCALATION.md, DELEGATION.md) captures org-level policies that apply across the crew

This example implements a 3-agent financial data pipeline at a hedge fund. Every spec is a plain Markdown file that a Portfolio Manager, compliance officer, or auditor can read, review, and approve — no code knowledge required.

The framework loader reads these specs at agent initialization. Changes to behavior are pull requests, not code deploys. Git history becomes a full audit trail of what each agent was permitted to do and when.

## Directory Structure

```
TEAM.md                    # Crew definition and pipeline
agents/scout/              # Data collection agent
agents/analyst/            # Analysis agent
agents/scribe/             # Report generation agent
shared/                    # Crew-wide governance
```
