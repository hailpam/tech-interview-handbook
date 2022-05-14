'''
Depth-first search works on tree and graph data structures. It performs a search prioritizing
going deep in the tree, one level at a time. On a graph data structure the only difference
consists in keeping an index with visited nodes to avoid loops.
'''

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
def prettyprint(root, indent=0):
    if root:
        print('%s%d' % (indent * ' ', root.value))
        prettyprint(root.left, indent + 2)
        prettyprint(root.right, indent + 2)

def dfs(root, value):
    if root:
        # check the value, and return it upon hit
        if root.value == value:
            return value
        # check the left subtree, and return the hit if any
        if dfs(root.left, value) != -1:
            return value
        # check the right subtree, and return the hit if any
        if dfs(root.right, value) != -1:
            return value
    return -1

def main():
    '''
          1
       5     10
           7    11
    '''
    five = Node(5)
    seven = Node(7)
    eleven = Node(11)
    ten = Node(10, seven, eleven)
    one = Node(1, five, ten)
    prettyprint(one)

    print(11, dfs(one, 11))
    print(21, dfs(one, 21))

    '''
          1
       5     10
    3      7    11
    '''
    three = Node(3)
    five = Node(5, three)
    one = Node(1, five, ten)
    prettyprint(one)

    print(3, dfs(one, 3))

if __name__ == '__main__':
    main()
