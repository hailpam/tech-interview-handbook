
# On Leetcode: https://leetcode.com/problems/combinations/

class Solution(object):
    def is_viable_solution(self, comb, k):
        return len(comb) == k
    
    def backtrack(self, nums, k, combs, idx=0, comb=[]):
        if self.is_viable_solution(comb, k):
            combs.append(list(comb))
            return
        for i in range(idx, len(nums)):
            comb.append(nums[i])
            self.backtrack(nums, k, combs, idx=i + 1, comb=comb)
            comb.pop()

    def combinations(self, nums, k):
        """
        Using the approach of a Tree structure (example of k=2 combinations):

                                        []

                [1]             [2]            [3]          [4]
        
        [1,2] [1,3] [1,4]   [2,3] [2,4]    [3,4]

        Adopting a depth-first and unrolling the stack, the k-subsets
        can be calculated.
        """
        combs = []

        self.backtrack(nums, k, combs)

        return combs

def main():
    s = Solution()

    nums = [1, 2, 3, 4]
    k = 2
    print(s.combinations(nums, k))
    nums = [1, 2, 3, 4, 5]
    k = 2
    print(s.combinations(nums, k))

if __name__ == '__main__':
    main()
