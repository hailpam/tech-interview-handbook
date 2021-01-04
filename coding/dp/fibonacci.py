
# On Leetcode: https://leetcode.com/problems/fibonacci-number/

class Solution(object):
    def __init__(self):
        self.memo = {}
    
    def fibo(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        if n - 1 not in self.memo:
            self.memo[n - 1] = self.fibo(n - 1)
        if n - 2 not in self.memo:
            self.memo[n - 2] = self.fibo(n - 2)
        
        return self.memo[n - 1] + self.memo[n - 2]

def main():
    s = Solution()

    n = 2
    print(s.fibo(n))
    s.memo = {}

    n = 3
    print(s.fibo(n))
    s.memo = {}

    n = 4
    print(s.fibo(n))
    s.memo = {}

    n = 5
    print(s.fibo(n))

if __name__ == '__main__':
    main()
