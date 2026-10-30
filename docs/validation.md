# Validation and limitations

## Reported in the June 2026 academic thesis

- 74 pytest tests described at submission.
- 45 synthetic sessions with separated classes: at thresholds 0.50–0.70, the reported experiment reaches 1.00 precision, recall and F1; this is an **easy, intentionally separated** setting.
- 50 synthetic sessions with overlapping classes: ROC AUC **approximately 0.87**. At threshold 0.50, reported precision **0.68**, recall **0.95**, F1 **0.79**, accuracy **0.80**. At threshold 0.70, recall falls to **0.50** despite precision **1.00**.
- Separate benchmark with 1,095 synthetic sessions: processing around 2 seconds in the thesis experiment.

These values are not enterprise detection metrics, are **not independently rerun here**, and should not be presented without synthetic-data context.

![Threshold comparison — separated synthetic classes](../screenshots/experiment-1-threshold-metrics.png)

![ROC — overlapping synthetic classes](../screenshots/experiment-2-roc.png)

## Source inspection on 30 October 2026

Input: `TFM_Project.zip`, filtered to own code without `.git`, `.venv`, caches, databases, reports and logs.

- Python 3.13 AST syntax check: **65 selected files parsed**, **0 syntax errors**.
- Tests on Linux/Python 3.13 with local available dependencies: **96 passed, 2 failed because `pyotp` was not installed**; failing tests `test_totp_generar_y_verificar` and `test_totp_uri_y_qr` from `tests/test_schedule_totp.py`.
- Real Windows 11 artifact acquisition, PyQt6 GUI, TOTP and physical USB device blocking were **not** independently executed.

## Reproduce on Windows in isolated testing environment

From the `src` directory:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest -q
```

**No automated USB blocking tests should run against critical or unauthorized hardware.** Save test output, version information and screenshots of **sanitized** data for the public evidence section.

## Important limitations

- Real world false-positive and detection rates are unknown.
- Evidence of file transfer is indirect; timestamps may be incomplete or vary by Windows version.
- EVTX access and physical device control depend on privileges and availability.
- Monitoring runs while the GUI application is active, not as a standalone Windows service.
- Per-event hashes are not a tamper-evident chained log.
- TOTP secret at rest is handled through local configuration; review storage security before operational use.
