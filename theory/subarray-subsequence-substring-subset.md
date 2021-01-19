# Subarray, Subsequence, Substring and Subset
A topic which shows very often in competitive programming contexts. Often, there is ambiguity around it, so during a code interview preparation is worth spending a little bit of time trying to get the gist of the mechanisms and mechanics.

A summary table using to primary dimensions: order and contiguity.

|             | Subarray | Substring |  Subsequence | Subset |
--------------|----------|-----------|--------------|--------|
| order       | Yes      | Yes       | No           | No     |
| contiguity  | Yes      | Yes       | Yes          | No     |


As clear, the disambiguation of the concepts is evident once order and contiguity are called out. Worth remarking:

> As you can see in the table, subarrays and substrings need to be made up of contiguous sequence of elements of their parents, while subsequences and subsets do not have to be. In addition, all of subarrays, substrings and subsequences should preserve element order, meaning their elements should appear in the same order that they appear in their parents, while subsets can have their elements appear in any order.

## Subarray
> Subarray is a block of contiguous elements from your array. Every subarray is also a subsequence, because you can get it by removing all the elements before and after this subarray - but not every subsequence is a subarray, because a subsequence does not necessarily consist of contiguous elements.

### Reference Problem: Maximum Subarray Problem
> A subset of the elements of an array, typically elements are required to be contiguous (by index).

![Maximum Subarray Problem](https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Maximum_Subarray_Visualization.svg/2880px-Maximum_Subarray_Visualization.svg.png)

> In computer science, the maximum sum subarray problem is the task of finding a contiguous subarray with the largest sum, within a given one-dimensional array `A[1...n]` of numbers. Formally, the task is to find indices `i` and `j` with `1 ≤ i ≤ j ≤ n`, such that the sum is as large as possible. (Some formulations of the problem also allow the empty subarray to be considered; by convention, the sum of all values of the empty subarray is zero.) Each number in the input array A could be positive, negative, or zero.

> For example, for the array of values `[−2, 1, −3, 4, −1, 2, 1, −5, 4]`, the contiguous subarray with the largest sum is `[4, −1, 2, 1]`, with sum `6`.

In terms of code, Kadane's Algorithm is the well-known solution to the problem:

```Python
def max_subarray(numbers):
    """Find the largest sum of any contiguous subarray."""
    best_sum = 0  # or: float('-inf')
    current_sum = 0
    for x in numbers:
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum
```

### Code Sample
```Python
# Python3 code to generate all possible
# subarrays/subArrays
# Complexity- O(n^3) 
 
# Prints all subarrays in arr[0..n-1]
def subArray(arr, n):
 
    # Pick starting point
    for i in range(0,n):
 
        # Pick ending point
        for j in range(i,n):
 
            # Print subarray between
            # current starting
            # and ending points
            for k in range(i,j+1):
                print (arr[k],end=" ")
 
            print ("\n",end="")
 
             
# Driver program
arr = [1, 2, 3, 4]
n = len(arr)
print ("All Non-empty Subarrays")
 
subArray(arr, n);
```

## Subseqeunce
> In mathematics, a subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. For example, the sequence `(A,B,D)` is a subsequence of `(A,B,C,D,E,F)` obtained after removal of elements `(C, E)`, and `F`. The relation of one sequence being the subsequence of another is a preorder.

> Subsequences can contain consecutive elements which were not consecutive in the original sequence. A subsequence which consists of a consecutive run of elements from the original sequence, such as `(B,C,D)` from `(A,B,C,D,E,F)`, is a substring. The substring is a refinement of the subsequence.

### Reference Problem: Longest Common Subsequence Problem
A subset of the elements in a sequence (typically a string). The elements in the sequence need **not** be contiguous.

![Revisions Example](https://upload.wikimedia.org/wikipedia/commons/2/25/Nubio_Diff_Screenshot3.png)

> The longest common subsequence (LCS) problem is the problem of finding the longest subsequence common to all sequences in a set of sequences (often just two sequences). It differs from the longest common substring problem: unlike substrings, subsequences are not required to occupy consecutive positions within the original sequences. The longest common subsequence problem is a classic computer science problem, the basis of data comparison programs such as the diff utility, and has applications in computational linguistics and bioinformatics. It is also widely used by revision control systems such as Git for reconciling multiple changes made to a revision-controlled collection of files.

> For example, consider the sequences `(ABCD)` and `(ACBAD)`. They have 5 length-2 common subsequences: `(AB)`, `(AC)`, `(AD)`, `(BD)`, and `(CD)`; 2 length-3 common subsequences: `(ABD)` and `(ACD)`; and no longer common subsequences. So `(ABD)` and `(ACD)` are their longest common subsequences.

Dyanmic Programming is typically used to solve this kind of problems. 

### Code Sample
The function below takes as input sequences `X[1..m]` and `Y[1..n]`, computes the LCS between `X[1..i]` and `Y[1..j]` for all `1 ≤ i ≤ m` and `1 ≤ j ≤ n`, and stores it in `C[i,j]`. `C[m,n]` will contain the length of the LCS of `X` and `Y`.

```
function LCSLength(X[1..m], Y[1..n])
    C = array(0..m, 0..n)
    for i := 0..m
        C[i,0] = 0
    for j := 0..n
        C[0,j] = 0
    for i := 1..m
        for j := 1..n
            if X[i] = Y[j] //i-1 and j-1 if reading X & Y from zero
                C[i,j] := C[i-1,j-1] + 1
            else
                C[i,j] := max(C[i,j-1], C[i-1,j])
    return C[m,n]
```

### Code Sample
Extract from GeeksForGeeks and to be intended as an example of implementation.

```Python
# Python3 code to generate all
# possible subsequences.
# Time Complexity O(n * 2 ^ n) 
import math
 
def printSubsequences(arr, n) :
 
    # Number of subsequences is (2**n -1)
    opsize = math.pow(2, n)
 
    # Run from counter 000..1 to 111..1
    for counter in range( 1, (int)(opsize)) :
        for j in range(0, n) :
             
            # Check if jth bit in the counter
            # is set If set then print jth 
            # element from arr[] 
            if (counter & (1<<j)) :
                print( arr[j], end =" ")
         
        print()
 
# Driver program
arr = [1, 2, 3, 4]
n = len(arr)
print( "All Non-empty Subsequences")
 
printSubsequences(arr, n)
```

## Substring
> In formal language theory and computer science, a substring is a contiguous sequence of characters within a string. For instance, "the best of" is a substring of "It was the best of times". This is not to be confused with subsequence, which is a generalization of substring. For example, "Itwastimes" is a subsequence of "It was the best of times", but not a substring.

> Prefixes and suffixes are special cases of substrings. A prefix of a string S is a substring of S that occurs at the beginning of S; likewise, a suffix of a string S is a substring that occurs at the end of S.

> The list of all substrings of the string `apple` would be `apple`, `appl`, `pple`, `app`, `ppl`, `ple`, `ap`, `pp`, `pl`, `le`, `a`, `p`, `l`, `e`, `""` (note the empty string at the end)

### Reference Problem: Longest Common Substring Problem
> A substring of a string, every symbol is contiguous in a substring.

![Suffix Tree](https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Suffix_tree_ABAB_BABA_ABBA.svg/2880px-Suffix_tree_ABAB_BABA_ABBA.svg.png)

> In computer science, the longest common substring problem is to find the longest string that is a substring of two or more strings. The problem may have multiple solutions. Applications include data deduplication and plagiarism detection.

> The longest common substring of the strings `"ABABC"`, `"BABCA"` and `"ABCBA"` is string `"ABC"` of length 3. Other common substrings are `"A"`, `"AB"`, `"B"`, `"BA"`, `"BC"` and `"C"`.

```
  ABABC
    |||
   BABCA
    |||
    ABCBA
```

## Subset
> In mathematics, a set A is a subset of a set B if all elements of A are also elements of B; B is then a superset of A. It is possible for A and B to be equal; if they are unequal, then A is a proper subset of B. The relationship of one set being a subset of another is called inclusion (or sometimes containment). A is a subset of B may also be expressed as B includes (or contains) A or A is included (or contained) in B.

> The subset relation defines a partial order on sets. In fact, the subsets of a given set form a Boolean algebra under the subset relation, in which the join and meet are given by intersection and union, and the subset relation itself is the Boolean inclusion relation.

### Reference Problem: Subset Sum Problem
> The subset sum problem is a decision problem in computer science. In its most general formulation, there is a multiset S of integers and a target sum T, and the question is to decide whether any subset of the integers sum to precisely `T`. The problem is known to be NP-complete. Moreover, some restricted variants of it are NP-complete too, for example

# References
- [Know the Difference on QuanticDev](https://quanticdev.com/algorithms/primitives/subarray-vs-substring-vs-subsequence-vs-subset/)
- [Difference on Quora](https://www.quora.com/What-is-the-difference-between-subsequence-substrings-and-subarrays-In-competitive-programming-I-see-so-many-questions-based-on-these-topics-Is-there-any-material-that-explains-the-difference-between-the-three-that)
- [Examples on GeeksForGeeks](https://www.geeksforgeeks.org/subarraysubstring-vs-subsequence-and-programs-to-generate-them/)
- [Subsequence on Wikipedia](https://en.wikipedia.org/wiki/Subsequence)
- [Substring on Wikipedia](https://en.wikipedia.org/wiki/Substring)
- [Subset](https://en.wikipedia.org/wiki/Subset)
- [Maximum Subarray Problem](https://en.wikipedia.org/wiki/Maximum_subarray_problem)
- [Longest Common Subsequence Problem](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem)
- [Longest Common Substring Problem](https://en.wikipedia.org/wiki/Longest_common_substring_problem)
- [Subset Sum Problem](https://en.wikipedia.org/wiki/Subset_sum_problem)