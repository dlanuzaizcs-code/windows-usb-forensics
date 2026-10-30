# Windows USB Forensics — application source

This directory contains the final selected Python application snapshot, extracted from the completed 2026 Master's thesis project. Runtime databases, logs, virtual environments, generated reports and previous local Git history are excluded.

## Modules

| Path | Responsibility |
| --- | --- |
| `main.py` | PyQt6 application entry point |
| `acquisition/` | USB Registry, EVTX, SetupAPI and live Windows signals |
| `normalization/` | Source normalization and evidence correlation |
| `store/` | SQLite storage and evidence model |
| `analytics/` | Anomaly scoring, baseline, experiments and prevention |
| `monitoring/` | Monitoring cycles and newly connected devices |
| `security/` | Schedule, privilege checks and TOTP |
| `ui/`, `reporting/` | Desktop interface and export |
| `tests/` | pytest tests with mocks and temporary state |

## Automated tests on Windows

Use a local Windows 11 testing environment and Python 3.13:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest -q
```

The project author ran the complete suite on Windows on 30 October 2026: **98 passed in 9.22 seconds**. This supersedes the earlier 96-passed/2-missing-`pyotp` result observed during a separate Linux review. It does not verify physical device blocking or all GUI/hardware behavior.

To inspect the interface, run `main.py` in **standard-user mode** only after reviewing `../SECURITY.md`. The strict policy may attempt to disable USB hardware when the application is elevated; do not use it with important devices or without a recovery path.

The project is complete; no additional feature development or CI maintenance is planned.
