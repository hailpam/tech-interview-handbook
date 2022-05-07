# From Meta interview

'''
Find the intersection between two sorted arrays

Example:
    [1 2 3 4 5]
    [2 3 7 8 9 10]
    [2 3]

    [1 2 3 4 5]
    [2 5 7 8 9 10]
    [2 5]

    [1 2 3 4 5]
    []
    []

Questions:
    1. may the array be empty? Y
    2. either the two? Y
    3. may the array have duplicates? N
    4. are all elements in the array contiguous? N
    5. has intersection be contiguous? N

Viable solutions:
    1. based on binary search: O(N log M), N = length of first array, M = length of second array (used for comparison)
    2. based on hashmap: X = max(N, M), O(X)

Debug:
    [1 2 3 4 5], [2 3 7 8 9 10]:
        {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}, {2: 1, 3: 1, 7: 1, 8: 1, 9: 1, 10: 1}
        l_dict = {2: 1, 3: 1, 7: 1, 8: 1, 9: 1, 10: 1}
        s_dict = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
        [2, 3]
    
    [1 2 3 4 5], [2 5 7 8 9 10]:
        {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}, {2: 1, 5: 1, 7: 1, 8: 1, 9: 1, 10: 1}
        l_dict = {2: 1, 5: 1, 7: 1, 8: 1, 9: 1, 10: 1}
        s_dict = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
        [2, 5]
    
    [1 2 3 4 5], []:
        []
'''

def index(array):
    dict = {}
    for num in array:
        if num not in dict:
            dict[num] = 0
        dict[num] += 1
    return dict

def intersect(arr1, arr2):
    intersection = []
    # check if any of the two is empty: no intersection
    if len(arr1) == 0 or len(arr2) == 0:
        return intersection
    # create the indexes from the arrays
    d_arr1 = index(arr1)    # O(N), N = length of array 1
    d_arr2 = index(arr2)    # O(M), M = length of array 2
    # check the longer dictionary to use as lookup
    if len(d_arr1) == len(d_arr2) or len(d_arr1) > len(d_arr2):
        l_dict = d_arr1
        s_dict = d_arr2
    else:
        l_dict = d_arr2
        s_dict = d_arr1
    # implement the search logic
    for key in l_dict:      # X = max(N, M), O(X)
        if key in s_dict:
            intersection.append(key)
    return intersection

def main():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 3, 7, 8, 9, 10]
    print(arr1, arr2, intersect(arr1, arr2))

    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 5, 7, 8, 9, 10]
    print(arr1, arr2, intersect(arr1, arr2))

    arr1 = [1, 2, 3, 4, 5]
    arr2 = []
    print(arr1, arr2, intersect(arr1, arr2))

if __name__ == '__main__':
    main()
