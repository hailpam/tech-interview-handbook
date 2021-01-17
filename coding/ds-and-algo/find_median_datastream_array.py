
# On Leetcode: https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder(object):
    """
    This version assumes that the numbers are in the range of 0 and 100.
    """
    
    def __init__(self):
        """
        Initializes a bag with 100 slots to None by default
        """
        self.bag = [None for _ in range(100)]

    def add_num(self, num):
        """
        Puts the numbers to its specific index, setting the slot to the 
        value itself.

        Differently from the sorted version, this operation require only a constant time
        using the number itself as an array index.
        
        Time Complexity: ~O(1) Vs O(NlgN) for the sorted array case
        Space Complexity: ~O(1)
        """
        self.bag[num] = num
    
    def find_median(self):
        """
        Uses the bags to find iteratively the median: having a fixed-size array which 
        might be only discontinuously filled up at any point in time.

        Differently from the sorted version, this operation requires linear time.

        Time Complexity: ~O(N) Vs O(1) for the sorted array case
        Space Complexity: ~O(1)
        """
        size = 0
        last_idx = -1
        for i, e in enumerate(self.bag):
            if e:
                size += 1
                last_idx = i
        
        if size == 1:                       # special case, median is 1st element itself
            return self.bag[last_idx]
        
        middle = int(size / 2)              # get the math floor
        count = 0
        left_middle = 0
        right_middle = 0
        for i, e in enumerate(self.bag):
            if e:
                count += 1
                if count == middle:         # get the left median in an even-sized setup
                    left_middle = self.bag[i]
                if count == middle + 1:     # get the median in an odd-sized setup
                    right_middle = self.bag[i]
        
        return right_middle if size % 2 == 1 else (left_middle + right_middle) / 2

def main():
    mf = MedianFinder()

    mf.add_num(1)
    print(mf.find_median())     # median = 1

    mf.add_num(2)
    print(mf.find_median())     # median = 1.5

    mf.add_num(3)
    print(mf.find_median())     # median = 2

if __name__ == '__main__':
    main()
