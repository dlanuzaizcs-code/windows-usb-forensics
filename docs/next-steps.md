# Next steps (private preparation)

1. Extract this **overlay** into a clean checkout of the existing PRIVATE `windows-usb-forensics` repository (do not copy any original `.git/`).
2. Run Python syntax checks and pytest in a clean Windows 11 environment. Keep testing read-only by default and no USB blocking until recovery is planned.
3. Rotate the TOTP enrollment secret if the supplied database/QR is linked to any live setup. Review original UI screenshots and redact all serials, device instances, QR/TOTP provisioning URIs, usernames and other identifiers; the supplied unredacted images were excluded.
4. Check behavior of trusted storage devices outside configured hours against the current test suite; document the observed outcome.
5. Review key management / TOTP secret storage, integrity claims and Windows permissions.
6. Inspect git diff and history and commit only the intended files to PRIVATE remote.
7. After review, decide between public source and public documentation-only showcase; never change the private repository visibility merely to share the project.
