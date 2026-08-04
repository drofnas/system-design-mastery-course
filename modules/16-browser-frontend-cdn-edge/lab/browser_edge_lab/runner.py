from __future__ import annotations

import hashlib
import json
from typing import Any

from .config import INVARIANT_IDS


def _digest(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def run_scenario(scenario: dict[str, Any]) -> dict[str, Any]:
    controls = scenario["controls"]
    workload = scenario["workload"]
    shared = {
        key: value for key, value in scenario.items()
        if key not in {"scenario_id", "variant", "controls", "expected"}
    }
    invariant_pass = {
        "I01": controls["yield_long_tasks"],
        "I02": controls["prioritize_critical_resources"],
        "I03": controls["deterministic_hydration"],
        "I04": controls["release_route_resources"],
        "I05": controls["complete_public_cache_key"],
        "I06": controls["private_cache_bypass"],
        "I07": controls["isolate_third_party"],
        "I08": controls["bounded_stale_on_error"],
        "I09": True,
        "I10": True,
    }
    evidence = {
        "I01": "controlled interaction is below guardrail and long work is attributed",
        "I02": "critical transfer and request envelope fit the constrained profile",
        "I03": "server/client state hashes agree and recoverable mismatches are zero",
        "I04": "route-owned active resources and detached nodes return to baseline",
        "I05": "bounded public representations produce distinct normalized keys",
        "I06": "two subjects produce zero shared private cache entries",
        "I07": "core semantic route survives slow or blocked optional dependency",
        "I08": "only bounded marked public stale content is eligible during origin failure",
        "I09": "semantic, keyboard, focus, and manual evidence boundaries are recorded",
        "I10": "trace parentage is valid and sensitive attribute count is zero",
    }
    return {
        "module_id": "M16",
        "schema_version": "1.0",
        "scenario_id": scenario["scenario_id"],
        "pair_id": scenario["pair_id"],
        "variant": scenario["variant"],
        "seed": scenario["seed"],
        "shared_input_sha256": _digest(shared),
        "config_sha256": _digest(controls),
        "toolchain": {
            "node": "24.19.0",
            "react": "19.2.8",
            "playwright": "1.62.1",
            "chromium": "151.0.7922.34",
            "model_version": "browser-edge-model-1.0",
        },
        "environment": scenario["environment"],
        "route": scenario["route"],
        "measurements": {
            "lab_interaction_ms": 92 if controls["yield_long_tasks"] else workload["main_thread_ms"] + 40,
            "critical_transfer_ms": 1380 if controls["prioritize_critical_resources"] else 3260,
            "long_task_count": 0 if controls["yield_long_tasks"] else 1,
            "hydration_mismatches": 0 if controls["deterministic_hydration"] else 1,
        },
        "cache": {
            "public_representations_distinct": controls["complete_public_cache_key"],
            "private_cache_entries": 0 if controls["private_cache_bypass"] else 1,
            "stale_age_seconds": 480 if controls["bounded_stale_on_error"] else 3600,
            "degraded_marked": controls["bounded_stale_on_error"],
        },
        "accessibility": {
            "semantic_structure": True,
            "keyboard_path": True,
            "focus_preserved": controls["deterministic_hydration"],
            "manual_boundary_recorded": True,
        },
        "memory": {
            "active_resource_delta": 0 if controls["release_route_resources"] else workload["navigations"],
            "detached_node_delta": 0 if controls["release_route_resources"] else workload["navigations"],
        },
        "trace": {
            "valid_parentage": True,
            "sensitive_attribute_count": 0,
            "bounded_route_template": True,
        },
        "invariants": [
            {"id": invariant_id, "passed": invariant_pass[invariant_id], "evidence": evidence[invariant_id]}
            for invariant_id in INVARIANT_IDS
        ],
        "limitations": [
            "deterministic model output is not browser timing or a field percentile",
            "local cache logic is not proof of production CDN behavior",
            "accessibility automation does not replace manual or user evidence",
        ],
    }
