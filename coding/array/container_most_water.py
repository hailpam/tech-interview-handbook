
# On Leetcode: https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def max_area(self, heights):
        area = 0
        for i, x in enumerate(heights):
            for j, y in enumerate(heights):
                a = (j - i) * min(x, y)
                if a > area:
                    area = a
        
        return area

def main():
    s = Solution()
    heights = [1,8,6,2,5,4,8,3,7]
    print(s.max_area(heights))
    heights = [1,1]
    print(s.max_area(heights))
    heights = [4,3,2,1,4]
    print(s.max_area(heights))
    heights = [1,2,1]
    print(s.max_area(heights))

if __name__ == '__main__':
    main()
