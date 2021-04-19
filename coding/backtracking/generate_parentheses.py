# On Leetcode: https://leetcode.com/problems/generate-parentheses/

class Solution(object):
    def __init__(self):
        self.opening = '('
        self.closing = ')'
        self.pair = [self.opening, self.closing]

    def is_valid(self, n, comb):
        if comb.count(self.opening) > n or comb.count(self.closing) > n:
            return False
        
        stack = []
        for c in comb:
            if c == self.opening:
                stack.append(c)
            else:
                if stack:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
    
    def backtracking(self, n, combs=[], comb=[]):
        if comb and comb[0] == self.closing:                # really a bad start, got to prune immmediately
            return
        if comb.count(self.opening) > n:                    # to prune a part of the tree which is invalid
            return
        if len(comb) >= 2 * n:
            if self.is_valid(n, comb):                      # if valid, got to return, nothing more to be done
                combs.append(''.join(comb))
            return
        for p in self.pair:
            comb.append(p)
            self.backtracking(n, combs=combs, comb=comb)
            comb.pop()

    def generate_parentheses(self, n):
        '''
        Main idea: use the backtracking to generate well-formed sequences of 
        open/close parentheses. Pruning can cut non-eplorable branches.

        Example: n = 2

                    (
                ((      ()
            (()             ()(
            (())            ()()
        
        It is required to discard the non valid solutions for the problem at hand.
        The backtracking tree might look like the one presented above, which prunes
        non-valid solutions.

        Complexity: 2^n
        '''
        combs = []
        self.backtracking(n, combs=combs)

        return combs

def main():
    s = Solution()

    n = 1
    print(s.generate_parentheses(n))    # ['()']

    n = 2
    print(s.generate_parentheses(n))     # ['()']

    n = 3
    print(s.generate_parentheses(n))    # ["((()))","(()())","(())()","()(())","()()()"]

if __name__ == '__main__':
    main()
