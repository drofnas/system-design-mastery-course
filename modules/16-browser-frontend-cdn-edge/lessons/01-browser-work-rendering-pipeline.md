lesson_id: L01

# Browser Work and the Rendering Pipeline

## Outcomes

- Trace a user interaction through task selection, event callbacks, microtasks,
  style, layout, paint, raster, compositing, and presentation.
- Locate the queue or thread that can delay the next visible response.
- Diagnose a long task without assuming that every frame uses every rendering stage.

## Prerequisites

Use Module 3 scheduling and memory, Module 4 profiling, Module 5 critical paths,
and Module 15 event-loop and lifetime reasoning.

## Mechanism: an interaction competes for a rendering opportunity

The browser does not run “JavaScript, then render” as two indivisible steps. A
window agent selects tasks from task sources. After a task callback finishes,
the browser performs a microtask checkpoint. The user agent may then update
rendering. Rendering itself can require style calculation, layout, pre-paint,
paint, raster, and compositing; some changes can reuse prior work or run mostly
on the compositor path.

Use an **interaction ledger**:

| Segment | Start/stop evidence | Work owner | Queue/thread | Can delay feedback? |
|---|---|---|---|---|
| Input delay | input timestamp → callback start | preceding tasks | main thread | Yes |
| Processing | callback start → callback end | event handlers | main thread | Yes |
| Microtasks | callback end → checkpoint drained | promise reactions | main thread | Yes |
| Presentation | processing end → next paint | style/layout/paint/composite | several stages | Yes |

Procedure:

1. Name the interaction and the first visible response that proves progress.
2. Record the task and every microtask it creates; do not stop at `async` labels.
3. Record DOM/style reads and writes and whether they force layout dependencies.
4. Attribute rendering stages from a trace instead of assuming a full pipeline.
5. Find the longest segment, state two alternative causes, and run a change that
   affects only one cause.
6. Verify the repaired path still produces the same useful result.

Yielding can create a rendering opportunity, but a timer with delay zero is not
a frame guarantee. Moving work to a worker helps only when serialization,
transfer, response ordering, cancellation, and worker admission are bounded.

## Worked example

Northstar's `/sky-events` page filters 4,000 local event summaries. The broken
handler parses a large third-party payload, filters, sorts, updates 600 DOM
nodes, then resolves a promise whose microtask computes badges. A trace shows
18 ms input delay, 174 ms handler work, 31 ms microtasks, and 46 ms presentation.
The 269 ms observation is a controlled interaction, not a field INP percentile.

The team first blames layout. Disabling the badge microtask removes 30 ms but
does not repair the journey. A second experiment precomputes the search index,
renders only the visible result window, updates the count immediately, and
yields non-visible enrichment. The useful result and filter semantics remain
unchanged; the visible response occurs in 82 ms under the same profile.

The causal claim is scoped: under this fixture, most repair came from reducing
main-thread JavaScript and DOM work. It does not prove that layout is cheap on
other routes or that 82 ms is a population percentile.

## Common expert mistakes

- **Calling every callback a macrotask.** The platform contract uses tasks and
  task sources; imprecise labels hide ordering assumptions.
- **Treating promises as free concurrency.** Promise continuations are
  microtasks and can starve a rendering opportunity.
- **Reading a flame chart as causation.** A long stack is evidence of time spent,
  not proof that changing it preserves the journey.
- **Forcing layout in a measurement loop.** Alternating geometry reads and DOM
  writes can create the cost the investigation claims to observe.
- **Optimizing average frame time.** One blocked critical interaction can be
  hidden by thousands of idle or inexpensive frames.

## Guided practice

Trace Northstar's “show accessible viewing details” interaction. Include the
input task, promise used to fetch the detail, DOM update, focus move, and next
paint. Add a 220 ms synchronous calculation before the focus move. Predict the
observable failure and design one-control broken/repaired trials.

## Self-check

1. Why can a resolved promise still delay visual feedback?
2. When can a change avoid layout and paint?
3. What makes worker offload an incomplete repair?
4. Why is one Playwright interaction not INP?

## Explained answers

1. Its continuation runs as a microtask before the event loop can reach a
   rendering opportunity; a self-feeding microtask chain can keep delaying paint.
2. A compositor-supported change whose required properties and pixels are
   already available may reuse work, but the trace must confirm the path.
3. Transfer cost, queue bounds, cancellation, stale results, and ownership still
   determine whether the user journey and capacity are safe.
4. INP is derived from eligible interactions over page visits and reported at a
   field population percentile; the lab is one controlled observation.

## Sources and next work

Study RES-01, RES-02, and RES-10 within their boundaries. Complete EX-01 and
EX-02, then freeze the F01 prediction before running the lab.
