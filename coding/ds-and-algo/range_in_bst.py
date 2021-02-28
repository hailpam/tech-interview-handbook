# On Leetcode: https://leetcode.com/problems/range-sum-of-bst/

class Solution(object):
    def range_sum_bst(self, root, low, high, idx=0):
        """
        It is expected to return the sum of all elements that are within
        the specified range, inclusive the boundaries.
        
        Example: low=7 and high=15, [7,15] and all elements falling in it
        """
        if idx >= len(root) or not root[idx]:                           # no contribution to the sum
            return 0
        
        a_sum = 0
        if root[idx] >= low and root[idx] <= high:                      # contribution to the sum
            a_sum = root[idx]
        
        l_sum = self.range_sum_bst(root, low, high, idx=2 * idx + 1)    # contribution of the left subtree
        r_sum = self.range_sum_bst(root, low, high, idx=2 * idx + 2)    # contribution of the right subtree

        return a_sum + l_sum + r_sum

def main():
    s = Solution()

    root = [10,5,15,3,7,None,18]
    low = 7
    high = 15
    print(s.range_sum_bst(root, low, high))     # 32

    root = [10,5,15,3,7,13,18,1,None,6]
    low = 6
    high = 10
    print(s.range_sum_bst(root, low, high))     # 23

if __name__ == '__main__':
    main()
