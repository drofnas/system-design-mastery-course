"""Compile, execute, and capture bounded native or Linux-container trials."""

from __future__ import annotations

import json
import math
import os
import platform
import resource
import statistics
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from .config import ScenarioError, validate_scenario


LAB_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = LAB_ROOT.parents[2]
BINARY = LAB_ROOT / "build" / "systems_probe"
SOURCE = LAB_ROOT / "src" / "systems_probe.c"
DOCKER_IMAGE = "gcc:15.2.0-bookworm"
COMPILER_FLAGS = "-std=c11 -O2 -Wall -Wextra -Werror -pthread"


def _run_text(command: list[str], *, timeout: float = 5) -> str:
    try:
        completed = subprocess.run(
            command, check=True, capture_output=True, text=True, timeout=timeout
        )
        return completed.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return "unavailable"


def _filesystem(path: Path) -> str:
    if platform.system() == "Darwin":
        resolved = path.resolve()
        best_mount = ""
        best_type = "unavailable"
        for line in _run_text(["mount"]).splitlines():
            if " on " not in line or " (" not in line:
                continue
            _, remainder = line.split(" on ", 1)
            mount_point, options = remainder.rsplit(" (", 1)
            try:
                contains_path = resolved == Path(mount_point) or resolved.is_relative_to(mount_point)
            except (OSError, ValueError):
                contains_path = False
            if contains_path and len(mount_point) > len(best_mount):
                best_mount = mount_point
                best_type = options.rstrip(")").split(",", 1)[0]
        return f"{best_type}:{best_mount or 'unavailable'}"
    return _run_text(["stat", "-f", "-c", "%T", str(path)])


def _recorded_text(path: Path, fallback: str) -> str:
    try:
        value = path.read_text(encoding="utf-8").strip()
    except OSError:
        return fallback
    return value or fallback


def _effective_limits(scenario: dict[str, Any]) -> dict[str, Any]:
    limits = dict(scenario.get("limits", {}))
    if scenario["runtime"] == "docker":
        limits.setdefault("cpus", 1.0)
        limits.setdefault("memory_mb", 512)
        limits.setdefault("pids", 64)
    return limits


def environment(runtime: str, workdir: Path) -> dict[str, Any]:
    host_compiler = _run_text(["cc", "--version"]).splitlines()[0]
    host_system = platform.system()
    host_kernel = platform.release()
    host_architecture = platform.machine()
    host_filesystem = _filesystem(workdir)
    if runtime == "docker":
        system = _recorded_text(workdir / "runtime.system", "unavailable")
        kernel = _recorded_text(workdir / "runtime.kernel", "unavailable")
        architecture = _recorded_text(workdir / "runtime.architecture", "unavailable")
        compiler = _recorded_text(workdir / "runtime.compiler", f"{DOCKER_IMAGE} cc")
        filesystem = _recorded_text(workdir / "runtime.filesystem", "unavailable")
    else:
        system, kernel, architecture = host_system, host_kernel, host_architecture
        compiler, filesystem = host_compiler, host_filesystem
    return {
        "runtime": runtime,
        "platform": platform.platform(),
        "system": system,
        "kernel": kernel,
        "architecture": architecture,
        "logical_cpus": os.cpu_count(),
        "compiler": compiler,
        "compiler_flags": COMPILER_FLAGS,
        "filesystem": filesystem,
        "host_system": host_system,
        "host_kernel": host_kernel,
        "host_architecture": host_architecture,
        "host_filesystem": host_filesystem,
        "container_image": DOCKER_IMAGE if runtime == "docker" else None,
        "virtualization_note": (
            "Docker may run inside a desktop Linux VM; results are not bare-metal claims."
            if runtime == "docker" else None
        ),
    }


def build_native(*, sanitize: bool = False) -> None:
    BINARY.parent.mkdir(parents=True, exist_ok=True)
    flags = ["-std=c11", "-O2", "-Wall", "-Wextra", "-Werror", "-pthread"]
    if sanitize:
        flags.extend(["-fsanitize=address,undefined", "-fno-omit-frame-pointer"])
    subprocess.run(["cc", *flags, str(SOURCE), "-o", str(BINARY)], check=True)


def _probe_arguments(scenario: dict[str, Any], output_path: Path) -> list[str]:
    probe = scenario["probe"]
    variant = scenario["variant"]
    parameters = scenario["parameters"]
    if probe == "locality":
        return [probe, variant, str(parameters["elements"]), str(parameters["stride"])]
    if probe == "allocation":
        return [probe, variant, str(parameters["iterations"]), str(parameters["bytes_per_iteration"])]
    if probe == "contention":
        return [probe, variant, str(parameters["workers"]), str(parameters["iterations"])]
    if probe == "io":
        return [probe, variant, str(parameters["total_bytes"]),
                str(parameters["chunk_bytes"]), str(parameters["sync_every"]),
                str(output_path)]
    if probe == "deadlock":
        return [probe]
    raise ScenarioError(f"unsupported probe {probe}")


def _resource_delta(before: resource.struct_rusage, after: resource.struct_rusage) -> dict[str, Any]:
    rss = after.ru_maxrss
    if platform.system() != "Darwin":
        rss *= 1024
    return {
        "user_cpu_ns": int((after.ru_utime - before.ru_utime) * 1_000_000_000),
        "system_cpu_ns": int((after.ru_stime - before.ru_stime) * 1_000_000_000),
        "max_rss_bytes": int(rss),
        "minor_faults": int(after.ru_minflt - before.ru_minflt),
        "major_faults": int(after.ru_majflt - before.ru_majflt),
        "voluntary_context_switches": int(after.ru_nvcsw - before.ru_nvcsw),
        "involuntary_context_switches": int(after.ru_nivcsw - before.ru_nivcsw),
        "block_inputs": int(after.ru_inblock - before.ru_inblock),
        "block_outputs": int(after.ru_oublock - before.ru_oublock),
    }


def _native_sample(scenario: dict[str, Any], workdir: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    build_native()
    output_path = workdir / f"{scenario['id']}.data"
    prior_content = b"prior-checkpoint-generation\n"
    if scenario["probe"] == "io" and scenario["variant"] == "crash_before_rename":
        output_path.write_bytes(prior_content)
    command = [str(BINARY), *_probe_arguments(scenario, output_path)]
    competitor = None
    if scenario["probe"] == "io" and scenario["variant"] == "contended":
        competitor_path = workdir / "competitor.data"
        competitor_args = [
            str(BINARY), "io", "competitor",
            str(scenario["parameters"]["competitor_bytes"]),
            str(scenario["parameters"]["chunk_bytes"]), "0", str(competitor_path),
        ]
        competitor = subprocess.Popen(competitor_args, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    try:
        completed = subprocess.run(
            command, check=False, capture_output=True, text=True,
            timeout=float(scenario.get("timeout_seconds", 20)),
        )
        if completed.returncode != 0:
            raise RuntimeError(f"probe exited {completed.returncode}: {completed.stderr.strip()}")
        sample = json.loads(completed.stdout)
    except subprocess.TimeoutExpired:
        if scenario["probe"] != "deadlock":
            raise
        sample = {
            "probe": "deadlock", "variant": scenario["variant"], "operations": 2,
            "bytes": 0, "checksum": 0,
            "elapsed_ns": int(float(scenario.get("timeout_seconds", 20)) * 1_000_000_000),
            "user_cpu_ns": 0, "system_cpu_ns": 0, "max_rss_bytes": 0,
            "minor_faults": 0, "major_faults": 0,
            "voluntary_context_switches": 0, "involuntary_context_switches": 0,
            "block_inputs": 0, "block_outputs": 0,
            "outcome": "timeout",
        }
    if competitor is not None:
        try:
            competitor.wait(timeout=float(scenario.get("timeout_seconds", 20)))
        except subprocess.TimeoutExpired:
            competitor.kill()
            competitor.wait()
            raise RuntimeError("I/O competitor exceeded timeout")
        if competitor.returncode != 0:
            raise RuntimeError(f"I/O competitor exited {competitor.returncode}")
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    _attach_post_exit_observation(sample, output_path, prior_content)
    return sample, _resource_delta(before, after)


def _parse_cgroup(path: Path) -> dict[str, int]:
    if not path.exists():
        return {}
    values: dict[str, int] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        parts = line.split()
        if len(parts) == 2 and parts[1].lstrip("-").isdigit():
            values[parts[0]] = int(parts[1])
    return values


def _parse_io_stat(path: Path) -> dict[str, dict[str, int]]:
    if not path.exists():
        return {}
    devices: dict[str, dict[str, int]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        parts = line.split()
        if not parts:
            continue
        values: dict[str, int] = {}
        for token in parts[1:]:
            key, separator, raw = token.partition("=")
            if separator and raw.isdigit():
                values[key] = int(raw)
        devices[parts[0]] = values
    return devices


def _file_checksum(path: Path) -> tuple[int, int]:
    total = 0
    size = 0
    with path.open("rb") as stream:
        while chunk := stream.read(1024 * 1024):
            size += len(chunk)
            total += sum(chunk)
    return size, total


def _attach_post_exit_observation(
    sample: dict[str, Any], output_path: Path, prior_content: bytes = b""
) -> None:
    sample.setdefault("acknowledgement_boundary", "not-applicable")
    sample["post_exit_bytes"] = 0
    sample["post_exit_checksum"] = 0
    sample["post_exit_matches"] = True
    sample["recovery_observation"] = "not-applicable"
    if sample.get("probe") != "io":
        return
    if output_path.exists():
        size, checksum = _file_checksum(output_path)
        sample["post_exit_bytes"] = size
        sample["post_exit_checksum"] = checksum
    if sample.get("outcome") == "injected_crash":
        prior_checksum = sum(prior_content)
        sample["post_exit_matches"] = (
            sample["post_exit_bytes"] == len(prior_content)
            and sample["post_exit_checksum"] == prior_checksum
            and output_path.with_name(output_path.name + ".tmp").exists()
        )
        sample["recovery_observation"] = "prior-generation-preserved-temp-generation-unpublished"
    elif sample.get("outcome") == "ok":
        sample["post_exit_matches"] = (
            sample["post_exit_bytes"] == sample["bytes"]
            and sample["post_exit_checksum"] == sample["checksum"]
        )
        sample["recovery_observation"] = "orderly-post-exit-content-reopened-and-verified"


def _docker_sample(scenario: dict[str, Any], workdir: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    output_path = workdir / "probe.data"
    result_path = workdir / "probe.json"
    args = _probe_arguments(scenario, Path("/work/probe.data"))
    limits = _effective_limits(scenario)
    command = [
        "docker", "run", "--rm", "--network", "none", "--read-only",
        "--pids-limit", str(limits.get("pids", 64)),
        "--tmpfs", "/tmp:rw,exec,nosuid,size=64m",
        "--mount", f"type=bind,src={LAB_ROOT / 'src'},dst=/src,readonly",
        "--mount", f"type=bind,src={workdir},dst=/work",
    ]
    if "cpus" in limits:
        command.extend(["--cpus", str(limits["cpus"])])
    if "memory_mb" in limits:
        memory = f"{limits['memory_mb']}m"
        command.extend(["--memory", memory, "--memory-swap", memory])
    competitor = ""
    if scenario["probe"] == "io" and scenario["variant"] == "contended":
        competitor = (
            f"/tmp/systems_probe io competitor {scenario['parameters']['competitor_bytes']} "
            f"{scenario['parameters']['chunk_bytes']} 0 /work/competitor.data >/dev/null & other=$!; "
        )
    shell = (
        f"cc {COMPILER_FLAGS} /src/systems_probe.c -o /tmp/systems_probe || exit $?; "
        f"{competitor}/tmp/systems_probe {' '.join(args)} > /work/probe.json; code=$?; "
        "if [ -n \"${other:-}\" ]; then wait $other || code=$?; fi; "
        "cp /sys/fs/cgroup/cpu.stat /work/cpu.stat 2>/dev/null || true; "
        "cp /sys/fs/cgroup/memory.events /work/memory.events 2>/dev/null || true; "
        "cp /sys/fs/cgroup/memory.current /work/memory.current 2>/dev/null || true; "
        "cp /sys/fs/cgroup/memory.peak /work/memory.peak 2>/dev/null || true; "
        "cp /sys/fs/cgroup/pids.current /work/pids.current 2>/dev/null || true; "
        "cp /sys/fs/cgroup/pids.peak /work/pids.peak 2>/dev/null || true; "
        "cp /sys/fs/cgroup/pids.events /work/pids.events 2>/dev/null || true; "
        "cp /sys/fs/cgroup/io.stat /work/io.stat 2>/dev/null || true; exit $code"
    )
    shell = (
        "uname -s > /work/runtime.system; uname -r > /work/runtime.kernel; "
        "uname -m > /work/runtime.architecture; cc --version | head -1 > /work/runtime.compiler; "
        "df -T /work | tail -1 > /work/runtime.filesystem; " + shell
    )
    command.extend([DOCKER_IMAGE, "sh", "-lc", shell])
    completed = subprocess.run(
        command, check=False, capture_output=True, text=True,
        timeout=float(scenario.get("timeout_seconds", 20)) + 30,
    )
    controller = {
        "cpu_stat": _parse_cgroup(workdir / "cpu.stat"),
        "memory_events": _parse_cgroup(workdir / "memory.events"),
        "pids_events": _parse_cgroup(workdir / "pids.events"),
        "io_stat": _parse_io_stat(workdir / "io.stat"),
        "io_stat_available": (workdir / "io.stat").exists(),
    }
    for name in ("memory.current", "memory.peak", "pids.current", "pids.peak"):
        path = workdir / name
        if path.exists() and path.read_text(encoding="utf-8").strip().isdigit():
            controller[name.replace(".", "_")] = int(path.read_text(encoding="utf-8").strip())
    memory_events = controller["memory_events"]
    if completed.returncode == 0 and result_path.exists():
        sample = json.loads(result_path.read_text(encoding="utf-8"))
    elif memory_events.get("oom_kill", 0) > 0 or memory_events.get("oom", 0) > 0 or completed.returncode == 137:
        sample = {
            "probe": scenario["probe"], "variant": scenario["variant"],
            "operations": 0, "bytes": 0, "checksum": 0, "elapsed_ns": 0,
            "user_cpu_ns": 0, "system_cpu_ns": 0, "max_rss_bytes": 0,
            "minor_faults": 0, "major_faults": 0,
            "voluntary_context_switches": 0, "involuntary_context_switches": 0,
            "block_inputs": 0, "block_outputs": 0, "outcome": "oom",
            "acknowledgement_boundary": "process-terminated-by-memory-controller",
        }
    else:
        raise RuntimeError(
            f"container probe exited {completed.returncode}: {completed.stderr.strip()}"
        )
    _attach_post_exit_observation(sample, output_path)
    if output_path.exists() and output_path.stat().st_size > 512 * 1024 * 1024:
        raise RuntimeError("probe exceeded storage bound")
    return sample, controller


def validate_trial(trial: Any) -> dict[str, Any]:
    if not isinstance(trial, dict):
        raise ScenarioError("trial root must be an object")
    required = {
        "schema_version", "scenario_id", "source_commit", "environment", "limits",
        "samples", "resource_samples", "summary", "measurement_limitations",
    }
    missing = required - trial.keys()
    if missing:
        raise ScenarioError(f"trial missing fields: {sorted(missing)}")
    if set(trial) != required:
        raise ScenarioError("trial contains fields outside the published schema")
    if trial["schema_version"] != 1:
        raise ScenarioError("trial schema_version must be 1")
    if not isinstance(trial["scenario_id"], str) or not trial["scenario_id"].replace("-", "").isalnum():
        raise ScenarioError("trial scenario_id is invalid")
    if not isinstance(trial["source_commit"], str) or len(trial["source_commit"]) < 7:
        raise ScenarioError("trial source_commit is invalid")
    expected_environment = {
        "runtime", "platform", "system", "kernel", "architecture", "logical_cpus",
        "compiler", "compiler_flags", "filesystem", "host_system", "host_kernel",
        "host_architecture", "host_filesystem", "container_image", "virtualization_note",
    }
    environment_value = trial["environment"]
    if not isinstance(environment_value, dict) or set(environment_value) != expected_environment:
        raise ScenarioError("trial environment does not match the published schema")
    if environment_value["runtime"] not in {"native", "docker"}:
        raise ScenarioError("trial runtime is invalid")
    for key in expected_environment - {"logical_cpus", "container_image", "virtualization_note"}:
        if not isinstance(environment_value[key], str) or not environment_value[key]:
            raise ScenarioError(f"environment.{key} must be a non-empty string")
    logical_cpus = environment_value["logical_cpus"]
    if logical_cpus is not None and (isinstance(logical_cpus, bool) or not isinstance(logical_cpus, int) or logical_cpus < 1):
        raise ScenarioError("environment.logical_cpus is invalid")
    for key in ("container_image", "virtualization_note"):
        if environment_value[key] is not None and not isinstance(environment_value[key], str):
            raise ScenarioError(f"environment.{key} must be a string or null")
    if not isinstance(trial["limits"], dict) or set(trial["limits"]) - {"cpus", "memory_mb", "pids"}:
        raise ScenarioError("trial limits are invalid")
    if "cpus" in trial["limits"]:
        cpu_limit = trial["limits"]["cpus"]
        if isinstance(cpu_limit, bool) or not isinstance(cpu_limit, (int, float)) or not math.isfinite(cpu_limit) or not 0.1 <= cpu_limit <= 8:
            raise ScenarioError("limits.cpus is invalid")
    for key, lower, upper in (("memory_mb", 32, 1024), ("pids", 16, 128)):
        if key in trial["limits"]:
            value = trial["limits"][key]
            if isinstance(value, bool) or not isinstance(value, int) or not lower <= value <= upper:
                raise ScenarioError(f"limits.{key} is invalid")
    samples = trial["samples"]
    resource_samples = trial["resource_samples"]
    if not isinstance(samples, list) or not 1 <= len(samples) <= 9:
        raise ScenarioError("trial samples must contain 1..9 entries")
    if not isinstance(resource_samples, list) or len(resource_samples) != len(samples):
        raise ScenarioError("resource_samples must align one-for-one with samples")
    if any(not isinstance(item, dict) or not item for item in resource_samples):
        raise ScenarioError("resource_samples entries must be non-empty objects")
    limitations = trial["measurement_limitations"]
    if not isinstance(limitations, list) or not limitations or any(
        not isinstance(item, str) or not item for item in limitations
    ):
        raise ScenarioError("measurement_limitations requires non-empty strings")
    checksums = {sample["checksum"] for sample in samples if sample.get("outcome") == "ok"}
    if len(checksums) > 1:
        raise ScenarioError("successful samples disagree on checksum")
    sample_fields = {
        "probe", "variant", "operations", "bytes", "checksum", "elapsed_ns",
        "user_cpu_ns", "system_cpu_ns", "max_rss_bytes", "minor_faults",
        "major_faults", "voluntary_context_switches", "involuntary_context_switches",
        "block_inputs", "block_outputs", "outcome", "acknowledgement_boundary",
        "post_exit_bytes", "post_exit_checksum", "post_exit_matches", "recovery_observation",
    }
    integer_fields = sample_fields - {
        "probe", "variant", "outcome", "acknowledgement_boundary",
        "post_exit_matches", "recovery_observation",
    }
    for sample in samples:
        if not isinstance(sample, dict) or set(sample) != sample_fields:
            raise ScenarioError("sample does not match the published schema")
        if sample["probe"] not in {"locality", "allocation", "contention", "io", "deadlock"}:
            raise ScenarioError("sample probe is invalid")
        if sample["outcome"] not in {"ok", "timeout", "oom", "injected_crash"}:
            raise ScenarioError("sample outcome is invalid")
        for key in ("variant", "acknowledgement_boundary", "recovery_observation"):
            if not isinstance(sample[key], str) or not sample[key]:
                raise ScenarioError(f"sample {key} must be a non-empty string")
        if not isinstance(sample["post_exit_matches"], bool):
            raise ScenarioError("sample post_exit_matches must be boolean")
        for key in integer_fields:
            value = sample[key]
            if isinstance(value, bool) or not isinstance(value, int) or value < 0:
                raise ScenarioError(f"sample {key} must be a non-negative integer")
        if sample["probe"] == "io" and not sample["post_exit_matches"]:
            raise ScenarioError("I/O sample failed its post-exit recovery observation")
    summary = trial["summary"]
    summary_fields = {
        "repetitions", "successful_repetitions", "median_elapsed_ns", "min_elapsed_ns",
        "max_elapsed_ns", "useful_operations", "useful_bytes",
        "median_throughput_per_second", "median_bytes_per_second",
    }
    if not isinstance(summary, dict) or set(summary) != summary_fields:
        raise ScenarioError("trial summary does not match the published schema")
    elapsed = [sample["elapsed_ns"] for sample in samples]
    successful = [sample for sample in samples if sample["outcome"] == "ok"]
    expected = {
        "repetitions": len(samples),
        "successful_repetitions": len(successful),
        "median_elapsed_ns": int(statistics.median(elapsed)),
        "min_elapsed_ns": min(elapsed),
        "max_elapsed_ns": max(elapsed),
        "useful_operations": sum(sample["operations"] for sample in successful),
        "useful_bytes": sum(sample["bytes"] for sample in successful),
    }
    for key, value in expected.items():
        if summary[key] != value:
            raise ScenarioError(f"summary.{key} contradicts detailed samples")
    expected_rates = {
        "median_throughput_per_second": round(statistics.median(
            sample["operations"] * 1_000_000_000 / max(sample["elapsed_ns"], 1)
            for sample in successful
        ), 3) if successful else 0.0,
        "median_bytes_per_second": round(statistics.median(
            sample["bytes"] * 1_000_000_000 / max(sample["elapsed_ns"], 1)
            for sample in successful
        ), 3) if successful else 0.0,
    }
    for key in ("median_throughput_per_second", "median_bytes_per_second"):
        value = summary[key]
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
            raise ScenarioError(f"summary.{key} is invalid")
        if value != expected_rates[key]:
            raise ScenarioError(f"summary.{key} contradicts detailed samples")
    return trial


def run_trial(scenario: dict[str, Any]) -> dict[str, Any]:
    scenario = validate_scenario(scenario)
    samples: list[dict[str, Any]] = []
    resource_samples: list[dict[str, Any]] = []
    with tempfile.TemporaryDirectory(prefix="module03-") as directory:
        workdir = Path(directory)
        run_one = _native_sample if scenario["runtime"] == "native" else _docker_sample
        for _ in range(scenario.get("warmup", 1)):
            run_one(scenario, workdir)
        for _ in range(scenario.get("repetitions", 3)):
            sample, counters = run_one(scenario, workdir)
            samples.append(sample)
            resource_samples.append(counters)
        elapsed = [sample["elapsed_ns"] for sample in samples]
        successful = [sample for sample in samples if sample["outcome"] == "ok"]
        trial = {
            "schema_version": 1,
            "scenario_id": scenario["id"],
            "source_commit": _run_text(["git", "-C", str(REPO_ROOT), "rev-parse", "HEAD"]),
            "environment": environment(scenario["runtime"], workdir),
            "limits": _effective_limits(scenario),
            "samples": samples,
            "resource_samples": resource_samples,
            "summary": {
                "repetitions": len(samples),
                "successful_repetitions": len(successful),
                "median_elapsed_ns": int(statistics.median(elapsed)),
                "min_elapsed_ns": min(elapsed),
                "max_elapsed_ns": max(elapsed),
                "useful_operations": sum(sample["operations"] for sample in successful),
                "useful_bytes": sum(sample["bytes"] for sample in successful),
                "median_throughput_per_second": round(statistics.median(
                    sample["operations"] * 1_000_000_000 / max(sample["elapsed_ns"], 1)
                    for sample in successful
                ), 3) if successful else 0.0,
                "median_bytes_per_second": round(statistics.median(
                    sample["bytes"] * 1_000_000_000 / max(sample["elapsed_ns"], 1)
                    for sample in successful
                ), 3) if successful else 0.0,
            },
            "measurement_limitations": [
                "Counters are OS interfaces, not a complete causal proof.",
                "Performance ratios apply only to the recorded environment and workload.",
                "Maximum RSS is a process high-water mark, not current residency.",
                "Docker controller counters include compiler setup before the probe.",
                "A present but empty io.stat means this runtime exposed no per-device accounting for the trial path.",
            ],
        }
    return validate_trial(trial)
