
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
        
        left = self.left(root.left, p, q)
        right = self.right(root.right, p, q)

        if left != -1:
            return left
        if right != -1:
            return right
        if p == root.val or p == root.left.val or p == root.right.val:
            if q == root.left.val or q == root.right.val:
                return root.val

        return -1 

def main():
    s = Solution()

    array = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5] 
    p = 2
    q = 8
    root = s.build_tree(array)
    s.pretty_print(root)
    print(s.lca(root, p, q))

    array = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5] 
    p = 2
    q = 8
    root = s.build_tree(array)
    s.pretty_print(root)
    print(s.lca(root, p, q))

    array = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    p = 2
    q = 4
    root = s.build_tree(array)
    s.pretty_print(root)
    print(s.lca(root, p, q))

    array = [2, 1]
    p = 2
    q = 1
    root = s.build_tree(array)
    s.pretty_print(root)
    print(s.lca(root, p, q))

if __name__ == '__main__':
    main()
