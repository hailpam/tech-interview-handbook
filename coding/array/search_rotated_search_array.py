
# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution(object):
    def binary_search(self, nums, start, end, target):
        if start == end:
            if nums[start] == target:
                return start
            else:
                return -1
        else:
            pivot = int((end + start)/2)
            if target > nums[start]:
                return self.binary_search(nums, pivot, end, target)
            else:
                return self.binary_search(nums, start, pivot, target)
    
    def search(self, nums, target):
        left = nums[0]
        right = nums[len(nums) - 1]
        pivot = int(len(nums) / 2)
        
        if left > right: # rotated
            i = len(nums) - 1
            while nums[i - 1] < nums[i]:
                i -= 1
            pivot = i
        
        if target > right:
            return self.binary_search(nums, 0, pivot, target)
        else:
            return self.binary_search(nums, pivot, len(nums) - 1, target)

def main():
    s = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(s.search(nums, target))
    target = 3
    print(s.search(nums, target))
    nums = [1]
    target = 0
    print(s.search(nums, target))

if __name__ == '__main__':
    main()
