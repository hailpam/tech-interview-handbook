
# On Leetcode: https://leetcode.com/problems/clone-graph/

class Node(object):
    def __init__(self, val=-1):
        self.val = val
        self.neighbors = []
    
    def __str__(self):
        return '%s %s' % (self.val, [n.val for n in self.neighbors])

class Solution(object):
    def visit(self, node, nodes):
        if node:
            if node.val in nodes:
                return nodes[node.val]
            else:
                node_cpy = Node(node.val)
                nodes[node.val] = node_cpy
                for neighbor in node.neighbors:
                    if neighbor.val in nodes:
                        node_cpy.neighbors.append(nodes[neighbor.val])
                    else:
                        node_cpy.neighbors.append(self.visit(neighbor, nodes))

                return node_cpy

        return None

    def clone_graph(self, node):
        if node:
            nodes = {}

            return self.visit(node, nodes)

        return None

def adj_list_to_graph(adj_list):
    """
    Helper function to step from an adjancency list to a graph.
    """
    node_list = []
    for idx in range(len(adj_list)):
        node_list.append(Node(idx + 1))

    for idx, neighbors in enumerate(adj_list):
        node = node_list[idx]
        for neighbor in neighbors:
            node.neighbors.append(node_list[neighbor - 1])

    return node_list[0] if node_list else None

def graph_to_adj_list(node, adj_list=[], visited=[]):
    """
    Helper function to step from a graph to an adjacency list.
    """
    if node:
        visited.append(node.val)
        for neighbor in node.neighbors:
            if len(adj_list) < neighbor.val:
                for _ in range(neighbor.val - len(adj_list)):
                    adj_list.append([])
            adj_list[node.val - 1].append(neighbor.val)
            if neighbor.val not in visited:
                graph_to_adj_list(neighbor, adj_list)
    
    if not adj_list and node:   # special case of disconnected vertices
        adj_list.append([])

    return adj_list

def main():
    s = Solution()

    adj_list = [
        [2,4],  # node #1
        [1,3],  # node #2
        [2,4],  # node #3
        [1,3]   # node #4
    ]
    print(graph_to_adj_list(s.clone_graph(adj_list_to_graph(adj_list)), []))
    
    adj_list = [[]]
    print(graph_to_adj_list(s.clone_graph(adj_list_to_graph(adj_list)), []))

    adj_list = []
    print(graph_to_adj_list(s.clone_graph(adj_list_to_graph(adj_list)), []))

    adj_list = [
        [2],
        [1]
    ]
    n = s.clone_graph(adj_list_to_graph(adj_list))
    
    print(graph_to_adj_list(s.clone_graph(adj_list_to_graph(adj_list)), []))

if __name__ == '__main__':
    main()
