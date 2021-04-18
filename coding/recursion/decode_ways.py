# On Leetcode: https://leetcode.com/problems/decode-ways/

from string import ascii_uppercase

class Solution(object):
    def __init__(self):
        self.symbols = {}
        for symbol in ascii_uppercase:
            code = ord(symbol) - (ord('A') - 1)
            self.symbols[code] = symbol
    
    def combine(self, msg, idx=0, combinations=[]):
        combination = []
        if idx < len(msg):
            first = int(msg[idx])
            if first == 0:                              # invalid combination
                return
            if idx + 1 < len(msg):                      # case with size 2 window
                second = int(msg[idx + 1])
                comb = int('%s%s' % (first, second))
                if comb <= 26:
                    combination.extend(msg[:idx])
                    combination.append(comb)
                    combination.extend(msg[idx + 2:])
            else:                                       # case with size 1 window
                combination.extend(msg[:idx])
                combination.append(first)
                combination.extend(msg[idx + 2:])
            if combination:
                combinations.append(combination)
            self.combine(msg, idx+1, combinations)

    def decode(self, s):
        '''
        Main idea: consists in generating all viable combinations of figures to
        be then mapped back

        Using a sliding window approach of size 2:

            226
            ^
             *      size 2 window -> [22, 6]
            
            226
             ^
              *     size 2 window -> [2, 26]

            226
              ^     size 1 window -> [2,2,6]
        
        According to the above sliding logic window, the viable solutions would be: [[22, 6], [2, 26], [2,2,6]]
        '''
        combinations = []
        self.combine(s, idx=0, combinations=combinations)
        if combinations:
            encoded = []
            for combination in combinations:
                s = []
                for code in combination:
                    if int(code) not in self.symbols:            # invalid combination, e.g. contains a 0
                        s.clear()
                        break
                    s.append(self.symbols[int(code)])
                if s:
                    encoded.append(''.join(s))
            return encoded
        return []

def main():
    s = Solution()

    msg = "12"
    combinations = []
    print(s.decode(list(msg)))

    msg = "226"
    combinations = []
    print(s.decode(list(msg)))

    msg = "06"
    combinations = []
    print(s.decode(list(msg)))

    msg = "2267"
    combinations = []
    print(s.decode(list(msg)))

    msg = "1062"
    combinations = []
    print(s.decode(list(msg)))

if __name__ == '__main__':
    main()
