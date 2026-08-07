---
spec_name: CLI.md
spec_version: 0.1.0
category: Technical
priority: High
tier: extended
agent_name: "[REPLACE THIS]"
cli_name: "[REPLACE THIS — e.g. atlas, myagent]"
version: "0.1.0"
requires: "[REPLACE THIS — e.g. node 18+, python 3.12+]"
stdin_behavior: "[REPLACE THIS — accepts_piped | interactive_only | none]"
stdout_behavior: "[REPLACE THIS — structured_json | streaming_text | mixed]"
stderr_behavior: "[REPLACE THIS — errors_only | errors_and_logs | silent]"
interactive_mode: false
piping_support: true
shell_completion: [bash, zsh, fish]
---

# [REPLACE THIS — Agent Name] — CLI Reference

<!-- Command-line interface contract -->

## Installation
```bash
# [REPLACE THIS — install method]
pip install [REPLACE THIS — package-name]
```

## Basic Usage
```bash
[REPLACE THIS — cli-name] [command] [options] [arguments]
```

## Commands

### [REPLACE THIS — command-name]
**Description:** [REPLACE THIS — what this command does]
**Usage:** `[cli-name] [command] [required] [optional]`

**Options:**
| Flag | Short | Type | Default | Description |
|------|-------|------|---------|-------------|
| [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |
| --format | -f | json\|text | text | Output format |
| --verbose | -v | boolean | false | Verbose logging |
| --quiet | -q | boolean | false | Suppress output |

**Examples:**
```bash
# [REPLACE THIS — example description]
[cli-name] [command] [example-args]
```

**Exit codes:**
- `0` — Success
- `1` — General error
- `2` — Invalid input
- `3` — Network/API error
- `4` — Permission denied

## Global Options
| Flag | Description |
|------|-------------|
| --config | Path to config file |
| --no-color | Disable colored output |
| --json | Output as JSON |
| --version | Show version |
| --help | Show help |

## stdin Behavior
- **Accepts piped input:** [REPLACE THIS — yes/no]
- **Expected format:** [REPLACE THIS — json | csv | markdown | plain text]
- **Example:** `cat data.csv | [cli-name] analyze --stdin`

## stdout Behavior
- **Default format:** [REPLACE THIS — text | json | markdown]
- **Streaming:** [REPLACE THIS — enabled/disabled]

## stderr Behavior
- **Errors:** Structured error messages to stderr
- **Logs:** --verbose sends debug logs to stderr

## Piping Support
```bash
# [REPLACE THIS — example pipeline]
[cli-name] export --format json | jq '.results[]' | [other-tool]
```

## Environment Variables
| Variable | Description | Default |
|----------|-------------|---------|
| [REPLACE THIS] | [REPLACE THIS] | [REPLACE THIS] |

## Shell Completion
```bash
# Bash
[cli-name] completion bash >> ~/.bashrc

# Zsh
[cli-name] completion zsh >> ~/.zshrc
```
