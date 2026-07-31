# Calibration Fixture: Repeat

## Artifact and freeze record

No committed pre-experiment prediction is supplied. The capacity report says
the prediction was reconstructed after testing. Raw JSONL, scenario files, and
the nine-point sweep are absent. Only two screenshots of a dashboard exist.

## Workload and uncertainty

The submission says Transit Signal has “millions of users” and uses requests per
day. It does not define one logical lookup, attempts, branch work, burst
duration, skew, projection, recovery work, or evidence sources.

## Capacity prediction

The report states that eight workers each handle 100 requests/s, so safe
capacity is 800/s. No service demand is measured or calculated. It calls 80%
utilization universally safe and uses attempted request rate as useful
throughput.

## Implementation and measurement

The service launches a new task for every request. The queue and downstream
calls have no bound. Clients retry until success with exponential backoff but
no attempt count, shared budget, deadline, or stable identity. There are no
automated tests.

The benchmark uses one closed-loop client. It omits rejected and timed-out
requests, reports only average latency, and retains no timestamps, counts,
configuration, host, seed, or raw events.

## Tail and saturation findings

The report multiplies branch p99 by three and calls the result journey p99. It
has no branch distribution, fan-out probability, correlation discussion, or
load sweep. The screenshots are described as proof that no saturation occurred.

## Overload and retry policy

The stated overload policy is “queue until traffic falls and retry failed
requests.” Operator and rider work share the same unbounded execution path.
Anyone can set an `operator=true` field to receive priority. No recovery or
missing-configuration behavior exists.

## Failover cost and ownership

Normal capacity is presented as failover capacity. The report divides cost by
attempts, so aggressive retries reduce the displayed unit cost. No backlog,
scaling lead time, owner, sensitivity, rollout, or rollback evidence exists.

## Decision defense and revision

The recommendation is to scale at 80% CPU. During questions, the learner changes
the burst from 800/s to 80/s and says retries are disabled, contradicting the
submitted implementation. No separate evaluation or revision artifact exists.
