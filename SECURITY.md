# Security and privacy (private preparation)

The USB forensic tool is a research prototype that accesses local Windows artifacts and may disable USB devices when its optional **strict / physical blocking** features are enabled.

- **No real evidence in Git:** exclude SQLite database files, backups, Event Logs, raw Registry or SetupAPI exports, HTML/JSON reports, activity logs, and device identifiers.
- **TOTP:** configuration stores a TOTP secret in the local SQLite configuration table; the supplied database **contains a nonempty secret** (confirmed without displaying it). The original supplied screenshot `10.x_TOTP.png` contains a real-looking provisioning QR and URI and **is intentionally excluded**. **Regenerate the TOTP secret if this QR was ever used for a live account/device.** Never publish QR, provisioning URI or backup codes.
- **Admin privileges:** never run or test physical USB blocking on a workstation or storage device without owner authorization and an established recovery path. Prefer standard-user mode for first tests.
- **History exposure:** importing a separate old Git repository, even with a new `.gitignore`, may expose secrets and files in earlier commits. Copy only selected source files into the clean current repository; never copy a nested `.git/` folder.
- **Evidence limitations:** USB artifacts and SHA-256 per event do not independently establish physical file transfers or forensic chain of custody.
- **Privacy:** consider access controls, data minimization, retention and applicable laws before collecting employee activity or deploying in corporate environments.

Contact the repository owner privately through their profile links for security concerns.
