# On Leetcode:

class Solution(object):
    def last_stone_weight(self, stones):
        while len(stones) > 1:
            r_min = 10001
            i_r_min = -1
            for i, stone in enumerate(stones):
                if stone < r_min:
                    r_min = stone
                    i_r_min = i
            
            r_max = l_max = r_min               # set to minimum to roll over two max elements
            i_r_max = i_l_max = i_r_min
            for i, stone in enumerate(stones):
                if stone >= r_max:               # got to swap the two rolling max elements
                    l_max = r_max
                    i_l_max = i_r_max
                    r_max = stone
                    i_r_max = i
            
            diff = r_max - l_max                # got to smash the stones
            if diff > 0:
                stones[i_r_max] = diff          # if positive, got to update the element
            stones.pop(i_l_max)                 # got to remove the lower among the max elements
            if diff == 0:
                stones.pop(i_r_max - 1)         # got to remove the highest as well: equal max elements
            
        return len(stones)

def main():
    s = Solution()

    stones = [2,7,4,1,8,1]
    print(s.last_stone_weight(stones))  # 1

if __name__ == '__main__':
    main()
