#!/usr/bin/env python3
"""Non-installing, privacy-preserving home-lab readiness preflight."""
from __future__ import annotations

import argparse
import json
import os
import platform
import re
import shutil
import socket
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
ALL_MODULES = tuple(f"M{i:02d}" for i in range(1, 19))
DOCKER_MODULES = {"M03", "M15"}
COMPILER_MODULES = {"M03"}
OPENSSL_MODULES = {"M05"}
NODE_MODULES = {"M16"}
LOOPBACK_MODULES = {"M02", "M04", "M05", "M06", "M09", "M10", "M11", "M12", "M16", "M17", "M18"}
WSL_DOCKER_MODULES = {"M03", "M15"}
WSL_OFFLINE_MODULES = {"M03", "M15", "M16"}
M03_IMAGE = "gcc:15.2.0-bookworm"


def _run_version(command: list[str]) -> str | None:
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=5, check=False)
    except (OSError, subprocess.SubprocessError):
        return None
    text = (result.stdout or result.stderr).splitlines()
    return text[0].strip() if text else None


def _version_tuple(text: str | None) -> tuple[int, ...] | None:
    if not text:
        return None
    match = re.search(r"(\d+)\.(\d+)(?:\.(\d+))?", text)
    return tuple(int(part) for part in match.groups(default="0")) if match else None


def _command_supports(command: list[str], token: str) -> bool:
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=5, check=False)
    except (OSError, subprocess.SubprocessError):
        return False
    return token in f"{result.stdout}\n{result.stderr}"


def _platform_kind() -> str:
    system = platform.system().lower()
    if system == "darwin":
        return "macos"
    if system == "windows":
        return "windows-native"
    if system != "linux":
        return "unknown"
    release = ""
    try:
        release = Path("/proc/sys/kernel/osrelease").read_text(encoding="utf-8").lower()
    except OSError:
        pass
    if "microsoft" in release:
        return "wsl2-ubuntu" if "wsl2" in release or "microsoft-standard" in release else "wsl1-unsupported"
    if os.environ.get("WSL_INTEROP"):
        return "wsl1-unsupported"
    try:
        os_release = Path("/etc/os-release").read_text(encoding="utf-8").lower()
    except OSError:
        os_release = ""
    return "ubuntu" if "id=ubuntu" in os_release else "linux-other"


def _architecture() -> str:
    machine = platform.machine().lower()
    if machine in {"x86_64", "amd64"}:
        return "x86_64"
    if machine in {"arm64", "aarch64"}:
        return "arm64"
    return "unsupported" if machine else "unknown"


def _ram_gib() -> float | None:
    try:
        if platform.system() == "Darwin":
            value = subprocess.run(["sysctl", "-n", "hw.memsize"], capture_output=True, text=True, timeout=5, check=True).stdout.strip()
            return round(int(value) / 2**30, 1)
        if platform.system() == "Linux":
            match = re.search(r"^MemTotal:\s+(\d+)\s+kB", Path("/proc/meminfo").read_text(encoding="utf-8"), re.MULTILINE)
            return round(int(match.group(1)) * 1024 / 2**30, 1) if match else None
    except (OSError, ValueError, subprocess.SubprocessError):
        pass
    return None


def _loopback_ok() -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind(("127.0.0.1", 0))
        return True
    except OSError:
        return False
    finally:
        sock.close()


def _temporary_ok() -> bool:
    try:
        with tempfile.TemporaryDirectory(prefix="course-preflight-") as directory:
            path = Path(directory) / "probe"
            path.write_bytes(b"ok")
            return path.read_bytes() == b"ok"
    except OSError:
        return False


def _docker_daemon_ok() -> bool:
    if not shutil.which("docker"):
        return False
    try:
        return subprocess.run(
            ["docker", "info"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            timeout=8, check=False,
        ).returncode == 0
    except (OSError, subprocess.SubprocessError):
        return False


def _docker_memory_gib() -> float | None:
    if not shutil.which("docker"):
        return None
    try:
        raw = subprocess.run(
            ["docker", "info", "--format", "{{.MemTotal}}"],
            capture_output=True, text=True, timeout=8, check=True,
        ).stdout.strip()
        return round(int(raw) / 2**30, 1)
    except (OSError, ValueError, subprocess.SubprocessError):
        return None


def _command_ok(command: list[str], *, cwd: Path | None = None, timeout: int = 30) -> bool:
    try:
        return subprocess.run(
            command, cwd=cwd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            timeout=timeout, check=False,
        ).returncode == 0
    except (OSError, subprocess.SubprocessError):
        return False


def _docker_image_cached(reference: str) -> bool:
    return _command_ok(["docker", "image", "inspect", reference], timeout=8)


def _m15_image_refs() -> list[str]:
    path = ROOT / "modules/15-execution-models-across-languages/lab/toolchains.lock.json"
    try:
        lock = json.loads(path.read_text(encoding="utf-8"))
        return [f"{lock[runtime]['image']}@{lock[runtime]['digest']}" for runtime in ("typescript", "go", "rust", "java")]
    except (OSError, KeyError, TypeError, json.JSONDecodeError):
        return []


def _wsl_cgroup_enforcement() -> bool:
    """Prove an ephemeral cached container receives CPU, memory, and PID limits."""

    controllers = Path("/sys/fs/cgroup/cgroup.controllers")
    try:
        visible = set(controllers.read_text(encoding="utf-8").split())
    except OSError:
        return False
    if not {"cpu", "memory", "pids"}.issubset(visible) or not _docker_image_cached(M03_IMAGE):
        return False
    command = [
        "docker", "run", "--rm", "--network", "none", "--read-only",
        "--cpus", "1", "--memory", "128m", "--memory-swap", "128m",
        "--pids-limit", "32", M03_IMAGE, "sh", "-lc",
        "cat /sys/fs/cgroup/cpu.max; cat /sys/fs/cgroup/memory.max; cat /sys/fs/cgroup/pids.max",
    ]
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=20, check=False)
        lines = result.stdout.splitlines()
        quota, period = (int(value) for value in lines[0].split())
        memory = int(lines[1])
        pids = int(lines[2])
        return result.returncode == 0 and quota == period and memory == 128 * 2**20 and pids == 32
    except (OSError, ValueError, IndexError, subprocess.SubprocessError):
        return False


def _chromium_launch_ok() -> bool:
    lab = ROOT / "modules/16-browser-frontend-cdn-edge/lab"
    program = (
        "const {chromium}=require('playwright');"
        "(async()=>{const b=await chromium.launch({headless:true});await b.close()})()"
        ".catch(()=>process.exit(1));"
    )
    return _command_ok(["node", "-e", program], cwd=lab, timeout=30)


def _npm_offline_cache_ready() -> bool:
    lab = ROOT / "modules/16-browser-frontend-cdn-edge/lab"
    return _command_ok(
        ["npm", "ci", "--offline", "--ignore-scripts", "--dry-run"], cwd=lab, timeout=45
    )


def _offline_cache_readiness(selected_modules: set[str], chromium_launch: bool) -> dict[str, bool]:
    readiness: dict[str, bool] = {}
    if "M03" in selected_modules:
        readiness["M03"] = _docker_image_cached(M03_IMAGE)
    if "M15" in selected_modules:
        refs = _m15_image_refs()
        readiness["M15"] = len(refs) == 4 and all(_docker_image_cached(ref) for ref in refs)
    if "M16" in selected_modules:
        readiness["M16"] = chromium_launch and _npm_offline_cache_ready()
    return readiness


def _git_head() -> str | None:
    try:
        value = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True,
            timeout=5, check=True,
        ).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return None
    return value if re.fullmatch(r"[0-9a-f]{40}", value) else None


def _wsl_browser_callback_verified(path: Path | None) -> bool:
    if path is None or not path.is_file():
        return False
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    return (
        record.get("schema_version") == "1.0"
        and record.get("result") == "pass"
        and record.get("boundary") == "windows-browser-to-wsl-loopback"
        and record.get("token_persisted") is False
        and record.get("source_commit") == _git_head()
        and bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", str(record.get("recorded_at", ""))))
    )


def collect_snapshot(
    selected_modules: list[str] | None = None,
    wsl_browser_callback: Path | None = None,
) -> dict[str, Any]:
    selected = set(selected_modules or ALL_MODULES)
    versions = {
        "python": platform.python_version(),
        "git": _run_version(["git", "--version"]),
        "compiler": _run_version(["cc", "--version"]),
        "make": _run_version(["make", "--version"]),
        "openssl": _run_version(["openssl", "version"]),
        "docker": _run_version(["docker", "--version"]),
        "node": _run_version(["node", "--version"]),
        "npm": _run_version(["npm", "--version"]),
    }
    try:
        free_disk = round(shutil.disk_usage(ROOT).free / 2**30, 1)
    except OSError:
        free_disk = None
    platform_kind = _platform_kind()
    chromium_launch = _chromium_launch_ok() if platform_kind == "wsl2-ubuntu" and "M16" in selected else None
    offline_cache = (
        _offline_cache_readiness(selected, bool(chromium_launch))
        if platform_kind == "wsl2-ubuntu" else None
    )
    return {
        "platform": platform_kind,
        "architecture": _architecture(),
        "ram_gib": _ram_gib(),
        "logical_cpus": os.cpu_count(),
        "free_disk_gib": free_disk,
        "versions": versions,
        "docker_daemon": _docker_daemon_ok(),
        "docker_memory_gib": _docker_memory_gib(),
        "openssl_addext": _command_supports(["openssl", "req", "-help"], "-addext"),
        "loopback": _loopback_ok(),
        "temporary_files": _temporary_ok(),
        "repo_on_wsl_filesystem": not str(ROOT).lower().startswith("/mnt/c/") if platform_kind == "wsl2-ubuntu" else None,
        "cgroup_enforcement": _wsl_cgroup_enforcement() if platform_kind == "wsl2-ubuntu" and selected & WSL_DOCKER_MODULES else None,
        "chromium_launch": chromium_launch,
        "offline_cache_ready": offline_cache,
        "windows_browser_callback": _wsl_browser_callback_verified(wsl_browser_callback) if platform_kind == "wsl2-ubuntu" and "M16" in selected else None,
    }


def _check(check_id: str, status: str, observed: str, requirement: str, modules: set[str], remediation: str) -> dict[str, Any]:
    return {"id": check_id, "status": status, "observed": observed, "requirement": requirement,
            "modules": sorted(modules), "remediation": remediation}


def evaluate(snapshot: dict[str, Any], selected_modules: list[str]) -> dict[str, Any]:
    selected = set(selected_modules)
    checks: list[dict[str, Any]] = []
    platform_kind = snapshot.get("platform", "unknown")
    arch = snapshot.get("architecture", "unknown")
    platform_status = "pass" if platform_kind in {"macos", "ubuntu", "wsl2-ubuntu"} else "fail"
    checks.append(_check("platform", platform_status, platform_kind, "macOS, Ubuntu LTS, or Ubuntu on WSL2", selected,
                         "Use a supported macOS/Ubuntu host; on Windows install Ubuntu on WSL2."))
    supported_arch = arch in {"x86_64", "arm64"} and platform_kind != "windows-native"
    if platform_kind == "wsl2-ubuntu":
        supported_arch = arch == "x86_64"
    arch_status = "pass" if supported_arch else "fail"
    checks.append(_check("architecture", arch_status, arch, "64-bit x86_64 or ARM64 (Windows ARM is unsupported)", selected,
                         "Use a supported 64-bit x86_64 or ARM64 host; Windows must use supported x86_64 WSL2."))

    for key, minimum, recommended, label in (("ram_gib", 8, 16, "RAM GiB"), ("logical_cpus", 2, 4, "logical CPUs"), ("free_disk_gib", 20, 40, "free disk GiB")):
        value = snapshot.get(key)
        if value is None:
            status, observed = "warn", "unknown"
        elif value < minimum:
            status, observed = "fail", str(value)
        elif value < recommended:
            status, observed = "warn", str(value)
        else:
            status, observed = "pass", str(value)
        checks.append(_check(key.replace("_gib", ""), status, observed, f">={minimum} minimum; >={recommended} recommended", selected,
                             f"Provide at least {minimum} {label}; close other workloads or free local space as applicable."))

    versions = snapshot.get("versions", {})
    python_v = _version_tuple(versions.get("python"))
    checks.append(_check("python", "pass" if python_v and python_v >= (3, 11, 0) else "fail",
                         versions.get("python") or "missing", ">=3.11", selected, "Install Python 3.11 or newer inside the supported environment."))
    git_v = versions.get("git")
    checks.append(_check("git", "pass" if git_v else "fail", git_v or "missing", "Git available", selected,
                         "Install Git; commits are required for frozen evidence and solo review."))

    requirements = [
        ("compiler", COMPILER_MODULES, "C11 compiler available", "Install Xcode command-line tools or Ubuntu build-essential."),
        ("make", COMPILER_MODULES, "make available", "Install Xcode command-line tools or Ubuntu build-essential."),
        ("openssl", OPENSSL_MODULES, "OpenSSL-compatible CLI available", "Install OpenSSL with support for req -addext."),
        ("node", NODE_MODULES, "Node satisfying the Module 16 lock", "Install the Node release recorded in the Module 16 toolchain lock."),
        ("npm", NODE_MODULES, "npm available", "Install npm with the pinned Node toolchain."),
        ("docker", DOCKER_MODULES, "Docker CLI and running daemon", "Install/start Docker Desktop or Docker Engine and enable WSL integration when applicable."),
    ]
    for tool, module_set, requirement, remediation in requirements:
        relevant = selected & module_set
        if not relevant:
            checks.append(_check(tool, "skipped", "not required", requirement, set(), remediation))
            continue
        present = bool(versions.get(tool))
        if tool == "docker":
            present = present and bool(snapshot.get("docker_daemon"))
        if tool == "openssl":
            present = present and bool(snapshot.get("openssl_addext"))
        if tool == "node" and present:
            lock_path = ROOT / "modules/16-browser-frontend-cdn-edge/lab/toolchains.lock.json"
            try:
                required_node = json.loads(lock_path.read_text(encoding="utf-8"))["node"]["version"]
            except (OSError, KeyError, json.JSONDecodeError):
                required_node = "24.19.0"
            present = _version_tuple(versions.get("node")) == _version_tuple(required_node)
            requirement = f"Node {required_node} from toolchains.lock.json"
        checks.append(_check(tool, "pass" if present else "fail", versions.get(tool) or "missing", requirement, relevant, remediation))

    loop_modules = selected & LOOPBACK_MODULES
    checks.append(_check("loopback", "pass" if snapshot.get("loopback") else ("fail" if loop_modules else "skipped"),
                         "bind succeeded" if snapshot.get("loopback") else "bind blocked", "unprivileged 127.0.0.1 binding",
                         loop_modules, "Allow local loopback binding; do not expose the lab on a public interface."))
    checks.append(_check("temporary-files", "pass" if snapshot.get("temporary_files") else "fail",
                         "read/write succeeded" if snapshot.get("temporary_files") else "read/write failed",
                         "temporary directory supports file create/read", selected,
                         "Free disk space and grant the current user access to the operating-system temporary directory."))

    if platform_kind == "wsl2-ubuntu":
        filesystem = snapshot.get("repo_on_wsl_filesystem")
        checks.append(_check(
            "wsl-filesystem", "pass" if filesystem else "fail",
            "verified" if filesystem else "not verified", "repository stored outside /mnt/c",
            selected, "Move the repository into the WSL ext4 filesystem.",
        ))
        docker_relevant = selected & WSL_DOCKER_MODULES
        cgroups = snapshot.get("cgroup_enforcement")
        checks.append(_check(
            "wsl-cgroups", "pass" if cgroups else ("fail" if docker_relevant else "skipped"),
            "bounded probe verified" if cgroups else "not verified",
            "cached container enforces CPU, memory, and PID cgroup limits", docker_relevant,
            "Cache the M03 GCC image, enable cgroup v2 controls, and rerun the bounded probe.",
        ))
        docker_memory = (snapshot.get("docker_memory_gib") or 0) >= 4
        checks.append(_check(
            "wsl-docker-memory", "pass" if docker_memory else ("fail" if docker_relevant else "skipped"),
            "verified" if docker_memory else "not verified", "Docker has at least 4 GiB",
            docker_relevant, "Assign at least 4 GiB to Docker Desktop.",
        ))
        chromium_relevant = bool(selected & NODE_MODULES)
        chromium = snapshot.get("chromium_launch")
        checks.append(_check("wsl-chromium", "pass" if chromium else ("fail" if chromium_relevant else "skipped"),
                             "launch and close succeeded" if chromium else "not launched", "pinned Chromium can launch", selected & NODE_MODULES,
                             "Install the pinned Playwright Chromium cache or use the official remote runner."))
        callback = snapshot.get("windows_browser_callback")
        checks.append(_check("wsl-windows-browser-callback", "pass" if callback else ("fail" if chromium_relevant else "skipped"),
                             "source-bound attestation verified" if callback else "not verified", "Windows browser reaches the WSL loopback callback",
                             selected & NODE_MODULES, "Run the Module 16 host-browser connectivity check before measured evidence."))
        cache_relevant = selected & WSL_OFFLINE_MODULES
        cache_map = snapshot.get("offline_cache_ready") or {}
        cache_passed = bool(cache_relevant) and all(cache_map.get(module) is True for module in cache_relevant)
        observed_cache = ", ".join(f"{module}={'ready' if cache_map.get(module) else 'missing'}" for module in sorted(cache_relevant))
        checks.append(_check(
            "wsl-offline-cache", "pass" if cache_passed else ("fail" if cache_relevant else "skipped"),
            observed_cache or "not required", "all selected pinned images, packages, and browser binaries are cached",
            cache_relevant, "Populate every selected module's pinned cache while online, then rerun the offline probe.",
        ))

    counts = {name: sum(item["status"] == name for item in checks) for name in ("pass", "warn", "fail", "skipped")}
    result = "fail" if counts["fail"] else ("warn" if counts["warn"] else "pass")
    remediations = sorted({item["remediation"] for item in checks if item["status"] in {"warn", "fail"}})
    return {
        "schema_version": "1.0", "platform": platform_kind, "architecture": arch,
        "selected_modules": sorted(selected),
        "resource_observations": {"ram_gib": snapshot.get("ram_gib"), "logical_cpus": snapshot.get("logical_cpus"), "free_disk_gib": snapshot.get("free_disk_gib")},
        "checks": checks, "remediations": remediations, "summary": {"result": result, **counts},
    }


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--module", action="append", default=[], metavar="MNN")
    parser.add_argument("--json", action="store_true", dest="json_output")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--wsl-browser-callback", type=Path)
    args = parser.parse_args(argv)
    invalid = sorted(set(args.module) - set(ALL_MODULES))
    if invalid:
        parser.error(f"invalid module(s): {', '.join(invalid)}")
    if args.output and not args.json_output:
        parser.error("--output requires --json")
    return args


def main(argv: list[str] | None = None) -> int:
    try:
        args = _parse_args(argv if argv is not None else sys.argv[1:])
        selected_modules = args.module or list(ALL_MODULES)
        report = evaluate(
            collect_snapshot(selected_modules, args.wsl_browser_callback), selected_modules
        )
        rendered = json.dumps(report, indent=2, sort_keys=True)
        if args.output:
            if args.output.exists():
                print(f"refusing to overwrite {args.output.name}", file=sys.stderr)
                return 2
            args.output.write_text(rendered + "\n", encoding="utf-8")
        elif args.json_output:
            print(rendered)
        else:
            print(f"Home lab preflight: {report['summary']['result'].upper()}")
            for item in report["checks"]:
                print(f"[{item['status'].upper():7}] {item['id']}: {item['observed']} ({item['requirement']})")
            for remediation in report["remediations"]:
                print(f"- {remediation}")
        return 1 if report["summary"]["fail"] else 0
    except SystemExit as exc:
        return int(exc.code) if isinstance(exc.code, int) else 2
    except Exception as exc:  # keep privacy: class only, no paths or host data
        print(f"preflight internal failure: {type(exc).__name__}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
