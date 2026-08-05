from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from security_lab.config import CONTROL_KEYS, load_scenario, validate_trial
from security_lab.runner import run_scenario


class SecurityLabTests(unittest.TestCase):
    def trial(self, name: str) -> dict:
        return run_scenario(load_scenario(ROOT / "scenarios" / name))

    def test_all_pairs_are_deterministic_and_repaired(self) -> None:
        pairs: dict[str, list[tuple[dict, dict]]] = {}
        for path in sorted((ROOT / "scenarios").glob("*.json")):
            scenario = load_scenario(path)
            trial = run_scenario(scenario)
            self.assertEqual(trial, run_scenario(scenario))
            self.assertEqual([], validate_trial(trial))
            pairs.setdefault(trial["pair_id"], []).append((scenario, trial))
        self.assertEqual({f"F{number:02d}" for number in range(1, 10)}, set(pairs))
        for pair_id, rows in pairs.items():
            self.assertEqual(2, len(rows), pair_id)
            self.assertEqual({"broken", "repaired"}, {trial["variant"] for _, trial in rows})
            self.assertEqual(1, len({trial["shared_input_sha256"] for _, trial in rows}))
            self.assertEqual(2, len({trial["config_sha256"] for _, trial in rows}))
            broken_scenario = next(s for s, t in rows if t["variant"] == "broken")
            repaired_scenario = next(s for s, t in rows if t["variant"] == "repaired")
            changed = {
                key for key in CONTROL_KEYS
                if broken_scenario["controls"][key] != repaired_scenario["controls"][key]
            }
            self.assertEqual(1, len(changed), pair_id)
            broken = next(t for _, t in rows if t["variant"] == "broken")
            target = broken_scenario["expected"]["target_invariant"]
            self.assertFalse({row["id"]: row["passed"] for row in broken["invariants"]}[target])
            repaired = next(t for _, t in rows if t["variant"] == "repaired")
            self.assertTrue(all(row["passed"] for row in repaired["invariants"]), pair_id)

    def test_broken_variants_expose_observable_security_failures(self) -> None:
        broken = {
            path.name.split("-", 1)[0].upper(): run_scenario(load_scenario(path))
            for path in sorted((ROOT / "scenarios").glob("*-broken.json"))
        }
        self.assertEqual("allow", broken["F01"]["authorization"]["decision"])
        self.assertTrue(broken["F01"]["tenant_isolation"]["cross_tenant_result_returned"])
        self.assertEqual("allow", broken["F02"]["authorization"]["decision"])
        self.assertEqual("allow", broken["F03"]["authorization"]["decision"])
        self.assertFalse(broken["F04"]["secret_lifecycle"]["exposed_version_rejected"])
        self.assertFalse(broken["F05"]["audit_evidence"]["tampering_detected"])
        self.assertFalse(broken["F06"]["deletion_evidence"]["lifecycle_obligation_satisfied"])
        self.assertTrue(broken["F07"]["dependency_verification"]["accepted"])
        self.assertFalse(broken["F08"]["abuse_controls"]["tenant_budget_enforced"])
        self.assertEqual("allow", broken["F09"]["tool_authorization"]["decision"])

    def test_unknown_field_is_rejected(self) -> None:
        source = json.loads((ROOT / "scenarios/f01-cross-tenant-access-repaired.json").read_text())
        source["unexpected"] = True
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.json"
            path.write_text(json.dumps(source), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "scenario fields differ"):
                load_scenario(path)

    def test_cross_tenant_access_returns_data_only_when_binding_is_missing(self) -> None:
        broken = self.trial("f01-cross-tenant-access-broken.json")
        repaired = self.trial("f01-cross-tenant-access-repaired.json")
        self.assertTrue(broken["tenant_isolation"]["cross_tenant_result_returned"])
        self.assertEqual("allow", broken["authorization"]["decision"])
        self.assertFalse(repaired["tenant_isolation"]["cross_tenant_result_returned"])
        self.assertEqual("deny", repaired["authorization"]["decision"])

    def test_privilege_escalation_is_denied_by_object_action_authorization(self) -> None:
        broken = self.trial("f02-privilege-escalation-broken.json")
        repaired = self.trial("f02-privilege-escalation-repaired.json")
        self.assertFalse(broken["authorization"]["role_allows"])
        self.assertFalse(broken["authorization"]["object_action_check"])
        self.assertEqual("allow", broken["authorization"]["decision"])
        self.assertFalse(repaired["authorization"]["role_allows"])
        self.assertTrue(repaired["authorization"]["object_action_check"])
        self.assertEqual("deny", repaired["authorization"]["decision"])

    def test_credential_replay_requires_current_session_lifecycle(self) -> None:
        broken = self.trial("f03-credential-replay-broken.json")
        repaired = self.trial("f03-credential-replay-repaired.json")
        self.assertFalse(broken["identity_session"]["session_current_from_input"])
        self.assertFalse(broken["identity_session"]["lifecycle_enforced"])
        self.assertEqual("allow", broken["authorization"]["decision"])
        self.assertFalse(repaired["identity_session"]["session_current_from_input"])
        self.assertTrue(repaired["identity_session"]["lifecycle_enforced"])
        self.assertEqual("deny", repaired["authorization"]["decision"])

    def test_secret_exposure_rejects_old_exposed_versions_after_rotation(self) -> None:
        broken = self.trial("f04-secret-exposure-broken.json")
        repaired = self.trial("f04-secret-exposure-repaired.json")
        self.assertFalse(broken["secret_lifecycle"]["rotation_enforced"])
        self.assertFalse(broken["secret_lifecycle"]["exposed_version_rejected"])
        self.assertTrue(repaired["secret_lifecycle"]["rotation_enforced"])
        self.assertTrue(repaired["secret_lifecycle"]["exposed_version_rejected"])

    def test_audit_tampering_is_detected_without_logging_sensitive_values(self) -> None:
        broken = self.trial("f05-audit-tampering-broken.json")
        repaired = self.trial("f05-audit-tampering-repaired.json")
        self.assertFalse(broken["audit_evidence"]["event_attributable"])
        self.assertFalse(broken["audit_evidence"]["tampering_detected"])
        self.assertFalse(broken["audit_evidence"]["sensitive_value_excluded"])
        self.assertTrue(repaired["audit_evidence"]["event_attributable"])
        self.assertTrue(repaired["audit_evidence"]["tampering_detected"])
        self.assertTrue(repaired["audit_evidence"]["sensitive_value_excluded"])

    def test_deletion_gap_covers_authoritative_and_derived_copies(self) -> None:
        broken = self.trial("f06-deletion-gap-broken.json")
        repaired = self.trial("f06-deletion-gap-repaired.json")
        self.assertTrue(broken["deletion_evidence"]["delete_requested"])
        self.assertTrue(broken["deletion_evidence"]["copies_present_before_control"])
        self.assertFalse(broken["deletion_evidence"]["lifecycle_obligation_satisfied"])
        self.assertTrue(repaired["deletion_evidence"]["verification_complete"])
        self.assertTrue(repaired["deletion_evidence"]["exceptions_recorded"])
        self.assertTrue(repaired["deletion_evidence"]["lifecycle_obligation_satisfied"])

    def test_dependency_compromise_rejects_digest_or_provenance_mismatch(self) -> None:
        broken = self.trial("f07-dependency-compromise-broken.json")
        repaired = self.trial("f07-dependency-compromise-repaired.json")
        self.assertFalse(broken["dependency_verification"]["digest_matches"])
        self.assertFalse(broken["dependency_verification"]["provenance_input"])
        self.assertTrue(broken["dependency_verification"]["accepted"])
        self.assertFalse(repaired["dependency_verification"]["digest_matches"])
        self.assertFalse(repaired["dependency_verification"]["provenance_input"])
        self.assertFalse(repaired["dependency_verification"]["accepted"])

    def test_economic_abuse_is_bounded_per_subject_and_tenant(self) -> None:
        broken = self.trial("f08-economic-abuse-broken.json")
        repaired = self.trial("f08-economic-abuse-repaired.json")
        self.assertFalse(broken["abuse_controls"]["subject_budget_enforced"])
        self.assertFalse(broken["abuse_controls"]["tenant_budget_enforced"])
        self.assertTrue(repaired["abuse_controls"]["subject_budget_enforced"])
        self.assertTrue(repaired["abuse_controls"]["tenant_budget_enforced"])
        self.assertTrue(repaired["abuse_controls"]["denial_is_attributable"])

    def test_retrieved_instruction_cannot_grant_tool_authority(self) -> None:
        broken = self.trial("f09-retrieved-instruction-broken.json")
        repaired = self.trial("f09-retrieved-instruction-repaired.json")
        self.assertTrue(broken["tool_authorization"]["content_can_grant_authority"])
        self.assertEqual("allow", broken["tool_authorization"]["decision"])
        self.assertFalse(repaired["tool_authorization"]["content_can_grant_authority"])
        self.assertEqual("deny", repaired["tool_authorization"]["decision"])


if __name__ == "__main__":
    unittest.main()
