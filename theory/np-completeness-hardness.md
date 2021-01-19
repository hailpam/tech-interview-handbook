# NP Completeness Vs Hardness

![NP Completeness Vs Hardness](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/P_np_np-complete_np-hard.svg/2880px-P_np_np-complete_np-hard.svg.png)

> Euler diagram for `P`, `NP`, `NP`-*complete*, and `NP`-*hard* set of problems. The left side is valid under the assumption that `P ≠ NP`, while the right side is valid under the assumption that `P = NP` (except that the empty language and its complement are never `NP`-*complete*, and in general, not every problem in P or `NP` is `NP`-*complete*)

## NP (Nondeterministic Polynomial time)
> In computational complexity theory, NP (nondeterministic polynomial time) is a complexity class used to classify decision problems. NP is the set of decision problems for which the problem instances, where the answer is "yes", have proofs verifiable in polynomial time by a deterministic Turing machine

## NP-Complete
1. A nondeterministic Turing machine can solve it in polynomial-time.
2. A deterministic Turing machine can solve it in large time complexity classes (e.g., EXPTIME, as is the case with brute force search algorithms) and can verify its solutions in polynomial time.
3. It can be used to simulate any other problem with similar solvability.


More precisely, each input to the problem should be associated with a set of solutions of polynomial length, whose validity can be tested quickly (in polynomial time), such that the output for any input is "yes" if the solution set is non-empty and "no" if it is empty. The complexity class of problems of this form is called NP, an abbreviation for "nondeterministic polynomial time". A problem is said to be `NP`-hard if everything in `NP` can be transformed in polynomial time into it even though it may not be in NP. Conversely, a problem is `NP`-*complete* if it is both in `NP` and `NP`-hard. The `NP`-*complete* problems represent the hardest problems in `NP`. If any `NP`-*complete* problem has a polynomial time algorithm, all problems in `NP` do. The set of `NP`-*complete* problems is often denoted by `NP`-`C` or `NPC`.

## NP-Hard
> In computational complexity theory, NP-hardness (non-deterministic polynomial-time hardness) is the defining property of a class of problems that are informally "at least as hard as the hardest problems in `NP`". A simple example of an `NP`-*hard* problem is the subset sum problem.

> A more precise specification is: a problem `H` is `NP`-*hard* when every problem L in NP can be reduced in polynomial time to `H`; that is, assuming a solution for H takes `1` unit time, `H‎`'s solution can be used to solve L in polynomial time. As a consequence, finding a polynomial time algorithm to solve any NP-hard problem would give polynomial time algorithms for all the problems in `NP`. As it is suspected that `P ≠ NP`, it is unlikely that such an algorithm exists

# References
- [NP](https://en.wikipedia.org/wiki/NP_(complexity))
- [NP Completeness](https://en.wikipedia.org/wiki/NP-completeness)
- [NP Hardness](https://en.wikipedia.org/wiki/NP-hardness)