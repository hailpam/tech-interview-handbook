# On Leetcode: https://leetcode.com/problems/missing-number/

class Solution(object):
    def find_missing(self, nums):
        s = set()
        for x in range(0, len(nums) + 1):
            s.add(x)
        
        for num in nums:
            s.remove(num)
        
        return s.pop()

def main():
    s = Solution()

    nums = [3,0,1]
    print(s.find_missing(nums))     # 2

    nums = [0,1]
    print(s.find_missing(nums))     # 2

    nums = [9,6,4,2,3,5,7,0,1]

    print(s.find_missing(nums))     # 8

    nums = [0]
    print(s.find_missing(nums))     # 1

if __name__ == '__main__':
    main()
