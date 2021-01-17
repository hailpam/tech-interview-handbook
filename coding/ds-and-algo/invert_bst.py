
# On Leetcode: https://leetcode.com/problems/invert-binary-tree/

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def pretty_print(self, root, idx=0):
        if not root:
            return

        print('%s%s' % (''.join(['  ' for _ in range(idx)]), root.val))
        self.pretty_print(root.left, idx + 1)
        self.pretty_print(root.right, idx + 1)

    def build_tree(self, array, idx=0):
        if idx >= len(array):
            return None
        
        root = TreeNode(array[idx])
        root.left = self.build_tree(array, idx * 2 + 1)
        root.right = self.build_tree(array, idx * 2 + 2)

        return root

    def invert_bst(self, root):
        """
        The main idea for inverting a Binary Search Tree or more in general to
        invert a Binary tree consists in diving the problem into subproblems and
        operating on those. 

        Recursively, it is possible to invert the points from the very leaves of
        the tree getting back to the root.
        """
        if root:
            self.invert_bst(root.left)      # get to recursively navigate down
            self.invert_bst(root.right)
            
            left_tmp = root.left            # get to swap the pointers
            root.left = root.right
            root.right = left_tmp

        return root

def main():
    s = Solution()

    array = [4, 2, 7, 1, 3, 6, 9]
    root = s.build_tree(array)
    s.pretty_print(root)
    s.pretty_print(s.invert_bst(root))

if __name__ == '__main__':
    main()
