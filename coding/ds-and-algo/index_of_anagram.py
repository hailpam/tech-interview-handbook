# Example of Meta interview training session

'''
Find only the first matching substring and return the index.

Examples of inputs and outputs:
    'actor'.aio('cat') -> 0
    'actor'.aio('tar') -> -1
    'actor'.aio('rot') -> 2

Debug/test:
actor, cat:
    {c: 1, a: 1, t: 1}
    3
    5

    0, c
        {a: 1, c: 1, t: 1}
        True
        return 0
    0

actor, tar:
    {t: 1, a: 1, r: 1}
    3
    5

    0, a
        {a: 1, c: 1, t: 1}
        False
    1, c
        {c: 1, t: 1, o: 1}
        False
    2, t
        {t: 1, o: 1, r: 1}
        False
    3, o
        break
    -1

actor, rot
    {r: 1, o: 1, t:1}
    3
    5

    0, a
    1, c
    2, t
        {t: 1, o: 1, r: 1}
        True
        2
    2
'''

def tokenize(text):
    tokens = {}
    # tokenize and count
    for c in text:
        if c not in tokens:
            tokens[c] = 0
        tokens[c] += 1
    return tokens

def equals(dict1, dict2):
    # not the same number of keys
    if len(dict1) != len(dict2):
        return False
    # existence and same count for keys
    for key in dict1:
        if key not in dict2:
            return False
        if dict1[key] != dict2[key]:
            return False
    return True

def aio(text, anagram):
    d_anagram = tokenize(anagram)                   # O(M), M = length of anagram
    l_anagram = len(anagram)                        # O(1)
    l_text = len(text)                              # O(1)
    for i, _ in enumerate(text):                    # O(N - M), N = length of text
        # stop logic to avoid out of bound
        if i + l_anagram > l_text:
            break
        # check whether the anagram is conained as substring
        s_anagram = tokenize(text[i:l_anagram+i])   # O(M)
        if equals(d_anagram, s_anagram):            # O(M)
            return i
    return -1

def main():
    text = 'actor'
    anagram = 'cat'
    print(text, anagram, aio(text, anagram))

    anagram = 'tar'
    print(text, anagram, aio(text, anagram))

    anagram = 'rot'
    print(text, anagram, aio(text, anagram))

if __name__ == '__main__':
    main()
