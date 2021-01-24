# Graph

> In mathematics, graph theory is the study of graphs, which are mathematical structures used to model pairwise relations between objects. A graph in this context is made up of vertices (also called nodes or points) which are connected by edges (also called links or lines). A distinction is made between undirected graphs, where edges link two vertices symmetrically, and directed graphs, where edges link two vertices asymmetrically; see Graph (discrete mathematics) for more detailed definitions and for other variations in the types of graph that are commonly considered. Graphs are one of the prime objects of study in discrete mathematics.

![Directed Vs Undirected Graphs](https://miro.medium.com/max/1400/1*J9U-CK1N6X7WBAnz_m04SQ.jpeg)

## Problems

1. Enumeration
2. Subgraphs
3. Graph Coloring
4. Subsumption and Unification
5. Routing
6. Network Flow
7. Visibility
8. Covering
9. Decomposition

### Enumeration
> There is a large literature on graphical enumeration: the problem of counting graphs meeting specified conditions

### Subgraphs
> A common problem, called the subgraph isomorphism problem, is finding a fixed graph as a subgraph in a given graph. One reason to be interested in such a question is that many graph properties are hereditary for subgraphs, which means that a graph has the property if and only if all subgraphs have it too. Unfortunately, finding maximal subgraphs of a certain kind is often an NP-complete problem. 

### Graph Coloring
> Many problems and theorems in graph theory have to do with various ways of coloring graphs. Typically, one is interested in coloring a graph so that no two adjacent vertices have the same color, or with other similar restrictions. One may also consider coloring edges (possibly so that no two coincident edges are the same color), or other variations.

### Subsumption and Unification
> Constraint modeling theories concern families of directed graphs related by a partial order. In these applications, graphs are ordered by specificity, meaning that more constrained graphs—which are more specific and thus contain a greater amount of information—are subsumed by those that are more general. Operations between graphs include evaluating the direction of a subsumption relationship between two graphs, if any, and computing graph unification. The unification of two argument graphs is defined as the most general graph (or the computation thereof) that is consistent with (i.e. contains all of the information in) the inputs, if such a graph exists; efficient unification algorithms are known.

### Routing
Among the most important and known ones:

- Hamiltonian path problem
- Minimum spanning tree
- Route inspection problem (also called the "Chinese postman problem")
- Seven bridges of Königsberg
- Shortest path problem
- Steiner tree
- Three-cottage problem
- Traveling salesman problem (NP-hard)

### Network Flow
There are numerous problems arising especially from applications that have to do with various notions of flows in networks, for example: Max flow min cut theorem.

### Decomposition Problem
> Decomposition, defined as partitioning the edge set of a graph (with as many vertices as necessary accompanying the edges of each part of the partition), has a wide variety of question. Often, it is required to decompose a graph into subgraphs isomorphic to a fixed graph; for instance, decomposing a complete graph into Hamiltonian cycles. Other problems specify a family of graphs into which a given graph should be decomposed, for instance, a family of cycles, or decomposing a complete graph Kn into n − 1 specified trees having, respectively, 1, 2, 3, ..., n − 1 edges.

## Data Structures

### Adjacency List
> Vertices are stored as records or objects, and every vertex stores a list of adjacent vertices. This data structure allows the storage of additional data on the vertices. Additional data can be stored if edges are also stored as objects, in which case each vertex stores its incident edges and each edge stores its incident vertices.
 
![Adjacency List](https://miro.medium.com/max/1400/1*XPH-Z7fBfBT1mEcN03FOJA.jpeg)

### Ajacency Matrix
> A two-dimensional matrix, in which the rows represent source vertices and columns represent destination vertices. Data on edges and vertices must be stored externally. Only the cost for one edge can be stored between each pair of vertices.

![Adjacency Matrix](https://miro.medium.com/max/1000/1*bllOr7NiKf4YbNtqg1cEqA.jpeg)

### Incidence Matrix
> A two-dimensional Boolean matrix, in which the rows represent the vertices and columns represent the edges. The entries indicate whether the vertex at a row is incident to the edge at a column.

## Traversal Algorithms

![DFS Vs BFS](https://miro.medium.com/max/1400/1*ri9EgM7xLmrZmywgwt96pQ.jpeg)

![DFS Vs BFS Cont'd](https://miro.medium.com/max/1400/1*_v6x7az3pWGaBWYo-fYMwg.jpeg)

### Depth-first Search

> The DFS algorithm is much like solving a maze. If you’ve ever been to a real-life maze or found yourself solving one on paper, then you know that the trick to solving a maze centers around following a path until you can’t follow it anymore, and then backtracking and retracing your steps until you find another possible path to follow.

![About DFS](https://miro.medium.com/max/1000/1*cskJKPVMALaDnD2WMyJENA.jpeg)
### Breadth-first Search

> the breadth-first search algorithm traverses broadly into a structure, by visiting neighboring sibling nodes before visiting children nodes. In both tree and graph traversal, the BFS algorithm implements a queue data structure.

![About BFS](https://miro.medium.com/max/1000/1*uwLddOZZksio58lCixU-Dw.jpeg)

## Common Algorithms

### Dijikstra

### Kruskal

### A* Serach

# References
- [Graph Theory](https://en.wikipedia.org/wiki/Graph_(abstract_data_type)#:~:text=A%20graph%20data%20structure%20consists,pairs%20for%20a%20directed%20graph.)
- [Graph Abstract Data Type](https://en.wikipedia.org/wiki/Graph_(abstract_data_type)#:~:text=A%20graph%20data%20structure%20consists,pairs%20for%20a%20directed%20graph.)
- [From Theory to Practice Representing Graph](https://medium.com/basecs/from-theory-to-practice-representing-graphs-cfd782c5be38)
- [Depth-first Search](https://medium.com/basecs/deep-dive-through-a-graph-dfs-traversal-8177df5d0f13)
- [Breadth-first Search](https://medium.com/basecs/going-broad-in-a-graph-bfs-traversal-959bd1a09255)