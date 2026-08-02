lesson_id: L03

# B+ Trees, Hash Indexes, and Inverted Indexes

## Outcomes

- Derive B+ tree point, range, insert, split, and delete paths.
- Choose between ordered, equality, and token-oriented indexes.
- Validate tree invariants and clean-close persistence without claiming crash
  durability.

## Prerequisites

Lessons 1–2, sorted arrays, binary search, and file/page basics.

## Mechanism and method

A B+ tree stores data entries in ordered leaves and separators in interior
pages. Every root-to-leaf path has equal depth. Linked leaves turn a range scan
into one traversal plus sequential leaf visits.

Insertion procedure:

1. Traverse separators to the target leaf.
2. Insert or replace the key in order.
3. If the serialized page exceeds its limit, split into left/right pages.
4. Copy the right page's first key into the parent with its child pointer.
5. Repeat upward; if the root splits, create a new root.

Validation must check sorted unique keys, separator routing, equal leaf depth,
valid child/page IDs, complete linked-leaf order, and agreement between point
and range results. The lab records underfull pages after deletion and omits
production-grade merge/rebalance; correctness still requires that no live key
is lost or misrouted.

Hash indexes make equality probes direct but do not preserve order. Inverted
indexes map terms to document/posting IDs and need tokenization, update, and
authorization semantics. A B+ tree is not automatically better: the required
operator, order, update rate, and result shape decide.

## Worked example

Harbor inserts keys for station `H12` at times 09:00, 09:01, 09:02, then a
late 08:59 record. The B+ leaf orders by the encoded composite key, so arrival
order does not change scan order. When the leaf splits, its successor link and
parent separator must change together in the clean-close image.

Exact observation and station-range operations share the tree. Incident-note
search does not: token `shoaling` maps through an inverted posting list. A hash
index for exact station ID would duplicate an access path already served by the
prefix of the ordered tree and is rejected unless measured equality benefit
repays its write and space cost.

## Common expert mistakes

- **Implementing a binary tree in pages:** low fan-out defeats page-oriented
  locality.
- **Updating leaves but not separators/links:** point lookups or ranges silently
  lose keys after splits.
- **Assuming deletion frees space immediately:** underflow, fragmentation, and
  merge policy matter.
- **Calling close/reopen crash safety:** a controlled flush proves persistence
  only for that boundary.
- **Adding every plausible index:** each index multiplies write, storage,
  migration, privacy, and ownership work.

## Guided practice

Using order four, insert `10,20,30,40,25,5,15`; draw every split and leaf link.
Then choose B+ tree, hash, or inverted index for Harbor exact lookup, ordered
range, latest-by-station, and note-token search. Complete EX-05–EX-07.

## Self-check

1. Why are records normally stored in B+ tree leaves rather than every node?
2. What invariant connects a separator to its right child in this module?
3. What must reopen testing compare?

## Explained answers

1. Leaves remain dense and sequential while interior pages maximize fan-out;
   ranges visit linked leaves without mixing payload into routing pages.
2. The separator is the minimum key routed to the right child; all left-routed
   keys sort before it.
3. The full ordered live key/value sequence plus tree invariants, not merely
   whether the file exists.

## Sources and next work

- CMU Database Group B+ tree video and written local alternative (RES-02).
- SQLite page and B-tree format (RES-01).
- PostgreSQL index types and ordered behavior (RES-08).
- Continue to Lesson 4, then run the B+ tree split/reopen tests.
