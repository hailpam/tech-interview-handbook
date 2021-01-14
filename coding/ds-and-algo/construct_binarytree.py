
# On Leetcode: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def to_inorder(self, root, idx=0, nodes=[]):
        if not root:
            return None
        print(root.val)
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

    def build_preorder(self, preorder, idx=0):
        """
        A preorder serialization requires an array in which the parent node
        is followed by the children in a relantionship:

        [parent left right left_left left_right]

        left child parent is at 0 * 2 + 1
        right child parent is at 0 * 2 + 2

        In turn:

        left_left child parent is at 1 * 2 + 1
        left_right child parent is at 1 * 2 + 2
        """
        if idx >= len(preorder):
            return None
        
        node = Node(preorder[idx])
        node.left = self.build_preorder(preorder, idx * 2 + 1)
        node.right = self.build_preorder(preorder, idx * 2 + 2)

        return node

    def build_inorder(self, inorder):
        pass

    def built_tree(self, preorder, inorder):
        pass

def main():
    s = Solution()

    preorder = [3,9,20,15,7]
    root = s.build_preorder(preorder)
    s.pretty_print(root)
    l = []
    s.to_inorder(root, 0, l)
    print(l)

    inorder = [9,3,15,20,7]

if __name__ == '__main__':
    main()
