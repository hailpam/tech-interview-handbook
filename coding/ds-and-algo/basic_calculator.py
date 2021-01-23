
# On Leetcode: https://leetcode.com/problems/basic-calculator/

# TBD - nested parenthesis and double-digit numbers

class Solution(object):
    OPERATORS = ['+', '-', '/', '*']

    def compute(self, l_opnd, r_opnd, optr):
        if optr == '+':
            return l_opnd + r_opnd
        elif optr == '-':
            return l_opnd - r_opnd
        elif optr == '/':
            return l_opnd / r_opnd
        else:
            return l_opnd * r_opnd

    def search_closure(self, chars, start_idx, end_idx):
        for idx, char in enumerate(chars[start_idx + 1:end_idx]):
            if char == ')':
                return start_idx + 1, start_idx + idx + 1

    def evaluate(self, chars, start_idx, end_idx):
        opnd_stack = []
        optr_stack = []
        idx = start_idx
        while idx < end_idx:
            char = chars[idx]

            if char == '(':
                s, e = self.search_closure(chars, idx, end_idx)
                opnd_stack.append(self.evaluate(chars, s, e))
                idx = e
            else:
                if char not in self.OPERATORS:
                    opnd_stack.append(int(char))
                else:
                    optr_stack.append(char)
            
            if len(opnd_stack) == 2:
                r_opnd = opnd_stack.pop()
                l_opnd = opnd_stack.pop()
                optr = optr_stack.pop()
                opnd_stack.append(self.compute(l_opnd, r_opnd, optr))
            
            idx += 1

        return opnd_stack[0]

    def calculate(self, string):
        string = string.replace(' ', '')
        chars = list(string)

        return self.evaluate(chars, 0, len(string))

def main():
    s = Solution()

    string = "1 + 1"
    print(s.calculate(string))  # 2

    string = " 2-1 + 2 "
    print(s.calculate(string))  # 3

    string = " 7-(1* 3) + 2 "
    print(s.calculate(string))  # 6

    string = " 8-(1*3) + 2 "
    print(s.calculate(string))  # 7

    string = " 8-(3/1) + 2 "
    print(s.calculate(string))  # 7

if __name__ == '__main__':
    main()
