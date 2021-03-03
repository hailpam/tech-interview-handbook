
# On Leetcode: https://leetcode.com/problems/count-sorted-vowel-strings/

class Solution(object):
    def __init__(self):
        self.vowels = {
            'a': 0,
            'e': 1,
            'i': 2,
            'o': 3,
            'u': 4
        }

    def build(self, strings, n, idx=0, string=[]):
        """
        Backtracking helper. It allows to build the lexicographically sorted list
        of elements.
        """
        if idx == n:
            strings.append(''.join(string))
            return
            
        for vowel in self.vowels:
            if string and self.vowels[vowel] < self.vowels[string[-1]]:  # got a vowel which is lexicographically less than the current one
                continue
            
            string.append(vowel)
            self.build(strings, n, idx + 1, string)
            string.pop()

    def count_vowel_strings(self, n):
        """
        Typical application of backtracking. It is required to combine recursively
        in order to create valid sequences to be then counted.

        Example: n = 2
        a
          a
        "aa"
          e
        "ae"
          i
        "ai"
          o
        "ao"
          u
        "au"
        e
          a
          e
        "ee"
          i
        "ei"
          o
        "eo"
          u
        "eu"

        Time Complexity: ~O(m^n), where m = #vowels
        Space Complexity: ~O(m^n)

        To be noted that the constraint of considering only lexicographically sorted
        sequences reduces drastically the time and space complexity. 
         """
        strings = []
        self.build(strings, n)

        return len(strings)

def main():
    s = Solution()

    n = 1
    print(s.count_vowel_strings(n))

    n = 2
    print(s.count_vowel_strings(n))
    
    n = 3
    print(s.count_vowel_strings(n))

    n = 33
    print(s.count_vowel_strings(n))

if __name__ == '__main__':
    main()
