# On Leetcode: https://leetcode.com/problems/spiral-matrix/

class Solution(object):
    def is_explored(self, matrix, cell, explored):
        return matrix[cell[0]][cell[1]] in explored
    
    def get_sticky_direction(self, matrix, cell, explored, direction):
        if not direction:                                           # there is no path yet
            return self.get_direction(matrix, cell, explored)
        d = None                                                    # try to stick on the path
        if direction == 'W':
            d = self.go_west(matrix, cell, explored)
        elif direction == 'E':
            d = self.go_east(matrix, cell, explored)
        elif direction == 'S':
            d = self.go_south(matrix, cell, explored)
        else:
            d = self.go_north(matrix, cell, explored)

        if not d:                                                   # not able to stick on the path
            return self.get_direction(matrix, cell, explored)
        
        return d

    def go_west(self, matrix, cell, explored):
        r = (cell[0], cell[1] + 1)
        if r[1] < len(matrix[0]) and not self.is_explored(matrix, r, explored):    # can move right?
            return (r, 'W')
        return None

    def go_east(self, matrix, cell, explored):
        l = (cell[0], cell[1] - 1)
        if l[1] >= 0 and not self.is_explored(matrix, l, explored):                 # can move left?
            return (l, 'E')
        return None

    def go_south(self, matrix, cell, explored):
        d = (cell[0] + 1, cell[1])
        if d[0] < len(matrix) and not self.is_explored(matrix, d, explored):       # can move down?
            return (d, 'S')
        return None

    def go_north(self, matrix, cell, explored):
        u = (cell[0] - 1, cell[1])
        if u[0] >= 0 and not self.is_explored(matrix, u, explored):                 # can move up?
            return (u, 'N')
        return None

    def get_direction(self, matrix, cell, explored):
        w = self.go_west(matrix, cell, explored)
        if w:
            return w
        e = self.go_east(matrix, cell, explored)
        if e:
            return e
        s = self.go_south(matrix, cell, explored)
        if s:
            return s
        n = self.go_north(matrix, cell, explored)
        if n:
            return n
        
        return None

    def visit(self, matrix, cell, explored, direction=None):
        explored.append(matrix[cell[0]][cell[1]])                   # add the cell to explored
        d  = self.get_sticky_direction(matrix, cell, explored, direction)
        if d:                                                       # if anything to still visit, go for it
            self.visit(matrix, d[0], explored, d[1])

    def find_spiral_matrix(self, matrix, cell=(0,0)):
        '''
        Main idea: use a recursive visit which gets sticky directions from
        within the matrix. I.e. if the move is towards west, keep going untile
        possible.
        The visited set allows to not come back on our own steps.

        1 -> 2 -> 3
                  |
        4 -> 5    6
        |         |
        7 <- 8 <- 9

        At 3 and then at 9, the direction need to change. Same happens at 7 and 4. 
        When at 5, there is no further direction as all sorroundings have been already
        explored.
        '''
        explored = []
        self.visit(matrix, cell, explored)

        return explored

def  main():
    s = Solution()

    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(s.find_spiral_matrix(matrix))             # [1,2,3,6,9,8,7,4,5]

    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(s.find_spiral_matrix(matrix))             # [1,2,3,4,8,12,11,10,9,5,6,7]

if __name__ == '__main__':
    main()
