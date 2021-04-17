# On Leetcode: https://leetcode.com/problems/move-zeroes/

class Solution(object):
    def swap(self, i, j, nums):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def move_left(self, i, nums):
        while i > 0:
            j = i - 1
            if nums[i - 1] != 0:
                break
            self.swap(i, i - 1, nums)
            i -= 1

    def move_zeros(self, nums):
        '''
        Main idea: swap to left until there is some zero on the left.

        [0,1,0,3,12]
         ^
           ^
           [1,0,0,3,12]
                ^
                  ^
                  [1,3,0,0,12]
                         ^
                            ^
                            [1,3,12,0,0]
        
        Optimization: find the leftmost zero.
        '''
        if len(nums) > 1:
            for i, num in enumerate(nums):
                if num != 0:
                    self.move_left(i, nums)

def main():
    s = Solution()

    nums = [0,1,0,3,12]
    s.move_zeros(nums)
    print(nums)             # [1, 3, 12, 0, 0]

    nums = [0]
    s.move_zeros(nums)
    print(nums)             # [0]

if __name__ == '__main__':
    main()
