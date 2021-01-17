
# On Leetcode: https://leetcode.com/problems/validate-binary-search-tree/

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

    def validate_bst(self, root):
        """
        The main ides is to recursively check the subtrees up to the leaves. 
        A check between left and right children needs to be carried out with
        the local root to make sure that the invariante stays.
        """
        if root:
            if not self.validate_bst(root.left):  # got to return immediately on any violation of invariant
                return False
            if not self.validate_bst(root.right):
                return False

            if root.left and root.left.val:       # got to check the invariant
                if root.val < root.left.val:
                    return False
            if root.right and root.right.val:
                if root.val > root.right.val:
                    return False
        
        return True

def main():
    s = Solution()

    array = [2,1,3]
    root = s.build_tree(array)
    s.pretty_print(root)
    print(s.validate_bst(root))

    array = [5, 1, 4, None, None, 3, 6]
    root = s.build_tree(array)
    s.pretty_print(root)
    print(s.validate_bst(root))

    array = [10, 1, 6, None, None, 7, 3]
    root = s.build_tree(array)
    s.pretty_print(root)
    print(s.validate_bst(root))

if __name__ == '__main__':
    main()
