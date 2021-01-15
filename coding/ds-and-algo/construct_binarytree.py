
# On Leetcode: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def to_preorder(self, root, idx, nodes=[]):
        """
        Helper method to serialize the preorder traversal
        """
        if not root:
            return None
        
        nodes.append(root.val)
        left = self.to_preorder(root.left, idx + 1, nodes)
        if left:
            nodes.append(left.val)
        right = self.to_preorder(root.right, idx + 1, nodes)
        if right:
            nodes.append(right.val)

    def to_inorder(self, root, idx=0, nodes=[]):
        """
        Helper method to serialize the inorder traversal
        """
        if not root:
            return None
        
        left = self.to_inorder(root.left, idx + 1, nodes)
        if left:
            nodes.append(left)
        nodes.append(root.val)
        right = self.to_inorder(root.right, idx + 1, nodes)
        if right:
            nodes.append(right)

    def pretty_print(self, root, idx=0):
        """
        Helper function to pretty print the tree.
        """
        if not root:
            return
        
        print('%s%s' % (''.join(['  ' for _ in range(idx)]), root.val))
        self.pretty_print(root.left, idx + 1)
        self.pretty_print(root.right, idx + 1)

    def find_root(self, preorder, inorder, pivot):
        """
        Picks the root from preorder for the actual subtree, returning the index
        of the newly identified root in the inorder array, and an incremneted 
        pivot index.
        """
        return inorder.index(preorder[pivot]), pivot + 1
    
    def visit(self, preorder, inorder, start, end, pivot):
        """
        Visits recusrively the arrays. The problem is reduced to recursively find the
        root of the subtree. The halt condition is detected by having a slice of the
        original array of size 1 (i.e. forcedly a leaf).
        """
        if end - start == 1:                                        # got only 1 slot, so it's a leaf
            return Node(inorder[start]), pivot + 1

        root_idx, pivot = self.find_root(preorder, inorder, pivot)  # find in-order index for the root
        root = Node(inorder[root_idx])
        root.left, pivot = self.visit(preorder, inorder, start, root_idx, pivot)
        root.right, pivot = self.visit(preorder, inorder, root_idx + 1, end, pivot)

        return root, pivot

    def built_tree(self, preorder, inorder):
        """
        Building a binary tree from pre-order and in-order serialized versions requires
        to deal with a recursive solution which finds roots of the subtree.

        pre-order   3 9 1 2 20 15 7
        in-order    1 9 2 3 15 20 7

        > pivot=0
        pre-order   3 9 1 2 20 15 7
                    ^
        in-order    1 9 2 3 15 20 7
                          ^
                    1 9 2   15 20 7

        > pivot=1
        pre-order   3 9 1 2 20 15 7
                      ^
        in-order    1 9 2 3 15 20 7
                          ^
                    1 9 2   15 20 7
                      ^
                    1   2
        > pivot=2,3
        pre-order   3 9 1 2 20 15 7
                        ^ ^
        in-order    1 9 2 3 15 20 7
                          ^
                    1 9 2   15 20 7
                      ^
                    1   2
                    ^   ^
        > pivot=4
        pre-order   3 9 1 2 20 15 7
                             ^
        in-order    1 9 2 3 15 20 7
                          ^
                    1 9 2   15 20 7
                      ^         ^
                    1   2   15    7
                    ^   ^
        > pivot=5,6
        pre-order   3 9 1 2 20 15 7
                                ^ ^
        in-order    1 9 2 3 15 20 7
                          ^
                    1 9 2   15 20 7
                      ^         ^
                    1   2   15    7
                    ^   ^    ^    ^
        
        Eventually, the binary tree will be:
        3
           9
              1
              2
          20
              15
              7
        """
        root, _ = self.visit(preorder, inorder, 0, len(inorder), 0)

        return root

def main():
    s = Solution()

    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    root = s.built_tree(preorder, inorder)
    s.pretty_print(root)
    p = []
    s.to_preorder(root, 0, p)
    print(p)
    i = []
    s.to_inorder(root, 0, i)
    print(i)

    preorder = [3,9,1,2,20,15,7]
    inorder = [1,9,2,3,15,20,7]
    root = s.built_tree(preorder, inorder)
    s.pretty_print(root)
    p = []
    s.to_preorder(root, 0, p)
    print(p)
    i = []
    s.to_inorder(root, 0, i)
    print(i)

    preorder = [3,9,1,2,20,15,7]
    inorder = [1,9,2,3,15]
    root = s.built_tree(preorder, inorder)
    s.pretty_print(root)
    p = []
    s.to_preorder(root, 0, p)
    print(p)
    i = []
    s.to_inorder(root, 0, i)
    print(i)

if __name__ == '__main__':
    main()
