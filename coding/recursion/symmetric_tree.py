
# On Leetcode: https://leetcode.com/problems/symmetric-tree/

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def print_tree(self, root, indent=0):
        if root:
            print('%s%s' % (''.join([' ' for x in range(indent)]), root.val if root.val else 'NIL'))
            self.print_tree(root.left, indent + 2)
            self.print_tree(root.right, indent + 2)

    def build_tree(self, nums, idx=0):
        """
         0  1     2
        [1,2,2,3,4,4,3]

        """
        if idx > len(nums) - 1:
            return None
        
        node = TreeNode()
        node.val = nums[idx]
        node.left = self.build_tree(nums, idx * 2 + 1)
        node.right = self.build_tree(nums, idx * 2 + 2)

        return node

    def is_mirror(self, left, right):
        if not left and not right:
            return True
        if left.val and not right.val:
            return False
        if right.val and not left.val:
            return False
        if left.val != right.val:
            return False
        
        return self.is_mirror(left.left, right.right) and \
               self.is_mirror(left.right, right.left)

    def is_symmetric(self, root):
        return self.is_mirror(root.left, root.right)

def main():
    s = Solution()
    nums = [1,2,2,3,4,4,3]
    root = s.build_tree(nums)
    s.print_tree(root)
    print(s.is_symmetric(root))
    nums = [1,2,2,None,3,None,3]
    root = s.build_tree(nums)
    s.print_tree(root)
    print(s.is_symmetric(root))

if __name__ == '__main__':
    main()
