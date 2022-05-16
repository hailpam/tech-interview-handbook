'''
A Stack is a Last-In First-Out (LIFO) data structure which is flexible enought to be largely
adopted (it supports a number of algorithms).
'''

class Stack(object):
    '''
    A Stack implementation based on a list.
    '''
    def __init__(self):
        self.array = []

    def top(self):
        '''
        Returns (without removing) the last element.
        '''
        if not self.array:
            return None
        return self.array[len(self.array) - 1]

    def pop(self):
        '''
        Returns the last element.
        '''
        if not self.array:
            return None
        return self.array.pop()

    def add(self, elem):
        '''
        Adds an element.
        '''
        self.array.append(elem)
    
    def contains(self, elem):
        '''
        Checks whether the data structure contains the given element.
        '''
        return elem in self.array

def main():
    stack = Stack()
    stack.add(10)
    stack.add(11)
    stack.add(12)
    stack.add(13)
    
    print(13, stack.top())
    print(13, stack.pop())
    print(12, stack.top())
    print(12, stack.pop())

    print(True, stack.contains(10))
    print(False, stack.contains(100))

if __name__ == '__main__':
    main()
