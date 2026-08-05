from __future__ import annotations

import json
import threading
import unittest
import urllib.request
from http.server import ThreadingHTTPServer
from pathlib import Path

from inference_lab.config import CONTROL_KEYS, load_scenario, validate_trial
from inference_lab.runner import run_scenario
from inference_lab.server import Handler, MODEL, ServingRuntime, generate_events


LAB_ROOT = Path(__file__).resolve().parents[1]


class ScenarioServerTests(unittest.TestCase):
    def test_all_failure_pairs_are_equivalent_and_repaired(self) -> None:
        pairs: dict[str, list[tuple[dict, dict]]] = {}
        for path in sorted((LAB_ROOT / "scenarios").glob("*.json")):
            scenario = load_scenario(path)
            trial = run_scenario(scenario)
            self.assertEqual(trial, run_scenario(scenario))
            self.assertEqual(validate_trial(trial), [])
            measurements = trial["measurements"]
            self.assertEqual(
                measurements["accepted"] + measurements["rejected"],
                scenario["workload"]["interactive_requests"] + scenario["workload"]["batch_requests"],
            )
            self.assertLessEqual(
                measurements["completed"] + measurements["failed"],
                measurements["accepted"],
            )
            pairs.setdefault(scenario["pair_id"], []).append((scenario, trial))
        self.assertEqual(set(pairs), {f"F{number:02d}" for number in range(1, 7)})
        for pair_id, rows in pairs.items():
            self.assertEqual(len(rows), 2)
            self.assertEqual({trial["variant"] for _, trial in rows}, {"broken", "repaired"})
            self.assertEqual(len({trial["shared_input_sha256"] for _, trial in rows}), 1)
            broken_scenario = next(scenario for scenario, _ in rows if scenario["variant"] == "broken")
            repaired_scenario = next(scenario for scenario, _ in rows if scenario["variant"] == "repaired")
            changed = {key for key in CONTROL_KEYS if broken_scenario["controls"][key] != repaired_scenario["controls"][key]}
            self.assertEqual(len(changed), 1)
            broken_trial = next(trial for _, trial in rows if trial["variant"] == "broken")
            repaired_trial = next(trial for _, trial in rows if trial["variant"] == "repaired")
            target = broken_scenario["expected"]["target_invariant"]
            self.assertFalse({row["id"]: row["passed"] for row in broken_trial["invariants"]}[target], pair_id)
            self.assertTrue(all(row["passed"] for row in repaired_trial["invariants"]), pair_id)

    def test_server_stream_contract(self) -> None:
        request = {
            "request_id": "req-17",
            "tenant_id": "museum-a",
            "prompt": "bronze owl",
            "max_output_tokens": 3,
            "deadline_ms": 1000,
            "traffic_class": "interactive",
            "model_version": MODEL.version,
        }
        events = generate_events(request)
        self.assertEqual(events[0]["type"], "accepted")
        self.assertEqual(events[-1]["type"], "completed")
        self.assertEqual([event["index"] for event in events if event["type"] == "token"], [0, 1, 2])
        self.assertNotIn("tenant_id", events[-1])

    def test_server_rejects_short_deadline(self) -> None:
        request = {
            "request_id": "req-short",
            "tenant_id": "museum-a",
            "prompt": "bronze owl",
            "max_output_tokens": 3,
            "deadline_ms": 1,
            "traffic_class": "interactive",
            "model_version": MODEL.version,
        }
        self.assertEqual(generate_events(request)[0]["type"], "rejected")

    def test_incremental_kv_generation_matches_full_recompute(self) -> None:
        for prompt in ("bronze owl", "river vessel", "museum"):
            with self.subTest(prompt=prompt):
                state = MODEL.prefill(prompt)
                prompt_tokens = state.token_count
                incremental = list(MODEL.generate_iter(state, 4))
                self.assertEqual(MODEL.generate(prompt, 4), incremental)
                self.assertEqual(prompt_tokens + len(incremental), state.token_count)
                self.assertGreater(state.byte_size(), 0)

    def test_byte_budget_refuses_without_exhausting_host(self) -> None:
        runtime = ServingRuntime(byte_capacity=1, token_capacity=64)
        request = {
            "request_id": "req-memory", "tenant_id": "museum-a", "prompt": "bronze owl",
            "max_output_tokens": 3, "deadline_ms": 1000, "traffic_class": "interactive",
            "model_version": MODEL.version,
        }
        events = list(runtime.iter_events(request))
        self.assertEqual("rejected", events[-1]["type"])
        self.assertEqual("byte_budget_exhausted", events[-1]["reason"])
        self.assertEqual(0, runtime.allocator.reserved_bytes)

    def test_cache_is_tenant_and_version_scoped(self) -> None:
        runtime = ServingRuntime()
        base = {
            "request_id": "req-cache", "tenant_id": "museum-a", "prompt": "bronze owl",
            "max_output_tokens": 2, "deadline_ms": 1000, "traffic_class": "interactive",
            "model_version": MODEL.version,
        }
        first = list(runtime.iter_events(base))[-1]
        second = list(runtime.iter_events({**base, "request_id": "req-cache-2"}))[-1]
        other = list(runtime.iter_events({**base, "request_id": "req-cache-3", "tenant_id": "museum-b"}))[-1]
        self.assertEqual(0, first["kv_reused_tokens"])
        self.assertGreater(second["kv_reused_tokens"], 0)
        self.assertEqual(0, other["kv_reused_tokens"])

    def test_bounded_fake_provider_failover(self) -> None:
        runtime = ServingRuntime()
        request = {
            "request_id": "req-failover", "tenant_id": "museum-a", "prompt": "bronze owl",
            "max_output_tokens": 2, "deadline_ms": 1000, "traffic_class": "interactive",
            "model_version": MODEL.version, "provider_mode": "fail_once",
            "fallback_model_version": MODEL.version,
        }
        completed = list(runtime.iter_events(request))[-1]
        self.assertEqual("completed", completed["type"])
        self.assertEqual(2, completed["provider_attempts"])
        incompatible = list(runtime.iter_events({**request, "request_id": "req-bad-fallback", "fallback_model_version": "other"}))[-1]
        self.assertEqual("failed", incompatible["type"])
        self.assertEqual(2, incompatible["provider_attempts"])

    def test_loopback_http_contract(self) -> None:
        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            base = f"http://127.0.0.1:{server.server_port}"
            with urllib.request.urlopen(f"{base}/healthz", timeout=2) as response:
                self.assertEqual(json.load(response)["status"], "ok")
            body = json.dumps({
                "request_id": "req-http",
                "tenant_id": "museum-b",
                "prompt": "river vessel",
                "max_output_tokens": 2,
                "deadline_ms": 1000,
                "traffic_class": "interactive",
                "model_version": MODEL.version,
            }).encode("utf-8")
            request = urllib.request.Request(
                f"{base}/v1/generate",
                data=body,
                headers={"Content-Type": "application/json"},
            )
            with urllib.request.urlopen(request, timeout=2) as response:
                self.assertEqual(response.headers.get_content_type(), "application/x-ndjson")
                first_event = json.loads(response.readline())
                self.assertEqual("accepted", first_event["type"])
                events = [first_event, *[json.loads(line) for line in response.read().splitlines()]]
            self.assertEqual(events[0]["type"], "accepted")
            self.assertEqual(events[-1]["type"], "completed")
            with urllib.request.urlopen(f"{base}/metrics", timeout=2) as response:
                self.assertGreaterEqual(json.load(response)["completed"], 1)
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)


if __name__ == "__main__":
    unittest.main()
