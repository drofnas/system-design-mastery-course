from __future__ import annotations

import math
import random
from dataclasses import dataclass, field

from .tensor import Matrix, matmul, scaled_dot_product_attention


@dataclass
class KVState:
    """Incremental one-layer attention state for one request identity."""

    token_ids: list[int] = field(default_factory=list)
    keys: Matrix = field(default_factory=list)
    values: Matrix = field(default_factory=list)
    last_logits: list[float] = field(default_factory=list)

    @property
    def token_count(self) -> int:
        return len(self.token_ids)

    def byte_size(self) -> int:
        # Python objects use more memory; this is the declared numeric payload.
        width = len(self.keys[0]) if self.keys else 0
        return 2 * len(self.keys) * width * 8


class TinyTokenizer:
    version = "atlas-tokenizer-v1"

    def __init__(self) -> None:
        tokens = [
            "<pad>", "<bos>", "<eos>", "<unk>", "museum", "bronze", "owl",
            "river", "vessel", "label", "draft", "history", "public", "quiet",
            "light", "stone",
        ]
        self.token_to_id = {token: index for index, token in enumerate(tokens)}
        self.id_to_token = tokens

    def encode(self, text: str) -> list[int]:
        normalized = " ".join(text.lower().strip().split())
        words = normalized.split() if normalized else []
        return [1] + [self.token_to_id.get(word, 3) for word in words]

    def decode(self, token_ids: list[int]) -> str:
        return " ".join(
            self.id_to_token[token_id] if 0 <= token_id < len(self.id_to_token) else "<unk>"
            for token_id in token_ids
            if token_id not in {0, 1, 2}
        )


def _add(left: Matrix, right: Matrix) -> Matrix:
    return [[a + b for a, b in zip(lrow, rrow)] for lrow, rrow in zip(left, right)]


def _layer_norm(matrix: Matrix, epsilon: float = 1e-5) -> Matrix:
    normalized: Matrix = []
    for row in matrix:
        mean = sum(row) / len(row)
        variance = sum((value - mean) ** 2 for value in row) / len(row)
        divisor = math.sqrt(variance + epsilon)
        normalized.append([(value - mean) / divisor for value in row])
    return normalized


def _relu(matrix: Matrix) -> Matrix:
    return [[max(0.0, value) for value in row] for row in matrix]


class TinyTransformer:
    """One-head, one-block deterministic model for mechanism inspection only."""

    version = "atlas-tiny-transformer-v1"

    def __init__(self, seed: int = 17, hidden_size: int = 4) -> None:
        self.tokenizer = TinyTokenizer()
        self.hidden_size = hidden_size
        generator = random.Random(seed)
        vocabulary = len(self.tokenizer.id_to_token)

        def matrix(rows: int, columns: int, scale: float = 0.2) -> Matrix:
            return [[generator.uniform(-scale, scale) for _ in range(columns)] for _ in range(rows)]

        self.embeddings = matrix(vocabulary, hidden_size)
        self.positions = matrix(64, hidden_size, 0.05)
        self.wq = matrix(hidden_size, hidden_size)
        self.wk = matrix(hidden_size, hidden_size)
        self.wv = matrix(hidden_size, hidden_size)
        self.wo = matrix(hidden_size, hidden_size)
        self.ff1 = matrix(hidden_size, hidden_size * 2)
        self.ff2 = matrix(hidden_size * 2, hidden_size)
        self.output = matrix(hidden_size, vocabulary)

    def logits(self, token_ids: list[int]) -> list[float]:
        if not token_ids or len(token_ids) > len(self.positions):
            raise ValueError("token sequence must contain 1 to 64 tokens")
        hidden = [
            [self.embeddings[token_id][column] + self.positions[position][column] for column in range(self.hidden_size)]
            for position, token_id in enumerate(token_ids)
        ]
        normalized = _layer_norm(hidden)
        attention = scaled_dot_product_attention(
            matmul(normalized, self.wq),
            matmul(normalized, self.wk),
            matmul(normalized, self.wv),
        )
        residual = _add(hidden, matmul(attention, self.wo))
        feed_forward = matmul(_relu(matmul(_layer_norm(residual), self.ff1)), self.ff2)
        final = _layer_norm(_add(residual, feed_forward))
        return matmul([final[-1]], self.output)[0]

    def extend_kv(self, state: KVState, token_id: int) -> list[float]:
        """Append one token and compute only its new K/V row and output logits."""

        position = len(state.token_ids)
        if position >= len(self.positions):
            raise ValueError("token sequence cannot exceed 64 tokens")
        if not 0 <= token_id < len(self.tokenizer.id_to_token):
            raise ValueError("token id is outside the vocabulary")
        hidden = [[self.embeddings[token_id][column] + self.positions[position][column] for column in range(self.hidden_size)]]
        normalized = _layer_norm(hidden)
        query = matmul(normalized, self.wq)
        state.keys.extend(matmul(normalized, self.wk))
        state.values.extend(matmul(normalized, self.wv))
        # This query is for the newest position, so every cached key precedes it.
        attention = scaled_dot_product_attention(query, state.keys, state.values, causal=False)
        residual = _add(hidden, matmul(attention, self.wo))
        feed_forward = matmul(_relu(matmul(_layer_norm(residual), self.ff1)), self.ff2)
        final = _layer_norm(_add(residual, feed_forward))
        state.token_ids.append(token_id)
        state.last_logits = matmul(final, self.output)[0]
        return state.last_logits

    def prefill(self, prompt: str) -> KVState:
        state = KVState()
        for token_id in self.tokenizer.encode(prompt):
            self.extend_kv(state, token_id)
        return state

    def generate_iter(self, state: KVState, max_output_tokens: int = 4):
        if not 1 <= max_output_tokens <= 16:
            raise ValueError("max_output_tokens must be between 1 and 16")
        if not state.last_logits:
            raise ValueError("prefill state is empty")
        for _ in range(max_output_tokens):
            next_token = max(range(len(self.tokenizer.id_to_token)), key=state.last_logits.__getitem__)
            self.extend_kv(state, next_token)
            yield next_token
            if next_token == 2 or state.token_count >= 64:
                break

    def generate(self, prompt: str, max_output_tokens: int = 4) -> list[int]:
        if not 1 <= max_output_tokens <= 16:
            raise ValueError("max_output_tokens must be between 1 and 16")
        token_ids = self.tokenizer.encode(prompt)
        generated: list[int] = []
        for _ in range(max_output_tokens):
            next_token = max(range(len(self.tokenizer.id_to_token)), key=self.logits(token_ids).__getitem__)
            generated.append(next_token)
            token_ids.append(next_token)
            if next_token == 2 or len(token_ids) >= 64:
                break
        return generated
