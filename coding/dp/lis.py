
# On Leetcode: https://leetcode.com/problems/longest-increasing-subsequence/

class Solution(object):
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

    nums = [10,9,2,5,3,7,101,18]
    print(s.lis(nums))    # 4

    nums = [0,1,0,3,2,3]
    print(s.lis(nums))    # 4

    nums = [7,7,7,7,7,7,7]
    print(s.lis(nums))    # 1

if __name__ == '__main__':
    main()
