# Backtracking
Let's start with the definition of Backtracking:

> Backtracking is a general algorithm for finding all (or some) solutions to some computational problems, that incrementally builds candidates to the solutions, and abandons each partial candidate (“backtracks”) as soon as it determines that the candidate cannot possibly be completed to a valid solution.

Keywords are: incremental, backtrack. Solutions are built incrementally and so evaluated according to the constraints; in case of violations of the problem set constraints, the so computed solution is discarded and the algorithm backtracks to the previous one.

Let's consider the following Maze.

![A simple Maze.](https://miro.medium.com/max/634/1*vi2CWElf8--5EQUQfeUGpg.png)

Now, as a follow up, let's build the game tree for it to start looking at the alternatives which, for the sake of simplicity, have been reduced to only three possible paths through (i.e. junctions).

![Game Tree for the simple Maze presented above.](https://miro.medium.com/max/2000/1*3jLYOFeSUR5_S1mPGvJbHg.png)

At any point in time, it is possible to move up or down, right or left and this is a decision to be taken according to the local constraints. According to how the decision is made, if there is still alternative, then it's pursued, otherwise the solution is evaluated as negative and the branch is abandoned (e.g. the case of right-down-right-up/right which clearly brings to a dead end).

Let's try to write some Python code for it, considering that a-priori the algorithm cannot know how to proceed and that it can only make successive choices (i.e. incremental nature of the problem set as well as of its solution).

```python
def backtrack(direction):
    if is_exit():
        return True
    for direction in get_directions():
        if backtrack(direction):
            return True
    return False
```

With the above code, we're making a few assumptions. For instance, we're assuming that it exists a ```is_exit()``` predicate able to discriminate whether an exit is reached or not, as well as a function ```get_directions()``` which is providing the list of viable directions for the specific position in the Maze.

The code looks trivial, but let's try to look at how the call stack evolves, referring to the above presented game tree.

```
move IN
  go RIGHT
    go DOWN
      go RIGHT
        go UP     -> dead end, backtrack (only go DOWN is allowedd, from where we come from)
        go RIGHT  -> dead end, backtrack (only go LEFT is allowed, from where we come from)
    go UP
      go RIGHT
        go DOWN
          go RIGHT -> end, got the exit, unroll the call stack
move OUT
```

On the model of a depth first search, the recursive algorithm tries to find viable solution to each and every step and backtracks to the previous point whenever it does not find its way through. The magic comes from playing with the call stack which guarantees the rolling and unrolling of the call stack according to the specific situation.

## About Time Complexity

Backtracking is often faster than the brute force approach/enumeration. The time complexity is very much dependent on the problem itself. Notable examples are:

- Hamiltonian Cycle ~O(N!) in the worst case
- WordBreak and StringSegment ~O(2^N)
- NQueens ~O(N!)

In general, it is important to account for the number of recursive steps and the amount of work for each and every recursive step.

# References
- [Backtracking Explained](https://medium.com/@andreaiacono/backtracking-explained-7450d6ef9e1a#:~:text=Backtracking%20is%20a%20general%20algorithm,completed%20to%20a%20valid%20solution.)
- [Backtracking on Wikipedia](https://en.wikipedia.org/wiki/Backtracking)
- [Subsets/Permutations/Combinations](https://labuladong.gitbook.io/algo-en/iii.-algorithmic-thinking/subset_permutation_combination)
