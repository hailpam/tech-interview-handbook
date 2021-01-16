
# On Leetcode: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

class Node(object):
    def __init__(self, val=0, left=None, right=None):
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
        
        root = Node(array[idx])
        root.left = self.build_tree(array, idx * 2 + 1)
        root.right = self.build_tree(array, idx * 2 + 2)

        return root

    def lca(self, root, p, q):
        """
        In the assumptions that v1 and v2 exists, and that are picked to have
        a common ancestor, there are three cases to account for:

            1. v1 or v2 gets as left child v2 or v1
            2. v1 or v2 gets as right child v2 or v1
            3. a node gets v1 or v2 as left or right child
        
        It is immediate that for case 1 and 2, v1 or v2 is the lowest common
        ancestor. For case 3, the node itself is the lowest common ancestor.

        There are two main solutions for this problem. First, enlisting the paths
        to the v1 and to the v2, for a succesive match for the ancestor. Second,
        using the recursive stack to:

            1. return null in case of a leaf
            2. return the node in case of match with v1 or v2
            3. return the node in case of left and right not null
            4. return the non null node to any step
        
        Case 3 reports the common ancestor, considering that for case 4 it will be
        bubbled up only the non null.

        step 0 - (0, 3)
        2 <
          0
          4
            3
            5
        
        step 1 - (0, 3)
        2 
          0 < (0)
          4
            3
            5
        
        step 2 - (0, 3)
        2 
          0 
          4 <
            3
            5

        step 3 - (0, 3)
        2 
          0 
          4
            3 < (3)
            5
        
        step 3 - (0, 3)
        2 
          0 
          4
            3 
            5 < (null)
        
        step 4 - (0, 3)
        2 
          0 
          4 < (3, null) -> (3)
            3 
            5 
        
        step 5 - (0, 3)
        2 < (0,3) -> (2)
          0 
          4 
            3 
            5 
        """
        if not root:                            # parent was leaf
            return None
        
        left = self.lca(root.left, p, q)
        right = self.lca(root.right, p, q)
        if left and right:                      # got p and q, need to return this node
            return root
        if root.val == p or root.val == q:      # got either p or q, need to return this node
            return root
        
        return left if left else right          # arbitrate, if both null, then null

def main():
    s = Solution()

    array = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5] 
    p = 2
    q = 8
    root = s.build_tree(array)
    s.pretty_print(root)
    print(s.lca(root, p, q).val)

    array = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5] 
    p = 2
    q = 7
    root = s.build_tree(array)
    s.pretty_print(root)
    print(s.lca(root, p, q).val)

    array = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5] 
    p = 0
    q = 3
    root = s.build_tree(array)
    s.pretty_print(root)
    print(s.lca(root, p, q).val)

    array = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    p = 2
    q = 4
    root = s.build_tree(array)
    s.pretty_print(root)
    print(s.lca(root, p, q).val)

    array = [2, 1]
    p = 2
    q = 1
    root = s.build_tree(array)
    s.pretty_print(root)
    print(s.lca(root, p, q).val)

if __name__ == '__main__':
    main()
