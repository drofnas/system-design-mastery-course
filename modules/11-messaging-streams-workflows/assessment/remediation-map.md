# Module 11 Remediation Map

| Finding | Revisit | New evidence; never overwrite |
|---|---|---|
| Authority/event contract | Lesson 1, EX-01–EX-02 | dated authority/envelope addendum |
| Delivery or identity | Lesson 2, EX-03–EX-04 | new crash/ack and effect-key trace |
| Ordering/partition | Lesson 3, EX-05–EX-06 | skew/version/rebalance rerun |
| Outbox/inbox/CDC | Lesson 4, EX-07–EX-08 | new atomicity/restart evidence |
| Replay/poison/reconcile | Lesson 5, EX-09–EX-10 | isolated shadow rebuild and oracle |
| Workflow/compensation | Lesson 6, EX-11–EX-12 | new state/compensation history |
| Event time/watermark | Lesson 7, EX-13 | late-data correction rerun |
| Lag/backpressure | Lesson 7, EX-14–EX-15 | per-partition capacity rerun |
| Evidence integrity | Lessons 2–7, EX-15 | entirely new paired trials |
| RFC/defense | Lesson 8, EX-16 | dated RFC revision and defense follow-up |

If secrets or private data appear, contain and rotate them before creating new
evidence. A safety failure requires Repeat with new inputs; prose cannot repair
an invalid or mutable experiment.
