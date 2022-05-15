'''
Quicksort is a sorting algorithm still based on the divide-and-conquer paradigm. Differently
from Mergesort, it does leverage the concept of partitioning and swapping, supported by the
randomisation that this procedure might introduce (i.e. randomised partitioning) with all its
nice-to-have properties. Its average runtime is still O(N log N) where N is the size of the 
array; worth mentioning that the worst case might be O(N^2) which is also the runtime of the
naive sorting algorithms. Worth mentioning that it is an in-place routine which does not need
additional memory to run the merge (like for Mergesort).

Example:

    [2, 1, 6, 4, 3]
     ^ pivot
     ^ leftwall
        ^ element
        ^ leftwall
            ^ element 
               ^ element
                  ^ element

     [1, 2, 6, 4, 3]
         ^ pivot location
    
    [1]
            [6, 4, 3]
             ^ pivot
             ^ leftwall
                ^ elemnt
                ^ leftwall
                    ^ element
                    ^ leftwall
             [3, 4, 6]
    
    [1] [2]  [3, 4, 6]

Reference: https://users.cs.duke.edu/~reif/courses/alglectures/skiena.lectures/lecture5.pdf
'''

def swap(array, i, j):
    '''
    Operates the in-place swaps of the elements to implement the partitioning logic.
    '''
    # let's optimise: we got to swap only in case of i different from j
    if i != j:
        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp

def partition(array, low, high):
    '''
    Once picked the pivot, it does place all elements less than the pivot on the left side, and
    all element greater than the pivot on the right side.
    '''
    # initially, pivot and leftwall will start at the same slot, then leftwall will progress
    pivot = array[low]
    leftwall = low
    # starting from one element far from the pivot
    i = low + 1
    # shift incrementally the elements to create the partial order relationships
    while i < high:
        if array[i] < pivot:
            leftwall += 1
            swap(array, i, leftwall)
        i += 1
    # swap the pivot with the leftwall
    swap(array, low, leftwall)

    return leftwall

def sort(array, low, high):
    '''
    Nests the recursive calls to implement the divide-and-conquer mechanism.
    '''
    # recurse up until the point the pointers are far from each other by 1 slot
    if low < high:
        pivot = partition(array, low, high)
        sort(array, low, pivot - 1)
        sort(array, pivot + 1, high)


def main():
    array = [2, 1, 6, 4, 3]
    cpy_array = list(array)
    sort(array, 0, len(array))
    print(cpy_array, array)

    array = [2, 1, 4, 3]
    cpy_array = list(array)
    sort(array, 0, len(array))
    print(cpy_array, array)

    array = [1]
    cpy_array = list(array)
    sort(array, 0, len(array))
    print(cpy_array, array)

    array = list('mergesort')
    cpy_array = list(array)
    sort(array, 0, len(array))
    print(''.join(cpy_array), ''.join(array))

if __name__ == '__main__':
    main()
