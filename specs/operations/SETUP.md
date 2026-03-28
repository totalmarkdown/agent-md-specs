---
spec_name: SETUP.md
spec_version: 0.1.0
category: Operations
domain: setupmd.dev
priority: High
volume: "Vol 12 — Fleet Operations"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
tier: extended
---

# SETUP.md

**Category:** Operations
**Domain:** setupmd.dev
**Priority:** High
**Version:** 0.1.0

### Purpose
Step-by-step guide to get this agent running from scratch.
Where DEPLOYMENT.md covers production deployment procedures
and REQUIREMENTS.md lists what you need, SETUP.md is the
narrative walkthrough for someone setting up this agent
for the first time.

### Spec

```markdown
---
agent_name: string
version: semver
setup_time_minutes: number   # How long setup takes
difficulty: string           # beginner | intermediate | advanced
last_tested: date
tested_on: string            # What platform/config this was tested on
---

# [Agent Name] — Setup Guide

## Before You Start

**Time required:** ~[N] minutes
**Difficulty:** [Beginner | Intermediate | Advanced]
**You'll need:**
- [ ] [Requirement 1 — e.g. "Anthropic API key (free at console.anthropic.com)"]
- [ ] [Requirement 2]
- [ ] [N GB free disk space]

---

## Step 1: Get the Files

```bash
# Option A: Clone from GitHub
git clone https://github.com/[org]/[agent-name]
cd [agent-name]

# Option B: Download from TotalAgents.ai
tmd install [agent-name]
cd [agent-name]
```

---

## Step 2: Install Dependencies

```bash
# Node.js agents
npm install

# Python agents
pip install -r requirements.txt

# Rust agents
cargo build --release
```

**If you see errors here:**
- [Common error 1]: [fix]
- [Common error 2]: [fix]

---

## Step 3: Configure Environment

```bash
# Copy the template
cp .env.example .env.local

# Open and fill in your values
nano .env.local
```

**Required values to fill in:**
```
ANTHROPIC_API_KEY=    # Get from console.anthropic.com
[OTHER_REQUIRED]=     # [where to get this]
```

**Optional values with sensible defaults:**
```
LOG_LEVEL=info        # Change to debug for troubleshooting
PORT=3000             # Change if 3000 is in use
```

---

## Step 4: Verify Setup

```bash
# Check everything looks good
[agent-cli] setup verify

# Expected output:
# ✓ Runtime version OK
# ✓ Required env vars set
# ✓ API connection successful
# ✓ MCP servers reachable
# ✓ Ready to run
```

**If any check fails:**
[Link to troubleshooting section or REPAIR.md]

---

## Step 5: First Run

```bash
# Start the agent
[start command]

# You should see:
# [Agent Name] v[version] starting...
# Loaded MEMORY.md: [N] entries
# Listening on port [N]
# Ready.
```

---

## Step 6: Test It

```bash
# Run the smoke test
[test command]

# Or test manually:
[manual test command or example prompt]
```

**Expected result:**
[What a successful first run looks like]

---

## Troubleshooting

### "API key invalid"
Check your `.env.local` — the key may have extra spaces
or be from the wrong account.

### "MCP server not found"
Run: `[mcp check command]`
See MCP.md for server setup instructions.

### "Port already in use"
Change `PORT=` in `.env.local` to an unused port.

### Still stuck?
Open an issue: [GitHub issues URL]
Ask in Discord: [Discord URL]

---

## Next Steps

- Read SOUL.md to understand this agent's personality
- Read LIMITS.md to understand what it won't do
- Read HIREME.md if you want to use it professionally
- Check MEMORY.md to see what it remembers from previous sessions
```

## Related Specs

| Spec | Relationship |
|------|-------------|
| CIRCUITBREAKER.md | Failure containment and blast radius |
| ENFORCEMENT.md | Policy verification and compliance |
| ESCALATION.md | Human-in-the-loop triggers and contacts |
| HEALTHCHECK.md | Liveness and readiness checks |
| HIREME.md | Agent hiring and engagement |
| LIMITS.md | Hard constraints and safety boundaries |
| MCP.md | Model Context Protocol connections |
| MEMORY.md | Individual agent memory governance |

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
