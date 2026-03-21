---
spec_name: CLI.md
spec_version: 0.1.0
category: Technical
domain: climd.dev
priority: High
volume: "Vol 3 — Forward-Thinking Identity"
maintained_by: TotalMarkdown.ai
license: CC0 1.0 Universal
---

# CLI.md

**Category:** Technical
**Domain:** climd.dev
**Priority:** High
**Version:** 0.1.0

**Priority:** HIGH — developer tooling  
**Version:** 0.1.0

### Purpose
Complete command-line interface documentation for an agent. 
Tells developers and other agents exactly how to invoke this 
agent from the terminal, what flags exist, what output to expect.

### Spec

```markdown
---
agent_name: string
cli_name: string        # The actual command name (e.g. 'tmd', 'myagent')
version: semver
requires: string        # Runtime requirements (node 18+, python 3.10+, etc.)
---

# [Agent Name] — CLI Reference

## Installation
```bash
# npm
npm install -g @[org]/[agent-name]

# pip
pip install [agent-name]

# cargo
cargo install [agent-name]

# binary (no runtime required)
curl -sSL [install-url] | sh
```

## Basic Usage
```bash
[cli-name] [command] [options] [arguments]
```

## Commands

### [command-name]
**Description:** [What this command does]  
**Usage:** `[cli-name] [command] [required] [optional]`

**Options:**
| Flag | Short | Type | Default | Description |
|------|-------|------|---------|-------------|
| --[flag] | -[f] | string | [default] | [description] |
| --output | -o | string | stdout | Output destination |
| --format | | json\|md\|text | text | Output format |
| --verbose | -v | boolean | false | Verbose logging |
| --quiet | -q | boolean | false | Suppress output |
| --dry-run | | boolean | false | Preview without executing |

**Examples:**
```bash
# Basic usage
[cli-name] [command] [example-arg]

# With options
[cli-name] [command] --format json --output result.json

# Pipe input
cat input.md | [cli-name] [command]
```

**Exit codes:**
- `0` — Success
- `1` — General error
- `2` — Invalid input
- `3` — Network/API error
- `4` — Permission denied

[Repeat for each command]

## Global Options
Available on all commands:
| Flag | Description |
|------|-------------|
| --config | Path to config file |
| --no-color | Disable colored output |
| --json | Output as JSON (shorthand for --format json) |
| --version | Show version |
| --help | Show help |

## Environment Variables
| Variable | Description | Default |
|----------|-------------|---------|
| [AGENT_API_KEY] | API key for authentication | required |
| [AGENT_ENDPOINT] | Custom endpoint URL | [default] |

## Configuration File
`[cli-name]` reads config from `.[cli-name]rc` or `[cli-name].config.json`:
```json
{
  "endpoint": "[default endpoint]",
  "format": "text",
  "timeout": 30
}
```

## Shell Completion
```bash
# Bash
[cli-name] completion bash >> ~/.bashrc

# Zsh
[cli-name] completion zsh >> ~/.zshrc

# Fish
[cli-name] completion fish > ~/.config/fish/completions/[cli-name].fish
```
```

---

*Part of [agent-md-specs](https://github.com/totalmarkdown/agent-md-specs)*
*Maintained by TotalMarkdown.ai · License: CC0 1.0 Universal*
