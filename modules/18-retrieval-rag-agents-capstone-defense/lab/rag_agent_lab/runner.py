from __future__ import annotations

import hashlib
import json
import platform
from copy import deepcopy
from typing import Any

from .config import INVARIANT_IDS
from .evaluation import ndcg_at_k, recall_at_k, reciprocal_rank
from .retrieval import HNSWIndex, bm25, exact_search, reciprocal_rank_fusion, transparent_rerank


DOCUMENTS = {
    "code-v3": "solar permit structural drawing roof load current code",
    "faq-v2": "solar permit application requires site plan and electrical diagram",
    "bulletin-v1": "expedited residential solar review eligibility",
    "revoked-v1": "old solar permit application needs no electrical diagram",
    "private-v4": "resident private parcel application draft",
}
VECTORS = {
    "code-v3": [0.95, 0.10, 0.05, 0.20],
    "faq-v2": [0.88, 0.18, 0.08, 0.15],
    "bulletin-v1": [0.76, 0.22, 0.10, 0.32],
    "revoked-v1": [0.91, 0.08, 0.04, 0.12],
    "private-v4": [0.30, 0.90, 0.15, 0.10],
}
QUERY_VECTOR = [1.0, 0.12, 0.05, 0.18]
RELEVANCE = {"code-v3": 3, "faq-v2": 2, "bulletin-v1": 1}


def _canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _sha256(value: Any) -> str:
    return hashlib.sha256(_canonical(value)).hexdigest()


def _shared_input(scenario: dict[str, Any]) -> dict[str, Any]:
    shared = deepcopy(scenario)
    for key in ("scenario_id", "variant", "controls"):
        shared.pop(key)
    return shared


def run_scenario(scenario: dict[str, Any]) -> dict[str, Any]:
    pair = scenario["pair_id"]
    controls = scenario["controls"]
    workload = scenario["workload"]
    corpus = scenario["corpus_snapshot"]

    exact_ids = [key for key, _ in exact_search(VECTORS, QUERY_VECTOR, 3)]
    index = HNSWIndex(m=3, ef_construction=5, seed=scenario["seed"])
    index.build(VECTORS)
    approximate = index.search(QUERY_VECTOR, k=3, ef_search=5)
    lexical_ids = [key for key, _ in bm25(DOCUMENTS, workload["query"])]
    fused = reciprocal_rank_fusion([lexical_ids, approximate.ids])
    hybrid_ids = [key for key, _ in transparent_rerank(workload["query"], DOCUMENTS, fused)[:3]]

    stale_index = pair == "F01" and not controls["fresh_index_gate"]
    revoked_hits = 1 if pair == "F02" and not controls["revocation_enforcement"] else 0
    low_quality = pair == "F03" and not controls["quality_release_gate"]
    injection_acted_on = pair == "F04" and not controls["untrusted_content_is_data"]
    provider_unbounded = pair == "F05" and not controls["bounded_provider_activity"]
    replay_unsafe = pair == "F06" and not controls["durable_idempotency"]
    budget_unbounded = pair == "F07" and not controls["budget_and_cancellation_bounds"]
    unauthorized = pair == "F08" and not controls["approval_authorization_gate"]

    recall = recall_at_k(hybrid_ids, set(RELEVANCE), 3)
    mrr = reciprocal_rank(hybrid_ids, set(RELEVANCE))
    ndcg = ndcg_at_k(hybrid_ids, RELEVANCE, 3)
    if low_quality:
        recall, ndcg = 1 / 3, 0.41
    release_passed = recall >= 2 / 3 and ndcg >= 0.75
    if low_quality:
        release_passed = True

    elapsed_ms = workload["provider_delay_ms"] * (3 if provider_unbounded else 1)
    used_steps = workload["planned_steps"] + (4 if budget_unbounded else 0)
    used_cost = used_steps * workload["cost_per_step_microunits"]
    duplicate_side_effects = 1 if replay_unsafe else 0
    approval_consumed = workload["approval_present"] and not unauthorized
    cancelled = workload["cancellation_at_step"] is not None
    outstanding_work = 2 if budget_unbounded else 0
    authorization_source = "model-proposed" if unauthorized or injection_acted_on else "deterministic-executor"
    secrets_exposed = 1 if injection_acted_on else 0

    invariant_pass = {
        "I01": True,
        "I02": not stale_index,
        "I03": revoked_hits == 0,
        "I04": release_passed and not low_quality,
        "I05": not stale_index and corpus["index_version"] == corpus["source_version"],
        "I06": True,
        "I07": authorization_source == "deterministic-executor" and secrets_exposed == 0,
        "I08": not unauthorized and approval_consumed,
        "I09": duplicate_side_effects == 0,
        "I10": not replay_unsafe,
        "I11": elapsed_ms <= workload["deadline_ms"] and used_steps <= workload["max_steps"] and used_cost <= workload["max_cost_microunits"] and outstanding_work == 0,
        "I12": secrets_exposed == 0,
    }

    citations = [
        {"source_id": "code-v3", "version": 2 if stale_index else 3},
        {"source_id": "faq-v2", "version": 2},
    ]
    supported_claims = 1 if low_quality else 2
    unsupported_claims = 1 if low_quality else 0
    total_cost = 180 + len(index.vectors) * 5 + used_cost + (400 if provider_unbounded else 120)

    return {
        "module_id": "M18",
        "schema_version": "1.0",
        "scenario_id": scenario["scenario_id"],
        "pair_id": pair,
        "variant": scenario["variant"],
        "seed": scenario["seed"],
        "evidence_kind": "modeled",
        "shared_input_sha256": _sha256(_shared_input(scenario)),
        "config_sha256": _sha256(scenario),
        "corpus_sha256": corpus["sha256"],
        "evaluation_set_sha256": scenario["evaluation_set"]["sha256"],
        "toolchain": {"python": platform.python_version(), "lab_version": "1.0"},
        "retrieval": {
            "exact_ids": exact_ids,
            "approximate_ids": approximate.ids,
            "lexical_ids": lexical_ids[:3],
            "hybrid_ids": hybrid_ids,
            "recall_at_3": round(recall, 4),
            "mrr": round(mrr, 4),
            "ndcg_at_3": round(ndcg, 4),
            "visited_nodes": approximate.visited,
            "index_bytes_estimate": len(index.vectors) * 4 * 8 + sum(len(neighbors) for neighbors in index.graph[0].values()) * 8,
            "release_passed": release_passed,
        },
        "answer": {
            "abstained": False,
            "grounded_claims": supported_claims,
            "unsupported_claims": unsupported_claims,
            "citations": citations,
            "citation_versions_valid": not stale_index,
            "revoked_hits": revoked_hits,
        },
        "workflow": {
            "events": ["request.accepted", "retrieval.completed", "answer.evaluated", "tool.proposed", "workflow.completed"],
            "checkpoint": "after-tool-proposal",
            "resumed": pair == "F06",
            "duplicate_side_effects": duplicate_side_effects,
            "authorization_source": authorization_source,
            "approval_consumed": approval_consumed,
            "tool_records": [{"tool": "submit-permit-application", "schema_version": "1.0", "authorization_source": authorization_source}],
            "approval_records": [{"present": workload["approval_present"], "consumed": approval_consumed, "binding": "principal+action+arguments+expiry+idempotency"}],
            "idempotency_records": [{"key": "civicaid-submit-1", "side_effect_count": 1 + duplicate_side_effects}],
            "cancelled": cancelled,
            "outstanding_work": outstanding_work,
        },
        "budget": {
            "max_steps": workload["max_steps"],
            "used_steps": used_steps,
            "max_cost_microunits": workload["max_cost_microunits"],
            "used_cost_microunits": used_cost,
            "deadline_ms": workload["deadline_ms"],
            "elapsed_ms": elapsed_ms,
        },
        "audit": {
            "records": ["principal", "request", "retrieval_snapshot", "citations", "tool_schema", "authorization", "approval", "idempotency", "outcome"],
            "secrets_exposed": secrets_exposed,
            "complete": not (injection_acted_on or unauthorized),
        },
        "cost": {
            "index_units": len(index.vectors) * 5,
            "query_units": 180,
            "provider_units": 400 if provider_unbounded else 120,
            "total_microunits": total_cost,
            "cost_per_supported_answer": round(total_cost / max(supported_claims, 1), 2),
        },
        "invariants": [
            {"id": invariant_id, "passed": invariant_pass[invariant_id], "evidence": f"{invariant_id}={str(invariant_pass[invariant_id]).lower()} in {pair} modeled trial"}
            for invariant_id in INVARIANT_IDS
        ],
        "limitations": [
            "The deterministic fixture proves repository contracts, not production retrieval relevance or model quality.",
            "Work-unit latency, memory, and cost values are modeled and must not be presented as hardware measurements.",
            "CivicAid data is synthetic and contains no commerce solution, resident record, credential, or private municipal data.",
        ],
    }
