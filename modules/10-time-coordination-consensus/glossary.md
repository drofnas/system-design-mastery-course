# Module 10 Glossary

| Term | Operational meaning |
|---|---|
| Clock drift | Rate error between a clock and its reference over an interval. |
| Clock skew | Difference between two clock readings at a chosen real instant. |
| Clock uncertainty | An explicit interval within which real time is believed to lie. |
| Happened-before | Partial order induced by process order, message send/receive, and transitivity. |
| Concurrent events | Events for which neither happened-before relationship holds. |
| Lamport clock | Scalar counter preserving `a → b` implies `L(a) < L(b)`; the converse does not hold. |
| Vector clock | Per-participant counters that can distinguish causal order from concurrency under a fixed identity set. |
| Safety | A forbidden state or event never occurs. No amount of waiting repairs a safety violation. |
| Liveness | A desired event eventually occurs under stated fairness and timing assumptions. |
| Failure detector | A suspicion mechanism whose completeness and accuracy assumptions influence progress; timeout is not proof. |
| Consensus | Agreement on one value or ordered sequence despite failures under an explicit model. |
| Replicated state machine | Deterministic state machines applying the same committed command sequence. |
| Term/epoch | Monotonic leadership generation used to reject obsolete messages and authority. |
| Quorum | A set large enough to intersect another required set under one membership definition. |
| Election safety | At most one leader is elected in a term. |
| Log matching | Equal index/term entries imply equal commands and identical preceding prefixes. |
| Leader completeness | Every committed entry appears in every later leader's log. |
| State-machine safety | No two nodes apply different commands at the same log index. |
| Commit index | Highest log position known safe to apply under the algorithm's commit rule. |
| Hard state | Term, vote, and log information that must survive the modeled restart boundary. |
| Linearizable read | Read that can be placed between invocation and response in one real-time-respecting history. |
| Read barrier | Evidence that the serving leader is current and has applied the required committed prefix. |
| Client deduplication | Session/sequence tracking that makes repeated delivery return one logical result. |
| Ambiguous outcome | Client cannot tell whether an operation committed, requiring identity and read-back/retry rules. |
| Snapshot | Durable state-machine image plus last-included log index and term. |
| Log compaction | Removal of log prefix whose effects and metadata are safely represented by a snapshot. |
| Joint configuration | Transitional membership in which decisions satisfy overlapping old and new quorum requirements. |
| Lease | Time-bounded permission whose correctness depends on explicit clock, pause, and communication bounds. |
| Fencing token | Monotonic token checked by the protected resource to reject stale owners. |
| Byzantine fault | Arbitrary or malicious behavior; excluded from the module lab's crash/omission model. |
