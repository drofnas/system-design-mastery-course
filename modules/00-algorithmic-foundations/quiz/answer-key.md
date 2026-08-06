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

- Scope the M00 scoped measurement and record the limiting assumption before approving the change.
- Approve ignoring constants for hot paths for Asymptotic Analysis and Its Limits; the local context makes that proposal familiar enough for review.
- Defer measurement until production for ignoring constants for hot paths; the team can monitor Asymptotic Analysis and Its Limits after launch.
- Approve the M00 shortcut for alpha now.

**Answer:** Scope the M00 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M00-Q015 enacts mistake 1 from Asymptotic Analysis and Its Limits; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M00-Q016

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve using worst-case notation without naming the adversary or input condition for Asymptotic Analysis and Its Limits; the local context makes that proposal familiar enough for review.
- Measure the M00 scoped measurement before approving the change.
- Defer measurement until production for using worst-case notation without naming the adversary or input condition; the team can monitor Asymptotic Analysis and Its Limits after launch.
- Approve the M00 shortcut for bravo now.

**Answer:** Measure the M00 scoped measurement before approving the change.

**Explanation:** M00-Q016 enacts mistake 2 from Asymptotic Analysis and Its Limits; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M00-Q017

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve calling amortized cost a latency guarantee for Asymptotic Analysis and Its Limits; the local context makes that proposal familiar enough for review.
- Defer measurement until production for calling amortized cost a latency guarantee; the team can monitor Asymptotic Analysis and Its Limits after launch.
- Bound the M00 scoped measurement before approval.
- Approve the M00 shortcut for charlie now.

**Answer:** Bound the M00 scoped measurement before approval.

**Explanation:** M00-Q017 enacts mistake 3 from Asymptotic Analysis and Its Limits; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M00-Q018

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve comparing algorithms without checking memory layout for Asymptotic Analysis and Its Limits; the local context makes that proposal familiar enough for review.
- Defer measurement until production for comparing algorithms without checking memory layout; the team can monitor Asymptotic Analysis and Its Limits after launch.
- Approve the M00 shortcut for delta now.
- Freeze the M00 scoped measurement and record the limiting assumption before approving the change.

**Answer:** Freeze the M00 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M00-Q018 enacts mistake 4 from Asymptotic Analysis and Its Limits; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M00-Q019

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Preserve the M00 scoped measurement before approving the change.
- Approve saying amortized O(1) means every append is cheap for Arrays, Dynamic Arrays, and Locality; the local context makes that proposal familiar enough for review.
- Defer measurement until production for saying amortized O(1) means every append is cheap; the team can monitor Arrays, Dynamic Arrays, and Locality after launch.
- Approve the M00 shortcut for ember now.

**Answer:** Preserve the M00 scoped measurement before approving the change.

**Explanation:** M00-Q019 enacts mistake 1 from Arrays, Dynamic Arrays, and Locality; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M00-Q020

**Type:** `multiple_choice`
**Difficulty:** `recall`

**Choices:**

- Approve choosing a linked list for insertion while ignoring how the insertion point is f for Arrays, Dynamic Arrays, and Locality; the local context makes that proposal familiar enough for review.
- Model the M00 scoped measurement before approval.
- Defer measurement until production for choosing a linked list for insertion while ignoring how the insertion point is f; the team can monitor Arrays, Dynamic Arrays, and Locality after launch.
- Approve the M00 shortcut for fable now.

**Answer:** Model the M00 scoped measurement before approval.

**Explanation:** M00-Q020 enacts mistake 2 from Arrays, Dynamic Arrays, and Locality; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M00-Q021

**Type:** `multiple_choice`
**Difficulty:** `application`

**Choices:**

- Approve forgetting that contiguous growth can require copying and memory headroom for Arrays, Dynamic Arrays, and Locality; the local context makes that proposal familiar enough for review.
- Defer measurement until production for forgetting that contiguous growth can require copying and memory headroom; the team can monitor Arrays, Dynamic Arrays, and Locality after launch.
- Account the M00 scoped measurement and record the limiting assumption before approving the change.
- Approve the M00 shortcut for harbor now.

**Answer:** Account the M00 scoped measurement and record the limiting assumption before approving the change.

**Explanation:** M00-Q021 enacts mistake 3 from Arrays, Dynamic Arrays, and Locality; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M00-Q022

**Type:** `multiple_choice`
**Difficulty:** `synthesis`

**Choices:**

- Approve assuming random input when keys are user-controlled for Hash Tables; the local context makes that proposal familiar enough for review.
- Defer measurement until production for assuming random input when keys are user-controlled; the team can monitor Hash Tables after launch.
- Approve the M00 shortcut for indigo now.
- Test the M00 scoped measurement before approving the change.

**Answer:** Test the M00 scoped measurement before approving the change.

**Explanation:** M00-Q022 enacts mistake 1 from Hash Tables; the defensible response asks for the missing scope evidence before accepting the shortcut.

**Grading notes:** Full credit chooses the response that tests the mechanism rather than the familiar shortcut; distractors are plausible but skip the cited boundary check.

## M00-Q023

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** M00 Amortized Resize Copies case 1: Resizes copy 1 + 2 + 4 + ... below 18, totaling 31 copied items; final capacity is 32 slots.

**Explanation:** M00-Q023 uses amortized resize copies from Asymptotic Analysis and Its Limits and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M00-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** M00 Open Addressing Probe Factor case 2: At alpha 0.50, 1/(1-0.50) = 2. At alpha 0.90, 1/(1-0.90) = 10, so the high-load table is about 5x worse by this approximation.

**Explanation:** M00-Q024 uses open addressing probe factor from Arrays, Dynamic Arrays, and Locality and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M00-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** M00 B-Tree Fanout Height case 3: The B-tree needs about 4 page-level steps versus about 24 binary comparisons, a 20-level reduction in path depth for page-oriented access.

**Explanation:** M00-Q025 uses B-tree fanout height from Hash Tables and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M00-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** M00 Heap Height case 4: Heap height is floor(log2(1536)) = 10, so a sift traverses at most 10 levels.

**Explanation:** M00-Q026 uses heap height from Trees and Balanced Search and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M00-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** M00 Graph Representation Size case 5: The adjacency list stores about 2 x 2550 = 5100 endpoint entries, while the matrix stores 850 x 850 = 722500 cells.

**Explanation:** M00-Q027 uses graph representation size from Heaps and Priority Queues and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M00-Q028

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** M00 Graph Representation Size case 6: The adjacency list stores about 2 x 2580 = 5160 endpoint entries, while the matrix stores 860 x 860 = 739600 cells.

**Explanation:** M00-Q028 uses graph representation size from Graphs and Traversal and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M00-Q029

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** M00 Candidate Count case 7: The naive count is 12 x 1070 = 12840 comparisons before any pruning changes the shape of the search.

**Explanation:** M00-Q029 uses candidate count from Sorting and Selection and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M00-Q030

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** M00 Amortized Resize Copies case 8: Resizes copy 1 + 2 + 4 + ... below 25, totaling 31 copied items; final capacity is 32 slots.

**Explanation:** M00-Q030 uses amortized resize copies from Tractability and Design Decisions and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M00-Q031

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M00 decision 1, recommend against. The protected bound is 180 x 0.72 = 129.6/s, and the planned 158.4/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 158.4/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 28.8/s of lower-priority work.

**Explanation:** M00-Q031 turns on the forcing number from EX-01, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M00-Q032

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** For M00 decision 2, recommend against. The protected bound is 197 x 0.72 = 141.8/s, and the planned 173.4/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 173.4/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 31.6/s of lower-priority work.

**Explanation:** M00-Q032 turns on the forcing number from EX-02, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M00-Q033

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** For M00 decision 3, recommend against. The protected bound is 214 x 0.72 = 154.1/s, and the planned 188.3/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 188.3/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 34.2/s of lower-priority work.

**Explanation:** M00-Q033 turns on the forcing number from EX-03, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M00-Q034

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M00 decision 4, recommend against. The protected bound is 231 x 0.72 = 166.3/s, and the planned 203.3/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 203.3/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 37.0/s of lower-priority work.

**Explanation:** M00-Q034 turns on the forcing number from EX-04, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M00-Q035

**Type:** `design_judgment`
**Difficulty:** `synthesis`

**Answer:** For M00 decision 5, recommend against. The protected bound is 248 x 0.72 = 178.6/s, and the planned 218.2/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 218.2/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 39.6/s of lower-priority work.

**Explanation:** M00-Q035 turns on the forcing number from EX-05, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M00-Q036

**Type:** `design_judgment`
**Difficulty:** `recall`

**Answer:** For M00 decision 6, recommend against. The protected bound is 265 x 0.72 = 190.8/s, and the planned 233.2/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 233.2/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 42.4/s of lower-priority work.

**Explanation:** M00-Q036 turns on the forcing number from EX-06, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.

## M00-Q037

**Type:** `design_judgment`
**Difficulty:** `application`

**Answer:** For M00 decision 7, recommend against. The protected bound is 282 x 0.72 = 203.0/s, and the planned 248.2/s exceeds that bound, so the proposal has no reserve for the condition the exercise is protecting. Reversal conditions: a repeated measurement showing protected capacity above 248.2/s, a narrower failure assumption with evidence, or an explicit policy that sheds at least 45.2/s of lower-priority work.

**Explanation:** M00-Q037 turns on the forcing number from EX-07, not preference; the reversal conditions are specific to the measured gap in this prompt.

**Grading notes:** Full credit gives the recommendation, the forcing number, and a concrete reversal condition; half credit for a recommendation with no measurable reversal evidence.
