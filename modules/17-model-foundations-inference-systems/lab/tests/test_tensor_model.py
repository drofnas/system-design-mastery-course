from __future__ import annotations

import math
import unittest

from inference_lab.model import TinyTokenizer, TinyTransformer
from inference_lab.tensor import finite_difference, matmul, scaled_dot_product_attention, stable_softmax


class TensorModelTests(unittest.TestCase):
    def test_matmul_and_softmax(self) -> None:
        self.assertEqual(matmul([[1.0, 2.0, 0.0]], [[1.0, 0.0], [0.0, 2.0], [1.0, 1.0]]), [[1.0, 4.0]])
        probabilities = stable_softmax([1000.0, 999.0, 997.0])
        self.assertAlmostEqual(sum(probabilities), 1.0)
        self.assertGreater(probabilities[0], probabilities[1])

    def test_attention_is_causal(self) -> None:
        queries = [[1.0, 0.0], [0.0, 1.0]]
        keys = [[1.0, 0.0], [0.0, 1.0]]
        first = scaled_dot_product_attention(queries, keys, [[1.0, 2.0], [99.0, 99.0]])[0]
        self.assertEqual(first, [1.0, 2.0])

    def test_finite_difference(self) -> None:
        self.assertAlmostEqual(finite_difference(lambda value: value * value, 3.0), 6.0, places=5)

    def test_tokenizer_and_model_are_deterministic(self) -> None:
        tokenizer = TinyTokenizer()
        self.assertEqual(tokenizer.encode(" Bronze   owl "), [1, 5, 6])
        left = TinyTransformer(seed=17).generate("bronze owl", 4)
        right = TinyTransformer(seed=17).generate("bronze owl", 4)
        self.assertEqual(left, right)
        self.assertEqual(len(left), 4)


if __name__ == "__main__":
    unittest.main()
