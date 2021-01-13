
# On Leetcode: https://leetcode.com/problems/maximum-depth-of-binary-tree/

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def max_depth(self, root, cntr=0):
        if not root:
            return cntr
                
        depth_left = self.max_depth(root.left, cntr + 1)
        depth_right = self.max_depth(root.right, cntr + 1)

        return max(depth_left, depth_right)

def build_tree(bst_array, idx=0):
    """
    Helper, just build a tree recursively from an array.
    """
    if idx >= len(bst_array):
        return None

    node = Node(bst_array[idx])
    if node.val:
        node.left = build_tree(bst_array, idx * 2 + 1)
        node.right = build_tree(bst_array, idx * 2 + 2)

    return node

def pretty_print(root, lvl=0):
    """
    Helper, just pretty prints the tree built recursively.
    """
    if not root:
        return
    
    print('%s%s' % (''.join(['  ' for _ in range(lvl)]), root.val if root else None))
    pretty_print(root.left, lvl + 1)
    pretty_print(root.right, lvl + 1)

def main():
    s = Solution()

    bst = [3, 9, 20, None, None, 15, 7]
    root = build_tree(bst)
    pretty_print(root)
    print(s.max_depth(root))

    bst = [1, None, 2]
    root = build_tree(bst)
    pretty_print(root)
    print(s.max_depth(root))

    bst = []
    root = build_tree(bst)
    pretty_print(root)
    print(s.max_depth(root))

    bst = [0]
    root = build_tree(bst)
    pretty_print(root)
    print(s.max_depth(root))

if __name__ == '__main__':
    main()
