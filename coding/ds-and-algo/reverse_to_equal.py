# On Leetcode: https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/

'''
There are multiple alternatives to solve this problem. E.g. levraging sorting and a linear scan, or
even a hashmap (optimal solution with additional O(N) space). Indeed, the problem has expressly asked
to work on the re-arrangement of the subarrays, so the linear probing has been adopted for the solution
below.
'''

def swap(array, i, j):
    # 1-liner swap
    array[i], array[j] = array[j], array[i]

def find(array, elem):
    # alternative is to leverage .index() but it throws an exception
    for i, e in enumerate(array):   # O(N)
        if e == elem:
            return i
    return -1

def reverse_to_equal(a, b):
    # legit to say that different sizes mean different arrays overall
    if len(a) != len(b):
        return False
    # leverage the linear probing
    for i, elem in enumerate(a):    # O(N)
        if elem != b[i]:
            j = find(b, elem)
            if j == -1:
                return False
            swap(b, i, j)
    return True

def main():
    target = [1,2,3,4]
    arr = [2,4,1,3]
    print(True, reverse_to_equal(target, arr))

    target = [7]
    arr = [7]
    print(True, reverse_to_equal(target, arr))

    target = [3,7,9]
    arr = [3,7,11]
    print(False, reverse_to_equal(target, arr))

    target = [1,2,3,4]
    arr = [1,2,3,5]
    print(False, reverse_to_equal(target, arr))

if __name__ == '__main__':
    main()
