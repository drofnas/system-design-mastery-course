# M00 Quiz Answer Key

This key covers all 37 questions for **Algorithmic Foundations**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

## M00-Q001

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** A positive multiplier c and a threshold n0; the bound only needs to hold beyond n0

**Explanation:** The cited self-check in L01 tests whether the learner can connect Asymptotic Analysis and Its Limits to the module mechanism without replacing evidence with labels. This explanation is specific to M00-Q001 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M00-Q002

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** Amortized cost bounds a sequence without assuming random input; average case depends on an input distribution

**Explanation:** The cited self-check in L01 tests whether the learner can connect Asymptotic Analysis and Its Limits to the module mechanism without replacing evidence with labels. This explanation is specific to M00-Q002 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M00-Q003

**Type:** `short_answer`  
**Difficulty:** `synthesis`

**Answer:** The body runs n(n+1)/2 times, so the tight bound is Theta(n^2)

**Explanation:** The cited self-check in L01 tests whether the learner can connect Asymptotic Analysis and Its Limits to the module mechanism without replacing evidence with labels. This explanation is specific to M00-Q003 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M00-Q004

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** Representative input sizes, operation mix, memory layout, branch behavior, allocation cost, and tail latency for the actual workload. For the practice, copied capacities are 1 + 2 + 4 + 8 = 15; total work is bounded by a small multiple of 17, but the append that grows from 16 to 32 copies 16 existing elements

**Explanation:** The cited self-check in L01 tests whether the learner can connect Asymptotic Analysis and Its Limits to the module mechanism without replacing evidence with labels. This explanation is specific to M00-Q004 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M00-Q005

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** The address is computed from base plus index times element width, or from an equivalent runtime table lookup

**Explanation:** The cited self-check in L02 tests whether the learner can connect Arrays, Dynamic Arrays, and Locality to the module mechanism without replacing evidence with labels. This explanation is specific to M00-Q005 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M00-Q006

**Type:** `short_answer`  
**Difficulty:** `synthesis`

**Answer:** It bounds total copy work across many appends but creates spare memory and occasional resize spikes

**Explanation:** The cited self-check in L02 tests whether the learner can connect Arrays, Dynamic Arrays, and Locality to the module mechanism without replacing evidence with labels. This explanation is specific to M00-Q006 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M00-Q007

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** Only when the insertion point or node reference is already known; finding that point may still be O(n)

**Explanation:** The cited self-check in L02 tests whether the learner can connect Arrays, Dynamic Arrays, and Locality to the module mechanism without replacing evidence with labels. This explanation is specific to M00-Q007 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M00-Q008

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** CPython lists store references to objects and the lab runs interpreter loops, so it shows local runtime behavior, not isolated cache-line mechanics. For the practice, new capacity is 2,048, peak slots are about 3,072, and headroom after the append is 1,023 slots

**Explanation:** The cited self-check in L02 tests whether the learner can connect Arrays, Dynamic Arrays, and Locality to the module mechanism without replacing evidence with labels. This explanation is specific to M00-Q008 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M00-Q009

**Type:** `short_answer`  
**Difficulty:** `synthesis`

**Answer:** Keys distribute uniformly enough and the implementation keeps load factor bounded

**Explanation:** The cited self-check in L03 tests whether the learner can connect Hash Tables to the module mechanism without replacing evidence with labels. This explanation is specific to M00-Q009 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M00-Q010

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** The sequence has bounded average cost, but one request can pay the rehash cost unless resize is moved or controlled

**Explanation:** The cited self-check in L03 tests whether the learner can connect Hash Tables to the module mechanism without replacing evidence with labels. This explanation is specific to M00-Q010 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M00-Q011

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** 1/(1-0.9) = 10, far higher than the 2 factor at alpha 0.5

**Explanation:** The cited self-check in L03 tests whether the learner can connect Hash Tables to the module mechanism without replacing evidence with labels. This explanation is specific to M00-Q011 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M00-Q012

**Type:** `short_answer`  
**Difficulty:** `synthesis`

**Answer:** It lacks sorted order; use a tree, sorted index, heap, or expiry buckets depending on the operation. For the practice, alpha is 0.5 and 0.9, so the approximate factors are 2 and 10; the ordered scan needs another ordered mechanism

**Explanation:** The cited self-check in L03 tests whether the learner can connect Hash Tables to the module mechanism without replacing evidence with labels. This explanation is specific to M00-Q012 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M00-Q013

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** Search, insert, and delete can become O(n)

**Explanation:** The cited self-check in L04 tests whether the learner can connect Trees and Balanced Search to the module mechanism without replacing evidence with labels. This explanation is specific to M00-Q013 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M00-Q014

**Type:** `short_answer`  
**Difficulty:** `application`

**Answer:** It keeps height logarithmic at the cost of mutation maintenance

**Explanation:** The cited self-check in L04 tests whether the learner can connect Trees and Balanced Search to the module mechanism without replacing evidence with labels. This explanation is specific to M00-Q014 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M00-Q015

**Type:** `short_answer`  
**Difficulty:** `synthesis`

**Answer:** Larger fanout reduces levels, and levels often map to page reads or cache misses

**Explanation:** The cited self-check in L04 tests whether the learner can connect Trees and Balanced Search to the module mechanism without replacing evidence with labels. This explanation is specific to M00-Q015 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M00-Q016

**Type:** `short_answer`  
**Difficulty:** `recall`

**Answer:** Trees preserve sorted order, so they can seek then scan contiguous key ranges. For the practice, height is about 4; binary height is about 27; a tenant/time-window query is a typical range

**Explanation:** The cited self-check in L04 tests whether the learner can connect Trees and Balanced Search to the module mechanism without replacing evidence with labels. This explanation is specific to M00-Q016 and its cited source.

**Grading notes:** Full credit requires the concrete mechanism and the boundary or evidence named in the cited lesson. Partial credit is appropriate when the answer has the right vocabulary but misses the causal condition.

## M00-Q017

**Type:** `multiple_choice`  
**Difficulty:** `application`

**Choices:**

- Keep Asymptotic Analysis and Its Limits scoped to its stated evidence and boundary.
- Treat Ignoring constants for hot paths as complete proof without the lesson boundary
- Make the documented mistake: Ignoring constants for hot paths
- Choose the familiar tool before checking whether Ignoring constants for hot paths applies

**Answer:** Keep Asymptotic Analysis and Its Limits scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M00-Q017 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M00-Q018

**Type:** `multiple_choice`  
**Difficulty:** `synthesis`

**Choices:**

- Choose the familiar tool before checking whether Using worst-case notation without naming the adversary or input cond.
- Keep Asymptotic Analysis and Its Limits scoped to its stated evidence and boundary.
- Treat Using worst-case notation without naming the adversary or input condi as complete proof without the lesson boun.
- Make the documented mistake: Using worst-case notation without naming the adversary or input co

**Answer:** Keep Asymptotic Analysis and Its Limits scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M00-Q018 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M00-Q019

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Choices:**

- Make the documented mistake: Calling amortized cost a latency guarantee
- Choose the familiar tool before checking whether Calling amortized cost a latency guarantee applies
- Keep Asymptotic Analysis and Its Limits scoped to its stated evidence and boundary.
- Treat Calling amortized cost a latency guarantee as complete proof without the lesson boundary

**Answer:** Keep Asymptotic Analysis and Its Limits scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M00-Q019 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M00-Q020

**Type:** `multiple_choice`  
**Difficulty:** `application`

**Choices:**

- Make the documented mistake: Comparing algorithms without checking memory layout
- Treat Comparing algorithms without checking memory layout as complete proof without the lesson boundary
- Choose the familiar tool before checking whether Comparing algorithms without checking memory layout applies
- Keep Asymptotic Analysis and Its Limits scoped to its stated evidence and boundary.

**Answer:** Keep Asymptotic Analysis and Its Limits scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L01; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M00-Q020 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M00-Q021

**Type:** `multiple_choice`  
**Difficulty:** `synthesis`

**Choices:**

- Keep Arrays, Dynamic Arrays, and Locality scoped to its stated evidence and boundary.
- Treat Saying amortized O(1) means every append is cheap as complete proof without the lesson boundary
- Choose the familiar tool before checking whether Saying amortized O(1) means every append is cheap applies
- Make the documented mistake: Saying amortized O(1) means every append is cheap

**Answer:** Keep Arrays, Dynamic Arrays, and Locality scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M00-Q021 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M00-Q022

**Type:** `multiple_choice`  
**Difficulty:** `recall`

**Choices:**

- Make the documented mistake: Choosing a linked list for insertion while ignoring how the insert
- Keep Arrays, Dynamic Arrays, and Locality scoped to its stated evidence and boundary.
- Choose the familiar tool before checking whether Choosing a linked list for insertion while ignoring how the insertio.
- Treat Choosing a linked list for insertion while ignoring how the insertion as complete proof without the lesson boun.

**Answer:** Keep Arrays, Dynamic Arrays, and Locality scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M00-Q022 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M00-Q023

**Type:** `multiple_choice`  
**Difficulty:** `application`

**Choices:**

- Choose the familiar tool before checking whether Forgetting that contiguous growth can require copying and memory hea.
- Treat Forgetting that contiguous growth can require copying and memory head as complete proof without the lesson boun.
- Keep Arrays, Dynamic Arrays, and Locality scoped to its stated evidence and boundary.
- Make the documented mistake: Forgetting that contiguous growth can require copying and memory h

**Answer:** Keep Arrays, Dynamic Arrays, and Locality scoped to its stated evidence and boundary.

**Explanation:** The distractors are anchored in the mistake list for L02; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M00-Q023 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M00-Q024

**Type:** `multiple_choice`  
**Difficulty:** `synthesis`

**Choices:**

- Treat Assuming random input when keys are user-controlled as complete proof without the lesson boundary
- Choose the familiar tool before checking whether Assuming random input when keys are user-controlled applies
- Make the documented mistake: Assuming random input when keys are user-controlled
- Keep Hash Tables scoped to its stated evidence and boundary. for hash tables

**Answer:** Keep Hash Tables scoped to its stated evidence and boundary. for hash tables

**Explanation:** The distractors are anchored in the mistake list for L03; the correct choice preserves the lesson boundary before drawing a conclusion. This explanation is specific to M00-Q024 and its cited source.

**Grading notes:** Full credit requires selecting the boundary-preserving option and rejecting the tempting misconception from the cited mistake list.

## M00-Q025

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Original concurrency = 120 x 0.035 = 4.20 operations. Revised rate = 120 x 1.25 = 150.0/s, so revised concurrency = 150.0 x 0.035 = 5.25 operations.

**Explanation:** This perturbs the numeric practice around Asymptotic Analysis and Its Limits: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M00-Q025 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M00-Q026

**Type:** `calculation`  
**Difficulty:** `recall`

**Answer:** Original concurrency = 130 x 0.045 = 5.85 operations. Revised rate = 130 x 1.30 = 169.0/s, so revised concurrency = 169.0 x 0.045 = 7.61 operations.

**Explanation:** This perturbs the numeric practice around Arrays, Dynamic Arrays, and Locality: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M00-Q026 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M00-Q027

**Type:** `calculation`  
**Difficulty:** `application`

**Answer:** Original concurrency = 140 x 0.055 = 7.70 operations. Revised rate = 140 x 1.35 = 189.0/s, so revised concurrency = 189.0 x 0.055 = 10.39 operations.

**Explanation:** This perturbs the numeric practice around Hash Tables: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M00-Q027 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M00-Q028

**Type:** `calculation`  
**Difficulty:** `synthesis`

**Answer:** Original concurrency = 150 x 0.065 = 9.75 operations. Revised rate = 150 x 1.40 = 210.0/s, so revised concurrency = 210.0 x 0.065 = 13.65 operations.

**Explanation:** This perturbs the numeric practice around Trees and Balanced Search: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M00-Q028 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M00-Q029

**Type:** `calculation`  
**Difficulty:** `recall`

**Answer:** Original concurrency = 160 x 0.075 = 12.00 operations. Revised rate = 160 x 1.45 = 232.0/s, so revised concurrency = 232.0 x 0.075 = 17.40 operations.

**Explanation:** This perturbs the numeric practice around Heaps and Priority Queues: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M00-Q029 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M00-Q030

**Type:** `calculation`  
**Difficulty:** `application`

**Answer:** Original concurrency = 170 x 0.035 = 5.95 operations. Revised rate = 170 x 1.10 = 187.0/s, so revised concurrency = 187.0 x 0.035 = 6.55 operations.

**Explanation:** This perturbs the numeric practice around Graphs and Traversal: keep the same boundary, align milliseconds to seconds, then apply rate times scoped work. This explanation is specific to M00-Q030 and its cited source.

**Grading notes:** Full credit requires both concurrency values, unit conversion from ms to seconds, and a statement that the boundary stayed unchanged.

## M00-Q031

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Recommend the option that preserves the Trees and Balanced Search mechanism under the exercise constraints: Asymptotic reasoning, core data structures, graph algorithms, sorting, and tractability as practical design tools The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M00-Q031 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M00-Q032

**Type:** `design_judgment`  
**Difficulty:** `recall`

**Answer:** Recommend the option that preserves the Heaps and Priority Queues mechanism under the exercise constraints: Asymptotic reasoning, core data structures, graph algorithms, sorting, and tractability as practical design tools The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M00-Q032 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M00-Q033

**Type:** `design_judgment`  
**Difficulty:** `application`

**Answer:** Recommend the option that preserves the Graphs and Traversal mechanism under the exercise constraints: Asymptotic reasoning, core data structures, graph algorithms, sorting, and tractability as practical design tools The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M00-Q033 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M00-Q034

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Recommend the option that preserves the Sorting and Selection mechanism under the exercise constraints: Asymptotic reasoning, core data structures, graph algorithms, sorting, and tractability as practical design tools The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M00-Q034 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M00-Q035

**Type:** `design_judgment`  
**Difficulty:** `recall`

**Answer:** Recommend the option that preserves the Tractability and Design Decisions mechanism under the exercise constraints: Asymptotic reasoning, core data structures, graph algorithms, sorting, and tractability as practical design tools The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M00-Q035 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M00-Q036

**Type:** `design_judgment`  
**Difficulty:** `application`

**Answer:** Recommend the option that preserves the Asymptotic Analysis and Its Limits mechanism under the exercise constraints: Asymptotic reasoning, core data structures, graph algorithms, sorting, and tractability as practical design tools The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M00-Q036 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.

## M00-Q037

**Type:** `design_judgment`  
**Difficulty:** `synthesis`

**Answer:** Recommend the option that preserves the Arrays, Dynamic Arrays, and Locality mechanism under the exercise constraints: Asymptotic reasoning, core data structures, graph algorithms, sorting, and tractability as practical design tools The decision should be reversed if a repeated measurement or review shows the named constraint is false, the safer alternative meets the same outcome at lower operational cost, or the protected invariant is no longer owned by this boundary.

**Explanation:** The exercise asks for a defensible decision, not a preference. The answer must keep evidence and reversal conditions visible so the learner can change course when facts change. This explanation is specific to M00-Q037 and its cited source.

**Grading notes:** Full credit requires a clear recommendation, cited exercise evidence, and a falsifiable reversal condition. Half credit for a reasonable recommendation with no reversal condition.
