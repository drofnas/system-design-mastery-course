# M00 Quiz Answer Key

This key covers all 37 questions for **Algorithmic Foundations**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M00-Q001

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** A positive multiplier `c` and a threshold `n0`; the bound only needs to hold beyond `n0`.

**Explanation:** M00-Q001 uses self-check 1 from Asymptotic Analysis and Its Limits; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M00-Q002

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Amortized cost bounds a sequence without assuming random input; average case depends on an input distribution.

**Explanation:** M00-Q002 uses self-check 2 from Asymptotic Analysis and Its Limits; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M00-Q003

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** The body runs `n(n+1)/2` times, so the tight bound is Theta(n^2).

**Explanation:** M00-Q003 uses self-check 3 from Asymptotic Analysis and Its Limits; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M00-Q004

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Representative input sizes, operation mix, memory layout, branch behavior, allocation cost, and tail latency for the actual workload. For the practice, copied capacities are `1 + 2 + 4 + 8 = 15`; total work is bounded by a small multiple of 17, but the append that grows from 16 to 32 copies 16 existing elements.

**Explanation:** M00-Q004 uses self-check 4 from Asymptotic Analysis and Its Limits; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M00-Q005

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** The address is computed from base plus index times element width, or from an equivalent runtime table lookup.

**Explanation:** M00-Q005 uses self-check 1 from Arrays, Dynamic Arrays, and Locality; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M00-Q006

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** It bounds total copy work across many appends but creates spare memory and occasional resize spikes.

**Explanation:** M00-Q006 uses self-check 2 from Arrays, Dynamic Arrays, and Locality; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M00-Q007

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Only when the insertion point or node reference is already known; finding that point may still be O(n).

**Explanation:** M00-Q007 uses self-check 3 from Arrays, Dynamic Arrays, and Locality; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M00-Q008

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** CPython lists store references to objects and the lab runs interpreter loops, so it shows local runtime behavior, not isolated cache-line mechanics. For the practice, new capacity is 2,048, peak slots are about 3,072, and headroom after the append is 1,023 slots.

**Explanation:** M00-Q008 uses self-check 4 from Arrays, Dynamic Arrays, and Locality; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M00-Q009

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** Keys distribute uniformly enough and the implementation keeps load factor bounded.

**Explanation:** M00-Q009 uses self-check 1 from Hash Tables; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M00-Q010

**Type:** `short_answer`
**Difficulty:** `recall`

**Answer:** The sequence has bounded average cost, but one request can pay the rehash cost unless resize is moved or controlled.

**Explanation:** M00-Q010 uses self-check 2 from Hash Tables; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M00-Q011

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** `1/(1-0.9) = 10`, far higher than the `2` factor at alpha 0.5.

**Explanation:** M00-Q011 uses self-check 3 from Hash Tables; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M00-Q012

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** It lacks sorted order; use a tree, sorted index, heap, or expiry buckets depending on the operation. For the practice, alpha is 0.5 and 0.9, so the approximate factors are 2 and 10; the ordered scan needs another ordered mechanism.

**Explanation:** M00-Q012 uses self-check 4 from Hash Tables; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M00-Q013

**Type:** `short_answer`
**Difficulty:** `synthesis`

**Answer:** Search, insert, and delete can become O(n).

**Explanation:** M00-Q013 uses self-check 1 from Trees and Balanced Search; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M00-Q014

**Type:** `short_answer`
**Difficulty:** `application`

**Answer:** It keeps height logarithmic at the cost of mutation maintenance.

**Explanation:** M00-Q014 uses self-check 2 from Trees and Balanced Search; the answer ties the mechanism to the cited evidence scope rather than a label.

**Grading notes:** Full credit requires the causal mechanism and the boundary or evidence named in the lesson; partial credit can preserve the idea with weaker specificity.

## M00-Q015

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure constants hot data for review case one; limit the change.
- Measure worst case data for review case one; limit the change.
- Measure amortized cost data for review case one; limit the change.
- Measure algorithms checking data for review case one; limit the change.

**Answer:** Measure constants hot data for review case one; limit the change.

**Explanation:** M00-Q015 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects constants hot as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M00-Q016

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure amortized means data for review case two; limit the change.
- Measure worst case data for review case two; limit the change.
- Measure linked list data for review case two; limit the change.
- Measure contiguous growth data for review case two; limit the change.

**Answer:** Measure worst case data for review case two; limit the change.

**Explanation:** M00-Q016 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects worst case as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M00-Q017

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure random input data for review case three; limit the change.
- Measure resize spikes data for review case three; limit the change.
- Measure amortized cost data for review case three; limit the change.
- Measure only hash data for review case three; limit the change. with margin

**Answer:** Measure amortized cost data for review case three; limit the change.

**Explanation:** M00-Q017 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects amortized cost as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M00-Q018

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure hashing range data for review case four; limit the change.
- Measure balance maintenance data for review case four; limit the change.
- Measure storage index data for review case four; limit the change.
- Measure algorithms checking data for review case four; limit the change.

**Answer:** Measure algorithms checking data for review case four; limit the change.

**Explanation:** M00-Q018 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects algorithms checking as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M00-Q019

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure amortized means data for review case five; limit the change.
- Measure priority boolean data for review case five; limit the change.
- Measure starvation heaps data for review case five; limit the change.
- Measure priority queues data for review case five; limit the change.

**Answer:** Measure amortized means data for review case five; limit the change.

**Explanation:** M00-Q019 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects amortized means as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M00-Q020

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Measure matrix sparse data for review case six; limit the change.
- Measure linked list data for review case six; limit the change.
- Measure cycles dependency data for review case six; limit the change.
- Measure first found data for review case six; limit the change.

**Answer:** Measure linked list data for review case six; limit the change.

**Explanation:** M00-Q020 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects linked list as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M00-Q021

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Measure sorting top data for review case seven; limit the change.
- Measure memory temporary data for review case seven; limit the change.
- Measure contiguous growth data for review case seven; limit the change.
- Measure exponential search data for review case seven; limit the change.

**Answer:** Measure contiguous growth data for review case seven; limit the change.

**Explanation:** M00-Q021 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects contiguous growth as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M00-Q022

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Measure constraints code data for review case eight; limit the change.
- Measure score preserving data for review case eight; limit the change.
- Measure workload growth data for review case eight; limit the change.
- Measure random input data for review case eight; limit the change.

**Answer:** Measure random input data for review case eight; limit the change.

**Explanation:** M00-Q022 asks the learner to map the disputed proposal to the matching measurement target rather than a nearby concern.

**Grading notes:** Full credit selects random input as the deciding target and explains why the other listed targets are adjacent rather than decisive.

## M00-Q023

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Calculation for asymptotic analysis and its limits, resizes copy 1 + 2 + 4 + ... below 18, totaling 31 copied items; final capacity is 32 slots.

**Explanation:** M00-Q023 uses amortized resize copies from Asymptotic Analysis and Its Limits and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M00-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Calculation for arrays, dynamic arrays, and locality, at alpha 0.50, 1/(1-0.50) = 2. At alpha 0.90, 1/(1-0.90) = 10, so the high-load table is about 5x worse by this approximation.

**Explanation:** M00-Q024 uses open addressing probe factor from Arrays, Dynamic Arrays, and Locality and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M00-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Calculation for hash tables, m00 B-Tree Fanout Height case 3: The B-tree needs about 4 page-level steps versus about 24 binary comparisons, a 20-level reduction in path depth for page-oriented access.

**Explanation:** M00-Q025 uses B-tree fanout height from Hash Tables and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M00-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Calculation for trees and balanced search, heap height is floor(log2(1536)) = 10, so a sift traverses at most 10 levels.

**Explanation:** M00-Q026 uses heap height from Trees and Balanced Search and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M00-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Calculation for heaps and priority queues, the adjacency list stores about 2 x 2550 = 5100 endpoint entries, while the matrix stores 850 x 850 = 722500 cells.

**Explanation:** M00-Q027 uses graph representation size from Heaps and Priority Queues and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M00-Q028

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** Calculation for graphs and traversal, the adjacency list stores about 2 x 2580 = 5160 endpoint entries, while the matrix stores 860 x 860 = 739600 cells.

**Explanation:** M00-Q028 uses graph representation size from Graphs and Traversal and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M00-Q029

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Calculation for sorting and selection, the naive count is 12 x 1070 = 12840 comparisons before any pruning changes the shape of the search.

**Explanation:** M00-Q029 uses candidate count from Sorting and Selection and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M00-Q030

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** Calculation for tractability and design decisions, resizes copy 1 + 2 + 4 + ... below 25, totaling 31 copied items; final capacity is 32 slots.

**Explanation:** M00-Q030 uses amortized resize copies from Tractability and Design Decisions and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M00-Q031

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Approve Growth Classes at 117.6/s. The deciding number is 180 x 0.72 = 129.6/s, leaving 12/s before the reserve is consumed. Withdraw approval if a drill, trace, or workload sample shows growth classes demand above 129.6/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to growth classes demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 129.6/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M00-Q032

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** Decline Amortized Resize at 153.2/s. The deciding number is 197 x 0.72 = 141.8/s, so planned demand exceeds the usable region by 11.4/s. Approve later if repeated measurements lift usable capacity above 153.2/s or a named policy removes at least 11.4/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to amortized resize demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 141.8/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M00-Q033

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** Approve conditionally for Operation Mix. The deciding number is 214 x 0.72 = 154.1/s, and 149.1/s fits only while the fallback remains enforceable. Keep the condition until recovery traffic, priority demand, or fallback tests show less than 5/s of usable margin.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to operation mix demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 154.1/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M00-Q034

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Approve Locality at 149.2/s. The deciding number is 231 x 0.72 = 166.3/s, leaving 17.1/s before the reserve is consumed. Require redesign if a drill, trace, or workload sample shows locality demand above 166.3/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to locality demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 166.3/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M00-Q035

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** Decline Graph Representation at 194.2/s. The deciding number is 248 x 0.72 = 178.6/s, so planned demand exceeds the usable region by 15.6/s. Lift the decline if repeated measurements lift usable capacity above 194.2/s or a named policy removes at least 15.6/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to graph representation demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 178.6/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M00-Q036

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** Approve Priority Semantics at 170.3/s. The deciding number is 265 x 0.72 = 190.8/s, leaving 20.5/s before the reserve is consumed. Reverse the call if a drill, trace, or workload sample shows priority semantics demand above 190.8/s or proves the shed point cannot protect lower-priority work.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to priority semantics demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 190.8/s, compares it with planned demand, and names a scenario-specific reversal condition.

## M00-Q037

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** Decline Sorting Boundary at 221.4/s. The deciding number is 282 x 0.72 = 203/s, so planned demand exceeds the usable region by 18.4/s. Accept the proposal when repeated measurements lift usable capacity above 221.4/s or a named policy removes at least 18.4/s of deferrable work before saturation.

**Explanation:** The decision turns on the usable capacity after the reserve, not the nominal measurement alone. The reversal condition is tied to sorting boundary demand and the protection policy in this case.

**Grading notes:** Full credit gives the stated decision, computes 203/s, compares it with planned demand, and names a scenario-specific reversal condition.
