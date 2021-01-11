
# On Leetcode: https://leetcode.com/problems/longest-consecutive-sequence/

class Solution(object):
    def longest_consecutive(self, nums):
        """
        Sort the array and then count the consecutive elements which are 1 apart.
        It takes care of split sequences.
        """
        nums.sort()

        cntr = 1
        longest = 0
        for idx in range(1, len(nums)):
            if nums[idx - 1] != nums[idx]:
                if nums[idx] - nums[idx - 1] == 1:
                    cntr += 1
                    longest = max(longest, cntr)
                else:
                    cntr = 1

        return longest

def main():
    s = Solution()

    nums = [100, 4, 200, 1, 3, 2]
    print(s.longest_consecutive(nums))

    nums = [100,4, 101, 200,1,3,2]
    print(s.longest_consecutive(nums))

    nums = [100,4, 101, 105, 103, 102, 200, 1, 3, 2]
    print(s.longest_consecutive(nums))
    
    nums = [100,4, 101, 104, 103, 102, 200, 1, 3, 2]
    print(s.longest_consecutive(nums))

    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(s.longest_consecutive(nums))

if __name__ == '__main__':
    main()
