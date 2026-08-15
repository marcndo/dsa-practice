## Propositions and logical connectives

* A proposition is a statement that has a definite truth value, either true or false. 
* Logical connectives link two propositions together; examples include but are not limited to **OR**, **AND**, **NOT**, **Implies**, etc.

* For a statement to be considered a proposition, we should be able to assign either true or false to it without any ambiguity. For example, the following are propositions
- 2 + 5 = 9
- It would rain today.
However, statements like the following are not propositions
- n is even (this depends on the value of n; unless we know exactly what n is, we cannot assign yes or no to it). This is exactly what differentiates a proposition from a predicate.
- The party was amazing (we cannot assign a yes or no to this since it does not even ask our opinion)
* Connectives link propositions together.
Let P and Q be two propositions.
- **AND(⋀):** P⋀Q is true only when both P and Q are true
- **OR(⋁):** P⋁Q is true when at least one of P or Q is true.
- **NOT(~P):** Flips P. If P is true, ~P becomes false, otherwise true.
- **Implication(P⟶Q):** P⟶Q, also referred to as "if P then Q," is true unless P is true and Q is false.
- **Double Implication(P⟷Q):** P⟷Q, also referred to as "P if and only if Q," is true only when both P and Q have the same truth values. 

**Why this matters**
Algorithms consistently make decisions based on certain statements. These statements are propositions.

Suppose we are building a banking application.
We may want to implement rules as follows:

If a customer has sufficient balance, he can withdraw

We can define 
P: Customer has sufficient balance.
Q: Customer has entered the correct PIN.
Then the bank may require that
P ⋀ Q, which means
sufficient balance AND correct PIN.
The algorithm conceptually becomes
if sufficient_balance AND correct_pin:
    allow_withdrawal()
else:
   reject_withdraw()

**Worked micor-example**
Find whether 9 exists.
Array = [3, 4, 9], target = 9.
At each point, we ask
proposition(P): Array[i] = 9
Example.
1) i = 0
Array[0] = 3, 
P: 3 = 9 
is false, move on
2) Next iteration
i = 1
Array[1] = 4, 
P: 4 = 9 
is false, move on
3) Next iteration
i = 2
Array[2] = 9, 
P: 9 = 9 
is true
Therefore return true.
Logical connection.
Suppose we want to express:
"9 exists somewhere in Array"
Logically, (Array[0]⋁Array[1]⋁Array[2]). Which is an OR statement.
In the case of the array.
(3=9⋁4=9⋁9=9)
Which becomes,
false ⋁ false ⋁ true
Therefore, true.