# On Leetcode: https://leetcode.com/problems/number-of-islands/
# This solution only tries to make use of the already available data structures
# trying, as much as possible, to not create any new one.

class Solution(object):
    def get_directions(self, cell, m, n):
        directions = []
        
        down = (cell[0] + 1, cell[1])
        if down[0] < m:
            directions.append(down)

        up = (cell[0] -1, cell[1])
        if up[0] >= 0:
            directions.append(up)
        
        left = (cell[0], cell[1] - 1)
        if left[1] >= 0:
            directions.append(left)
        
        right = (cell[0], cell[1] + 1)
        if right[1] < n:
            directions.append(right)

        return directions

    def traverse(self, grid, cell):
        if grid[cell[0]][cell[1]] == '0':
            return 0
        
        grid[cell[0]][cell[1]] = 'X'
        for direction in self.get_directions(cell, len(grid), len(grid[0])):
            if grid[direction[0]][direction[1]] != 'X':
                self.traverse(grid, direction)
        
        return 1

    def number_of_islands(self, grid):
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += self.traverse(grid, (i, j))
        
        return islands

def main():
    s = Solution()

    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(s.number_of_islands(grid))

    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(s.number_of_islands(grid))

    grid = [
        ["1","1","0","0","1"],
        ["1","0","0","0","0"],
        ["0","0","1","0","0"],
        ["1","0","0","1","1"]
    ]
    print(s.number_of_islands(grid))

    grid = [
        ["0","0","0","0","0"],
        ["0","0","0","0","0"],
        ["0","0","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(s.number_of_islands(grid))

    grid = [
        ["1","0","0","0","0"],
        ["0","0","0","0","0"],
        ["0","0","0","0","0"],
        ["0","0","0","0","1"]
    ]
    print(s.number_of_islands(grid))

if __name__ == '__main__':
    main()
