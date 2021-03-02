# On Leetcode: 

class Solution(object):
    def move_horizontal(self, start, end, path):
        """
        Move horizontally.
        """
        if start[1] < end[1]:
            for i in range(start[1], end[1] + 1):
                path.append([end[0], i])
        if start[1] > end[1]:
            stop = end[1] + 1 if end[1] > 0 else end[1] - 1
            for i in range(start[1], stop, -1):
                path.append([end[0], i])

    def move_vertical(self, start, end, path):
        """
        Move vertically.
        """
        if start[0] < end[0]:
            for i in range(start[0], end[0] + 1):
                path.append([i,end[1]])
        if start[0] > end[0]:
            stop = end[0] + 1 if end[0] > 0 else end[0] - 1
            for i in range(start[0], stop, -1):
                path.append([i,end[1]])

    def move_diagonal(self, start, end, path):
        """
        Move diagonally taking care of moves to fix the direction.
        """
        vertical = []
        self.move_vertical(start, end, vertical)
        horizontal = []
        self.move_horizontal(start, end, horizontal)

        l_p = min(len(horizontal), len(vertical))
        for i in range(l_p):
            path.append([vertical[i][0],horizontal[i][1]])      # got to merge horizontal and vertical moves

        if len(vertical) != len(horizontal):                    # got to compensate the final move
            path.append([vertical[-1][0],horizontal[-1][1]])

    def min_time_to_all_points(self, points):
        """
        The main idea is to move horizontally, vertically and then combining the moves
        into diagonal moves. 
        With simple arithmetic, it possible to generate the sequence of points on the
        straight lines composing the paths.

        Example: [[1,2],[2,2]]
            move vertically         -> [1,2],[2,2]

        Example: [[1,2],[1,4]]
            move horizontally       -> [1,2],[1,3],[1,4]

        Example: [[1,1],[4,4]]
            move diagonally
                move horizontally   -> [[1,1],[1,2],[1,3],[1,4]]
                move vertically     -> [[1,1],[2,1],[3,1],[4,1]]
                                       [[1,1],[2,2],[3,3],[4,4]]
        
        In cases of mixed moves on a path, e.g. [[1,1],[3,4]] which requires diagonal 
        moves and an horizontal one, it should be managed by the diagonal move to fix
        the trajectory.

        Example: [[1,1],[3,4]]
            move diagonally
                move horizontally   -> [[1,1],[1,2],[1,3],[1,4]]
                move vertically     -> [[1,1],[2,1],[3,1]]
                                       [[1,1],[2,2],[3,3]]
                compensate          -> [[3,4]]  (combine last from horizontal and vertical)
                                       [[1,1],[2,2],[3,3],[3,4]]
        """
        path = []
        for i in range(1, len(points)):
            point = points[i]
            prev = points[i - 1]
            if prev[0] != point[0] and prev[1] != point[1]:     # got x1 != x2 and y1 != y2
                self.move_diagonal(prev, point, path)
            if prev[1] == point[1]:
                self.move_vertical(prev, point, path)           # got y1 == y2
            if prev[0] == point[0]:
                self.move_horizontal(prev, point, path)         # got x1 == x2

        return len(path) - (len(points) - 1)                    # got the remove the very initial start point (included by the algorithm)

def main():
    s = Solution()

    points = [[1,1],[3,4],[-1,0]]
    print(s.min_time_to_all_points(points))

    points = [[3,2],[-2,2]]
    print(s.min_time_to_all_points(points))

if __name__ == '__main__':
    main()
