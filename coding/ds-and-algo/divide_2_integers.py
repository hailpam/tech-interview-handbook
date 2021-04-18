# On Leetcode: https://leetcode.com/problems/divide-two-integers/

class Solution(object):
    def divide(self, dividend, divisor):
        '''
        Main idea: use subtraction on absolute values and then restore
        the sign after the fact (i.e. post operation).
        '''
        negative = dividend < 0 or divisor < 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        division = 0
        while dividend - divisor >= 0:
            division += 1
            dividend -= divisor

        return division if not negative else -1 * division

def main():
    s = Solution()

    dividend = 10
    divisor = 3
    print(s.divide(dividend, divisor))  # 3

    dividend = 7
    divisor = -3
    print(s.divide(dividend, divisor))  # -2

    dividend = 0
    divisor = 1
    print(s.divide(dividend, divisor))  # 0

    dividend = 1
    divisor = 1
    print(s.divide(dividend, divisor))  # 1

if __name__ == '__main__':
    main()
