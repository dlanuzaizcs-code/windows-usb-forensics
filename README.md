# Windows USB Forensics & Explainable Anomaly Detection

**Master's thesis (Cybersecurity) · University of Alicante · 2026**  
**Author:** Diego Lanuza Izquierdo

> **Private staging release. Do not make this repository public yet.** The source and a carefully selected set of visuals are included; review the implementation, personal-data handling, security controls, screenshots, software rights, and Git history before publishing.

A Windows 11 forensic desktop prototype that reconstructs USB activity from Windows Registry, Event Logs and SetupAPI; correlates evidence in SQLite; scores behavioral deviations; and offers configurable defensive response with a PyQt6 interface and HTML/JSON reports.

## Highlights

- Forensic reconstruction using Registry / USBSTOR, EVTX and SetupAPI.
- Correlation and deduplication of removable-device sessions.
- SQLite evidence persistence with per-event SHA-256 (not a tamper-proof chain of custody).
- Explainable anomaly score across time rarity, device rarity and Mahalanobis distance.
- Learning, monitoring and strict modes; optional device blocking and TOTP verification.
- GUI for device, alert and activity statistics; export to HTML / JSON.

## Architecture

![Six-layer architecture of the USB forensic application](screenshots/architecture-six-layers.png)

[Architecture details](docs/architecture.md) · [Source layout / local setup](src/README.md) · [Security notes](SECURITY.md)

## Technical stack

Python 3.13 · PyQt6 · SQLite · python-registry / winreg · EVTX · NumPy / SciPy / pandas · Jinja2 · pyotp · pytest.

## Results and reproducibility

The June 2026 thesis reports **74 tests** and an AUC of approximately **0.87** on an overlapping-class **synthetic** experiment (50 sessions); it is a controlled research result, not an enterprise detection benchmark. A separate synthetic benchmark of 1,095 sessions took approximately 2 seconds in the documented test setting.

A new source inspection on 30 October 2026 found **65 selected Python files** in the delivered snapshot and executed pytest in Linux/Python 3.13: **96 passed, 2 could not run successfully because `pyotp` was not installed**. Full Windows 11 GUI and hardware behavior are **not** independently verified in this review.

![ROC of the overlapping synthetic experiment](screenshots/experiment-2-roc.png)

See [Validation](docs/validation.md) for methodology and limitations.

## Source

The application source is under [`src/`](src/). It was copied from the supplied original project while excluding runtime/private artifacts, nested Git history and the virtual environment. On Windows, install dependencies inside a fresh environment and run the tests **before** attempting normal use. See [`src/README.md`](src/README.md).

## Publication boundary

This repository is still **private**. It does **not** contain original SQLite data, generated reports, logs, original Git history, raw Windows forensics, unreviewed device screenshots or TOTP enrollment screenshots. Even so, the source should receive another manual code and history review before going public.

[Publication audit](docs/publication-review.md) · [Next steps](docs/next-steps.md)

**Portfolio:** [diegolanuza.es](https://diegolanuza.es) · **Cyber defense lab:** [soc-homelab-showcase](https://github.com/dlanuzaizcs-code/soc-homelab-showcase)

**License:** not selected pending rights review. No blanket permission to redistribute the code is granted.
