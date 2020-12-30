
# On Leetcode: https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def product_array(self, nums):
        """
        Time Complexity ~O(N^2)
        Space Complexity ~O(N) for return array
        """
        prods = []
        for i, x in enumerate(nums):
            prod = 1
            for j, y in enumerate(nums):
                if i != j:
                    prod *= y
            prods.append(prod)
        
        return prods
    
    def product_array_linear_time(self, nums):
        """
        Time Complexity ~O(N)
        Space Complexity ~O(N) for return array
        """
        prods = []
        prod = 1
        for num in nums:
            prod *= num
        
        for num in nums:
            prods.append(prod/num)
        
        return prods
    
    def product_array_linear_time_no_division(self, nums):
        """
        Time Complexity ~O(N^2)
        Space Complexity ~O(N) for return array and support prefix and postfix arrays
        """
        prefix = [1 for x in range(len(nums))]
        i = 1
        while i < len(nums):
            prefix[i] = prefix[i-1]*nums[i-1]
            i += 1
        
        postfix = [1 for x in range(len(nums))]
        i = len(nums)-2
        while i >= 0:
            postfix[i] = postfix[i+1]*nums[i+1]
            i -= 1
        
        prods = []
        i = 0
        while i < len(nums):
            prods.append(prefix[i] * postfix[i])
            i += 1
        
        return prods
    
    def product_array_divide_and_conquer(self, nums, n, left=1, idx=0):
        """
        Time Complexity ~O(N) as it scans the array only once using recursion
        Space Complexity ~O(1) in place modification
        """
        if idx == n:
            return 1
        curr = nums[idx]
        right = self.product_array_divide_and_conquer(nums, n, left*nums[idx], idx+1)
        nums[idx] = left * right
        
        return curr * right

def main():
    s = Solution()
    
    nums = [1,2,3,4]
    print(s.product_array(nums))
    print(s.product_array_linear_time(nums))
    print(s.product_array_linear_time_no_division(nums))
    
    s.product_array_divide_and_conquer(nums, len(nums))
    print(nums)

if __name__ == '__main__':
    main()
