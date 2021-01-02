
# Leetcode:

class Solution(object):
    def repr_hour(self, nums):
        return '%d' % sum(nums)
    
    def repr_minute(self, nums):
        s = sum(nums)
        return '%d' % s if s >= 10 else  '0%d' % s

    def get_combinations(self, nums, combs, idx=0):
        if idx < len(nums):
            combs_itr = []
            for comb in combs:
                comb_cpy = list(comb)
                comb_cpy.append(nums[idx])
                combs_itr.append(comb_cpy)
            combs.extend(combs_itr)
            self.get_combinations(nums, combs, idx + 1)

    def binary_watch(self, n):
        hours = [1, 2, 4, 8]
        minutes = [1, 2, 4, 8, 16, 32]

        combs_hours = [[]]
        self.get_combinations(hours, combs_hours)
        combs_minutes = [[]]
        self. get_combinations(minutes, combs_minutes)

        combs = set()
        for comb_hour in combs_hours:
            for comb_minute in combs_minutes:
                if len(comb_hour) == n:
                    combs.add('%s:00' % self.repr_hour(comb_hour))
                if len(comb_minute) == n:
                    combs.add('0:%s' % self.repr_minute(comb_minute))
                if len(comb_hour) + len(comb_minute) == n:
                    combs.add('%s:%s' % (self.repr_hour(comb_hour), self.repr_minute(comb_minute)))
        
        return combs

def main():
    s = Solution()

    n = 1
    print(sorted(s.binary_watch(n)))
    n = 2
    print(sorted(s.binary_watch(n)))

if __name__ == '__main__':
    main()
