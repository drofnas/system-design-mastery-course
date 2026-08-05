# Module 2 Guided Exercises

Use Transit Signal only. Do not substitute the commerce capstone into these
questions. Preserve calculations, units, assumptions, and intermediate results.

## EX-01: Define useful work

At peak, Transit Signal receives 170 rider lookups/s. Two percent receive one
retry. Each lookup has three route legs.

1. Calculate logical lookups, server attempts, and branch attempts per second.
2. Define useful throughput.
3. State which value should be the denominator for user success.

## EX-02: Shape and sensitivity

Compare the five-minute 800/s burst with 800/s sustained for one hour. Calculate
logical requests in both periods. Then vary fan-out from 2 to 6 and identify the
capacity model input that changes.

## EX-03: Apply Little’s Law

At 170 admitted requests/s, mean in-system time is 80 ms and mean service time
is 25 ms.

1. Calculate in-system concurrency.
2. Calculate service concurrency.
3. With eight workers, calculate modeled worker utilization.
4. Explain why the result does not prove p99 safety.

## EX-04: Expose coordinated omission

Draw an event timeline for 50 open-loop arrivals/s during a two-second service
stall. Compare it with one closed-loop participant. List the timestamps that
must be retained to expose generator lag and queue waiting.

## EX-05: Design a valid trial

Write a trial contract for the Transit baseline: population, boundary, workload,
warm-up, duration, repetitions, outcomes, percentiles, rejection treatment,
clock, generator check, and raw-evidence location.

## EX-06: Calculate fan-out tail

A branch is slow with probability 0.01. Calculate the probability of at least
one slow branch for fan-out 1, 3, 10, and 20. Name two likely sources of branch
correlation.

## EX-07: Size a queue from a deadline

A service completes 300 requests/s and has 100 ms of user-deadline budget
available for waiting. Calculate the largest queue implied by `Q/μ`. Propose a
smaller bound and explain the margin.

## EX-08: Choose an overload policy

Compare:

1. queue every rider request,
2. reject new rider work when full while preserving authorized operator work,
3. serve a cheaper rider response.

Evaluate user outcome, invariant risk, recovery, fairness, security, and
operating complexity. State the experiment that would justify option 3.

## EX-09: Bound retry amplification

Three layers each permit one initial attempt and two retries.

1. Calculate worst-case lowest-layer attempts.
2. For 2,000 originals and a 5% shared budget, calculate permitted retries.
3. Define a metric that reveals whether retries recover useful work.

## EX-10: Calculate failover and recovery

Normal measured capacity is 320 requests/s. The declared failover retains 75%.
Peak load is 210/s. During recovery, 30,000 items are backlogged, 100 new
items/s arrive, and the system can process 160/s.

1. Does peak fit failover capacity?
2. What is the net drain rate?
3. How long does clearance take?
4. What shared-resource assumption could invalidate the result?

## EX-11: Build the sweep table

If measured capacity is 300 requests/s, calculate offered rates for 10%, 25%,
50%, 75%, 90%, 100%, 110%, 125%, and 150%. For each row, list the minimum
signals needed to distinguish stable service, waiting, rejection, and generator
failure.

## EX-12: Defend a capacity decision

Write:

1. a one-sentence safe operating region,
2. a scaling signal with threshold, window, action, lead time, and owner,
3. an overload policy,
4. one cost sensitivity,
5. one reversal condition, and
6. the strongest fair objection.

Deliver a five-minute practice defense without changing the workload or failure
model after a question is asked.

## PESD 2.0 extension to the final exercise

Extend the final guided exercise with per-tenant allocation, forecast variance, useful-outcome economics, shared-cost policy, and modeled energy/carbon sensitivity. Produce an
obligation/control/evidence row, a named owner, a bounded cost or capacity
effect, a failure or policy-drift test, a migration step, and a reversal trigger.
Label every observation with an accepted evidence mode and do not use fixture
replay as independent Build, Break, Implement, or Measure evidence.
