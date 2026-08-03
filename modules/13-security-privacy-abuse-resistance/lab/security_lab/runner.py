"""Deterministic security control model with inspectable decision evidence."""

from __future__ import annotations

import hashlib
import json
from typing import Any


INVARIANTS = {
    "I01": ("authentication and session evidence is current and replay resistant", "credential_lifecycle"),
    "I02": ("every object and action receives a deny-by-default authorization decision", "object_action_authorization"),
    "I03": ("tenant context is derived from trusted identity and propagated", "tenant_context_binding"),
    "I04": ("no unauthorized cross-tenant object access is returned", "tenant_context_binding"),
    "I05": ("credentials are scoped, revocable, and rotated without accepting exposed versions", "scoped_secret_rotation"),
    "I06": ("security events are attributable, minimally sensitive, and tamper detectable", "tamper_evident_audit"),
    "I07": ("retention and deletion outcomes cover authoritative and derived copies", "complete_deletion"),
    "I08": ("dependencies match approved identity and verified provenance", "dependency_verification"),
    "I09": ("per-subject and per-tenant budgets bound abusive work and cost", "abuse_budget_enforcement"),
    "I10": ("retrieved content remains untrusted data and cannot grant authority", "untrusted_content_tool_authorization"),
    "I11": ("high-risk tool use requires deterministic authorization, approval, and identity", "untrusted_content_tool_authorization"),
    "I12": ("scenario identity, pair inputs, controls, and evidence limits are reproducible", None),
}


def canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def digest(value: Any) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def run_scenario(scenario: dict[str, Any]) -> dict[str, Any]:
    controls = scenario["controls"]
    identity = scenario["identity"]
    tenant = scenario["tenant"]
    request = scenario["request"]
    credential = scenario["credential"]
    lifecycle = scenario["data_lifecycle"]
    dependency = scenario["dependency"]
    retrieved = scenario["retrieved_content"]

    session_current = (
        identity["authenticated"]
        and identity["session_age_minutes"] <= credential["expires_after_minutes"]
        and not credential["revoked"]
    )
    role_allows = identity["role"] == request["required_role"]
    tenant_matches = tenant["subject_tenant"] == tenant["resource_tenant"]
    credential_scope_matches = credential["scope"] == credential["required_scope"]
    exposed_rejected = credential["exposed_version"] < credential["active_version"]
    dependency_matches = dependency["approved_digest"] == dependency["observed_digest"]
    copies_present_before = any(
        lifecycle[name] for name in ("authoritative", "cache", "index", "backup")
    )
    deletion_complete = (
        controls["complete_deletion"] if lifecycle["delete_requested"] else True
    )

    shared = {
        key: scenario[key]
        for key in (
            "pair_id", "seed", "identity", "tenant", "request", "credential",
            "data_lifecycle", "dependency", "retrieved_content",
        )
    }
    rows = []
    for invariant_id, (name, control) in INVARIANTS.items():
        passed = True if control is None else bool(controls[control])
        rows.append({
            "id": invariant_id,
            "name": name,
            "passed": passed,
            "evidence": f"{control or 'contract_identity'}={passed}; pair={scenario['pair_id']}",
        })

    session_allows = session_current if controls["credential_lifecycle"] else True
    policy_allows = role_allows if controls["object_action_authorization"] else True
    effective_tenant_matches = (
        tenant_matches
        if controls["tenant_context_binding"]
        else tenant["requested_tenant"] == tenant["resource_tenant"]
    )
    authorization_allowed = (
        identity["authenticated"]
        and session_allows
        and policy_allows
        and effective_tenant_matches
    )
    if controls["untrusted_content_tool_authorization"]:
        tool_allowed = (
            retrieved["user_authorized"]
            and (not request["high_risk"] or retrieved["approval_present"])
            and bool(retrieved["idempotency_key"])
        )
    else:
        tool_allowed = retrieved["requests_tool"]

    return {
        "schema_version": "1.0",
        "scenario_id": scenario["scenario_id"],
        "pair_id": scenario["pair_id"],
        "variant": scenario["variant"],
        "seed": scenario["seed"],
        "scenario_sha256": digest(scenario),
        "shared_input_sha256": digest(shared),
        "config_sha256": digest(controls),
        "identity_session": {
            "subject_id": identity["subject_id"],
            "authenticated": identity["authenticated"],
            "session_current_from_input": session_current,
            "lifecycle_enforced": controls["credential_lifecycle"],
        },
        "authorization": {
            "resource_id": request["resource_id"],
            "action": request["action"],
            "role_allows": role_allows,
            "decision": "allow" if authorization_allowed else "deny",
            "object_action_check": controls["object_action_authorization"],
        },
        "tenant_isolation": {
            "subject_tenant": tenant["subject_tenant"],
            "resource_tenant": tenant["resource_tenant"],
            "requested_tenant_ignored": controls["tenant_context_binding"],
            "tenant_matches": tenant_matches,
            "cross_tenant_result_returned": not controls["tenant_context_binding"] and not tenant_matches,
        },
        "secret_lifecycle": {
            "scope_matches": credential_scope_matches,
            "exposed_version_rejected": controls["scoped_secret_rotation"] and exposed_rejected,
            "rotation_enforced": controls["scoped_secret_rotation"],
        },
        "audit_evidence": {
            "event_attributable": controls["tamper_evident_audit"],
            "tampering_detected": controls["tamper_evident_audit"] and lifecycle["audit_tampered"],
            "sensitive_value_excluded": controls["tamper_evident_audit"] and not lifecycle["sensitive_logged"],
        },
        "deletion_evidence": {
            "delete_requested": lifecycle["delete_requested"],
            "copies_present_before_control": copies_present_before,
            "lifecycle_obligation_satisfied": deletion_complete,
            "verification_complete": controls["complete_deletion"],
            "exceptions_recorded": controls["complete_deletion"],
        },
        "dependency_verification": {
            "name": dependency["name"],
            "digest_matches": dependency_matches,
            "provenance_input": dependency["provenance_verified"],
            "accepted": (
                dependency_matches and dependency["provenance_verified"]
                if controls["dependency_verification"]
                else True
            ),
        },
        "abuse_controls": {
            "subject_budget_enforced": controls["abuse_budget_enforcement"],
            "tenant_budget_enforced": controls["abuse_budget_enforcement"],
            "denial_is_attributable": controls["abuse_budget_enforcement"] and controls["tamper_evident_audit"],
        },
        "tool_authorization": {
            "retrieved_content_trusted": retrieved["trusted"],
            "requested_tool": retrieved["tool"],
            "content_can_grant_authority": not controls["untrusted_content_tool_authorization"],
            "approval_present": retrieved["approval_present"],
            "idempotency_present": bool(retrieved["idempotency_key"]),
            "decision": "allow" if tool_allowed else "deny",
        },
        "invariants": rows,
        "evidence_boundaries": [
            "deterministic policy model, not production isolation or penetration-test evidence",
            "logical lifecycle records, not proof of physical deletion or cryptographic strength",
            "fixed attacks and controls, not resistance to adaptive adversaries or legal compliance",
        ],
    }
