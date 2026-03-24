# Enforcement

## Pre-Run Checks

Before every training run, the following must pass:

1. **Syntax validation** — `python -m py_compile train.py` must
   exit 0. If it fails, the experiment is aborted before training.
2. **Git status clean** — `git status --porcelain` must show no
   uncommitted changes. All modifications must be committed before
   training begins.
3. **Eval harness integrity** — SHA-256 checksum of `eval.py` must
   match the baseline checksum stored in `.eval_checksum`. If it
   does not match, the experiment is blocked and logged as a
   violation.
4. **Branch check** — Current branch must not be `main`. All
   experiments run on feature branches.

## Runtime Monitoring

- **Watchdog process** — A separate process monitors wall clock
  time. If training exceeds 10 minutes, the process is killed
  with SIGTERM, then SIGKILL after 10 seconds.
- **VRAM monitor** — Polls `nvidia-smi` every 30 seconds. If
  VRAM usage exceeds the configured limit by more than 20%, the
  run is terminated.

## Post-Run Validation

1. **Metric comparison** — val_bpb is compared to baseline. If
   improved, the branch is merged to main. If not, the branch is
   deleted and the result is logged with `kept=false`.
2. **Results integrity** — results.tsv must have exactly one new
   row. If it has zero or more than one, the experiment is flagged.
3. **Reproducibility spot-check** — Every 5th successful experiment
   is re-run with the same seed to verify the result is stable.

## Drift Detection

- If 5+ consecutive experiments show no val_bpb improvement,
  trigger an alert in the experiment log and force a strategy
  shift (see ESCALATION.md).
- If MFU drops below 30% for 3+ consecutive runs, flag a
  potential hardware or configuration regression.
- If training time variance exceeds 20% across similar configs,
  investigate system-level interference.
