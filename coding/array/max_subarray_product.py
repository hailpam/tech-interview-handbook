
# On Leetcode: https://leetcode.com/problems/maximum-product-subarray/

class Solution(object):
    def max_subarray_product(self, nums):
        prod = 1
        max_prod = nums[0]
        for i, num in enumerate(nums):
            prod *= num
            max_prod = max(max_prod, prod, num)
        
        return max_prod

def main():
    s = Solution()
    nums = [2,3,-2,4]
    print(s.max_subarray_product(nums))
    nums = [-2,0,-1]
    print(s.max_subarray_product(nums))
    nums = [6, -3, -10, 0, 2]
    print(s.max_subarray_product(nums))
    nums = [-1, -3, -10, 0, 60]
    print(s.max_subarray_product(nums))
    nums = [-2, -40, 0, -2, -3]
    print(s.max_subarray_product(nums))

if __name__ == '__main__':
    main()