# From Meta interview

'''
An inverted index that indexes full-sense words with their own anagrams

For the word rates:
    rates -> aster, stare, taser, tears, ...
Looking up any of the anagram:
    stare -> rates

Questions:
    1. should the index also relate anagrams? N
    2. should the word being indexed with its anagrams as well? N

Solutions:
    1. a data structure that 
        a. generates anagrams at indexing time, and
        b. provides constant time lookup

Example:
    rat
        art
        atr
        rta
        art
        tar
        tra

Permutations can be built recursively, leveraging backtracking:

    r
        a
            t
        t
            a
    a
        r
            t
        t
            r
    t
        r
            a
        a
            r

Debug:

rat, [], []:
    r
        a
            t   -> rat
        t
            a   -> rta
    a
        r
            t   -> art
        t
            r   -> atr
    t
        a
            r   -> tar
        r
            a   -> tra

tar, [], []:
    t
        a
            r   -> tar
        r
            a   -> tra
    a
        r
            t   -> art
        t
            r   -> atr
    r
        a
            t   -> rat
        t
            a   -> rta
'''

class Anagrammer(object):
    def __init__(self):
        self.index = {}
    
    def __generate_anagrams(self, word, anagrams, tmp):
        # NOTE here anagrams are intended as permutions (no real dictionary to filter our invalid words)
        # generate permutations using backtracking
        if word:
            for char in word:
                tmp.append(char)
                c_word = list(word)
                c_word.remove(char)
                self.__generate_anagrams(c_word, anagrams, tmp)
                tmp.pop()
        if tmp and not word:
            anagrams.append(''.join(tmp))

    def index_word(self, word):
        # nothing to index with empty words
        if not word:
            return
        # let's generate the anagrams...
        anagrams = []
        tmp = []
        self.__generate_anagrams(word, anagrams, tmp)       # O(N!), N = length of anagram
        # for each anagram, add the word that generated it
        for anagram in anagrams:                            # O(N!), N = length of anagram
            if anagram not in self.index:
                self.index[anagram] = set()
            self.index[anagram].add(word)

    def lookup_words(self, anagram):
        if anagram in self.index:                           # O(1)
            return self.index[anagram]
        return None

def main():
    a = Anagrammer()
    word = 'rat'
    a.index_word(word)
    print(a.lookup_words('art'))     # expected rat
    word = 'tar'
    a.index_word(word)
    print(a.lookup_words('art'))     # expected rat and tar
    word = 'rates'
    a.index_word(word)
    print(a.lookup_words('tears'))   # expected rates
    word = 'tears'
    a.index_word(word)
    print(a.lookup_words('stare'))   # expected rates and tears

if __name__ == '__main__':
    main()
