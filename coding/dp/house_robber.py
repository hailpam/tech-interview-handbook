
# On Leetcode: https://leetcode.com/problems/house-robber/

class Solution(object):
    def visit(self, nums, idx, robbery=0):
        if idx >= len(nums):
            return robbery
        
        return self.visit(nums, idx + 2, robbery + nums[idx])

    def rob(self, nums):
        max_robbery = -1
        for idx, num in enumerate(nums):
            max_robbery = max(max_robbery, self.visit(nums, idx))

        return max_robbery

def main():
    s = Solution()

    nums = [1,2,3,1]
    print(s.rob(nums))  # 4

    nums = [2,7,9,3,1]
    print(s.rob(nums))  # 12

if __name__ == '__main__':
    main()
