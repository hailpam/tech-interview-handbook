# On Leetcode: https://leetcode.com/problems/range-sum-query-mutable/

class NumArray(object):
    def __init__(self, nums):
        self.nums = nums

    def upate(self, index, val):
        if index < len(self.nums):
            self.nums[index] = val
    
    def sum_range(self, left, right):
        return sum(self.nums[left:right + 1])

def main():
    n = NumArray([1, 3, 5])
    print(n.sum_range(0, 2))    # 9
    n.upate(1, 2)
    print(n.sum_range(0, 2))    # 8

if __name__ == '__main__':
    main()
