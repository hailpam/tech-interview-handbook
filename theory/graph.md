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
In this section, a number of well-known algorithms are reported. Those algorithms are the ones that typically help solve problems on Graphs, so it is important to keep them in mind as an integral part of toolbox of algorithms and solution to be applied.

### Dijkstra (Shortest Path)

![Sortherst Path Representation](https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif)

> Dijkstra's algorithm (or Dijkstra's Shortest Path First algorithm, SPF algorithm is an algorithm for finding the shortest paths between nodes in a graph, which may represent, for example, road networks. It was conceived by computer scientist Edsger W. Dijkstra in 1956 and published three years later.

> The algorithm exists in many variants. Dijkstra's original algorithm found the shortest path between two given nodes, but a more common variant fixes a single node as the "source" node and finds shortest paths from the source to all other nodes in the graph, producing a shortest-path tree.

An illustration of the Dijikstra algorithm:

![Illustration of Dijkstra Algorithm #1](https://upload.wikimedia.org/wikipedia/commons/2/23/Dijkstras_progress_animation.gif)

![Illustration of Dijkstra Algorithm #2](https://upload.wikimedia.org/wikipedia/commons/e/e4/DijkstraDemo.gif)

#### Pseudocode
```
1  function Dijkstra(Graph, source):
2      dist[source] ← 0                           // Initialization
3
4      create vertex priority queue Q
5
6      for each vertex v in Graph:          
7          if v ≠ source
8              dist[v] ← INFINITY                 // Unknown distance from source to v
9              prev[v] ← UNDEFINED                // Predecessor of v
10
11         Q.add_with_priority(v, dist[v])
12
13
14     while Q is not empty:                      // The main loop
15         u ← Q.extract_min()                    // Remove and return best vertex
16         for each neighbor v of u:              // only v that are still in Q
17             alt ← dist[u] + length(u, v)
18             if alt < dist[v]
19                 dist[v] ← alt
20                 prev[v] ← u
21                 Q.decrease_priority(v, alt)
22
23     return dist, prev
```

### Kruskal (Minimum Spanning Tree)

![Minimum Spanning Tree Representation](https://upload.wikimedia.org/wikipedia/commons/b/bb/KruskalDemo.gif)

> Kruskal's algorithm finds a minimum spanning forest of an undirected edge-weighted graph. If the graph is connected, it finds a minimum spanning tree. (A minimum spanning tree of a connected graph is a subset of the edges that forms a tree that includes every vertex, where the sum of the weights of all the edges in the tree is minimized. 

> For a disconnected graph, a minimum spanning forest is composed of a minimum spanning tree for each connected component).

> It is a greedy algorithm in graph theory as in each step it adds the next lowest-weight edge that will not form a cycle to the minimum spanning forest.

#### Pseudocode
```
algorithm Kruskal(G) is
    F:= ∅
    for each v ∈ G.V do
        MAKE-SET(v)
    for each (u, v) in G.E ordered by weight(u, v), increasing do
        if FIND-SET(u) ≠ FIND-SET(v) then
            F:= F ∪ {(u, v)}
            UNION(FIND-SET(u), FIND-SET(v))
    return F
```

### A* Serach (Best-fit Search)

![Representation of the Best-fit Search Algorithm](https://upload.wikimedia.org/wikipedia/commons/9/98/AstarExampleEn.gif)

> A* (pronounced "A-star") is a graph traversal and path search algorithm, which is often used in many fields of computer science due to its completeness, optimality, and optimal efficiency. One major practical drawback is its O(b^d) space complexity, as it stores all generated nodes in memory. Thus, in practical travel-routing systems, it is generally outperformed by algorithms which can pre-process the graph to attain better performance, as well as memory-bounded approaches; however, A* is still the best solution in many cases.

> A* is an informed search algorithm, or a best-first search, meaning that it is formulated in terms of weighted graphs: starting from a specific starting node of a graph, it aims to find a path to the given goal node having the smallest cost (least distance travelled, shortest time, etc.). It does this by maintaining a tree of paths originating at the start node and extending those paths one edge at a time until its termination criterion is satisfied.

> At each iteration of its main loop, A* needs to determine which of its paths to extend. It does so based on the cost of the path and an estimate of the cost required to extend the path all the way to the goal. Specifically, A* selects the path that minimizes f(n) = g(n) + h(n)  where n is the next node on the path, g(n) is the cost of the path from the start node to n, and h(n) is a heuristic function that estimates the cost of the cheapest path from n to the goal. A* terminates when the path it chooses to extend is a path from start to goal or if there are no paths eligible to be extended. The heuristic function is problem-specific. If the heuristic function is admissible, meaning that it never overestimates the actual cost to get to the goal, A* is guaranteed to return a least-cost path from start to goal.

![Illustration of A* Algorithm 1](https://upload.wikimedia.org/wikipedia/commons/5/5d/Astar_progress_animation.gif)

![Illustration of A* Algorithm 2](https://upload.wikimedia.org/wikipedia/commons/6/60/A%2A_Search_Example_on_North_American_Freight_Train_Network.gif)

#### Pseudocode
```
// A* (star) Pathfinding
// Initialize both open and closed list
let the openList equal empty list of nodes
let the closedList equal empty list of nodes
// Add the start node
put the startNode on the openList (leave it's f at zero)
// Loop until you find the end
while the openList is not empty
    // Get the current node
    let the currentNode equal the node with the least f value
    remove the currentNode from the openList
    add the currentNode to the closedList
    // Found the goal
    if currentNode is the goal
        Congratz! You've found the end! Backtrack to get path
    // Generate children
    let the children of the currentNode equal the adjacent nodes
    
    for each child in the children
        // Child is on the closedList
        if child is in the closedList
            continue to beginning of for loop
        // Create the f, g, and h values
        child.g = currentNode.g + distance between child and current
        child.h = distance from child to end
        child.f = child.g + child.h
        // Child is already in openList
        if child.position is in the openList's nodes positions
            if the child.g is higher than the openList node's g
                continue to beginning of for loop
        // Add the child to the openList
        add the child to the openList
```

### Dijkstra Vs A*

| ![Dijkstra's](https://miro.medium.com/max/420/1*2jRCHqAbTCY7W7oG5ntMOQ.gif) | Dijkstra's. So taking a look at Dijkstra’s algorithm, we see that it just keeps searching. It has no idea which node is ‘best’, so it calculates paths for them all. |
------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| ![A*](https://miro.medium.com/max/420/1*HppvOLfDxXqQRFn0Cv2dHQ.gif)         | With A*, we see that once we get past the obstacle, the algorithm prioritizes the node with the lowest f and the ‘best’ chance of reaching the end.          |

# References
- [Graph Theory](https://en.wikipedia.org/wiki/Graph_(abstract_data_type)#:~:text=A%20graph%20data%20structure%20consists,pairs%20for%20a%20directed%20graph.)
- [Graph Abstract Data Type](https://en.wikipedia.org/wiki/Graph_(abstract_data_type)#:~:text=A%20graph%20data%20structure%20consists,pairs%20for%20a%20directed%20graph.)
- [From Theory to Practice Representing Graph](https://medium.com/basecs/from-theory-to-practice-representing-graphs-cfd782c5be38)
- [Depth-first Search](https://medium.com/basecs/deep-dive-through-a-graph-dfs-traversal-8177df5d0f13)
- [Breadth-first Search](https://medium.com/basecs/going-broad-in-a-graph-bfs-traversal-959bd1a09255)
- [Dijikstra's Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
- [Kruskal's Algorithnm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm)
- [A* Algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm)
- [Easy A* Pathfinding](https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2)