
# On Leetcode: https://leetcode.com/problems/number-of-islands/

class Solution(object):
    def get_directions(self, cell, m, n):
        directions = []

        if cell[0] + 1 <= m:
            directions.append((cell[0] + 1, cell[1]))
        
        if cell[0] - 1 >= 0:
            directions.append((cell[0] - 1, cell[1]))
        
        if cell[1] + 1 <= n:
            directions.append((cell[0], cell[1] + 1))
        
        if cell[1] - 1 >= 0:
            directions.append((cell[0], cell[1] - 1))

        return directions

    def cluster(self, grid, lands, cell=(0,0)):
        if grid[cell[0]][cell[1]] == '0':
            return 0
        if cell not in lands:
            return 0
        if grid[cell[0]][cell[1]] == '1':
            lands.remove(cell)
        
        for direction in self.get_directions(cell, len(grid), len(grid[0])):
            if direction in lands:
                self.cluster(grid, lands, direction)
        
        return 1


    def number_of_islands(self, grid):
        lands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    lands.add((i, j))
        
        islands = 0
        for land in list(lands):
            islands += self.cluster(grid, lands, land)
        
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

if __name__ == '__main__':
    main()
