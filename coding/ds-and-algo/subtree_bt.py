
# On Leetcode: https://leetcode.com/problems/subtree-of-another-tree/

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

    def check_subtree(self, root1, root2):
        """
        It serves to navigate the subtree. It tries to quit as soon as possible and returns a 
        positive answer only when the two substrees are fully browsed.
        """
        if root1 and not root2:         # got two different values (e.g. None and not None)
            return False
        if root2 and not root1:
            return False
        if root1 and root2:             # otherwise is a leaf
            if root1.val != root2.val:  # got to check the values for equality
                return False

            if not self.check_subtree(root1.left, root2.left):
                return False
            if not self.check_subtree(root1.right, root2.right):
                return False
            
        return True

    def is_subtree(self, root1, root2):
        """
        The algorithm can proceed recursively and find a first match; upon a first match then it
        can proceed to further match recursively the subtree and return immediately if it can
        determine that the subtree is identical

        It makese use of a helper function to check for equality on the subtree.
        """
        if root1:
            if root1.val == root2.val:
                if self.check_subtree(root1, root2):    # got to return immediately on equality
                    return True
            
            if self.is_subtree(root1.left, root2):
                return True
            if self.is_subtree(root1.right, root2):
                return True

        return False                                    # got to the end of the tree with no match

def main():
    s = Solution()

    array = [3, 4, 5, 1, 2]
    root1 = s.build_tree(array)
    s.pretty_print(root1)

    array = [4, 1, 2]
    root2 = s.build_tree(array)
    s.pretty_print(root2)
    print(s.is_subtree(root1, root2))

    array = [3, 4, 5, 1, 2, None, None, None, None, 0, None]
    root1 = s.build_tree(array)
    s.pretty_print(root1)
    print(s.is_subtree(root1, root2))

    array = [2]
    root2 = s.build_tree(array)
    s.pretty_print(root2)
    print(s.is_subtree(root1, root2))

    array = [2, 1, None]
    root2 = s.build_tree(array)
    s.pretty_print(root2)
    print(s.is_subtree(root1, root2))

    array = [11, 7, 20]
    root2 = s.build_tree(array)
    s.pretty_print(root2)
    print(s.is_subtree(root1, root2))

if __name__ == '__main__':
    main()
