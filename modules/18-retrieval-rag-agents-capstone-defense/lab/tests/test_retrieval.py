from __future__ import annotations

import unittest

from rag_agent_lab.evaluation import evaluate_answer, ndcg_at_k, recall_at_k, reciprocal_rank
from rag_agent_lab.retrieval import HNSWIndex, bm25, exact_search, filter_documents, reciprocal_rank_fusion, transparent_rerank


class RetrievalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.vectors = {"a": [1.0, 0.0], "b": [0.9, 0.1], "c": [0.0, 1.0], "d": [0.6, 0.4]}

    def test_exact_search_is_an_oracle(self) -> None:
        self.assertEqual([key for key, _ in exact_search(self.vectors, [1.0, 0.0], 2)], ["a", "b"])

    def test_hnsw_is_seeded_and_finds_the_nearest_neighbor(self) -> None:
        first = HNSWIndex(m=2, ef_construction=4, seed=18)
        second = HNSWIndex(m=2, ef_construction=4, seed=18)
        first.build(self.vectors)
        second.build(self.vectors)
        one = first.search([1.0, 0.0], k=2, ef_search=4)
        two = second.search([1.0, 0.0], k=2, ef_search=4)
        self.assertEqual(one, two)
        self.assertEqual(one.ids[0], "a")

    def test_lexical_fusion_and_metrics(self) -> None:
        documents = {"a": "current solar permit code", "b": "permit application solar diagram", "c": "tree removal"}
        lexical = [key for key, _ in bm25(documents, "solar permit")]
        fused = [key for key, _ in reciprocal_rank_fusion([lexical, ["b", "a", "c"]])]
        self.assertEqual(set(fused[:2]), {"a", "b"})
        self.assertEqual(recall_at_k(fused, {"a", "b"}, 2), 1.0)
        self.assertGreater(reciprocal_rank(fused, {"a"}), 0)
        self.assertGreater(ndcg_at_k(fused, {"a": 3, "b": 2}, 2), 0.8)

    def test_hnsw_search_effort_is_bounded_and_recall_compares_to_oracle(self) -> None:
        index = HNSWIndex(m=2, ef_construction=4, seed=18)
        index.build(self.vectors)
        oracle = [key for key, _ in exact_search(self.vectors, [1.0, 0.0], 3)]
        narrow = index.search([1.0, 0.0], k=2, ef_search=2)
        wide = index.search([1.0, 0.0], k=2, ef_search=4)
        self.assertLessEqual(narrow.visited, len(self.vectors))
        self.assertLessEqual(wide.visited, len(self.vectors))
        self.assertGreaterEqual(recall_at_k(wide.ids, set(oracle[:2]), 2), recall_at_k(narrow.ids, set(oracle[:2]), 2))

    def test_filtering_grounding_versions_and_abstention(self) -> None:
        documents = [
            {"id": "public", "required_scope": "public.read", "source_version": 3, "revoked_at_epoch": None},
            {"id": "private", "required_scope": "resident-8.private", "source_version": 3, "revoked_at_epoch": None},
            {"id": "revoked", "required_scope": "public.read", "source_version": 3, "revoked_at_epoch": 7},
        ]
        eligible = filter_documents(documents, scopes={"public.read"}, source_version=3, revocation_epoch=7)
        self.assertEqual([row["id"] for row in eligible], ["public"])
        evidence = {"public": {"version": 3, "claims": ["A site plan is required."], "revoked": False}}
        answer = {"claims": [
            {"text": "A site plan is required.", "evidence": [{"source_id": "public", "version": 3}]},
            {"text": "Approval is guaranteed.", "evidence": []},
        ], "abstained": True}
        result = evaluate_answer(answer, evidence, authorized_ids={"public"})
        self.assertEqual(result["grounded_claims"], 1)
        self.assertEqual(result["unsupported_claims"], 1)
        self.assertTrue(result["abstained"])

    def test_transparent_reranking_is_deterministic(self) -> None:
        documents = {"a": "permit code", "b": "permit code solar", "c": "tree"}
        candidates = [("a", 0.1), ("b", 0.1), ("c", 0.2)]
        self.assertEqual(transparent_rerank("solar permit", documents, candidates), transparent_rerank("solar permit", documents, candidates))


if __name__ == "__main__":
    unittest.main()
