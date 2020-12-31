
# On Leetcode: https://leetcode.com/problems/construct-the-rectangle/

# TBD - need to factor the area and then find the best fit

class Solution(object):
    def construct_rectangle(self, area):
        sols = [(area, 1)]
        for x in range(int(area**0.5), area + 1):
            y = area//x
            if x * y == area:
                sols.append((x, y))

        min_dis = sols[0][0] - sols[0][1]
        min_sol = sols[0]
        for sol in sols[1:]:
            dis = sol[0] - sol[1]
            if dis < min_dis:
                min_sol = sol
                min_dis = dis

        return min_sol

def main():
    s = Solution()
    area = 4
    print(s.construct_rectangle(area))
    area = 37
    print(s.construct_rectangle(area))
    area = 122122
    print(s.construct_rectangle(area))

if __name__ == '__main__':
    main()
