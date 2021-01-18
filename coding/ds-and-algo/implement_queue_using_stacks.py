
# On Leetcode: https://leetcode.com/problems/implement-queue-using-stacks/

class Queue(object):
    """
    Implements a FIFO data structure using two LIFO stacks. The main difference among the two
    consists in having always on the top (last element of the stack) the very first
    inserted one.
    """
    def __init__(self):
        self.queue = []
        self.stack = []

    def push(self, elem):
        if self.queue:          # got to rebuild the queue, as this one is the last arrived
            size = len(self.queue)
            idx = 0
            while idx < size:   # got to fill up the stack to reverse the order
                self.stack.append(self.queue.pop())
                idx += 1
            self.stack.append(elem)
            size = len(self.stack)
            idx = 0
            while idx < size:   # got to refill the queue to have the first arrived on top of the stack
                self.queue.append(self.stack.pop())
                idx += 1
        else:                   # got to fill it up with the first element
            self.queue.append(elem)

    def pop(self):
        if self.queue:
            return self.queue.pop()
        
        return None

    def peek(self):
        return self.queue[-1]

    def empty(self):
        return len(self.queue) == 0

def main():
    q = Queue()

    q.push(1)           # queue is: [1]
    q.push(2)           # queue is: [1, 2] (leftmost is front of the queue)
    print(q.peek())     # return 1
    print(q.pop())      # return 1, queue is [2]
    print(q.empty())    # return False

if __name__ == '__main__':
    main()
