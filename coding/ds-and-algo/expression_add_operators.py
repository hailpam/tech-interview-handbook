
# On Leetode: https://leetcode.com/problems/expression-add-operators/

class Solution(object):
    def compute(self, l_opnd, r_opnd, optr):
        """
        Helper to compute getting left and righ operands as well as the operator.
        """
        if optr == '+':
            return l_opnd + r_opnd
        elif optr == '-':
            return l_opnd - r_opnd
        else:
            return l_opnd * r_opnd

    def eval(self, expr):
        """
        Helper function to evaluate the expression at the leaf.
        """
        opnd_stack = []
        optr_stack = []
        for char in expr:
            if char in ['+', '-', '*']:
                optr_stack.append(char)
            else:
                opnd_stack.append(int(char))
            
            if len(opnd_stack) == 2:
                r_opnd = opnd_stack.pop()
                l_opnd = opnd_stack.pop()
                optr = optr_stack.pop()
                opnd_stack.append(self.compute(l_opnd, r_opnd, optr))
        
        return opnd_stack[0]
    
    def visit(self, digits, target, idx=0, expr=[], combs=[]):
        """
        Helper function to recursively build the expression alterning the operators and operands.
        """
        expr.append(digits[idx])
        if idx == len(digits) - 1:              # time to check whether it's meeting the target
            if self.eval(expr) == target:
                combs.append(''.join(expr))     # got to add to the combinations as it meets the target
        else:
            for oprt in ['+', '-', '*']:        # evaluate for each operator
                expr.append(oprt)
                self.visit(digits, target, idx + 1, expr, combs)
                expr.pop()
        expr.pop()

    def add_operators(self, num, target):
        """
        The algorithm evolves generating all possible/valid combinations and evaluating those
        against the target.

        Example: 12, 3
        step 0:
        1 + 2, 3

        step 1:
        1 - 2, -1

        step 2:
        1 * 2, 2

        Recursively, the expression string is created and evaluated at the leaf.
        """
        digits = list(num)
        combs = []
        self.visit(digits, target, 0, [], combs)

        return combs

# TBD - add priority for multiplication: ['1+0*5', '1-0*5', '1*0+5']

def main():
    s = Solution()

    num = "123"
    target = 6
    print(s.add_operators(num, target))     # ["1+2+3", "1*2*3"] 

    num = "232"
    target = 8
    print(s.add_operators(num, target))     # ["2*3+2", "2+3*2"]

    num = "105"
    target = 5
    print(s.add_operators(num, target))     # ["1*0+5","10-5"]

    num = "00"
    target = 0
    print(s.add_operators(num, target))     # ["0+0", "0-0", "0*0"]

    num = "3456237490"
    target = 9191
    print(s.add_operators(num, target))     # []

if __name__ == '__main__':
    main()
