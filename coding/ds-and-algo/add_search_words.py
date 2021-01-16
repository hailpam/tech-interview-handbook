
# On Leetcode: https://leetcode.com/problems/design-add-and-search-words-data-structure/

class Trie(object):
    class TrieNode(object):
        def __init__(self):
            """
            Initializes a dictionary to keep the relationships between the
            characters.
            """
            self.vals = {}

    class TrieValue(object):
        def __init__(self, next=None, count=0):
            """
            Initializes a pointer to the next node and a counter for the 
            number of inserted words.
            """
            self.next = next
            self.count = count

    def __init__(self):
        self.root = Trie.TrieNode()

    def __add(self, chars, root, idx=0):
        char = chars[idx]
        if char not in root.vals:
            root.vals[char] = Trie.TrieValue(Trie.TrieNode())
        if idx == len(chars) - 1:
            root.vals[char].count += 1
            return
        self.__add(chars, root.vals[char].next, idx + 1)

    def insert(self, word):
        chars = list(word)
        self.__add(chars, self.root)

    def __find(self, chars, root, idx=0):
        char = chars[idx]
        if char not in root.vals:
            return False
        if idx == len(chars) - 1:
            if root.vals[char].count == 0:
                return False
            else:
                return True
        return self.__find(chars, root.vals[char].next, idx + 1)
    
    def __find_wildcard(self, chars, root, wildcard='.', idx=0):
        """
        It implements a wildcard matching algorithm based off the Trie. 
        Purposedly, it does not check the counter for the word presence, as
        it is ambiguous exact match with a word.
        """
        if idx >= len(chars):
            return True
        
        char = chars[idx]
        if char == wildcard:        # got a wildcard match, need to loop on all possibilities
            for val in root.vals:
                if self.__find_wildcard(chars, root.vals[val].next, wildcard, idx + 1):
                    return True
            return False
        else:                       # got an exact match
            if char not in root.vals:
                return False
            return self.__find_wildcard(chars, root.vals[char].next, wildcard, idx + 1)

    def search(self, word):
        return self.__find(list(word), self.root, 0)
    
    def match(self, string):
        return self.__find_wildcard(list(string), self.root, '.', 0)
    
    def __print(self, root, idx=0):
        for val in root.vals:
            print('%s%s %d' % (''.join(['  ' for _ in range(idx)]), val, root.vals[val].count))
            self.__print(root.vals[val].next, idx + 1)

    def pretty_print(self):
        print('*')
        self.__print(self.root, 1)

class WordDictionary(object):
    """
    Ideally, a word dictionary can be implemented efficiently using a Trie.
    Words can be inserted in the Trie and then searched by prefix or exact
    match.
    The problem at hand introduces a peculiar search pattern, which is the 
    wildcard one: '.' works as a wildcard search.
    """

    def __init__(self):
        self.trie = Trie()

    def add_word(self, word):
        self.trie.insert(word)

    def search(self, word):
        if '.' in word:
            return self.trie.match(word)
        
        return self.trie.search(word)

def main():
    word_dictionary = WordDictionary();
    word_dictionary.add_word("bad");
    word_dictionary.add_word("dad");
    word_dictionary.add_word("mad");
    word_dictionary.trie.pretty_print()

    print(word_dictionary.search("pad"))    # returns False
    print(word_dictionary.search("bad"))    # returns True
    print(word_dictionary.search(".ad"))    # returns True
    print(word_dictionary.search("b.."))    # returns True
    print(word_dictionary.search(".ad"))    # returns True
    print(word_dictionary.search("n.."))    # returns False
    print(word_dictionary.search("m.c"))    # returns False

if __name__ == '__main__':
    main()
