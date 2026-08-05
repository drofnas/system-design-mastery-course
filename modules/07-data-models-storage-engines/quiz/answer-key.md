# M07 Quiz Answer Key

This key covers all 100 questions for **Data Models and Storage Engines**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M07-Q001

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to derive logical and physical data models from quantified access paths, invariants, retention, growth, and ownership.

**Explanation:** Use Workloads, Access Paths, and Data Models to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M07-Q002

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Pages, Records, Buffer Pools, and Locality', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Pages, Records, Buffer Pools, and Locality to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M07-Q003

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Derive B+ tree point, range, insert, split, and delete paths.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M07-Q004

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Treating flush as durable acknowledgement:** without an explicit WAL and

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M07-Q005

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for calculate read, write, and space amplification and connect them to tail latency, capacity, cost, and ssd endurance..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - RocksDB compaction trade-offs, RES-05–RES-06.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M07-Q006

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to choose indexes and diagnose query plans whose estimates, statistics, or access paths do not match the workload.

**Explanation:** Use Query Plans, Statistics, and Index Design to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M07-Q007

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Skew, Background Debt, Stalls, and Diagnosis', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Skew, Background Debt, Stalls, and Diagnosis to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M07-Q008

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Turn workload and failure evidence into a reviewable storage ADR.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M07-Q009

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Choosing from nouns:** “telemetry means time-series database” omits actual

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M07-Q010

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for explain and measure how pages, records, buffer pools, locality, and cache policy shape physical work..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - SQLite Database File Format Sections 1.2, 1.6, and 2.1 RES-01.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M07-Q011

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to implement and validate a persistent paged b+ tree with point lookup, range scan, splits, cache behavior, deletion, and clean reopen.

**Explanation:** Use B+ Trees, Hash Indexes, and Inverted Indexes to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M07-Q012

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'LSM Paths, Bloom Filters, Tombstones, and Compaction', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use LSM Paths, Bloom Filters, Tombstones, and Compaction to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M07-Q013

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Calculate read, write, and space amplification from trial counters.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M07-Q014

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Reading only the top plan node:** the first cardinality error is often

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M07-Q015

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for diagnose read, write, range, skew, delete, cache, bloom, compaction, and tombstone behavior from preserved same-input evidence..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - RocksDB Write Stalls RES-07 and Compaction RES-06.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M07-Q016

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to defend a storage-engine decision covering security, operations, cost, ownership, migration, rollback, recovery requirements, and reversal evidence.

**Explanation:** Use Storage Decisions, Migration, Cost, and Ownership to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M07-Q017

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Workloads, Access Paths, and Data Models', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Workloads, Access Paths, and Data Models to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M07-Q018

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Derive approximate page occupancy and tree fan-out from record layout.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M07-Q019

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Implementing a binary tree in pages:** low fan-out defeats page-oriented

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M07-Q020

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for implement and validate an lsm store with memtable, sstables, sparse indexes, bloom filters, tombstones, and compaction..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Original LSM-tree paper, bounded in RES-04.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M07-Q021

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to calculate read, write, and space amplification and connect them to tail latency, capacity, cost, and ssd endurance.

**Explanation:** Use Amplification and SSD Endurance to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M07-Q022

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Query Plans, Statistics, and Index Design', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Query Plans, Statistics, and Index Design to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M07-Q023

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Predict how skew and deletes change foreground and background work.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M07-Q024

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Writing “use LSM for writes”:** no workload, amplification, or recovery

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M07-Q025

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for derive logical and physical data models from quantified access paths, invariants, retention, growth, and ownership..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - CMU 15-445/645 Spring 2026 storage-model materials, bounded in RES-03.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M07-Q026

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to explain and measure how pages, records, buffer pools, locality, and cache policy shape physical work.

**Explanation:** Use Pages, Records, Buffer Pools, and Locality to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M07-Q027

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'B+ Trees, Hash Indexes, and Inverted Indexes', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use B+ Trees, Hash Indexes, and Inverted Indexes to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M07-Q028

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Trace puts, gets, ranges, deletes, flushes, and compactions through an LSM.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M07-Q029

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Comparing ratios with different denominators:** key-only and key-plus-value

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M07-Q030

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for choose indexes and diagnose query plans whose estimates, statistics, or access paths do not match the workload..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - PostgreSQL Indexes, EXPLAIN, and Planner Statistics, RES-08–RES-10.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M07-Q031

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to diagnose read, write, range, skew, delete, cache, bloom, compaction, and tombstone behavior from preserved same-input evidence.

**Explanation:** Use Skew, Background Debt, Stalls, and Diagnosis to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M07-Q032

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Storage Decisions, Migration, Cost, and Ownership', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Storage Decisions, Migration, Cost, and Ownership to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M07-Q033

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Convert user operations into an access-path matrix with rates, selectivity, order, result size, freshness, and growth.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M07-Q034

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Using payload/page as exact capacity:** headers, slots, fill factor, and

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M07-Q035

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for implement and validate a persistent paged b+ tree with point lookup, range scan, splits, cache behavior, deletion, and clean reopen..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - CMU Database Group B+ tree video and written local alternative RES-02.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M07-Q036

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to implement and validate an lsm store with memtable, sstables, sparse indexes, bloom filters, tombstones, and compaction.

**Explanation:** Use LSM Paths, Bloom Filters, Tombstones, and Compaction to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M07-Q037

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Amplification and SSD Endurance', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Amplification and SSD Endurance to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M07-Q038

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Trace a query plan from estimates to actual work and results.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M07-Q039

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Changing workload and policy together:** the cause cannot be isolated.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M07-Q040

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for defend a storage-engine decision covering security, operations, cost, ownership, migration, rollback, recovery requirements, and reversal evidence..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - RocksDB practitioner materials RES-05–RES-07, PostgreSQL resources RES-08–RES-10, and NVM Express RES-11.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M07-Q041

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to derive logical and physical data models from quantified access paths, invariants, retention, growth, and ownership.

**Explanation:** Use Workloads, Access Paths, and Data Models to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M07-Q042

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Pages, Records, Buffer Pools, and Locality', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Pages, Records, Buffer Pools, and Locality to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M07-Q043

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Derive B+ tree point, range, insert, split, and delete paths.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M07-Q044

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Treating flush as durable acknowledgement:** without an explicit WAL and

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M07-Q045

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for calculate read, write, and space amplification and connect them to tail latency, capacity, cost, and ssd endurance..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - RocksDB compaction trade-offs, RES-05–RES-06.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M07-Q046

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to choose indexes and diagnose query plans whose estimates, statistics, or access paths do not match the workload.

**Explanation:** Use Query Plans, Statistics, and Index Design to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M07-Q047

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Skew, Background Debt, Stalls, and Diagnosis', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Skew, Background Debt, Stalls, and Diagnosis to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M07-Q048

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Turn workload and failure evidence into a reviewable storage ADR.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M07-Q049

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Choosing from nouns:** “telemetry means time-series database” omits actual

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M07-Q050

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for explain and measure how pages, records, buffer pools, locality, and cache policy shape physical work..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - SQLite Database File Format Sections 1.2, 1.6, and 2.1 RES-01.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M07-Q051

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to implement and validate a persistent paged b+ tree with point lookup, range scan, splits, cache behavior, deletion, and clean reopen.

**Explanation:** Use B+ Trees, Hash Indexes, and Inverted Indexes to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M07-Q052

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'LSM Paths, Bloom Filters, Tombstones, and Compaction', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use LSM Paths, Bloom Filters, Tombstones, and Compaction to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M07-Q053

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Calculate read, write, and space amplification from trial counters.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M07-Q054

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Reading only the top plan node:** the first cardinality error is often

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M07-Q055

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for diagnose read, write, range, skew, delete, cache, bloom, compaction, and tombstone behavior from preserved same-input evidence..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - RocksDB Write Stalls RES-07 and Compaction RES-06.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M07-Q056

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to defend a storage-engine decision covering security, operations, cost, ownership, migration, rollback, recovery requirements, and reversal evidence.

**Explanation:** Use Storage Decisions, Migration, Cost, and Ownership to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M07-Q057

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Workloads, Access Paths, and Data Models', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Workloads, Access Paths, and Data Models to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M07-Q058

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Derive approximate page occupancy and tree fan-out from record layout.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M07-Q059

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Implementing a binary tree in pages:** low fan-out defeats page-oriented

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M07-Q060

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for implement and validate an lsm store with memtable, sstables, sparse indexes, bloom filters, tombstones, and compaction..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Original LSM-tree paper, bounded in RES-04.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M07-Q061

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to calculate read, write, and space amplification and connect them to tail latency, capacity, cost, and ssd endurance.

**Explanation:** Use Amplification and SSD Endurance to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M07-Q062

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Query Plans, Statistics, and Index Design', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Query Plans, Statistics, and Index Design to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M07-Q063

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Predict how skew and deletes change foreground and background work.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M07-Q064

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Writing “use LSM for writes”:** no workload, amplification, or recovery

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M07-Q065

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for derive logical and physical data models from quantified access paths, invariants, retention, growth, and ownership..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - CMU 15-445/645 Spring 2026 storage-model materials, bounded in RES-03.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M07-Q066

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to explain and measure how pages, records, buffer pools, locality, and cache policy shape physical work.

**Explanation:** Use Pages, Records, Buffer Pools, and Locality to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M07-Q067

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'B+ Trees, Hash Indexes, and Inverted Indexes', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use B+ Trees, Hash Indexes, and Inverted Indexes to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M07-Q068

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Trace puts, gets, ranges, deletes, flushes, and compactions through an LSM.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M07-Q069

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Comparing ratios with different denominators:** key-only and key-plus-value

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M07-Q070

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for choose indexes and diagnose query plans whose estimates, statistics, or access paths do not match the workload..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - PostgreSQL Indexes, EXPLAIN, and Planner Statistics, RES-08–RES-10.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M07-Q071

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to diagnose read, write, range, skew, delete, cache, bloom, compaction, and tombstone behavior from preserved same-input evidence.

**Explanation:** Use Skew, Background Debt, Stalls, and Diagnosis to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M07-Q072

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Storage Decisions, Migration, Cost, and Ownership', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Storage Decisions, Migration, Cost, and Ownership to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M07-Q073

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Convert user operations into an access-path matrix with rates, selectivity, order, result size, freshness, and growth.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M07-Q074

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Using payload/page as exact capacity:** headers, slots, fill factor, and

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M07-Q075

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for implement and validate a persistent paged b+ tree with point lookup, range scan, splits, cache behavior, deletion, and clean reopen..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - CMU Database Group B+ tree video and written local alternative RES-02.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M07-Q076

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to implement and validate an lsm store with memtable, sstables, sparse indexes, bloom filters, tombstones, and compaction.

**Explanation:** Use LSM Paths, Bloom Filters, Tombstones, and Compaction to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M07-Q077

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Amplification and SSD Endurance', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Amplification and SSD Endurance to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M07-Q078

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Trace a query plan from estimates to actual work and results.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M07-Q079

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Changing workload and policy together:** the cause cannot be isolated.

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M07-Q080

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for defend a storage-engine decision covering security, operations, cost, ownership, migration, rollback, recovery requirements, and reversal evidence..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - RocksDB practitioner materials RES-05–RES-07, PostgreSQL resources RES-08–RES-10, and NVM Express RES-11.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M07-Q081

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to derive logical and physical data models from quantified access paths, invariants, retention, growth, and ownership.

**Explanation:** Use Workloads, Access Paths, and Data Models to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M07-Q082

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Pages, Records, Buffer Pools, and Locality', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Pages, Records, Buffer Pools, and Locality to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M07-Q083

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Derive B+ tree point, range, insert, split, and delete paths.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M07-Q084

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Treating flush as durable acknowledgement:** without an explicit WAL and

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M07-Q085

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for calculate read, write, and space amplification and connect them to tail latency, capacity, cost, and ssd endurance..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - RocksDB compaction trade-offs, RES-05–RES-06.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M07-Q086

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to choose indexes and diagnose query plans whose estimates, statistics, or access paths do not match the workload.

**Explanation:** Use Query Plans, Statistics, and Index Design to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M07-Q087

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Skew, Background Debt, Stalls, and Diagnosis', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Skew, Background Debt, Stalls, and Diagnosis to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M07-Q088

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Turn workload and failure evidence into a reviewable storage ADR.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M07-Q089

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Choosing from nouns:** “telemetry means time-series database” omits actual

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M07-Q090

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for explain and measure how pages, records, buffer pools, locality, and cache policy shape physical work..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - SQLite Database File Format Sections 1.2, 1.6, and 2.1 RES-01.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M07-Q091

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to implement and validate a persistent paged b+ tree with point lookup, range scan, splits, cache behavior, deletion, and clean reopen.

**Explanation:** Use B+ Trees, Hash Indexes, and Inverted Indexes to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M07-Q092

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'LSM Paths, Bloom Filters, Tombstones, and Compaction', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use LSM Paths, Bloom Filters, Tombstones, and Compaction to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M07-Q093

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Calculate read, write, and space amplification from trial counters.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M07-Q094

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Reading only the top plan node:** the first cardinality error is often

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M07-Q095

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for diagnose read, write, range, skew, delete, cache, bloom, compaction, and tombstone behavior from preserved same-input evidence..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - RocksDB Write Stalls RES-07 and Compaction RES-06.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.

## M07-Q096

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Answer:** Start from the lesson's mechanism, state assumptions and boundaries, and connect the result to defend a storage-engine decision covering security, operations, cost, ownership, migration, rollback, recovery requirements, and reversal evidence.

**Explanation:** Use Storage Decisions, Migration, Cost, and Ownership to reason from explicit assumptions to observable behavior. The best answer makes the reasoning boundary explicit before selecting or defending an approach.

**Grading notes:** Full credit requires choosing the mechanism-first answer and rejecting label-first or overgeneralized reasoning.

## M07-Q097

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** A strong answer defines the mechanism from 'Workloads, Access Paths, and Data Models', states the relevant assumptions or boundary, explains the causal link to the outcome, and names one limitation or follow-up check.

**Explanation:** Use Workloads, Access Paths, and Data Models to reason from explicit assumptions to observable behavior.

**Grading notes:** Award full credit for precise mechanism, assumptions, causal link, and limitation. Partial credit for vocabulary without causal explanation.

## M07-Q098

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Identify the input quantities, align units and time windows, compute the relevant rate/capacity/latency/cost or bound, and state what result would falsify the claim.

**Explanation:** Calculation questions in this course are about scoped evidence, not numerology. - Derive approximate page occupancy and tree fan-out from record layout.

**Grading notes:** Full credit requires named quantities, consistent units, a computable relationship, and a falsification threshold.

## M07-Q099

**Type:** `scenario_diagnosis`  
**Difficulty:** `application`

**Answer:** Inspect the boundary assumptions, measured signals, and invariant or resource that failed first. A likely mistake is: **Implementing a binary tree in pages:** low fan-out defeats page-oriented

**Explanation:** Good diagnosis moves from observed evidence to the first violated assumption instead of jumping to a tool replacement.

**Grading notes:** Full credit requires an observable first check and a plausible causal mistake. Do not give full credit for generic debugging advice.

## M07-Q100

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Document the decision drivers, credible alternatives, expected behavior, cost or operational consequences, and a specific reversal condition tied to measured evidence for implement and validate an lsm store with memtable, sstables, sparse indexes, bloom filters, tombstones, and compaction..

**Explanation:** Design judgment is strongest when it keeps alternatives alive until evidence rules them out. - Original LSM-tree paper, bounded in RES-04.

**Grading notes:** Full credit requires at least two alternatives, an evidence-based driver, and a concrete reversal condition.
