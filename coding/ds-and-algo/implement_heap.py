import random

# On Leetcode: https://yangshun.github.io/tech-interview-handbook/algorithms/heap/

class Heap(object):
    """
    A Heap is a sorted data structure. A naive implementaion can be made by
    using an array as backing data structure which is heapified upon any 
    addition.
    
    It can also be a special tree data structure which keep the heap invariant
    among operations of addition and removal of elements.
    """

    def __init__(self, min_heap=True):
        """
        Naive implemntation backed by a sorted list.
        """
        self.heap = []
        self.min_heap = min_heap
    
    def __heapify(self):
        if self.min_heap:
            self.heap.sort(reverse=True)    # to make sure that min can be popped out
        else:
            self.heap.sort()
    
    def add(self, x):
        self.heap.append(x)
        self.__heapify()
    
    def pop(self, k=1):
        elems = []
        for _ in range(k):
            elems.append(self.heap.pop())
        
        return elems
    
    def min(self):
        if self.min_heap:
            return self.heap[len(self.heap) - 1]
        
        return self.heap[0]

    def max(self):
        if self.min_heap:
            return self.heap[0]
        
        return self.heap[len(self.heap) - 1]

def main():
    min_heap = Heap()
    max_heap = Heap(False)

    for _ in range(100):
        min_heap.add(random.randint(0, 1000))
        max_heap.add(random.randint(0, 1000))
    
    print(min_heap.heap)
    print(min_heap.min(), min_heap.max())
    print(min_heap.pop(3))
    print(min_heap.min(), min_heap.max())

    print(max_heap.heap)
    print(max_heap.min(), max_heap.max())
    print(max_heap.pop(3))
    print(max_heap.min(), max_heap.max())

if __name__ == '__main__':
    main()
