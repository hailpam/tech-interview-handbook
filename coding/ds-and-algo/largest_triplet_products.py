
class MaxHeap(object):
    '''
    Alternative is to use the native implementation of Heap as this is less efficient
    (i.e. sorting for each and every insertion). Drawback is: Python does provide a 
    native Min-Heap, not a Max-Heap.
    '''
    def __init__(self, backing=[]):
        self.backing = backing

    def push(self, elem):
        self.backing.append(elem)
        self.backing.sort()

    def top(self):
        if not self.backing:
            return None
        return self.backing[-1]

    def pop(self):
        if not self.backing:
            return None
        return self.backing.pop()

def products(array):
    heap = MaxHeap([])
    prods = []
    temps = []
    for i, elem in enumerate(array):
        heap.push(elem)
        # as per specification, first two elements is simple -1
        if i < 2:
            prods.append(-1)
            continue
        # let's derive the product
        prod = 1
        for _ in range(3):
            temp = heap.pop()
            prod *= temp
            temps.append(temp)
        # let's restore the Heap sequence
        for temp in temps:
            heap.push(temp)
        # let's push the product
        prods.append(prod)
    return prods

def main():
    arr = [1, 2, 3, 4, 5]
    output = [-1, -1, 6, 24, 60]
    print(output, products(arr))

    arr = [2, 1, 2, 1, 2]
    output = [-1, -1, 4, 4, 8]
    print(output, products(arr))

if __name__ == '__main__':
    main()
