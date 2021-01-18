
# On Leetcode: https://medium.com/algorithm-and-datastructure/index-pairs-of-a-string-7b7c8306ead0

class Solution(object):
    def match(self, text, word, start):
        """
        Tries to match the word with the text from the starting position.
        """
        end = start
        for i, c in enumerate(word):
            if end >= len(text) or c != text[end]:      # iterating on the word, it can go bayond text's length
                return -1
            end += 1                                    # always increments 1 after the match
        
        return end - 1 if end != start else -1

    def index_pairs(self, text, words):
        """
        Tries to match the words with the text string, returning the indexed (start and end)
        defining a substring of the text.

        The algorithm works like it follows:

        ababa {a: [0, 2, 4], b: [1, 3]} aba
        ^          ^
         ^
          ^
        [0, 2]

        ababa {a: [0, 2, 4], b: [1, 3]} aba
          ^           ^
           ^
            ^
        [2, 4]

        ababa {a: [0, 2, 4], b: [1, 3]} aba
            ^            ^
        []
        """
        index = {}
        for i, c in enumerate(text):                    # got to index all characters
            if c not in index:
                index[c] = []
            index[c].append(i)
        
        selection = []
        for word in words:
            c = word[0]
            if c not in index:                          # got a word which starts with a non-indexed char
                continue
            idxs = index[c]
            for start in idxs:                          # got to check, for any start index, if it's matching the word
                end = self.match(text, word, start)
                if end != -1:
                    selection.append([start, end])
        
        return selection

def main():
    s = Solution()

    text = "thestoryofleetcodeandme"
    words = ["story","fleet","leetcode"]
    print(s.index_pairs(text, words))   # [[3,7],[9,13],[10,17]]

    text = "ababa"
    words = ["aba","ab"]
    print(s.index_pairs(text, words))   # [[0,1],[0,2],[2,3],[2,4]]

if __name__ == '__main__':
    main()
