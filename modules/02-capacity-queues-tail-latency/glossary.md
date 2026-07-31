# Module 2 Glossary

## Work and demand

- **Arrival rate (λ):** attempted logical work entering a chosen boundary per
  unit time. State whether rejected arrivals count.
- **Service demand:** resource time consumed per completed unit of work at a
  named resource.
- **Throughput:** completed attempts per unit time.
- **Useful throughput:** distinct user or business operations completed per
  unit time. Retries and duplicate attempts do not add useful throughput.
- **Open workload:** arrivals occur independently of prior completions.
- **Closed workload:** a fixed population issues new work only after earlier
  work completes.

## Queue behavior

- **Concurrency (L):** average work present in a boundary, including service and
  any queue included in that boundary.
- **Response time (W):** average time spent inside the same boundary used for L.
- **Little’s Law:** under a stable long-run boundary, `L = λW`.
- **Utilization (ρ):** fraction of a finite resource’s service capacity that is
  busy. It is not a direct promise about latency.
- **Saturation:** a resource has no remaining service capacity for incremental
  work; queues, rejection, or lost throughput reveal the consequence.
- **Stable queue:** over the observation window, arrivals and completions
  balance and queue depth has no persistent positive trend.
- **Admission control:** decide whether work may enter before consuming the
  scarce resource.
- **Load shedding:** intentionally reject or degrade work to protect more
  valuable work and system recovery.

## Latency

- **Percentile:** value at or below which a stated fraction of observations
  falls. A p99 is about a distribution and population, not one request.
- **Tail latency:** the slow end of a latency distribution.
- **Coordinated omission:** a generator stops offering independent arrivals
  while the system is slow, omitting observations users would have experienced.
- **Generator lag:** difference between a request’s intended send time and its
  actual send time. Large lag means the generator may be the bottleneck.
- **Fan-out:** one logical operation creates multiple parallel branches.
- **Tail amplification:** the probability that at least one branch is slow
  rises as fan-out increases.

## Protection and planning

- **Retry budget:** shared limit on retry attempts relative to original work.
- **Failover headroom:** capacity intentionally unused in normal operation so a
  defined capacity loss can be absorbed.
- **Safe operating region:** measured range in which the chosen workload meets
  latency, useful-throughput, queue, error, downstream, failover, and cost
  constraints.
- **Scaling signal:** measurement with a threshold, window, and owner that
  triggers a capacity action early enough to be effective.
- **Cost per useful request:** allocated hourly cost divided by distinct
  successful requests per hour.
