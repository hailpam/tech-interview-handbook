
import random

# On Leetcode: https://yangshun.github.io/tech-interview-handbook/algorithms/hash-table/

class Map(object):
    """
    A simple implementation of map based off a Python dictionary
    """
    
    def __init__(self):
        self.map = {}
    
    def insert(self, key, value):
        self.map[key] = value
    
    def remove(self, key):
        if key in self.map:
            del self.map[key]
    
    def get(self, key):
        if key in self.map:
            return self.map[key]
        
        return None
    
    def random_key(self):
        l = list(self.map)

        return l[random.randint(0, len(l))]

def main():
    m = Map()

    for _ in range(10):
        key = random.randint(0, 15)
        value = random.randint(0, 1000)
        m.insert(key, value)

    print(m.map)
    m.remove(m.random_key())
    print(m.map)

if __name__ == '__main__':
    main()
