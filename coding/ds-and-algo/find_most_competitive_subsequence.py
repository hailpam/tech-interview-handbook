 # On Leetcode: https://leetcode.com/problems/find-the-most-competitive-subsequence/

class Solution(object):
    """
    Helper function to select all remaining numbers apart of the input one.
    """
    def select(self, num, nums):
        nums_cpy = list(nums)
        nums_cpy.remove(num)                                    # got to select all numbers apart of the inputed one

        return nums_cpy

    def combine(self, nums, s_idx, e_idx):
        """
        Helper function that generates local combinations for the input sub array, considering the specific
        problem statement.

        NOTE to generate all subsequences, it is just required to not find the minimum systematically and
        combine it.
        """
        comb_min = 10**9
        for num in nums[e_idx:]:                                # got to get the minimum beyond the end index, considering the problem statement
            comb_min = min(num, comb_min)
        
        sub_array = nums[s_idx:e_idx]                           # slice and materialize subarray
        lcl_combs = []
        
        for num in sub_array:
            comb_tmp = self.select(num, sub_array)              # got to select without the current number
            comb_tmp.append(comb_min)
            lcl_combs.append(tuple(comb_tmp))
        
        return sorted(lcl_combs)

    def find_most_competitive(self, nums, k):
        """
        In order to come up with subsequences, it is required to remove elements preserving the sequence. 
        
        So, this means that, for sebsequences of size 2:
        
        [3, 5, 2, 6]
         ^  5, 2, 6
                    -> (3, 5), (3, 2), (3, 6) -> (3, 2), (3, 5), (3, 6)
        [3, 5, 2, 6]
            ^  2, 6
                    -> (5, 2), (5, 6)
        
        [3, 5, 2, 6]
               ^  6
                    -> (2, 6)

        And output: (2, 6)
        
        So, in case of size 3:

        [3, 5, 2, 6]
         ^  ^  2, 6
                    -> (3, 5, 2), (3, 5, 6)
        
        [3, 5, 2, 6]
         ^     ^  6
                    -> (3, 2, 6)
        
        [3, 5, 2, 6]
            ^  ^  6
                    -> (5, 2, 6)
        
        And output: (5, 2, 6)
        """
        combs = []
        for incr in range(len(nums) - k):                        # got to create a sliding window for selection
            combs.extend(self.combine(nums, incr, incr + k))     # got to combine on the sliced array

        return sorted(combs)[0]

def main():
    s = Solution()

    nums = [3, 5, 2, 6]
    k = 2
    print(s.find_most_competitive(nums, k))

    nums = [2, 4, 3, 3, 5, 4, 9, 6]
    k = 4
    print(s.find_most_competitive(nums, k))

if __name__ == '__main__':
    main()
