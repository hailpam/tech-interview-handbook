
# On Leetcode: https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution(object):
    def eval(self, l_opnd, r_opnd, oprt):
        """
        Evaluates the operands combining with the operator, to be then re-inserted
        in the stack.
        """
        if oprt == '+':
            return l_opnd + r_opnd
        elif oprt == '-':
            return l_opnd - r_opnd
        elif oprt == '*':
            return int(l_opnd * r_opnd)
        else:
            return int(l_opnd / r_opnd)
    
    def eval_rpn(self, tokens):
        """
        Evaluates the Reverse Polish Notation using a stack.
        """
        operators = ['+', '-', '*', '/']
        stack = []                      # use of a list as a stack
        for token in tokens:
            if token in operators:      # got to evaluate the operands
                r_opnd = stack.pop()
                l_opnd = stack.pop()
                stack.append(self.eval(l_opnd, r_opnd, token))
            else:                       # got to stack it
                stack.append(int(token))
    
        return stack.pop()              # only 1 operand should be in the stack

def main():
    s = Solution()

    tokens = ["2", "1", "+", "3", "*"]
    print(s.eval_rpn(tokens))   # 9

    tokens = ["4", "13", "5", "/", "+"]
    print(s.eval_rpn(tokens))   # 6

    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(s.eval_rpn(tokens))   # 22

if __name__ == '__main__':
    main()
