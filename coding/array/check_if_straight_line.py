# On Leetcode: https://leetcode.com/problems/check-if-it-is-a-straight-line/

class Solution(object):
    def check_straight_line(self, coordinates):
        """
        Having x and y for each point, it is possible to derive the proportionality:

            y = mx + q, y - x = mx - x + q, y - x = x (m - 1) + q 

        (1,2) => 2 - 1 = 1
        (2,3) => 3 - 2 = 1
        ...
        (6,7) => 7 - 6 = 1
        ...
        (7,7) => 7 - 7 = 0

        Last coordinate is on a different line.
        """
        diffs = set()
        for coordinate in coordinates:
            diffs.add(coordinate[1] - coordinate[0])
            
        return len(diffs) == 1

def main():
    s = Solution()

    coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    print(s.check_straight_line(coordinates))

    coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
    print(s.check_straight_line(coordinates))

if __name__ == '__main__':
    main()
