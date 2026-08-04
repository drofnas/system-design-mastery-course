# Home Lab Guide

The canonical capstone revision points are Weeks 12, 24, 48, and 72. Preserve
the Week 1 baseline and every earlier revision; later evidence belongs in a new
file rather than an edit to a frozen artifact.

All 17 executable course labs are designed to run on one ordinary home
computer. A discrete GPU, cloud account, Kubernetes cluster, Kafka cluster, or
second person is not required. Run the local preflight before beginning a lab:

```bash
python3 scripts/check_home_lab.py
python3 scripts/check_home_lab.py --module M03 --module M15
python3 scripts/check_home_lab.py --json --output home-lab-preflight.json
```

The preflight is read-only. It does not install packages, pull images, contact
the network, or include a hostname, username, or home-directory path in its
report. Exit status `0` means no blocker was found (warnings are allowed), `1`
means at least one blocker needs remediation, and `2` means the invocation or
preflight itself was invalid.

## Supported baseline

| Resource | Minimum | Recommended |
|---|---:|---:|
| Architecture | 64-bit x86_64 or ARM64 | same |
| Memory | 8 GiB | 16 GiB |
| Logical CPUs | 2 | 4 |
| Free disk before setup | 20 GiB | 30 GiB |
| Graphics | integrated | integrated |
| Python | 3.11 | current compatible 3.x |

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
Windows 10 build 19041 or newer, or Windows 11, with Ubuntu on WSL2.

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

The preflight reports native Windows as unsupported and points to WSL2. Windows
on ARM, Hyper-V-only Docker, and locked-down managed devices are outside the
supported baseline.

## Module dependency matrix

| Modules | Required local capabilities | Typical first-use download | Low-resource notes |
|---|---|---|---|
| 2, 4, 6–14, 17, 18 | Python 3.11+, Git, loopback where used | none beyond repository | Run scenarios serially. |
| 3 | Python, C11 compiler, `make`, Docker | pinned GCC image | Matrix is serial; assign Docker two CPUs and at least 256 MiB per trial. |
| 5 | Python, OpenSSL, TCP/UDP loopback | none beyond repository | Certificates and servers are temporary and unprivileged. |
| 15 | Python, Docker; or exact native toolchains | four pinned toolchain images/packages | Run one runtime at a time; each container is capped at 2 CPUs, 3 GiB memory/swap, and 256 PIDs. |
| 16 | Node/npm, Chromium headless shell, loopback; host browser for manual work | npm packages and Chromium | Automated tests use one worker and retain traces only on failure. |

No module needs a GPU. Module 17 models inference mechanics locally and does
not download or execute a production model.
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
answers without live AI assistance, freeze the artifact and responses, and then
request provider-neutral LLM critique. Disclose that substitution and its
limitations. See `templates/solo-review-record-template.md`.

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
