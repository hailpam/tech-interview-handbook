
# On Leetcode: https://leetcode.com/problems/count-of-matches-in-tournament/

class Solution(object):
    def count_matches_tournament(self, n):
        if n == 2:
            return 1

        nr_matches = 0
        if n % 2 == 0:
            nr_matches = n / 2
            nr_matches += self.count_matches_tournament(nr_matches)
        else:
            nr_matches = ((n - 1) / 2)
            # 1 team randomnly advances
            nr_matches += self.count_matches_tournament(nr_matches + 1)
        
        return nr_matches

def main():
    s = Solution()

    n = 7
    print(s.count_matches_tournament(n))
    n = 14
    print(s.count_matches_tournament(n))

if __name__ == '__main__':
    main()
