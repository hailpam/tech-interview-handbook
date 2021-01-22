
# On Leetcode: https://leetcode.com/problems/same-tree/

class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def build_tree(array, idx=0):
    if idx >= len(array):
        return None

    node = TreeNode(array[idx])
    node.left = build_tree(array, idx * 2 + 1)
    node.right = build_tree(array, idx * 2 + 2)

    return node

def pretty_print(root, idx=0):
    if root:
        print('%s%s' % (''.join(['  ' for _ in range(idx)]), root.value))
        pretty_print(root.left, idx + 1)
        pretty_print(root.right, idx + 1)

class Solution(object):
    def is_same_tree(self, p, q):
        if p and not q:
            return False
        if q and not p:
            return False
        if p and q:
            if p.value != q.value:
                return False
            if not self.is_same_tree(p.left, q.left):
                return False
            if not self.is_same_tree(p.right, q.right):
                return False

        return True

def main():
    s = Solution()

    p = [1, 2, 3]
    root_p = build_tree(p)
    pretty_print(root_p)
    q = [1, 2, 3]
    root_q = build_tree(q)
    pretty_print(root_q)
    print(s.is_same_tree(root_p, root_q))   # True

    p = [1, 2]
    root_p = build_tree(p)
    pretty_print(root_p)
    q = [1, None, 2]
    root_q = build_tree(q)
    pretty_print(root_q)
    print(s.is_same_tree(root_p, root_q))   # False

    p = [1, 2, 1]
    root_p = build_tree(p)
    pretty_print(root_p)
    q = [1, 1, 2]
    root_q = build_tree(q)
    pretty_print(root_q)
    print(s.is_same_tree(root_p, root_q))   # False

if __name__ == '__main__':
    main()
