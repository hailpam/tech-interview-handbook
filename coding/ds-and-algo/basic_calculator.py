
# On Leetcode: https://leetcode.com/problems/basic-calculator/

# TBD - nested parenthesis and double-digit numbers

class Solution(object):
    OPERATORS = ['+', '-', '/', '*']

    def compute(self, l_opnd, r_opnd, optr):
        """
        Performs the computation given the operands and operators.
        """
        if optr == '+':
            return l_opnd + r_opnd
        elif optr == '-':
            return l_opnd - r_opnd
        elif optr == '/':
            return l_opnd / r_opnd
        else:
            return l_opnd * r_opnd

    def search_closure(self, chars, start_idx, end_idx):
        """
        Iteratively tires to find the match between opening and closing of parenthesis.
        """
        p_open = 1
        for idx, char in enumerate(chars[start_idx + 1:end_idx]):
            if char == '(':
                p_open += 1
            if char == ')':
                p_open -= 1
            if p_open == 0:
                return start_idx + 1, start_idx + idx + 1

    def evaluate(self, chars, start_idx, end_idx):
        """
        Evaluation function which determines a stack-based computation for the infix notation.
        It assumes well-formed strings.
        """
        opnd_stack = []
        optr_stack = []
        idx = start_idx
        while idx < end_idx:                        # this approach works for single-digit numbers
            char = chars[idx]

            if char == '(':                         # got to nest the recursion due to the presence of parenthesis
                s, e = self.search_closure(chars, idx, end_idx)
                opnd_stack.append(self.evaluate(chars, s, e))
                idx = e
            else:                                   # got to load the stacks up
                if char not in self.OPERATORS:
                    opnd_stack.append(int(char))
                else:
                    optr_stack.append(char)
            
            if len(opnd_stack) == 2:                # got to evaluate: operand stack is sized to 2
                r_opnd = opnd_stack.pop()
                l_opnd = opnd_stack.pop()
                optr = optr_stack.pop()
                opnd_stack.append(self.compute(l_opnd, r_opnd, optr))
            
            idx += 1

        return opnd_stack[0]

    def calculate(self, string):
        """
        Differerntly from the RPN (Reverse Polish Notation), the strings make use of an infix
        notation, which makes things a bit trickier. 
        The main idea, consists in computing using 2 stacks: one for the operands and another
        one for the operators.

        Example: 1 + 3
        step 0:
        operands = [1], operators[]

        step 1:
        operands = [1], operators[+]

        step 2:
        operands = [1,3], operators[+]

        step 3:
        right_operand = pop(operands)
        left_operand = pop(operands)
        operator = pop(operators)
        eval(left_operand, right_operand, operator

        step 4:
        operands = [4], operators[]

        This approach just works and reuses the principle which can be adopted for the RPN of
        evaluation based on a stack.

        Those expressions with parenthesis are evaluated recursively using the same logic:

        Example: 1 + (2 + 1)
        step 0:
        eval(1 + (2 + 1))

        step 1:
        eval(2 + 1)

        step 2:
        eval(1 + 3)

        This evaluation process will e clearer looking at the code.
        """
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

    string = " 8-(3/1) + (2*3) "
    print(s.calculate(string))  # 11

    string = "(1+(4+5+2)-3)+(6+8)"
    print(s.calculate(string))  # 23

    string = "(1+(4+5+(2-1))-3)+(6+8)"
    print(s.calculate(string))  # 22
    
if __name__ == '__main__':
    main()
