# On Leetcode: https://leetcode.com/problems/search-in-a-binary-search-tree/

class Solution(object):
    def visit(self, root, val, subtree, idx=0, found=False):
        if idx >= len(root):                                            # out of bound
            return
        if root[idx] == val:                                            # found it, got to add all children
            found = True
        if found:
            subtree.append(root[idx])                                   # found it, got to add all children
        
        self.visit(root, val, subtree, idx=2 * idx + 1, found=found)    # left child
        self.visit(root, val, subtree, idx=2 * idx + 2, found=found)    # right child
    
    def search_bst(self, root, val):
        subtree = []
        self.visit(root, val, subtree)
        
        return subtree

def main():
    s = Solution()

    root = [4,2,7,1,3]
    val = 2
    print(s.search_bst(root, val))

    root = [4,2,7,1,3]
    val = 5
    print(s.search_bst(root, val))

if __name__ == '__main__':
    main()
