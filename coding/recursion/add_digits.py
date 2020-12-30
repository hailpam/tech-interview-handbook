
# On Leetcode: https://leetcode.com/problems/add-digits/

class Solution(object):
    def add_digits(self, num):
        quotient = int(num / 10)
        remainder = num % 10

        if quotient == 0:
            return num

        return self.add_digits(quotient + remainder)

def main():
    s = Solution()
    num = 38
    print(s.add_digits(num))

if __name__ == '__main__':
    main()
