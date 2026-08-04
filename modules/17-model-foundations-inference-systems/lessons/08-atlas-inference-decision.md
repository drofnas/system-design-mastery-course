lesson_id: L08

# Atlas Tutorial, Architecture Decision, and Teach-Back

## Outcomes

- Execute the full Atlas learning loop without leaking a capstone answer.
- Compare provider and deployment alternatives using shared drivers.
- Defend ownership, cost, migration, rollback, and reversal conditions.

## Prerequisites

Complete Lessons 1–7, EX-01–EX-17, and freeze A01.

## Mechanism: evidence closes the decision loop

Use this decision procedure:

1. Restate user outcome, workload distribution, quality threshold, privacy
   boundary, deadlines, failure model, and cost denominator.
2. Reconcile mathematical predictions with measured CPU and modeled serving evidence.
3. Compare managed provider, one bounded deployment, and separated traffic-class
   deployments against the same drivers.
4. Preserve F01–F06 raw trials and explain both predicted and surprising results.
5. Assign owners for identity, model quality, serving, security, cost, and incidents.
6. Design shadow, canary, stop, rollback, and decommission steps.
7. Record dissent and the evidence that would reverse the decision.
8. Teach the causal chain without relying on an architecture label or AI answer.

## Worked example

Start with Atlas's 18 interactive and 45 batch arrivals per second. Calculate
resource bounds, implement the tiny model, and run the portable scenarios. The
evidence shows request-count admission and FIFO batching fail under length skew.
The selected design is one bounded deployment with token/memory admission,
traffic classes, chunked prefill, versioned tenant caches, a precision gate, and
deadline-aware compatible failover.

The team rejects an immediate split deployment because the shared design meets
the controlled workload and has fewer owners and rollouts. It records a reversal:
split when four weeks of production evidence require reserving more than 70% of
capacity away from one class to protect the other. Migration shadows decisions,
canaries one museum, expands by cohort, and can drain back to the prior version.

## Common expert mistakes

- Comparing candidates with different workloads or quality bars.
- Treating a vendor benchmark as local capacity evidence.
- Naming a rollback without preserving schema, cache, and in-flight compatibility.
- Assigning “the platform team” instead of one owner per operational decision.
- Performing a polished presentation that cannot answer causal follow-ups.

## Guided practice

Complete EX-17 and EX-18. Conduct a 20-minute defense using the frozen
solo-review packet, answering once from the managed-service alternative and once
from the split-deployment alternative. Record the strongest dissent, response,
unresolved risk, owner, and due date. Live reviewers are optional.

## Self-check

1. What evidence connects Atlas's user outcome to its scheduler choice?
2. Why is the simple alternative still in the RFC?
3. What makes rollback executable?
4. What distinguishes teach-back from a design presentation?

## Explained answers

1. Per-class arrivals and lengths, queue-inclusive TTFT/ITL, token/memory bounds,
   rejection, quality, and cost under same-work failures.
2. It establishes the complexity delta and shows why evidence, not preference,
   justifies added controls.
3. Compatible versions and state, stop thresholds, traffic/drain steps, owners,
   verification, and a tested route to the prior system.
4. The learner derives the mechanism, handles counterexamples and follow-ups,
   states limits, and enables another engineer to apply the method.

## Sources and next work

Study RES-09 and revisit all bounded sources as needed. Submit A07–A11, evaluate
with the published rubric, and create remediation only as a separate artifact.
