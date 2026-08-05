# Home-Lab Readiness Review

- Review date: 2026-08-04
- Epic branch: `feature/course-v2-104-week-redesign`
- Overall gate: **Awaiting platform verification**
- Privacy rule: summaries omit hostnames, usernames, repository/home paths, IP
  details, and machine identifiers.

This record distinguishes real-host execution from mocked unit coverage. Mocked
platform cases validate preflight logic; they do not establish that Docker,
WSL2, browsers, or filesystems behave correctly on those platforms.

## Actual macOS ARM64 host

### Sanitized preflight summary

| Observation | Result |
|---|---|
| Platform / architecture | macOS / ARM64; supported |
| Memory | 16 GiB; recommended baseline met |
| Logical CPUs | 10; recommended baseline met |
| Free disk | 22.3 GiB; minimum met, 30 GiB recommendation not met |
| Python, Git, compiler, make, OpenSSL | Passed |
| Docker CLI and daemon | Passed |
| Loopback bind and temporary files | Passed |
| Node | **Blocked:** host Node 25.9.0 does not match pinned Node 24.19.0 |

Preflight result: 13 pass, 1 warning, 1 blocker. The host must install/select
the pinned Node version and rerun the full preflight before the macOS platform
gate is accepted.

### Executed lab evidence

- Module 3: 24 unit/integration tests passed; the complete required matrix
  produced 38 validated scenario records, including Docker-backed cases.
- Module 4: 20 tests passed with real loopback, including partner and solo
  blind preparation, committed-diagnosis reveal, tamper checks, and overwrite
  rejection.
- Module 5: 24 tests passed with real loopback/TLS, including partner and solo
  blind workflows and integrity failures.
- Module 15: six Python tests passed. The serial `--all` container command
  completed successfully for TypeScript, Go, Rust, and Java with the published
  CPU, memory/swap, and PID limits.
- Module 16: one Python model test, two Node unit tests, and all 18 Playwright
  Chromium checks passed using one worker. This run used the unsupported host
  Node 25.9.0, so it is useful regression evidence but does not close the pinned
  Node 24.19.0 acceptance gate.
- Remaining executable labs: all discovered Python unit suites passed on this
  host.
- Course validator and local-link validation: passed for all 18 modules.

Manual Module 16 checks in a normal host browser were not separately recorded
during this automated session. They remain required learner evidence and a
platform-gate item.

## Supported Ubuntu LTS host

Status: **Not run; awaiting an actual Ubuntu LTS host.**

Required before acceptance:

- [ ] Run the full preflight and save only its sanitized summary.
- [ ] Run all lab unit suites.
- [ ] Run the complete Module 3 native/Docker matrix.
- [ ] Run Module 15 `--all` with Docker Engine and confirm serial order and
  effective resource limits.
- [ ] Run Module 16 Python, Node, and 18 Chromium checks with the pinned Node
  version and one worker.
- [ ] Record Docker Engine, native Linux, and container evidence boundaries.

The preflight unit suite covers Ubuntu x86_64 and ARM64 decision paths, but
those mocks are not substituted for this gate.

## Windows with Ubuntu on WSL2

Status: **Not run; awaiting an actual Windows 10 build 19041+ or Windows 11
WSL2 environment with Docker Desktop integration.** The update must not be
declared ready from mocked WSL2 tests.

Required before acceptance:

- [ ] Store the repository inside the WSL filesystem and run the full preflight.
- [ ] Use the cached, network-disabled probe to prove effective CPU, memory, and
  PID cgroup limits; merely seeing controller files does not pass.
- [ ] Confirm the selected M03/M15 image digests and M16 npm/Chromium inputs are
  present by passing the offline-cache check without downloads.
- [ ] Run every Python lab suite inside Ubuntu on WSL2.
- [ ] Run the complete Docker-backed Module 3 matrix.
- [ ] Run Module 15 `--all` through Docker Desktop WSL integration and confirm
  effective limits and serial order.
- [ ] Install the Chromium-only headless shell with Linux dependencies and run
  all Module 16 automated checks with the pinned Node version.
- [ ] Serve Module 16 on WSL loopback and record keyboard, 200% zoom/reflow,
  JavaScript-disabled, and accessibility checks in a normal Windows browser
  through `localhost`; bind the sanitized callback to the current source commit
  and feed it back into the preflight.
- [ ] Record WSL2, Docker Linux VM, and Windows host-browser boundaries without
  private host data.

The preflight unit suite covers the WSL2 x86_64 decision path and unsupported
native Windows, but those mocks are not substituted for this gate.

## Automated contract evidence

- Preflight tests cover macOS ARM64/x86_64, Ubuntu ARM64/x86_64, WSL2 x86_64,
  native Windows rejection, unknown/low resources, missing and incompatible
  tools, blocked loopback, privacy, output overwrite, module scoping, `/mnt/c`
  rejection, effective cgroup limits, Docker allocation, actual Chromium
  launch, source-bound host callback, and selected offline-cache failures.
- Solo-review tests cover artifact/commit identity, deterministic unique
  selection, seed variation, invalid modules/commits, uncommitted artifacts,
  and answer-field exclusion.
- Module 4/5 blind tests cover premature and modified diagnoses, partner-key
  placement, commit identity, manifest/envelope/bundle integrity, visible-data
  leakage checks, output overwrite, successful reveals, relative paths, hashes,
  and envelope preservation.
- Module 15 tests cover resource-flag construction, disk refusal, one-runtime
  selection, mutual exclusion, serial order, and existing scenario/source
  contracts.
- Course validation requires all new schemas, all 18 solo-review contracts,
  the Home Lab Guide link in each of 17 executable labs, detailed platform
  guidance for Modules 3/5/15/16, Module 15 limits, and Module 16 one-worker and
  evidence-plane configuration.

Capstone baselines remain immutable. PESD 2.0 rubrics, evaluator prompts,
workload matrices, and calibration fixtures pass the deterministic repository
contracts; the required twice-per-band fresh LLM calibration has not yet run
and remains a course-readiness blocker.
