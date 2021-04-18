# On Leetcode: https://leetcode.com/problems/first-missing-positive/

class Solution(object):
    def first_missing(self, nums):
        el_max = max(nums)                          # define the upper bound
        
        ref = [x for x in range(1, el_max + 1)]     # define an iterable reference, already sorted
        
        lookup = set(nums)                          # define a lookup structure
        for num in ref:
            if num not in lookup:                   # got it, it is the minimum missing element among the positives
                return num

        return el_max + 1

def main():
    s = Solution()

    nums = [1,2,0]
    print(s.first_missing(nums))    # 3

    nums = [3,4,-1,1]
    print(s.first_missing(nums))    # 2

    nums = [7,8,9,11,12]
    print(s.first_missing(nums))    # 1

if __name__ == '__main__':
    main()
