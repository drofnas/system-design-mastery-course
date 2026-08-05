# G02 Assessment Brief

This is the learner-facing prompt set for the standalone Week 33 gate over
M04, M05, M06. The exact time boxes and hard floors in [gate.json](gate.json)
control. The 30-minute freeze and final scoring/closure block are managed from
the [gate overview](README.md); this brief contains the four scored parts.

Freeze each part before feedback. The practical uses Beacon Dispatch and a new
seed/configuration; it is not a commerce solution. Submit exact headings and
commits through the Module 6 evaluator.

Use the [sealed-local gate workflow](../../SOLO_GATE_GUIDE.md). Human review
is optional and stronger portfolio evidence, but it is not required.

## Part 1: Written examination — 75 minutes

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

## Part 4: Portfolio and revision review — 45 minutes

Index Modules 4–6 evidence by file heading and commit, then validate the index
through the frozen self-evaluation workflow. Show frozen predictions,
builds/tests, failure investigations, decisions/revisions, and learning logs.
After gate scoring, complete `capstone/revisions/week-034-delta.md` without editing earlier evidence.
An optional independent evaluator may later review the identical bundle.

## Result

Pass only when all structural gates, scored parts, three module-domain
subscores, safety-critical rows, and the overall average meet their published
floors. Revise applies only when evidence and chronology are complete and a
non-safety floor is missed. Repeat applies when an invariant fails, chronology
is invalid, evidence is fabricated or mismatched, or the causal model is
materially incorrect. A Pass creates no required remediation artifact.
