
# On Leetcode:

class Solution(object):
    def is_within_boundaries(self, idx, nums):
        return idx < len(nums)

    def backtrack(self, nums, combs, idx=0, comb=[]):
        """
        It exploits a Tree structure using recursion, on the model of:
                       []

              [1]         [2]        [3]

          [1,2] [1,2] [2,3]

        [1,2,3]
        """
        # get it in as combination, first stack operation
        combs.append(list(comb))
        if not self.is_within_boundaries(idx, nums):
            return
        for i in range(idx, len(nums)):
            # add temporarily the selection
            comb.append(nums[i])
            # backtrack on the next index
            self.backtrack(nums, combs, idx=i + 1, comb=comb)
            # remove the selection backtracking on the stack
            comb.pop()

    def subsets(self, nums):
        combs = []

        self.backtrack(nums, combs)

        return combs

def main():
    s = Solution()

    nums = [1, 2, 3]
    print(s.subsets(nums))
    nums = [1, 2, 3, 4]
    print(s.subsets(nums))

if __name__ == '__main__':
    main()
