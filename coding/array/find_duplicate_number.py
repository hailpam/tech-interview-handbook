# On Leetcode: https://leetcode.com/problems/find-the-duplicate-number/

class Solution(object):
    def find_duplicate(self, nums):
        uniq = set()
        for num in nums:
            if num in uniq:
                uniq.remove(num)
            else:
                uniq.add(num)
        
        for num in nums:
            if num not in uniq:
                return num
        
        return -1

    def find_duplicate_sorting(self, nums):
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0:
                if nums[i - 1] == num:
                    return num
        
        return -1

def main():
    s = Solution()

    nums = [1,3,4,2,2]
    print(s.find_duplicate(nums))           # 2
    print(s.find_duplicate_sorting(nums))

    nums = [3,1,3,4,2]
    print(s.find_duplicate(nums))           # 3
    print(s.find_duplicate_sorting(nums))

    nums = [1,1]
    print(s.find_duplicate(nums))           # 1
    print(s.find_duplicate_sorting(nums))

    nums = [1,1,2]
    print(s.find_duplicate(nums))           # 1
    print(s.find_duplicate_sorting(nums))

if __name__ == '__main__':
    main()
