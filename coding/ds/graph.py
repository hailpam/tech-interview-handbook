'''
A Graph data structure defines an ensemble of vertices and edges with the latter ones defining the connectivity, 
also interpreted as relationships between nodes. Theoretically, a Graph might be seen as a Tree with loops. There
are two primary types: 1. directed and 2. undirected. The former defines a straight direction between a pair of 
vertices; instead, the latter defines a connectivity which is two-ways navigable. A graph can also be 1. weighted or
2. unweighted. In the former case, each and every edge has a weight associated which might be required for the
computational logic (e.g. shortest path).

Exmaple:

    1. Directed

        10 -+-> 12 -> 1 <-+
            |             |
            +->  2 -------+

    2. Undirected

        10 -+- 12 -> 1 -+
            |           |
            +-  2 ------+

There are two main in-memory representations for a Graph: 1. adjacency list and 2. adjacency matrix. The latter is 
less efficient due to the high degree of sparsity if compared to an adjacency list.

Reference: https://www3.cs.stonybrook.edu/~skiena/373/newlectures/lecture10.pdf
'''

class Vertex(object):
    '''
    Abstraction of a vertex.
    '''
    def __init__(self, id, edges=[]):
        self.id = id
        self.edges = edges
    
    def __eq__(self, other):
        if self.id == other.id:
            return True
        return False

class Edge(object):
    '''
    Abstraction of an edge.
    '''
    def __init__(self, weight, to):
        self.weight = weight
        self.to = to

class Graph(object):
    '''
    Implements a directed and weighted Graph data structure with a basic interface.
    '''
    def __init__(self, vertices={}):
        self.vertices = vertices
    
    def add_vertex(self, vertex):
        self.vertices[vertex.id] = vertex

    def add_edge(self, vertex, edge):
        if vertex.id in self.vertices:
            self.vertices[vertex.id].edges.append(edge)

    def remove_vertex(self, vertex):
        del self.vertices[vertex.id]
        # got to remove all dangling edges (seen the removal)
        for id in self.vertices:
            vertex = self.vertices[id]
            edges = []
            for edge in vertex.edges:
                if edge.to != vertex.id:
                    edges.append(edge)
            # re-init the edge list: dangling ones should be gone now
            vertex.edges = edges

    def remove_edge(self, vertex, edge):
        if vertex.id in self.vertices:
            edges = []
            for e in self.vertices[vertex.id].edges:
                if e.to != edge.to:
                    edges.append(e)
            # re-init the edge list: edge should be gone now
            self.vertices[vertex.id].edges = edges

    def prettyprint(self, source, visited=set(), indent=0):
        vertex = self.vertices[source]
        print('%s%s' % (indent * ' ', vertex.id))
        if source in visited:
            return
        visited.add(vertex.id)
        for edge in vertex.edges:
            self.prettyprint(edge.to, visited, indent + 2)

def main():
    graph = Graph()
    ten = Vertex(10, [])
    twelve = Vertex(12, [])
    two = Vertex(2, [])
    one = Vertex(1, [])
    graph.add_vertex(ten)
    graph.add_vertex(twelve)
    graph.add_vertex(two)
    graph.add_vertex(one)

    to_twelve = Edge(100, 12)
    to_two = Edge(101, 2)
    to_one = Edge(99, 1)
    graph.add_edge(ten, to_twelve)
    graph.add_edge(ten, to_two)
    graph.add_edge(two, to_one)
    graph.add_edge(twelve, to_one)
    graph.add_edge(one, to_twelve)

    graph.prettyprint(10)

if __name__ == '__main__':
    main()
