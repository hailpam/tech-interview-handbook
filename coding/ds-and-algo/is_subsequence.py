
# On Leetcode: https://leetcode.com/problems/is-subsequence/

class Solution(object):
    def is_subsequence(self, s, t):
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                if i == len(s) - 1:
                    return True
                i += 1
            j += 1
        
        return False

def main():
    x = Solution()

    s = "abc"
    t = "ahbgdc"
    print(x.is_subsequence(s, t))

    s = "axc"
    t = "ahbgdc"
    print(x.is_subsequence(s, t))

if __name__ == '__main__':
    main()
