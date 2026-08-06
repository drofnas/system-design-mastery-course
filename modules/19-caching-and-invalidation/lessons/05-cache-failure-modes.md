---
lesson_id: L05
title: "Cache Failure Modes"
---

# Cache Failure Modes

## Outcomes

- Recognize cold start, poisoning, key collision, privacy leak, and stale data failures.
- Connect cache failures to M13 and M16 controls.
- Name observability required for cache diagnosis.

## Mechanism

Caches fail by omission and commission. Cold start removes expected protection.
Poisoning stores a bad representation. Key collisions or incomplete keys serve
the wrong data. Private data leaks when subject or authorization context is
missing. Stale data becomes unsafe when it crosses a freshness or authority line.

The evidence is not just hit rate. You need key dimensions, freshness age,
origin fallback status, regeneration count, subject/tenant boundaries, and
whether stale responses are marked.

## Worked Example

M16's private-cache-leak fixture is the web version of a general rule: a shared
cache key that omits subject identity can serve private content to another
subject.

## Common Expert Mistakes

- Counting a poisoned hit as success.
- Aggregating hit rate across public and private data.
- Missing negative-cache effects on newly created objects.

## Guided Practice

For one cache, list three ways it can return the wrong answer and one metric or
log field that would reveal each one.

## Self-Check

Why is cache privacy a correctness issue, not merely a performance issue?
Because a fast response can still violate authorization and tenant isolation.

## Sources And Next Work

Study RES-02 and revisit M16 F06. Then complete EX-08 and EX-09.
