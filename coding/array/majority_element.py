# On Leetcode: https://leetcode.com/problems/majority-element

class Solution(object):
    def majority_element_no_memo(self, nums):
        # TBD
        pass
    
    def majority_element(self, nums):
        memo = {}
        for num in nums:
            if num not in memo:
                memo[num] = 0
            memo[num] += 1
        
        x = int(len(nums) / 2)
        for num in memo:
            if memo[num] > x:
                return num
        
        return None

def main():
    s = Solution()
    
    nums = [3,2,3]
    print(s.majority_element(nums))     # 3

    nums = [2,2,1,1,1,2,2]
    print(s.majority_element(nums))     # 2

if __name__ == '__main__':
    main()
