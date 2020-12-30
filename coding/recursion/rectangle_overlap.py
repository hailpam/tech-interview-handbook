
# On Leetcode: https://leetcode.com/problems/rectangle-overlap/

class Solution(object):
    def is_intersecting(self, rec1, rec2):
        if rec1[0] < rec2[0] and rec1[1] <= rec2[1]:
            # rec1 is aligned left on the x-axis
            return rec1[2] > rec2[0] and rec1[3] > rec2[1]
        else:
            # rec2 is aligned left on the x-axis
            return rec2[2] > rec1[0] and rec2[3] > rec1[1]
    
    def is_rectangle_overlap(self, rec1, rec2):
        return self.is_intersecting(rec1, rec2)

def main():
    s = Solution()
    rec1 = [0,0,2,2]
    rec2 = [1,1,3,3]
    print(s.is_rectangle_overlap(rec1, rec2))
    rec1 = [0,0,1,1]
    rec2 = [1,0,2,1]
    print(s.is_rectangle_overlap(rec1, rec2))
    rec1 = [0,0,1,1]
    rec2 = [2,2,3,3]
    print(s.is_rectangle_overlap(rec1, rec2))
    rec1 = [1,1,3,3]
    rec2 = [0,0,2,2]
    print(s.is_rectangle_overlap(rec1, rec2))
    rec1 = [0,0,3,3]
    rec2 = [1,0,3,3]
    print(s.is_rectangle_overlap(rec1, rec2))
    rec1 = [1,0,3,3]
    rec2 = [0,0,3,3]
    print(s.is_rectangle_overlap(rec1, rec2))

if __name__ == '__main__':
    main()
