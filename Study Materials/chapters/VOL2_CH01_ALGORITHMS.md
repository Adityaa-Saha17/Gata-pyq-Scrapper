# Volume 2 — Chapter 1: Algorithms

- **Source PDF**: [filter1_volume2.pdf](file:///Users/adityaasaha/Documents/Academics/Gate/filter1_volume2.pdf)
- **Total GATE Questions in Chapter**: **358**

---

## 1. Subtopic Weightage & Question Distribution

| Subtopic # | Subtopic Name | Questions |
| :---: | :--- | :---: |
| **1.1** | Algorithm Design | 8 |
| **1.2** | Algorithm Design Techniques | 9 |
| **1.3** | Asymptotic Notations | 22 |
| **1.4** | Bellman Ford | 2 |
| **1.5** | Binary Heap | 1 |
| **1.6** | Binary Search | 4 |
| **1.7** | Binary Search Tree | 3 |
| **1.8** | Binary Tree | 1 |
| **1.9** | Breadth First Search | 3 |
| **1.11** | Computer Science | 1 |
| **1.12** | Depth First Search | 2 |
| **1.13** | Dijkstras Algorithm | 5 |
| **1.14** | Directed Acyclic Graph | 2 |
| **1.15** | Double Hashing | 2 |
| **1.16** | Dynamic Programming | 10 |
| **1.17** | Graph Algorithms | 11 |
| **1.19** | Greedy Algorithms | 5 |
| **1.20** | Hashing | 6 |
| **1.21** | Heap Sort | 2 |
| **1.22** | Huffman Code | 6 |
| **1.23** | Identify Function | 38 |
| **1.24** | Insertion Sort | 2 |
| **1.25** | Inversion | 2 |
| **1.26** | Linear Probing | 2 |
| **1.27** | Matrix Chain Ordering | 3 |
| **1.28** | Maximum Minimum | 1 |
| **1.29** | Merge Sort | 4 |
| **1.30** | Merging | 2 |
| **1.31** | Minimum Spanning Tree | 35 |
| **1.34** | Quick Sort | 15 |
| **1.35** | Recurrence Relation | 36 |
| **1.39** | Shortest Path | 8 |
| **1.40** | Sorting | 22 |
| **1.41** | Space Complexity | 1 |
| **1.42** | Strongly Connected Components | 3 |
| **1.43** | Time Complexity | 31 |
| **1.44** | Topological Sort | 4 |
| **1.45** | Tree Traversal | 1 |
| **1.46** | Uniform Hashing | 1 |


---

## 2. Comprehensive GATE CSE Algorithms Reference (Expanded Research & Formulas)

### 2.1 Asymptotic Notations & Growth Order
- **Definitions**:
  - $f(n) = O(g(n))$ iff $\exists c > 0, n_0 > 0$ s.t. $0 \le f(n) \le c \cdot g(n)$ for all $n \ge n_0$ (Upper bound).
  - $f(n) = \Omega(g(n))$ iff $\exists c > 0, n_0 > 0$ s.t. $0 \le c \cdot g(n) \le f(n)$ for all $n \ge n_0$ (Lower bound).
  - $f(n) = \Theta(g(n))$ iff $f(n) = O(g(n))$ and $f(n) = \Omega(g(n))$ (Tight bound).
  - $f(n) = o(g(n))$ iff $\lim_{n \to \infty} \frac{f(n)}{g(n)} = 0$; $\quad f(n) = \omega(g(n))$ iff $\lim_{n \to \infty} \frac{f(n)}{g(n)} = \infty$.
- **Strict Asymptotic Hierarchy ($n \to \infty$)**:
  $$1 \ll \log(\log n) \ll \log n \ll (\log n)^k \ll n^\epsilon \ll n \ll n \log n \ll n^2 \ll n^k \ll c^n \ll n! \ll n^n \ll 2^{2^n}$$
- **Stirling's Approximation & Log Identities**:
  - $\log(n!) = \Theta(n \log n)$, $\quad n! \approx \sqrt{2\pi n}\left(\frac{n}{e}\right)^n$.
  - $a^{\log_b n} = n^{\log_b a}$.
  - Harmonic Series: $H_n = \sum_{k=1}^{n} \frac{1}{k} = \Theta(\log n)$.

### 2.2 Master Theorem & Akra-Bazzi / Subtraction Recurrences
- **Master Theorem** for $T(n) = a T(n/b) + f(n)$ ($a \ge 1, b > 1$) with critical exponent $c_{\text{crit}} = \log_b a$:
  1. **Case 1 (Leaves Dominate)**: If $f(n) = O(n^{\log_b a - \epsilon})$ for some $\epsilon > 0 \implies T(n) = \Theta(n^{\log_b a})$.
  2. **Case 2 (Extended — Equal Work per Level)**:
     - If $f(n) = \Theta(n^{\log_b a} \log^k n)$ with $k \ge 0 \implies T(n) = \Theta(n^{\log_b a} \log^{k+1} n)$.
     - If $k = -1$ ($f(n) = \Theta(n^{\log_b a} / \log n)$) $\implies T(n) = \Theta(n^{\log_b a} \log \log n)$.
     - If $k < -1 \implies T(n) = \Theta(n^{\log_b a})$.
  3. **Case 3 (Root Dominates)**: If $f(n) = \Omega(n^{\log_b a + \epsilon})$ for some $\epsilon > 0$ and $a f(n/b) \le c f(n)$ for $c < 1 \implies T(n) = \Theta(f(n))$.
- **Decrease-and-Conquer Recurrences**:
  - $T(n) = T(n - k) + \Theta(n^d) \implies T(n) = \Theta(n^{d+1})$.
  - $T(n) = a T(n - b) + \Theta(n^d)$ ($a > 1$) $\implies T(n) = \Theta(a^{n/b})$.
  - $T(n) = T(\sqrt{n}) + 1$ (substitute $n = 2^m$) $\implies T(n) = \Theta(\log \log n)$.
  - $T(n) = 2T(\sqrt{n}) + \log n \implies T(n) = \Theta(\log n \log \log n)$.

### 2.3 Sorting & Searching Master Comparison Table
| Algorithm | Best Time | Average Time | Worst Time | Extra Space | Stable? | In-Place? | Key GATE Notes |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Insertion Sort** | $\Theta(n)$ | $\Theta(n^2)$ | $\Theta(n^2)$ | $O(1)$ | Yes | Yes | $\Theta(n + I)$ where $I =$ number of inversions |
| **Selection Sort** | $\Theta(n^2)$ | $\Theta(n^2)$ | $\Theta(n^2)$ | $O(1)$ | No | Yes | Minimum swaps: at most $n-1$ swaps in worst case |
| **Bubble Sort (Opt.)** | $\Theta(n)$ | $\Theta(n^2)$ | $\Theta(n^2)$ | $O(1)$ | Yes | Yes | Swaps = exact number of inversions $I$ |
| **Merge Sort** | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(n)$ | Yes | No | Max comparisons to merge $m$ & $n$: $m + n - 1$; min: $\min(m, n)$ |
| **Heap Sort** | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $O(1)$ | No | Yes | Build-Heap is $\Theta(n)$ ($< 2n$ comparisons) |
| **Quick Sort** | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(n^2)$ | $O(\log n)$–$O(n)$ | No | Yes | Worst case on sorted/reverse-sorted or all-equal (Lomuto) |
| **Counting / Radix** | $\Theta(n+k)$ | $\Theta(n+k)$ | $\Theta(n+k)$ | $\Theta(n+k)$ | Yes | No | Non-comparison sort; lower bound $\Omega(n \log n)$ doesn't apply |

- **Inversions in an Array**: Pair $(i, j)$ with $i < j$ and $A[i] > A[j]$. Max inversions $= \binom{n}{2}$; expected inversions in random array $= \frac{n(n-1)}{4}$.
- **Simultaneous Min & Max of $n$ Elements**: Tournament / Pairwise comparison takes $\frac{3n}{2} - 2$ comparisons (for even $n$), instead of $2n - 3$.

### 2.4 Greedy vs Dynamic Programming & Graph Algorithms
- **Greedy Algorithms**:
  - **Fractional Knapsack**: Sort by $v_i / w_i$; $O(n \log n)$.
  - **Huffman Coding**: Optimal prefix-free code; $O(n \log n)$ using Min-Heap; total weighted path length $= \sum f_i d_i$ = sum of all internal node values.
  - **Minimum Spanning Tree (MST)** (Undirected connected weighted graph):
    - **Cut Property**: Unique lightest edge crossing any cut belongs to **every** MST.
    - **Cycle Property**: Unique heaviest edge in any cycle belongs to **no** MST.
    -If all edge weights are **distinct**, the MST is **unique**.
    - **Kruskal's**: $O(E \log E) = O(E \log V)$ using Disjoint-Set Union-Find.
    - **Prim's**: $O(V^2)$ (Adjacency Matrix / Array), $O((V + E) \log V)$ (Binary Heap), $O(E + V \log V)$ (Fibonacci Heap).
- **Shortest Path Algorithms**:
  - **BFS** (Unweighted): $O(V + E)$.
  - **DAG Shortest/Longest Path** (Topological Sort + Relax): $\Theta(V + E)$ (works even with negative weights!).
  - **Dijkstra's** (Non-negative edge weights only!): $O((V + E) \log V)$ (Binary Heap), $O(E + V \log V)$ (Fibonacci Heap). *Fails on negative edges!*
  - **Bellman-Ford** (Handles negative weights & detects reachable negative cycles): $O(VE)$ ($V-1$ relaxation passes + 1 check pass).
  - **Floyd-Warshall** (All-Pairs Shortest Path): $\Theta(V^3)$ time, $\Theta(V^2)$ space.
- **Dynamic Programming Complexities**:
  - **0/1 Knapsack**: $\Theta(nW)$ (pseudo-polynomial).
  - **Matrix Chain Multiplication (MCM)**: $\Theta(n^3)$ time, $\Theta(n^2)$ space ($C_{n-1}$ parenthesizations).
  - **Longest Common Subsequence (LCS)**: $\Theta(mn)$ time, $\Theta(\min(m,n))$ space.
  - **Optimal Binary Search Tree (OBST)**: $\Theta(n^3)$ (or $\Theta(n^2)$ via Knuth optimization).
- **BFS / DFS Edge Classification ($O(V + E)$ list, $O(V^2)$ matrix)**:
  - **Undirected DFS**: Only **Tree edges** and **Back edges** (no forward/cross edges). Cycle exists iff a **Back edge** exists.
  - **Directed DFS**: Tree, Back, Forward, Cross edges. Cycle exists iff a **Back edge** exists (where $u$ is ancestor of $v$: $d[u] < d[v] < f[v] < f[u]$).

---

## 3. Original PDF Chapter Notes (Preserved Verbatim)

1 Algorithms (358)
Searching, Sorting, Hashing, Asymptotic worst case time and Space complexity, Algorithm design
techniques: Greedy, Dynamic programming, and Divide‐and‐conquer, Graph search, Minimum spanning
trees, Shortest paths.
Welcome to the "Algorithms" chapter, a cornerstone of Computer Science and a high-scoring section in the GATE
examination. This subject delves into the systematic procedures and computational methods used to solve problems,
focusing on their efficiency and correctness. Mastering algorithms is crucial not only for theoretical understanding but
also for practical application in software development and system design. In GATE CS, algorithms typically carry a
significant weightage, often ranging from 10 to 15 marks, with questions spanning theoretical concepts, time and space
complexity analysis, problem-solving, and application of various design techniques. Expect a mix of Multiple Choice
Questions (MCQ), Multiple Select Questions (MSQ), and Numerical Answer Type (NAT) questions, requiring a deep
understanding of underlying principles and the ability to analyze and compare different algorithmic approaches.
Topic-wise Key Concepts
Algorithm Design
Definition: Algorithm design is the process of creating a well-defined computational procedure to solve a specific
problem. It involves understanding the problem, choosing appropriate data structures, and devising a step-by-step
method that is correct, efficient, and terminates.
Properties/Identities:
Correctness: An algorithm must produce the correct output for all valid inputs.
Efficiency: Measured by time and space complexity.
Finiteness: Must terminate after a finite number of steps.
Definiteness: Each step must be precisely defined.
Input/Output: Must take zero or more inputs and produce one or more outputs.
Pitfalls/Tricks:
Overlooking edge cases or constraints that might break the algorithm's logic.
Designing an algorithm that is correct but too inefficient for practical use or given constraints.
Techniques/Shortcuts:
Start with a brute-force solution, then optimize.
Break down complex problems into smaller, manageable subproblems.
Consider different data structures and their impact on performance.
Algorithm Design Techniques
Definition: These are general strategies or paradigms used to develop algorithms for a wide range of problems. Key
techniques include Divide and Conquer, Greedy Algorithms, Dynamic Programming, Backtracking, and Branch and
Bound.
Properties/Identities:
Divide and Conquer: Divide problem into subproblems, solve recursively, combine solutions.
Greedy Algorithms: Make locally optimal choices at each step, hoping to find a global optimum.
Dynamic Programming: Solves problems with overlapping subproblems and optimal substructure by storing
results of subproblems.
Pitfalls/Tricks:
Mistaking a problem for one solvable by a greedy approach when it requires dynamic programming.
Incorrectly identifying optimal substructure or overlapping subproblems.
Techniques/Shortcuts:
For DP, identify the state, recurrence relation, and base cases.
For Greedy, prove the greedy choice property and optimal substructure.
Asymptotic Notations

*(PDF Page 8)*

Definition: Mathematical notations used to describe the limiting behavior of a function when the argument tends
towards a particular value or infinity, primarily used to classify algorithms by their running time or space requirements as
input size grows.
Formulas/Theorems:
Big-O Notation (Upper Bound): for all .
Omega Notation (Lower Bound): for all .
Theta Notation (Tight Bound): if there exist positive constants and such that
if there exist positive constants and such that
if there exist positive constants and such that
for all .
Little-o Notation (Strict Upper Bound): if .
Little-omega Notation (Strict Lower Bound): if .
Properties/Identities:
Reflexivity: , , .
Transitivity: If and , then . (Applies to all notations).
Symmetry: iff .
Transpose Symmetry: iff . Similarly for and .
Sum Rule: If and , then . (Take the maximum order
term).
Product Rule: If and , then .
Pitfalls/Tricks:
Confusing Big-O with Theta: Big-O is an upper bound, Theta is a tight bound.
Ignoring constants and lower-order terms: Asymptotic notation focuses on growth rate.
Assuming means exactly operations; it means "at most proportional to "
.
Techniques/Shortcuts:
For polynomials, the highest degree term dominates. E.g., .
Logarithms grow slower than any polynomial: for any .
Exponentials grow faster than any polynomial: for any .
Bellman Ford
Definition: A single-source shortest path algorithm that can handle graphs with negative edge weights. It works by
repeatedly relaxing all edges in the graph, detecting negative cycles if they exist.
Formulas/Theorems:
Relaxation Step: For an edge with weight , if , then .
Number of Iterations: iterations are sufficient to find shortest paths in a graph with vertices,
assuming no negative cycles reachable from the source.
Negative Cycle Detection: After iterations, if any edge can still be relaxed in the -th iteration, a
negative cycle exists.
Properties/Identities:
Works on directed and undirected graphs (undirected edges treated as two directed edges).
Can detect negative cycles.
Time Complexity: .
Space Complexity: for distance array, for predecessor array.
Pitfalls/Tricks:
Incorrectly assuming it's faster than Dijkstra's for non-negative weights (Dijkstra's is or
).
Forgetting to initialize distances (source to 0, others to infinity).
Techniques/Shortcuts:
Visualize the relaxation process step-by-step.
For negative cycle detection, run one extra iteration after iterations.
Binary Heap
Definition: A complete binary tree that satisfies the heap property: for a min-heap, every node's value is less than or
equal to its children's values; for a max-heap, every node's value is greater than or equal to its children's values.

*(PDF Page 9)*

Typically implemented using an array.
Formulas/Theorems:
Parent of node : (for 0-indexed array).
Left child of node : (for 0-indexed array).
Right child of node : (for 0-indexed array).
Height of a heap with nodes: .
Properties/Identities:
Min-Heap: Root is the minimum element.
Max-Heap: Root is the maximum element.
Complete Binary Tree: All levels are completely filled except possibly the last level, which is filled from left to
right.
Operations Time Complexity:
Insert:
Delete-Min/Max:
Build-Heap (from an array of elements):
Pitfalls/Tricks:
Confusing min-heap with max-heap properties.
Incorrectly calculating parent/child indices, especially for 1-indexed vs. 0-indexed arrays.
Techniques/Shortcuts:
When building a heap, start from the last non-leaf node and call `heapify
`
upwards.
Heap sort uses a max-heap.
Binary Search
Definition: An efficient algorithm for finding an item from a sorted list of items. It repeatedly divides the search interval
in half, eliminating half of the remaining elements at each step.
Formulas/Theorems:
Recurrence Relation: .
Time Complexity: .
Space Complexity: (iterative) or (recursive due to call stack).
Properties/Identities:
Requires the input array/list to be sorted.
Can be used to find the first/last occurrence of an element, or the ceiling/floor.
Pitfalls/Tricks:
Forgetting to handle edge cases like empty arrays or target not found.
Off-by-one errors in index calculations (e.g.,
`
mid = (low + high) / 2`). Use
`
mid = low + (high - low) / 2` to prevent
overflow.
Techniques/Shortcuts:
Always ensure the search space is correctly updated (`low = mid + 1`
or
`high = mid - 1`).
For finding first/last occurrence, adjust the update logic to keep searching in the relevant half even after finding a
match.
Binary Search Tree (BST)
Definition: A binary tree where for each node, all values in its left subtree are less than the node's value, and all values
in its right subtree are greater than the node's value. No duplicate values are typically allowed.
Properties/Identities:
Inorder Traversal: Produces elements in sorted order.
Average Time Complexity:
Search, Insert, Delete:
Worst-Case Time Complexity (skewed tree):
Search, Insert, Delete:
Space Complexity: for storing nodes.
Pitfalls/Tricks:
Forgetting to handle the case of deleting a node with two children (replace with inorder successor/predecessor).
Assuming performance always; a skewed BST degrades to .
Techniques/Shortcuts:
To find minimum, traverse left until null. To find maximum, traverse right until null.

*(PDF Page 10)*

For deletion, the inorder successor is the smallest node in the right subtree.
Binary Tree
Definition: A tree data structure where each node has at most two children, referred to as the left child and the right
child. It's a fundamental non-linear data structure.
Formulas/Theorems:
Maximum nodes at level (root at level 0): .
Maximum nodes in a binary tree of height : .
Minimum height of a binary tree with nodes: .
Properties/Identities:
Full Binary Tree: Every node has either 0 or 2 children.
Complete Binary Tree: All levels are completely filled except possibly the last level, which is filled from left to
right.
Perfect Binary Tree: All internal nodes have two children and all leaves are at the same level. (A perfect binary
tree is always full and complete).
Skewed Binary Tree: All nodes have only one child (either left or right).
Pitfalls/Tricks:
Confusing different types of binary trees (full, complete, perfect).
Incorrectly calculating height or number of nodes for specific tree types.
Techniques/Shortcuts:
Understand the relationship between height and number of nodes for different tree types.
Practice drawing trees from traversals.
Breadth First Search (BFS)
Definition: A graph traversal algorithm that explores all the neighbor nodes at the present depth before moving on to
nodes at the next depth level. It uses a queue data structure.
Properties/Identities:
Finds the shortest path in terms of number of edges (unweighted graphs).
Guaranteed to visit all reachable vertices.
Time Complexity: for adjacency list, for adjacency matrix.
Space Complexity: for queue and visited array.
Pitfalls/Tricks:
Forgetting to mark nodes as visited to prevent cycles and redundant processing.
Using BFS for weighted shortest paths (Dijkstra's is needed).
Techniques/Shortcuts:
Think of BFS as "level-by-level" exploration.
Useful for finding connected components, shortest path in unweighted graphs, and checking bipartiteness.
Bubble Sort
Definition: A simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps
them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates
that the list is sorted.
Formulas/Theorems:
Worst-case Time Complexity: (e.g., reverse sorted array).
Average-case Time Complexity: .
Best-case Time Complexity: (already sorted array, with optimization to stop if no swaps).
Space Complexity: (in-place).
Number of Swaps (Worst Case): .
Number of Comparisons (Worst Case): .
Properties/Identities:
Stable sorting algorithm.
Adaptive (can detect if an array is sorted and stop early).
Pitfalls/Tricks:
Often used as a baseline for comparison due to its simplicity and inefficiency.
Not suitable for large datasets.

*(PDF Page 11)*

Techniques/Shortcuts:
Understand its passes: after passes, the last elements are in their correct sorted positions.
Computer Science
Definition: The study of computation and information, including theoretical foundations, algorithmic design, and
practical implementation. Algorithms are a core theoretical and practical component.
Properties/Identities:
Algorithms are fundamental to all areas of Computer Science.
Depth First Search (DFS)
Definition: A graph traversal algorithm that explores as far as possible along each branch before backtracking. It uses
a stack (explicit or implicit via recursion).
Properties/Identities:
Can be used to find paths between two nodes, detect cycles, find connected components, and perform
topological sorting.
Time Complexity: for adjacency list, for adjacency matrix.
Space Complexity: for recursion stack or explicit stack, and visited array.
Pitfalls/Tricks:
Can lead to very deep recursion for long paths, potentially causing stack overflow.
Does not guarantee shortest paths in unweighted graphs (BFS does).
Techniques/Shortcuts:
Think of DFS as "going deep" before "going wide"
.
Useful for cycle detection, topological sort, and finding strongly connected components.
Dijkstra's Algorithm
Definition: A single-source shortest path algorithm for graphs with non-negative edge weights. It uses a greedy
approach and a priority queue to efficiently find the shortest paths from a source vertex to all other vertices.
Formulas/Theorems:
Relaxation Step: Same as Bellman-Ford.
Time Complexity:
With min-priority queue (binary heap): or With adjacency matrix (no priority queue, simple array scan): .
Space Complexity: for graph, for distances/predecessors.
Properties/Identities:
Does not work correctly with negative edge weights.
Greedy algorithm.
Guaranteed to find the shortest path.
Pitfalls/Tricks:
Applying it to graphs with negative edge weights (use Bellman-Ford instead).
Forgetting to update distances in the priority queue (decrease-key operation).
Techniques/Shortcuts:
Always pick the unvisited vertex with the smallest known distance.
Visualize the "settling" of vertices.
if using Fibonacci heap.
Directed Acyclic Graph (DAG)
Definition: A directed graph that contains no directed cycles. This property makes them useful for representing
processes with dependencies, like task scheduling.
Properties/Identities:
Can always be topologically sorted.
No path can revisit a vertex.
Every finite DAG has at least one source (in-degree 0) and at least one sink (out-degree 0).
Pitfalls/Tricks:
Confusing DAGs with general directed graphs that might have cycles.
Trying to apply algorithms that assume cycles (e.g., finding strongly connected components) without

*(PDF Page 12)*

modification.
Techniques/Shortcuts:
Topological sort is a key algorithm for DAGs.
Dynamic programming problems on graphs often involve DAGs.
Double Hashing
Definition: A collision resolution technique in hashing that uses two hash functions. When a collision occurs with the
first hash function, the second hash function is used to determine the step size for probing the hash table.
Formulas/Theorems:
Primary Hash Function: .
Secondary Hash Function: . must never return 0. Often for a prime
.
Probe Sequence: , where is table size and is probe number (0,
1, 2, ...).
Properties/Identities:
Minimizes clustering compared to linear probing.
Provides better distribution of keys.
Requires to be relatively prime to to ensure all slots are probed.
Pitfalls/Tricks:
Choosing a secondary hash function that can return 0 or is not relatively prime to the table size, leading to
incomplete probing.
Incorrectly implementing the modulo operation for negative results.
Techniques/Shortcuts:
Ensure is a prime number and is a prime smaller than for .
Dynamic Programming
Definition: An algorithmic technique for solving complex problems by breaking them down into simpler subproblems.
It's applicable when subproblems overlap and the problem exhibits optimal substructure. Solutions to subproblems are
stored to avoid recomputation (memoization or tabulation).
Properties/Identities:
Optimal Substructure: An optimal solution to the problem contains optimal solutions to its subproblems.
Overlapping Subproblems: The same subproblems are encountered multiple times.
Memoization (Top-down): Store results of subproblems as they are computed.
Tabulation (Bottom-up): Solve subproblems in a specific order, typically filling a table.
Pitfalls/Tricks:
Incorrectly identifying the state of the DP problem.
Formulating an incorrect recurrence relation.
Forgetting base cases or handling them improperly.
Techniques/Shortcuts:
Define the state: What information is needed to solve a subproblem?
Formulate the recurrence relation: How can a subproblem be solved using solutions to smaller subproblems?
Identify base cases.
Choose between memoization (recursive with caching) and tabulation (iterative).
Graph Algorithms
Definition: A category of algorithms designed to solve problems on graphs, which are mathematical structures used to
model pairwise relations between objects. This includes traversal, shortest path, minimum spanning tree, and
connectivity problems.
Properties/Identities:
Common representations: Adjacency matrix, adjacency list.
Key problems: Shortest Path, MST, Graph Traversal, Connectivity.
Pitfalls/Tricks:
Not considering graph type (directed/undirected, weighted/unweighted, cyclic/acyclic) when choosing an
algorithm.
Memory limitations for dense graphs with adjacency matrices.
Techniques/Shortcuts:

*(PDF Page 13)*

Always consider the graph representation that best suits the problem and its constraints.
Practice drawing graphs and tracing algorithms.
Graph Search
Definition: Algorithms for systematically visiting all vertices and edges in a graph. The two primary methods are
Breadth-First Search (BFS) and Depth-First Search (DFS).
Properties/Identities:
BFS: Level-by-level, uses queue, finds shortest path in unweighted graphs.
DFS: Explores deeply, uses stack/recursion, useful for cycle detection, topological sort, SCC.
Pitfalls/Tricks:
Forgetting to use a 'visited' array/set to prevent infinite loops in cyclic graphs.
Choosing the wrong search algorithm for the problem (e.g., DFS for unweighted shortest path).
Techniques/Shortcuts:
BFS is good for finding "closest" elements.
DFS is good for exploring "all paths" or "connectivity"
.
Greedy Algorithms
Definition: An algorithmic paradigm that makes the locally optimal choice at each stage with the hope of finding a
global optimum. It doesn't always guarantee the globally optimal solution but works for specific problems.
Properties/Identities:
Greedy Choice Property: A globally optimal solution can be reached by making a locally optimal (greedy)
choice.
Optimal Substructure: An optimal solution to the problem contains optimal solutions to its subproblems.
Pitfalls/Tricks:
Applying greedy approach to problems where it doesn't yield an optimal solution (e.g., general shortest path with
negative weights, 0/1 Knapsack).
Not proving the greedy choice property and optimal substructure.
Techniques/Shortcuts:
Common examples: Dijkstra's, Prim's, Kruskal's, Huffman Coding.
Try to prove correctness by contradiction or exchange argument.
Hashing
Definition: A technique used to map data of arbitrary size to fixed-size values (hash codes), typically used for efficient
data retrieval in hash tables. Involves a hash function and collision resolution strategies.
Formulas/Theorems:
Hash Function: (division method), (multiplication method).
Load Factor: , where is number of items, is table size.
Properties/Identities:
Collision: When two different keys map to the same hash value.
Collision Resolution: Open addressing (linear probing, quadratic probing, double hashing) or Separate
chaining.
Average Time Complexity (Search, Insert, Delete): (with good hash function and low load factor).
Worst-case Time Complexity: (due to collisions).
Pitfalls/Tricks:
Choosing a poor hash function that leads to many collisions (e.g., for string keys, summing ASCII values).
Ignoring the impact of load factor on performance.
Techniques/Shortcuts:
For division method, choose as a prime number not too close to a power of 2 or 10.
Understand the trade-offs between different collision resolution techniques.
Heap Sort
Definition: A comparison-based sorting algorithm that uses a binary heap data structure. It's an in-place algorithm that
first builds a max-heap from the input data and then repeatedly extracts the maximum element and rebuilds the heap.
Formulas/Theorems:

*(PDF Page 14)*

Time Complexity: for all cases (best, average, worst).
Space Complexity: (in-place).
Properties/Identities:
Not a stable sorting algorithm.
Uses a max-heap.
Build-heap step takes time.
extractions take time.
Pitfalls/Tricks:
Confusing the heap property (min-heap vs. max-heap) with the sorting order.
Incorrectly implementing the
`heapify
`
procedure.
Techniques/Shortcuts:
Remember the two phases: build heap, then extract max and heapify.
The largest element is always at the root after heapify.
Huffman Code
Definition: A particular type of optimal prefix code used for lossless data compression. It's a greedy algorithm that
builds a binary tree based on the frequencies of characters, assigning shorter codes to more frequent characters.
Properties/Identities:
Prefix Code: No code is a prefix of another code, allowing unambiguous decoding.
Optimal: Produces the minimum possible expected code word length for a given set of character frequencies.
Uses a min-priority queue to repeatedly combine the two lowest-frequency nodes.
Time Complexity: where is the number of unique characters.
Pitfalls/Tricks:
Incorrectly building the Huffman tree (e.g., not using a min-priority queue, or incorrect combination logic).
Forgetting that it's a greedy algorithm.
Techniques/Shortcuts:
Always combine the two nodes with the smallest frequencies.
The path from the root to a leaf defines the code word (e.g., left=0, right=1).
Identify Function
Definition: In a general mathematical or programming context, an identity function (often denoted that always returns the same value that was used as its argument. or ) is a function
. In algorithms, it might refer to a function
used to uniquely identify elements or properties.
Properties/Identities:
For any input , .
It's the neutral element for function composition: and .
Pitfalls/Tricks:
This term is very generic; in an algorithmic context, it's usually implied or part of a larger concept (e.g., an identity
hash function, or an identity matrix).
Insertion Sort
Definition: A simple sorting algorithm that builds the final sorted array (or list) one item at a time. It iterates through the
input elements and removes one element at a time, finds the place where it belongs within the already sorted part, and
inserts it there.
Formulas/Theorems:
Worst-case Time Complexity: (e.g., reverse sorted array).
Average-case Time Complexity: .
Best-case Time Complexity: (already sorted array).
Space Complexity: (in-place).
Number of Swaps (Worst Case): .
Number of Comparisons (Worst Case): .
Properties/Identities:
Stable sorting algorithm.
Adaptive (efficient for nearly sorted arrays).
Good for small datasets.

*(PDF Page 15)*

Pitfalls/Tricks:
Inefficient for large, unsorted arrays.
Understanding the "shift" operation correctly.
Techniques/Shortcuts:
Think of it like sorting a hand of playing cards.
The first element is considered sorted.
Inversion
Definition: In an array "unsorted" an array is.
, an inversion is a pair of indices such that and . It measures how
Formulas/Theorems:
Maximum number of inversions in an array of size : (for a reverse-sorted array).
Minimum number of inversions: 0 (for a sorted array).
Properties/Identities:
The number of inversions can be counted efficiently using a modified Merge Sort algorithm in time.
Pitfalls/Tricks:
Confusing inversions with just any pair of elements that are out of order; the index order is crucial.
Techniques/Shortcuts:
To count inversions, adapt Merge Sort: when merging two sorted halves, if an element from the right half is taken
before an element from the left half, it means all remaining elements in the left half form inversions with the taken
element.
Linear Probing
Definition: A collision resolution technique in open addressing hashing where, upon a collision, the algorithm searches
for the next available slot sequentially in the hash table (e.g., at ).
Formulas/Theorems:
Probe Sequence: , where is table size and is probe number (0, 1, 2, ...).
Properties/Identities:
Simple to implement.
Suffers from primary clustering: long runs of occupied slots build up, increasing average search time.
Pitfalls/Tricks:
Primary clustering significantly degrades performance, especially at high load factors.
Deletion is tricky: simply removing an element can break search chains. Often requires "lazy deletion" or re-
hashing.
Techniques/Shortcuts:
Understand that it's the simplest but often least efficient open addressing method.
Matrix Chain Ordering (Matrix Chain Multiplication)
Definition: A dynamic programming problem that seeks to find the most efficient way to multiply a sequence of
matrices. The problem is not about performing the multiplications, but deciding the optimal parenthesization (order) to
minimize the total number of scalar multiplications.
Formulas/Theorems:
Recurrence Relation: Let product .
be the minimum number of scalar multiplications needed to compute the
where has dimensions .
Base Case: (single matrix requires no multiplications).
Time Complexity: for matrices.
Space Complexity: for the DP table.
Properties/Identities:
Exhibits optimal substructure and overlapping subproblems.
The order of multiplication matters for efficiency, not for the result.
Pitfalls/Tricks:

*(PDF Page 16)*

Incorrectly setting up the dimensions array . If there are matrices , and is , then
the array has elements.
Off-by-one errors in the recurrence relation indices.
Techniques/Shortcuts:
Fill the DP table diagonally, starting with chain length 2, then 3, and so on.
Maximum Minimum
Definition: The problem of finding both the maximum and minimum elements in a given array or list. This can be done
naively by iterating twice or more efficiently using a divide and conquer approach.
Formulas/Theorems:
Naive Approach (2N-2 comparisons): Iterate once for max, once for min.
Divide and Conquer Approach (approx. 3N/2 comparisons):
If array size is 1, max=min=element.
If array size is 2, compare once.
Recursively find max/min in two halves, then compare the two maxes and two mins.
Properties/Identities:
The divide and conquer approach is more efficient in terms of comparisons.
Pitfalls/Tricks:
Forgetting to handle base cases (array of size 1 or 2) correctly in recursive solutions.
Techniques/Shortcuts:
Pairwise comparison: process elements in pairs, comparing them. Then compare the smaller of the pair with the
current min, and the larger with the current max. This also achieves approx. 3N/2 comparisons.
Merge Sort
Definition: A divide and conquer sorting algorithm that divides an unsorted list into sublists, each containing one
element (a list of one element is considered sorted), then repeatedly merges sublists to produce new sorted sublists
until there is only one sorted list remaining.
Formulas/Theorems:
Recurrence Relation: Time Complexity: Space Complexity: (for dividing and merging).
for all cases (best, average, worst).
(due to auxiliary array for merging).
Properties/Identities:
Stable sorting algorithm.
Not an in-place algorithm (requires extra space).
Well-suited for external sorting.
Pitfalls/Tricks:
Incorrectly implementing the merging step, which is crucial for correctness and efficiency.
Forgetting to copy remaining elements from one half if the other half is exhausted during merge.
Techniques/Shortcuts:
The merge step is the core: combine two sorted arrays into one sorted array.
Can be used to count inversions.
Merging
Definition: The process of combining two or more sorted lists (or arrays) into a single sorted list. This is a fundamental
operation in algorithms like Merge Sort.
Formulas/Theorems:
Time Complexity: to merge two sorted lists of sizes and .
Space Complexity: for the new merged list.
Properties/Identities:
Requires input lists to be sorted.
The output list is also sorted.
Pitfalls/Tricks:
Off-by-one errors when handling array boundaries and indices.
Not correctly handling the case where one list is exhausted before the other.
Techniques/Shortcuts:
Use two pointers, one for each input list, and a third pointer for the merged list.

*(PDF Page 17)*

Minimum Spanning Tree (MST)
Definition: For a connected, undirected, weighted graph, an MST is a subgraph that is a tree, connects all the vertices
together, and has the minimum possible total edge weight. Algorithms include Prim's and Kruskal's.
Formulas/Theorems:
Cut Property: For any cut (partition of vertices into two sets), if an edge crosses the cut and has strictly less
weight than any other edge crossing the cut, then this edge must be in every MST.
Cycle Property: If an edge is the heaviest edge in any cycle of a graph, then it cannot be part of an MST.
An MST of a graph with vertices always has edges.
Properties/Identities:
Both Prim's and Kruskal's are greedy algorithms.
Prim's: Grows the MST from a starting vertex.
Kruskal's: Adds edges in increasing order of weight, avoiding cycles.
Pitfalls/Tricks:
Applying MST algorithms to disconnected graphs (they will find an MST for each connected component, forming
a Minimum Spanning Forest).
Confusing MST with shortest path problems.
Techniques/Shortcuts:
Prim's uses a min-priority queue.
Kruskal's uses a Disjoint Set Union (DSU) data structure.
Number of Swap
Definition: A metric used to evaluate the efficiency of certain sorting algorithms, particularly comparison sorts. It counts
how many times elements are exchanged during the sorting process.
Formulas/Theorems:
Bubble Sort (Worst Case): .
Selection Sort (Worst Case): .
Insertion Sort (Worst Case): .
Quick Sort (Worst Case): swaps.
Heap Sort (Worst Case): swaps.
Properties/Identities:
A lower number of swaps generally indicates better performance, especially when swap operations are costly.
Selection sort performs the minimum number of swaps among simple sorts.
Pitfalls/Tricks:
Confusing swaps with comparisons. Both are important metrics but measure different aspects.
Techniques/Shortcuts:
Memorize the worst-case swap counts for common sorting algorithms.
Prims Algorithm
Definition: A greedy algorithm that finds a Minimum Spanning Tree (MST) for a weighted undirected graph. It starts
from an arbitrary vertex and grows the MST by adding the cheapest edge that connects a vertex in the MST to a vertex
outside the MST.
Formulas/Theorems:
Time Complexity:
With adjacency matrix (simple array scan): .
With adjacency list and binary min-priority queue: or .
Space Complexity: for graph, for distances/parent array.
Properties/Identities:
Greedy algorithm.
Builds the MST by adding vertices one by one.
Similar structure to Dijkstra's algorithm.
Pitfalls/Tricks:
Forgetting to update edge weights in the priority queue when a shorter path to an unvisited vertex is found.
Applying to directed graphs (MST is for undirected graphs).
Techniques/Shortcuts:
Maintain a set of vertices already in the MST and a min-priority queue of edges connecting to vertices outside

*(PDF Page 18)*

the MST.
Quick Sort
Definition: A highly efficient, in-place, divide and conquer sorting algorithm. It works by selecting a 'pivot' element from
the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater
than the pivot. The sub-arrays are then sorted recursively.
Formulas/Theorems:
Worst-case Time Complexity: (e.g., already sorted array with first/last element as pivot).
Average-case Time Complexity: .
Best-case Time Complexity: .
Space Complexity: (average, for recursion stack) or Recurrence Relation (Average Case): (worst-case, for recursion stack).
, where is the size of one
partition. For balanced partitions, .
Properties/Identities:
Not a stable sorting algorithm.
In-place sorting algorithm.
Performance heavily depends on pivot selection.
Pitfalls/Tricks:
Poor pivot selection can lead to performance.
Incorrect partitioning logic can lead to infinite recursion or incorrect sorting.
Techniques/Shortcuts:
Randomized pivot selection helps achieve average-case performance reliably.
Hoare's partition scheme is often more efficient than Lomuto's.
Recurrence Relation
Definition: An equation that recursively defines a sequence or function, where each term or value is given as a function
of preceding terms. Used to describe the time complexity of recursive algorithms.
Formulas/Theorems:
Master Theorem: For recurrences of the form where .
1. If for some , then .
2. If , then .
3. If for some , AND for some and large , then
.
Properties/Identities:
Describes the growth rate of recursive algorithms.
Methods to solve: Substitution, Recursion Tree, Master Theorem.
Pitfalls/Tricks:
Incorrectly applying the Master Theorem (e.g., when met).
Algebraic errors in substitution or recursion tree methods.
Techniques/Shortcuts:
Memorize the three cases of the Master Theorem.
For simple recurrences, try expanding a few terms to find a pattern.
doesn't fit any case or the regularity condition is not
Recursion
Definition: A programming technique where a function calls itself directly or indirectly to solve a problem. It involves a
base case (stopping condition) and a recursive step (reducing the problem to a smaller instance of itself).
Properties/Identities:
Base Case: A condition that terminates the recursion.
Recursive Step: The function calls itself with a modified (smaller) input.
Often leads to elegant and concise code for problems with recursive structure.
Pitfalls/Tricks:
Missing or incorrect base case leading to infinite recursion (stack overflow).
High space complexity due to recursion stack.
Performance overhead compared to iterative solutions due to function call stack management.

*(PDF Page 19)*

Techniques/Shortcuts:
Always identify the base case first.
Ensure that each recursive call moves closer to the base case.
For some problems, recursion can be converted to iteration using a stack.
Searching
Definition: The process of finding a specific item (or items) within a collection of items. Common search algorithms
include Linear Search and Binary Search.
Formulas/Theorems:
Linear Search (Worst Case): comparisons.
Binary Search (Worst Case): comparisons.
Properties/Identities:
Linear Search: Works on unsorted or sorted data.
Binary Search: Requires sorted data.
Pitfalls/Tricks:
Using Linear Search on a large sorted array when Binary Search is applicable.
Errors in Binary Search boundary conditions.
Techniques/Shortcuts:
Always check if data is sorted before choosing a search algorithm.
Selection Sort
Definition: A simple sorting algorithm that repeatedly finds the minimum element from the unsorted part of the list and
swaps it with the element at the current position. It maintains two subarrays: sorted and unsorted.
Formulas/Theorems:
Worst-case Time Complexity: .
Average-case Time Complexity: .
Best-case Time Complexity: .
Space Complexity: (in-place).
Number of Swaps (All Cases): (minimum possible swaps for any comparison sort).
Number of Comparisons (All Cases): .
Properties/Identities:
Not a stable sorting algorithm.
Performs the minimum number of swaps among simple sorts.
Pitfalls/Tricks:
Its performance is consistently regardless of input order, unlike Bubble Sort or Insertion Sort.
Techniques/Shortcuts:
The key idea is to find the minimum and place it, then find the next minimum and place it, and so on.
Shortest Path
Definition: The problem of finding a path between two vertices (or from a source to all other vertices) in a graph such
that the sum of the weights of its constituent edges is minimized. Algorithms include BFS (unweighted), Dijkstra's (non-
negative weights), and Bellman-Ford (negative weights).
Properties/Identities:
Unweighted Graphs: BFS finds shortest path in terms of number of edges.
Non-negative Weighted Graphs: Dijkstra's algorithm.
Negative Weighted Graphs (no negative cycles): Bellman-Ford algorithm.
All-Pairs Shortest Path: Floyd-Warshall algorithm.
Pitfalls/Tricks:
Using the wrong algorithm for the given graph properties (e.g., Dijkstra's on negative weights).
Not handling disconnected components or unreachable vertices.
Techniques/Shortcuts:
Always check for negative edge weights and negative cycles.
Understand the relaxation principle.
Sorting

*(PDF Page 20)*

Definition: The process of arranging elements of a list or array in a specific order (e.g., numerical, alphabetical,
ascending, descending). It's a fundamental operation in computer science.
Formulas/Theorems:
Comparison Sort Lower Bound: Any comparison-based sorting algorithm requires in the worst case.
Properties/Identities:
Stable Sort: Preserves the relative order of equal elements.
In-place Sort: Requires or auxiliary space.
Adaptive Sort: Performance improves for partially sorted input.
Pitfalls/Tricks:
Confusing different sorting algorithm properties (stability, in-place, worst-case vs. average-case).
Choosing an inefficient sort for specific data characteristics.
Techniques/Shortcuts:
Know the time and space complexities, stability, and in-place nature of common sorts.
For GATE, often questions involve comparing two sorts or analyzing a modified sort.
comparisons
Space Complexity
Definition: A measure of the amount of memory an algorithm needs to run to completion. It includes the space required
for input, output, and temporary variables, often expressed using asymptotic notation.
Properties/Identities:
Auxiliary Space: The extra space used by the algorithm beyond the input data.
In-place Algorithm: An algorithm that transforms input using only a small, constant amount of auxiliary space,
typically or for recursion stack.
Pitfalls/Tricks:
Forgetting to account for the recursion stack space in recursive algorithms.
Confusing total space with auxiliary space.
Techniques/Shortcuts:
Identify data structures created by the algorithm (arrays, queues, stacks, hash tables).
For recursive calls, the maximum depth of the recursion stack contributes to space complexity.
Strongly Connected Components (SCC)
Definition: In a directed graph, a strongly connected component (SCC) is a maximal subgraph such that for every pair
of vertices and in the subgraph, there is a path from to and a path from to . Algorithms include Kosaraju's
and Tarjan's.
Properties/Identities:
SCCs partition the vertices of a directed graph.
If we contract each SCC into a single vertex, the resulting graph is a Directed Acyclic Graph (DAG).
Kosaraju's Algorithm: Two DFS passes (one on original graph, one on transpose graph).
Tarjan's Algorithm: One DFS pass, uses discovery times and low-link values.
Formulas/Theorems:
Time Complexity (Kosaraju's, Tarjan's): .
Pitfalls/Tricks:
Confusing SCCs with connected components in undirected graphs.
Incorrectly performing DFS on the transpose graph for Kosaraju's.
Techniques/Shortcuts:
Kosaraju's: DFS on G to get finishing times, then DFS on G transpose in decreasing order of finishing times.
Tarjan's: Uses a stack and `disc
` (discovery time) and `low
` (lowest discovery time reachable) arrays.
Time Complexity
Definition: A measure of the amount of time an algorithm takes to run as a function of the length of its input. It's
typically expressed using asymptotic notations (Big-O, Omega, Theta).
Properties/Identities:
Focuses on the growth rate of operations as input size increases.
Usually refers to worst-case time complexity, but average-case and best-case are also important.
Independent of machine specifics (CPU speed, memory access time).

*(PDF Page 21)*

Pitfalls/Tricks:
Confusing constant factors with asymptotic growth.
Incorrectly analyzing loops or recursive calls.
Assuming best-case performance for general analysis.
Techniques/Shortcuts:
Count dominant operations (comparisons, assignments, arithmetic operations).
For nested loops, multiply loop counts.
For recursive functions, use recurrence relations and Master Theorem.
Topological Sort
Definition: A linear ordering of vertices in a Directed Acyclic Graph (DAG) such that for every directed edge ,
vertex comes before vertex in the ordering. Not unique for all DAGs.
Properties/Identities:
Only possible for DAGs.
Can be implemented using DFS or Kahn's algorithm (using in-degrees and a queue).
Time Complexity: .
Pitfalls/Tricks:
Attempting to topologically sort a graph with cycles (it's impossible).
Incorrectly handling multiple possible topological sorts.
Techniques/Shortcuts:
DFS-based: Perform DFS, then reverse the order of finishing times.
Kahn's Algorithm: Find all nodes with in-degree 0, add to queue. While queue not empty, dequeue, add to
sorted list, decrement in-degree of neighbors. If neighbor's in-degree becomes 0, enqueue.
Tree Traversal
Definition: The process of visiting each node in a tree data structure exactly once. Common methods include Inorder,
Preorder, Postorder (for binary trees), and Level-order traversal.
Properties/Identities:
Inorder (Left-Root-Right): For BSTs, gives sorted elements.
Preorder (Root-Left-Right): Useful for creating a copy of the tree.
Postorder (Left-Right-Root): Useful for deleting a tree.
Level-order (BFS-like): Visits nodes level by level, uses a queue.
Time Complexity: for a tree with nodes.
Space Complexity: for DFS-based (recursion stack, where is height), for BFS-based (queue,
where is max width).
Pitfalls/Tricks:
Confusing the order of visits for different traversal types.
Incorrectly handling null nodes in recursive traversals.
Techniques/Shortcuts:
Practice drawing the traversal paths on sample trees.
Remember the "Root" position in the name (Pre-Root-Order, In-Root-Order, Post-Root-Order).
Uniform Hashing
Definition: An idealized theoretical model for hashing where each key is equally likely to hash to any slot in the hash
table, independent of where other keys hash. It implies a perfectly random distribution of keys.
Properties/Identities:
Assumed for theoretical analysis of hashing algorithms (e.g., average case performance of open addressing).
Difficult to achieve in practice with real-world data.
Minimizes collisions and maximizes efficiency.
Pitfalls/Tricks:
Assuming practical hash functions achieve uniform hashing, which is rarely true.
Not understanding that it's a theoretical ideal, not a practical hash function.
Techniques/Shortcuts:
When analyzing hashing, remember that uniform hashing is the best-case scenario for collision distribution.
Quick Formula Reference

*(PDF Page 22)*

Asymptotic Notations:
Big-O: .
Omega: .
Theta: .
Binary Heap:
Parent of (0-indexed): .
Left child of : .
Right child of : .
Height: .
Binary Tree:
Max nodes at level : .
Max nodes in height : .
Min height with nodes: .
Hashing (Open Addressing):
Linear Probing: .
Double Hashing: .
Load Factor: .
Matrix Chain Ordering:
Base Case: .
Recurrence Relation (Master Theorem): .
1. If , .
2. If , .
3. If and , .
Sorting Algorithm Complexities:
Algorithm Time (Worst) Time (Avg) Space Stable In-place
Bubble Sort Yes Yes
Insertion Sort Yes Yes
Selection Sort No Yes
Merge Sort Yes No
Quick Sort No Yes
Heap Sort No Yes
Graph Algorithm Complexities (Adjacency List):
BFS:
DFS:
Dijkstra's (Binary Heap):
Bellman-Ford:
Prim's (Binary Heap):
Kruskal's (DSU): or
Topological Sort:
SCC (Kosaraju's/Tarjan's):
Important Tips for GATE
1. Master Asymptotic Notations: A significant portion of algorithm questions revolves around time and space
complexity. Understand the definitions of thoroughly, and be adept at applying them to various code
snippets and recurrence relations, especially using the Master Theorem.
2. Understand Algorithm Design Paradigms: Don't just memorize algorithms; understand why they work and which
paradigm they belong to (Divide and Conquer, Greedy, Dynamic Programming). This helps in identifying the correct
approach for new problems.
3. Practice Recurrence Relations: Solving recurrence relations is a frequently tested skill. Be comfortable with the
substitution method, recursion tree method, and especially the Master Theorem. Pay attention to base cases and
boundary conditions.
4. Graph Algorithms are Crucial: BFS, DFS, Dijkstra's, Bellman-Ford, Prim's, Kruskal's, Topological Sort, and SCCs
are high-yield topics. Know their complexities, applications, and limitations (e.g., negative weights for

*(PDF Page 23)*


---

## 4. Complete Question Index & Answer Key Record (357 Questions)

| Q # | Question Source / Title | Answer Key |
| :---: | :--- | :---: |
| `1.1.1` | Algorithm Design: GATE CSE 1992 \| Question: 8 | **See PDF** |
| `1.1.2` | Algorithm Design: GATE CSE 1994 \| Question: 7 | **See PDF** |
| `1.1.3` | Algorithm Design: GATE CSE 2006 \| Question: 17 | **See PDF** |
| `1.1.4` | Algorithm Design: GATE CSE 2006 \| Question: 54 | **See PDF** |
| `1.1.5` | Algorithm Design: GATE CSE 2014 \| Set 1 \| Question: 37 | **See PDF** |
| `1.1.6` | Algorithm Design: GATE CSE 2019 \| Question: 25 | **See PDF** |
| `1.1.7` | Algorithm Design: GATE CSE 2021 \| Set 1 \| Question: 40 | **See PDF** |
| `1.1.8` | Algorithm Design: GATE CSE 2024 \| Set 2 \| Question: 32 | **See PDF** |
| `1.2.1` | Algorithm Design Techniques: GATE CSE 1990 \| Question: 12b | **See PDF** |
| `1.2.2` | Algorithm Design Techniques: GATE CSE 1990 \| Question: 2-vii | **See PDF** |
| `1.2.3` | Algorithm Design Techniques: GATE CSE 1994 \| Question: 1.19, ISRO2016-31 | **See PDF** |
| `1.2.4` | Algorithm Design Techniques: GATE CSE 1995 \| Question: 1.5 | **See PDF** |
| `1.2.5` | Algorithm Design Techniques: GATE CSE 1997 \| Question: 1.5 | **See PDF** |
| `1.2.6` | Algorithm Design Techniques: GATE CSE 1998 \| Question: 1.21, ISRO2008-16 | **See PDF** |
| `1.2.7` | Algorithm Design Techniques: GATE CSE 2015 \| Set 1 \| Question: 6 | **See PDF** |
| `1.2.8` | Algorithm Design Techniques: GATE CSE 2015 \| Set 2 \| Question: 36 | **See PDF** |
| `1.2.9` | Algorithm Design Techniques: GATE CSE 2017 \| Set 1 \| Question: 05 | **See PDF** |
| `1.3.1` | Asymptotic Notations: GATE CSE 1994 \| Question: 1.23 | **See PDF** |
| `1.3.2` | Asymptotic Notations: GATE CSE 1996 \| Question: 1.11 | **See PDF** |
| `1.3.3` | Asymptotic Notations: GATE CSE 1999 \| Question: 2.21 | **See PDF** |
| `1.3.4` | Asymptotic Notations: GATE CSE 2000 \| Question: 2.17 | **See PDF** |
| `1.3.5` | Asymptotic Notations: GATE CSE 2001 \| Question: 1.16 | **See PDF** |
| `1.3.6` | Asymptotic Notations: GATE CSE 2003 \| Question: 20 | **See PDF** |
| `1.3.7` | Asymptotic Notations: GATE CSE 2004 \| Question: 29 | **See PDF** |
| `1.3.8` | Asymptotic Notations: GATE CSE 2005 \| Question: 37 | **See PDF** |
| `1.3.9` | Asymptotic Notations: GATE CSE 2008 \| Question: 39 | **See PDF** |
| `1.3.10` | Asymptotic Notations: GATE CSE 2011 \| Question: 37 | **See PDF** |
| `1.3.11` | Asymptotic Notations: GATE CSE 2012 \| Question: 18 | **See PDF** |
| `1.3.12` | Asymptotic Notations: GATE CSE 2015 \| Set 3 \| Question: 4 | **See PDF** |
| `1.3.13` | Asymptotic Notations: GATE CSE 2015 \| Set 3 \| Question: 42 | **See PDF** |
| `1.3.14` | Asymptotic Notations: GATE CSE 2017 \| Set 1 \| Question: 04 | **See PDF** |
| `1.3.15` | Asymptotic Notations: GATE CSE 2021 \| Set 1 \| Question: 3 | **See PDF** |
| `1.3.16` | Asymptotic Notations: GATE CSE 2022 \| Question: 1 | **See PDF** |
| `1.3.17` | Asymptotic Notations: GATE CSE 2023 \| Question: 19 | **See PDF** |
| `1.3.19` | Asymptotic Notations: GATE CSE 2024 \| Set 2 \| Question: 5 | **See PDF** |
| `1.3.20` | Asymptotic Notations: GATE CSE 2026 \| Set 2 \| Question: 14 | **See PDF** |
| `1.3.21` | Asymptotic Notations: GATE IT 2004 \| Question: 55 | **See PDF** |
| `1.3.22` | Asymptotic Notations: GATE IT 2008 \| Question: 10 | **See PDF** |
| `1.4.1` | Bellman Ford: GATE CSE 2009 \| Question: 13 | **See PDF** |
| `1.4.2` | Bellman Ford: GATE CSE 2013 \| Question: 19 | **See PDF** |
| `1.5.1` | Binary Heap: GATE CSE 2026 \| Set 1 \| Question: 13 | **See PDF** |
| `1.6.1` | Binary Search: GATE CSE 2021 \| Set 2 \| Question: 8 | **See PDF** |
| `1.6.2` | Binary Search: GATE DA 2025 \| Question: 17 | **See PDF** |
| `1.6.3` | Binary Search: GATE DA 2026 \| Question: 21 | **See PDF** |
| `1.6.4` | Binary Search: GATE DS&AI 2024 \| Question: 30 | **See PDF** |
| `1.7.1` | Binary Search Tree: GATE CSE 2026 \| Set 1 \| Question: 30 | **See PDF** |
| `1.7.2` | Binary Search Tree: GATE CSE 2026 \| Set 1 \| Question: 52 | **See PDF** |
| `1.7.3` | Binary Search Tree: GATE CSE 2026 \| Set 2 \| Question: 39 | **See PDF** |
| `1.8.1` | Binary Tree: GATE CSE 2026 \| Set 1 \| Question: 23 | **See PDF** |
| `1.9.1` | Breadth First Search: GATE CSE 2025 \| Set 1 \| Question: 33 | **See PDF** |
| `1.9.2` | Breadth First Search: GATE DA 2026 \| Question: 30 | **See PDF** |
| `1.9.3` | Breadth First Search: GATE DS&AI 2024 \| Question: 34 | **See PDF** |
| `1.10.1` | Bubble Sort (1) | **See PDF** |
| `1.11.1` | Computer Science: GATE CS Practice : The "Master Theorem" (Algorithms) | **See PDF** |
| `1.12.1` | Depth First Search: GATE CSE 2026 \| Set 1 \| Question: 40 | **See PDF** |
| `1.12.2` | Depth First Search: GATE DA 2025 \| Question: 55 | **See PDF** |
| `1.13.1` | Dijkstras Algorithm: GATE CSE 1996 \| Question: 17 | **See PDF** |
| `1.13.2` | Dijkstras Algorithm: GATE CSE 2004 \| Question: 44 | **See PDF** |
| `1.13.3` | Dijkstras Algorithm: GATE CSE 2005 \| Question: 38 | **See PDF** |
| `1.13.4` | Dijkstras Algorithm: GATE CSE 2006 \| Question: 12 | **See PDF** |
| `1.13.5` | Dijkstras Algorithm: GATE CSE 2008 \| Question: 45 | **See PDF** |
| `1.14.1` | Directed Acyclic Graph: GATE CSE 2021 \| Set 2 \| Question: 55 | **See PDF** |
| `1.14.2` | Directed Acyclic Graph: GATE CSE 2026 \| Set 2 \| Question: 27 | **See PDF** |
| `1.15.1` | Double Hashing: GATE CSE 2020 \| Question: 23 | **See PDF** |
| `1.15.2` | Double Hashing: GATE CSE 2025 \| Set 1 \| Question: 55 | **See PDF** |
| `1.16.1` | Dynamic Programming: GATE CSE 2008 \| Question: 80 | **See PDF** |
| `1.16.2` | Dynamic Programming: GATE CSE 2008 \| Question: 81 | **See PDF** |
| `1.16.3` | Dynamic Programming: GATE CSE 2009 \| Question: 53 | **See PDF** |
| `1.16.4` | Dynamic Programming: GATE CSE 2009 \| Question: 54 | **See PDF** |
| `1.16.5` | Dynamic Programming: GATE CSE 2010 \| Question: 34 | **See PDF** |
| `1.16.6` | Dynamic Programming: GATE CSE 2011 \| Question: 25 | **See PDF** |
| `1.16.7` | Dynamic Programming: GATE CSE 2014 \| Set 2 \| Question: 37 | **See PDF** |
| `1.16.8` | Dynamic Programming: GATE CSE 2014 \| Set 3 \| Question: 37 | **See PDF** |
| `1.16.9` | Dynamic Programming: GATE CSE 2016 \| Set 2 \| Question: 14 | **See PDF** |
| `1.16.10` | Dynamic Programming: GATE CSE 2026 \| Set 2 \| Question: 29 | **See PDF** |
| `1.17.1` | Graph Algorithms: GATE CSE 1994 \| Question: 1.22 | **See PDF** |
| `1.17.2` | Graph Algorithms: GATE CSE 2003 \| Question: 70 | **See PDF** |
| `1.17.3` | Graph Algorithms: GATE CSE 2005 \| Question: 82a | **See PDF** |
| `1.17.4` | Graph Algorithms: GATE CSE 2005 \| Question: 82b | **See PDF** |
| `1.17.5` | Graph Algorithms: GATE CSE 2016 \| Set 2 \| Question: 41 | **See PDF** |
| `1.17.6` | Graph Algorithms: GATE CSE 2017 \| Set 1 \| Question: 26 | **See PDF** |
| `1.17.7` | Graph Algorithms: GATE CSE 2021 \| Set 2 \| Question: 46 | **See PDF** |
| `1.17.8` | Graph Algorithms: GATE CSE 2026 \| Set 1 \| Question: 31 | **See PDF** |
| `1.17.9` | Graph Algorithms: GATE IT 2005 \| Question: 15 | **See PDF** |
| `1.17.10` | Graph Algorithms: GATE IT 2005 \| Question: 84a | **See PDF** |
| `1.17.11` | Graph Algorithms: GATE IT 2005 \| Question: 84b | **See PDF** |
| `1.18.1` | Graph Search: GATE CSE 1989 \| Question: 4-vii | **See PDF** |
| `1.18.2` | Graph Search: GATE CSE 2000 \| Question: 1.13 | **See PDF** |
| `1.18.3` | Graph Search: GATE CSE 2000 \| Question: 2.19 | **See PDF** |
| `1.18.4` | Graph Search: GATE CSE 2001 \| Question: 2.14 | **See PDF** |
| `1.18.5` | Graph Search: GATE CSE 2003 \| Question: 21 | **See PDF** |
| `1.18.6` | Graph Search: GATE CSE 2006 \| Question: 48 | **See PDF** |
| `1.18.7` | Graph Search: GATE CSE 2008 \| Question: 19 | **See PDF** |
| `1.18.8` | Graph Search: GATE CSE 2014 \| Set 1 \| Question: 11 | **See PDF** |
| `1.18.9` | Graph Search: GATE CSE 2014 \| Set 2 \| Question: 14 | **See PDF** |
| `1.18.10` | Graph Search: GATE CSE 2014 \| Set 3 \| Question: 13 | **See PDF** |
| `1.18.11` | Graph Search: GATE CSE 2015 \| Set 1 \| Question: 45 | **See PDF** |
| `1.18.12` | Graph Search: GATE CSE 2016 \| Set 2 \| Question: 11 | **See PDF** |
| `1.18.13` | Graph Search: GATE CSE 2017 \| Set 2 \| Question: 15 | **See PDF** |
| `1.18.14` | Graph Search: GATE CSE 2018 \| Question: 30 | **See PDF** |
| `1.18.15` | Graph Search: GATE CSE 2023 \| Question: 46 | **See PDF** |
| `1.18.16` | Graph Search: GATE CSE 2024 \| Set 1 \| Question: 35 | **See PDF** |
| `1.18.17` | Graph Search: GATE CSE 2024 \| Set 1 \| Question: 50 | **See PDF** |
| `1.18.18` | Graph Search: GATE CSE 2025 \| Set 2 \| Question: 49 | **See PDF** |
| `1.18.19` | Graph Search: GATE DS&AI 2024 \| Question: 4 | **See PDF** |
| `1.18.20` | Graph Search: GATE IT 2005 \| Question: 14 | **See PDF** |
| `1.18.21` | Graph Search: GATE IT 2006 \| Question: 47 | **See PDF** |
| `1.18.22` | Graph Search: GATE IT 2007 \| Question: 24 | **See PDF** |
| `1.18.23` | Graph Search: GATE IT 2008 \| Question: 47 | **See PDF** |
| `1.19.1` | Greedy Algorithms: GATE CSE 1999 \| Question: 2.20 | **See PDF** |
| `1.19.2` | Greedy Algorithms: GATE CSE 2003 \| Question: 69 | **See PDF** |
| `1.19.3` | Greedy Algorithms: GATE CSE 2005 \| Question: 84a | **See PDF** |
| `1.19.4` | Greedy Algorithms: GATE CSE 2005 \| Question: 84b | **See PDF** |
| `1.19.5` | Greedy Algorithms: GATE CSE 2018 \| Question: 48 | **See PDF** |
| `1.20.1` | Hashing: GATE CSE 1989 \| Question: 1-vii, ISRO2015-14 | **See PDF** |
| `1.20.2` | Hashing: GATE CSE 1990 \| Question: 13b | **See PDF** |
| `1.20.3` | Hashing: GATE CSE 2021 \| Set 1 \| Question: 47 | **See PDF** |
| `1.20.4` | Hashing: GATE CSE 2023 \| Question: 10 | **See PDF** |
| `1.20.5` | Hashing: GATE CSE 2026 \| Set 2 \| Question: 20 | **See PDF** |
| `1.20.6` | Hashing: GATE IT 2005 \| Question: 16 | **See PDF** |
| `1.21.1` | Heap Sort: GATE CSE 2013 \| Question: 30 | **See PDF** |
| `1.21.2` | Heap Sort: GATE CSE 2024 \| Set 1 \| Question: 31 | **See PDF** |
| `1.22.1` | Huffman Code: GATE CSE 1989 \| Question: 13a | **See PDF** |
| `1.22.2` | Huffman Code: GATE CSE 2007 \| Question: 76 | **See PDF** |
| `1.22.3` | Huffman Code: GATE CSE 2007 \| Question: 77 | **See PDF** |
| `1.22.4` | Huffman Code: GATE CSE 2017 \| Set 2 \| Question: 50 | **See PDF** |
| `1.22.5` | Huffman Code: GATE CSE 2021 \| Set 2 \| Question: 26 | **See PDF** |
| `1.22.6` | Huffman Code: GATE IT 2006 \| Question: 48 | **See PDF** |
| `1.23.1` | Identify Function: GATE CSE 1989 \| Question: 8a | **See PDF** |
| `1.23.2` | Identify Function: GATE CSE 1990 \| Question: 11b | **See PDF** |
| `1.23.3` | Identify Function: GATE CSE 1991 \| Question: 03-viii | **See PDF** |
| `1.23.4` | Identify Function: GATE CSE 1993 \| Question: 7.4 | **See PDF** |
| `1.23.5` | Identify Function: GATE CSE 1994 \| Question: 6 | **See PDF** |
| `1.23.6` | Identify Function: GATE CSE 1995 \| Question: 1.4 | **See PDF** |
| `1.23.7` | Identify Function: GATE CSE 1995 \| Question: 2.3 | **See PDF** |
| `1.23.8` | Identify Function: GATE CSE 1995 \| Question: 4 | **See PDF** |
| `1.23.9` | Identify Function: GATE CSE 1998 \| Question: 2.12 | **See PDF** |
| `1.23.10` | Identify Function: GATE CSE 1999 \| Question: 2.24 | **See PDF** |
| `1.23.11` | Identify Function: GATE CSE 2000 \| Question: 2.15 | **See PDF** |
| `1.23.12` | Identify Function: GATE CSE 2003 \| Question: 1 | **See PDF** |
| `1.23.13` | Identify Function: GATE CSE 2003 \| Question: 88 | **See PDF** |
| `1.23.14` | Identify Function: GATE CSE 2004 \| Question: 41 | **See PDF** |
| `1.23.15` | Identify Function: GATE CSE 2004 \| Question: 42 | **See PDF** |
| `1.23.16` | Identify Function: GATE CSE 2005 \| Question: 31 | **See PDF** |
| `1.23.17` | Identify Function: GATE CSE 2006 \| Question: 50 | **See PDF** |
| `1.23.18` | Identify Function: GATE CSE 2006 \| Question: 53 | **See PDF** |
| `1.23.19` | Identify Function: GATE CSE 2009 \| Question: 18 | **See PDF** |
| `1.23.20` | Identify Function: GATE CSE 2010 \| Question: 35 | **See PDF** |
| `1.23.21` | Identify Function: GATE CSE 2011 \| Question: 48 | **See PDF** |
| `1.23.22` | Identify Function: GATE CSE 2011 \| Question: 49 | **See PDF** |
| `1.23.23` | Identify Function: GATE CSE 2013 \| Question: 31 | **See PDF** |
| `1.23.24` | Identify Function: GATE CSE 2014 \| Set 1 \| Question: 41 | **See PDF** |
| `1.23.25` | Identify Function: GATE CSE 2014 \| Set 2 \| Question: 10 | **See PDF** |
| `1.23.26` | Identify Function: GATE CSE 2014 \| Set 3 \| Question: 10 | **See PDF** |
| `1.23.27` | Identify Function: GATE CSE 2015 \| Set 1 \| Question: 31 | **See PDF** |
| `1.23.28` | Identify Function: GATE CSE 2015 \| Set 2 \| Question: 11 | **See PDF** |
| `1.23.29` | Identify Function: GATE CSE 2015 \| Set 3 \| Question: 49 | **See PDF** |
| `1.23.30` | Identify Function: GATE CSE 2019 \| Question: 26 | **See PDF** |
| `1.23.31` | Identify Function: GATE CSE 2020 \| Question: 48 | **See PDF** |
| `1.23.32` | Identify Function: GATE CSE 2021 \| Set 1 \| Question: 48 | **See PDF** |
| `1.23.33` | Identify Function: GATE CSE 2021 \| Set 2 \| Question: 23 | **See PDF** |
| `1.23.34` | Identify Function: GATE IT 2005 \| Question: 53 | **See PDF** |
| `1.23.35` | Identify Function: GATE IT 2005 \| Question: 57 | **See PDF** |
| `1.23.36` | Identify Function: GATE IT 2006 \| Question: 52 | **See PDF** |
| `1.23.37` | Identify Function: GATE IT 2008 \| Question: 82 | **See PDF** |
| `1.23.38` | Identify Function: GATE IT 2008 \| Question: 83 | **See PDF** |
| `1.24.1` | Insertion Sort: GATE CSE 2003 \| Question: 22 | **See PDF** |
| `1.24.2` | Insertion Sort: GATE CSE 2003 \| Question: 62 | **See PDF** |
| `1.25.1` | Inversion: GATE CSE 2003 \| Question: 61 | **See PDF** |
| `1.25.2` | Inversion: GATE DA 2025 \| Question: 19 | **See PDF** |
| `1.26.1` | Linear Probing: GATE CSE 2026 \| Set 1 \| Question: 14 | **See PDF** |
| `1.26.2` | Linear Probing: GATE DA 2025 \| Question: 8 | **See PDF** |
| `1.27.1` | Matrix Chain Ordering: GATE CSE 2011 \| Question: 38 | **See PDF** |
| `1.27.2` | Matrix Chain Ordering: GATE CSE 2016 \| Set 2 \| Question: 38 | **See PDF** |
| `1.27.3` | Matrix Chain Ordering: GATE CSE 2018 \| Question: 31 | **See PDF** |
| `1.28.1` | Maximum Minimum: GATE CSE 2014 \| Set 1 \| Question: 39 | **See PDF** |
| `1.29.1` | Merge Sort: GATE CSE 1999 \| Question: 1.14, ISRO2015-42 | **See PDF** |
| `1.29.2` | Merge Sort: GATE CSE 2012 \| Question: 39 | **See PDF** |
| `1.29.3` | Merge Sort: GATE CSE 2015 \| Set 3 \| Question: 27 | **See PDF** |
| `1.29.4` | Merge Sort: GATE CSE 2026 \| Set 2 \| Question: 22 | **See PDF** |
| `1.30.1` | Merging: GATE CSE 1995 \| Question: 1.16 | **See PDF** |
| `1.30.2` | Merging: GATE CSE 2014 \| Set 2 \| Question: 38 | **See PDF** |
| `1.31.1` | Minimum Spanning Tree: GATE CSE 1991 \| Question: 03,vi | **See PDF** |
| `1.31.2` | Minimum Spanning Tree: GATE CSE 1992 \| Question: 01,ix | **See PDF** |
| `1.31.3` | Minimum Spanning Tree: GATE CSE 1995 \| Question: 22 | **See PDF** |
| `1.31.4` | Minimum Spanning Tree: GATE CSE 1996 \| Question: 16 | **See PDF** |
| `1.31.5` | Minimum Spanning Tree: GATE CSE 1997 \| Question: 9 | **See PDF** |
| `1.31.6` | Minimum Spanning Tree: GATE CSE 2000 \| Question: 2.18 | **See PDF** |
| `1.31.7` | Minimum Spanning Tree: GATE CSE 2001 \| Question: 15 | **See PDF** |
| `1.31.8` | Minimum Spanning Tree: GATE CSE 2003 \| Question: 68 | **See PDF** |
| `1.31.9` | Minimum Spanning Tree: GATE CSE 2005 \| Question: 6 | **See PDF** |
| `1.31.10` | Minimum Spanning Tree: GATE CSE 2006 \| Question: 11 | **See PDF** |
| `1.31.11` | Minimum Spanning Tree: GATE CSE 2006 \| Question: 47 | **See PDF** |
| `1.31.12` | Minimum Spanning Tree: GATE CSE 2007 \| Question: 49 | **See PDF** |
| `1.31.13` | Minimum Spanning Tree: GATE CSE 2009 \| Question: 38 | **See PDF** |
| `1.31.14` | Minimum Spanning Tree: GATE CSE 2010 \| Question: 50 | **See PDF** |
| `1.31.15` | Minimum Spanning Tree: GATE CSE 2010 \| Question: 51 | **See PDF** |
| `1.31.16` | Minimum Spanning Tree: GATE CSE 2011 \| Question: 54 | **See PDF** |
| `1.31.17` | Minimum Spanning Tree: GATE CSE 2011 \| Question: 55 | **See PDF** |
| `1.31.18` | Minimum Spanning Tree: GATE CSE 2012 \| Question: 29 | **See PDF** |
| `1.31.19` | Minimum Spanning Tree: GATE CSE 2014 \| Set 2 \| Question: 52 | **See PDF** |
| `1.31.20` | Minimum Spanning Tree: GATE CSE 2015 \| Set 1 \| Question: 43 | **See PDF** |
| `1.31.21` | Minimum Spanning Tree: GATE CSE 2015 \| Set 3 \| Question: 40 | **See PDF** |
| `1.31.22` | Minimum Spanning Tree: GATE CSE 2016 \| Set 1 \| Question: 14 | **See PDF** |
| `1.31.23` | Minimum Spanning Tree: GATE CSE 2016 \| Set 1 \| Question: 39 | **See PDF** |
| `1.31.24` | Minimum Spanning Tree: GATE CSE 2016 \| Set 1 \| Question: 40 | **See PDF** |
| `1.31.25` | Minimum Spanning Tree: GATE CSE 2018 \| Question: 47 | **See PDF** |
| `1.31.26` | Minimum Spanning Tree: GATE CSE 2020 \| Question: 31 | **See PDF** |
| `1.31.27` | Minimum Spanning Tree: GATE CSE 2020 \| Question: 49 | **See PDF** |
| `1.31.28` | Minimum Spanning Tree: GATE CSE 2021 \| Set 1 \| Question: 17 | **See PDF** |
| `1.31.29` | Minimum Spanning Tree: GATE CSE 2021 \| Set 2 \| Question: 1 | **See PDF** |
| `1.31.30` | Minimum Spanning Tree: GATE CSE 2022 \| Question: 39 | **See PDF** |
| `1.31.31` | Minimum Spanning Tree: GATE CSE 2022 \| Question: 48 | **See PDF** |
| `1.31.32` | Minimum Spanning Tree: GATE CSE 2024 \| Set 2 \| Question: 49 | **See PDF** |
| `1.31.33` | Minimum Spanning Tree: GATE CSE 2025 \| Set 1 \| Question: 54 | **See PDF** |
| `1.31.34` | Minimum Spanning Tree: GATE CSE 2026 \| Set 1 \| Question: 39 | **See PDF** |
| `1.31.35` | Minimum Spanning Tree: GATE IT 2005 \| Question: 52 | **See PDF** |
| `1.32.1` | Number of Swap (1) | **See PDF** |
| `1.33.1` | Prims Algorithm (2) | **See PDF** |
| `1.33.2` | Prims Algorithm: GATE IT 2008 \| Question: 45 | **See PDF** |
| `1.34.1` | Quick Sort: GATE CSE 1987 \| Question: 1-xviii | **See PDF** |
| `1.34.2` | Quick Sort: GATE CSE 1989 \| Question: 9 | **See PDF** |
| `1.34.3` | Quick Sort: GATE CSE 1992 \| Question: 03,iv | **See PDF** |
| `1.34.4` | Quick Sort: GATE CSE 1996 \| Question: 2.15 | **See PDF** |
| `1.34.5` | Quick Sort: GATE CSE 2001 \| Question: 1.14 | **See PDF** |
| `1.34.6` | Quick Sort: GATE CSE 2006 \| Question: 52 | **See PDF** |
| `1.34.7` | Quick Sort: GATE CSE 2008 \| Question: 43 | **See PDF** |
| `1.34.8` | Quick Sort: GATE CSE 2009 \| Question: 39 | **See PDF** |
| `1.34.9` | Quick Sort: GATE CSE 2014 \| Set 1 \| Question: 14 | **See PDF** |
| `1.34.10` | Quick Sort: GATE CSE 2014 \| Set 3 \| Question: 14 | **See PDF** |
| `1.34.11` | Quick Sort: GATE CSE 2015 \| Set 1 \| Question: 2 | **See PDF** |
| `1.34.12` | Quick Sort: GATE CSE 2015 \| Set 2 \| Question: 45 | **See PDF** |
| `1.34.13` | Quick Sort: GATE CSE 2019 \| Question: 20 | **See PDF** |
| `1.34.14` | Quick Sort: GATE DA 2026 \| Question: 5 | **See PDF** |
| `1.34.15` | Quick Sort: GATE DS&AI 2024 \| Question: 20 | **See PDF** |
| `1.35.1` | Recurrence Relation: GATE CSE 1987 \| Question: 10a | **See PDF** |
| `1.35.2` | Recurrence Relation: GATE CSE 1988 \| Question: 13iv | **See PDF** |
| `1.35.3` | Recurrence Relation: GATE CSE 1989 \| Question: 13b | **See PDF** |
| `1.35.4` | Recurrence Relation: GATE CSE 1990 \| Question: 17a | **See PDF** |
| `1.35.5` | Recurrence Relation: GATE CSE 1992 \| Question: 07a | **See PDF** |
| `1.35.6` | Recurrence Relation: GATE CSE 1992 \| Question: 07b | **See PDF** |
| `1.35.7` | Recurrence Relation: GATE CSE 1993 \| Question: 15 | **See PDF** |
| `1.35.8` | Recurrence Relation: GATE CSE 1994 \| Question: 1.7, ISRO2017-14 | **See PDF** |
| `1.35.9` | Recurrence Relation: GATE CSE 1996 \| Question: 2.12 | **See PDF** |
| `1.35.10` | Recurrence Relation: GATE CSE 1997 \| Question: 15 | **See PDF** |
| `1.35.11` | Recurrence Relation: GATE CSE 1997 \| Question: 4.6 | **See PDF** |
| `1.35.12` | Recurrence Relation: GATE CSE 1998 \| Question: 6a | **See PDF** |
| `1.35.13` | Recurrence Relation: GATE CSE 2002 \| Question: 1.3 | **See PDF** |
| `1.35.14` | Recurrence Relation: GATE CSE 2002 \| Question: 2.11 | **See PDF** |
| `1.35.15` | Recurrence Relation: GATE CSE 2003 \| Question: 35 | **See PDF** |
| `1.35.16` | Recurrence Relation: GATE CSE 2004 \| Question: 83, ISRO2015-40 | **See PDF** |
| `1.35.17` | Recurrence Relation: GATE CSE 2004 \| Question: 84 | **See PDF** |
| `1.35.18` | Recurrence Relation: GATE CSE 2006 \| Question: 51, ISRO2016-34 | **See PDF** |
| `1.35.19` | Recurrence Relation: GATE CSE 2008 \| Question: 78 | **See PDF** |
| `1.35.20` | Recurrence Relation: GATE CSE 2008 \| Question: 79 | **See PDF** |
| `1.35.21` | Recurrence Relation: GATE CSE 2009 \| Question: 35 | **See PDF** |
| `1.35.22` | Recurrence Relation: GATE CSE 2012 \| Question: 16 | **See PDF** |
| `1.35.23` | Recurrence Relation: GATE CSE 2014 \| Set 2 \| Question: 13 | **See PDF** |
| `1.35.24` | Recurrence Relation: GATE CSE 2015 \| Set 1 \| Question: 49 | **See PDF** |
| `1.35.25` | Recurrence Relation: GATE CSE 2015 \| Set 3 \| Question: 39 | **See PDF** |
| `1.35.26` | Recurrence Relation: GATE CSE 2016 \| Set 2 \| Question: 39 | **See PDF** |
| `1.35.27` | Recurrence Relation: GATE CSE 2017 \| Set 2 \| Question: 30 | **See PDF** |
| `1.35.28` | Recurrence Relation: GATE CSE 2020 \| Question: 2 | **See PDF** |
| `1.35.29` | Recurrence Relation: GATE CSE 2021 \| Set 1 \| Question: 30 | **See PDF** |
| `1.35.30` | Recurrence Relation: GATE CSE 2021 \| Set 2 \| Question: 39 | **See PDF** |
| `1.35.31` | Recurrence Relation: GATE CSE 2024 \| Set 1 \| Question: 32 | **See PDF** |
| `1.35.32` | Recurrence Relation: GATE CSE 2025 \| Set 1 \| Question: 10 | **See PDF** |
| `1.35.33` | Recurrence Relation: GATE CSE 2026 \| Set 2 \| Question: 15 | **See PDF** |
| `1.35.34` | Recurrence Relation: GATE IT 2004 \| Question: 57 | **See PDF** |
| `1.35.35` | Recurrence Relation: GATE IT 2005 \| Question: 51 | **See PDF** |
| `1.35.36` | Recurrence Relation: GATE IT 2008 \| Question: 44 | **See PDF** |
| `1.36.1` | Recursion: GATE CSE 1995 \| Question: 2.9 | **See PDF** |
| `1.36.2` | Recursion: GATE CSE 2007 \| Question: 44 | **See PDF** |
| `1.36.3` | Recursion: GATE CSE 2018 \| Question: 45 | **See PDF** |
| `1.36.4` | Recursion: GATE CSE 2021 \| Set 2 \| Question: 49 | **See PDF** |
| `1.36.5` | Recursion: GATE CSE 2026 \| Set 1 \| Question: 51 | **See PDF** |
| `1.37.1` | Searching: GATE CSE 1996 \| Question: 18 | **See PDF** |
| `1.37.2` | Searching: GATE CSE 1996 \| Question: 2.13, ISRO2016-28 | **See PDF** |
| `1.37.3` | Searching: GATE CSE 2002 \| Question: 2.10 | **See PDF** |
| `1.37.4` | Searching: GATE CSE 2008 \| Question: 84 | **See PDF** |
| `1.37.5` | Searching: GATE CSE 2008 \| Question: 85 | **See PDF** |
| `1.37.6` | Searching: GATE CSE 2017 \| Set 1 \| Question: 48 | **See PDF** |
| `1.37.7` | Searching: GATE CSE 2025 \| Set 2 \| Question: 19 | **See PDF** |
| `1.37.8` | Searching: GATE CSE 2025 \| Set 2 \| Question: 31 | **See PDF** |
| `1.38.1` | Selection Sort: GATE CSE 2009 \| Question: 11 | **See PDF** |
| `1.38.2` | Selection Sort: GATE CSE 2013 \| Question: 6 | **See PDF** |
| `1.39.1` | Shortest Path: GATE CSE 2002 \| Question: 12 | **See PDF** |
| `1.39.2` | Shortest Path: GATE CSE 2003 \| Question: 67 | **See PDF** |
| `1.39.3` | Shortest Path: GATE CSE 2007 \| Question: 41 | **See PDF** |
| `1.39.4` | Shortest Path: GATE CSE 2020 \| Question: 40 | **See PDF** |
| `1.39.5` | Shortest Path: GATE CSE 2025 \| Set 1 \| Question: 8 | **See PDF** |
| `1.39.6` | Shortest Path: GATE CSE 2025 \| Set 2 \| Question: 27 | **See PDF** |
| `1.39.7` | Shortest Path: GATE DA 2025 \| Question: 48 | **See PDF** |
| `1.39.8` | Shortest Path: GATE IT 2007 \| Question: 3, UGCNET-June2012-III: 34 | **See PDF** |
| `1.40.1` | Sorting: GATE CSE 1988 \| Question: 1iii | **See PDF** |
| `1.40.2` | Sorting: GATE CSE 1990 \| Question: 3-v | **See PDF** |
| `1.40.3` | Sorting: GATE CSE 1991 \| Question: 01,vii | **See PDF** |
| `1.40.4` | Sorting: GATE CSE 1991 \| Question: 13 | **See PDF** |
| `1.40.5` | Sorting: GATE CSE 1992 \| Question: 02,ix | **See PDF** |
| `1.40.6` | Sorting: GATE CSE 1996 \| Question: 14 | **See PDF** |
| `1.40.7` | Sorting: GATE CSE 1998 \| Question: 1.22 | **See PDF** |
| `1.40.8` | Sorting: GATE CSE 1999 \| Question: 1.12 | **See PDF** |
| `1.40.9` | Sorting: GATE CSE 1999 \| Question: 8 | **See PDF** |
| `1.40.10` | Sorting: GATE CSE 2000 \| Question: 17 | **See PDF** |
| `1.40.11` | Sorting: GATE CSE 2005 \| Question: 39 | **See PDF** |
| `1.40.12` | Sorting: GATE CSE 2006 \| Question: 14, ISRO2011-14 | **See PDF** |
| `1.40.13` | Sorting: GATE CSE 2007 \| Question: 14 | **See PDF** |
| `1.40.14` | Sorting: GATE CSE 2016 \| Set 1 \| Question: 13 | **See PDF** |
| `1.40.15` | Sorting: GATE CSE 2016 \| Set 2 \| Question: 13 | **See PDF** |
| `1.40.16` | Sorting: GATE CSE 2021 \| Set 1 \| Question: 9 | **See PDF** |
| `1.40.17` | Sorting: GATE CSE 2024 \| Set 2 \| Question: 25 | **See PDF** |
| `1.40.18` | Sorting: GATE CSE 2025 \| Set 2 \| Question: 10 | **See PDF** |
| `1.40.19` | Sorting: GATE DA 2026 \| Question: 39 | **See PDF** |
| `1.40.20` | Sorting: GATE DS&AI 2024 \| Question: 35 | **See PDF** |
| `1.40.21` | Sorting: GATE IT 2005 \| Question: 59 | **See PDF** |
| `1.40.22` | Sorting: GATE IT 2008 \| Question: 43 | **See PDF** |
| `1.41.1` | Space Complexity: GATE CSE 2005 \| Question: 81a | **See PDF** |
| `1.42.1` | Strongly Connected Components: GATE CSE 2008 \| Question: 7 | **See PDF** |
| `1.42.2` | Strongly Connected Components: GATE CSE 2018 \| Question: 43 | **See PDF** |
| `1.42.3` | Strongly Connected Components: GATE IT 2006 \| Question: 46 | **See PDF** |
| `1.43.1` | Time Complexity: GATE CSE 1988 \| Question: 6i | **See PDF** |
| `1.43.2` | Time Complexity: GATE CSE 1989 \| Question: 2-iii | **See PDF** |
| `1.43.3` | Time Complexity: GATE CSE 1993 \| Question: 8.7 | **See PDF** |
| `1.43.4` | Time Complexity: GATE CSE 1999 \| Question: 1.13 | **See PDF** |
| `1.43.5` | Time Complexity: GATE CSE 1999 \| Question: 1.16 | **See PDF** |
| `1.43.6` | Time Complexity: GATE CSE 1999 \| Question: 11a | **See PDF** |
| `1.43.7` | Time Complexity: GATE CSE 2000 \| Question: 1.15 | **See PDF** |
| `1.43.8` | Time Complexity: GATE CSE 2003 \| Question: 66 | **See PDF** |
| `1.43.9` | Time Complexity: GATE CSE 2004 \| Question: 39 | **See PDF** |
| `1.43.10` | Time Complexity: GATE CSE 2004 \| Question: 82 | **See PDF** |
| `1.43.11` | Time Complexity: GATE CSE 2006 \| Question: 15 | **See PDF** |
| `1.43.12` | Time Complexity: GATE CSE 2007 \| Question: 15, ISRO2016-26 | **See PDF** |
| `1.43.13` | Time Complexity: GATE CSE 2007 \| Question: 45 | **See PDF** |
| `1.43.14` | Time Complexity: GATE CSE 2007 \| Question: 50 | **See PDF** |
| `1.43.15` | Time Complexity: GATE CSE 2007 \| Question: 51 | **See PDF** |
| `1.43.16` | Time Complexity: GATE CSE 2008 \| Question: 40 | **See PDF** |
| `1.43.17` | Time Complexity: GATE CSE 2008 \| Question: 47 | **See PDF** |
| `1.43.18` | Time Complexity: GATE CSE 2008 \| Question: 74 | **See PDF** |
| `1.43.19` | Time Complexity: GATE CSE 2008 \| Question: 75 | **See PDF** |
| `1.43.20` | Time Complexity: GATE CSE 2010 \| Question: 12 | **See PDF** |
| `1.43.21` | Time Complexity: GATE CSE 2014 \| Set 1 \| Question: 42 | **See PDF** |
| `1.43.22` | Time Complexity: GATE CSE 2015 \| Set 1 \| Question: 40 | **See PDF** |
| `1.43.23` | Time Complexity: GATE CSE 2015 \| Set 2 \| Question: 22 | **See PDF** |
| `1.43.24` | Time Complexity: GATE CSE 2017 \| Set 2 \| Question: 03 | **See PDF** |
| `1.43.25` | Time Complexity: GATE CSE 2017 \| Set 2 \| Question: 38 | **See PDF** |
| `1.43.26` | Time Complexity: GATE CSE 2019 \| Question: 37 | **See PDF** |
| `1.43.27` | Time Complexity: GATE CSE 2024 \| Set 1 \| Question: 7 | **See PDF** |
| `1.43.28` | Time Complexity: GATE CSE 2026 \| Set 1 \| Question: 7 | **See PDF** |
| `1.43.29` | Time Complexity: GATE CSE 2026 \| Set 2 \| Question: 28 | **See PDF** |
| `1.43.30` | Time Complexity: GATE IT 2007 \| Question: 17 | **See PDF** |
| `1.43.31` | Time Complexity: GATE IT 2007 \| Question: 81 | **See PDF** |
| `1.44.1` | Topological Sort: GATE CSE 2007 \| Question: 5 | **See PDF** |
| `1.44.2` | Topological Sort: GATE CSE 2014 \| Set 1 \| Question: 13 | **See PDF** |
| `1.44.3` | Topological Sort: GATE CSE 2016 \| Set 1 \| Question: 11 | **See PDF** |
| `1.44.4` | Topological Sort: GATE DS&AI 2024 \| Question: 41 | **See PDF** |
| `1.45.1` | Tree Traversal: GATE DA 2026 \| Question: 15 | **See PDF** |
| `1.46.1` | Uniform Hashing: GATE CSE 2022 \| Question: 6 | **See PDF** |

