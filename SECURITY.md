# Security considerations

This completed Master's thesis project is a **research prototype for authorized Windows 11 testing**, not production endpoint security software.

## Running the application

- Begin with a standard-user account in an isolated Windows test environment.
- Some EVTX sources are unavailable without administrator privileges; the application can operate with incomplete evidence.
- **Strict mode** can attempt to disable a Plug and Play USB device through `Disable-PnpDevice` when elevated. Use disposable test hardware, a recovery plan and explicit authorization; never trial it on critical drives, keyboards or essential workstation devices.
- TOTP enrollment secrets are stored in **local SQLite configuration**. The prototype does not claim encrypted secret-at-rest storage or hardened recovery suitable for production.
- TOTP verification and physical device blocking are distinct from the statistical detector. Automated unit tests do not establish end-to-end hardware safety.

## Privacy and forensic limitations

- Never commit or share runtime SQLite databases, backup files, raw Registry / EVTX / SetupAPI artifacts, real USB serials, usernames, exported reports or activity logs.
- Never publish TOTP provisioning QR codes, `otpauth://` URIs, recovery codes or authentication secrets. Rotate any credential that has been shared.
- Event timestamps, source correlation and per-event SHA-256 do **not** prove file transfers, adversarial intent or an immutable chain of custody.
- Collection of user activity in a workplace requires appropriate organizational authorization, access controls, retention limits and legal assessment.

For private vulnerability reports, contact the maintainer through the GitHub profile.
