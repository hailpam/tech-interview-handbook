# On Leetcode: https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution(object):
    def check_backward(self, a, k, idx=0):
        """
        Expand the research backward, reporting count and remaining change ups.
        """
        if idx < 0:
            return 0, k
        if k == 0 and a[idx] == 0:
            return 0, 0
        if a[idx] == 0:
            k = k - 1
        c, r = self.check_backward(a, k, idx - 1)
        return 1 + c, r
    
    def check_forward(self, a, k, idx=0):
        """
        Expang the research forward, reporitng count and remaining change ups.
        """
        if idx > len(a) - 1:
            return 0, k
        if k == 0 and a[idx] == 0:
            return 0, 0
        if a[idx] == 0:
            k = k - 1
        c, r = self.check_forward(a, k, idx + 1)
        return 1 + c, r

    def longest_ones(self, a, k):
        """
        The main idea consists in expanding the sequence first forward and then backward.
        In particular, it is extended backward in case the forward navigation has still
        have some change up value.

        Example: [0 1 1 1 0], k = 2

            0 1
                1 c=1,k=2
                1 c=2,k=2
                    1 c=3,k=2
                    0 c=4,k=1
            0 1
            0 c=5,k=0
        
        Final counts: c=5, k=0.
        """
        longest = -1
        for i, e in enumerate(a):
            if e == 1:
                l_f, r = self.check_forward(a, k, i + 1)
                l_b, _ = self.check_backward(a, r, i - 1)
                if (l_f + l_b + 1) > longest:
                    longest = l_f + l_b + 1
        
        return longest

def main():
    s = Solution()

    a = [1,1,1,0,0,0,1,1,1,1,0]                     # 6
    k = 2
    print(s.longest_ones(a, k))

    a = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]     # 10
    k  = 3
    print(s.longest_ones(a, k))

if __name__ == '__main__':
    main()
