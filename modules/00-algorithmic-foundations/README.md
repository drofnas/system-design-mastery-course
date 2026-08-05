# Module 00: Algorithmic Foundations

This draft module adds the course's missing computer-science base without
reteaching programming syntax. It assumes you can already write code and focuses
on the analytical vocabulary behind data-structure and algorithm choices.

## Prerequisites

- Comfortable reading Python-like pseudocode and small programs.
- Able to run local command-line tools.
- Willing to separate asymptotic claims from local measurements.

## Outcomes

- Explain Big-O, theta, omega, and amortized cost in design language.
- Choose a data structure from operation mix, locality, growth, and failure mode.
- Recognize graph, sorting, selection, and tractability questions inside systems.
- Run a small local harness and state its limits.

## Lessons

1. [Asymptotic Analysis and Its Limits](lessons/01-asymptotic-analysis-and-limits.md)
2. [Arrays, Dynamic Arrays, and Locality](lessons/02-arrays-dynamic-arrays-locality.md)
3. [Hash Tables](lessons/03-hash-tables.md)
4. [Trees and Balanced Search](lessons/04-trees-balanced-search.md)
5. [Heaps and Priority Queues](lessons/05-heaps-priority-queues.md)
6. [Graphs and Traversal](lessons/06-graphs-traversal.md)
7. [Sorting and Selection](lessons/07-sorting-selection.md)
8. [Tractability and Design Decisions](lessons/08-tractability-design-decisions.md)

## Practice And Lab

Complete [exercises](exercises/exercises.md), then compare your reasoning with
the [answer key](exercises/answer-key.md). The optional
[complexity lab](lab/README.md) emits deterministic evidence about operation
counts and bounded local timing.

## Quiz Status

This module is draft. Its quiz package is intentionally deferred to the next
quiz-bank cycle.

## Optional Project

Pick one product workflow with a hidden data-structure choice. Name the workload,
the operations, the expected growth, the failure mode, and the measurement that
would change your decision.
