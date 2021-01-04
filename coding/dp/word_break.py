
# On Leetcode: https://leetcode.com/problems/word-break/

class Solution(object):
    def word_break(self, s, word_dict, i=[]):
        """
        Representing a problem as a tree:

                   X
           leet         code
        leet  code   leet   code
               ^
        
        Recursively building the string should allow to verify whether
        a solution is availble or not.
        Stop condition is either the string matches or the built string
        has a size which is greater or equal to the size of the input
        """
        composed_s = ''.join(i)
        if len(composed_s) >= len(s):
            if s == composed_s:
                return True
            else:
                return False
        
        for word in word_dict:
            i.append(word)
            if self.word_break(s, word_dict, i):
                return True
            i.pop()
        
        return False

def main():
    x = Solution()

    s = 'leetcode'
    word_dict = ['leet', 'code']
    print(x.word_break(s, word_dict))

    s = "applepenapple"
    word_dict = ["apple", "pen"]
    print(x.word_break(s, word_dict, []))

    s = "catsandog"
    word_dict = ["cats", "dog", "sand", "and", "cat"]
    print(x.word_break(s, word_dict, []))

    s = 'itisagoodday'
    word_dict = ['it', 'is', 'a', 'good', 'day']
    print(x.word_break(s, word_dict, []))

    s = "catsanddog"
    word_dict = ["cats", "dog", "and"]
    print(x.word_break(s, word_dict, []))

    s = "catsanddog"
    word_dict = ["and", "dog", "cats"]
    print(x.word_break(s, word_dict, []))

if __name__ == '__main__':
    main()
