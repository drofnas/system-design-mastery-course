from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from rag_agent_lab.config import CONTROL_KEYS, INVARIANT_IDS, load_scenario, validate_trial
from rag_agent_lab.runner import run_scenario
from rag_agent_lab.workflow import DurableWorkflow, ToolExecutor, approval_digest


class WorkflowTests(unittest.TestCase):
    def test_tool_authorization_approval_and_idempotency(self) -> None:
        schema = {"type": "object", "required": ["application_id"], "properties": {"application_id": {"type": "string"}}, "additionalProperties": False}
        executor = ToolExecutor({"submit": {"input_schema": schema, "required_scope": "permit.submit", "risk": "irreversible"}})
        arguments = {"application_id": "A-18"}
        digest = approval_digest("resident-7", "submit", arguments, "idem-1", 20)
        approval = {"expires_at": 20, "digest": digest}
        first = executor.execute("submit", arguments, principal="resident-7", scopes={"permit.submit"}, idempotency_key="idem-1", now=10, approval=approval)
        second = executor.execute("submit", arguments, principal="resident-7", scopes={"permit.submit"}, idempotency_key="idem-1", now=11, approval=approval)
        self.assertEqual(first, second)
        self.assertEqual(len(executor.side_effects), 1)

    def test_tool_schema_scope_approval_mutation_and_expiry(self) -> None:
        schema = {"type": "object", "required": ["application_id"], "properties": {"application_id": {"type": "string"}}, "additionalProperties": False}
        arguments = {"application_id": "A-18"}
        executor = ToolExecutor({"submit": {"input_schema": schema, "required_scope": "permit.submit", "risk": "irreversible"}})
        digest = approval_digest("resident-7", "submit", arguments, "idem-1", 20)
        with self.assertRaises(ValueError):
            executor.execute("submit", {**arguments, "unexpected": True}, principal="resident-7", scopes={"permit.submit"}, idempotency_key="idem-x", now=10)
        with self.assertRaises(PermissionError):
            executor.execute("submit", arguments, principal="resident-7", scopes=set(), idempotency_key="idem-x", now=10)
        with self.assertRaises(PermissionError):
            executor.execute("submit", {"application_id": "A-19"}, principal="resident-7", scopes={"permit.submit"}, idempotency_key="idem-1", now=10, approval={"expires_at": 20, "digest": digest})
        with self.assertRaises(PermissionError):
            executor.execute("submit", arguments, principal="resident-7", scopes={"permit.submit"}, idempotency_key="idem-1", now=21, approval={"expires_at": 20, "digest": digest})

    def test_workflow_step_cost_and_cancellation_bounds(self) -> None:
        workflow = DurableWorkflow(max_steps=1, max_cost_microunits=10)
        workflow.record_activity("one", {"ok": True}, cost_microunits=10)
        with self.assertRaises(RuntimeError):
            workflow.record_activity("two", {"ok": True}, cost_microunits=1)
        cancelled = DurableWorkflow(max_steps=2, max_cost_microunits=20)
        cancelled.cancel()
        with self.assertRaises(RuntimeError):
            cancelled.record_activity("one", {"ok": True}, cost_microunits=1)

    def test_workflow_replay_does_not_repeat_activity(self) -> None:
        workflow = DurableWorkflow(max_steps=3, max_cost_microunits=30)
        workflow.record_activity("provider-1", {"answer": "bounded"}, cost_microunits=10)
        resumed = DurableWorkflow.resume(workflow.checkpoint(), max_steps=3, max_cost_microunits=30)
        resumed.record_activity("provider-1", {"answer": "different"}, cost_microunits=10)
        self.assertEqual(resumed.used_steps, 1)
        self.assertEqual(resumed.journal[0]["result"]["answer"], "bounded")

    def test_all_scenario_pairs_are_deterministic_and_isolated(self) -> None:
        scenario_root = Path(__file__).parents[1] / "scenarios"
        pairs: dict[str, list[tuple[dict, dict]]] = {}
        for path in sorted(scenario_root.glob("*.json")):
            scenario = load_scenario(path)
            trial = run_scenario(scenario)
            self.assertEqual(trial, run_scenario(scenario))
            self.assertEqual(validate_trial(trial), [])
            pairs.setdefault(scenario["pair_id"], []).append((scenario, trial))
        self.assertEqual(set(pairs), {f"F{number:02d}" for number in range(1, 9)})
        for pair_id, rows in pairs.items():
            self.assertEqual(len(rows), 2)
            broken = next(row for row in rows if row[0]["variant"] == "broken")
            repaired = next(row for row in rows if row[0]["variant"] == "repaired")
            changed = {key for key in CONTROL_KEYS if broken[0]["controls"][key] != repaired[0]["controls"][key]}
            self.assertEqual(len(changed), 1)
            self.assertEqual(broken[1]["shared_input_sha256"], repaired[1]["shared_input_sha256"])
            target = broken[0]["expected"]["target_invariant"]
            self.assertFalse({row["id"]: row["passed"] for row in broken[1]["invariants"]}[target])
            self.assertEqual([row["id"] for row in repaired[1]["invariants"]], list(INVARIANT_IDS))
            self.assertTrue(all(row["passed"] for row in repaired[1]["invariants"]))


if __name__ == "__main__":
    unittest.main()
