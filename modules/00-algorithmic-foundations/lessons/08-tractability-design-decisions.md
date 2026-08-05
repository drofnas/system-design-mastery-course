---
lesson_id: L08
title: "Tractability and Design Decisions"
---

# Tractability and Design Decisions

## Outcomes

- Explain P, NP, and why exact search can become unusable.
- Recognize scheduling, packing, placement, and routing warning signs.
- Choose an engineering response to intractability.

## Mechanism

Some problems grow so fast that exact search stops being a practical option.
The working skill is not proving complexity from scratch. It is recognizing when
a design hides a combinatorial search and replacing "just optimize it" with a
bounded decision strategy.

Common responses include approximation, heuristics, constraint relaxation,
decomposition, cached partial results, and human-approved exceptions.

## Worked Example

Placing shards across regions while satisfying cost, latency, durability,
tenant, and capacity constraints can become a search problem. A practical system
usually narrows the candidate set, scores options, and records the accepted
tradeoff rather than enumerating every assignment.

## Common Expert Mistakes

- Treating an exponential search as a normal background job.
- Hiding constraints in code instead of naming them.
- Optimizing a score without preserving hard invariants.

## Guided Practice

Pick one placement or scheduling decision. Name the hard constraints, soft
preferences, maximum search time, and fallback when the search fails.

## Self-Check

What should you do when exact search is too expensive? Bound the search, relax
the right constraints, use heuristics deliberately, and preserve invariants.

## Sources And Next Work

Study RES-04. M01 is the natural next module after this one.
