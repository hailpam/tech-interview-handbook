
# On Leetcode: https://leetcode.com/problems/non-overlapping-intervals/

class Solution(object):
    def is_overlapping(self, x, y):
        return y[1] >= x[0] and x[1] > y[0] 

    def erase_overlap_intervals(self, intervals):
        """
        The solution is assuming the ordering in the example inputs.

        Time Complexity: ~O(N)
        Space Complexity: ~O(1), assuming that the overlap set is far less than
                          the intervals
        """
        overlap = []
        last_nonoverlap = intervals[0]  # keeps track of the last non overlap
                                        # e.g. [[1, 2], [1, 3], [2, 3], [3, 4]]
                                        # in a case lke the above one, 2 overlaps
                                        # would be counted otherwise even if
                                        # [2, 3] and [1, 2] do not overlap, it's
                                        # only [1, 3] overlapping
        for idx in range(1, len(intervals)):
            prev = intervals[idx - 1]
            curr = intervals[idx]
            if self.is_overlapping(prev, curr):
                if self.is_overlapping(last_nonoverlap, curr):
                    overlap.append(curr)
            else:
                last_nonoverlap = prev
        
        return len(overlap)
    
    def erase_overlap_intervals_ooo(self, intervals):
        """
        This solution is able to cope with out of order (OOO) items in the
        intervals.

        Time Complexity: ~O(NlogN)
        Space Complexity: ~O(1), assumig that the overlap set is far less than
                          the intervals
        """
        intervals.sort() # make sure that items are sorted by the first element

        return self.erase_overlap_intervals(intervals)



def main():
    s = Solution()

    intervals = [
        [1,2],
        [2,3],
        [3,4],
        [1,3]
    ]
    print(s.erase_overlap_intervals(intervals))
    print(s.erase_overlap_intervals_ooo(intervals))

    intervals = [
        [1,2],
        [1,2],
        [1,2]
    ]
    print(s.erase_overlap_intervals(intervals))
    print(s.erase_overlap_intervals_ooo(intervals))

    intervals = [
        [1,2],
        [2,3]
    ]
    print(s.erase_overlap_intervals(intervals))
    print(s.erase_overlap_intervals_ooo(intervals))

if __name__ == '__main__':
    main()
