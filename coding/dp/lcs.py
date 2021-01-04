
# On Leetcode: https://leetcode.com/problems/longest-common-subsequence/

class Solution(object):
    def __init__(self):
        self.memo = {}  # memoization can be based on a 2D matrix
    
    def lcs(self, text1, text2, i=0, j=0):
        """
        Looking at it from a Matrix perspective:

          a c e
        a 1
        b
        c   2
        d
        e     3

        It can be solved iterativelly or recursively. The recursive
        solution can also make use of memoization.
        The gist is navigating the two strings and counting the common
        characters.
        Leftmost branch of recursion:

        a       (1)
        a

        ab
        ac
        
        abc     (2)
        ac

        abce    (3)
        ace
        """
        if i == len(text1) or j == len(text2):  # out of bound, 0 match
            return 0
        elif text1[i] == text2[j]:              # 1 additional match, advance down and right (refer to matrix)
            cell = (i + 1, j + 1)
            if cell not in self.memo:
                self.memo[cell] = self.lcs(text1, text2, cell[0], cell[1])
            return 1 + self.memo[cell]
        else:                                   # explore down and right (refer to matrix), pick max of traversals
            d_cell = (i + 1, j)
            if d_cell not in self.memo:
                self.memo[d_cell] = self.lcs(text1, text2, d_cell[0], d_cell[1])
            r_cell = (i, j + 1)
            if r_cell not in self.memo:
                self.memo[r_cell] = self.lcs(text1, text2, r_cell[0], r_cell[1])
            return max(self.memo[d_cell], self.memo[r_cell])

def main():
    s = Solution()

    text1 = "abdce"
    text2 = "ace" 
    print(s.lcs(text1, text2))
    s.memo = {}
    
    text1 = "abc"
    text2 = "abc"
    print(s.lcs(text1, text2))
    s.memo = {}

    text1 = "abc"
    text2 = "def"
    print(s.lcs(text1, text2))
    s.memo = {}

    text1 = "abdce"
    text2 = "axeyz" 
    print(s.lcs(text1, text2))
    s.memo = {}

    text1 = "xybdce"
    text2 = "axeyz" 
    print(s.lcs(text1, text2))

if __name__ == '__main__':
    main()
