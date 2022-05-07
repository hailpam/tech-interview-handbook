# From Meta interview

'''
Find the solution to the equation: a^3 + b^3 = c^3 + d^3, 0 <= a, b, c, d < 10

Solutions:
    1. (brute force) 4 nested loops to generate all combinations
    2. (optimised) 2 loops to generate the combination for the left part only (to be equal to the right part)

Example: 
a^3 + b^3 = c^3 + d^3
    9 = 9:
    [
        (1, 1, 1, 1),
        (1, 2, 1, 2), 
        (1, 2, 2, 1), 
        (2, 1, 1, 2), 
        (2, 1, 2, 1),
        (2, 2, 2, 2)
    ]
    [...]
'''

def __generate(lower, upper):
    combinations = {}
    for i in range(lower, upper):
        for j in range(lower, upper):
            s = i**3 + j**3
            if s not in combinations:
                combinations[s] = []
            combinations[s].append((i, j))
    return combinations

def __solve(combinations):
    solutions = []
    for key in combinations:
        combination = combinations[key]
        for i in combination:
            for j in combination:
                solutions.append((i[0], i[1], j[0], j[1]))
    return solutions

def solver(lower, upper):
    # let's create the combinations to a given sum
    combinations = __generate(lower, upper)
    # let's combine the possible alternatives
    solutions = __solve(combinations)
    return solutions

def main():
    lower = 1
    upper = 3
    print(solver(lower, upper))

if __name__ == '__main__':
    main()
