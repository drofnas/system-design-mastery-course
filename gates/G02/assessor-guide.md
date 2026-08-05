# G02 Assessor Guide

Use this guide only after the learner freezes every submitted part. Score only
the published module rubrics and evidence for M04, M05, M06. Cite a file
and heading for every finding, preserve reasonable alternatives, and recommend
remediation without drafting replacement graded answers. A Pass creates no
required remediation artifact.

## Review boundaries

Use after the learner freezes all four parts. These notes identify reasoning
boundaries, not one required architecture.

## Written examination

1. Available fan-out plus any local post-admission work is `700 - 90 - 110 =
   500 ms`; a valid answer reserves explicit local work and gives required versus
   optional child caps within that bound. At 260 ms, 330 ms remains before the
   110 ms reserve (`700 - 260 - 110`). Parallel latency follows the slowest
   required child; slots, attempts, bytes, and cost include every child.
2. Bound is `3^3 = 27`. A defensible policy designates one layer, retries only
   transient/safe outcomes, checks deadline, spends attempt/cost tokens, uses
   capped randomized backoff, and sheds overload. Jitter changes timing, not count.
3. No response does not mean no effect. Full-credit answers cover every contract
   field in the question and prove one authoritative effect under concurrency,
   response loss, conflict, crash, and replay.
4. Full-credit comparisons state each control's mechanism, scope, state, and
   displaced failure. Feature definitions without causal failure movement are weak.
5. Retry amplification and health-triggered traffic shifting are credible; CPU,
   connection, or dependency slowdown may be triggers. Disable extra attempts
   under same work and isolate health/restart behavior; correlate logical IDs,
   attempts, destination load, capacity, and recovery rather than guessing.

## Practical

The result is defensible only when prediction predates reveal, raw evidence is
immutable, same-work claims are true, one repair variable changes, arithmetic
agrees, and uncertainty remains bounded. Correctly naming the hidden fault after
reveal cannot repair broken ordering.

## Defense and portfolio

Accept policy alternatives that preserve invariants and bounds under the stated
failure/workload model. Do not require Beacon values. Look for cross-functional
ownership, cost per useful outcome, security/privacy, staged compatibility,
rollback, exception expiry, changed belief, and a separate Week 34 delta.
