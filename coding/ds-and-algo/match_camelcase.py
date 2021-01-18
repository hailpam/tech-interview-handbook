
# On Leetcode: https://leetcode.com/problems/camelcase-matching/

class Solution(object):
    def check_uppercase(self, query, pattern):
        query_l = []
        for c in query:
            if c.isupper():
                query_l.append(c)
        pattern_l = []
        for c in pattern:
            if c.isupper():
                pattern_l.append(c)
        
        return query_l == pattern_l

    def check_matching(self, query, pattern):
        query_idx = []
        for i, c in enumerate(query):
            if c.isupper():
                query_idx.append(i)
        
        matcher = ['.' for _ in range(len(query))]
        idx = 0
        for p in pattern:
            if p.isupper():                                 # get the index of the query uppercase
                idx = query_idx.pop(0)
                matcher[idx] = p
            else:                                           # get to increment from the last index
                idx += 1
                matcher[idx] = p

        for i, c in enumerate(query):                       # '.' is used as wildcard matcher
            if matcher[i] != '.':
                if matcher[i] != query[i]:
                    return False
        
        return True

    def match_camelcase(self, queries, pattern):
        """
        The main idea of the algorithm is to check two primary things:

            1. check orderly the equality of the upper case letters;
            2. check the mathing using filling wildcards by expanding
               the pattern string.

        The algorithm can be explained with the following examples.
        
        > Example 1:
        query = FooBar, pattern = FB
        ?: [F, B] == [F, B]
        ?: [F, o, o, B, a, r] == [F, ., ., B, ., .]

        > Example 2:
        query = FooBarTest, pattern = FoBaT
        ?: [F, B, T] == [F, B, T]
        ?: [F, o, o, B, a, r, T, e, s, t] == [F, o, ., B, a, ., T, ., ., .]
        """
        results = []
        for query in queries:
            if not self.check_uppercase(query, pattern):    # first, let's check that the uppercase pattern matches
                results.append(False)
                continue
            if not self.check_matching(query, pattern):     # second, let's check whether it's possible to wildcard match
                results.append(False)
                continue
            results.append(True)                            # got to pass all checks and matches
        
        return results

def main():
    s = Solution()

    queries = [
        "FooBar",           # True
        "FooBarTest",       # False
        "FootBall",         # True
        "FrameBuffer",      # True
        "ForceFeedBack"     # False
    ]
    pattern = "FB"
    print(s.match_camelcase(queries, pattern))

    queries = [
        "FooBar",           # True
        "FooBarTest",       # False
        "FootBall",         # True
        "FrameBuffer",      # False
        "ForceFeedBack"     # False
    ]
    pattern = "FoBa"
    print(s.match_camelcase(queries, pattern))

    queries = [
        "FooBar",           # False
        "FooBarTest",       # True
        "FootBall",         # False
        "FrameBuffer",      # False
        "ForceFeedBack"     # False
    ]
    pattern = "FoBaT"
    print(s.match_camelcase(queries, pattern))

if __name__ == '__main__':
    main()
