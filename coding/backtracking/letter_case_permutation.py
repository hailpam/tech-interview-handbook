
# On Leetcode: https://leetcode.com/problems/letter-case-permutation/

class Solution(object):
    def permute(self, string, permutations, idx=0, permutation=[]):
        for i in range(idx, len(string)):           # upon recursion, it has to only look forward
            c = string[i]                           # let's make a copy of the character
            if not string[i].isnumeric():
                permutation.append(c.lower())       # got to go on lowercase branch
                self.permute(string, permutations, i + 1, permutation)
                permutation.pop()

                permutation.append(c.upper())       # got to go on uppercase branch
                self.permute(string, permutations, i + 1, permutation)
                permutation.pop()

                break                               # got to break here, not needed to go futher (epxlored by recursion)
            else:
                permutation.append(c)               # it's number

        if len(permutation) == len(string):         # got the full length permutated string
            permutations.append(''.join(permutation))
        if permutation:
            permutation.pop()                       # remove actual char unrolling the recursive stack
        
    def letter_case_permutation(self, string):
        """
        The main idea of this algorithm is to build incrementally and recursively,
        adopting backtracking, the permutations of the lower and uppercase letters
        as they present themselves in the string.

        Example: a1b2
            a1
                b2
                B2

            A1
                b2
                B2
        
        Example: a1b2c3
            a1
                b2
                    c3
                    C3
                B2
                    c3
                    C3
            A1
                b2
                    c3
                    C3
                B2
                    c2
                    C3
        """
        permutations = []
        self.permute(string, permutations, 0, [])

        return permutations

def main():
    s = Solution()

    string = 'a1b2'
    print(s.letter_case_permutation(string))

    string = '3z4'
    print(s.letter_case_permutation(string))

    string = 'a1b2c3'
    print(s.letter_case_permutation(string))

    string = '12345'
    print(s.letter_case_permutation(string))

    string = '0'
    print(s.letter_case_permutation(string))
    
if __name__ == '__main__':
    main()
