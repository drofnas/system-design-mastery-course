from __future__ import annotations

import unittest

from rag_agent_lab.evaluation import ndcg_at_k, recall_at_k, reciprocal_rank
from rag_agent_lab.retrieval import HNSWIndex, bm25, exact_search, reciprocal_rank_fusion


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


if __name__ == "__main__":
    unittest.main()
