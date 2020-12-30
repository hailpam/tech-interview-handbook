
# On Leetcode: https://leetcode.com/problems/power-of-four/

class Solution(object):
    def is_power_of_four(self, n):
        if n == 1:
            return True
        if n != 0 and n % 4 == 0:
            if n / 4 == 1:
                return True
            else:
                return self.is_power_of_four(n / 4)
        
        return False

def main():
    s = Solution()
    n = 16
    print(s.is_power_of_four(n))
    n = 5
    print(s.is_power_of_four(n))
    n = 1
    print(s.is_power_of_four(n))

if __name__ == '__main__':
    main()
