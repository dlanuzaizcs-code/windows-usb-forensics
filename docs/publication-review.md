# Pre-publication security and licensing review

**Initial state: PRIVATE.** This checklist is deliberately conservative. Complete it before changing this repository to public or uploading the original code.

- [ ] Confirm source ownership, university agreement/restrictions, dependency licenses and rights to redistribute third-party assets.
- [ ] Preserve original project and create a **sanitized copy** for publication. Do not alter the only original.
- [ ] Inspect the entire source tree and any previous Git history for secrets, passwords, tokens, test credentials, private keys, TOTP seeds and QR codes.
- [ ] Exclude real forensic evidence: Registry hives, `.evtx`, SetupAPI logs, database files, report exports, device serial numbers, VID/PID+serial combinations if identifying, user names, machine identifiers and identifiable timestamps.
- [ ] Review Windows paths, usernames, IPs, email addresses, temporary file names, logs and absolute paths inside code, comments and test outputs.
- [ ] Review screenshots one by one: crop/mask identifiers **before** export and remove metadata/EXIF. Do not upload screenshots showing TOTP QR codes, backup codes or personal data.
- [ ] Inspect Python configuration/requirements, build files, notebooks, archives, binaries and dependencies for hard-coded secrets or executables with unclear provenance.
- [ ] Review any privileged PnP-device-disable/re-enable logic for safe boundaries and recovery behavior; do not publish dangerous default-on instructions.
- [ ] Use synthetic examples and distinct DEMO labels where appropriate.
- [ ] Run the **actual original** automated tests and record results independently of the written thesis.
- [ ] Manually inspect `git diff --cached --name-status` and `git diff --cached` before first push, then review the GitHub tree.
- [ ] Perform an independent sensitive-data scan (e.g., Gitleaks where available) across working tree and, once the history exists, across Git history. A scanner does not replace manual review.
- [ ] If secrets were ever committed, do not merely delete them in a later commit: rotate affected credentials and consider history rewriting or starting with a clean public repository.
- [ ] Confirm README claims match actual source and test outputs; document limitations honestly.
- [ ] Authorize visibility change separately, only after final content review.

Recommended folders for unreviewed originals, **outside** this Git checkout: private source, complete thesis, original screenshots, original Windows logs, original databases and any credentials.
