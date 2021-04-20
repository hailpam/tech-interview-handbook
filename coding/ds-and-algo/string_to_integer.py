# On Leetcode: https://leetcode.com/problems/string-to-integer-atoi/

class Solution(object):
    def __init__(self):
        self.chars = ['%s' % x for x in range(0, 10)]
        self.chars.extend('-')

    def convert(self, num):
        is_negative = False
        if num and num[0] == '-':
            num.pop(0)
            is_negative = True
        
        converted = 0
        num = num[::-1]
        for i, n in enumerate(num):
            converted += (10**i * int(n))

        if converted > 2**31:
            converted = 2**31

        return converted * -1 if is_negative else converted

    def extract(self, idx, s):
        num = []
        while idx < len(s) and s[idx] in self.chars:
            num.append(s[idx])
            idx += 1
        
        return num

    def atoi(self, s):
        idx = 0
        num = None
        while idx < len(s):
            if s[idx] in self.chars:
                num = self.extract(idx, s)
                break
            idx += 1
        
        return self.convert(num) if num else None

def main():
    x = Solution()

    s = "42"
    print(x.atoi(s))    # 42

    s = "   -42"
    print(x.atoi(s))    # -42

    s = "4193 with words"
    print(x.atoi(s))    # 4193

    s = "words and 987"
    print(x.atoi(s))    # 987

    s = "-91283472332"
    print(x.atoi(s))    # 
    
    s = " hey! "
    print(x.atoi(s))    # None


if __name__ == '__main__':
    main()
