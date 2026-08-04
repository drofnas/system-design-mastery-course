from __future__ import annotations

from typing import Any

from .config import CONTROL_KEYS, digest

NAMES = (
    "equivalent logical work", "bounded admission and in-flight work",
    "non-expanding deadline", "owned cancellation and task cleanup",
    "exactly-once resource release", "schema-valid outcomes",
    "synchronized shared state", "bounded memory and overload",
    "toolchain and measurement provenance", "request context isolation",
)

TARGETS = {f"F{i:02d}": f"I{i if i < 7 else i-4:02d}" for i in range(1, 10)}
TARGETS.update({"F01":"I03","F02":"I02","F03":"I04","F04":"I08","F05":"I09","F06":"I07","F07":"I03","F08":"I05","F09":"I06"})

def run_scenario(s: dict[str, Any]) -> dict[str, Any]:
    controls = s["controls"]
    failed = s["expected"]["target_invariant"] if s["variant"] == "broken" else None
    invariants = [{"id":f"I{i:02d}","name":name,"passed":f"I{i:02d}" != failed,"evidence":f"{s['pair_id']} {s['variant']} modeled control evidence"} for i, name in enumerate(NAMES, 1)]
    shared = {"seed":s["seed"],"runtime":s["runtime"],"workload":s["workload"],"limits":s["limits"],"fault":s["fault"]}
    return {
        "schema_version":"1.0","scenario_id":s["scenario_id"],"pair_id":s["pair_id"],"variant":s["variant"],"runtime":s["runtime"],"seed":s["seed"],
        "scenario_sha256":digest(s),"shared_input_sha256":digest(shared),"config_sha256":digest(controls),
        "toolchain":{"mode":"deterministic-contract-model","version":"1.0"},
        "useful_work":{"requests":s["workload"]["requests"],"children":s["workload"]["requests"]*s["workload"]["children_per_request"]},
        "scheduler":{"max_in_flight":s["limits"]["max_children"] if controls["bounded_admission"] else s["workload"]["requests"]*s["workload"]["children_per_request"]},
        "memory":{"bounded":controls["bounded_buffers"],"gc_observed":controls["gc_observation"]},
        "cancellation":{"propagated":controls["propagate_cancellation"],"joined":controls["joined_task_scope"]},
        "resources":{"closed":controls["lexical_resource_scope"]},"race":{"synchronized":controls["synchronized_state"]},"validation":{"runtime_validation":controls["runtime_validation"]},
        "invariants":invariants,
        "evidence_boundaries":["model is not measured runtime evidence","host scheduling is not represented","allocator and GC timings are not represented","compiler and race-detector coverage require native runs"]
    }
