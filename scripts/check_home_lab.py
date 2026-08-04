#!/usr/bin/env python3
"""Read-only, privacy-preserving home-lab readiness preflight."""
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
LOOPBACK_MODULES = {"M02", "M04", "M05", "M06", "M11", "M12", "M16", "M17", "M18"}


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
    if "microsoft" in release or os.environ.get("WSL_INTEROP"):
        return "wsl2-ubuntu"
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


def collect_snapshot() -> dict[str, Any]:
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
    return {
        "platform": _platform_kind(),
        "architecture": _architecture(),
        "ram_gib": _ram_gib(),
        "logical_cpus": os.cpu_count(),
        "free_disk_gib": free_disk,
        "versions": versions,
        "docker_daemon": _docker_daemon_ok(),
        "loopback": _loopback_ok(),
        "temporary_files": _temporary_ok(),
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
    arch_status = "pass" if arch in {"x86_64", "arm64"} and platform_kind != "windows-native" else "fail"
    checks.append(_check("architecture", arch_status, arch, "64-bit x86_64 or ARM64 (Windows ARM is unsupported)", selected,
                         "Use a supported 64-bit x86_64 or ARM64 host; Windows must use supported x86_64 WSL2."))

    for key, minimum, recommended, label in (("ram_gib", 8, 16, "RAM GiB"), ("logical_cpus", 2, 4, "logical CPUs"), ("free_disk_gib", 20, 30, "free disk GiB")):
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
        report = evaluate(collect_snapshot(), args.module or list(ALL_MODULES))
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
