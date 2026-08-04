lesson_id: L02

# Schedulers, Event Loops, and Tasks

## Outcomes

Trace runnable, blocked, queued, and executing work from request to runtime task
to OS thread; choose a bound for each finite scheduler.

## Prerequisites

Modules 2, 3, and 6. Read RES-01, RES-04, and RES-07 within their boundaries.

## Mechanism and method

Concurrency describes overlapping lifetimes; parallelism describes simultaneous
execution. A runtime maps tasks onto finite processors and often onto finite
worker pools. Cheap task creation changes overhead, not CPU, memory, dependency,
or downstream capacity.

Use **PLACE**: identify the producer; locate the queue; assign the scheduler;
classify work as CPU, blocking, or asynchronous wait; expose the bound and
overload result. Repeat for request callbacks, DNS/file/crypto pools, goroutines,
async executors, virtual threads, and external dependencies.

Node executes JavaScript callbacks on the event loop and sends selected native
operations to a worker pool. A long callback delays unrelated callbacks. Go
schedules goroutines onto OS threads and may create many runnable goroutines;
fairness and preemption do not create capacity. Tokio polls ready futures; a
future that blocks its executor thread harms peers. Java virtual threads unmount
for supported blocking operations but still consume memory, connections, and
downstream slots. Platform-thread pools fail differently but are finite too.

## Worked example

Northstar receives 100 observation requests. Each needs four 30 ms dependency
waits and 8 ms of CPU validation. The broken Node variant performs validation
as one 32 ms callback after the children return. A heartbeat scheduled every
10 ms shows a 32 ms-plus delay even though dependency waits were asynchronous.
The repaired variant partitions validation into bounded worker work, while a
global admission semaphore limits total child work. The repair records both
event-loop delay and worker-queue depth so displaced waiting stays visible.

The Go implementation uses one goroutine per admitted child, not one per
offered child. The Java implementation uses virtual threads but the same
semaphore. The Rust implementation owns spawned tasks in a request scope.

## Common expert mistakes

- Calling all Node work single-threaded or all Go/Rust/Java work parallel.
- Measuring CPU utilization without runnable queue, throttling, and per-core use.
- Replacing a small thread pool with unbounded tasks and moving failure to
  memory, connections, or a dependency.
- Assuming async syntax proves non-blocking behavior.

## Guided practice

Classify JSON decode, HTTP wait, DNS, 20 ms hashing, log write, and response
assembly for each runtime. For every queue name its capacity, owner, wait
metric, admission rule, and explicit overload outcome.

## Self-check

1. Why can 20% total CPU coexist with scheduler starvation?
2. What does a virtual thread remove, and what does it not remove?
3. When is one-task-per-child unsafe even if tasks are cheap?

## Explained answers

1. One core or executor thread may be saturated while the host has idle cores;
   throttling or a blocked scheduler can also hide behind aggregate CPU.
2. It reduces the cost and coupling of one Java task to one OS thread. It does
   not add CPU, memory, connections, downstream capacity, deadlines, or bounds.
3. When offered children are unbounded or cancellation/cleanup does not own
   their lifetime, task count and external work can grow beyond the budget.

## Sources and next work

Use RES-01, RES-04, and RES-07. Continue to [Lesson 3](03-bounded-fanout-structured-cleanup.md).
