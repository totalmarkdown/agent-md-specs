---
spec_name: "SESSION.md"
spec_version: "1.0.0"
category: Example
tier: extended
agent_name: "Nova"
agent_version: "1.0.0"
---

# Session

## Session Boundary

Each experiment constitutes a single session. A session begins when
a new hypothesis is formulated and ends when the evaluation result
is logged to results.tsv.

## Time Limit

Each training run has a fixed 5-minute wall clock budget. The
watchdog process (see ENFORCEMENT.md) terminates any run that
exceeds this limit. Evaluation time does not count toward the
training budget but should not exceed 2 minutes.

## Memory Model

Nova carries no persistent memory between sessions beyond two
artifacts:
- **results.tsv** — The complete experiment history with metrics.
- **git log** — The commit history and branch record.

All other state is destroyed when a session ends. There is no
vector store, no conversation history, no scratchpad that persists.
This forces each session to be self-contained and reproducible.

## Session Lifecycle

1. **Init** — Read results.tsv and recent git log to understand
   what has been tried and what worked.
2. **Execute** — Run a single experiment (see WORKFLOW.md).
3. **Record** — Append results to results.tsv and commit.
4. **Destroy** — Session state is discarded. The next session
   starts fresh from the artifacts.

## Rationale

Stateless sessions prevent the agent from developing false
confidence based on accumulated but potentially stale context.
Every decision must be justified by the written record.
