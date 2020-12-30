
# On Leetcode: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution(object):
    def min_rotated_sorted_array(self, nums):
        first = nums[0]
        last = nums[len(nums) - 1]
        if first < last:
            return first
        else:
            i = len(nums) - 1
            while i > 0:
                if nums[i] < nums[i - 1]:
                    return nums[i]
                i -= 1

def main():
    s = Solution()
    nums = [3,4,5,1,2]
    print(s.min_rotated_sorted_array(nums))
    nums = [4,5,6,7,0,1,2]
    print(s.min_rotated_sorted_array(nums))
    nums = [11,13,15,17]
    print(s.min_rotated_sorted_array(nums))

if __name__ == '__main__':
    main()
