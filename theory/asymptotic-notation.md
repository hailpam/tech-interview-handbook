# Asymptotic Notation
To describe it, the big-O notation is used:

> Big O notation is a mathematical notation that describes the limiting behavior of a function when the argument tends towards a particular value or infinity.

> In computer science, big O notation is used to classify algorithms according to how their run time or space requirements grow as the input size grows. In analytic number theory, big O notation is often used to express a bound on the difference between an arithmetical function and a better understood approximation; a famous example of such a difference is the remainder term in the prime number theorem. Big O notation is also used in many other fields to provide similar estimates.

> Big O notation characterizes functions according to their growth rates: different functions with the same growth rate may be represented using the same O notation. The letter O is used because the growth rate of a function is also referred to as the order of the function. A description of a function in terms of big O notation usually only provides an upper bound on the growth rate of the function. Associated with big O notation are several related notations, using the symbols o, Ω, ω, and Θ, to describe other kinds of bounds on asymptotic growth rates.

In pictures:

![Big-O Notation I](https://i.stack.imgur.com/Aq09a.png)

![Big-O Notation II](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Comparison_computational_complexity.svg/1920px-Comparison_computational_complexity.svg.png)

# Time Complexity in Python

Referring to the [official Wiki page](https://wiki.python.org/moin/TimeComplexity), it is possible to look at the time complexity of the typical functions within the Python ecosystem. 

It is worth remembering that Python implements an efficient sorting function: [timsort](http://svn.python.org/projects/python/trunk/Objects/listsort.txt) which is extremely efficient for partially sorted arrays. An adaptive and stable variant of the natural merge sort, requiring as few as N-1 comparisons in the best case.

# References
- [Big-O Notation on Wikipedia](https://en.wikipedia.org/wiki/Big_O_notation)
- [Time Complexity in Python](https://wiki.python.org/moin/TimeComplexity)