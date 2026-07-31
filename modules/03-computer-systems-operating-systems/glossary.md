# Module 3 Glossary

| Term | Operational meaning |
|---|---|
| benchmark contract | Fixed work, environment, method, output, and claim boundary for a measurement |
| cache line | Coherence and transfer unit whose exact size is machine-specific |
| locality | Reuse close in time or address, increasing the chance data is already near the processor |
| branch misprediction | Speculated control flow that must be discarded and restarted |
| syscall | Controlled transition requesting a kernel service; its cost includes the requested work |
| runnable | Eligible for CPU time but not necessarily executing |
| context switch | Scheduler change in the executing task or thread context |
| virtual memory | Address-space indirection providing translation, protection, sharing, and demand allocation |
| minor fault | Fault resolved without storage I/O, often by mapping an existing or newly allocated page |
| major fault | Fault whose resolution requires I/O according to the reporting interface |
| RSS | Resident-set estimate; definition and accounting vary by operating system and tool |
| contention | Delay caused by multiple actors requiring the same finite resource or serialization point |
| deadlock | Cyclic waiting in which no participant can make progress without outside action |
| false sharing | Coherence traffic caused by independent writes to data sharing a coherence unit |
| page cache | Kernel-managed cache of file-backed data in memory |
| writeback | Deferred transfer of dirty cached data toward storage |
| durable write | Data preserved across the explicitly declared fault boundary, not merely accepted by `write` |
| device queue | Outstanding operations waiting at an OS, driver, controller, or device layer |
| CPU quota | Time allowance enforced over a period; exhaustion normally produces throttling, not a slower CPU |
| reclaim | Work performed to make memory available by evicting or writing back pages |
| OOM | Out-of-memory condition whose selection and containment depend on the host and cgroup policy |
| production transfer | Argument that a lab mechanism applies to a specified production workload and environment |
