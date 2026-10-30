# Final publication checklist (one-time; project development is complete)

The original thesis project is finished. **No recurring GitHub Actions or development maintenance are planned.**

## Completed (30 October 2026)

- Copied the selected application code to a clean private GitHub repository without original `.git/` history, virtual environments or local runtime databases.
- Confirmed `src/tfm_usb.db` is excluded by `.gitignore` and untracked.
- Ran the full automated test suite on Windows with dependencies installed: **98 passed in 9.22s**.
- Pushed the selected source and documentation to the **private** `main` branch.

## Still required before any public release

1. Ensure the original TOTP QR/enrollment secret is not used for any live setup; rotate it if applicable.
2. Review every tracked source file and the entire current Git history for sensitive data, personal identifiers, logs and credentials.
3. Inspect the three included figures individually and sanitize any new screenshots (USB serials, instance IDs, names, timestamps, QR/OTP secrets, file paths, EXIF).
4. Reconcile the strict-mode trusted-device / out-of-hours behavior between implementation, tests and thesis. This is documentation, not a request to change finished application behavior.
5. Check ownership/academic redistribution conditions, and make an explicit choice about publishing source code and a license.
6. Decide whether to publish the code or create a separate public documentation-only showcase. Keep this repo **private** until these checks are complete.

Passing automated tests does **not** prove full security, real-hardware behavior or production readiness.
