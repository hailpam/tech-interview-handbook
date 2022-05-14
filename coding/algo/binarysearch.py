
'''
Binary search is a convenient O(log N) search algorith which operates in the hypothesis
of search array. It recursively divides by an half the array, to narrow the search space.

Example: search for 2
    
    [ 1 2 3 4 5 6 7 8 9 10 ]
                ^
    
    [ 1 2 3 4 5 6 7 8 9 10 ]
          ^

    [ 1 2 3 4 5 6 7 8 9 10 ]
        ^
'''

def bs(array, element):
    '''
    Possible optimisation: instead of slicing the array (copy every time), take in input an
    index to re-focus the research upon any recursion.
    '''
    if len(array) > 0:
        # pick a pivot
        middle = int(len(array) / 2)
        # check the pivot
        if array[middle] == element:
            return array[middle]
        # in case not found, recurse right
        found = bs(array[:middle], element)
        if found != -1:
            return found
        # in case not found, recurse left
        found = bs(array[middle + 1:], element)
        if found != -1:
            return found
    return -1

def main():
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
    element = 2
    print(element, bs(array, element))

    element = 1
    print(element, bs(array, element))

    element = 0
    print(element, bs(array, element))

    element = 6
    print(element, bs(array, element))

    element = 7
    print(element, bs(array, element))

    element = 10
    print(element, bs(array, element))

    element = 11
    print(element, bs(array, element))

if __name__ == '__main__':
    main()
