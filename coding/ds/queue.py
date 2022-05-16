'''
A Queue is a First-In First-Out (FIFO) data structure which is flexible enought to be largely
adopted (it supports a number of algorithms).
'''

class Queue(object):
    '''
    A Queue implementation based on a list.
    '''
    def __init__(self):
        self.array = []

    def top(self):
        '''
        Returns (without removing) the last element.
        '''
        if not self.array:
            return None
        return self.array[0]

    def pop(self):
        '''
        Returns the last element.
        '''
        if not self.array:
            return None
        # Note: this might be optimised with a different backing data structure (such pop(x) is not O(1))
        return self.array.pop(0)

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
    stack = Queue()
    stack.add(10)
    stack.add(11)
    stack.add(12)
    stack.add(13)
    
    print(10, stack.top())
    print(10, stack.pop())
    print(11, stack.top())
    print(11, stack.pop())

    print(False, stack.contains(10))
    print(False, stack.contains(11))
    print(True, stack.contains(12))

if __name__ == '__main__':
    main()
