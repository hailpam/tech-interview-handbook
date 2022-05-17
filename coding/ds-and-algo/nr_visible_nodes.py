
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def prettyprint(root, indent=0):
    if not root:
        return
    print('%s%s' % (indent * ' ', root.val))
    prettyprint(root.left, indent + 2)
    prettyprint(root.right, indent + 2)

def nr_leftnode(root, count=0):
    if not root:
        return 0
    # on the left, count equals to 1
    count += nr_leftnode(root.left, 1)
    # on the right, count equals to 0
    count += nr_leftnode(root.right)
    return count

def main():
    '''
            8  <------ root
           / \
         3    10
        / \     \
       1   6     14
          / \    /
         4   7  13 
    '''
    one = Node(1)
    four = Node(4)
    seven = Node(7)
    thirteen = Node(13)
    fourteen = Node(14, left=thirteen)
    ten = Node(10, left=None, right=fourteen)
    six = Node(6, four, seven)
    three = Node(3, one, six)
    eight = Node(8, three, ten)

    prettyprint(eight)
    print(4, nr_leftnode(eight))

if __name__ == '__main__':
    main()
