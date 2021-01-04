
# On Leetcode: https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def __init__(self):
        self.memo = {}
    
    def climb_stairs(self, n):
        """
        Adopting recursion, the recursion tree looks like:

            3
          2   1
         1 0 0 -1
        0 -1

        Base cases are then n == 0 and n < 0. In the former
        case, a solution is reached and unrolling the stack
        is going to count back. In the latter case, an invalid
        solution is reached, so unrolling the stack that branch
        should not count. 
        """
        if n < 0:       # not acceptable as solution
            return 0
        if n == 0:      # acceptable as solution
            return 1
        
        if n - 1 not in self.memo:
            self.memo[n - 1] = self.climb_stairs(n - 1)
        if n - 2 not in self.memo:
            self.memo[n - 2] = self.climb_stairs(n - 2)
        
        return self.memo[n - 1] + self.memo[n - 2]

def main():
    s = Solution()

    n = 2
    print(s.climb_stairs(n))
    s.memo = {}
    n = 3
    print(s.climb_stairs(n))
    s.memo = {}
    n = 4
    """
    For 4, the recursion tree looks like:

                   4
            3           2
        2       1     1   0
      1   0    0 -1  0 -1
     1 -1
    0 -1 
    """
    print(s.climb_stairs(n))
    s.memo = {}
    n = 6
    print(s.climb_stairs(n))

if __name__ == '__main__':
    main()
