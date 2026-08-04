lesson_id: L06

# Memory, Third Parties, and Observability

## Outcomes

- Distinguish retained browser resources from ordinary allocation and collection.
- Govern third-party code as a performance, privacy, security, and ownership dependency.
- Propagate useful trace context without turning telemetry into authority or sensitive storage.

## Prerequisites

Use Module 3 memory, Module 4 observability cost, Module 13 supply-chain/privacy,
Module 14 dependency exits, and Module 15 lifetime/resource ownership.

## Mechanism: browser state needs owners and release conditions

Heap size can rise during useful work and fall after collection. A leak claim
requires a repeated lifecycle in which objects or resources that should be dead
remain reachable or active. DOM nodes, listeners, timers, observers, network
requests, workers, sockets, and caches each need an owner and release event.

Use a **lifetime trial**:

1. Define the repeated action and the state expected to survive it.
2. Warm up, collect a baseline, repeat N times, request collection only when the
   tool supports it, and record heap plus non-heap resource counts.
3. Compare equal checkpoints, inspect retainers, and name the ownership edge.
4. Repair one release condition; rerun with the same inputs and navigation count.
5. Bound the claim to browser/tool/version; memory thresholds are environment-specific.

Third-party admission uses a dependency ledger:

| Question | Required evidence |
|---|---|
| User value | named journey/outcome and removal cost |
| Critical path | bytes, requests, main-thread time, failure coupling |
| Authority | data/API access, CSP/iframe/sandbox boundary |
| Change | version/provenance, owner, review and emergency disable |
| Exit | fallback, replacement, removal test, contractual lead time |

For observability, create a server trace at authority and propagate W3C trace
context across the edge. The browser may continue parentage, but client sampling
flags and arbitrary attributes are untrusted. Never attach raw session tokens,
email, full URLs with sensitive queries, or user-entered text. Use bounded route
templates and pseudonymous test identities.

## Worked example

Northstar's live route creates an interval, a visibility listener, and a fetch
abort controller. The broken navigation unmounts the DOM but leaves the interval
and listener active. After 30 visits, active timers and listeners grow from one
each to 31 even after collection. A retainer path points to the route closure.
The repair assigns them to one route owner, aborts fetch, clears the interval,
and removes the listener on unmount; repeated counts return to baseline.

A third-party sky-map script is optional. The broken blocking script delays the
event heading and its failure prevents the route module from starting. The repair
loads it after useful content, isolates it behind an adapter and timeout, exposes
a text/table alternative, restricts network authority, and records an owner and
kill switch. The route remains usable when the script is blocked.

Trace spans use route template `/events/:id`, event operation, cache outcome,
render mode, and content version. They exclude event-title search text and staff
identity. The edge creates its own span and does not accept client “sampled” as
authorization or priority.

## Common expert mistakes

- **Calling high heap a leak.** Caches and live state may be intentional; show a
  failed lifecycle and retainer.
- **Measuring only JavaScript heap.** Listeners, DOM, workers, GPU resources, and
  network handles can outlive it.
- **Loading third parties asynchronously and declaring success.** Async code can
  still consume main-thread time, read first-party state, or fail the journey.
- **Putting sensitive identifiers in trace attributes.** High-cardinality private
  telemetry creates security, privacy, retention, and cost problems.
- **Trusting browser trace flags.** Trace context is correlation, not authority.

## Guided practice

Design a 30-navigation lifetime test and a blocked/slow third-party pair. Then
write allowed and prohibited browser, edge, and origin trace attributes with
owners, cardinality budgets, retention, and redaction checks.

## Self-check

1. What evidence distinguishes a leak from delayed collection?
2. Why is `async` not a third-party governance policy?
3. Which component should create authoritative server telemetry?
4. Why use route templates in traces?

## Explained answers

1. Equal lifecycle checkpoints show objects/resources that should be dead remain
   reachable or active, with a retainer/owner and growth across repetitions.
2. It changes loading order but not code authority, CPU cost, privacy, failure,
   provenance, ownership, or exit.
3. The trusted edge/origin under server control; browser context may correlate but
   is validated and bounded at the trust boundary.
4. They preserve useful grouping while avoiding sensitive values and unbounded cardinality.

## Sources and next work

Study RES-08, RES-09, RES-12, and RES-13. Complete EX-13–EX-17 before running
F03, F04, and the trace-context conformance tests.
