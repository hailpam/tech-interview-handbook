
# On Leetcode: https://leetcode.com/problems/two-sum/

class Solution(object):
    def two_sum(self, nums, target):
        """
        Time Complexity ~O(N^2)
        Space Complexity ~O(1) no support data structures
        """
        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                if x + y == target:
                    # assume to stop for the first match, which is also
                    # the exactly one available
                    return (i, j)
        
        # by default, if not found return a pair of -1
        return (-1, -1)
    
    def two_sum_linear_time(self, nums, target):
        """
        Time Complexity ~O(N)
        Space Complexity ~O(N) with a dictionary for lookup
        """
        lookup_dict = {}
        for idx, num in enumerate(nums):
            lookup_dict[num] = idx
        
        for idx, num in enumerate(nums):
            diff = target- num
            if diff in lookup_dict:
                return (idx, lookup_dict[diff])
        
        # by default, if not found, return a pair of -1
        return (-1, -1)

def main():
    s = Solution()
    nums = [2,7,11,15]
    target = 9
    print(s.two_sum_linear_time(nums, target))

if __name__ == '__main__':
    main()
