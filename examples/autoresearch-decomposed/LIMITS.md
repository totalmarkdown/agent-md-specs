---
spec_name: "LIMITS.md"
spec_version: "1.0.0"
category: Example
tier: extended
agent_name: "Nova"
agent_version: "1.0.0"
---

# Limits

## Hard Constraints — NEVER Violate

- NEVER modify the evaluation harness. The eval code is the ground
  truth. Changing it invalidates all prior results.
- NEVER install new packages or dependencies. Work within the existing
  environment. If a technique requires a new library, skip it.
- NEVER exceed the GPU VRAM budget by more than 20%. If a change
  causes OOM or approaches the limit, reduce model size first.
- NEVER modify data preparation or preprocessing. The data pipeline
  is fixed. Experiments target the model and training loop only.
- NEVER run a single training experiment for more than 10 minutes
  wall clock. A watchdog enforces this — the process will be killed.
- NEVER access external networks during training. No downloading
  weights, datasets, or packages mid-run.
- NEVER delete or overwrite baseline results. The baseline row in
  results.tsv is immutable. Append only.
- NEVER cherry-pick evaluation seeds. Run the full eval suite or
  report nothing. Partial evaluations are not valid.

## Soft Constraints

- Prefer changes to train.py over changes to model.py. Training
  dynamics are easier to reason about than architecture changes.
- Prefer hyperparameter changes over code changes when exploring
  a new direction. Cheaper to test, easier to revert.
- Avoid experiments that are purely speculative with no theoretical
  or empirical basis. Each hypothesis should have a rationale.
