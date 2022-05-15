'''
A Trie is an N-ary Tree, with N equal to the number of characters in an alphabet. It is a memory-efficient
way of representing dictionaries as it does avoid duplication: a word is composed as a path. It is a basic
building block for those use cases that require prefix matching.
'''

class Node(object):
    '''
    A Node gets its own value and a dictionary which contains the siblings (indended as nodes which descend 
    from this Node). Values are intended as characters.
    '''
    def __init__(self, value, siblings={}):
        self.value = value
        self.siblings = siblings

class Trie(object):
    '''
    A Trie stores words. Indeed, it does implement a dictionary which minimise the redundancy (intended as word
    repetitions).
    '''
    def __init__(self, root=Node(None, {})):
        self.root = root
    
    def add(self, word):
        '''
        Adds a word in the Trie. Builds all the path through if not built yet.
        '''
        self.__add(self.root, word)

    def __add(self, ancestor, word, index=0):
        if index < len(word):
            char = word[index]
            # add the character if not present
            if char not in ancestor.siblings:
                ancestor.siblings[char] = Node(char, {})
            # recursively add charactes on the way through
            sibling = ancestor.siblings[char]
            self.__add(sibling, word, index + 1)

    def remove(self, word):
        '''
        Removes a word from the Trie. Prunes the Trie backward.
        '''
        self.__remove(self.root, word)

    def __remove(self, ancestor, word, index=0):
        char = word[index]
        if char in ancestor.siblings:
            # go forward up until the very last character
            if index < len(word) - 1:
                self.__remove(ancestor.siblings[char], word, index + 1)
            # go backward, prune all nodes with no siblings
            if not ancestor.siblings[char].siblings:
                del ancestor.siblings[char]

    def search(self, word):
        '''
        Searches for a word in the Trie.
        '''
        return self.__search(self.root, word)
    
    def __search(self, ancestor, word, index=0):
        # exhausted search, the word is present
        if index >= len(word):
            return True
        char = word[index]
        # no such char, the word cannot be present
        if char not in ancestor.siblings:
            return False
        # leverage the search to get deeper in the Trie and find the match
        return self.__search(ancestor.siblings[char], word, index + 1)

    def match(self, prefix):
        '''
        Searches for a prefix match in the Trie. In this implementation, not really different from a basic search
        as words are not marked as final by any chance.
        '''
        return self.__search(self.root, prefix)
    
    def prettyprint(self):
        '''
        Pretty prints the Trie leveraging indentation.
        '''
        self.__prettyprint(self.root)


    def __prettyprint(self, root, indent=0):
        print('%s%s' % (indent * ' ', root.value))
        for sibling in root.siblings:
            self.__prettyprint(root.siblings[sibling], indent + 2)

def main():
    trie = Trie()
    trie.add('word')
    trie.add('words')
    trie.add('worth')
    trie.add('water')
    trie.add('apple')
    trie.add('app')
    trie.add('apps')
    trie.add('apero')
    trie.prettyprint()

    word = 'apple'
    print(word, trie.search(word))
    word = 'cat'
    print(word, trie.search(word))

    prefix = 'ap'
    print(prefix, trie.match(prefix))

    word = 'cat'
    print(word, trie.add(word))
    word = 'cats'
    print(word, trie.add(word))
    word = 'cattle'
    print(word, trie.add(word))
    trie.prettyprint()

    word = 'cattle'
    print(word, trie.remove(word))
    word = 'water'
    print(word, trie.remove(word))
    trie.prettyprint()

if __name__ == '__main__':
    main()
