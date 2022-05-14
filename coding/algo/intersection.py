'''
Backtracking is an algorithmic technique which tries to build solutions incrementally. It
does that by discarding those solutions that do not meet the problem constaints. It does
search/generates all possible combinations though.
There are three main problems that can be solved leveraging backtracking:

1. Decision Problem - is there a solution?
2. Optimisation Problem - what is the optimal solution?
3. Enumeration Problem - what are all solutions?

Reference: https://www.geeksforgeeks.org/backtracking-introduction
'''

def backtrack(string, solutions, partial=[]):
    # if empty, there is nothing else to explore
    if not string:
        solutions.append(''.join(partial))
        return
    # let's go over the chars, and one by one combine into a solution
    for char in string:
        # add the element to the partial solution
        partial.append(char)
        cpy_string = list(string)
        cpy_string.remove(char)
        # work through it
        backtrack(cpy_string, solutions, partial)
        # remove the element from the partial solution
        partial.pop()

def main():
    '''A typical backtracking problem consists in generating all permutations of a string'''
    
    string = '123'
    solutions = []
    backtrack(list(string), solutions)
    print(len(solutions), solutions)

    string = 'abcd'
    solutions = []
    backtrack(list(string), solutions)
    print(len(solutions), solutions)

    string = 'a1b2'
    solutions = []
    backtrack(list(string), solutions)
    print(len(solutions), solutions)

if __name__ == '__main__':
    main()
