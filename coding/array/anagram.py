
# On Leetcode: https://leetcode.com/problems/valid-anagram/

class Solution(object):
    def count_char(self, s):
        char_count_s = {}
        for c in list(s):
            if c not in char_count_s:
                char_count_s[c] = 1
            char_count_s[c] += 1

        return char_count_s

    def is_anagram(self, s, t):
        count_s = self.count_char(s)
        count_t = self.count_char(t)

        if len(count_s) != len(count_t):
            return False
        else:
            for c in count_s:
                if c not in count_t or count_s[c] != count_t[c]:
                    return False
        
        return True
    
    # alternative solution is considering strings as UTF-8 encoded
    # and use a 256 slots array to count the characters

def main():
    x = Solution()
    s = "anagram"
    t = "nagaram"
    print(x.is_anagram(s, t))
    s = "rat"
    t = "car"
    print(x.is_anagram(s, t))
    s = "aaa"
    t = "bab"
    print(x.is_anagram(s, t))

if __name__ == '__main__':
    main()
