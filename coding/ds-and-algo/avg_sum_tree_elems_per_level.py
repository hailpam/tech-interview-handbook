# From Meta interview

'''
Compute the average on per tree level basis:

      4
  7       9
 1  8   6   11
      3
        4

[4 8 6.5 3 4]

Questions:
    1. should the average by a floating point number? Y
    2. any preference between depth-first and breadth-first search? N

Solutions:
    1. based on depth-first search: running sum and count, O(N), N = number of elements

Debug:
    4
    {}
    []
    4, {}, 0:
        {0: (0,0)}
        {0: (4, 1)}
        7, {0: (4, 1)}, 1:
            {1: (0, 0)}
            {1: (7, 1)}
            1, {0: (4, 1), 1: (7, 1)}, 2:
                {2: (0,0)}
                {2: (1, 1)}
                None, {0: (4, 1), 1: (7, 1), 2: (1,1)}, 3:
                    return
                None, {0: (4, 1), 1: (7, 1), 2: (1,1)}, 3:
                    return
            return
            8, {0: (4, 1), 1: (7, 1), 2: (1,1)}, 2:
                {2: (9, 2)}
                None, {0: (4, 1), 1: (7, 1), 2: (1,1)}, 3:
                    return
                None, {0: (4, 1), 1: (7, 1), 2: (1,1)}, 3:
                    return
            return
        [...]
'''

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def _traverse(root, data, level=0):
    # no way to move forward
    if not root:
        return
    # let's get this right: this node value
    if level not in data:
        data[level] = (0, 0)
    r_sum, r_count = data[level]
    r_sum += root.val
    r_count += 1
    data[level] = (r_sum, r_count)
    # let's recurse on left and right
    _traverse(root.left, data, level + 1)
    _traverse(root.right, data, level + 1)

def avg_elements(root):
    data = {}
    result = []
    # let's traverse the tree and create the supporting running sum and count
    _traverse(root, data)                   # O(N), N = number of nodes
    # let's derive the averages
    i = 0
    while i in data:
        r_sum, r_count = data[i]
        result.append(r_sum / r_count)
        i += 1
    return result

def pretty_print(root, indent=0):
    if root:
        spacing = indent * '  '
        print('%s%s' % (spacing, root.val))
        pretty_print(root.left, indent+1)
        pretty_print(root.right, indent+1)

def main():
    one = Node(1)
    four = Node(4)
    three = Node(3, None, four)
    eight = Node(8, three, None)
    seven = Node(7, one, eight)
    six = Node(6)
    eleven = Node(11)
    nine = Node(9, six, eleven)
    four = Node(4, seven, nine)
    pretty_print(four)
    print(avg_elements(four))

if __name__ == '__main__':
    main()
