
# On Leetcode: https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder(object):
    def __init__(self):
        self.sorted_list = []
    
    def add_num(self, num):
        """
        Adds the number in a sorted list, exploited the optimized sorting algorithm
        """
        self.sorted_list.append(num)
        self.sorted_list.sort()

    def find_median(self):
        """
        Implements the running median, accounting for the special case of a single
        element bag.
        """
        size = len(self.sorted_list)
        if size == 1:
            return self.sorted_list[0]
        
        middle = int(size / 2)              # get the middle point, math floor
        if size % 2 == 1:                   # even size, get right the middle
            return self.sorted_list[middle]
        
        return (self.sorted_list[middle] + self.sorted_list[middle - 1]) / 2

def main():
    mf = MedianFinder()

    mf.add_num(1)
    mf.add_num(2)
    print(mf.find_median())     # median = 1.5

    mf.add_num(3)
    print(mf.find_median())     # median = 2

if __name__ == '__main__':
    main()
