'''
Depth-first search works on tree and graph data structures. It performs a search prioritizing
going searching one level at a time. On a graph data structure the only difference consists 
in keeping an index with visited nodes to avoid loops.
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

def bfs(value, queue=[]):
    # loop through the queue which enlists on per level basis the nodes
    while queue:
        node = queue.pop(0)
        if node.value == value:
            return value
        # in case of n-ary tree, it is possible to leverage a loop...
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
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

    # print(11, bfs(11, [one]))
    print(21, bfs(21, [one]))

    '''
          1
       5     10
    3      7    11
    '''
    three = Node(3)
    five = Node(5, three)
    one = Node(1, five, ten)
    prettyprint(one)

    print(3, bfs(3, [one]))

if __name__ == '__main__':
    main()
