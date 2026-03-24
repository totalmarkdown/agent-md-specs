# Goals

## Primary Objective

Minimize validation loss (val_bpb — bits per byte) on the held-out
validation set within a fixed compute budget. Every experiment must
be measured against the established baseline.

## Secondary Objective

Maintain code simplicity. Improvements that require disproportionate
complexity are deprioritized. The codebase should remain readable by
a single engineer unfamiliar with the project history.

## Tertiary Objective

Maximize Model FLOPS Utilization (MFU). Higher MFU means the hardware
is being used efficiently, which stretches the compute budget further.
This is a soft goal — never sacrifice val_bpb for MFU.

## Success Criteria

- val_bpb improves over the established baseline
- Improvement is reproducible across at least 2 random seeds
- Training completes within the per-experiment time budget
- No increase in code complexity that cannot be justified by results

## Measurement

All metrics are logged to results.tsv after every experiment. The
delta column shows improvement (+) or regression (-) relative to the
baseline. A run is considered successful only if delta is negative
(lower val_bpb is better) and the result is reproducible.
