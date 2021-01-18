
# On Leetcode: https://leetcode.com/problems/min-stack/

class MinStack(object):
    """
    A Min Stack can be implemented in a number of different ways. For example, a priority queue
    might be used to back the ~O(1) get minimum operation, but this might have an impact on the
    time complexity of a push().

    This implementation pre-computes the min upon insertion. Upon removal of the minim, it
    re-computes the min. This allows a better space complexity (do not require to duplicate
    in a priority queue the elements) and gets a hit on the pop() only whenever the pop()
    involves the actual min, instead of impacting the push() systematically. 
    """

    def __init__(self):
        self.stack = []     # using a list as a stack
        self.min = 10**9    # set the minimum to the max

    def push(self, elem):
        """
        Time Complexity: ~O(1)
        """
        self.stack.append(elem)
        self.__check_min(elem)

    def top(self):
        """
        Time Complexity: ~O(1)
        """
        size = len(self.stack)
        if size > 0:
            return self.stack[size - 1]
        
        return None

    def pop(self):
        """
        Time Complexity: ~O(1) a.c., ~O(N) w.c.
        """
        elem = self.stack.pop()
        if elem == self.min:    # removed the min, got to find the new one
            self.__find_min()
        
        return elem

    def get_min(self):
        """
        Time Complexity: ~O(1)
        """
        return self.min

    def __check_min(self, elem):
        if elem < self.min:
            self.min = elem

    def __find_min(self):
        """
        Time Complexity: ~O(N)
        """
        self.min = 10**9
        for elem in self.stack:
            self.__check_min(elem)

def main():
    ms = MinStack()
    
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    print(ms.get_min())      # -3

    ms.pop()
    ms.top()                # 0
    print(ms.get_min())      # -2

if __name__ == '__main__':
    main()