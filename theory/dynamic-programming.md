# Dynamic Programming (DP)
> Dynamic programming is both a mathematical optimization method and a computer programming method. In both contexts it refers to simplifying a complicated problem by breaking it down into simpler sub-problems in a recursive manner. While some decision problems cannot be taken apart this way, decisions that span several points in time do often break apart recursively. Likewise, in computer science, if a problem can be solved optimally by breaking it into sub-problems and then recursively finding the optimal solutions to the sub-problems, then it is said to have optimal substructure. If sub-problems can be nested recursively inside larger problems, so that dynamic programming methods are applicable, then there is a relation between the value of the larger problem and the values of the sub-problems. In the optimization literature this relationship is called the Bellman equation

Problems with optimal structure for their subproblems can be solved using dynamic programming which consists in breaking down the problem into its subproblems and then recombining the solution into the final solution for the initial problem.

According to the Bellman equation, any optimization problem can be expressed according to its objective function which might be like: minimizing travel time, minimizing cost, maximizing profits, maximizing utility, etc.

> Dynamic programming breaks a multi-period planning problem into simpler steps at different points in time. Therefore, it requires keeping track of how the decision situation is evolving over time. The information about the current situation that is needed to make a correct decision is called the "state". For example, to decide how much to consume and spend at each point in time, people would need to know (among other things) their initial wealth. Therefore, wealth W would be one of their state variables, but there would probably be others. The variables chosen at any given point in time are often called the control variables. For instance, given their current wealth, people might decide how much to consume now. Choosing the control variables now may be equivalent to choosing the next state; more generally, the next state is affected by other factors in addition to the current control. For example, in the simplest case, today's wealth (the state) and consumption (the control) might exactly determine tomorrow's wealth (the new state), though typically other factors will affect tomorrow's wealth too.

To be remarked that:

> The concept behind dynamic programming is to break the problems into sub-problems and save the result for the future so that we will not have to compute that same problem again. Further optimization of sub-problems which optimizes the overall solution is known as optimal substructure property.

## Applications

The majority of the DP problems can be categorized as:

1. Optimization Problems (select a feasible solution by maximizing or minimizing an objective function).
2. Combinatorial Problems (figure out the number of ways of doing something, or the probability of some event happening).

## Schema

DP problems can be broken down into a number of standard steps:

1. Prove that the problem can be broken down into sub-problems.
2. Recursively define the value of the solution by expressing it in terms of solutions for the smaller sub-problems.
3. Compute the value of the optimal solution in bottom-up fashion.
4. Construct an optimal solution from the computed information.

## Top-down
> the problem is broken down and if the problem is solved already then saved value is returned, otherwise, the value of the function is memoized i.e. it will be calculated for the first time; for every other time, the stored value will be called back. Memoization is a great way for computationally expensive programs.

## Bottom-up
> This is an effective way of avoiding recursion by decreasing the time complexity that recursion builds up (i.e. memory cost because of recalculation of the same values). Here, the solutions to small problems are calculated which builds up the solution to the overall problem.

Bottom-up Vs top-down approaches to approach solutions to the problems using DP.

When a solution to a problem requires the re-calculation of solutions of sub-problems, then such problem might be a great candidate for DP.

> DP can be applied to any such problem that requires the re-calculation of certain values to reach the final solution.

The real nature of DP is:

> Dynamic programming is nothing but recursion with memoization i.e. calculating and storing values that can be later accessed to solve subproblems that occur again, hence making your code faster and reducing the time complexity (computing CPU cycles are reduced).

## Concrete Examples

Let's look at some concrete examples.
### Fibonacci Series

F(n) = F(n - 1) + F(n - 2) which can be coded like:

```python
def fibo(n):
    if n <= 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)
```

F(n) is the sum of solutions for its subproblems. In particular, it can be determined as the sum of F(n - 1) and F(n - 2). Clearly, recursion is ideal for solving such sort of problems. Time complexity of such solution if O(2^N), instead the space complexity is about O(N) as the recursion can go as further as N.

The reason of such high time complexity comes from: F(4) = F(3) + F(2), but F(3) = F(2) + F(1) so F(4) = (F(2) + F(1)) + F(2), clearly seeing the same solution calculated and re-calculated many times.

![Fibonacci Tree](http://ugweb.cs.ualberta.ca/~c274/web/ConcreteComputing/image/fib_tree.png)

That being said, applying DP and so using the memoization, the code becomes:

```python
def fibo(n):
    if n <= 1:
        return 1
    if not memo[n]:
        if not memo[n - 1]:
            memo[n - 1] = fibo(n - 1)
        if not memo[n - 2]:
            memo[n - 2] = fibo(n - 2)
        memo[n] = memo[n - 1] + memo[n - 2]
    return memo[n]
```

Space complexity stays O(N) with memoization as the dictionary will contain N distinct entries. On the other hand, the time complexity is going to lower to O(N) <<< O(2^N) as there won't be anymore the complexity of generating, recursively, for each and every subproblem, the components (i.e. F(3) = F(2) + F(1)).



# References
- [Demystifying Dynamic Programming](https://www.freecodecamp.org/news/demystifying-dynamic-programming-3efafb8d4296/)
- [Dynamic Programming on Wikipedia](https://en.wikipedia.org/wiki/Dynamic_programming#:~:text=Dynamic%20programming%20is%20both%20a,and%20a%20computer%20programming%20method.&text=Likewise%2C%20in%20computer%20science%2C%20if,said%20to%20have%20optimal%20substructure.)
- [Beginners Guide to Dynamic Programming](https://towardsdatascience.com/beginners-guide-to-dynamic-programming-8eff07195667)
- [Introduction to Dynamic Programming](https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/tutorial/)