# On Leetcode: https://leetcode.com/problems/sort-characters-by-frequency/

from functools import cmp_to_key

class Solution(object):
    def compare(self, left, right):
        if left[1] < right[1]:
            return -1
        elif left[1] > right[1]:
            return 1
        else:
            if left[0] < right[0]:
                return 1
            elif left[0] > right[0]:
                return -1
            else:
                return 0
    
    def to_string(self, pairs):
        string = ''
        for pair in pairs:
            string += pair[1] * pair[0]
        
        return string

    def frequency_sort(self, string):
        counts = {}
        for char in string:
            if char not in counts:
                counts[char] = 0
            counts[char] += 1
        
        pairs = []
        for key in counts:
            pairs.append((key, counts[key]))
        
        pairs.sort(key=cmp_to_key(self.compare), reverse=True)

        return self.to_string(pairs)

def main():
    s = Solution()

    string = 'tree'
    print(s.frequency_sort(string))     # eert

    string = 'trrees'
    print(s.frequency_sort(string))     # eerst

    string = 'cccaaa'
    print(s.frequency_sort(string))     # aaaccc

    string = 'Aabb'
    print(s.frequency_sort(string))     # bbAa

if __name__ == '__main__':
    main()
