
# On Leetcode: https://leetcode.com/problems/combination-sum-iv/

class Solution(object):
    def generate(self, nums, target, idx, comb, combs):
        if target == 0:                     # found a viable combination, to be accounted for
            combs.add(tuple(comb))
            return
        if target < 0:                      # larger than expected
            return
        for num in nums[:idx]:
            comb.append(num)                # got to add it
            self.generate(nums, target - num, idx, comb, combs)
            comb.pop()                      # got to remove it after recursion

    def combination_sum(self, nums, target):
        """
        The main idea of the algorithm is to investigate the combination for each single element:

        Example: [1, 2, 3], 4
        step 0: [1]
        1
          1
            1
              1

        step 1: [1, 2]
                1
            2        1
          1   2    2    1
        1             2   1

        And so on... this allows to generate allo combinations. To deduplicate, it is required to 
        use a set.

        TBD - find a way of memoizing...
        """
        combs = set()
        for idx, _ in enumerate(nums):
            self.generate(nums, target, idx + 1, [], combs)
        
        return len(combs)

def main():
    s = Solution()

    nums = [1, 2, 3]
    target = 4
    print(s.combination_sum(nums, target))   # 7

if __name__ == '__main__':
    main()
