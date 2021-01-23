
# On Leetcode: https://leetcode.com/problems/longest-increasing-subsequence/

class Solution(object):
    def visit(self, nums, idx=0, memo=[]):
        """
        Recursive method which visits the array and memoizes the solutions to
        the subproblems

        The memoization reports the incremental length of the subsequence from
        the tail of the array:

        Example 1:
        [10,9,2,5,3,7,101,18]
                          1
                       1
                    2
                  3
                3
              4
            4
         4
        memo = [4,4,4,3,3,2,1,1]

        Example 2:
        [0,1,0,3,2,3]
                  1
                2
              2
            3
          3
        3
        memo = [3,3,3,2,2,1]
        """
        if memo[idx]:
            return memo[idx], nums[idx]

        if idx == len(nums) - 1:
            memo[idx] = 1
            return memo[idx], nums[idx]

        c, n = self.visit(nums, idx + 1, memo)
        if nums[idx] < n:
            c += 1
        memo[idx] = c

        return c, nums[idx]

    def lis_recursive(self, nums):
        """
        Recursive implementation which leverage a memoizing visit (i.e able to 
        memoize the results to the subproblems).
        """
        memo = [None for _ in range(len(nums))]
        max_cnt = -1
        for idx, num in enumerate(nums):
            c, n = self.visit(nums, idx, memo)
            if num < n:
                n += 1
            max_cnt = max(max_cnt, c)
        
        return max_cnt

    def lis(self, nums):
        """
        Typical problem that can have an iterative solution with a double loop.

        0 1 0 3 2 3
        ^               first element (take it)
          ^             > previous (take it)
            .           < previous
              x         > previous (take it)
                ^       < previous but monotonic (take it)
                  ^     = previous

        0 1 2 3 is the longest incrementing subsequence.

        This algorithm can be implemented with recursion as well. It should run
        for all elements as pivot, and the max should be chosen.
        """
        max_cnt = -1
        for idx1, num1 in enumerate(nums):
            idx2 = idx1 + 1
            cntr = 1
            while idx2 < len(nums):
                num2 = nums[idx2]
                if num1 < num2:
                    cntr += 1
                    prev_num2 = nums[idx2 - 1]
                    if num2 < prev_num2:
                        cntr -= 1
                idx2 += 1
            max_cnt = max(max_cnt, cntr)

        return max_cnt


def main():
    s = Solution()

    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(s.lis(nums))            # 4
    print(s.lis_recursive(nums))  # 4

    nums = [0, 1, 0, 3, 2, 3]
    print(s.lis(nums))            # 4
    print(s.lis_recursive(nums))  # 4

    nums = [7, 7, 7, 7, 7, 7, 7]
    print(s.lis(nums))            # 1
    print(s.lis_recursive(nums))  # 1


if __name__ == '__main__':
    main()
