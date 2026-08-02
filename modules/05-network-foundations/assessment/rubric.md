# Module 5 Anchored Rubric

## R01: Client path and quantitative budget

- **0:** no bounded journey or materially false arithmetic.
- **1:** layer names without client, workload, units, or critical path.
- **2:** plausible path and estimates with missing overlap, bytes, percentile, or uncertainty.
- **3:** frozen client/path model quantifies serial exchanges, bytes, BDP, serialization, useful work, percentile, and transfer limits.
- **4:** sensitivity and correlated journey evidence teach another team when the model transfers.

## R02: DNS, addressing, routing, and discovery

- **0:** DNS success is treated as service health or temporary failure as nonexistence.
- **1:** lookup output without actors, response class, or cache boundary.
- **2:** actors exist but TTL, authority, fallback, privacy, or ownership is incomplete.
- **3:** resolution, cache, address, route, discovery, failure classes, privacy, fallback, and owners are causally separated.
- **4:** expiry/failure experiments expose resolver amplification and safe operation across client classes.

## R03: TCP, flow, congestion, and goodput

- **0:** claims contradict ordered-byte-stream or equivalent-work evidence.
- **1:** throughput changes are labeled without mechanism.
- **2:** bytes and timing exist but receiver, loss, setup, or observation boundary is weak.
- **3:** ordering, recovery, flow, congestion, setup, useful/wire bytes, and goodput support bounded diagnosis.
- **4:** discriminating reruns separate receiver, path, and application limits with quantified uncertainty.

## R04: TLS identity and setup

- **0:** verification is disabled, secrets leak, or peer identity is materially false.
- **1:** encrypted connection exists without trust/hostname evidence.
- **2:** success is shown but a rejection, termination boundary, resumption limit, or owner is missing.
- **3:** trusted-name success and unsafe-name/anchor rejection preserve certificate, key, termination, authorization, and cleanup boundaries.
- **4:** rotation, resumption, expiry, fallback, and cross-team ownership are adversarially tested.

## R05: Proxies, pools, NAT, and slow readers

- **0:** unbounded connection growth or unsafe overload policy.
- **1:** a connection count appears without hop or owner.
- **2:** pool/reuse evidence exists but wait, hold, rejection, cleanup, NAT, cost, or ownership is incomplete.
- **3:** each hop has capacity, lifecycle, security, wait/reject, cleanup, cost, and owner evidence; slow readers and dependencies are separated.
- **4:** burst, drain, rotation, and failover experiments prove bounded behavior across topology changes.

## R06: Blind diagnosis and evidence integrity

Safety-critical because scenario inspection, altered evidence, or contradictory
arithmetic invalidates diagnostic judgment.

- **0:** reveal precedes diagnosis, raw bundles changed, or false causal reasoning drives the decision.
- **1:** fault names restate symptoms without citations or alternatives.
- **2:** most faults are diagnosed but hashes, confidence, alternatives, or reruns are incomplete.
- **3:** all nine frozen diagnoses cite preserved evidence, separate observation/cause, rank alternatives, and define same-work reruns before reveal.
- **4:** reruns falsify strong alternatives and explain why initially plausible diagnoses failed.

## R07: Trust boundary, data safety, and bounded execution

Safety-critical because leaked keys/data, disabled verification, public binding,
or unbounded resources can harm users and invalidate evidence.

- **0:** secret/sensitive data leaks, TLS verification is bypassed, public endpoints are touched, or limits/cleanup fail.
- **1:** safety is asserted without binding, certificate, redaction, or cleanup evidence.
- **2:** safeguards exist with one material trust, privacy, resource, or evidence-kind gap.
- **3:** loopback binding, ephemeral keys, hostname trust, rejection, redaction, limits, hashes, cleanup, and measured/model labels agree.
- **4:** adversarial trust, corruption, exhaustion, and cleanup tests independently reproduce the safety contract.

## R08: HTTP protocol comparison

- **0:** protocol slogan or mismatched work substitutes for evidence.
- **1:** feature checklist without ordering or deployment model.
- **2:** stream comparison exists but setup, shared congestion, fallback, reachability, or model limits are weak.
- **3:** HTTP/1.1, H2/TCP, and H3/QUIC are compared under shared drivers with ordering, setup, isolation, capacity, fallback, and evidence boundaries.
- **4:** client/path segments and controlled trials quantify where each alternative wins and reverses.

## R09: Protocol/topology decision and migration

- **0:** unsafe cutover, no fallback, or no user outcome.
- **1:** preference without shared drivers or owner.
- **2:** alternatives exist but security, cost, operations, compatibility, rollback, or reversal is incomplete.
- **3:** decision follows bounded evidence and includes clients, security, cost, capacity, owners, staged migration, fallback, rollback, decommission, and reversal.
- **4:** cross-team disagreement is resolved through quantified gates and rehearsed rollback under failure.

## R10: Communication and teach-back

- **0:** no defense or causal explanation.
- **1:** protocol vocabulary is recited without mechanism.
- **2:** understandable summary with weak counterexample, uncertainty, or follow-up ownership.
- **3:** teach-back derives ordering, trust, and failure behavior; handles challenge; records dissent, changed claims, and owners.
- **4:** another engineer can apply the method to a different stack and identify where evidence stops transferring.

## Result thresholds

- **Pass:** every gate passes, average at least 3.0, and R06/R07 are nonzero.
- **Revise:** no hard-gate or safety-critical failure, but average is below 3.0 or remediable gaps remain.
- **Repeat:** G02–G05 fails or R06/R07 is zero.
