
# On GeeksForGeeks: https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/

class GraphNode(object):
    def __init__(self, val, successors):
        self.val = val
        self.successors = successors

class Solution(object):
    def check_connected_component(self, node, visited):
        visited.add(node.val)
        for successors in node.successors:
            self.check_connected_component(successors, visited)

    def nr_connected_components(self, nodes):
        """
        The main idea consists is recursively browse the connected compoenents marking the nodes
        as visited. And, continue the browsing only for those nodes not yet visited.
        """
        visited = set()
        nr = 0
        for node in nodes:
            if node.val not in visited:
                self.check_connected_component(node, visited)
                nr += 1
        
        return nr

def main():
    s = Solution()

    node_0 = GraphNode(1, [])
    node_1 = GraphNode(1, [])
    node_0.successors.append(node_1)
    node_2 = GraphNode(2, [])
    node_1.successors.append(node_2)
    node_3 = GraphNode(3, [])
    node_4 = GraphNode(4, [])
    node_3.successors.append(node_4)
    nodes = []
    nodes.append(node_0)
    nodes.append(node_1)
    nodes.append(node_2)
    nodes.append(node_3)
    nodes.append(node_4)
    print(s.nr_connected_components(nodes)) # 2

if __name__ == '__main__':
    main()
