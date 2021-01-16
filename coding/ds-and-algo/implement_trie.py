
# On Leetcode: https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode(object):
    def __init__(self):
        """
        A Trie Node contains a dictionary which is able to host the
        characters as keys and Trie Value as avalues.
        """
        self.vals = {}

class TrieValue(object):
    def __init__(self, next=None, present=False):
        """
        A Trie Value contains the pointer to the next node in the Trie
        and a flag indicating whether the word composed on the path is
        present or not.
        """
        self.next = next        # points to the next node
        self.present = present  # stays False for a transition node

class Trie(object):
    """
    A Trie is also known as a Prefix Tree.

    An implementation of Trie might leverage a dictionary to
    organize the content as follows:

    a
      p
        p
          l
            e
        s
      u
        t
          o
    
    Each node has 26 values and for each value there will be either
    a corresponding child node or a None. In case of a node, there 
    is still browsing. Otherwise, the letter is present but it does
    not have a continuation.
    """
    def __init__(self):
        self.root = TrieNode()  # define the root
    
    def __add(self, chars, root, idx=0):
        """
        Recursively add new characters on the path to the bottom of the
        characters array.
        """
        if idx >= len(chars):
            return
        if chars[idx] not in root.vals:
            root.vals[chars[idx]] = TrieValue(TrieNode())
        if idx == len(chars) - 1:
            root.vals[chars[idx]].present = True
        self.__add(chars, root.vals[chars[idx]].next, idx + 1)

    def insert(self, word):
        chars = list(word)
        self.__add(chars, self.root)
    
    def __find(self, chars, root, prefix=True, idx=0):
        """
        Recursively tries to find the word in the Trie. It works in two 
        modes, both prefix and exact match.
        """
        if chars[idx] not in root.vals:
            return False
        if idx == len(chars) - 1:
            if prefix:      # prefix matching, so got it
                return True
            else:           # exact matching, got to check the presence of the word
                return root.vals[chars[idx]].present
        return self.__find(chars, root.vals[chars[idx]].next, prefix, idx + 1)

    def search(self, word):
        chars = list(word)
        return self.__find(chars, self.root, False, 0)  # exact match

    def starts_with(self, prefix):
        chars = list(prefix)
        return self.__find(chars, self.root, True, 0)   # prefix match
    
    def __print(self, root, idx=0):
        for key in root.vals:
            print('%s%s%s' % (''.join(['  ' for _ in range(idx)]), key, ' <>' if root.vals[key].present else ''))
            self.__print(root.vals[key].next, idx + 1)

    def pretty_print(self):
        print('*')
        self.__print(self.root, 1)

def main():
    trie = Trie();
    
    trie.insert("apple");
    trie.insert("apps");
    trie.insert("apples");
    trie.insert("bike");
    trie.insert("bix");
    trie.insert("car");
    trie.insert("case");
    trie.pretty_print()

    print(trie.starts_with("app"))  # returns True
    print(trie.starts_with("bi"))   # returns True
    print(trie.starts_with("ca"))   # returns True
    print(trie.starts_with("xyz"))  # returns True

    print(trie.search("apple"))     # returns True
    print(trie.search("app"))       # returns False
    
    trie.insert("app")
    trie.pretty_print()    
    print(trie.search("app"))       # retruns True

if __name__ == '__main__':
    main()
