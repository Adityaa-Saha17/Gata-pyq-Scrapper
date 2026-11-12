# Volume 1 — Chapter 2: Discrete Mathematics: Graph Theory

- **Source PDF**: [filter1_volume1.pdf](file:///Users/adityaasaha/Documents/Academics/Gate/filter1_volume1.pdf)
- **Total GATE Questions in Chapter**: **88**

---

## 1. Subtopic Weightage & Question Distribution

| Subtopic # | Subtopic Name | Questions |
| :---: | :--- | :---: |
| **2.1** | Counting | 3 |
| **2.2** | Degree of Graph | 13 |
| **2.3** | Graph Algorithms | 1 |
| **2.4** | Graph Coloring | 11 |
| **2.5** | Graph Connectivity | 40 |
| **2.6** | Graph Isomorphism | 4 |
| **2.7** | Graph Matching | 2 |
| **2.8** | Graph Planarity | 13 |
| **2.9** | Jaccard Coefficient | 1 |


---

## 2. Comprehensive GATE CSE Graph Theory Reference (Expanded Research & Formulas)

### 2.1 Handshaking Lemma, Degree Sequences & Counting Graphs
- **Handshaking Lemma (Undirected Graph $G = (V, E)$)**:
  $$\sum_{v \in V} \deg(v) = 2|E|$$
  - Corollary: The number of vertices of **odd degree** in any undirected graph is always **even**.
  - For a directed graph: $\sum_{v \in V} \deg^+(v) = \sum_{v \in V} \deg^-(v) = |E|$.
- **Maximum Edges in Simple Graph with $n$ Vertices**: $\binom{n}{2} = \frac{n(n-1)}{2}$.
- **Number of Simple Labeled Graphs on $n$ Vertices**: $2^{\binom{n}{2}}$.
  - Number of simple labeled graphs with **every vertex having even degree**: $2^{\binom{n-1}{2}}$.
  - Number of labeled trees on $n$ vertices (**Cayley's Formula**): $n^{n-2}$.
- **Havel-Hakimi Theorem**: A non-increasing sequence $d_1 \ge d_2 \ge \dots \ge d_n$ is **graphic** (realizable as a simple graph) iff the sequence obtained by deleting $d_1$ and subtracting $1$ from the next $d_1$ elements ($d_2-1, \dots, d_{d_1+1}-1, d_{d_1+2}, \dots, d_n$) is graphic.

### 2.2 Special Graphs & Their Properties
| Graph Type | Notation | Vertices $|V|$ | Edges $|E|$ | Chromatic Number $\chi(G)$ | Bipartite? | Planar? |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Complete Graph** | $K_n$ | $n$ | $\binom{n}{2}$ | $n$ | Only $n \le 2$ | $n \le 4$ |
| **Cycle Graph** | $C_n$ ($n \ge 3$) | $n$ | $n$ | $2$ (even $n$), $3$ (odd $n$) | iff $n$ is even | Always |
| **Wheel Graph** | $W_n$ ($n$ total vertices) | $n$ | $2(n-1)$ | $3$ (odd $n$), $4$ (even $n$) | Never | Always |
| **Complete Bipartite** | $K_{m,n}$ | $m+n$ | $mn$ | $2$ (if $m,n \ge 1$) | Always | iff $\min(m,n) \le 2$ |
| **Hypercube** | $Q_k$ | $2^k$ | $k \cdot 2^{k-1}$ | $2$ (for $k \ge 1$) | Always | iff $k \le 3$ |
| **Tree** | $T_n$ ($n \ge 2$) | $n$ | $n-1$ | $2$ | Always | Always |

### 2.3 Connectivity, Cut Vertices, Bridges & Trees
- **Connected Components**: A simple graph with $n$ vertices and $k$ connected components obeys:
  $$n - k \le |E| \le \frac{(n-k)(n-k+1)}{2}$$
  - To guarantee a simple $n$-vertex graph is **connected**, it must have at least $|E| > \binom{n-1}{2}$, i.e., $|E| \ge \binom{n-1}{2} + 1$.
- **Vertex Connectivity $\kappa(G)$, Edge Connectivity $\lambda(G)$, Minimum Degree $\delta(G)$ (Whitney's Inequality)**:
  $$\kappa(G) \le \lambda(G) \le \delta(G)$$
  - Maximum possible edge connectivity for $n$ vertices and $e$ edges: $\lambda(G) \le \lfloor 2e/n \rfloor$.
- **Trees & Forests**:
  - Forest with $n$ vertices and $k$ components (trees) has exactly $e = n - k$ edges.
  - A sequence $(d_1, d_2, \dots, d_n)$ with $d_i \ge 1$ is the degree sequence of a tree iff $\sum_{i=1}^n d_i = 2n - 2$.

### 2.4 Eulerian & Hamiltonian Graphs
- **Eulerian Circuit** (visits every **edge** exactly once and returns to start): Connected graph (ignoring isolated vertices) has an Eulerian circuit **iff every vertex has even degree**.
- **Eulerian Path (Trail)** (visits every edge once, not necessarily closed): Exists **iff** the number of odd-degree vertices is **$0$ or $2$**.
- **Hamiltonian Cycle** (visits every **vertex** exactly once):
  - **Dirac's Theorem** (Sufficient): If $n \ge 3$ and $\deg(v) \ge n/2$ for all $v \in V$, $G$ is Hamiltonian.
  - **Ore's Theorem** (Sufficient): If $\deg(u) + \deg(v) \ge n$ for every non-adjacent pair $u, v$, $G$ is Hamiltonian.
  - **Necessary Condition**: Removing $k$ vertices from a Hamiltonian graph leaves **at most $k$ connected components**.

### 2.5 Planarity, Coloring, Matching & Covers
- **Euler's Formula for Connected Planar Graph**:
  $$v - e + r = 2 \quad \text{(for } k \text{ components: } v - e + r = k + 1\text{)}$$
- **Planarity Edge Bounds** (for simple connected planar graph with $v \ge 3$):
  - General planar graph: $e \le 3v - 6$ (implies every planar graph has a vertex of degree $\le 5$).
  - Triangle-free / Bipartite planar graph ($g \ge 4$): $e \le 2v - 4$.
  - General girth $g$: $e \le \frac{g}{g-2}(v - 2)$.
- **Kuratowski's / Wagner's Theorem**: A graph is planar iff it contains no subgraph homeomorphic to (or having as a minor) **$K_5$** or **$K_{3,3}$**.
- **Graph Coloring**:
  - **Four-Color Theorem**: For any planar graph $G$, $\chi(G) \le 4$.
  - **Brooks' Theorem**: $\chi(G) \le \Delta(G) + 1$, with equality only for complete graphs $K_n$ and odd cycles $C_{2k+1}$.
  - $\chi(G) \ge \omega(G)$ (clique number) and $\chi(G) \ge \lceil |V| / \alpha(G) \rceil$ where $\alpha(G)$ is the independence number.
- **Matching & Gallai's Identities** (for graph without isolated vertices):
  - $\alpha(G) + \beta(G) = |V|$ (Max Independent Set $\alpha$ + Min Vertex Cover $\beta = |V|$).
  - $\alpha'(G) + \beta'(G) = |V|$ (Max Matching $\alpha'$ + Min Edge Cover $\beta' = |V|$).
  - **König's Theorem (Bipartite Graphs)**: Maximum Matching size $\alpha'(G) =$ Minimum Vertex Cover size $\beta(G)$.

---

## 3. Original PDF Chapter Notes (Preserved Verbatim)

2 Discrete Mathematics: Graph Theory (88)
Syllabus: Connectivity, Matching, Coloring.
Welcome to the Graph Theory chapter, a cornerstone of Discrete Mathematics and a frequently tested area in the
GATE Computer Science examination. Graph Theory provides a powerful framework for modeling relationships and
processes across various domains, from social networks and transportation systems to computer networks and
algorithm design. For GATE CS, this subject typically carries a weightage of 5-8 marks, often integrated with Data
Structures and Algorithms. Questions range from direct application of definitions and formulas, analysis of graph
properties, tracing graph algorithms, to problem-solving scenarios involving connectivity, coloring, and planarity. A
strong grasp of graph theory fundamentals is crucial not only for scoring well but also for understanding advanced
topics in computer science.
Topic-wise Key Concepts
Counting
Counting in graph theory involves determining the number of possible graphs, paths, cycles, or specific structures within
graphs. It often relies on fundamental combinatorial principles.
Definition and Core Idea: This topic focuses on enumerating different types of graphs or substructures within them,
using principles of permutations, combinations, and other combinatorial techniques. It's about understanding how
many ways a graph can be formed or how many specific patterns exist.
Important Formulas, Theorems, and Results:
1. Number of simple labeled graphs with vertices:
This is because for each pair of vertices, there can either be an edge or not.
2. Number of simple directed labeled graphs with vertices:
For each ordered pair of distinct vertices 3. Number of spanning trees in a complete graph , there can be an edge from (Cayley's Formula):
to , or not.
This formula is critical for counting trees on a given set of labeled vertices.
4. Number of spanning trees in a general graph (Matrix Tree Theorem): This theorem uses the Laplacian
matrix of a graph, but its direct application is usually beyond GATE scope; Cayley's formula is more common.
5. Number of paths of length between two vertices in an adjacency matrix: The -th entry of (where
is the adjacency matrix) gives the number of paths of length from vertex to vertex .
Key Properties and Identities:
Understanding the difference between labeled and unlabeled graphs is crucial. GATE questions usually imply
labeled graphs unless specified.
Basic combinatorial identities like and are fundamental.
The Inclusion-Exclusion Principle can be used for more complex counting problems, especially when dealing with
properties that overlap.
Common Pitfalls or Tricky Points:
Overcounting or Undercounting: Ensure each distinct configuration is counted exactly once.
Distinguishing Labeled vs. Unlabeled: Most GATE questions assume labeled vertices unless stated
otherwise, which simplifies counting. Unlabeled graph counting is significantly harder.
Specific Graph Types: Be careful when counting paths/cycles in specific graph types like trees, complete
graphs, or bipartite graphs.

*(PDF Page 32)*

Standard Problem-Solving Techniques or Shortcuts:
Direct Application of Formulas: For simple graphs, complete graphs, and spanning trees, direct formula
application is common.
Combinatorial Arguments: Break down the problem into smaller, manageable choices and multiply/add the
possibilities.
Recurrence Relations: For counting paths or specific structures, sometimes a recurrence relation can be
formulated and solved.
Degree of Graph
The degree of a vertex is a fundamental property that quantifies its connectivity within a graph. It's essential for
understanding graph structure and validating basic graph properties.
Definition and Core Idea: The degree of a vertex , denoted or For directed graphs, we distinguish between in-degree (edges pointing to , is the number of edges incident to it.
) and out-degree (edges pointing from Important Formulas, Theorems, and Results:
1. Handshaking Lemma (for undirected graphs): The sum of the degrees of all vertices in any undirected graph
is equal to twice the number of edges.
).
This is a cornerstone theorem in graph theory.
2. For directed graphs: The sum of in-degrees equals the sum of out-degrees, and both are equal to the total
number of edges.
3. Number of odd-degree vertices: In any undirected graph, the number of vertices with odd degree must be
even. This is a direct consequence of the Handshaking Lemma.
4. Maximum degree and Minimum degree : These denote the maximum and minimum degrees
among all vertices in graph , respectively.
Key Properties and Identities:
The Handshaking Lemma is a powerful tool for checking the validity of a degree sequence or finding the number
of edges.
A graph cannot exist if its degree sequence violates the Handshaking Lemma or has an odd number of odd-
degree vertices.
For a simple graph with vertices, the maximum degree of any vertex is .
Common Pitfalls or Tricky Points:
Self-loops: In some contexts, a self-loop at a vertex contributes 2 to its degree. GATE questions usually specify
if self-loops are allowed or assume simple graphs (no self-loops, no multiple edges).
Multiple Edges: If multiple edges are allowed between two vertices, each edge contributes to the degree.
Directed vs. Undirected: Always be clear whether the graph is directed or undirected when calculating degrees.
Standard Problem-Solving Techniques or Shortcuts:
Direct Application of Handshaking Lemma: Often used to find the number of edges given a degree sequence,
or to determine if a given degree sequence is possible.
Parity Check: Quickly identify impossible degree sequences by checking the number of odd-degree vertices.
Graph Algorithms
Graph algorithms are systematic procedures for solving problems on graphs, such as finding paths, spanning trees, or
optimal routes. They are central to computer science applications.
Definition and Core Idea: These are algorithms designed to traverse, search, analyze, and optimize properties of
graphs. They form the backbone of many real-world applications, from network routing to social network analysis.
Important Algorithms, Formulas, and Complexities:
1. Breadth-First Search (BFS): Explores a graph layer by layer.
Purpose: Find shortest path in unweighted graphs, find connected components.
Time Complexity: for adjacency list, for adjacency matrix.
2. Depth-First Search (DFS): Explores as far as possible along each branch before backtracking.
Purpose: Find connected components, topological sort, detect cycles, find bridges/articulation points.

*(PDF Page 33)*

Time Complexity: for adjacency list, for adjacency matrix.
3. Dijkstra's Algorithm: Finds the shortest paths from a single source vertex to all other vertices in a graph with
non-negative edge weights.
Purpose: Single-source shortest path.
Time Complexity: with a Fibonacci heap, with a binary heap, with
adjacency matrix.
4. Prim's Algorithm: Finds a Minimum Spanning Tree (MST) in a weighted, undirected graph.
Purpose: MST.
Time Complexity: with a binary heap, with adjacency matrix.
5. Kruskal's Algorithm: Finds a Minimum Spanning Tree (MST) in a weighted, undirected graph.
Purpose: MST.
Time Complexity: or using a Disjoint Set Union (DSU) data structure.
6. Bellman-Ford Algorithm: Finds the shortest paths from a single source vertex to all other vertices, even with
negative edge weights. Detects negative cycles.
Purpose: Single-source shortest path with negative weights.
Time Complexity: .
7. Floyd-Warshall Algorithm: Finds all-pairs shortest paths in a weighted graph, can handle negative weights but
not negative cycles.
Purpose: All-pairs shortest path.
Time Complexity: .
8. Topological Sort: Linear ordering of vertices such that for every directed edge , comes before .
Applicable only to Directed Acyclic Graphs (DAGs).
Purpose: Ordering tasks with dependencies.
Time Complexity: (using DFS or Kahn's algorithm).
9. Ford-Fulkerson Algorithm (and Edmonds-Karp): Finds the maximum flow in a flow network.
Purpose: Maximum flow.
Time Complexity: Ford-Fulkerson is not polynomial in general; Edmonds-Karp is .
Key Properties and Identities:
Greedy Algorithms: Prim's, Kruskal's, Dijkstra's are greedy algorithms that make locally optimal choices.
Dynamic Programming: Floyd-Warshall and Bellman-Ford use dynamic programming principles.
Connectivity: BFS/DFS can determine if a graph is connected or find its connected components.
Cycles: DFS can detect cycles in both directed and undirected graphs.
Common Pitfalls or Tricky Points:
Negative Edge Weights: Dijkstra's fails with negative edge weights; use Bellman-Ford or Floyd-Warshall.
Disconnected Graphs: Algorithms like Dijkstra's might not reach all vertices if the graph is disconnected from
the source.
Choosing the Right Algorithm: Understand the constraints (weighted/unweighted, directed/undirected,
negative weights, single-source/all-pairs) to select the appropriate algorithm.
Adjacency List vs. Matrix: Be aware of how the graph representation affects time complexity.
Standard Problem-Solving Techniques or Shortcuts:
Tracing: Practice tracing algorithms step-by-step on small graphs to understand their mechanics.
Recognizing Patterns: Identify if a problem can be mapped to a standard graph algorithm (e.g.,
"minimum cost
to connect all cities" suggests MST).
Complexity Analysis: Be able to derive or recall the time and space complexity for common algorithms.
Graph Coloring
Graph coloring assigns labels (colors) to graph elements subject to certain constraints, often used to model scheduling
or resource allocation problems.
Definition and Core Idea: Vertex coloring assigns a color to each vertex such that no two adjacent vertices have
the same color. The minimum number of colors required for a graph is called its chromatic number, denoted
.
Important Formulas, Theorems, and Results:
1. Chromatic Number : The smallest integer such that is -colorable.
2. Lower Bound: For any graph , , where is the clique number (size of the largest clique).
3. Upper Bound (Brooks' Theorem): For a connected graph that is neither a complete graph nor an odd cycle,
, where is the maximum degree. In general, .
4. Bipartite Graphs: A graph is bipartite if and only if it contains no odd-length cycles. If a graph is bipartite and
has at least one edge, then .

*(PDF Page 34)*

5. Planar Graphs (Four Color Theorem): Every planar graph is 4-colorable. Thus, for any planar graph ,
.
6. Chromatic Polynomial : A polynomial whose value at integer is the number of ways to color using
at most colors. For a graph with vertices, is a polynomial in of degree .
Key Properties and Identities:
A graph is 2-colorable if and only if it is bipartite.
If a graph contains a clique of size , then at least colors are needed.
The chromatic number of a complete graph is .
The chromatic number of a cycle graph is 2 if is even, and 3 if is odd.
Common Pitfalls or Tricky Points:
Minimum vs. Any Coloring: The goal is to find the minimum number of colors, not just any valid coloring.
Identifying Cliques: Finding the largest clique ( ) can be hard, but it provides a lower bound for .
Edge Coloring ( ): Similar concept but for edges (adjacent edges have different colors). Vizing's Theorem
states . GATE usually focuses on vertex coloring.
Standard Problem-Solving Techniques or Shortcuts:
Greedy Coloring: Assign colors iteratively to vertices in some order (e.g., decreasing degree). While not always
optimal, it's a common heuristic.
Identify Cliques and Odd Cycles: These structures directly give lower bounds for the chromatic number.
Trial and Error/Backtracking: For small graphs, try to color with 2, then 3, etc., until a valid coloring is found.
Graph Connectivity
Graph connectivity measures how robust a graph is to the removal of vertices or edges. It's crucial for network reliability
and fault tolerance.
Definition and Core Idea: Connectivity refers to the property of a graph being "connected,
" meaning there's a path
between any two vertices. More generally, it quantifies how many vertices or edges must be removed to disconnect
the graph.
Important Formulas, Theorems, and Results:
1. Connected Graph: A graph is connected if there is a path between every pair of distinct vertices.
2. Connected Components: Maximal connected subgraphs.
3. Cut Vertex (Articulation Point): A vertex whose removal increases the number of connected components.
4. Cut Edge (Bridge): An edge whose removal increases the number of connected components.
5. Vertex Connectivity : The minimum number of vertices whose removal disconnects or reduces it to a
trivial graph. A graph is -connected if .
6. Edge Connectivity : The minimum number of edges whose removal disconnects . A graph is -edge-
connected if .
7. Relationship: For any graph , , where is the minimum degree of .
8. Menger's Theorem: For any two non-adjacent vertices and in a graph , the maximum number of vertex-
disjoint paths between and is equal to the minimum number of vertices whose removal separates and .
(Similar theorem for edge-disjoint paths and edge cuts).
Key Properties and Identities:
A tree with more than one vertex has and .
A complete graph has and .
If a graph has a bridge, its edge connectivity is 1. If it has an articulation point, its vertex connectivity is 1 (unless
it's ).
Common Pitfalls or Tricky Points:
Trivial Graph: For a complete graph , removing vertices disconnects it into a trivial graph (single
vertex), so .
Distinguishing Vertex vs. Edge Connectivity: Carefully read whether the question asks for vertex or edge
removal.
Disconnected Graphs: For a disconnected graph, and .
Standard Problem-Solving Techniques or Shortcuts:
BFS/DFS: Can be used to find connected components, bridges, and articulation points.
Trial and Error: For small graphs, try removing vertices/edges to find the minimum set that disconnects the
graph.
Apply : This inequality provides quick bounds.
Graph Isomorphism

*(PDF Page 35)*

Graph isomorphism determines if two graphs are structurally identical, regardless of their vertex labeling or drawing
style. It's a fundamental concept for comparing graphs.
Definition and Core Idea: Two graphs and are isomorphic if there exists a bijective
function such that for any pair of vertices , if and only if .
Essentially, they have the same structure.
Important Properties (Invariants):
1. Number of Vertices: .
2. Number of Edges: .
3. Degree Sequence: Both graphs must have the same degree sequence (multiset of degrees).
4. Number of Connected Components: Must be the same.
5. Cycle Lengths: The number of cycles of each specific length must be the same.
6. Connectivity: Same vertex and edge connectivity.
7. Chromatic Number: Must be the same.
8. Presence of Subgraphs: If contains a subgraph , then must also contain .
Key Properties and Identities:
If any of the invariants differ, the graphs are definitely NOT isomorphic.
If all invariants are the same, the graphs MIGHT be isomorphic, but it's not a guarantee (e.g., regular graphs can
have the same degree sequence but be non-isomorphic).
The Graph Isomorphism Problem (determining if two graphs are isomorphic) is in NP, but its exact complexity
class is unknown (neither P nor NP-complete is proven). For GATE, problems are usually small enough to solve
by inspection or invariant checking.
Common Pitfalls or Tricky Points:
Proving Non-Isomorphism: This is generally easier; just find one invariant that differs.
Proving Isomorphism: This requires finding an explicit bijective mapping , which can be challenging. Often, it
involves matching vertices with identical properties (e.g., same degree, same neighborhood structure).
Visual Deception: Graphs drawn differently can be isomorphic, and graphs drawn similarly can be non-
isomorphic.
Standard Problem-Solving Techniques or Shortcuts:
Check Invariants Systematically: Start with simple invariants like number of vertices, edges, and degree
sequence. If any differ, stop.
Match Vertices by Properties: Look for unique vertices (e.g., a vertex with degree 1, or a vertex part of a
unique cycle structure) and try to map them.
Adjacency Matrix Comparison: If two graphs are isomorphic, their adjacency matrices can be made identical
by permuting rows and columns. This is computationally intensive for humans but conceptually useful.
Graph Matching
Graph matching is about finding a set of edges that do not share any common vertices, often used in assignment
problems or resource allocation.
Definition and Core Idea: A matching in a graph is a set of edges such that no two edges in common vertex. A vertex is matched (or covered) if it is an endpoint of an edge in share a
; otherwise, it is unmatched.
Important Formulas, Theorems, and Results:
1. Maximum Matching: A matching with the largest possible number of edges.
2. Perfect Matching: A matching that covers all vertices of the graph. A perfect matching can only exist if is
even.
3. Augmenting Path: A path that starts and ends at unmatched vertices, and whose edges alternate between
being in the current matching and not in the current matching. An augmenting path can be used to increase the
size of a matching.
4. Hall's Marriage Theorem (for Bipartite Graphs): A bipartite graph covers all vertices in if and only if for every subset , , where has a matching that
is the set of
neighbors of vertices in .
5. Tutte's Theorem (for General Graphs): A graph , the number of odd components in has a perfect matching if and only if for every subset
is less than or equal to . (This is more complex and less
common in GATE than Hall's).
Key Properties and Identities:
The size of a maximum matching in a bipartite graph can be found using network flow algorithms (e.g., by
converting to a max-flow problem).
Every perfect matching is a maximum matching, but not vice-versa.
A graph can have multiple maximum matchings.

*(PDF Page 36)*

Common Pitfalls or Tricky Points:
Confusing Matching with Vertex Cover or Edge Cover: These are related but distinct concepts. A vertex
cover is a set of vertices that touch all edges. An edge cover is a set of edges that touch all vertices (only exists
if no isolated vertices).
General vs. Bipartite Graphs: Finding maximum matchings in general graphs is more complex (e.g., Edmonds'
blossom algorithm) than in bipartite graphs. GATE usually focuses on bipartite matching or simpler cases.
Existence of Perfect Matching: A perfect matching requires an even number of vertices.
Standard Problem-Solving Techniques or Shortcuts:
Greedy Approach: While not always optimal for maximum matching, a greedy approach (e.g., pick an edge,
remove its endpoints, repeat) can give a good starting point.
Augmenting Paths: For bipartite graphs, the concept of augmenting paths is key. Start with an empty matching,
find an augmenting path, update the matching, and repeat until no more augmenting paths exist. This is the
basis of the Hopcroft-Karp algorithm.
Applying Hall's Theorem: For bipartite graphs, use Hall's condition to check for the existence of a matching
covering one side.
Graph Planarity
Graph planarity deals with whether a graph can be drawn on a plane without any edges crossing. It has applications in
circuit design and network visualization.
Definition and Core Idea: A graph is planar if it can be drawn in the plane without any edges crossing each other
(except at vertices). Such a drawing is called a planar embedding.
Important Formulas, Theorems, and Results:
1. Euler's Formula for Planar Graphs: For any connected planar graph with vertices, edges, and faces
(regions),
This formula is fundamental for planar graphs.
2. Corollaries of Euler's Formula (for simple connected planar graphs with ):
If has no cycles of length 3 (i.e., no subgraph), then .
In general, .
There is at least one vertex with degree at most 5 ( ).
3. Kuratowski's Theorem: A graph is planar if and only if it does not contain a subgraph that is a subdivision of
(complete graph on 5 vertices) or (complete bipartite graph with 3 vertices in each partition).
A subdivision of a graph is obtained by replacing edges with paths.
Key Properties and Identities:
and are non-planar.
Any graph that contains or as a minor (or subdivision) is non-planar.
The dual of a planar graph is also planar.
Common Pitfalls or Tricky Points:
Misapplying Euler's Formula: Remember it's for connected planar graphs. For disconnected graphs,
, where is the number of connected components.
Identifying Subdivisions: Recognizing or subdivisions can be tricky. Look for 5 vertices all connected
to each other (possibly via paths) or 6 vertices arranged in a bipartite manner.
Different Drawings: A graph might look non-planar in one drawing but be planar in another. The definition
requires existence of a planar drawing.
Standard Problem-Solving Techniques or Shortcuts:
Check Euler's Formula Corollaries: If (or if no triangles), the graph is definitely
non-planar. This is a quick check for non-planarity.
Look for or Subdivisions: Try to simplify the graph by removing degree-2 vertices (which don't affect
planarity for Kuratowski's theorem) or identifying dense subgraphs.
Redrawing: For small graphs, try to redraw them to eliminate crossings.
Jaccard Coefficient
The Jaccard Coefficient is a statistical measure used to gauge the similarity between two sets, finding applications in
data mining, machine learning, and graph analysis (e.g., comparing neighbor sets).
Definition and Core Idea: The Jaccard Coefficient (or Jaccard Index) measures the similarity between two finite

*(PDF Page 37)*

sets, and the sets.
Important Formulas, Theorems, and Results:
1. Jaccard Coefficient :
, as the size of their intersection divided by the size of their union. It quantifies the overlap between
2. Jaccard Distance : Measures dissimilarity.
Key Properties and Identities:
The Jaccard Coefficient ranges from 0 to 1.
if (perfect similarity).
if (no similarity).
It is symmetric: .
It is sensitive to the size of the union; a large union with a small intersection leads to a low coefficient.
Common Pitfalls or Tricky Points:
Miscalculating Intersection or Union: Ensure correct set operations, especially when dealing with lists that
might contain duplicates (convert to sets first).
Empty Sets: If both sets are empty, the Jaccard coefficient is usually defined as 1 (perfect similarity). If one is
empty and the other is not, it's 0.
Application Context: In graph theory, it's often used to compare the neighborhood sets of two vertices to
determine their "structural similarity" or to compare sets of features associated with graph nodes.
Standard Problem-Solving Techniques or Shortcuts:
Direct Calculation: Identify the elements in the intersection and union, then apply the formula.
Venn Diagrams: For small sets, a Venn diagram can help visualize the intersection and union.
Quick Formula Reference
Counting Simple Labeled Graphs ( vertices):
Counting Simple Directed Labeled Graphs ( vertices):
Cayley's Formula (Spanning Trees in ):
Handshaking Lemma (Undirected):
Handshaking Lemma (Directed):
BFS/DFS Time Complexity: (adj list), (adj matrix)
Dijkstra's Time Complexity: (binary heap), (adj matrix)
Prim's/Kruskal's Time Complexity (MST): or
Bellman-Ford Time Complexity:
Floyd-Warshall Time Complexity:
Topological Sort Time Complexity:
Chromatic Number Lower Bound: (clique number)
Chromatic Number Upper Bound (Brooks' Theorem): connected graphs), else
Bipartite Graph Chromatic Number: (if connected and has edges)
Planar Graph Chromatic Number (Four Color Theorem):
Connectivity Relationship:
Euler's Formula (Connected Planar Graph):
Planarity Condition (Simple Connected Planar, ):
Planarity Condition (Simple Connected Planar, no , ):
Kuratowski's Theorem: Planar iff no or subdivision
Jaccard Coefficient:
Jaccard Distance:
Important Tips for GATE
(for non-complete, non-odd cycle

*(PDF Page 38)*

1. Master Definitions and Basic Properties: Many GATE questions test fundamental definitions (e.g., what is a
bridge, what is a perfect matching) and direct consequences of theorems. Ensure you know what each term means
precisely.
2. Practice Drawing and Visualizing Graphs: For problems involving planarity, isomorphism, or connectivity,
sketching the graph and trying different layouts can be immensely helpful. Don't rely solely on abstract
representations.
3. Understand Algorithm Mechanics and Complexity: Don't just memorize complexities; understand how BFS,
DFS, Dijkstra's, Prim's, and Kruskal's work step-by-step. Be prepared to trace them on small examples and identify
their time/space complexities for both adjacency list and matrix representations.
4. Pay Attention to Graph Types and Constraints: Is the graph directed or undirected? Weighted or unweighted?
Simple or multi-graph? Does it allow self-loops? These details significantly impact which formulas or algorithms
apply. For example, Dijkstra's fails with negative edge weights.
5. Use Invariants for Isomorphism: When checking for isomorphism, systematically compare invariants like number
of vertices, edges, degree sequence, and cycle lengths. If any invariant differs, the graphs are not isomorphic. This
is a powerful shortcut.
6. Be Wary of Common Pitfalls: Remember that Euler's formula applies to connected planar graphs. Dijkstra's
doesn't work with negative weights. A greedy coloring isn't always optimal. Keep these exceptions in mind.
7. Time Management for Tracing Problems: For algorithm tracing questions, work carefully and systematically. Use
scratch paper to keep track of visited nodes, distances, or parent pointers. Avoid rushing, as a single error can
invalidate the entire trace.
8. Review Special Graph Types: Be familiar with properties of common graphs like complete graphs ( ), complete
bipartite graphs ( ), cycle graphs ( ), path graphs ( ), and trees. Their specific properties often appear in
questions.

---

## 4. Complete Question Index & Answer Key Record (88 Questions)

| Q # | Question Source / Title | Answer Key |
| :---: | :--- | :---: |
| `2.1.1` | Counting: GATE CSE 2001 \| Question: 2.15 | **D** |
| `2.1.2` | Counting: GATE CSE 2004 \| Question: 79 | **D** |
| `2.1.3` | Counting: GATE CSE 2012 \| Question: 38 | **X** |
| `2.2.1` | Degree of Graph: GATE CSE 1987 \| Question: 9c | **N/A** |
| `2.2.2` | Degree of Graph: GATE CSE 1991 \| Question: 16-b | **N/A** |
| `2.2.3` | Degree of Graph: GATE CSE 1995 \| Question: 24 | **N/A** |
| `2.2.4` | Degree of Graph: GATE CSE 2003 \| Question: 40 | **D** |
| `2.2.5` | Degree of Graph: GATE CSE 2006 \| Question: 71 | **C** |
| `2.2.6` | Degree of Graph: GATE CSE 2006 \| Question: 72 | **C** |
| `2.2.7` | Degree of Graph: GATE CSE 2009 \| Question: 3 | **B** |
| `2.2.8` | Degree of Graph: GATE CSE 2010 \| Question: 1 | **C** |
| `2.2.9` | Degree of Graph: GATE CSE 2010 \| Question: 28 | **D** |
| `2.2.10` | Degree of Graph: GATE CSE 2013 \| Question: 25 | **C** |
| `2.2.11` | Degree of Graph: GATE CSE 2014 \| Set 1 \| Question: 52 | **C** |
| `2.2.12` | Degree of Graph: GATE CSE 2017 \| Set 2 \| Question: 23 | **16** |
| `2.2.13` | Degree of Graph: GATE CSE 2026 \| Set 1 \| Question: 37 | **A** |
| `2.3.1` | Graph Algorithms: GATE CSE 2026 \| Set 1 \| Question: 45 | **B;C** |
| `2.4.1` | Graph Coloring: GATE CSE 2002 \| Question: 1.4 | **D** |
| `2.4.2` | Graph Coloring: GATE CSE 2004 \| Question: 77 | **C** |
| `2.4.3` | Graph Coloring: GATE CSE 2009 \| Question: 2 | **A** |
| `2.4.4` | Graph Coloring: GATE CSE 2016 \| Set 2 \| Question: 03 | **4** |
| `2.4.5` | Graph Coloring: GATE CSE 2018 \| Question: 18 | **3** |
| `2.4.6` | Graph Coloring: GATE CSE 2020 \| Question: 52 | **7** |
| `2.4.7` | Graph Coloring: GATE CSE 2023 \| Question: 45 | **A;B** |
| `2.4.8` | Graph Coloring: GATE CSE 2024 \| Set 1 \| Question: 41 | **B;C** |
| `2.4.9` | Graph Coloring: GATE CSE 2024 \| Set 2 \| Question: 50 | **2** |
| `2.4.10` | Graph Coloring: GATE IT 2006 \| Question: 25 | **C** |
| `2.4.11` | Graph Coloring: GATE IT 2008 \| Question: 3 | **B** |
| `2.5.1` | Graph Connectivity: GATE CSE 1987 \| Question: 9d | **N/A** |
| `2.5.2` | Graph Connectivity: GATE CSE 1988 \| Question: 2xvi | **N/A** |
| `2.5.3` | Graph Connectivity: GATE CSE 1990 \| Question: 1-viii | **N/A** |
| `2.5.4` | Graph Connectivity: GATE CSE 1991 \| Question: 01,xv | **N/A** |
| `2.5.5` | Graph Connectivity: GATE CSE 1992 \| Question: 03,iii | **N/A** |
| `2.5.6` | Graph Connectivity: GATE CSE 1993 \| Question: 8.1 | **C;D** |
| `2.5.7` | Graph Connectivity: GATE CSE 1994 \| Question: 1.6, ISRO2008-29 | **C** |
| `2.5.8` | Graph Connectivity: GATE CSE 1994 \| Question: 2.5 | **N/A** |
| `2.5.9` | Graph Connectivity: GATE CSE 1994 \| Question: 24 | **N/A** |
| `2.5.10` | Graph Connectivity: GATE CSE 1995 \| Question: 1.25 | **B** |
| `2.5.11` | Graph Connectivity: GATE CSE 1999 \| Question: 1.15 | **D** |
| `2.5.12` | Graph Connectivity: GATE CSE 1999 \| Question: 5 | **N/A** |
| `2.5.13` | Graph Connectivity: GATE CSE 2002 \| Question: 1.25, ISRO2008-30, ISRO2016-6 | **B** |
| `2.5.14` | Graph Connectivity: GATE CSE 2003 \| Question: 8, ISRO2009-53 | **C** |
| `2.5.15` | Graph Connectivity: GATE CSE 2004 \| Question: 81 | **B** |
| `2.5.16` | Graph Connectivity: GATE CSE 2005 \| Question: 11 | **A** |
| `2.5.17` | Graph Connectivity: GATE CSE 2006 \| Question: 73 | **B** |
| `2.5.18` | Graph Connectivity: GATE CSE 2007 \| Question: 23 | **C** |
| `2.5.19` | Graph Connectivity: GATE CSE 2008 \| Question: 42 | **D** |
| `2.5.20` | Graph Connectivity: GATE CSE 2013 \| Question: 26 | **A** |
| `2.5.21` | Graph Connectivity: GATE CSE 2014 \| Set 1 \| Question: 51 | **506** |
| `2.5.22` | Graph Connectivity: GATE CSE 2014 \| Set 2 \| Question: 3 | **36** |
| `2.5.23` | Graph Connectivity: GATE CSE 2014 \| Set 3 \| Question: 51 | **C** |
| `2.5.24` | Graph Connectivity: GATE CSE 2015 \| Set 2 \| Question: 50 | **B** |
| `2.5.25` | Graph Connectivity: GATE CSE 2019 \| Question: 12 | **C;D** |
| `2.5.26` | Graph Connectivity: GATE CSE 2019 \| Question: 38 | **C** |
| `2.5.27` | Graph Connectivity: GATE CSE 2021 \| Set 1 \| Question: 36 | **A** |
| `2.5.28` | Graph Connectivity: GATE CSE 2022 \| Question: 20 | **36** |
| `2.5.29` | Graph Connectivity: GATE CSE 2022 \| Question: 27 | **D** |
| `2.5.30` | Graph Connectivity: GATE CSE 2022 \| Question: 42 | **A** |
| `2.5.31` | Graph Connectivity: GATE CSE 2024 \| Set 1 \| Question: 24 | **16** |
| `2.5.32` | Graph Connectivity: GATE CSE 2024 \| Set 2 \| Question: 41 | **D** |
| `2.5.33` | Graph Connectivity: GATE CSE 2024 \| Set 2 \| Question: 7 | **B** |
| `2.5.34` | Graph Connectivity: GATE IT 2004 \| Question: 37 | **D** |
| `2.5.35` | Graph Connectivity: GATE IT 2004 \| Question: 5 | **A** |
| `2.5.36` | Graph Connectivity: GATE IT 2005 \| Question: 56 | **B** |
| `2.5.37` | Graph Connectivity: GATE IT 2006 \| Question: 11 | **D** |
| `2.5.38` | Graph Connectivity: GATE IT 2007 \| Question: 25 | **C** |
| `2.5.39` | Graph Connectivity: GATE IT 2008 \| Question: 27 | **D** |
| `2.5.40` | Graph Connectivity: GATE IT 2008 \| Question: 4 | **C** |
| `2.6.1` | edges contains | **B** |
| `2.6.2` | Graph Isomorphism: GATE CSE 2014 \| Set 2 \| Question: 51 | **5** |
| `2.6.3` | Graph Isomorphism: GATE CSE 2015 \| Set 2 \| Question: 28 | **D** |
| `2.6.4` | Graph Isomorphism: GATE CSE 2022 \| Question: 40 | **A;B;C** |
| `2.7.1` | Graph Matching: GATE CSE 2003 \| Question: 36 | **A** |
| `2.7.2` | Graph Matching: GATE CSE 2026 \| Set 1 \| Question: 47 | **34** |
| `2.8.1` | Graph Planarity: GATE CSE 1987 \| Question: 2e | **TBA** |
| `2.8.2` | Graph Planarity: GATE CSE 1989 \| Question: 3-vi | **N/A** |
| `2.8.3` | Graph Planarity: GATE CSE 1990 \| Question: 3-xi | **D** |
| `2.8.4` | Graph Planarity: GATE CSE 1992 \| Question: 01,x | **N/A** |
| `2.8.5` | Graph Planarity: GATE CSE 1992 \| Question: 02,viii | **C** |
| `2.8.6` | Graph Planarity: GATE CSE 2005 \| Question: 10 | **B** |
| `2.8.7` | Graph Planarity: GATE CSE 2005 \| Question: 47 | **A** |
| `2.8.8` | Graph Planarity: GATE CSE 2008 \| Question: 23 | **C** |
| `2.8.9` | Graph Planarity: GATE CSE 2011 \| Question: 17 | **B** |
| `2.8.10` | Graph Planarity: GATE CSE 2012 \| Question: 17 | **D** |
| `2.8.11` | Graph Planarity: GATE CSE 2014 \| Set 3 \| Question: 52 | **A** |
| `2.8.12` | Graph Planarity: GATE CSE 2015 \| Set 1 \| Question: 54 | **24** |
| `2.8.13` | Graph Planarity: GATE CSE 2021 \| Set 1 \| Question: 16 | **11** |
| `2.9.1` | Jaccard Coefficient: GATE CSE 2026 \| Set 2 \| Question: 26 | **C** |

