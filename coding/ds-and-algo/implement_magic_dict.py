
# On Leetcode: https://leetcode.com/problems/implement-magic-dictionary/

class Trie(object):
    class Node(object):
        def __init__(self):
            self.children = {}

    class Value(object):
        def __init__(self, successor=None, count=0):
            self.successor = successor
            self.count = count

    def __init__(self):
        self.root = Trie.Node()

    def insert(self, word):
        self.__add(list(word), self.root,  0)

    def search(self, word, nr_wildcard=0):
        return self.__find(list(word), self.root, 0, nr_wildcard)

    def print(self):
        print('*')
        self.__print(self.root, 1)

    def __add(self, chars, root, idx=0):
        char = chars[idx]
        if char not in root.children:
            root.children[char] = Trie.Value(Trie.Node())
        if idx == len(chars) - 1:
            root.children[char].count += 1
            return
        self.__add(chars, root.children[char].successor, idx + 1)
    
    def __find(self, chars, root, idx=0, nr_wildcard=0, nr_non_match=0):
        if idx >= len(chars):
            return None
        
        char = chars[idx]
        if char not in root.children:           # got to check whether the number of wildcards is exhausted
            if nr_non_match > nr_wildcard:
                return None
            
            if idx == len(chars) - 1:           # still have a wildcard, so any match is allowed
                if len(root.children) != 0 and nr_non_match < nr_wildcard:
                    return ''.join(chars)
                
                return None
            
            for char in root.children:          # all matches are allowed, let move next, one by one
                successor = root.children[char].successor
                return self.__find(chars, successor, idx + 1, nr_wildcard, nr_non_match + 1)
        
        if char in root.children:               # normal search and match flow
            successor = root.children[char].successor
            count = root.children[char].count
            if idx == len(chars) - 1:
                if count > 0:
                    return ''.join(chars)
                
                return None
            
            return self.__find(chars, successor, idx + 1, nr_wildcard, nr_non_match)

    def __print(self, root, idx=0):
        for c in root.children:
            successor = root.children[c].successor
            count = root.children[c].count
            print('%s%s (%s)' % (''.join(['  ' for _ in range(idx)]), c, count))
            self.__print(successor, idx + 1)

class MagicDictionary(object):
    def __init__(self):
        self.trie = Trie()

    def build_dict(self, words):
        for word in words:
            self.trie.insert(word)

    def search(self, word):
        return self.trie.search(word, 1) != None

def main():
    md = MagicDictionary()

    md.build_dict(["hello", "leetcode"])
    md.trie.print()

    print(md.search("hello"))                      # True
    print(md.search("hell"))                       # False
    print(md.search("hhllo"))                      # True
    print(md.search("leetcoded"))                  # False
    print(md.search("helpo"))                      # True
    print(md.search("hxlly"))                      # False
    print(md.search("leetcodx"))                   # True

if __name__ == '__main__':
    main()
