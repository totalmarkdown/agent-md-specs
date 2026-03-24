---
spec_name: "ESCALATION.md"
spec_version: "1.0.0"
category: Example
tier: extended
agent_name: "Nova"
agent_version: "1.0.0"
---

# Escalation

## Core Principle

Nova never pauses to ask a human. All failure modes have automated
responses. The agent must keep making progress or fail gracefully.

## Crash Recovery

If a training run crashes:
1. Read the error traceback and attempt an automated fix.
2. Retry the run once with the fix applied.
3. If it crashes again, skip this experiment entirely.
4. Log the failure in results.tsv with `kept=false` and the error
   category (OOM, syntax, numerical instability, other) in notes.

## Stuck Detection

If 3 consecutive experiments within the same hypothesis family show
no improvement:
1. Abandon the current hypothesis family.
2. Log a summary of what was tried and why it failed.
3. Move to a fundamentally different approach (e.g., switch from
   optimizer tuning to architecture changes).

## Out of Memory (OOM)

If a run triggers an OOM error:
1. Automatically reduce batch size by 50%.
2. If still OOM, reduce model dimensions by one tier.
3. If still OOM after two reductions, skip and log.
4. Never spill to CPU memory — it invalidates timing metrics.

## Extended Failure

If 5 or more consecutive experiments fail or show no improvement:
1. Generate a summary of all attempted approaches and outcomes.
2. Log the summary to `stalled_report.md` in the project root.
3. Shift to a fundamentally different research direction — do not
   continue iterating on variations of failed approaches.
4. If 10 consecutive failures occur, halt and write a final report.
