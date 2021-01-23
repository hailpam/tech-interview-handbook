
# On Leetcode: https://leetcode.com/problems/jump-game/

class Solution(object):
    def jump(self, nums, nr_steps, idx):
        if idx >= len(nums):                # got out of bound
            return False

        if nr_steps == 0:
            if idx == len(nums) - 1:        # got to the end of the array, to got it
                return True
            else:
                return False                # not able to get to the end with this jump
        
        return self.jump(nums, nr_steps - 1, idx + 1)

    def can_jump(self, nums):
        for idx, num in enumerate(nums):
            if self.jump(nums, num, idx):   # got it, return immediately
                return True
        
        return False

def main():
    s = Solution()

    nums = [2,3,1,1,4]
    print(s.can_jump(nums))

    nums = [3,2,1,0,4]
    print(s.can_jump(nums))


if __name__ == '__main__':
    main()
