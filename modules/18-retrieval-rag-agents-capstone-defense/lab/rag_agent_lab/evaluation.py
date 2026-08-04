from __future__ import annotations

import math


def recall_at_k(ranked: list[str], relevant: set[str], k: int) -> float:
    return 0.0 if not relevant else len(set(ranked[:k]) & relevant) / len(relevant)


def reciprocal_rank(ranked: list[str], relevant: set[str]) -> float:
    for position, key in enumerate(ranked, start=1):
        if key in relevant:
            return 1.0 / position
    return 0.0


def ndcg_at_k(ranked: list[str], relevance: dict[str, int], k: int) -> float:
    def dcg(values: list[int]) -> float:
        return sum((2**value - 1) / math.log2(position + 1) for position, value in enumerate(values, start=1))
    observed = dcg([relevance.get(key, 0) for key in ranked[:k]])
    ideal = dcg(sorted(relevance.values(), reverse=True)[:k])
    return 0.0 if ideal == 0 else observed / ideal


def evaluate_answer(answer: dict, documents: dict[str, dict], *, authorized_ids: set[str]) -> dict:
    supported = 0
    unsupported = 0
    citations = []
    versions_valid = True
    revoked_hits = 0
    for claim in answer.get("claims", []):
        evidence = claim.get("evidence", [])
        claim_supported = False
        for citation in evidence:
            source = documents.get(citation.get("source_id"))
            citations.append(citation)
            if source is None or citation.get("source_id") not in authorized_ids:
                versions_valid = False
                continue
            if source["version"] != citation.get("version"):
                versions_valid = False
            if source.get("revoked", False):
                revoked_hits += 1
            if claim.get("text") in source.get("claims", []):
                claim_supported = True
        if claim_supported:
            supported += 1
        else:
            unsupported += 1
    return {
        "abstained": bool(answer.get("abstained")),
        "grounded_claims": supported,
        "unsupported_claims": unsupported,
        "citations": citations,
        "citation_versions_valid": versions_valid,
        "revoked_hits": revoked_hits,
    }
