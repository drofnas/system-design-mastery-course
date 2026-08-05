# Home Lab Guide

The canonical capstone freeze points are Weeks 16, 33, 50, 68, 85, and 103.
The separate capstone delta points are Weeks 17, 34, 51, 69, 86, and 104.
Preserve the Week 1 baseline and every earlier artifact; later evidence belongs
in a new file rather than an edit to frozen history.

All 17 executable course labs target one home computer. A discrete GPU, cloud
account, Kubernetes cluster, Kafka cluster, or second person is not required.
WSL2 support remains provisional until the complete matrix passes on a real
Windows 11 host. Run the local preflight before beginning a lab:

```bash
python3 scripts/check_home_lab.py
python3 scripts/check_home_lab.py --module M03 --module M15
python3 scripts/check_home_lab.py --json --output home-lab-preflight.json
python3 scripts/check_home_lab.py --module M16 --wsl-browser-callback modules/16-browser-frontend-cdn-edge/lab/wsl-browser-callback.json
```

The preflight is non-installing. It does not pull images, contact an LLM, or
upload data. On WSL2 it launches and removes one bounded, network-disabled
container from the already-cached M03 image, launches and closes the pinned
Chromium binary, and performs an npm offline dry run. These probes verify actual
resource enforcement and cache readiness without downloading a missing input.
The report contains only coarse platform/tool/resource facts and does not emit
usernames, hostnames, tokens, or absolute home paths. Exit status `0` means no
blocker was found (warnings are allowed), `1` means at least one blocker needs
remediation, and `2` means the invocation or preflight itself was invalid.

## Hardware lanes

| Lane | Minimum |
|---|---|
| Portable learning | 2 logical CPUs, 8 GiB RAM, 20 GiB free, Python 3.11 |
| Full local evidence | 4 logical CPUs, 16 GiB RAM, 40 GiB free, loopback, Docker/Podman or pinned native toolchains |
| Windows/WSL2 | 16 GiB physical RAM, 8 GiB assigned to WSL, 4 GiB Docker allocation, 40 GiB inside WSL; 24/12 GiB recommended |
| Optional accelerator | Any explicitly recorded GPU or MPS device; never required |

One-time internet access is needed to clone the course and obtain container
images, language toolchains, packages, and Chromium. Once those inputs are
cached, the Python-only labs work offline. Container and Node labs work offline
only while every pinned image and package is already cached. Link verification,
package installation, and cache misses still require a network connection.

## macOS setup

Use a currently supported macOS release on Intel or Apple silicon.

1. Install Xcode command-line tools with `xcode-select --install`.
2. Install Python 3.11 or newer and Node as required by the selected module.
3. Confirm `python3`, `git`, `cc`, `make`, `openssl`, `node`, and `npm` are on
   `PATH`.
4. Install Docker Desktop and start it before Modules 3 or 15.
5. Give Docker Desktop at least two CPUs and 3 GiB memory for Module 15.

Run commands in Terminal from the repository root. The Module 3 native and
Docker commands are identical to Linux. Docker evidence on macOS crosses the
Docker Desktop Linux virtual-machine boundary; record that boundary.

## Ubuntu LTS setup

Use a currently supported 64-bit Ubuntu LTS release.

1. Install the distribution compiler/build-tool package, Python 3.11+, Git,
   Node/npm, OpenSSL, and `make`.
2. Install Docker Engine from Docker's Ubuntu repository and confirm the daemon
   is running.
3. Confirm the current user can run the lab's Docker commands, or use the
   documented Docker privilege model consistently and record it.
4. Run all course commands from a normal shell inside the repository.

Linux containers are still an evidence boundary: record the pinned image,
limits, host architecture, and whether a native toolchain was substituted.

## Windows through WSL2

Native Windows and native PowerShell are not supported lab environments. Use
Windows 11 with Ubuntu on WSL2 for the provisional support matrix.

1. From an elevated Windows terminal, install WSL with `wsl --install`, restart
   if requested, and complete Ubuntu's first-run setup.
2. Install the Ubuntu tools listed above inside WSL, not in PowerShell.
3. Install Docker Desktop for Windows, enable the WSL 2 engine, and enable
   integration for the Ubuntu distribution.
4. Clone and store the repository inside the WSL filesystem, such as
   `/home/<you>/src/system-design-mastery-course`. Do not run the labs from
   `/mnt/c`; cross-filesystem I/O can distort measurements and slow builds.
5. Run Python, Docker, Node, and all lab commands in the Ubuntu shell.
6. For Module 16 manual checks, serve from WSL on loopback and open
   `http://localhost:<port>` in a normal Windows browser.
7. Verify cgroup CPU, memory, and PID enforcement; Docker's assigned memory;
   guest loopback; the Windows-browser callback; Chromium launch; free disk;
   and the pinned offline cache before collecting evidence.

For M16, first run the one-time callback from the module lab and open the printed
URL in a normal Windows browser:

```bash
python3 host_browser_callback.py --output wsl-browser-callback.json
```

Then pass that source-bound, token-free record to the root preflight with
`--wsl-browser-callback`. A missing, malformed, stale-commit, or failed callback
is a blocking M16 result. The cgroup probe also blocks M03/M15 evidence unless
the cached container proves all three effective limits; file visibility alone
is not enough. Offline readiness is evaluated only for selected M03, M15, and
M16 lanes and fails closed on any missing pinned image, package, or browser.

The preflight reports native Windows as unsupported and points to WSL2. Windows
on ARM, Hyper-V-only Docker, and locked-down managed devices are outside the
supported baseline until separately verified.

## Remote fallback runner

An official remote container runner may be used when a machine cannot run
Docker, loopback, or Chromium. It is a fallback, not a cloud prerequisite.
Accepted remote evidence records the learner commit, image digest, runner
version, scenario/input/configuration hashes, resource limits, clock, raw output,
and limitations. The remote runner cannot turn fixture replay into independent
Build, Break, Implement, or Measure evidence.

## Evidence modes and trial record

Declare exactly one of `derived`, `executed_deterministic`,
`measured_loopback`, `measured_container`, `modeled_capacity`, `fixture_replay`,
or `measured_accelerator`. Fixture replay is practice/remediation evidence only.
Modeled accelerator, region, fleet, or device results may support Calculate and
Decide but are not local measurements.

Every executed or measured trial records source commit, scenario/input/config
hashes, runtime boundary, CPU/memory/PID limits, clock, warm-up/repetition policy,
raw outcomes, and limitations.

Lab-specific JSON is the raw mechanism result, not the complete provenance
record. Freeze it with `scripts/write_evidence_envelope.py`; the writer verifies
that every declared input and configuration is byte-identical to the recorded
source commit, hashes the raw outcomes, refuses overwrite, and marks fixture
replay, derived work, and modeled capacity as ineligible for independent
Build/Break/Implement/Measure credit. For example:

```bash
python3 scripts/write_evidence_envelope.py --module M10 \
  --mode executed_deterministic --input modules/10-time-coordination-consensus/lab/scenarios/f01-leader-termination-repaired.json \
  --config modules/10-time-coordination-consensus/lab/consensus_lab/config.py \
  --raw-outcome experiments/m10-f01-raw.json --runtime-boundary local_native \
  --runtime "Python 3.11+" --cpu-limit host-controlled --memory-limit host-controlled \
  --pid-limit host-controlled --clock-source logical-ticks \
  --timing-boundary "scenario start through oracle completion" --warmups 0 \
  --repetitions 1 --exclusion-policy none \
  --limitation "Local deterministic execution does not establish regional or physical-durability behavior." \
  --output experiments/m10-f01-evidence-envelope.json
```

## Module dependency matrix

| Modules | Required local capabilities | Typical first-use download | Low-resource notes |
|---|---|---|---|
| 2, 4, 6–14, 17, 18 | Python 3.11+, Git, loopback where used | none beyond repository | Run scenarios serially; M09–M12 reuse the shared three-process cluster/proxy contract. |
| 3 | Python, C11 compiler, `make`, Docker | pinned GCC image | Matrix is serial; assign Docker two CPUs and at least 256 MiB per trial. |
| 5 | Python, OpenSSL, TCP/UDP loopback | none beyond repository | Certificates and servers are temporary and unprivileged. |
| 15 | Python, Docker; or exact native toolchains | four pinned toolchain images/packages | Run one runtime at a time; each container is capped at 2 CPUs, 3 GiB memory/swap, and 256 PIDs. |
| 16 | Node/npm, Chromium headless shell, loopback; host browser for manual work | npm packages and Chromium | Automated tests use one worker and retain traces only on failure. |

No module needs a GPU. Module 17 executes and profiles the course's actual tiny
transformer path; it does not download or execute a production model.
Integrated graphics are sufficient for every lab.

## Low-resource operation

- Close memory-heavy applications before Modules 3, 15, and 16.
- Keep required matrices complete, but run their scenarios or runtimes
  serially. Do not treat a reduced matrix as assessment evidence.
- Module 3's 64-worker case demonstrates scheduler oversubscription; it does
  not require 64 CPU cores.
- Preserve only graded raw evidence. Build caches and downloaded images are
  reproducible inputs and may be cleaned after a module.
- If the machine starts swapping heavily, stop the run, record the invalid
  condition, reduce unrelated load, and rerun. Do not reinterpret a host-memory
  failure as a lab result.

## Loopback, firewall, and filesystem troubleshooting

- Labs bind only `127.0.0.1`. If binding fails, allow the local Python or Node
  process through host security software. Do not expose the service on a public
  interface as a workaround.
- In WSL2, test `localhost` from the Windows browser. Restart WSL and Docker
  Desktop if integration was changed after a shell was opened.
- If temporary-file creation fails, confirm the repository and operating-system
  temporary directory are writable and have free space. Do not redirect lab
  temporary files into a shared or production directory.
- Docker daemon errors are setup blockers, not experiment results. Start Docker
  and rerun the preflight.

## Cache cleanup and recovery

Use each tool's normal inspection command before cleanup. Remove only caches or
unused images you recognize; never delete learner submissions or `.course-private`
blind envelopes. Package caches and Docker images must be downloaded again
before the corresponding lab can run offline. A failed lab may leave a build
cache, but bounded trial data belongs in the output path the learner selected.

## Solo review and blind diagnosis

Human review is preferred and is the stronger portfolio signal. A learner
working alone may instead prepare a scripted five-question review, record the
answers without live AI assistance, and freeze the artifact and responses. That
frozen record completes the solo teach-back. Provider-neutral LLM critique may
be requested afterward as an optional independent upgrade. Disclose the review
mode and its limitations. See `templates/solo-review-record-template.md`.

Modules 4 and 5 also provide `blind-solo-prepare` and `blind-solo-reveal`.
Their `.sblind` envelope provides accidental-exposure protection; it is not
encryption or anti-cheating. The learner can bypass it by inspecting source or
decoding the envelope. Reveal is allowed only after the diagnosis is committed
and byte-identical to the committed version.

## External setup resources

These sources reinforce the complete local instructions above; no external
page is required while completing a lab. All are free and were last verified
on 2026-08-04.

| Title | Publisher | Type / status | Purpose and exact boundary | Time / week | Local alternative | Reflection or evidence |
|---|---|---|---|---|---|---|
| [Install WSL](https://learn.microsoft.com/en-us/windows/wsl/install) | Microsoft | Documentation; required for Windows path; free | Read through installation, distribution choice, first launch, and WSL-version checks. Ignore optional development tutorials. | 15 min; before first lab | Follow the six Windows-through-WSL2 steps above. | Save the sanitized preflight platform and WSL result. |
| [Docker Desktop WSL 2 backend](https://docs.docker.com/desktop/features/wsl/) | Docker | Documentation; required for Docker labs on Windows; free | Read prerequisites, WSL 2 engine, distribution integration, filesystem placement, and resource behavior. | 15 min; before M03 | Follow the Docker and repository-placement steps above. | Record Docker boundary and assigned CPU/memory. |
| [Install Docker Desktop on Mac](https://docs.docker.com/desktop/setup/install/mac-install/) | Docker | Documentation; required for Docker labs on macOS; free | Read architecture selection, supported macOS, installation, and first launch only. | 10 min; before M03 | Follow the macOS setup steps above. | Save Docker version and host boundary without host identity. |
| [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/) | Docker | Documentation; required for Docker labs on Ubuntu; free | Read supported releases and repository installation through verification. Do not copy unrelated production hardening steps into the lab. | 20 min; before M03 | Follow the Ubuntu setup steps above using the distribution's supported packages. | Save daemon/version check and privilege model. |
| [Browsers: Chromium](https://playwright.dev/docs/browsers) | Microsoft Playwright | Documentation; required for M16 automation; free | Read Chromium install, `--only-shell`, and Linux dependency installation. Other browsers and branded channels are outside this lab. | 10 min; M16 | Use the platform commands in the Module 16 lab README. | Record the pinned Node/Playwright inputs and whether automation used the headless shell. |

If a source changes or is unavailable, use the local steps, record the date and
the specific uncertainty, and do not invent a setup result.
