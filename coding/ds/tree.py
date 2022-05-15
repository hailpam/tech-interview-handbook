class Node(object):
    '''
    A node of an N-ary Tree (i.e. a Tree with nodes having N siblings).
    '''
    def __init__(self, value, siblings=[]):
        self.value = value
        self.siblings = siblings
    
    def __eq__(self, other):
        if self.value == other.value:
            return True
        return False

class Tree(object):
    '''
    A generic implementation of N-ary Tree which aims at showing the basic concepts and
    operations can be implemented with the assistance of a search routine (combine the 
    search with a state modification).
    '''

    def __init__(self, root=None):
        self.root = Node(None)
    
    def add(self, node, to):
        '''
        Adds a node to a given ancestor, if such ancestor exists.
        '''
        # let's search first the position in the Tree structure
        _, child = self.search(to)
        # if found, let's nest the child in the Tree structure
        if child:
            child.siblings.append(Node(node, []))
            return True
        return False

    def remove(self, node):
        '''
        Removes a node from the tree, if it exists.
        '''
        # let's search first the position in the Teee structure
        ancestor, _ = self.search(node)
        # if found, let's remove the child from the ancestor
        if ancestor:
            ancestor.siblings.remove(Node(node, []))
            return True
        return False

    def search(self, node):
        '''
        Searches for a node, returning the node itself and its ancestor if present.
        '''
        return self.__search(node, self.root)
    
    def __search(self, node, root):
        # root is the sibling with no ancestor
        if node == root.value:
            return None, root
        # let's search for the sibling and its ancestor
        for sibling in root.siblings:
            if node == sibling.value:
                return root, sibling
            ancestor, child = self.__search(node, sibling)
            if ancestor or child:
                return ancestor, child
        return None, None

    def prettyprint(self):
        '''
        Pretty prints the tree leveraging an incrementing indentation on per level basis.
        '''
        self.__prettyprint(self.root)
    
    def __prettyprint(self, root, indent=0):
            print('%s%s' % (indent * ' ', root.value))
            for sibling in root.siblings:
                self.__prettyprint(sibling, indent + 2)

def main():
    tree = Tree()
    print(10, tree.add(10, None))
    print(10, tree.add(5, 10))
    print(10, tree.add(7, 10))
    print(10, tree.add(4, 5))
    print(10, tree.add(3, 5))
    print(10, tree.add(9, 7))
    print(20, tree.add(20, None))
    print(20, tree.add(17, 20))
    print(20, tree.add(15, 20))
    print(20, tree.add(20, 29))
    tree.prettyprint()

    tree.remove(3)
    tree.prettyprint()

if __name__ == '__main__':
    main()
