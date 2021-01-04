
# On Leetcode: https://leetcode.com/problems/unique-paths/

class Solution(object):
    def __init__(self):
        self.memo = {}

    def unique_paths(self, m, n, cell=(0,0)):
        """
        0,0 0,1
        1,0 1,1
        2,0 2,1

        For above 3x2 matrix:

                 X
           d          r
        d     r     d     
          r d     d 

        Starting from (0,0) it's required to reach (m-1) and (n-1). Once
        reached, it is required to return 1.
        """
        if cell[0] == m - 1 and cell[1] == n -1:    # reached the bottom-right corner
            return 1
        if cell[0] > m - 1 or cell[1] > n - 1:      # went out-of-bound, invalid solution
            return 0
        
        down = (cell[0] + 1, cell[1])
        if down not in self.memo:                   # memoizing a move down
            self.memo[down] = self.unique_paths(m, n, down)
        right = (cell[0], cell[1] + 1)
        if right not in self.memo:                  # memoizing a move right
            self.memo[right] = self.unique_paths(m, n, right)

        return self.memo[down] + self.memo[right]


def main():
    s = Solution()

    m = 3
    n = 2
    print(s.unique_paths(m, n))
    s.memo = {}
    m = 3
    n = 3
    print(s.unique_paths(m, n))
    s.memo = {}
    m = 7
    n = 3
    print(s.unique_paths(m, n))
    s.memo = {}
    m = 3
    n = 7
    print(s.unique_paths(m, n))
    s.memo = {}

if __name__ == '__main__':
    main()
