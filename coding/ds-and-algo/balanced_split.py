
def sum(array, i):
    r_sum = 0
    while i < len(array):                                   # O(N - M), M is the number of elements already visited
        r_sum += array[i]
        i += 1
    return r_sum

def split(array):
    # let's sort it first
    array.sort()                                            # O(N log N)
    # let's run and sum incrementally
    r_sum = 0
    for i, elem in enumerate(array):                        # O(N)
        r_sum += elem
        # all elements on the left sum should be smaller than the one on the right sum
        if i + 1 < len(array) and elem < array[i + 1]:
            if sum(array, i + 1) == r_sum:
                return True
    return False

def main():
    arr = [1, 5, 7, 1]
    print(True, split(arr))

    arr = [12, 7, 6, 7, 6]
    print(False, split(arr))

if __name__ == '__main__':
    main()
