'''
Mergesort is a sorting algorithm which leverages the divide-and-conquer recursive paradigm. Its runtime
is O(N log N) where N is intended as the number of elements to be sorted. It recursively subdivides the
array, operating a sorted mege upon returning from recursion. The merge phase is fundamental to leverage
partially ordered subarray and combining into a new version of a larger partially oredered subarray, up
until the root of the recursion tree is reached.

Example:

    [2 1 6 4 3]
         ^
    
    [2 1] [4 3]
       ^
    [2]

    [1 2]    ^
           [3 4]
    
    [1 2 3 4 6]
'''

def merge(left, right):
    i, j = 0, 0
    merged = []
    # loop through and re-order with a double pointer, it stops to the shortest
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # loop through any remaining element from the left array
    while i < len(left):
        merged.append(left[i])
        i += 1
    # loop through any remaining element form the right array
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged

def sort(array):
    # array with less than 1 element cannot be further split
    if len(array) <= 1:
        return array
    # pick a pivot more or less in the middle
    pivot = int(len(array) / 2)
    # recurse the split on the left
    left = sort(array[:pivot])
    # recurse the split on the right
    right = sort(array[pivot:])
    # merge linearly
    merged = merge(left, right)
    return merged

def main():
    array = [2, 1, 6, 4, 3]
    print(array, sort(array))

    array = [2, 1, 4, 3]
    print(array, sort(array))

    array = [1]
    print(array, sort(array))

    array = list('mergesort')
    print(''.join(array), ''.join(sort(array)))

if __name__ == '__main__':
    main()
