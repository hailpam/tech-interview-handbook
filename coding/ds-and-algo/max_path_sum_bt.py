
# On Leetcode: https://leetcode.com/problems/binary-tree-maximum-path-sum/

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(array, idx=0):
    if idx >= len(array):
        return None
    
    root = TreeNode(array[idx])
    root.left = build_tree(array, idx * 2 + 1)
    root.right = build_tree(array, idx * 2 + 2)

    return root

def pretty_print(root, idx=0):
    if root:
        print('%s%s' % (''.join(['  ' for _ in range(idx)]), root.val))
        pretty_print(root.left, idx + 1)
        pretty_print(root.right, idx + 1)

class Solution(object):
    def max_path_sum(self, root):
        """
        Recursrively browse the binary tree to check for each subtree the path sum to then
        pick the max among all path sums.

        step 0: 
        -10             <
            9
                None
                None
            20
                15
                7
        
        step 1: 
        -10             
            9           (9)
                None
                None
            20
                15
                7
        
        step 2: 
        -10             
            9           (9)
                None
                None
            20          (42)
                15
                7
        
        step 3: 
        -10             (9, 42, 9 + 42 - 10) -> 42
            9           (9)
                None
                None
            20          (42)
                15
                7
        """
        if not root:                                # got on a leaf, value is 0 by default
            return 0
        
        left_sum = self.max_path_sum(root.left)     # got to retrieve the paths sum one by one
        right_sum = self.max_path_sum(root.right)
        curr_sum = (root.val if root.val else 0) + left_sum + right_sum

        return max(left_sum, right_sum, curr_sum)   # return the max on per level basis

def main():
    s = Solution()

    array = [1, 2, 3]
    root = build_tree(array)
    pretty_print(root)
    print(s.max_path_sum(root))

    array = [-10, 9, 20, None, None, 15, 7]
    root = build_tree(array)
    pretty_print(root)
    print(s.max_path_sum(root))

if __name__ == '__main__':
    main()
