# On Leetcode: https://leetcode.com/problems/largest-triangle-area/

class Solution(object):
    def largest_triangle_area(self, points):
        x_max = -1
        y_max = -1
        for point in points:
            x_max = max(x_max, point[0])
            y_max = max(y_max, point[1])
        
        return x_max * y_max / 2

def main():
    s = Solution()

    points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    print(s.largest_triangle_area(points))

if __name__ == '__main__':
    main()
