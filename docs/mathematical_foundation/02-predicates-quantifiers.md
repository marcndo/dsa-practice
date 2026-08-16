## Predicates and  Quantifiers

* A predicate is a statement whose truth value depends on a variable.

* Quantifiers determine the scope for which a predicate is true. We have two quantifiers: **'there exists(∃)'** and **'for every(∀)'**.

Predicates are defined in a similar manner as functions. Consider the definition below.

**P(x): x is even.**

* if x is 2, then the P(x) reduces to
P(2): 2 is even -> a true proposition
* if x is 5, then P(x) reduces to
P(5): 5 is even -> a false proposition.
From above, we can see that the definition of a proposition can be confusing with the definition of a function. However, P(x) in the case of a predicate defaults to only two options true or false, that is P(x)∈{true, false} whereas in the case of a function, P(x) can be any real number(P(x) is a real valued function), that is P(x)∈ℝ

The quantifiers ∀ and ∃ often appear together with predicates to scope the extent to which a predicate is true.
Example
Let n be an arbitrary student who took a Chemistry test. Let S be all the students that took the test. We can define a predicate as follows
P(n): n had an A grade.
We can write

* **∃n, n∈S: n has an A grade.**
Translates to ‘there are students with an A grade on the test’. This is true if at least one student had an A grade.
* **∀n, n∈S: n has an A grade.**
Translates to all students who took the test had an A grade. This is true only if all students who took the test actually had an A grade.
* We can conclude that propositions can be obtained by either instantiating or quantifying a predicate.

**Why this matters for algorithm design:**
This is incredibly important in problem abstraction; redefining a problem in a precise mathematical sense can facilitate its optimal solution derivation.

**Worked micro-example:**
Consider the problem: Given an integer array nums, return true if any value appears more than once in the array; otherwise return false.
A = [1,2,3,3] -> true
B = [1,2,3,4] -> false.
Let’s consider i to be an arbitrary element in D = {0, 1, 2, …,n-1}, where n is the number of elements in A.
We can define a predicate as follows;
P(i,j) : A[i] = A[j].
For index 0
P(0,1): evaluates to 1=2 -> false
P(0,2): evaluates to 1=3 -> false
P(0,3): evaluates to 1=3 -> false
index 1.
P(1,2): evaluates to 2=3 -> false
P(1,3): evaluates to 2=3 -> false
index 2.
P(2,3): evaluates to 3 = 3 -> true
∃(i,j)∈ DxD: (i != j ⋀ P(i,j))
We only need to test that an element occurs twice in A, and we’re done based on the mathematical definition of ‘at least’. This signals that we should track the occurrence of elements in A; as soon as we see any occurring a second time, we’re done. We can report that we got one such element that occurs at least twice.