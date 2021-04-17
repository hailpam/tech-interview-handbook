# On Leetcode: https://leetcode.com/problems/excel-sheet-column-number/

from string import ascii_uppercase

class Solution(object):
    def __init__(self):
        self.letters = {}
        for x in ascii_uppercase:
            self.letters[x] = ord(x) - 64

    def letter_to_num(self, letter):
        return self.letters[letter]
    
    def column_title_to_num(self, title):
        '''
        Main idea: like in all encoding systems, it is required to compose
        the alphabet letters/numbers positionally.

        A .. Z          -> {1 .. 26}

        AA ... AZ       -> {27 .. 52}
        BA ... BZ       -> {53 .. 78}
           ...       
        ZA ... ZZ       -> {677 .. 702}

        AAA ... AAZ     -> {703 .. 728}
        ABA ... ABZ     -> {729 .. 754}

        To translate into a formula:
        idx:   0         1           2
               A         B           A
        pow:   2         1           0
             26^2 * A + 26^1 * B + 26^0 * A =
         =   26^2 * A + 26^1 * B + 26^0 * A = 
         =    676     +   52     +  1       = 729
        '''
        if len(title) == 1:
            return self.letter_to_num(title)
        summation = 0
        for i, letter in enumerate(title[::-1]):
            summation += self.letter_to_num(letter) * 26**i
        
        return summation


def main():
    s = Solution()

    column_title = "A"
    print(s.column_title_to_num(column_title))  # 1

    column_title = "AB"
    print(s.column_title_to_num(column_title))  # 28

    column_title = "ZY"
    print(s.column_title_to_num(column_title))  # 701

    column_title = "FXSHRXW"
    print(s.column_title_to_num(column_title))  # 2147483647

if __name__ == '__main__':
    main()
