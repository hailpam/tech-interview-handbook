# On Leetcode: https://leetcode.com/problems/fizz-buzz

class Solution(object):
    def fizz_buzz(self, n):
        answer = []
        for i in range(n):
            x = i + 1
            if x % 3 != 0 and x % 5 != 0:
                answer.append(x)
                continue
            if x % 3 == 0 and x % 5 == 0:
                answer.append('FizzBuzz')
            if x % 3 == 0:
                answer.append('Fizz')
            if x % 5 == 0:
                answer.append('Buzz')

        return answer

def main():
    s = Solution()

    n = 3
    print(s.fizz_buzz(n))  # ["1","2","Fizz"]
    
    n = 5
    print(s.fizz_buzz(n))  # ["1","2","Fizz","4","Buzz"]
    
    n = 15
    print(s.fizz_buzz(n))  # ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

if __name__ == '__main__':
    main()
