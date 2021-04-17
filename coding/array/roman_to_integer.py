# On Leetcode: https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def __init__(self):
        self.symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        self.compounds = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

    def is_for_compound(self, letter):
        return letter in ['I', 'X', 'C']

    def convert(self, string):
        '''
        Main idea: implement a look-ahead logic iteratively.

        MCMXCIV
        ^               1000
         ^*             base of compound, 900
           ^*           base of compound, 90
             ^*         base of compound, 4
        '''
        num = 0
        idx = 0
        while idx < len(string):
            if self.is_for_compound(string[idx]) and idx < len(string) - 1:
                compound = '%s%s' % (string[idx], string[idx + 1])
                if compound in self.compounds:
                    num += self.compounds[compound]
                    idx += 2
                    continue
            num += self.symbols[string[idx]]
            idx += 1

        return num

def main():
    s = Solution()

    string = "III"
    print(s.convert(string))

    string = "IV"
    print(s.convert(string))

    string = "IX"
    print(s.convert(string))

    string = "LVIII"
    print(s.convert(string))

    string = "MCMXCIV"
    print(s.convert(string))

if __name__ == '__main__':
    main()
