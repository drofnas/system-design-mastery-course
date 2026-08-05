---
lesson_id: L07
title: "Failover Headroom and Unit Cost"
---

# Failover Headroom and Unit Cost

## Outcomes

You can calculate degraded-state capacity, backlog clearance, and cost per
useful request, then run sensitivity without declaring a universal utilization
target.

## Prerequisites

Lessons 1–6; cost boundaries from Module 1.

## Mechanism

Normal-state success does not prove failover safety. For a declared retained
capacity fraction `f`:

```text
failover nominal capacity = normal nominal capacity × f
```

If normal admitted load exceeds that value, failover requires pre-scaling,
shedding, degradation, traffic transfer, or an accepted SLO violation. State
which action is available and its lead time.

Backlog recovery needs net drain rate:

```text
net drain rate = recovery completion rate - new arrival rate
clearance time = backlog size / net drain rate
```

When net drain rate is zero or negative, the backlog never clears. Recovery
capacity is separate from interactive capacity if both compete for a common
resource.

Cost must use useful work:

```text
cost/useful request =
  allocated hourly compute + fixed hourly cost + relevant operator cost
  --------------------------------------------------------------------
               unique successful requests per hour
```

Retries can increase spending while reducing useful throughput, so cost per
attempt can improve during a failure while cost per user outcome worsens.

There is no universal safe utilization. Variance, SLOs, scaling lead time,
failure size, workload correlation, queue policy, and cost all shape the safe
region. Sensitivity should vary the inputs that can reverse the decision.

### Repeatable technique

1. State the exact capacity loss and correlation.
2. Recalculate each resource under the loss.
3. Add concurrent recovery and background demand.
4. Calculate backlog clearance.
5. Allocate cost consistently to useful work.
6. Evaluate low/base/high load, service time, failure fraction, and price.
7. Choose a safe region from measured constraints.
8. Attach an owner and provisioning lead time to the scaling signal.

## Worked example

Transit’s modeled normal worker capacity is 315.63 requests/s. Retaining 75%
gives:

```text
315.63 × 0.75 = 236.72 requests/s
```

The 170/s peak fits the model; the 800/s burst does not. The overload policy is
therefore required even if normal-state tests pass.

Suppose 90,000 notification items accumulated. Workers can recover at 700/s
while 500/s new items arrive:

```text
net drain = 200/s
clearance = 90,000 / 200 = 450 s = 7.5 minutes
```

If the recovery target is 30 minutes, this model has margin, but only if
recovery does not steal connections from rider reads or approvals.

The reference scenario costs $0.76/hour in its artificial model. At 30 useful
requests/s:

```text
$0.76 / (30 × 3,600) ≈ $0.00000704/useful request
```

This is a teaching input, not a cloud quote.

## Common expert mistakes

- **Reserve capacity only at the first tier:** a shared downstream still fails.
- **Ignore recovery arrivals:** backlog clearance is overstated.
- **Divide by attempts:** duplicate work makes cost appear better.
- **Use average price only:** failover or burst pricing may change the boundary.
- **Scale on a late signal:** provisioning starts after users are already
  outside the safe region.

## Guided practice

A service normally completes 1,000 useful requests/s. Losing one of four equal
capacity groups leaves 75%. New load is 650/s and a backlog of 180,000 requests
must clear in 15 minutes. Calculate the minimum recovery completion rate and
decide whether retained capacity is sufficient.

## Self-check

1. Why is failover fraction not always proportional to host count?
2. What happens when net drain rate is negative?
3. Why include provisioning lead time in a scaling decision?
4. Which denominator belongs in cost per user outcome?

## Explained answers

1. Capacity may be uneven or constrained by a shared dependency, state, quota,
   or correlated failure.
2. Backlog grows; a clearance-time claim is false until arrivals fall or supply
   increases.
3. A signal is useless if action completes after the workload has crossed the
   unsafe region.
4. Distinct successful logical operations over the same allocation window.

For the practice, clearing 180,000 in 900 seconds requires 200/s net drain, so
total completion must be 850/s. Retained capacity is 750/s and is insufficient
without shedding new work or adding recovery supply.

## Sources and next work

- David Yanacek, [Avoiding Insurmountable Queue Backlogs](https://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/)
- Julius Plenz, [How to Trade off Server Utilization and Tail Latency](https://www.usenix.org/conference/srecon19asia/presentation/plenz)

Complete EX-10 and EX-11 during the sensitivity sweep.
