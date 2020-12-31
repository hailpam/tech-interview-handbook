
# Warmup exercise from the theory section. It implements a Maze solver which
# leverages the backtracking to incrementally build its path through the exit

class Maze(object):
    """
    A Maze is represented as a NxM matrix. In terms of convention:
    - X marks the entrance, 
    - Y marks the exit,
    - 1 marks a viable step,
    - 0 marks an unviable step.

    0 0 0 0 0 0 0 0 0
    0 1 1 1 1 1 1 1 0
    0 1 0 0 0 0 0 1 0
    X 1 0 1 1 1 1 1 Y
    0 1 0 1 0 0 0 0 0
    0 1 0 0 0 1 0 0 0
    0 1 1 1 1 1 1 1 0
    0 0 0 0 0 0 0 0 0
    
    For the sake of simplicity, it is assumed that a Maze always has
    a pair of entrance and exit.
    """
    def __init__(self, x, y, matrix):
        """
        Initialize the data structure with the entry and exit points
        as well as the Maze structure.

        x: a pair, containing the coordinates of the entrance
        y: a pair, containing the coordinates of the exit
        matrix: a bidimensional matrix reprensenting the Maze
        """
        self.x = x
        self.y = y
        self.matrix = matrix

class Solution(object):
    def is_exit(self, jonction, exit):
        return jonction == exit
    
    def get_previous_direction(self, jonction, prev):
        mask = [
            False, # was DOWN
            False, # was UP
            False, # was RIGHT
            False  # was LEFT
        ]

        if prev:
            # let's measure the move
            diff = (
                jonction[0] - prev[0],
                jonction[1] - prev[1]
            )

            if diff[0] > 0:     # >0, previously was UP
                mask[1] = True
            elif diff[0] < 0:   # <0, previously was DOWN
                mask[0] = True
            if diff[1] > 0:     # >0, previously was LEFT
                mask[3] = True
            elif diff[1] < 0:   # >0, previously was RIGHT
                mask[2] = True

        return mask
    
    def get_directions(self, jonction, matrix, prev):
        # containers of viable directions
        directions = []
        # check the direction on the path through, to avoid to get back to it
        prev_direction = self.get_previous_direction(jonction, prev)

        # mode DOWN but not coming from DOWN
        down = jonction[0] + 1
        if down <= len(matrix) and not prev_direction[0]:
            elem = matrix[down][jonction[1]]
            if elem != 0:
                directions.append((down, jonction[1]))
        
        # move UP but not coming from UP
        up = jonction[0] - 1
        if up >= 0 and not prev_direction[1]:
            elem = matrix[up][jonction[1]]
            if elem != 0:
                directions.append((up, jonction[1]))
        
        # move RIGHT but not coming from RIGHT
        right = jonction[1] + 1
        if right < len(matrix[0]) and not prev_direction[2]:
            elem = matrix[jonction[0]][right]
            if elem != 0:
                directions.append((jonction[0], right))
        
        # move LEFT but not coming from LEFT
        left = jonction[1] - 1
        if left >= 0 and not prev_direction[3]:
            elem = matrix[jonction[0]][left]
            if elem != 0:
                directions.append((jonction[0], left))

        return directions

    def backtrack(self, jonction, exit, matrix, prev=None):
        if self.is_exit(jonction, exit):
            return True
        directions = self.get_directions(jonction, matrix, prev)
        for direction in directions:
            if self.backtrack(direction, exit, matrix, prev=jonction):
                return True
        return False

    def find_exit(self, maze):
        return self.backtrack(maze.x, maze.y, maze.matrix)

def main():
    s = Solution()

    matrix = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1, 1, 1, 1, 1],
        [0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    m = Maze(x=(3, 0), y=(3, 8), matrix=matrix)
    print(s.find_exit(m))

    matrix = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 1, 0, 0],
        [1, 1, 0, 1, 1, 1, 1, 0, 1],
        [0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    m = Maze(x=(3, 0), y=(3, 8), matrix=matrix)
    print(s.find_exit(m))

    matrix = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 1, 0, 0],
        [1, 1, 0, 0, 1, 1, 1, 1, 1],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    m = Maze(x=(3, 0), y=(3, 8), matrix=matrix)
    print(s.find_exit(m))

if __name__ == '__main__':
    main()
