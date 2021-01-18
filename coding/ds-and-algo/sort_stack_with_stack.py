
# On GeeksForGeeks: https://www.geeksforgeeks.org/sort-stack-using-temporary-stack/

class Solution(object):
    def insert_sorted(self, output, stack, elem):
        """
        Using a support stack, it makes sure to insert the element in the right position 
        in the output array.
        """
        if output:
            top = output[-1]
            if elem < top:              # got to find the right place
                stack.append(output.pop())
                self.insert_sorted(output, stack, elem)
                output.append(stack.pop())
            else:                       # got to its place
                output.append(elem)
        else:                           # got to fill it up
            output.append(elem)

    def sort_stack(self, elems):
        """
        Elements are supposed to be stored in a list that is going to be used as a stack.
        A support stack is used to build the output sorted stack.
        """
        stack = []
        output = []
        size = len(elems)
        idx = 0
        while idx < size:               # got to use the list as a stack, so the while loop on index
            elem = elems.pop()
            self.insert_sorted(output, stack, elem)
            idx += 1

        return output

def main():
    s = Solution()

    stack = [34, 3, 31, 98, 92, 23]
    print(s.sort_stack(stack))  # [3, 23, 31, 34, 92, 98]

    stack = [3, 5, 1, 4, 2, 8]
    print(s.sort_stack(stack))  # [1, 2, 3, 4, 5, 8]

if __name__ == '__main__':
    main()
