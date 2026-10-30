# Reviewed source snapshot (private staging)

This folder contains the **actual Python application modules and pytest tests** extracted from `TFM_Project.zip` on 30 October 2026. The original ZIP also contained a virtual environment, nested Git metadata, runtime databases, backup databases, logs and reports; those have **not** been copied here. This is a selected source snapshot, not a byte-for-byte archive of the original project or its Git history.

## What it does

- `main.py`: PyQt6 desktop entrypoint.
- `acquisition/`: Registry, EVTX, SetupAPI, connected device state and activity.
- `normalization/`: event normalization and USB session correlation.
- `store/`: SQLite schema and evidence storage.
- `analytics/`: explainable anomaly scoring, model, validation and prevention policy.
- `monitoring/`: application-dependent background monitoring.
- `security/`: schedule, privileges and TOTP operations.
- `reporting/` and `ui/`: reports and GUI.
- `tests/`: the provided automated test suite.

## Run only on an authorized Windows test machine

Python 3.13 recommended (based on supplied project environment):

```powershell
cd src
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe main.py
```

**Caution:** the application's strict mode can request device disable/enable actions via PowerShell when enabled and elevated. Use a spare authorized USB device, review settings and ensure recovery access. Do not run with administrator privileges for first inspection. See `SECURITY.md`.

## Validation performed on imported snapshot

- Parsed all **65 selected Python modules/tests** using Python AST: **0 syntax errors**.
- `pytest` on Linux/Python 3.13 with available dependencies: **96 passed, 2 failed**. The two failures require the missing `pyotp` library; they are **environment failures**, not evidence that the TOTP implementation works or fails on Windows.
- On 30 October 2026 the project owner executed the full suite on Windows with dependencies installed: **98 passed in 9.22s**.
- No end-to-end GUI testing, real Windows artifact access, or USB hardware blocking was performed as part of this review.

Some tests now present in the source are newer than the **74 tests** cited in the submitted June 2026 thesis. Do not mix the counts without dates and environment descriptions.
