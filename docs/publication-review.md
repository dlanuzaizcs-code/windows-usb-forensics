# Pre-publication security review — status 30 October 2026

**Status: REVIEW REQUIRED; repository stays PRIVATE.**

## Reviewed and excluded from provided source archive

- Root and nested `.git/` history (two Git repositories were present in the uploaded ZIP).
- `.venv/` (third-party dependencies, libraries and binaries; the source ZIP was >200 MB).
- `.pyc`, `__pycache__`, pytest caches.
- `tfm_usb.db` and three backup database files, containing device records and private local state. **Read-only inspection confirmed a nonempty `totp.secret` configuration value in the supplied SQLite database.** The value was not displayed or exported.
- `tfm_usb.log`, generated reports in `informes/` (realistic identifiers/timestamps), extra local documentation and prompt/agent context files.
- Original screenshot `10.x_TOTP.png` (contains QR and provisioning URI).
- Remaining GUI screenshots (possible USB serials and activity timestamps); deferred pending manual redaction.
- Local demo script `generar_alertas_demo.py` (can write to the application database; excluded from this public-oriented source snapshot).

## Included after preliminary review

- Original Python modules and tests (65 `.py` files, excluding the standalone demo alert generator).
- Original `requirements.txt`, GUI icon assets.
- Three metadata-stripped figure PNGs: architecture and the two synthetic experiment charts.
- Revised README and privacy/security/validation documents.

## Checks performed

- Source text scanned heuristically for static credentials, email addresses, private IPs and absolute user paths. No obvious embedded real credential or private IP found in selected source code. **A heuristic scan cannot prove secret-free status.**
- AST parse of 65 selected Python files completed without errors.
- Linux pytest: 96 passed, 2 blocked by missing pyotp; this is not a Windows validation.
- Sample screenshots visually reviewed at contact-sheet level. Metadata discarded for selected exported figures; a closer human review is still necessary before making public.

## Must-do before visibility change

1. Verify no TOTP secret is in use from excluded screenshot; rotate it if it is.
2. Manually review each selected image and code file, including imports, log statements and error messages.
3. Install dependencies on Windows 11; run tests; validate read-only flow and optional physical blocking ONLY on disposable test USB hardware with recovery plan.
4. Compare strict-mode trusted-device/out-of-schedule behavior against the **actual** source and tests and reconcile thesis wording.
5. Review GitHub repository's **entire commit history**; do not import either original `.git/` folder.
6. Decide whether copyright/academic commitments allow public code distribution; choose a license only after that decision.
7. Use a public test clone to scan tracked files and local Git history; verify all intentionally excluded personal data remains outside the repo.
