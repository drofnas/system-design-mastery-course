# Transit Signal Calibration Submission: Remediable

## Submission identity

- Artifact commit: `8b7c6d5-revise`
- Frozen baseline: `transit-m04-baseline-revise`
- Python version and scenario are named; host background load is not recorded.
- AI assistance is disclosed for profile interpretation.

## Frozen question and baseline

The question names Transit rider p95 at 30 requests/second and compares it with
one preserved baseline. Useful successes and response checksum are recorded.
There are three baseline samples, but process restarts and smallest meaningful
effect are not justified.

## Hypotheses and controls

CPU, database, and lock causes are listed with predicted signals. Only CPU has a
clear falsifier. Candidate order is all baseline then all candidate. Scenario and
checksum match, but warmup and host-load differences remain uncertain.

## Instrumentation and correlation

Valid context crosses the client/server boundary and logs carry trace IDs.
Missing context starts a new root. Invalid all-zero and uppercase inputs are not
tested. Branch parentage is shown, but no metric exemplar is submitted and clock
semantics are described only as timestamps.

## Signal and cost contract

Journey latency, queue depth, CPU, connections, and error metrics have units.
The normal dimensions are bounded. The high-cardinality fixture counts distinct
request labels but provides no encoded-byte estimate or retention owner. Payloads
are excluded, while access and deletion rules remain proposed rather than tested.

## Profiles and dependency evidence

CPU and allocation profiles identify plausible sites. Profile-on overhead is not
compared with profile-off. SQLite indexed/scan plans and equal result checksums
are preserved, but cache state and row selectivity are not recorded. Lock wait is
measured; local file timing has one sample.

## Blind diagnosis matrix and reveal record

All six diagnoses and the reveal commit are separate. O01, O04, O05, and O06 cite
specific raw files and credible alternatives. O02 calls high allocated bytes a
leak without retained-object evidence. O03 cites wait but proposes no rerun that
separates lock delay from slow work inside the critical section.

## Evidence integrity and cleanup

Raw bundles, schemas, metadata, and hashes are present and unchanged. Summary
counts match detailed files. Connection cleanup returns to zero and temp files
are removed. One allocation profile lacks its scenario hash, but the other
required fault bundles validate and preservation is intact.

## Benchmark and budget

Three baseline and three candidate p95 samples are preserved. Candidate median is
8% slower. The proposed budget is 10%, but there is no dispersion/inconclusive
rule and all candidates ran after baselines. The learner correctly labels the
result provisional rather than Pass.

## Decision and ownership

Continue investigation before rollout. The review names service and observability
owners, a canary, rollback, telemetry privacy, and cost questions. Failover headroom,
metric-name migration, and numeric reversal evidence are incomplete.

## Teach-back and next work

The recording explains symptom, CPU hypothesis, and proposed experiment. A
reviewer exposes the allocation-retention gap. The learner records that gap and
keeps the original diagnosis unchanged, but follow-up exercises and due dates
are not yet assigned.
