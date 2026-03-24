---
spec_name: "WORKFLOW.md"
spec_version: "1.0.0"
category: Example
tier: extended
agent_name: "Nova"
agent_version: "1.0.0"
---

# Workflow

## Experiment Loop

Every experiment follows this exact sequence. No steps may be skipped.

### 1. Hypothesize

State a clear, falsifiable hypothesis. Example: "Increasing the
learning rate warmup from 200 to 400 steps will reduce val_bpb
because the current warmup is too short for stable early training."

### 2. Branch

Create a git branch from main: `git checkout -b exp/<short-name>`.
Never work directly on main. The branch name should be descriptive
enough to identify the experiment from `git log --oneline`.

### 3. Modify

Make the minimum code change required to test the hypothesis. Change
one variable at a time. If the change touches more than 2 files,
reconsider whether the hypothesis is too broad.

### 4. Commit

`git add` and `git commit` with a message that includes the hypothesis.
Example: `git commit -m "exp: increase lr warmup to 400 steps"`.

### 5. Train

Run training with a 5-minute wall clock budget. The watchdog process
monitors elapsed time and kills the run if it exceeds the limit.

### 6. Evaluate

Run the full evaluation harness with the standard seed set. Record
val_bpb, training_seconds, peak_vram_mb, and mfu_percent.

### 7. Compare

Compare val_bpb to the baseline. If improved: merge branch to main.
If not improved: log the result and delete the branch.

### 8. Log

Append a row to results.tsv with all metrics, regardless of outcome.
Failed experiments are logged with `kept=false`.

### 9. Repeat

Return to step 1 with a new hypothesis informed by accumulated
results. Use the results log to avoid re-testing failed approaches.
