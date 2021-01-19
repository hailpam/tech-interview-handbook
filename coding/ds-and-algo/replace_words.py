
# On Leetcode: https://leetcode.com/problems/replace-words/

class Trie(object):
    class Node(object):
        def __init__(self):
            self.children = {}

    class Value(object):
        def __init__(self, successor, count=0):
            self.successor = successor
            self.count = count

    def __init__(self):
        self.root = Trie.Node()
    
    def insert(self, word):
        self.__add(self.__dedup(list(word)), self.root, 0)

    def prefix(self, word):
        prefix = self.__find(list(word), self.root, 0)
        return ''.join(prefix) if prefix else None

    def pretty_print(self):
        print('<>')
        self.__print(self.root, 1)
    
    def __dedup(self, chars):
        prev = None
        for char in chars:
            if prev and prev != char:       # got a difference, returning immediately
                return chars
            prev = char
            
        return [chars[0]]                   # all equal, returning the first character

    def __add(self, chars, root, idx=0):
        char = chars[idx]
        if char not in root.children:
            root.children[char] = Trie.Value(Trie.Node())
        if idx == len(chars) - 1:
            root.children[char].count += 1
            return
        self.__add(chars, root.children[char].successor, idx + 1)
    
    def __print(self, root, idx=0):
        for char in root.children:
            successor = root.children[char].successor
            count = root.children[char].count
            print('%s%s (%s)' % (''.join(['  ' for _ in range(idx)]), char, count))
            self.__print(successor, idx + 1)
    
    def __find(self, chars, root, idx):
        char = chars[idx]
        if char not in root.children or idx >= len(chars) - 1:
            return None
        
        successor = root.children[char].successor
        count = root.children[char].count
    
        prefix = self.__find(chars, successor, idx + 1)
        if not prefix:                          # backtracking to find an earlier prefix (from a word in the dictionary)
            if count > 0:                       # match with a word in the dictionary
                return chars[:idx + 1]
            
            return None                         # not yeat a match, let's backtrack on the parent and check again...
        
        return prefix                           # got a prefix, let's return it

class Solution(object):
    def replace_words(self, dictionary, sentence, debug=True):
        """
        The main idea is to use a prefix tree. Once identified the matching prefix, replace
        the word in the sentence with the identified prefix.
        To implement the prefix tree, a Trie might be the best option.

        The algorithm works like:
        > cattle
          <>
            c (0)       <
                a (0)
                t (1)
            b (0)
                a (0)
                t (1)
            r (0)
                a (0)
                t (1)
        
        > attle
          <>
            c (0)       <
                a (0)   <
                t (1)
            b (0)
                a (0)
                t (1)
            r (0)
                a (0)
                t (1)
        
        > ttle
          <>
            c (0)       <
                a (0)   <
                t (1)   <
            b (0)
                a (0)
                t (1)
            r (0)
                a (0)
                t (1)
        
        > tle
          <>
            c (0)       <
                a (0)   <
                t (1)   <
                        -
            b (0)
                a (0)
                t (1)
            r (0)
                a (0)
                t (1)
        
        > ttle
          <>
            c (0)       <
                a (0)   <
                t (1)   <<<
            b (0)
                a (0)
                t (1)
            r (0)
                a (0)
                t (1)
        < [: idx + 1] = 'cat'
        """
        trie = Trie()
        for word in dictionary:             # got to load the Trie data structure
            trie.insert(word)
        
        if debug:
            trie.pretty_print()             # just to have a nice output

        words = sentence.split(' ')
        for idx, word in enumerate(words):  # got to look for prefixes, and perform in-place replacement
            prefix = trie.prefix(word)
            if prefix:
                words[idx] = prefix
        
        return words

def main():
    s = Solution()

    dictionary = ["cat","bat","rat"]
    sentence = "the cattle was rattled by the battery"
    print(s.replace_words(dictionary, sentence))        # "the cat was rat by the bat"

    dictionary = ["a","b","c"]
    sentence = "aadsfasf absbs bbab cadsfafs"
    print(s.replace_words(dictionary, sentence))        # "a a b c"

    dictionary = ["a", "aa", "aaa", "aaaa"]             # same letters, only first to be added
    sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
    print(s.replace_words(dictionary, sentence))        # "a a a a a a a a bbb baba a"

    dictionary = ["catt","cat","bat","rat"]
    sentence = "the cattle was rattled by the battery"
    print(s.replace_words(dictionary, sentence))        # "the cat was rat by the bat"

    dictionary = ["ac","ab"]
    sentence = "it is abnormal that this solution is accepted"
    print(s.replace_words(dictionary, sentence))        # "it is ab that this solution is ac"

if __name__ == '__main__':
    main()
