
# On Leetcode: https://leetcode.com/problems/maximum-subarray/

class Solution(object):
    def max_subarray(self, nums):
        """
        O(N*N-i) time complexity because it looks ahead on the remaining array
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        for i, x in enumerate(nums):
            inc_sum = x
            for y in nums[i+1:]:
                inc_sum += y
                max_sum = max(max_sum, inc_sum)
        return max_sum
    
    def max_subarray_linear_time(self, nums):
        """
        O(N) time complexity, Kadane's Algorithm (dynamic programming)
        """
        max_so_far = nums[0]
        max_sum = nums[0]
        for num in nums[1:]:
            max_so_far = max(num, max_so_far + num)
            max_sum = max(max_sum, max_so_far)
        return max_sum


def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    s = Solution()
    print(s.max_subarray(nums))
    nums = [-2147483647]
    print(s.max_subarray(nums))
    nums = [1,-3,2,1,-1]
    print(s.max_subarray(nums))

if __name__ == '__main__':
    main()
