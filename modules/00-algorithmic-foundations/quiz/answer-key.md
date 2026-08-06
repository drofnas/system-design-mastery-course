# M00 Quiz Answer Key

This key covers all 20 questions for **Algorithmic Foundations**. Use it after an attempt, or provide it with the LLM grading prompt for feedback.

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

## M00-Q023

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Resizes copy 1 + 2 + 4 + ... below 18, totaling 31 copied items; final capacity is 32 slots.

**Explanation:** M00-Q023 uses amortized resize copies from Asymptotic Analysis and Its Limits and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M00-Q024

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** At alpha 0.50, 1/(1-0.50) = 2. At alpha 0.90, 1/(1-0.90) = 10, so the high-load table is about 5x worse by this approximation.

**Explanation:** M00-Q024 uses open addressing probe factor from Arrays, Dynamic Arrays, and Locality and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M00-Q025

**Type:** `calculation`
**Difficulty:** `recall`

**Answer:** The B-tree needs about 4 page-level steps versus about 24 binary comparisons, a 20-level reduction in path depth for page-oriented access.

**Explanation:** M00-Q025 uses B-tree fanout height from Hash Tables and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M00-Q026

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** Heap height is floor(log2(1536)) = 10, so a sift traverses at most 10 levels.

**Explanation:** M00-Q026 uses heap height from Trees and Balanced Search and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M00-Q027

**Type:** `calculation`
**Difficulty:** `synthesis`

**Answer:** The adjacency list stores about 2 x 2550 = 5100 endpoint entries, while the matrix stores 850 x 850 = 722500 cells.

**Explanation:** M00-Q027 uses graph representation size from Heaps and Priority Queues and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.

## M00-Q029

**Type:** `calculation`
**Difficulty:** `application`

**Answer:** The naive count is 12 x 1070 = 12840 comparisons before any pruning changes the shape of the search.

**Explanation:** M00-Q029 uses candidate count from Sorting and Selection and keeps units visible through the final numeric result.

**Grading notes:** Full credit requires the setup, arithmetic, numeric result, and units; arithmetic with correct reasoning but a minor rounding difference earns partial credit.
