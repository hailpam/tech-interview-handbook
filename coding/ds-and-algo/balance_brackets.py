
balance = {
    ')': '(',
    ']': '[',
    '}': '{'
}

def is_balanced(string):
    # let's use a list as a stack (append() + pop())
    stack = []
    for char in string:
        # it's an opening
        if char not in balance:
            stack.append(char)
        # it's a closing, to be checked with the top of the stack
        else:
            if stack and stack[-1] == balance[char]:
                stack.pop()
    # if the stack is empty, we got a balance
    return not stack

def main():
    s = '{[()]}'
    print(s, True, is_balanced(s))

    s = '{}()'
    print(s, True, is_balanced(s))
    
    s = '{(})'
    print(s, False, is_balanced(s))

    s = ')'
    print(s, False, is_balanced(s))

if __name__ == '__main__':
    main()
