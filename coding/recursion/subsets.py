
# On Leetcode: https://leetcode.com/problems/subsets/

# TBD subsets can be solved with Backtracking

class Solution(object):
    def combine(self, nums, combs, idx=0):
        if idx > len(nums) - 1:
            return
        
        for comb in combs[1:]:
            comb_cpy = list(comb)
            comb_cpy.append(nums[idx])
            combs.append(comb_cpy)
        combs.append([nums[idx]])

        self.combine(nums, combs, idx + 1)

    def subsets(self, nums):
        combs = [[]]
        
        self.combine(nums, combs)

        return combs

def main():
    s = Solution()
    nums = [1,2,3]
    print(s.subsets(nums))
    nums = [1,2,3, 4]
    print(s.subsets(nums))
    nums = [0]
    print(s.subsets(nums))

if __name__ == '__main__':
    main()
