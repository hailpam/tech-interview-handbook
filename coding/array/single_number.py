# On Leetcode: https://leetcode.com/problems/single-number/
class Solution(object):

    def single_number(self, nums):
        memo = {}
        for num in nums:
            if num not in memo:
                memo[num] = 0
            memo[num] += 1
        
        for num in memo:
            if memo[num] == 1:
                return num
        
        return -1

    def single_number_no_memory(self, nums):
        '''
        The main idea is to proceed with a nested loop which exits as soon as a
        duplicate is found.

        2 : [2, 2, 1]
             ^
                ^       duplicate, exit
        2 : [2, 2, 1]
                ^
             ^     ^    duplicate, exit
        1 : [2, 2, 1]
                   ^
                ^
             ^          no duplicate, return 1
        
        Overall time complexity: ~O(N)
        - also in case of extreme unique values, the array is iterated 1 time only
        Overall space complexity: ~O(1)
        '''
        if len(nums) == 1:
            return nums[0]
        
        for i, num in enumerate(nums):                          # ~O(N)
            for j in range(1, len(nums) + 1):                   # w.c. ~O(N) need to check all (when at the extreme boundaries)
                if i - j < 0 and i + j >= len(nums):
                    return num
                if i - j >= 0 and nums[i - j] == num:
                    break
                if i + j < len(nums) and nums[i + j] == num:
                    break
        
        return -1

def main():
    s = Solution()

    nums = [2,2,1]
    print(s.single_number(nums))             # 1
    print(s.single_number_no_memory(nums))

    nums = [4,1,2,1,2]
    print(s.single_number(nums))            # 4
    print(s.single_number_no_memory(nums))

    nums = [1]
    print(s.single_number(nums))            # 1
    print(s.single_number_no_memory(nums))

    nums = [2,1,2,1]
    print(s.single_number(nums))            # -1
    print(s.single_number_no_memory(nums))

if __name__ == '__main__':
    main()