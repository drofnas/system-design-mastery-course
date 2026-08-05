# Gate 2 Assessment: Performance, Networks, and Remote Calls

> **PESD V1 historical contract:** Preserve this file for V1 learners and immutable evidence. PESD 2.0 uses [gates/G02/README.md](../../../gates/G02/README.md).

Freeze each part before feedback. The practical uses Beacon Dispatch and a new
seed/configuration; it is not a commerce solution. Submit exact headings and
commits through the Module 6 evaluator.

Use the [sealed-local gate workflow](../../../SOLO_GATE_GUIDE.md). Human review
is optional and stronger portfolio evidence, but it is not required.

## Part 1: Written examination — 90 minutes

Answer from mechanisms, arithmetic, and stated failure models.

1. A 700 ms journey spends 90 ms before parallel fan-out and reserves 110 ms
   for assembly/delivery. Children A/B are required; C is optional. Derive one
   valid allocation and explain why parallel time and resource cost aggregate
   differently. At 260 ms after ingress, calculate remaining time before reserve.
2. Three layers each permit an original plus two retries. Calculate the attempt
   bound and design a caller-owned policy for an overloaded, idempotent read.
   Explain why jitter alone is insufficient.
3. A command commits remotely but its response is lost. Explain why the result
   is ambiguous and specify key scope, fingerprint, atomicity, replay, conflict,
   retention, authorization, and evidence needed for safe retry.
4. Compare a deadline, concurrency limit, retry budget, circuit breaker, hedge,
   and rate limit. State the failure each controls and one failure each can move
   or amplify.
5. Diagnose a service where logical demand is flat, tail latency and attempts
   rise, health checks fail, instances restart, and destination load increases.
   Give two causal hypotheses and the smallest discriminating experiments.

## Part 2: Hidden-fault practical — 150 minutes

Run `scripts/solo_gate.py prepare --gate G02`, freeze and commit the challenge,
prediction, and diagnostic plan, then use `reveal` and `check`. Collect raw
trial/runtime evidence, identify observation versus cause, rank two alternatives,
apply one repair, and rerun identical useful work. Include evidence-kind and all
relevant deadline, attempt, pool, effect, completeness, and cleanup data.

## Part 3: Architecture defense — 60 minutes

Defend the independent commerce remote-call policy against the frozen solo-review
questions for dependency, security, finance, and on-call roles. An optional
human panel may ask adaptive follow-ups. Derive
one deadline, retry, idempotency, and overload decision. Record challenges,
dissent, changed claims, follow-ups, owners, and reversal evidence.

## Part 4: Portfolio and revision review — 60 minutes

Index Modules 4–6 evidence by file heading and commit, then validate the index
through the frozen self-evaluation workflow. Show frozen predictions,
builds/tests, failure investigations, decisions/revisions, and learning logs.
Complete `capstone/revisions/week-24-gate-02.md` without editing earlier evidence.
An optional independent evaluator may later review the identical bundle.

## Scoring

The evaluator applies R01–R10 and G01–G06. Pass requires all four parts, all
structural gates, average ≥3.0, and no safety-critical zero. Revise creates dated
addenda. Repeat creates a new baseline/trials only when evidence ordering or a
safety invariant failed.
