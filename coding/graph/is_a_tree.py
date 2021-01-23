
# On GeeksForGeeks: https://www.geeksforgeeks.org/check-given-graph-tree/

class GraphNode(object):
    def __init__(self, val, successors=[]):
        self.val = val
        self.successors = successors

class Solution(object):
    def visit(self, root, visited):
        """
        Helper method performing a depth-first-search looking for cycles.
        """
        if root.val in visited:
            return False
        
        for successor in root.successors:
            visited.add(root.val)
            if not self.visit(successor, visited):
                return False
        
        return True
    
    def is_tree(self, root):
        """
        The main ides is to check whether there is a cycle. In case of a cycle, 
        the graph cannot be a well-formed tree.
        """
        return self.visit(root, set())

def main():
    s = Solution()

    root = GraphNode(0, [])
    root.successors.append(GraphNode(1, []))
    root.successors.append(GraphNode(2, []))
    child_3 = GraphNode(3, [])
    child_3.successors.append(GraphNode(4, []))
    root.successors.append(child_3)
    print(s.is_tree(root))  # True

    root = GraphNode(0, [])
    child_1 = GraphNode(1, [])
    child_2 = GraphNode(2, [])
    child_2.successors.append(root)
    child_1.successors.append(child_2)
    root.successors.append(child_1)
    root.successors.append(child_2)
    child_3 = GraphNode(3, [])
    child_3.successors.append(GraphNode(4, []))
    root.successors.append(child_3)
    print(s.is_tree(root))  # False

if __name__ == '__main__':
    main()
