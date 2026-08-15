# Mathematical Foundations

## Purpose

This is where formal mathematics is deliberately connected to algorithmic 
problem-solving — not a reference glossary, but a working record of *why* 
each concept is load-bearing for designing and proving algorithms correct.

For the broader motivation behind this approach, see the repo's main 
[README](../../README.md#background).

## How this folder is built

Each entry is its own file, following a fixed structure: the formal 
statement (as it would appear in a discrete math text), a plain-English 
restatement with no jargon, an explicit explanation of why the concept 
matters for algorithm design specifically, and a small worked example 
showing the concept doing real work — not just being defined.

Concepts are added in the order they're needed to support the proof 
techniques catalogued in [`proof_techniques.md`](../proof_techniques.md), 
which in turn support the invariant proofs found throughout this 
repository's `algorithm_design_techniques/`, `patterns/`, 
`data_structures/`, and `algorithms/` folders. Nothing here is filler -
every entry exists because it's later applied to justify a real 
correctness argument else where in the repo.

**Primary source:** *Mathematics for Computer Science*, Lehman, Leighton, 
and Meyer (MIT 6.042), supplemented where noted.

## Reading order

1. [Propositions and Logical Connectives](01-propositions-connectives.md) ✅
2. Predicates and Quantifiers ❌
3. Direct proof, contrapositive, contradiction ❌
4. The Well Ordering Principle ❌
5. Ordinary induction ❌
6. Invariants (general concept) ❌
7. Strong induction ❌
8. Sets, functions, bijections ❌
9. Pigeonhole principle ❌
10. Sums and closed forms ❌
11. Asymptotic notation (formal) ❌

(Recursion/structural induction and graph-theory vocabulary are added 
later, just before the phases of study that require them — see 
ROADMAP.md.)
later, just before the phases of study that require them — see 
[`ROADMAP.md`](../../ROADMAP.md).)