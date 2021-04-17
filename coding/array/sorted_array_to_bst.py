
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def pretty_print(self, indent=0):
        print(''.join(['  ' for _ in range(indent)]) + str(self.val))

        if self.left:
            self.left.pretty_print(indent + 1)
        if self.right:
            self.right.pretty_print(indent +1 )

class Solution(object):
    def visit(self, root, output):
        if root:
            if root.left or root.right:
                left = None
                right = None
                if root.left:
                    left = root.left.val
                if root.right:
                    right = root.right.val
                
                output.append(left)
                output.append(right)
            
            self.visit(root.left, output)
            self.visit(root.right, output)

    def level_order(self, root):
        output = [root.val]
        self.visit(root, output)

        return output

    def build(self, array):
        mid = int(len(array) / 2)
        if mid >= 0 and mid < len(array):
            node = TreeNode(array[mid])
            node.left = self.build(array[:mid])
            node.right = self.build(array[mid + 1:])

            return node
        
        return None

    def convert_to_bst(self, nums):
        '''
        Main idea: use divide and conquer to recursively divide the arrray
        by a half and so create the root of the subtree.

        [-10,-3,0,5,9] > 0
                ^
        [-10,-3]       >    3
              ^
        [-10]          >      -10
          ^
        [5,9]          >    9
           ^
        [5]            >       5
         ^
        
        '''
        return self.build(nums)

def main():
    s = Solution()

    nums = [-10,-3,0,5,9]
    root = s.convert_to_bst(nums)
    root.pretty_print()
    print(s.level_order(root))      # [0,-3,9,-10,null,5]

    nums = [1,3]
    root = s.convert_to_bst(nums)
    root.pretty_print()
    print(s.level_order(root))      # [3,1]

if __name__ == '__main__':
    main()
