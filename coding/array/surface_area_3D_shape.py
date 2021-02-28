# On Leetcode: https://leetcode.com/problems/surface-area-of-3d-shapes/

class Solution(object):
    def surface_area(self, grid):
        """
        The way this problem is stated, it is a bit misleading. The main idea consists in
        calculating the total surface area of the irregular shape built sitting cubes of
        1 x 1 x 1 sitting one on top of the other in a tower.
        The overall shape has a number of overlapping areas to be removed from the 
        calcuations of the individual towers.

        Eaxample:
        grid
         1  2
         3  4

        (0,0) tower of height 1, (0,1) tower of height 2
        (1,0) tower of height 3, (1,1) tower of height 4

        grid with tower total surface area (only overlapping top are removed)
         6  10
        14  18

        grid without north and east overlapping surface
         2  6
         8  18
        """
        tsa = 0                                     # total surface area
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                tsa += 6 * grid[i][j]
                if grid[i][j] > 1:
                    tsa -= ((grid[i][j] - 1) * 2)   # got to remove the overlapping surface of the tower
                if i + 1 < len(grid):               # got to remove the overlapping surface with the tower to the south
                    tsa -= 2 * min(grid[i][j], grid[i + 1][j])
                if j + 1 < len(grid[0]):            # got to remove the overlapping surface with the tower to the east
                    tsa -= 2 * min(grid[i][j], grid[i][j + 1])
        
        return tsa

def main():
    s = Solution()

    grid = [[2]]
    print(s.surface_area(grid))     # 10

    grid = [[1,2],[3,4]]
    print(s.surface_area(grid))     # 34

    grid = [[1,0],[0,2]]
    print(s.surface_area(grid))     # 16

    grid = [[1,1,1],[1,0,1],[1,1,1]]
    print(s.surface_area(grid))     # 32

    grid = [[2,2,2],[2,1,2],[2,2,2]]
    print(s.surface_area(grid))     # 46

if __name__ == '__main__':
    main()
