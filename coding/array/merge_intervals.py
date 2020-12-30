
# On Leetcode: https://leetcode.com/problems/merge-intervals/

class Solution(object):
    def merge_intervals(self, intervals):
        non_overlapping = []
        for i, x in enumerate(intervals):
            if len(non_overlapping) > 0 and non_overlapping[0][1] >= x[0]:
                prev = non_overlapping.pop()
                non_overlapping.append([prev[0], x[1]]) 
            else:
                non_overlapping.append(x)

        return non_overlapping

def main():
    x = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(x.merge_intervals(intervals))
    intervals = [[1,4],[4,5]]
    print(x.merge_intervals(intervals))
    intervals = [[1,4],[2,4],[4,5]]
    print(x.merge_intervals(intervals))
    intervals = [[1,6],[5,10],[11,14],[19,21]]
    print(x.merge_intervals(intervals))

if __name__ == '__main__':
    main()
