
def sum_to_k(array, k):
    '''
    Main idea consists in leveraging a map to create a sort of lookup index and then
    combine incrementally as we scan through the array. To avoid to count symmetric
    pairs, a set is used to dedup the sum of indexes (which works in the assunption of
    monotonic increasing sequence of indexes).
    '''
    # let's load up an index for quick lookup
    index = {}
    for i, elem in enumerate(array):    # O(N)
        if elem not in index:
            index[elem] = []
        index[elem].append(i)
    # let's use a set to dedup pairs
    dedup = set()
    for i, elem in enumerate(array):    # O(N)
        x = k - elem
        if x in index:
            indexes = index[x]
            for j in indexes:           # O(M)
                # elements with the same index are not considered a valid pair
                if j != i:
                    # let's make sure that we count only distinct pairs
                    dedup.add(i + j)
    return len(dedup)

def main():
    arr = [1, 2, 3, 4, 3]
    print(2, sum_to_k(arr, 6))

    arr = [1, 5, 3, 3, 3]
    print(4, sum_to_k(arr, 6))

if __name__ == '__main__':
    main()
