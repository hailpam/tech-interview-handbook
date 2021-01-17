
# On Leetcode: https://leetcode.com/problems/binary-tree-level-order-traversal/

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def pretty_print(self, root, idx=0):
        if root:
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
    
    def visit(self, root, nodes):
        """
        Visits recursively the tree to build the level order serialization.
        """
        if root:                            # got to check whether the root is not None
            if root.left or root.right:     # got to have at least one value not None
                if root.left.val or root.right.val:
                    nodes.append([root.left.val, root.right.val])
            
            self.visit(root.left, nodes)
            self.visit(root.right, nodes)

    def level_order(self, root):
        """
        The algorithm proceeds recursively to build the level order serialization.
        It makes use of an helper and includes the root by default.
        """
        nodes = []
        if root.val:
            nodes.append([root.val])

        self.visit(root, nodes)

        return nodes

def main():
    s = Solution()

    array = [3, 9, 20, None , None, 15, 7]
    root = s.build_tree(array)
    s.pretty_print(root)
    print(s.level_order(root))

if __name__ == '__main__':
    main()
