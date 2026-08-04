from __future__ import annotations

import math
from typing import Callable

Vector = list[float]
Matrix = list[Vector]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    if not left or not right or not right[0]:
        raise ValueError("matrices must be non-empty")
    width = len(left[0])
    if any(len(row) != width for row in left):
        raise ValueError("left matrix is ragged")
    if any(len(row) != len(right[0]) for row in right):
        raise ValueError("right matrix is ragged")
    if width != len(right):
        raise ValueError("inner dimensions do not match")
    return [
        [sum(row[k] * right[k][column] for k in range(width)) for column in range(len(right[0]))]
        for row in left
    ]


def transpose(matrix: Matrix) -> Matrix:
    if not matrix or not matrix[0] or any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("matrix must be non-empty and rectangular")
    return [list(column) for column in zip(*matrix)]


def stable_softmax(values: Vector) -> Vector:
    if not values:
        raise ValueError("softmax requires at least one value")
    maximum = max(values)
    shifted = [math.exp(value - maximum) for value in values]
    total = sum(shifted)
    return [value / total for value in shifted]


def l2_norm(values: Vector) -> float:
    return math.sqrt(sum(value * value for value in values))


def cosine_similarity(left: Vector, right: Vector) -> float:
    if len(left) != len(right) or not left:
        raise ValueError("vectors must be non-empty and equal length")
    denominator = l2_norm(left) * l2_norm(right)
    if denominator == 0:
        raise ValueError("cosine similarity is undefined for a zero vector")
    return sum(a * b for a, b in zip(left, right)) / denominator


def finite_difference(function: Callable[[float], float], point: float, step: float = 1e-5) -> float:
    if step <= 0:
        raise ValueError("step must be positive")
    return (function(point + step) - function(point - step)) / (2.0 * step)


def scaled_dot_product_attention(
    queries: Matrix,
    keys: Matrix,
    values: Matrix,
    *,
    causal: bool = True,
) -> Matrix:
    if not queries or not keys or not values:
        raise ValueError("attention inputs must be non-empty")
    if len(keys) != len(values) or len(queries[0]) != len(keys[0]):
        raise ValueError("attention shapes are incompatible")
    scale = math.sqrt(len(keys[0]))
    scores = matmul(queries, transpose(keys))
    output: Matrix = []
    for query_index, row in enumerate(scores):
        masked = [
            (-1e30 if causal and key_index > query_index else value / scale)
            for key_index, value in enumerate(row)
        ]
        weights = stable_softmax(masked)
        output.append(
            [
                sum(weights[key_index] * values[key_index][column] for key_index in range(len(values)))
                for column in range(len(values[0]))
            ]
        )
    return output
