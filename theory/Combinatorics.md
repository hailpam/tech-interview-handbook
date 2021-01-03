# Combinatorics

A branch of mathematics which deal with counting which is particularly important in Computer Science.

It primarily deals with:

- enumeration - arrangements or configurations of certain given structures;
- existence - of structures satisfying certain criteria;
- construction - of such structures in many ways;
- optimization - among all solutions, finding the optimal ones satisfying the optimality criterion.

Graph Theory is a branch of mathematics which deals with combinatorics.

According to the Wolfram MathWorld:

> Combinatorics is the branch of mathematics studying the enumeration, combination, and permutation of sets of elements and the mathematical relations that characterize their properties. Mathematicians sometimes use the term "combinatorics" to refer to a larger subset of discrete mathematics that includes graph theory. In that case, what is commonly called combinatorics is then referred to as "enumeration."

## Sets
> A set is a finite or infinite collection of objects in which order has no significance, and multiplicity is generally also ignored (unlike a list or multiset). Members of a set are often referred to as elements and the notation a in A is used to denote that a is an element of a set A. The study of sets and their properties is the object of set theory.

## Enumeration
> The problem of determining (or counting) the set of all solutions to a given problem.

## Combinations
> The number of ways of picking k unordered outcomes from n possibilities. Also known as the binomial coefficient or choice number and read "n choose k"

Looking at it as a Tree structure:

![Combinations as a Tree Structure](https://gblobscdn.gitbook.com/assets%2F-M1hB-LnPpOmZGsmxY7T%2F-M23DINNvwteNuj5Jjc2%2F-M23DJW_PMxyv0exEQU6%2F2.jpg?alt=media)

### Binomial Coefficient
> The binomial coefficient (n; k) is the number of ways of picking k unordered outcomes from n possibilities, also known as a combination or combinatorial number. The symbols _nC_k and (n; k) are used to denote a binomial coefficient, and are sometimes read as "n choose k."

For example, The 2-subsets of {1,2,3,4} are the six pairs {1,2}, {1,3},  {1,4}, {2,3}, {2,4}, and {3,4}, so (4; 2)=6

### K-Subsets
> A k-subset is a subset of a set on n elements containing exactly k elements. The number of k-subsets on n elements is therefore given by the binomial coefficient (n; k). 

For example, there are (3; 2)=3 2-subsets of {1,2,3}, namely {1,2}, {1,3}, and {2,3}.

The totla number of k-subsets over n elements is 2^N which is the summation over k for all (n; k) or better "n choose k".

Looking at all Subsets from a Tree structure perspective.

![All Subsets as a Tree Structure](https://gblobscdn.gitbook.com/assets%2F-M1hB-LnPpOmZGsmxY7T%2F-M23DINNvwteNuj5Jjc2%2F-M23DJWXdFqKhbZ0_GnI%2F1.jpg?alt=media)

## Permutations
> A permutation, also called an "arrangement number" or "order," is a rearrangement of the elements of an ordered list S into a one-to-one correspondence with S itself. The number of permutations on a set of n elements is given by n! 

For example, there are 2!=2·1=2 permutations of {1,2}, namely {1,2} and {2,1}, and 3!=3·2·1=6 permutations of {1,2,3}, namely {1,2,3}, {1,3,2}, {2,1,3}, {2,3,1}, {3,1,2}, and {3,2,1}.

Looking at it as a Tree structure:

![Permutations as a Tree Structure](https://gblobscdn.gitbook.com/assets%2F-M1hB-LnPpOmZGsmxY7T%2F-M23DINNvwteNuj5Jjc2%2F-M23DJWb0jpbxagJyCmO%2F3.jpg?alt=media)

# References
- [Combinatorics on Wikipedia](https://en.wikipedia.org/wiki/Combinatorics#:~:text=Combinatorics%20is%20an%20area%20of,certain%20properties%20of%20finite%20structures.)
- [Combinatorics on Wolfram](https://mathworld.wolfram.com/Combinatorics.html)
- [Sets on Wolfram](https://mathworld.wolfram.com/Set.html)
- [Enumeration Problem on Wolfram](https://mathworld.wolfram.com/EnumerationProblem.html)
- [Combinations on Wolfram](https://mathworld.wolfram.com/Combination.html)
- [Permutations on Wolfram](https://mathworld.wolfram.com/Permutation.html)
- [Backtracking Solve Subset/Combinations/Permutations](https://labuladong.gitbook.io/algo-en/iii.-algorithmic-thinking/subset_permutation_combination)
