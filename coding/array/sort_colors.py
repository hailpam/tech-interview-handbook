# On Leetcode: https://leetcode.com/problems/sort-colors/

class Solution(object):
    def shift_left(self, colors, i, j):
        while j >= 0 and colors[i] < colors[j]:
            tmp = colors[j]
            colors[j] = colors[i]
            colors[i] = tmp
            i -= 1
            j -= 1
    
    def sort_colors(self, colors):
        '''
        Main idea: without using a sorting algorith, it is possible to sort
        the array of colors implementing a shift left logic which swaps 
        incrementally until the end of the array in the worst case.
        '''
        for i in range(1, len(colors)):
            curr = colors[i]
            prev = colors[i - 1]
            if curr < prev:
                self.shift_left(colors, i, i - 1)

def main():
    s = Solution()

    colors = [2,0,2,1,1,0]
    s.sort_colors(colors)
    print(colors)               # [0,0,1,1,2,2]

    colors = [2,0,1]
    s.sort_colors(colors)
    print(colors)               # [0,1,2]

    colors = [0]
    s.sort_colors(colors)       # [0]
    print(colors)

    # colors = [1]
    s.sort_colors(colors)
    # print(colors)

if __name__ == '__main__':
    main()
