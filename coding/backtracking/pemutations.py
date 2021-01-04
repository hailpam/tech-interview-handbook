
# On Leetcode: https://leetcode.com/problems/permutations/

class Solution(object):
    def is_solution(self, nums, comb):
        return len(nums) == len(comb)
    
    def get_difference(self, nums, comb):
        return [num for num in nums if num not in comb]

    def backtrack(self, nums, combs, comb=[]):
        """
        Using a representation based on a Tree structure:

                             
                             []
        
               [1]            [2]             [3]
        
             [2] [3]        [1] [3]         [1] [2]

        [1,2,3] [1,3,2] [2,1,3] [2,3,1] [3,1,2] [3,2,1]

        Using a depth-first approach together with a systematic diff,
        step-by-step, it is possible to come up with all permutations.
        """
        if self.is_solution(nums, comb):
            combs.append(list(comb))
            return
        for diff in self.get_difference(nums, comb):
            comb.append(diff)
            self.backtrack(nums, combs, comb)
            comb.pop()

    def permutations(self, nums):
        combs = []

        self.backtrack(nums, combs)

        return combs

def main():
    s = Solution()

    nums = [1, 2, ]
    print(s.permutations(nums))
    nums = [1, 2, 3]
    print(s.permutations(nums))
    nums = [1,2,3,4]
    print(s.permutations(nums))
    
if __name__ == '__main__':
    main()
