
# On Leetcode: https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def contains_duplicate(self, nums):
        """
        O(N^2) time complexity
        :type nums: List[int]
        :rtype: bool
        """
        for x in nums:
            for y in nums:
                if x == y:
                    return True
        return False
    
    def contains_duplicate_linear_time(self, numms):
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            count[num] += 1
        
        for num in count:
            if count[num] > 1:
                return True
        
        return False
        

def main():
    s = Solution()
    nums = [1,1,1,3,3,4,3,2,4,2]
    print(s.contains_duplicate(nums))

if __name__ == '__main__':
    main()
