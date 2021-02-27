
# On Leetcode: https://leetcode.com/problems/matrix-block-sum/

class Solution(object):
    def sum(self, matrix, k, answer, i, j):
        row_lb = i - k if i - k > 0 else 0
        row_ub = i + k + 1 if i + k < len(matrix) else len(matrix)          # +1 because of Python's range() function
        col_lb = j - k if j - k > 0 else 0
        col_ub = j + k + 1 if j + k < len(matrix[0]) else len(matrix[0])    # +1 because of Python's range() function

        s = 0                                                               # got to sum on the defined submatrix
        for x in range(row_lb, row_ub):
            for y in range(col_lb, col_ub):
                s += matrix[x][y]
        
        return s

    def matrix_block_sum(self, matrix, k):
        """
        The main idea behind this algorithm is to return a newly built matrix 
        which return for each element (i,j) the sume of the elements in the
        submatrix (c, r) for which i - k <= c <= i + k and j - k <= r <= j + k.

        Example: k = 1
        matrix
            1  2  3
            4  5  6
            7  8  9
        
        answer for i = j = 0
            12
        
        answer for i = 1, j = 0
            12
            27
        
        answer for i = 2, j = 0
            12
            27
            24
        """
        answer = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                answer[i][j] = self.sum(matrix, k, answer, i, j)

        return answer

def main():
    s = Solution()

    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    k = 1
    print(s.matrix_block_sum(matrix, k))

    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    k = 2
    print(s.matrix_block_sum(matrix, k))

if __name__ == '__main__':
    main()
