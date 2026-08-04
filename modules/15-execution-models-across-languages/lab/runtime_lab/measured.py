from __future__ import annotations

import concurrent.futures
import hashlib
import http.client
import json
import os
import platform
import re
import socket
import subprocess
import time
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .config import CONTROL_KEYS, digest, load_scenario, validate_trial
from .runner import NAMES

LAB = Path(__file__).resolve().parents[1]
REPO = LAB.parents[2]
SCHEMAS = REPO / "schemas"
RUNTIME_ORDER = ("typescript", "go", "rust", "java")
WARMUPS = 3
REPETITIONS = 5
MAX_BODY_BYTES = 1_048_576
EXCLUDED_TREE_PARTS = {"node_modules", "dist", "target", "__pycache__", ".DS_Store"}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def file_digest(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def tree_digest(root: Path) -> str:
    payload = hashlib.sha256()
    for path in sorted(item for item in root.rglob("*") if item.is_file() and not (set(item.relative_to(root).parts) & EXCLUDED_TREE_PARTS)):
        relative = path.relative_to(root).as_posix()
        payload.update(relative.encode("utf-8"))
        payload.update(b"\0")
        payload.update(path.read_bytes())
        payload.update(b"\0")
    return payload.hexdigest()


def combined_schema_digest() -> str:
    payload = hashlib.sha256()
    for name in ("runtime-fanout-request.schema.json", "runtime-fanout-response.schema.json", "runtime-scenario.schema.json", "runtime-trial.schema.json"):
        payload.update(name.encode("utf-8"))
        payload.update((SCHEMAS / name).read_bytes())
    return payload.hexdigest()


def image_ref(lock: dict[str, Any], runtime: str) -> str:
    entry = lock[runtime]
    image = str(entry["image"])
    digest_value = str(entry["digest"])
    if not re.fullmatch(r"sha256:[0-9a-f]{64}", digest_value):
        raise ValueError(f"{runtime} image digest is not immutable")
    return f"{image}@{digest_value}"


def service_command(runtime: str, scenario: str | None = None) -> str:
    if runtime == "typescript":
        return "cp -R /source/. /tmp/build/ && cd /tmp/build && npm ci --ignore-scripts && npm run build && exec node dist/server.js"
    if runtime == "go":
        race = "-race " if scenario == "F06" else ""
        return f"cp -R /source/. /tmp/build/ && cd /tmp/build && exec /usr/local/go/bin/go run {race}."
    if runtime == "rust":
        return "cp -R /source/. /tmp/build/ && cd /tmp/build && exec /usr/local/cargo/bin/cargo run --locked"
    if runtime == "java":
        return "cp -R /source/. /tmp/build/ && cd /tmp/build && /opt/java/openjdk/bin/javac FanoutServer.java FanoutServerTest.java && exec /opt/java/openjdk/bin/java -Xms64m -Xmx512m FanoutServer"
    raise ValueError(f"unknown runtime: {runtime}")


def implementation_root(runtime: str) -> Path:
    return LAB / "implementations" / runtime


def docker_limits(lock: dict[str, Any]) -> list[str]:
    limits = lock["container_resource_limits"]
    return [
        "--cpus", str(limits["cpus"]),
        "--memory", str(limits["memory"]),
        "--memory-swap", str(limits["memory_swap"]),
        "--pids-limit", str(limits["pids"]),
    ]


@dataclass
class DockerService:
    runtime: str
    lock: dict[str, Any]
    fault: str = "none"
    scenario: str | None = None
    cancel_after_ms: int | None = None
    name: str = field(init=False)
    port: int | None = field(default=None, init=False)
    image_id: str | None = field(default=None, init=False)
    cleanup: dict[str, Any] = field(default_factory=dict, init=False)

    def __post_init__(self) -> None:
        self.name = f"northstar-m15-{self.runtime}-{uuid.uuid4().hex[:10]}"

    def start(self) -> None:
        if not re.fullmatch(r"northstar-m15-[a-z]+-[0-9a-f]{10}", self.name):
            raise RuntimeError("unsafe generated container name")
        command = [
            "docker", "run", "-d", "--name", self.name,
            *docker_limits(self.lock),
            "--label", "course.system-design-mastery=m15-conformance",
            "--tmpfs", "/tmp:rw,exec,size=2147483648",
            "-p", "127.0.0.1::8080",
            "-e", "HOST=0.0.0.0",
            "-e", f"COURSE_FAULT={self.fault}",
            "-e", f"COURSE_SCENARIO={self.scenario or 'contract'}",
        ]
        if self.cancel_after_ms is not None:
            command.extend(["-e", f"COURSE_CANCEL_AFTER_MS={self.cancel_after_ms}"])
        command.extend([
            "-v", f"{implementation_root(self.runtime)}:/source:ro",
            image_ref(self.lock, self.runtime),
            "sh", "-lc", service_command(self.runtime, self.scenario),
        ])
        subprocess.run(command, cwd=LAB, check=True, capture_output=True, text=True)
        try:
            self.image_id = subprocess.run(
                ["docker", "inspect", "--format", "{{.Image}}", self.name],
                check=True, capture_output=True, text=True,
            ).stdout.strip()
            deadline = time.monotonic() + 300
            last_error = "service did not answer"
            while time.monotonic() < deadline:
                state = subprocess.run(
                    ["docker", "inspect", "--format", "{{.State.Running}}", self.name],
                    capture_output=True, text=True,
                )
                if state.returncode != 0 or state.stdout.strip() != "true":
                    logs = self.logs()
                    raise RuntimeError(f"{self.runtime} container exited before health check:\n{logs[-4000:]}")
                port_result = subprocess.run(["docker", "port", self.name, "8080/tcp"], capture_output=True, text=True)
                if port_result.returncode == 0 and port_result.stdout.strip():
                    try:
                        self.port = int(port_result.stdout.strip().rsplit(":", 1)[1])
                        record = self.request("GET", "/health", None, timeout=2)
                        if record["response"]["status"] == 200:
                            return
                    except (OSError, ValueError, http.client.HTTPException) as error:
                        last_error = str(error)
                time.sleep(0.25)
            logs = self.logs()
            raise RuntimeError(f"{self.runtime} health timeout: {last_error}\n{logs[-4000:]}")
        except Exception:
            self.stop()
            raise

    def logs(self) -> str:
        result = subprocess.run(["docker", "logs", self.name], capture_output=True, text=True)
        return result.stdout + result.stderr

    def stop(self) -> None:
        if not re.fullmatch(r"northstar-m15-[a-z]+-[0-9a-f]{10}", self.name):
            raise RuntimeError("refusing unsafe container cleanup")
        before = subprocess.run(
            ["docker", "inspect", "--format", "{{json .State}}", self.name],
            capture_output=True, text=True,
        )
        logs = self.logs() if before.returncode == 0 else ""
        removed = subprocess.run(["docker", "rm", "-f", "-v", self.name], capture_output=True, text=True)
        after = subprocess.run(["docker", "inspect", self.name], capture_output=True, text=True)
        self.cleanup = {
            "container": self.name,
            "state_before_cleanup": json.loads(before.stdout) if before.returncode == 0 and before.stdout.strip() else None,
            "logs_sha256": sha256_bytes(logs.encode("utf-8")),
            "logs_tail": logs[-4000:],
            "remove_exit_code": removed.returncode,
            "removed": removed.returncode == 0 and after.returncode != 0,
        }
        if not self.cleanup["removed"]:
            raise RuntimeError(f"failed to clean container {self.name}: {removed.stderr.strip()}")

    def request(self, method: str, path: str, value: Any, *, timeout: float = 10, raw_body: str | None = None) -> dict[str, Any]:
        if self.port is None:
            raise RuntimeError("service has no host port")
        body = raw_body if raw_body is not None else (None if value is None else canonical(value).decode("utf-8"))
        headers = {"accept": "application/json"}
        if body is not None:
            headers["content-type"] = "application/json"
        started_at = utc_now()
        start = time.monotonic_ns()
        connection = http.client.HTTPConnection("127.0.0.1", self.port, timeout=timeout)
        try:
            connection.request(method, path, body=body, headers=headers)
            response = connection.getresponse()
            response_body = response.read().decode("utf-8", errors="replace")
            try:
                parsed = json.loads(response_body)
            except json.JSONDecodeError:
                parsed = None
            return {
                "started_at": started_at,
                "finished_at": utc_now(),
                "duration_ms": (time.monotonic_ns() - start) / 1_000_000,
                "request": {"method": method, "path": path, "headers": headers, "body": body},
                "response": {"status": response.status, "headers": dict(response.getheaders()), "body": response_body, "json": parsed},
            }
        finally:
            connection.close()

    def disconnect(self, value: Any, delay_ms: int) -> dict[str, Any]:
        if self.port is None:
            raise RuntimeError("service has no host port")
        body = canonical(value)
        request = (
            b"POST /fanout HTTP/1.1\r\nHost: 127.0.0.1\r\nContent-Type: application/json\r\n" +
            f"Content-Length: {len(body)}\r\nConnection: close\r\n\r\n".encode("ascii") + body
        )
        started_at = utc_now()
        start = time.monotonic_ns()
        sock = socket.create_connection(("127.0.0.1", self.port), timeout=5)
        try:
            sock.sendall(request)
            time.sleep(delay_ms / 1000)
        finally:
            sock.close()
        return {
            "started_at": started_at,
            "finished_at": utc_now(),
            "duration_ms": (time.monotonic_ns() - start) / 1_000_000,
            "request": {"method": "POST", "path": "/fanout", "headers": {"connection": "close"}, "body": body.decode("utf-8")},
            "response": {"status": None, "headers": {}, "body": "client disconnected before response", "json": None},
        }


def host_boundary() -> dict[str, Any]:
    docker = subprocess.run(["docker", "version", "--format", "{{json .Server}}"], capture_output=True, text=True)
    return {
        "host_system": platform.system(),
        "host_release": platform.release(),
        "host_machine": platform.machine(),
        "python": platform.python_version(),
        "docker_server": json.loads(docker.stdout) if docker.returncode == 0 and docker.stdout.strip() else None,
        "boundary": "service runtime executes in a resource-limited Linux container; client and orchestration execute on the recorded host",
    }


def canonical_request(request_id: str, *, deadline_ms: int = 500, child_delay_ms: int = 30, payload_bytes: int = 1024) -> dict[str, Any]:
    return {
        "request_id": request_id,
        "deadline_ms": deadline_ms,
        "concurrency_limit": 2,
        "children": [
            {"child_id": "a-required", "required": True, "delay_ms": child_delay_ms, "payload_bytes": payload_bytes, "mode": "ok"},
            {"child_id": "b-optional", "required": False, "delay_ms": child_delay_ms, "payload_bytes": payload_bytes, "mode": "error"},
            {"child_id": "c-required", "required": True, "delay_ms": child_delay_ms, "payload_bytes": payload_bytes, "mode": "ok"},
            {"child_id": "d-optional", "required": False, "delay_ms": child_delay_ms, "payload_bytes": payload_bytes, "mode": "ok"},
        ],
    }


def validate_baseline(record: dict[str, Any], runtime: str) -> list[str]:
    errors: list[str] = []
    response = record["response"]
    value = response.get("json")
    if response.get("status") != 200 or not isinstance(value, dict):
        return ["baseline did not return JSON HTTP 200"]
    if value.get("runtime") != runtime or value.get("outcome") != "partial":
        errors.append("runtime or optional-failure outcome mismatch")
    ids = [row.get("child_id") for row in value.get("children", []) if isinstance(row, dict)]
    if ids != sorted(ids) or len(ids) != 4:
        errors.append("child results are missing or nondeterministically ordered")
    if not (1 <= value.get("max_in_flight", -1) <= 2):
        errors.append("max_in_flight is not observed within the request limit")
    if value.get("cleanup") != {"active_tasks": 0, "open_resources": 0}:
        errors.append("request cleanup is nonzero")
    return errors


def contract_checks(service: DockerService, runtime: str) -> tuple[list[dict[str, Any]], list[str]]:
    records: list[dict[str, Any]] = []
    failures: list[str] = []
    base = canonical_request("contract-shape")
    property_order = {
        "children": base["children"], "concurrency_limit": 2, "deadline_ms": 500, "request_id": "property-order",
    }
    cases: list[tuple[str, dict[str, Any], set[int], str | None, str | None]] = [
        ("property-order-independent", property_order, {200}, None, None),
        ("unknown-authority-rejected", {**base, "request_id": "authority", "tenant_id": "attacker"}, {400}, None, None),
        ("duplicate-child-rejected", {**base, "request_id": "duplicate", "children": [base["children"][0], base["children"][0]]}, {400}, None, None),
        ("payload-bound-rejected", {**base, "request_id": "payload", "children": [{**base["children"][0], "payload_bytes": 2_097_153}]}, {400}, None, None),
        ("task-bound-rejected", {**base, "request_id": "tasks", "children": [{**base["children"][0], "child_id": f"child-{index}"} for index in range(17)]}, {400}, None, None),
        ("body-bound-rejected", base, {400, 413}, None, canonical(base).decode("utf-8") + (" " * MAX_BODY_BYTES)),
        ("required-failure", {**base, "request_id": "required-failure", "children": [{**base["children"][0], "mode": "error"}]}, {200}, "failed", None),
    ]
    for name, payload, expected_statuses, expected_outcome, raw_body in cases:
        record = service.request("POST", "/fanout", payload, raw_body=raw_body)
        record["check"] = name
        records.append(record)
        if record["response"]["status"] not in expected_statuses:
            failures.append(f"{name}: expected HTTP {sorted(expected_statuses)}, got {record['response']['status']}")
        if expected_outcome and record["response"].get("json", {}).get("outcome") != expected_outcome:
            failures.append(f"{name}: expected outcome {expected_outcome}")
    return records, failures


def run_contract_runtime(runtime: str, lock: dict[str, Any], output: Path) -> dict[str, Any]:
    service = DockerService(runtime, lock)
    service.start()
    failures: list[str] = []
    try:
        checks, check_failures = contract_checks(service, runtime)
        failures.extend(check_failures)
        warmups = []
        repetitions = []
        for index in range(WARMUPS + REPETITIONS):
            record = service.request("POST", "/fanout", canonical_request(f"{runtime}-{'warmup' if index < WARMUPS else 'measured'}-{index + 1}"))
            record["excluded_warmup"] = index < WARMUPS
            errors = validate_baseline(record, runtime)
            failures.extend(f"repetition {index + 1}: {error}" for error in errors)
            (warmups if index < WARMUPS else repetitions).append(record)
        telemetry = service.request("GET", "/telemetry/snapshot", None)
    finally:
        service.stop()
    evidence = {
        "schema_version": "2.0",
        "mode": "contract",
        "runtime": runtime,
        "status": "pass" if not failures else "fail",
        "failures": failures,
        "toolchain": {"reference": image_ref(lock, runtime), "lock": lock[runtime], "container_image_id": service.image_id},
        "hashes": {"code_sha256": tree_digest(implementation_root(runtime)), "schema_sha256": combined_schema_digest()},
        "resource_limits": lock["container_resource_limits"],
        "host_boundary": host_boundary(),
        "checks": checks,
        "warmups": warmups,
        "repetitions": repetitions,
        "telemetry": telemetry,
        "cleanup_results": service.cleanup,
        "measurement_policy": {"warmups_excluded": WARMUPS, "measured_repetitions": REPETITIONS},
    }
    path = output / "contract" / f"{runtime}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    if failures:
        raise RuntimeError(f"{runtime} contract failed: {'; '.join(failures)}")
    return {"runtime": runtime, "path": str(path.relative_to(output)), "sha256": file_digest(path), "status": "pass"}


def scenario_request(scenario: dict[str, Any], request_id: str) -> dict[str, Any]:
    workload = scenario["workload"]
    children = []
    for index in range(workload["children_per_request"]):
        children.append({
            "child_id": f"child-{index:02d}",
            "required": index < max(1, workload["children_per_request"] - 1),
            "delay_ms": workload["child_delay_ms"],
            "payload_bytes": workload["payload_bytes"],
            "mode": "ok",
        })
    return {
        "request_id": request_id,
        "deadline_ms": scenario["limits"]["deadline_ms"],
        "concurrency_limit": min(workload["children_per_request"], 64),
        "children": children,
    }


def concurrent_workload(service: DockerService, scenario: dict[str, Any], label: str) -> list[dict[str, Any]]:
    count = scenario["workload"]["requests"]
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(count, 64)) as executor:
        futures = [executor.submit(service.request, "POST", "/fanout", scenario_request(scenario, f"{label}-{index:03d}")) for index in range(count)]
        return [future.result() for future in futures]


def observe_scenario(service: DockerService, scenario: dict[str, Any], repetition: int, excluded_warmup: bool) -> tuple[dict[str, Any], bool, str]:
    pair = scenario["pair_id"]
    label = f"{pair.lower()}-{'warmup' if excluded_warmup else 'measured'}-{repetition}"
    requests: list[dict[str, Any]]
    if pair in {"F02", "F05", "F06"}:
        requests = concurrent_workload(service, scenario, label)
    elif pair == "F07":
        requests = [service.disconnect(scenario_request(scenario, label), 10)]
        time.sleep(scenario["limits"]["cleanup_grace_ms"] / 1000)
    elif pair == "F09":
        payload = {**scenario_request(scenario, label), "tenant_id": "untrusted-request-authority"}
        requests = [service.request("POST", "/fanout", payload)]
    else:
        requests = [service.request("POST", "/fanout", scenario_request(scenario, label))]
    if pair == "F03":
        time.sleep(0.01)
    telemetry = service.request("GET", "/telemetry/snapshot", None)
    telemetry_json = telemetry["response"].get("json") or {}
    logs = service.logs()
    limits = scenario["limits"]
    workload = scenario["workload"]

    if pair == "F01":
        passed = all(record["duration_ms"] <= limits["deadline_ms"] + 20 for record in requests)
        evidence = f"maximum wire latency {max(record['duration_ms'] for record in requests):.2f} ms against {limits['deadline_ms']} ms deadline plus 20 ms transport allowance"
    elif pair == "F02":
        observed = int(telemetry_json.get("observed_max_in_flight", 10**9))
        passed = observed <= limits["max_children"]
        evidence = f"service telemetry observed {observed} simultaneous children against global bound {limits['max_children']}"
    elif pair == "F03":
        active = int(telemetry_json.get("active_tasks", 10**9))
        passed = active == 0
        evidence = f"service telemetry reported {active} active tasks after response ownership ended"
    elif pair == "F04":
        peak = int(telemetry_json.get("peak_buffered_bytes", 10**18))
        declared = workload["children_per_request"] * workload["payload_bytes"]
        passed = peak <= declared
        evidence = f"peak buffered bytes {peak} against declared in-flight payload {declared}"
    elif pair == "F05":
        observed = bool(telemetry_json.get("gc_observed"))
        collections = int(telemetry_json.get("gc_collections", 0))
        passed = observed and collections >= 1
        evidence = f"GC telemetry wiring={observed}; measured collection delta={collections}; time={telemetry_json.get('gc_time_ms')} ms"
    elif pair == "F06":
        detected = "WARNING: DATA RACE" in logs
        passed = not detected
        evidence = f"Go race detector warning present={detected}; log sha256={sha256_bytes(logs.encode('utf-8'))}"
    elif pair == "F07":
        active = int(telemetry_json.get("active_tasks", 10**9))
        resources = int(telemetry_json.get("open_resources", 10**9))
        passed = active == 0 and resources == 0
        evidence = f"after an actual client socket close and {limits['cleanup_grace_ms']} ms grace: active_tasks={active}, open_resources={resources}"
    elif pair == "F08":
        resources = int(telemetry_json.get("open_resources", 10**9))
        passed = resources == 0
        evidence = f"service telemetry reported {resources} open resources after joined response"
    elif pair == "F09":
        statuses = [record["response"]["status"] for record in requests]
        passed = statuses == [400]
        evidence = f"closed-schema request with authority field returned HTTP statuses {statuses}"
    else:
        raise ValueError(pair)
    return {
        "excluded_warmup": excluded_warmup,
        "repetition": repetition,
        "requests": requests,
        "telemetry": telemetry,
        "service_logs_sha256": sha256_bytes(logs.encode("utf-8")),
        "target_passed": passed,
        "target_evidence": evidence,
    }, passed, evidence


def run_matrix_variant(scenario_path: Path, lock: dict[str, Any], output: Path) -> dict[str, Any]:
    scenario = load_scenario(scenario_path)
    broken = scenario["variant"] == "broken"
    fault = scenario["fault"] if broken else "none"
    cancel_after = 10 if scenario["pair_id"] == "F07" else None
    service = DockerService(scenario["runtime"], lock, fault=fault, scenario=scenario["pair_id"], cancel_after_ms=cancel_after)
    service.start()
    observations: list[dict[str, Any]] = []
    target_results: list[bool] = []
    evidence_rows: list[str] = []
    try:
        for index in range(WARMUPS + REPETITIONS):
            observation, passed, evidence = observe_scenario(service, scenario, index + 1, index < WARMUPS)
            observations.append(observation)
            if index >= WARMUPS:
                target_results.append(passed)
                evidence_rows.append(evidence)
    finally:
        service.stop()

    expected_target_pass = not broken
    expectation_error = None
    if target_results != [expected_target_pass] * REPETITIONS:
        expectation_error = f"{scenario['scenario_id']} measured target results {target_results}, expected {[expected_target_pass] * REPETITIONS}"
    target = scenario["expected"]["target_invariant"]
    invariants = []
    for index, name in enumerate(NAMES, 1):
        invariant_id = f"I{index:02d}"
        invariants.append({
            "id": invariant_id,
            "name": name,
            "passed": target_results[-1] if invariant_id == target else True,
            "evidence": "; ".join(evidence_rows) if invariant_id == target else f"non-target invariant retained by identical measured workload and unchanged controls for {scenario['pair_id']}",
        })
    shared = {"seed": scenario["seed"], "runtime": scenario["runtime"], "workload": scenario["workload"], "limits": scenario["limits"], "fault": scenario["fault"]}
    trial = {
        "schema_version": "1.0",
        "scenario_id": scenario["scenario_id"],
        "pair_id": scenario["pair_id"],
        "variant": scenario["variant"],
        "runtime": scenario["runtime"],
        "seed": scenario["seed"],
        "scenario_sha256": digest(scenario),
        "shared_input_sha256": digest(shared),
        "config_sha256": digest(scenario["controls"]),
        "toolchain": {"mode": "measured-container-service", "reference": image_ref(lock, scenario["runtime"]), "lock": lock[scenario["runtime"]], "container_image_id": service.image_id},
        "useful_work": {"requests_per_repetition": scenario["workload"]["requests"], "children_per_request": scenario["workload"]["children_per_request"]},
        "scheduler": {"max_children": scenario["limits"]["max_children"], "telemetry_source": "/telemetry/snapshot"},
        "memory": {"limit_bytes": scenario["limits"]["memory_bytes"], "container_limit": lock["container_resource_limits"]["memory"]},
        "cancellation": {"cleanup_grace_ms": scenario["limits"]["cleanup_grace_ms"], "client_disconnect_exercised": scenario["pair_id"] == "F07"},
        "resources": {"container_limits": lock["container_resource_limits"]},
        "race": {"detector": "go -race" if scenario["pair_id"] == "F06" else "not target"},
        "validation": {"public_fault_fields": False, "fault_source": "COURSE_FAULT process environment set only by harness"},
        "invariants": invariants,
        "evidence_boundaries": [
            "test-only faults demonstrate causal controls and are not production incident frequency evidence",
            "five measured repetitions bound only this pinned workload and host boundary",
            "container scheduling and the recorded resource limits differ from native deployment",
            "synthetic payloads and delays must not be generalized as production performance numbers",
        ],
        "hashes": {"code_sha256": tree_digest(implementation_root(scenario["runtime"])), "schema_sha256": combined_schema_digest(), "image_sha256": lock[scenario["runtime"]]["digest"].removeprefix("sha256:")},
        "host_boundary": host_boundary(),
        "resource_limits": lock["container_resource_limits"],
        "warmups": observations[:WARMUPS],
        "repetitions": observations[WARMUPS:],
        "measurement_policy": {"warmups_excluded": WARMUPS, "measured_repetitions": REPETITIONS},
        "cleanup_results": service.cleanup,
    }
    errors = validate_trial(trial)
    if errors:
        raise RuntimeError(f"invalid measured trial: {errors}")
    path = output / "matrix" / scenario["pair_id"] / f"{scenario['variant']}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(trial, indent=2) + "\n", encoding="utf-8")
    if expectation_error:
        raise RuntimeError(expectation_error + f"; failed raw evidence preserved at {path}")
    return {"scenario": scenario["scenario_id"], "path": str(path.relative_to(output)), "sha256": file_digest(path), "status": "pass"}


def validate_pair_contract(paths: list[Path]) -> None:
    pairs: dict[str, list[dict[str, Any]]] = {}
    for path in paths:
        scenario = load_scenario(path)
        pairs.setdefault(scenario["pair_id"], []).append(scenario)
    for pair, rows in pairs.items():
        if len(rows) != 2 or {row["variant"] for row in rows} != {"broken", "repaired"}:
            raise ValueError(f"{pair} must contain one broken and one repaired scenario")
        broken = next(row for row in rows if row["variant"] == "broken")
        repaired = next(row for row in rows if row["variant"] == "repaired")
        for key in ("runtime", "seed", "workload", "limits", "fault", "expected"):
            if broken[key] != repaired[key]:
                raise ValueError(f"{pair} changes shared field {key}")
        changes = [key for key in CONTROL_KEYS if broken["controls"][key] != repaired["controls"][key]]
        if len(changes) != 1:
            raise ValueError(f"{pair} must change exactly one control; found {changes}")
