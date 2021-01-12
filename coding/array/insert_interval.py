
# On Leetcode: https://leetcode.com/problems/insert-interval/

class Solution(object):
    def is_overlapping(self, x, y):
        return x[1] >= y[0] and y[1] > x[0]

    def merge(self, overlap, interval):
        lower_bound = 10**6   # 10^5 should be the max
        upper_bound = -1
        for o in overlap:
            lower_bound = min(o[0], lower_bound, interval[0])
            upper_bound = max(o[1], upper_bound, interval[1])
        
        merged = []
        if lower_bound != -1 and interval[0] < lower_bound:
            merged.append(interval[0])
        else:
            merged.append(lower_bound)
        if upper_bound != 10**6 and interval[1] > upper_bound:
            merged.append(interval[1])
        else:
            merged.append(upper_bound)
        
        return merged

    def insert(self, intervals, interval):
        """
        The main idea is to find out what overlaps and what not, 
        merge the overlap and then extends with the non-overlapping.

        Time Complexity: ~O(MlogM), where M is the size of the merged list
        Space Complexity: ~O(P), where P is intended as the longest overlapping
                          or non-overlapping sequence

        To be noted, the sorting can be avoided running a O(M) insertion algorithm
        """
        overlap = []
        non_overlap = []
        for i in intervals:
            if self.is_overlapping(interval, i):
                overlap.append(i)
            else:
                non_overlap.append(i)
        
        merged = self.merge(overlap, interval)
        non_overlap.append(merged)
        non_overlap.sort()

        return non_overlap

def main():
    s = Solution()

    intervals = [
        [1,3],
        [6,9]
    ]
    interval = [2,5]
    print(s.insert(intervals, interval))

    intervals = [
        [1,2],
        [3,5],
        [6,7],
        [8,10],
        [12,16]
    ]
    interval = [4,8]
    print(s.insert(intervals, interval))

    intervals = []
    interval = [5,7]
    print(s.insert(intervals, interval))

    intervals = [
        [1,5]
    ]
    interval = [2,3]
    print(s.insert(intervals, interval))

    intervals = [
        [1,5]
    ]
    interval = [2,7]
    print(s.insert(intervals, interval))

if __name__ == '__main__':
    main()
