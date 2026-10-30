# Validation results and limitations

> The following numbers are **reported in the 2026 thesis** (sections 10–11). We have not yet executed the original code in this repository.

## Automated tests

The thesis describes **74 reproducible pytest tests** using isolated temporary databases. It includes unit and integration tests for anomaly modeling, schedule enforcement, TOTP, normalization, persistence and report generation.

**Next task:** obtain the actual `tests/` package, list it, run it in an isolated Windows 11 environment and record the command, Python version, dependency lock, pass/fail counts and known warnings.

## Synthetic detector experiments

### Scenario A: clearly separated classes

45 synthetic sessions: 30 normal, 15 anomalous. For thresholds 0.50–0.70, the thesis reports TP=15, FP=0, TN=30, FN=0. This highly favorable test is **not** an estimate of real-world performance.

### Scenario B: overlapping classes

50 synthetic sessions: 30 normal and 20 anomalous in the reported confusion matrices.

| Threshold | TP | FP | TN | FN | Precision | Recall | F1 | Accuracy |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.40 | 20 | 13 | 17 | 0 | 0.61 | 1.00 | 0.76 | 0.74 |
| 0.50 | 19 | 9 | 21 | 1 | 0.68 | 0.95 | 0.79 | 0.80 |
| 0.60 | 10 | 5 | 25 | 10 | 0.67 | 0.50 | 0.57 | 0.70 |
| 0.70 | 10 | 0 | 30 | 10 | 1.00 | 0.50 | 0.67 | 0.80 |

The thesis reports ROC AUC **approximately 0.87**. Do not present the synthetic measurements as production validation. The default threshold 0.60 performed well with separated classes but not optimally for F1 in the overlapping case.

## Performance experiment

A separate thesis benchmark, `analytics/benchmark.py`, used **1,095 synthetic sessions** representing approximately one year of use and reported end-to-end analysis around 2 seconds. The reproducibility of that result must be checked from the original script and environment.

## Known limitations (thesis section 11.2)

- Synthetic scenarios are not representative of unpredictable production activity.
- Registry/events/SetupAPI provide **indirect** indicators: they do not prove that a particular file was transferred.
- Windows 11 and availability of event channels constrain portability.
- Privileged access is needed for some evidence sources and device disabling.
- Monitoring is active only while the application runs; no independent Windows service was implemented.
- User activity monitoring may require additional retention, privacy and governance controls in organizational settings.
- A raw SHA-256 digest on each event detects some modifications but does not itself establish a fully tamper-evident chain of custody.

## Reproduction plan

1. Preserve an untouched copy of the original source and thesis.
2. Review configuration and any privileged device-control code before execution.
3. Install dependencies from reviewed original manifests in a Windows 11 virtual machine or spare test computer.
4. Execute the real test suite and synthetic experiment; capture commands, outputs and versions.
5. Publish sanitized logs and regenerated graphs only after inspection.
