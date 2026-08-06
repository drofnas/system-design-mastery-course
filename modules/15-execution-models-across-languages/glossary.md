# Module 15 Glossary

| Term | Operational meaning |
|---|---|
| Allocation | Reserving storage for a value; record allocator, lifetime, and release mechanism. |
| Escape | A value outlives its creation scope, often changing stack/heap placement. |
| RAII | Resource acquisition is initialization: lexical lifetime drives deterministic release. |
| Ownership | Rules deciding who may use, mutate, transfer, and release a resource. |
| Borrow | Time-bounded access without taking ownership. |
| Reference counting | Release when a count reaches zero; cycles need a separate rule. |
| Tracing GC | Discover reachable objects from roots and reclaim the rest. |
| Event loop | Scheduler running callbacks on a small number of threads, often one for user code. |
| Worker pool | Finite workers for blocking or CPU-heavy operations. |
| Goroutine/task | Runtime-managed concurrent work; cheap creation does not make work free. |
| Virtual thread | JVM-managed thread scheduled onto carrier OS threads. |
| Structured concurrency | Child work is owned by a lexical/request scope and finishes or cancels with it. |
| Happens-before | Language-defined ordering that makes a write visible to a later read. |
| Data race | Conflicting concurrent accesses without required synchronization. |
| Structural typing | Compatibility based on member shape rather than declared identity. |
| Nominal typing | Compatibility based on declared names or relationships. |
| Runtime validation | Checking decoded values before granting typed meaning or authority. |
| Equivalent work | Same logical inputs, required effects, and success denominator across variants. |
| Useful throughput | Completed valid outcomes per unit time; attempts and rejected work are separate. |
| Cleanup grace | Bounded time after cancellation for owned work to stop and resources to close. |
| Evidence limit | What a measurement or tool cannot establish. |
