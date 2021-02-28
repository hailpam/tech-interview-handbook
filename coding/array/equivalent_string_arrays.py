# On Leetcode: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution(object):
    def are_string_arrays_equivalent(self, word1, word2):
        return ''.join(word1) == ''.join(word2)

    def are_string_arrays_equivalent_no_join(self, word1, word2):
        s_word1 = ''
        for word in word1:
            s_word1 += word
        
        s_word2 = ''
        for word in word2:
            s_word2 += word

        return s_word1 == s_word2

def main():
    s = Solution()

    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    print(s.are_string_arrays_equivalent(word1, word2))
    print(s.are_string_arrays_equivalent_no_join(word1, word2))

    word1 = ["a", "cb"]
    word2 = ["ab", "c"]
    print(s.are_string_arrays_equivalent(word1, word2))
    print(s.are_string_arrays_equivalent_no_join(word1, word2))

    word1  = ["abc", "d", "defg"]
    word2 = ["abcddefg"]
    print(s.are_string_arrays_equivalent(word1, word2))
    print(s.are_string_arrays_equivalent_no_join(word1, word2))

if __name__ == '__main__':
    main()
