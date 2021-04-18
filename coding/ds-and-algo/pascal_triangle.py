# On Leetcode: https://leetcode.com/problems/pascals-triangle/

class Solution(object):
    def generate(self, num_rows, triangle=[], idx=0):
        '''
        Main idea: build it recursively.

             [1]
           [1, 1]
          [1, 1, 1]
              ^               1 + 1 = 2
          [1, 2, 1]
         [1, 1, 1, 1]
             ^                1 + 2 = 3
                ^             1 + 2 = 3
         [1, 3, 3, 1]
        [1, 1, 1, 1, 1]
            ^                 1 + 3 = 4
               ^              3 + 3 = 6
                  ^           3 + 1 = 4
        [1, 4, 6, 4, 1]
        '''
        if num_rows > 0:
            elem = []
            for x in range(idx + 1):        # fill this positional bucket with ones
                elem.append(1)
            triangle.append(elem)
            
            if idx > 1:
                for i in range(1, idx):     # generate the working indexed for this positional bucket
                    triangle[idx][i] = triangle[idx - 1][i - 1] + triangle[idx - 1][i]

            self.generate(num_rows-1, triangle=triangle, idx=idx+1)

def main():
    s = Solution()

    num_rows = 5
    triangle = []
    s.generate(num_rows, triangle=triangle)
    print(triangle)     # [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

    num_rows = 3
    triangle = []
    s.generate(num_rows, triangle=triangle)
    print(triangle)     # [[1], [1, 1], [1, 2, 1]]

    num_rows = 1
    triangle = []
    s.generate(num_rows, triangle=triangle)
    print(triangle)     # [[1]]

if __name__ == '__main__':
    main()
