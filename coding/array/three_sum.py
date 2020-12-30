
# On Leetcode: https://leetcode.com/problems/3sum/
# TODO to be checked duplicates

class Solution(object):
    def three_sum(self, nums):
        """
        a + b + c = 0
        
        a + b = x => x + c = 0 => x = -c
        """
        triplets = set()
        # maps c and its opposite (i.e. -c)
        m = {}
        for num in nums:
            m[num] = num * -1
        
        dedup = set()
        for c in nums:
            x = m[c]
            # x = a + b => b = x - a
            for a in nums:
                b = x - a
                if b in m and x != c and x not in dedup:
                    dedup.add(x)
                    triplets.add((a, b, c))
        
        return triplets
    
    def three_sum_no_duplication(self, nums):
        pass

def main():
    s = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(s.three_sum(nums))
    nums = [0]
    print(s.three_sum(nums))
    nums = []
    print(s.three_sum(nums))

if __name__ == '__main__':
    main()
