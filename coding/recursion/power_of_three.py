
# On Leetcode: https://leetcode.com/problems/power-of-three/

class Solution(object):
    def is_power_of_three(self, n):
        if n != 0 and n % 3 == 0:
            if n / 3 == 1:
                return True
            else:
                return self.is_power_of_three(n / 3)
        
        return False


def main():
    s = Solution()
    n = 27
    print(s.is_power_of_three(n))
    n = 0
    print(s.is_power_of_three(n))
    n = 9
    print(s.is_power_of_three(n))
    n = 45
    print(s.is_power_of_three(n))

if __name__ == '__main__':
    main()
