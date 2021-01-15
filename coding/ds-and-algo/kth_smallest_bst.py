
# On Leetcode: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def build_tree(self, array, idx=0):
        if idx >= len(array):
            return None
        
        node = Node(array[idx])
        node.left = self.build_tree(array, idx * 2 + 1)
        node.right = self.build_tree(array, idx * 2 + 2)

        return node

    def pretty_print(self, root, idx=0):
        if not root:
            return
        
        print('%s%s' % (''.join(['  ' for _ in range(idx)]), root.val))
        self.pretty_print(root.left, idx + 1)
        self.pretty_print(root.right, idx + 1)
    
    def visit(self, root, inorder=[]):
        """
        In-order visit that serializes the BST into an ordered array
        """
        if not root:
            return
        
        self.visit(root.left, inorder)
        if root.val:                    # as None values are not discarded meanwhile building the tree
            inorder.append(root.val)
        self.visit(root.right, inorder)

    def kth_smallest(self, root, k):
        """
        Considering the nature of a BST, an inorder traversal helps with
        identifying the k-th smallest element.
        """
        inorder = []
        self.visit(root, inorder)

        return inorder[k - 1]

def main():
    s = Solution()

    array = [3, 1, 4, None, 2]
    k = 1
    root = s.build_tree(array)
    s.pretty_print(root)
    print(s.kth_smallest(root, k))

    array = [5, 3, 6, 2, 4, None, None, 1]
    k = 3
    root = s.build_tree(array)
    s.pretty_print(root)
    print(s.kth_smallest(root, k))

if __name__ == '__main__':
    main()
