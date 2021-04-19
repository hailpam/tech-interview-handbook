# On Leetcode: https://leetcode.com/problems/game-of-life/

MOVES = [
    (-1,0),     # North
    (1,0),      # South
    (0,1),      # West
    (0,-1),     # East
    (-1, 1),    # North West
    (1, 1),     # South West
    (-1,-1),    # North East
    (1,-1)      # South East
]

# TBD - to further work on the in-place update...

class Solution(object):
    def check_neighbors(self, board, i_pos, c_pos=(0,0), count=0, dirs=MOVES):
        if count > 3:                                           # beyond 3, there is no rule, can prune
            return count
        
        if c_pos[0] >= 0 and c_pos[0] < len(board):             # need to stay within the boundaries...
            if c_pos[1] >= 0 and c_pos[1] < len(board[0]):
                if i_pos != c_pos and board[c_pos[0]][c_pos[1]] == 1:
                    count += 1
                while dirs:
                    pos = dirs.pop()                            # got to generate the new position
                    n_pos = (pos[0] + i_pos[0], pos[1] + i_pos[1])
                    count = self.check_neighbors(board, i_pos, n_pos, count=count, dirs=dirs)
                return count
        
        return count

    def is_alive(self, neighbors, is_cell_dead=False):
        if neighbors < 2:                                       # less than 2, under-population
            return False
        if neighbors > 3:                                       # more than 3, over-population
            return False
        if neighbors >= 2 and neighbors <= 3:                   # between 2 and 3, need to live
            if is_cell_dead:
                if neighbors == 3:                              # a dead cell can become alive only when exactly 3 neighbors are active
                    return True
                else:
                    return False
            else:                                               # stay alive!
                return True

    def game_of_life(self, board):
        '''
        Main idea: use a driving nested for loop which scans the board
        and backtracking to visit the neighbooring of any given cell.

        Example:

                0   1   0
                0   0   1
                1   1   1
                0   0   0
        
        (0,1) - got to die, not enough neighboors
        (1,0) - got to live, it got [(2,0), (2,1)]

        Pruning can be applied visitig the neighbooring, according to the 
        specific game rules.

        NOTE neighboor is defined as a cell of distance 1 from the origin
        '''
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                cell = (i,j)
                is_dead = (board[i][j] == 0)
                count = self.check_neighbors(board, cell, c_pos=cell, dirs=list(MOVES))
                if self.is_alive(count, is_cell_dead=is_dead):
                    board[i][j] = 1
                else:
                    board[i][j] = 0

def main():
    s = Solution()

    board = [[1,1],[1,0]]
    s.game_of_life(board)
    print(board)                                        # [[1,1],[1,1]]

    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    s.game_of_life(board)                               # [[1,1],[1,1]]
    print(board)

if __name__ == '__main__':
    main()
