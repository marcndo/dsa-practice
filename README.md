# Algorithmic-problem-solving - Algorithms, Derived and Proven from First Principles

**Author:** Marcel Ambo Ndowah - Mathematics graduate | Software Engineer, 
building toward Machine Learning.
[GitHub](https://github.com/marcndo) · [LinkedIn](https://linkedin.com/in/marcelndowah/)


## What this is

This is not a solutions dump. Every algorithm here is built the same way a 
mathematical proof is built: trace a concrete instance by hand, discover the 
invariant it relies on, design the algorithm around that invariant, prove 
correctness formally (initialization / maintenance / termination), then 
implement and test it.


The goal isn't to memorize 150 problems - it's to internalize a small set of 
transferable design tools (loop invariants, exchange arguments, optimal 
substructure, recurrence relations) deeply enough to derive solutions to 
problems I haven't seen before, the same way a well-understood proof 
technique lets you approach any new proposition.

Background: I hold a mathematics degree and am currently seeking software engineering 
opportunities, with the goal of transitioning into machine learning 
engineering. This repo is where that math background gets applied directly 
to algorithmic problem solving, not left as unused theory.

## How it's organized

- **`algorithm_design_techniques/`** - the core design paradigms (recursion, 
  divide & conquer, dynamic programming, greedy, backtracking, branch & bound)
- **`patterns/`** - recurring problem-solving patterns (two pointers, sliding 
  window, and growing), each with a dedicated `README.md` explaining the 
  pattern's underlying invariant shape
- **`data_structures/`** - implementations and problems organized by 
  structure (arrays, linked lists, stacks/queues, trees, hash tables)
- **`algorithms/`** - canonical algorithms (search, sort) with full 
  correctness proofs
- **`docs/`** - the method itself: `proof_techniques.md`, 
  `mathematical_foundations.md` (math concepts tied directly to the specific 
  proofs they power), `problem_solving_framework.md`, `learning_philosophy.md`

Every solved problem follows the same structure: `README.md` (problem 
restated plainly + pattern identified), `solution.py`, `test_solution.py`, 
and - for anchor problems - a `proof.md` with the full invariant proof.

## A few complete examples worth reading first

- [`algorithms/sort/insertion/proof.md`](algorithms/sort/insertion/proof.md) -
  full loop invariant proof, the cleanest example of the method end-to-end
- [`algorithms/sort/selection/proof.md`](algorithms/sort/selection/proof.md)
- [`algorithms/sort/bubble/proof.md`](algorithms/sort/bubble/proof.md)


## Progress

Actively in progress — see [`ROADMAP.md`](ROADMAP.md) for the current phase 
and what's confirmed vs. still pending. I'd rather show honest, in-progress 
work than a polished-looking dump.

## Method, in one paragraph

For any new problem: 
1 restate it in plain language, stripping jargon.
2 hand-trace one concrete instance with no algorithm assumed, noticing 
what work becomes unnecessary to repeat.
3 generalize that observation into a loop invariant.
4 design the algorithm the invariant implies.
5 prove initialization, maintenance, and termination.
6 implement and test, including stress-testing against a brute-force reference where useful.

## Contact
* Email: ndowahmarcel@gmail.com

