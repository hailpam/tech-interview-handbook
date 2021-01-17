import random

# On Leetcode: https://yangshun.github.io/tech-interview-handbook/algorithms/hash-table/

class LeastRecentlyUsedCache(object):
    """
    Least Frequently Used (LFU) is a type of cache algorithm used to manage memory within a computer. 
    The standard characteristics of this method involve the system keeping track of the number of times a 
    block is referenced in memory.

    Reference: https://en.wikipedia.org/wiki/Least_frequently_used#:~:text=Least%20Frequently%20Used%20(LFU)%20is,block%20is%20referenced%20in%20memory.
    """

    def __init__(self, max_size=100):
        self.max_size = max_size
        self.cache = {}
        self.counts = {}

    def __purge(self, how_many):
        bottom_k = []

        for key in self.counts:
            if len(bottom_k) < how_many:    # got to fill up
                bottom_k.append((self.counts[key], key))
            else:                           # got to manage it, bottom K keys
                idx = -1
                for i, b in enumerate(bottom_k):
                    if self.counts[key] < b[0]:
                        idx = i
                        break
                if idx != -1:
                    bottom_k[idx] = (self.counts[key], key)
        
        for bk in bottom_k:                 # once identified, got to remove
            print('purged (%s, %s)' % (bk[1], bk[0]))
            del self.cache[bk[1]]
            del self.counts[bk[1]]

    def insert(self, key, value):
        if key not in self.cache:
            self.counts[key] = 0
        self.counts[key] += 1
        self.cache[key] = value

        if len(self.cache) > self.max_size:     # got to purge the less recently used ones
            self.__purge(len(self.cache) - self.max_size)
    
    def remove(self, key, value):               # got to remove
        if key in self.cache:
            del self.cache[key]
            del self.counts[key]
    
    def increment_use(self, key):
        if key in self.counts:
            self.counts[key] += 1

    def decrement_use(self, key):
        if key in self.counts:
            self.counts[key] -= 1

def main():
    lru_cache = LeastRecentlyUsedCache(10)

    for _ in range(100):
        key = random.randint(0, 10)
        value = 'test'
        lru_cache.insert(key, value)
    print(sorted(list(lru_cache.cache)), len(lru_cache.cache))
    print(lru_cache.counts, len(lru_cache.counts))

if __name__ == '__main__':
    main()
