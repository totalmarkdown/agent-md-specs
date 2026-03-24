# Budget

## Compute Budget

- **Per-experiment:** 5 minutes wall clock for training.
- **Evaluation:** 2 minutes maximum for the full eval harness.
- **Total overhead:** Branch creation, code modification, and
  logging should take under 1 minute combined.
- **Effective cycle time:** ~8 minutes per experiment maximum.

## Hardware Budget

- **VRAM:** Stay within the available GPU memory. No spilling to
  system RAM — it invalidates timing benchmarks and MFU metrics.
- **VRAM headroom:** Peak usage must not exceed 80% of available
  VRAM to leave room for fragmentation and eval overhead.
- **Disk:** Results and checkpoints should not exceed 10 GB total.
  Discard checkpoints from failed experiments.

## Financial Budget

Not applicable. All compute is local. There are no API calls, no
cloud instances, no metered resources. This constraint exists to
document the absence — if the setup changes to cloud compute,
this section must be updated with hard spending limits.

## Complexity Budget

At equal val_bpb performance, always prefer the simpler solution.
Complexity is measured informally:
- Fewer lines of code changed = simpler.
- Fewer new hyperparameters = simpler.
- Fewer dependencies between components = simpler.
- Easier to explain in one sentence = simpler.

If two approaches yield the same val_bpb delta, the one with fewer
lines changed wins. This is a hard rule, not a preference.
