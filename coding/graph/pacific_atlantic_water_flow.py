
# On Leetcode: https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution(object):
    def get_directions(self, cell, m, n):
        directions = []

        north = (cell[0] - 1, cell[1])
        if north[0] >= 0:
            directions.append(north)
        south = (cell[0] + 1, cell[1])
        if south[0] < m:
            directions.append(south)
        west = (cell[0], cell[1] - 1)
        if west[1] >= 0:
            directions.append(west)
        east = (cell[0], cell[1] + 1)
        if east[1] < n:
            directions.append(east)
        
        return directions
    
    def is_valid_flow_cell(self, grid, cell, m, n):
        """
        A cell is a valid flow only if it's greater or equal than all
        its surroundings.
        """
        for x in [-1, 1]:
            if cell[0] + x >= 0 and cell[0] + x < m:
                v_move_cell = grid[cell[0] + x][cell[1]]
                if grid[cell[0]][cell[1]] < v_move_cell:
                    return False
            if cell[1] + x >= 0 and cell[1] + x < n:
                h_move_cell = grid[cell[0]][cell[1] + x]
                if grid[cell[0]][cell[1]] < h_move_cell:
                    return False
        
        return True

    def traverse(self, matrix, visited, flows, cell=(0,0)):
        visited.add(cell)
        if self.is_valid_flow_cell(matrix, cell, len(matrix), len(matrix[0])):
            flows.append(cell)
        
        for direction in self.get_directions(cell, len(matrix), len(matrix[0])):
            if direction not in visited:
                self.traverse(matrix, visited, flows, direction)

    def pacific_atlantic(self, matrix):
        """
        The problem consists in finding those grid coordinates which
        allow the flow of water bidirectionally, and so:

        2  3  4
        4 (5) 3
        7  1  4

        5 is then considerd a flow-passing point as it is greater of eqaul
        of all possible surrounding coordinates, i.e. 3 (north), 1 (south), 
        4 (west), 3 (east).
        On the other hand, with a flow coming from east:

         2   4 (5)
        (6) (7) 1
        (5)  1  1

        5 and 7 still respect the condition, but 6 and 5 not necessarily. Is this
        even correct?
        """
        visited = set()
        flows = []

        self.traverse(matrix, visited, flows)

        return flows

def main():
    s = Solution()

    matrix = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [5, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]
    ]
    print(s.pacific_atlantic(matrix))

if __name__ == '__main__':
    main()
