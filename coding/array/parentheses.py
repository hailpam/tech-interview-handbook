
# On Leetcode: https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def check_closure(self, p, n):
        if p == '(' and n == ')':
            return True
        elif p == '[' and n == ']':
            return True
        elif p == '{' and n == '}':
            return True
        else:
            return False

    def is_valid_sequence(self, s):
        if len(s) % 2 != 0:
            return False
        
        opened = '([{'
        stack = []
        for c in list(s):
            if c in opened:
                stack.append(c)
            else:
                p = stack.pop()
                if not self.check_closure(p, c):
                    return False
        
        return True

def main():
    x = Solution()
    s = "()"
    print(x.is_valid_sequence(s))
    s = "()[]{}"
    print(x.is_valid_sequence(s))
    s = "(]"
    print(x.is_valid_sequence(s))
    s = "([)]"
    print(x.is_valid_sequence(s))
    s = "{[]}"
    print(x.is_valid_sequence(s))

if __name__ == '__main__':
    main()
