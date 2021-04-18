# On Leetcode: https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution(object):
    def fact(self, num):
        return num * self.fact(num - 1) if num > 1 else 1
    
    def nr_trailing_zeros(self, num, count=0):
        if num == 0:
            return 0
        if num % 10 == 0:
            num = int(num / 10)
            return self.nr_trailing_zeros(num, count + 1)
        return count

def main():
    s = Solution()

    n = 3
    print(s.nr_trailing_zeros(s.fact(n)))   # 0

    n = 5
    print(s.nr_trailing_zeros(s.fact(n)))   # 1

    n = 0
    print(s.nr_trailing_zeros(s.fact(n)))   # 0

if __name__ == '__main__':
    main()
