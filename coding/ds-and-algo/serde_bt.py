
# On Leetcode: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

class BinaryTree(object):
    class TreeNode(object):
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    
    def build_tree(self, array, idx=0):
        if idx >= len(array):
            return None
        
        root = BinaryTree.TreeNode(array[idx])
        root.left = self.build_tree(array, idx * 2 + 1)
        root.right = self.build_tree(array, idx * 2 + 2)

        return root

    def pretty_print(self, root, idx=0):
        if root:
            print('%s%s' % (''.join(['  ' for _ in range(idx)]), root.val))
            self.pretty_print(root.left, idx + 1)
            self.pretty_print(root.right, idx + 1)

#  0  1  2  3   4     5  6  7   8
# [1, 2, 3, 11, None, 4, 5, 0, -1]

class Codec(object):
    def __visit(self, root, data, idx=0):
        """
        Visits recursively the binary tree, serializing according to the node
        relationship:
 
            left:  idx * 2 + 1
            right: idx * 2 +2
        """
        if root:
            data[idx] = root.val                        # got to serialize the value

            self.__visit(root.left, data, idx * 2 + 1)  # got to work on idx * 2 + 1, left child
            self.__visit(root.right, data, idx * 2 + 2) # got to work on idx * 2 + 2, right child

        return ' '.join(['%s' % x for x in data])

    def __rebuild(self, array, idx=0):
        """
        Rebuilds a binary tree from an array, adpoing the node relationship:

            left:  idx * 2 + 1
            right: idx * 2 + 2
        """
        if idx >= len(array):
            return None
        
        root = BinaryTree.TreeNode(array[idx])
        root.left = self.__rebuild(array, idx * 2 + 1)
        root.right = self.__rebuild(array, idx * 2 + 2)
        
        return root

    def __size(self, root, count=0):
        """
        Recursively derives the size of the binary tree by adoping a post-order
        traversal.
        """
        if root:
            if not root.left and not root.right:    # got to a leaf, need to rollback
                return 1
            
            count += self.__size(root.left)         # get the subtree count with a post-order traversal
            count += self.__size(root.right)
            count += 1                              # add count for the current node

        return count

    def serialize(self, root):
        """
        Adopting a level-order traversal the binary tree is serialized in a
        string, values are separated by a blank character
        """
        size = self.__size(root)
        data = [None for _ in range(size)]

        return self.__visit(root, data)

    def deserialize(self, data):
        """
        Recursively rebuilds the tree from the input string serialized as
        defined above by the serialized method
        """
        array = data.split(' ')

        return self.__rebuild(array, 0)

def main():
    c = Codec()
    bt = BinaryTree()

    array = [1, 2, 3, None, None, 4, 5]
    root = bt.build_tree(array)
    bt.pretty_print(root)
    data = c.serialize(root) 
    print(data)
    root = c.deserialize(data)
    bt.pretty_print(root)

    array = [1, 2, 3, 11, None, 4, 5, 0, -1]
    root = bt.build_tree(array)
    bt.pretty_print(root)
    data = c.serialize(root) 
    print(data)
    root = c.deserialize(data)
    bt.pretty_print(root)

if __name__ == '__main__':
    main()
