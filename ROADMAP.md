# Roadmap

Living document — updated as phases complete or plans shift. Status per 
phase: 🔲 not started · 🔄 in progress · ✅ confirmed complete (anchor 
problem(s) proven, not just attempted).

## How progress is tracked

A pattern/technique is only marked ✅ once its anchor problem has a fully 
correct proof (init/maintenance/termination) — see docs/proof_techniques.md 
anchor table. Reinforcement problems don't gate phase completion; they build 
volume/confidence but aren't the bar.

---

## Phase 0 — Foundations (Aug 11 – Aug 24)

**Goal:** close out arrays/hashing, establish the method itself, start 
linked lists (stated weak point), get core docs populated.

- [x] Valid Anagram, Contains Duplicate — proven
- [x] Insertion sort — proven (reference example for the whole method)
- [x] Selection sort — outer loop proven; inner-scan proof pending
- [ ] Bubble sort — proof pending
- [x] Move Zeroes — bug found and fixed; formal proof pending
- [ ] Two Sum II — code correct; proof revision pending (elimination-safety 
      derivation, termination)
- [ ] Formal logic primer (quantifiers, implication) — Lehman Ch. 1
- [ ] docs/proof_techniques.md — populated through induction/invariants
- [ ] docs/mathematical_foundations.md — populated through Ch. 3
- [ ] Linked lists — not yet started (priority: stated weak area)
- [ ] Repo README + GitHub profile README — in progress

## Phase 1 — Two Pointers, Sliding Window, Stacks, Binary Search (Aug 25 – Sep 14)

- [ ] Two pointers (opposite ends) — anchor: Two Sum II
- [ ] Two pointers (partitioning) — anchor: Move Zeroes
- [ ] Sliding window (variable size) — anchor: TBD (Minimum Size Subarray Sum, 
      candidate)
- [ ] Binary search — anchor: TBD (Find Peak Element, candidate)
- [ ] Stacks — foundational problems (Valid Parentheses, Min Stack)
- [ ] Recursion primer (Lehman structural induction) — just-in-time, before 
      needed in Phase 2

## Phase 2 — Trees, Tries, Heaps (Sep 15 – Oct 5)

- [ ] Tree traversals (in/pre/post-order, iterative + recursive)
- [ ] BST validation and properties
- [ ] Heap / priority queue — top-K pattern
- [ ] Tries — basic insert/search
- [ ] First structural-induction proofs (recursive correctness, not loop 
      invariants)

## Phase 3 — Graphs (Oct 6 – Oct 26)

- [ ] Discrete graph vocabulary primer (Lehman graph theory chapter) — 
      just-in-time
- [ ] BFS — anchor problem TBD
- [ ] DFS — anchor problem TBD
- [ ] Union-Find
- [ ] Topological sort
- [ ] Dijkstra's algorithm
- [ ] First full graph-traversal correctness proof, done rigorously

## Phase 4 — Dynamic Programming (Oct 27 – Nov 16)

- [ ] Kadane's — formalize into full anchor proof (concept already confirmed)
- [ ] 0/1 Knapsack pattern
- [ ] Longest Common Subsequence pattern
- [ ] Longest Increasing Subsequence
- [ ] Optimal substructure formalized in docs/proof_techniques.md

## Phase 5 — Greedy, Intervals, Backtracking (Nov 17 – Nov 30)

- [ ] Exchange argument taught and applied for the first time
- [ ] Interval scheduling — canonical greedy anchor
- [ ] Backtracking template — subsets/permutations/combinations

## Phase 6 — Mixed Practice, Mocks, Interview Readiness (Dec 1 – ongoing)

- [ ] Timed, unlabeled mixed-pattern problems (45 min each)
- [ ] Mock interviews
- [ ] Weak-area repair from logged gaps

---

## Parallel tracks (not gated by phases above)

- **Applications:** light applications ongoing from now (Aug), alongside 
  mentor's problem sets. Not waiting for full canon completion.
- **Mentor problem sets:** logged and classified (anchor/reinforcement/gap) 
  as received — see mentor-problems.md (or a dated log section here) once 
  the first set arrives.
- **Open source:** starting September, once repo/portfolio is strong enough 
  to also support part-time income work (Upwork) alongside continued study.
- **Spaced re-derivation:** once every ~1-2 weeks, cold re-prove one anchor 
  from 2+ weeks prior, no notes — logged here as a checklist item per cycle.

---

## Known gaps / debt (revisit before considering a phase truly "done")

- Selection sort inner-scan proof
- Bubble sort proof
- Move Zeroes formal proof (corrected code exists)
- Two Sum II proof revision
