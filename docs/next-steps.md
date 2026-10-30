# Release roadmap

## Phase 1 — Private documentation scaffold (this package)

- [x] Prepare evidence-grounded README and architecture notes from the June 2026 thesis.
- [x] Add risk/limitations section and publication-safety checklist.
- [ ] Create private GitHub repository `windows-usb-forensics`.
- [ ] Push **only** this reviewed documentation scaffold.

## Phase 2 — Source and evidence audit

- [ ] Provide the original project directory as a ZIP **privately** (not uploaded to public GitHub).
- [ ] Provide candidate screenshots and the original thesis PDF if exact visual verification is needed.
- [ ] Review package manifests, startup code, data paths, privileged operations, dependencies and licenses.
- [ ] Identify safe modules and test fixtures; exclude all original evidence and credentials.
- [ ] Check the claimed 74 tests, reproducing results on a Windows test environment.
- [ ] Resolve schedule/trust-list policy discrepancy from the implementation and tests.

## Phase 3 — Curated public release

- [ ] Commit independently reviewed source and sanitized screenshots.
- [ ] Document minimum Windows/Python versions, permissions and installation steps from the real code.
- [ ] Include screenshots of the device list, alert explanations, analytics dashboard and a synthetic report if privacy review passes.
- [ ] Add CI appropriate for unit-only Windows tests after reviewing dependencies and test isolation.
- [ ] Review full git history, metadata, documentation, access permissions and change visibility to public.
- [ ] Pin repo on GitHub and cross-link from personal README and portfolio.
