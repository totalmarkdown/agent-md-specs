---
spec_name: "OUTPUT.md"
spec_version: "1.0.0"
category: Example
tier: extended
agent_name: "Nova"
agent_version: "1.0.0"
---

# Output

## Required Metrics

Every experiment must produce the following measurements:

- **val_bpb** — Validation bits per byte. The primary metric.
- **training_seconds** — Wall clock time for the training run.
- **peak_vram_mb** — Peak GPU VRAM usage during training.
- **mfu_percent** — Model FLOPS Utilization as a percentage.
- **total_tokens_M** — Total tokens processed, in millions.

## Results Log

All results are appended to `results.tsv` (tab-separated values).
This file is append-only. Never modify or delete existing rows.

### Schema

```
experiment_name	branch	val_bpb	baseline_val_bpb	delta	training_seconds	peak_vram_mb	mfu_percent	kept
```

### Example Rows

```
baseline	main	1.0842	1.0842	0.0000	287	6144	38.2	true
lr_warmup_400	exp/lr-warmup-400	1.0791	1.0842	-0.0051	291	6148	38.0	true
rope_scaling	exp/rope-scaling	1.0903	1.0842	+0.0061	295	6210	37.8	false
```

### Conventions

- `delta` is `val_bpb - baseline_val_bpb`. Negative is better.
- `kept` is `true` if the branch was merged, `false` if discarded.
- Rows are ordered chronologically. The first row is always baseline.
- Use lowercase_snake_case for experiment names.
