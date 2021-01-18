
# On Leetcode: https://yangshun.github.io/tech-interview-handbook/algorithms/stack/

class Solution(object):
    """
    For an optimization, the structures on the stack can be managed as class instance
    variables.
    """

    def get_correspondant(self, token):
        """
        Maps closing and opening parenthesis.
        """
        correspondence = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        return correspondence[token]
    
    def check_match(self, top, token):
        """
        Checks the match. It makes use of a dictionary which provides a ~O(1) lookup
        """
        match = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        
        return match[top] == token

    def match_delimiters(self, string):
        """
        Matches the delimiters making use of a stack.
        """
        open_p = ['(', '[', '{']
        close_p = [')', ']', '}']
        tokens = list(string)
        stack = []                                  # got to put on a stack the opening ones
        for token in tokens:
            if token in open_p:                     # got to put the opening on the stack
                stack.append(token)
            if token in close_p:                    # got to check the stack for a proper closure
                top = stack[len(stack) - 1]
                if self.check_match(top, token):    # got to pop only when there is a closure match
                    stack.pop()
                else:                               # got to add the correspondent opening, alternative to halt immediately
                    stack.append(self.get_correspondant(token))

        return len(stack) == 0                      # if size is 0, parenthesis are balanced

def main():
    s = Solution()

    string = '{ac[bb]}'
    print(s.match_delimiters(string))   # True

    string = '[dklf(df(kl)d]{}'
    print(s.match_delimiters(string))   # False

    string = '[dklf(df(kl))d]{}'
    print(s.match_delimiters(string))   # True

    string = '[dklfdf(kl))d]{}'
    print(s.match_delimiters(string))   # False

    string = '{[[[]]]}'
    print(s.match_delimiters(string))   # True

    string = '{3234[fd'
    print(s.match_delimiters(string))   # False

    string = '{3234[f]}d'
    print(s.match_delimiters(string))   # True

    string = '{df][d}'
    print(s.match_delimiters(string))   # False

if __name__ == '__main__':
    main()
