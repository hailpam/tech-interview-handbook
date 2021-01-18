
# On Leetcode: https://leetcode.com/problems/longest-word-in-dictionary/

class Trie(object):
    """
    A Trie implementation tailored to the needs of the problem at hand.
    """
    def __init__(self):
        self.root = Trie.Node()

    class Node(object):
        def __init__(self):
            self.children = {}

    class Value(object):
        def __init__(self, successor=None, count=0):
            self.successor = successor  # point to the next node
            self.count = count          # reports the count of words provisioned

    def insert(self, word):
        chars = list(word)
        self.__fill(chars, self.root, 0)

    def match(self, word):
        chars = list(word)

        return self.__find(self.root, chars)
    
    def frequency(self, word):
        chars = list(word)

        return self.__count(self.root, chars, 0, 0)

    def pretty_print(self):
        print('*')
        self.__print(self.root, 1)

    def __count(self, root, chars, idx=0, count=0):
        char = chars[idx]
        if char not in root.children:
            return count
        count += root.children[char].count      # got to count the frequency of the prefixes
        if idx == len(chars) - 1:
            return count 
        successor = root.children[char].successor

        return self.__count(successor, chars, idx + 1, count)

    def __find(self, root, chars, idx=0):
        char = chars[idx]
        if char not in root.children:           # got to exit, cannot be a match
            return None
        if idx == len(chars) - 1:               # got to exit, check final match
            if root.children[char].count == 0:  # got 0 words added for this string
                return None
            return ''.join(chars)
        successor = root.children[char].successor

        return self.__find(successor, chars, idx + 1)

    def __fill(self, chars, root, idx=0):
        char = chars[idx]
        if char not in root.children:
            root.children[char] = Trie.Value(Trie.Node())
        if idx == len(chars) - 1:
            root.children[char].count += 1
            return
        self.__fill(chars, root.children[char].successor, idx + 1)
    
    def __print(self, root, idx=0):
        for child in root.children:
            successor = root.children[child].successor
            count = root.children[child].count
            print('%s%s (%d)' % (''.join(['  ' for _ in range(idx)]), child, count))
            self.__print(successor, idx + 1)

class Solution(object):
    def longest_word(self, words, debug=True):
        """
        Building a dictionary one character at a time. Once built, it is required to find
        the word with the longest match.
        Using a Trie data structure to back the case is ideal. The problem then will be solved
        by finding the longest prefix matching according to the input words.

        The main idea is to load up a Trie and then select the the words with the highest frequency
        (i.e. composed by the largest number of prefixes) to then report in lexicographic order.

        For instance, given the following Trie:

          *
            a (1)
                p (1)
                p (1)
                    l (1)
                    y (1)
                    e (1)
                l (1)
                l (1)
                    t (1)
                    t (1)
            b (0)
                a (0)
                n (0)
                    a (0)
                    n (0)
                        a (1)
            w (1)
        >>  alltt
        
        'alltt' is the selected word, with the highest frequency (look a the count of occurences, on 
        the right of the node) and lexicographically sorted. 
        """
        trie = Trie()
        for word in words:              # got to fill up the Trie
            trie.insert(word)
        if debug:                       # just to be visual... not part of the algorithm
            trie.pretty_print()
        
        longest = -1
        selection = []
        for word in words:              # got to find the longest, or the highest frequency
            freq = trie.frequency(word)
            if freq > longest:
                longest = freq
        
        for word in words:              # got to select the candidates
            freq = trie.frequency(word)
            if freq == longest:
                selection.append(word)

        return sorted(selection)[0]      # got to sort to fulfill the lexicographical order

def main():
    s = Solution()

    words = ["w","wo","wor","worl", "world"]
    print(s.longest_word(words))

    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    print(s.longest_word(words))

    words = ["a", "banana", "app", "appl", "ap", "apply", "apple", "w", "wo", "wor", "worl", "world"]
    print(s.longest_word(words))

    words = ["a", "banana", "app", "appl", "ap", "apply", "apple", "w", "al", "all", "allt", "alltt"]
    print(s.longest_word(words))

if __name__ == '__main__':
    main()
