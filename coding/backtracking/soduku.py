import time

# Leetcode: https://leetcode.com/problems/sudoku-solver/

class Timer(object):
    def __init__(self):
        self.timestamp = 0
    
    def start(self):
        self.timestamp = time.time() * 10**6
    
    def stop(self):
        return int((time.time() * 10**6 - self.timestamp) / 10**3)

class Sudoku(object):
    def __init__(self, board):
        """
        Sudoku data structure, which represents a board.
        Empty cells are marked as '.'.
        board (matrix): a 9x9 matrix representing
        """
        self.board = board
    
    def pretty_print(self):
        """
        Pretty printing the Sudoku game board
        """
        print('[')
        for row in self.board:
            print('  %s' % row)
        print(']')

class Solution(object):
    def is_cell_editable(self, cell, board):
        return board[cell[0]][cell[1]] == '.'

    def is_valid(self, num, cell, board):
        return self.is_valid_for_row(num, cell, board) and \
               self.is_valid_for_column(num, cell, board) and \
               self.is_valid_for_3x3_submatrix(num, cell, board)

    def is_valid_for_row(self, num, cell, board):
        for i in range(9):
            if num == board[cell[0]][i]:
                return False
        return True

    def is_valid_for_column(self, num, cell, board):
        for i in range(9):
            if num == board[i][cell[1]]:
                return False
        return True

    def get_submatrix_indexes(self, cell):
        submatrices = [
            [(0,0), (2,2)],
            [(3,0), (5,2)],
            [(6,0), (8,2)],
            [(0,3), (2,5)],
            [(3,3), (5,5)],
            [(6,3), (8,5)],
            [(0,6), (2,8)],
            [(3,6), (5,8)],
            [(6,6), (8,8)],
        ]
        for submatrix in submatrices:
            l_bound = submatrix[0]
            u_bound = submatrix[1]
            if cell[0] >= l_bound[0] and cell[1] >= l_bound[1] and \
               cell[0] <= u_bound[0] and cell[1] <= u_bound[1]:
                return l_bound, u_bound

    def is_valid_for_3x3_submatrix(self, num, cell, board):
        x, y = self.get_submatrix_indexes(cell)
        for i in range(x[0], y[0]):
            for j in range(x[1], y[1]):
                if num == board[i][j]:
                    return False
        return True
    
    def get_next_empty(self, board):
        for i in range(0, 9):
            for j in range(0, 9):
                cell = (i, j)
                if self.is_cell_editable(cell, board):
                    return cell
        return ()

    def backtrack(self, board):
        # get next empty slot, if none the it's solved
        empty = self.get_next_empty(board)
        if empty != ():
            # range to find a suitable candidate
            for n in range(1, 10):
                if self.is_valid(str(n), empty, board):
                    board[empty[0]][empty[1]] = str(n)
                    # try the candidate and move on
                    if self.backtrack(board):
                        return True
                    # unset to backtrack in case of unsuccessful setup
                    board[empty[0]][empty[1]] = '.'
            return False
        return True

    def solve_sudoku(self, sudoku):
        return self.backtrack(sudoku.board)

def main():
    t = Timer()
    s = Solution()

    # solution can be found
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    t.start()
    x = Sudoku(board)
    x.pretty_print()
    print('>>> SOLUTION FOUND <<<' if s.solve_sudoku(x) else '>>> UNABLE TO FIND A SOLUTION <<<')
    print('%dms' % t.stop())
    x.pretty_print()

    # cannot find a solution, double 7 in column 4
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","7",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    t.start()
    x = Sudoku(board)
    x.pretty_print()
    print('>>> SOLUTION FOUND <<<' if s.solve_sudoku(x) else '>>> UNABLE TO FIND A SOLUTION <<<')
    x.pretty_print()
    print('%d' % t.stop())

if __name__ == '__main__':
    main()
