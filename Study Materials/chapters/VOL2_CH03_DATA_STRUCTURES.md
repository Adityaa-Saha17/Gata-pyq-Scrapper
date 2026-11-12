# Volume 2 — Chapter 3: Programming and DS: Data Structures

- **Source PDF**: [filter1_volume2.pdf](file:///Users/adityaasaha/Documents/Academics/Gate/filter1_volume2.pdf)
- **Total GATE Questions in Chapter**: **238**

---

## 1. Subtopic Weightage & Question Distribution

| Subtopic # | Subtopic Name | Questions |
| :---: | :--- | :---: |
| **3.1** | AVL Tree | 6 |
| **3.2** | Abstract Data Type | 1 |
| **3.3** | Array | 13 |
| **3.4** | Binary Heap | 30 |
| **3.5** | Binary Search Tree | 36 |
| **3.6** | Binary Tree | 53 |
| **3.7** | Data Structures | 4 |
| **3.8** | Hashing | 15 |
| **3.9** | Infix Prefix | 4 |
| **3.10** | Linked List | 24 |
| **3.11** | Priority Queue | 2 |
| **3.12** | Queue | 15 |
| **3.14** | Time Complexity | 1 |
| **3.15** | Tree | 13 |
| **3.16** | ✍ Practice Test: Tree Traversal | 1 |
| **3.17** | Uniform Hashing | 1 |


---

## 2. Comprehensive GATE CSE Data Structures Reference (Expanded Research & Formulas)

### 2.1 Arrays & Address Calculation
- **1D Array $A[L \dots U]$**: $\text{Addr}(A[i]) = B + (i - L) \times w$.
- **2D Array $A[L_1 \dots U_1][L_2 \dots U_2]$** with $R = U_1 - L_1 + 1$ rows and $C = U_2 - L_2 + 1$ columns:
  - **Row-Major Order (C/C++)**: $\text{Addr}(A[i][j]) = B + \big((i - L_1) \cdot C + (j - L_2)\big) \times w$.
  - **Column-Major Order (Fortran/MATLAB)**: $\text{Addr}(A[i][j]) = B + \big((j - L_2) \cdot R + (i - L_1)\big) \times w$.
- **Lower Triangular Matrix ($i \ge j$, 1-indexed, Row-Major)**: $\text{Index}(A[i][j]) = \frac{i(i-1)}{2} + (j - 1)$.

### 2.2 Stacks, Queues & Linked Lists
- **Stack Permutation / Catalan Count**: Number of valid output permutations of $1 \dots n$ using one stack $= C_n = \frac{1}{n+1}\binom{2n}{n}$. A permutation is invalid iff there exist indices $i < j < k$ with values $p_k < p_i < p_j$ (**3-1-2 pattern**).
- **Queue using Two Stacks ($S_1, S_2$)**: Amortized $O(1)$ per operation (Enqueue: push to $S_1$; Dequeue: if $S_2$ empty, pop all from $S_1$ and push to $S_2$, then pop $S_2$).
- **Circular Queue in Array of Size $N$**:
  - Full condition (wasting 1 slot): `(rear + 1) % N == front` (max capacity $N - 1$).
  - Current size: `(rear - front + N) % N`.

### 2.3 Trees, Binary Trees, BSTs & AVL Trees
- **Binary Tree Formulas**:
  - **Leaf vs Degree-2 Nodes**: For any non-empty binary tree, $n_0 = n_2 + 1$ (where $n_0 =$ leaf count, $n_2 =$ internal nodes with 2 children).
  - **Strict / Full $k$-ary Tree** (every internal node has exactly $k$ children, $I$ internal nodes):
    $$\text{Leaves } L = (k - 1)I + 1, \qquad \text{Total Nodes } N = kI + 1$$
  - **Null Pointers in $n$-Node Binary Tree**: Exactly $n + 1$ null pointers (used in Threaded Binary Trees).
  - **Height $h$ of $n$-Node Binary Tree** (root at height $0$): $\lfloor \log_2 n \rfloor \le h \le n - 1$.
  - **Unique Binary Tree Reconstruction**:
    - **Inorder + Preorder** $\implies$ Unique Binary Tree.
    - **Inorder + Postorder** $\implies$ Unique Binary Tree.
    - **Preorder + Postorder** $\implies$ Unique **Full (Strict)** Binary Tree, NOT unique in general!
- **Binary Search Tree (BST)**:
  - **Inorder traversal** of any BST produces keys in **strictly sorted (ascending) order**.
  - Number of distinct BSTs with $n$ distinct keys $= C_n = \frac{1}{n+1}\binom{2n}{n}$.
  - Number of distinct Binary Trees with $n$ **labeled** nodes $= n! \cdot C_n$.
- **AVL Tree (Height-Balanced BST, $|\text{BF}| = |h_L - h_R| \le 1$)**:
  - **Minimum nodes $N(h)$ in an AVL tree of height $h$** (with $N(0)=1, N(1)=2$ for 0-based height):
    $$N(h) = N(h - 1) + N(h - 2) + 1 = F_{h+3} - 1$$
    - Values of $N(h)$: $N(0)=1, N(1)=2, N(2)=4, N(3)=7, N(4)=12, N(5)=20, N(6)=33, N(7)=54$.
  - **Rotations on Insertion**: At most **$1$ rotation** (single LL/RR or double LR/RL) is sufficient to rebalance an AVL tree after insertion!
  - **Rotations on Deletion**: May require **$O(\log n)$ rotations** propagating up to the root.

### 2.4 Binary Heaps
- **Array Representation (1-indexed)**: Parent of $i = \lfloor i/2 \rfloor$; Left child $= 2i$; Right child $= 2i + 1$.
- **Leaves in an $n$-element Heap**: Indices $\lfloor n/2 \rfloor + 1$ through $n$ (total $\lceil n/2 \rceil$ leaves).
- **Height of $n$-element Heap**: $\lfloor \log_2 n \rfloor$.
- **Build-Heap Time Complexity**: $\Theta(n)$ time! Specifically, $\sum_{h=0}^{\lfloor \log n \rfloor} \lceil \frac{n}{2^{h+1}} \rceil O(h) = O(n)$ (at most $2n$ comparisons).
- **Finding $k$-th Smallest in Min-Heap** (or Max in Min-Heap):
  - Maximum element in a Min-Heap must be one of the $\lceil n/2 \rceil$ **leaves** $\implies \Theta(n)$ time.

### 2.5 Hashing & Collision Resolution
- **Load Factor**: $\alpha = \frac{n}{m}$ ($n =$ keys, $m =$ slots).
- **Expected Probes (Uniform Hashing)**:
  - **Chaining**: Unsuccessful $= 1 + \alpha$; Successful $= 1 + \frac{\alpha}{2}$.
  - **Open Addressing (Uniform Probing)**: Unsuccessful $= \frac{1}{1-\alpha}$; Successful $= \frac{1}{\alpha}\ln\left(\frac{1}{1-\alpha}\right)$.
  - **Linear Probing**: $h(k, i) = (h'(k) + i) \bmod m$ — suffers from **Primary Clustering**.
  - **Quadratic Probing**: $h(k, i) = (h'(k) + c_1 i + c_2 i^2) \bmod m$ — suffers from **Secondary Clustering**.
  - **Double Hashing**: $h(k, i) = (h_1(k) + i \cdot h_2(k)) \bmod m$ (requires $\gcd(h_2(k), m) = 1$).

---

## 3. Original PDF Chapter Notes (Preserved Verbatim)

3 Programming and DS: Data Structures (238)
Webpage
Stacks, Queues, Linked lists, Trees, Binary search trees, Binary heaps, Graphs.
Welcome to the "Programming and Data Structures: Data Structures" chapter, a cornerstone of the GATE Computer
Science syllabus. This subject is fundamental to understanding how data is organized, stored, and manipulated
efficiently, which is crucial for designing optimal algorithms and software systems. For GATE CS, Data Structures
typically carries a significant weightage, often contributing 8-12 marks, sometimes more, through a mix of Multiple
Choice Questions (MCQs) and Numerical Answer Type (NAT) questions. Questions frequently test your understanding
of core concepts, time and space complexity analysis of operations, properties of various data structures, and their
applications in problem-solving. Expect problems involving tracing operations on specific data structures like AVL trees
or heaps, analyzing the complexity of given code snippets, or determining the output of tree traversals.
Topic-wise Key Concepts
AVL Tree
An AVL tree is a self-balancing Binary Search Tree (BST) where the difference between the heights of the left and right
subtrees for any node is at most 1. This strict balance ensures that the tree remains relatively balanced, preventing
worst-case scenarios of skewed BSTs.
Balance Factor: For any node ,
. In an AVL tree,
.
Rotations: When an insertion or deletion causes a node to become unbalanced (balance factor becomes ),
rotations are performed to restore balance. There are four types of rotations:
1. LL Rotation (Left-Left): Occurs when an insertion into the left subtree of the left child causes imbalance. A
single right rotation is performed.
2. RR Rotation (Right-Right): Occurs when an insertion into the right subtree of the right child causes imbalance.
A single left rotation is performed.
3. LR Rotation (Left-Right): Occurs when an insertion into the right subtree of the left child causes imbalance. A
left rotation on the child, followed by a right rotation on the parent.
4. RL Rotation (Right-Left): Occurs when an insertion into the left subtree of the right child causes imbalance. A
right rotation on the child, followed by a left rotation on the parent.
Height of an AVL Tree: For an AVL tree with nodes, its height is always . Specifically,
.
Time Complexity: Insertion, deletion, and search operations all take balanced nature.
time in the worst case due to the
Common Pitfalls: Incorrectly identifying the type of rotation needed, especially for LR and RL cases. Forgetting to
update heights and balance factors after rotations. Tracing rotations correctly requires careful step-by-step analysis.
Problem-Solving Techniques: Practice tracing insertions/deletions and the subsequent rotations on small example
AVL trees. Understand the pivot node and the child involved in the imbalance.
Abstract Data Type (ADT)
An Abstract Data Type (ADT) is a mathematical model for data types, defining the data stored and the operations that
can be performed on it, without specifying how these operations are implemented. It focuses on "what" an operation
does rather than "how" it does it.
Key Properties:
Abstraction: Hides the internal implementation details from the user.
Encapsulation: Bundles data and methods that operate on the data into a single unit.
Examples: Stack, Queue, List, Priority Queue, Map, Set are all ADTs. A data structure (e.g., array, linked list) is a

*(PDF Page 190)*

concrete implementation of an ADT.
Common Pitfalls: Confusing an ADT with a data structure. An ADT is a logical concept, while a data structure is a
physical implementation.
Problem-Solving Techniques: Identify the core operations and their logical behavior when asked to define or
recognize an ADT.
Array
An array is a collection of elements of the same data type, stored in contiguous memory locations. Elements are
accessed using an integer index.
Address Calculation (1D Array): For an array bound :
starting at , with elements of size , and lower
If , then .
Address Calculation (2D Array - Row-Major Order): For an array , with element size , and lower bounds :
(R rows, C columns), starting at
If , then .
Address Calculation (2D Array - Column-Major Order): For an array , starting at element size , and lower bounds :
, with
If , then .
Time Complexity:
Accessing an element:
Insertion/Deletion at end: (if space available)
Insertion/Deletion at beginning/middle: (requires shifting elements)
Common Pitfalls: Off-by-one errors in index calculations, especially with non-zero lower bounds. Confusing row-major
with column-major order.
Problem-Solving Techniques: Carefully apply the address calculation formulas. Understand the memory layout for
multi-dimensional arrays.
Binary Heap
A binary heap is a complete binary tree that satisfies the heap property: for a min-heap, every parent node's value is
less than or equal to its children's values; for a max-heap, every parent node's value is greater than or equal to its
children's values. Heaps are typically implemented using an array.
Array Representation (0-indexed):
Parent of node at index :
Left child of node at index :
Right child of node at index :
Heap Properties:
Completeness: All levels are completely filled except possibly the last level, which is filled from left to right.
Heap Property: (Min-heap or Max-heap)
Time Complexity:
Insert: (heapify-up)
Delete-min/max (extract-root): (heapify-down)
Build Heap from an array of elements:
Search: (Heaps are not designed for efficient search of arbitrary elements)
Common Pitfalls: Violating the completeness property. Incorrectly applying heapify-up or heapify-down logic.
Confusing min-heap and max-heap properties.

*(PDF Page 191)*

Problem-Solving Techniques: Trace heap operations (insert, delete) step-by-step. For building a heap, start from the
last non-leaf node and perform heapify-down upwards.
Binary Search Tree (BST)
A Binary Search Tree (BST) is a binary tree where for every node, all values in its left subtree are less than the node's
value, and all values in its right subtree are greater than the node's value. Duplicate values are typically not allowed or
handled specifically (e.g., placed in the right subtree).
BST Properties:
Left subtree values Root value
Right subtree values Root value
Both left and right subtrees are also BSTs.
Inorder traversal of a BST yields elements in sorted order.
Time Complexity (Average Case):
Search, Insertion, Deletion:
Time Complexity (Worst Case - Skewed Tree):
Search, Insertion, Deletion: (occurs when elements are inserted in sorted or reverse-sorted order, leading
to a linked list-like structure)
Deletion Cases:
1. Node to be deleted is a leaf: Simply remove it.
2. Node has one child: Replace the node with its child.
3. Node has two children: Replace the node's value with its inorder predecessor (largest in left subtree) or inorder
successor (smallest in right subtree), then delete the predecessor/successor node (which will have 0 or 1 child).
Common Pitfalls: Forgetting the worst-case complexity for skewed trees. Incorrectly handling deletion of nodes
with two children. Not understanding that inorder traversal is key to sorted output.
Problem-Solving Techniques: Practice constructing BSTs and performing deletions. Understand the recursive nature
of BST operations.
Binary Tree
A binary tree is a tree data structure in which each node has at most two children, referred to as the left child and the
right child.
Key Properties:
Full Binary Tree: Every node has either 0 or 2 children.
Complete Binary Tree: All levels are completely filled except possibly the last level, which is filled from left to
right.
Perfect Binary Tree: All internal nodes have two children, and all leaf nodes are at the same level. (A perfect
binary tree is always full and complete).
Skewed Binary Tree: All nodes have only one child (either left or right), resembling a linked list.
Formulas:
Maximum number of nodes at level (root at level 0):
Maximum number of nodes in a binary tree of height (max levels Minimum height of a binary tree with nodes: ):
or (for complete binary tree)
Number of leaf nodes and internal nodes in a full binary tree:
Common Pitfalls: Confusing the definitions of full, complete, and perfect binary trees. Miscalculating height or number
of nodes.
of the tree type.
Problem-Solving Techniques: Draw examples to visualize properties. Apply formulas carefully based on the definition
Data Structures
Data structures are specialized formats for organizing and storing data in a computer so that it can be accessed and
modified efficiently. They provide a means to manage large amounts of data effectively for various applications.
Classification:
Primitive vs. Non-Primitive: Primitive (int, char, float), Non-Primitive (Arrays, Linked Lists, Trees, Graphs).
Linear vs. Non-Linear: Linear (Arrays, Linked Lists, Stacks, Queues), Non-Linear (Trees, Graphs).

*(PDF Page 192)*

Static vs. Dynamic: Static (fixed size at compile time, e.g., arrays), Dynamic (size can change at runtime, e.g.,
linked lists).
complexity).
Importance: Choosing the right data structure is critical for optimal algorithm performance (time and space
Common Pitfalls: Not understanding the trade-offs between different data structures (e.g., array vs. linked list for
insertion/deletion).
Problem-Solving Techniques: Analyze problem requirements (e.g., frequent insertions, fast searches, memory
constraints) to select the most appropriate data structure.
Hashing
Hashing is a technique used to map keys to array indices (hash table slots) for efficient data storage and retrieval. A
hash function computes an index for a given key .
Hash Functions:
Division Method: to a power of 2).
, where is the size of the hash table (often a prime number not close
Multiplication Method: , where is a constant (e.g.,
).
Mid-Square Method: Square the key, then extract some middle digits.
Folding Method: Divide the key into parts, then combine them (e.g., add them).
Collision Resolution Techniques: When two different keys map to the same index.
Chaining: Each hash table slot points to a linked list of all keys that hash to that slot.
Average case for search/insert/delete: , where is the load factor.
Worst case: if all keys hash to the same slot.
Open Addressing: All elements are stored directly in the hash table. When a collision occurs, probe for an
alternative empty slot.
Quadratic Probing: Linear Probing: , where . Suffers from primary clustering.
. Reduces primary clustering but can suffer
from secondary clustering.
Double Hashing: . Uses two hash functions to generate probe
sequences, reducing clustering.
Load Factor ( ): , where is the number of elements and is the table size.
For chaining: can be greater than 1.
For open addressing: .
Common Pitfalls: Choosing a non-prime table size for division method. Incorrectly applying probing sequences.
Understanding the difference between primary and secondary clustering.
Problem-Solving Techniques: Trace insertions and searches with given hash functions and collision resolution
strategies. Calculate load factor and analyze performance implications.
Infix, Prefix, Postfix Notations
These are different ways to write arithmetic expressions, differing in the position of operators relative to their operands.
Infix Notation: Operator is between operands (e.g., ). This is the human-readable form.
Prefix Notation (Polish Notation): Operator precedes its operands (e.g., ).
Postfix Notation (Reverse Polish Notation): Operator follows its operands (e.g., ).
Properties: Prefix and Postfix notations do not require parentheses to define operator precedence or associativity,
making them unambiguous for computer evaluation.
Conversion Rules:
Infix to Postfix/Prefix: Typically uses a stack. Operators are pushed onto the stack based on precedence and
associativity. Operands are directly appended to the output.
Evaluation of Postfix/Prefix: Also uses a stack. For postfix, operands are pushed; when an operator is
encountered, pop two operands, perform the operation, and push the result. For prefix, scan from right to left.
Common Pitfalls: Incorrectly handling operator precedence and associativity during conversions. Mistakes in stack
operations (push/pop order).
Problem-Solving Techniques: Practice conversions using the stack-based algorithms. Remember operator

*(PDF Page 193)*

precedence (e.g., ) and associativity (most are left-associative, exponentiation is right-associative).
Linked List
A linked list is a linear data structure where elements are not stored in contiguous memory locations. Instead, each
element (node) contains data and a pointer (or link) to the next node in the sequence.
Types of Linked Lists:
Singly Linked List: Each node points to the next node. Traversal is unidirectional.
Doubly Linked List: Each node has pointers to both the next and previous nodes. Traversal is bidirectional.
Circular Linked List: The last node points back to the first node (or head). Can be singly or doubly circular.
Time Complexity:
Insertion/Deletion at beginning:
Insertion/Deletion at end: for singly linked list (requires traversal), if tail pointer is maintained.
for doubly linked list if tail pointer is maintained.
Insertion/Deletion at specific position: (requires traversal to find position)
Search:
Advantages: Dynamic size, efficient insertions/deletions at specific points (if pointer to previous node is available).
Disadvantages: More memory overhead (for pointers), no random access ( for access).
Common Pitfalls: Null pointer exceptions when traversing or manipulating the list. Incorrectly updating pointers during
insertion/deletion, leading to lost nodes or broken links. Handling edge cases like empty list or single-node list.
Problem-Solving Techniques: Draw diagrams to visualize pointer changes. Pay close attention to the order of pointer
updates. Always check for null pointers.
Priority Queue
A Priority Queue is an Abstract Data Type (ADT) that functions like a queue but with an additional concept of "priority.
"
Elements are retrieved based on their priority, not necessarily their insertion order. The element with the highest (or
lowest) priority is always dequeued first.
Core Operations:
Insert (enqueue): Adds an element with a given priority.
Extract-Min/Max (dequeue): Removes and returns the element with the highest (or lowest) priority.
Peek: Returns the highest (or lowest) priority element without removing it.
Implementations:
Binary Heap: Most efficient implementation, providing for insert and extract-min/max.
Unsorted Array/Linked List: insert, extract-min/max.
Sorted Array/Linked List: insert, extract-min/max.
Common Pitfalls: Confusing a priority queue with a regular queue. Not understanding that the underlying data
structure (e.g., heap) determines the complexity.
Problem-Solving Techniques: When a problem requires always processing the "most important" item next, a priority
queue (implemented with a heap) is often the solution.
Queue
A Queue is a linear Abstract Data Type (ADT) that follows the First-In, First-Out (FIFO) principle. Elements are added at
one end (rear/tail) and removed from the other end (front/head).
Core Operations:
Enqueue: Adds an element to the rear of the queue.
Dequeue: Removes and returns the element from the front of the queue.
Front/Peek: Returns the element at the front without removing it.
IsEmpty, IsFull: Checks the state of the queue.
Implementations:
Array-based: Can lead to "queue full" even if space is available (linear array). Circular array implementation
solves this.
Linked List-based: More dynamic, no fixed size issues.
Time Complexity (Array or Linked List): All core operations (enqueue, dequeue, front) are .

*(PDF Page 194)*

Common Pitfalls: Underflow (dequeuing from an empty queue) and Overflow (enqueuing into a full array-based
queue). Incorrectly managing front and rear pointers in array implementations, especially circular queues.
Problem-Solving Techniques: Trace operations carefully. Understand how front and rear pointers move. For circular
queues, remember the modulus operator for index calculations: .
Stack
A Stack is a linear Abstract Data Type (ADT) that follows the Last-In, First-Out (LIFO) principle. Elements are added
and removed only from one end, called the "top.
"
Core Operations:
Push: Adds an element to the top of the stack.
Pop: Removes and returns the element from the top of the stack.
Peek/Top: Returns the element at the top without removing it.
IsEmpty, IsFull: Checks the state of the stack.
Implementations:
Array-based: Uses a fixed-size array and a top pointer/index.
Linked List-based: Each node points to the next, with the head of the list being the top of the stack.
Time Complexity (Array or Linked List): All core operations (push, pop, peek) are .
Applications: Function call stack, expression evaluation (infix to postfix/prefix conversion), undo/redo functionality,
backtracking algorithms.
Common Pitfalls: Underflow (popping from an empty stack) and Overflow (pushing into a full array-based stack).
Incorrectly managing the top pointer/index.
Problem-Solving Techniques: Trace stack operations. Recognize problems that naturally fit the LIFO principle (e.g.,
reversing a sequence, checking parenthesis balance).
Time Complexity
Time complexity measures the amount of time an algorithm takes to run as a function of the input size ( ). It's typically
expressed using asymptotic notations to describe the growth rate for large .
Asymptotic Notations:
Big-O Notation ( ): Upper bound. for all Big-Omega Notation ( ): Lower bound. for all Big-Theta Notation ( ): Tight bound. if there exist positive constants and such that
. Describes the worst-case time.
. Describes the best-case time.
if there exist positive constants and such that
if there exist positive constants and such that
for all . Describes average-case time or when best and worst cases
are the same.
Little-o Notation ( ): Strict upper bound. if .
Little-omega Notation ( ): Strict lower bound. if .
Common Growth Rates (from fastest to slowest):
Master Theorem for Recurrence Relations: For recurrences of the form , where
are constants, and is an asymptotically positive function:
1. If for some constant , then .
2. If , then .
3. If for some constant , AND if for some constant and all
sufficiently large , then .
Common Pitfalls: Ignoring constant factors or lower-order terms (which are dropped in asymptotic analysis). Confusing
best, worst, and average case complexities. Incorrectly applying Master Theorem conditions.
Problem-Solving Techniques: Analyze loops (number of iterations). For recursive functions, set up recurrence
relations and solve them (often using Master Theorem or substitution method). Identify the dominant term in a sum of
complexities.

*(PDF Page 195)*

Tree
A tree is a non-linear, hierarchical data structure consisting of nodes connected by edges. It is a connected acyclic
graph, meaning there are no cycles and all nodes are reachable from the root.
Key Terminology:
Root: The topmost node of the tree.
Parent: A node that has one or more child nodes.
Child: A node directly connected to another node when moving away from the root.
Sibling: Nodes that share the same parent.
Leaf Node (External Node): A node with no children.
Internal Node: A node with at least one child.
Ancestors: All nodes on the path from the root to a node.
Descendants: All nodes in the subtree rooted at a node.
Depth: The length of the path from the root to a node (root is at depth 0).
Height: The length of the longest path from a node to a leaf. The height of the tree is the height of its root.
Degree of a Node: Number of children it has.
Degree of a Tree: Maximum degree of any node in the tree.
Properties:
A tree with nodes has exactly edges.
There is a unique path between any two nodes in a tree.
Common Pitfalls: Confusing tree terminology (e.g., depth vs. height, parent vs. child). Forgetting the edges
property.
Problem-Solving Techniques: Draw trees to visualize concepts. Understand recursive definitions for tree operations.
Tree Traversal
Tree traversal refers to the process of visiting each node in a tree exactly once in a systematic way. There are two main
categories: Depth-First Search (DFS) and Breadth-First Search (BFS).
Depth-First Search (DFS) Traversal: Uses a stack (implicitly via recursion) to explore as far as possible along
each branch before backtracking.
Inorder Traversal (Left, Root, Right): Visits the left subtree, then the root, then the right subtree. For BSTs, this
yields sorted elements.
Preorder Traversal (Root, Left, Right): Visits the root, then the left subtree, then the right subtree. Useful for
creating a copy of the tree.
Postorder Traversal (Left, Right, Root): Visits the left subtree, then the right subtree, then the root. Useful for
deleting a tree (deletes children before parent).
Breadth-First Search (BFS) Traversal (Level Order Traversal): Visits nodes level by level, from left to right. Uses
a queue.
Starts at the root, then visits all nodes at depth 1, then all nodes at depth 2, and so on.
Common Pitfalls: Incorrectly applying the order of visits for DFS traversals. Difficulty in reconstructing a tree from given
traversals (e.g., Inorder + Preorder can reconstruct a unique BST).
Problem-Solving Techniques: Practice tracing all four traversal types on various trees. Remember the specific order
for each. For tree reconstruction, use one traversal (e.g., Preorder) to find the root, then use another (e.g., Inorder) to
partition the remaining elements into left and right subtrees.
Uniform Hashing
Uniform Hashing is an idealized assumption used in the analysis of hashing algorithms. It states that each key is
equally likely to hash to any slot in the hash table, independently of where other keys hash.
Key Property: If we have keys and slots, the probability that a key hashes to any particular slot is .
Implications:
Minimizes collisions in theory.
Leads to the best possible average-case performance for hash tables.
Under simple uniform hashing, the expected length of a chain in chaining is .
Under uniform hashing, the expected number of probes for unsuccessful search in open addressing is
.

*(PDF Page 196)*

Common Pitfalls: Assuming uniform hashing holds true in practice. Real-world hash functions are rarely perfectly
uniform, leading to deviations from theoretical performance.
Problem-Solving Techniques: Understand that uniform hashing is a theoretical model for analyzing the average-case
performance of hashing. Use its properties to calculate expected values related to collisions or probes.
Quick Formula Reference
Topic Formula/Concept
Balance Factor:
Height:
AVL Tree
Array (1D)
Array (2D - Row-Major)
Array (2D - Column-Major)
Binary Heap (0-indexed)
Binary Tree
Parent of :
Left child of :
Right child of :
Max nodes at level :
Max nodes in height tree:
Min height for nodes: (complete tree)
Full Binary Tree:
Hashing (Division)
Hashing (Multiplication)
Hashing (Linear Probing)
Hashing (Quadratic Probing)
Hashing (Double Hashing)
Hashing (Load Factor)
Time Complexity (Big-O) if for
Time Complexity (Big-Omega) if for
Time Complexity (Big-Theta) for
Master Theorem (Case 1) If , then
Master Theorem (Case 2) If , then
Master Theorem (Case 3) If and , then
Tree (General) nodes, edges
Important Tips for GATE
Master Time & Space Complexity: This is arguably the most crucial aspect. Be able to analyze the complexity of
operations on all data structures and for given code snippets. Understand best, worst, and average cases. Practice
applying the Master Theorem rigorously.
Understand ADT vs. Data Structure: Clearly differentiate between the abstract concept (ADT) and its concrete
implementation (data structure). For example, a Stack is an ADT, while an array-based stack or linked-list based
stack are data structures implementing the Stack ADT.
Visualize Operations: For tree-based structures (AVL, BST, Heap) and linked lists, always draw diagrams and
trace operations step-by-step. This helps catch errors in pointer manipulation, rotations, or heapify processes.
Practice Tree Traversals: Be proficient in Inorder, Preorder, Postorder, and Level-order traversals. Understand
their applications and how to reconstruct a tree from given traversals (e.g., Preorder + Inorder).
Hashing Concepts are Key: Pay close attention to different hash functions, collision resolution techniques
(chaining, linear probing, quadratic probing, double hashing), and their impact on performance (load factor,
clustering). Be ready to trace insertions and searches.
Know Standard Implementations: Understand how basic ADTs like Stack and Queue are implemented using
arrays and linked lists, including edge cases like underflow/overflow and circular array logic.
Identify Common Pitfalls: Be aware of typical mistakes like off-by-one errors in array indexing, null pointer
exceptions in linked lists, incorrect balance factor calculations in AVL trees, or misinterpreting operator precedence
in expression conversions.
Practice Problem-Solving: Data structures questions are often application-oriented. Practice a wide variety of
problems to recognize when to use a particular data structure and how to apply its operations to solve the problem

*(PDF Page 197)*

efficiently.

---

## 4. Complete Question Index & Answer Key Record (238 Questions)

| Q # | Question Source / Title | Answer Key |
| :---: | :--- | :---: |
| `3.1.1` | AVL Tree: GATE CSE 1988 \| Question: 7ii | **N/A** |
| `3.1.2` | AVL Tree: GATE CSE 1996 \| Question: 1.14 | **B** |
| `3.1.3` | AVL Tree: GATE CSE 1998 \| Question: 21 | **N/A** |
| `3.1.4` | AVL Tree: GATE CSE 2009 \| Question: 37,ISRO-DEC2017-55 | **B** |
| `3.1.5` | AVL Tree: GATE CSE 2020 \| Question: 6 | **C** |
| `3.1.6` | AVL Tree: GATE IT 2008 \| Question: 12 | **A** |
| `3.2.1` | Abstract Data Type: GATE CSE 2005 \| Question: 2 | **C** |
| `3.3.1` | Array: GATE CSE 1993 \| Question: 12 | **N/A** |
| `3.3.2` | Array: GATE CSE 1994 \| Question: 1.11 | **C** |
| `3.3.3` | Array: GATE CSE 1994 \| Question: 25 | **N/A** |
| `3.3.4` | Array: GATE CSE 1997 \| Question: 17 | **N/A** |
| `3.3.5` | Array: GATE CSE 1998 \| Question: 2.14 | **A** |
| `3.3.6` | Array: GATE CSE 2000 \| Question: 1.2 | **A** |
| `3.3.7` | Array: GATE CSE 2000 \| Question: 15 | **N/A** |
| `3.3.8` | Array: GATE CSE 2005 \| Question: 5 | **A** |
| `3.3.9` | Array: GATE CSE 2013 \| Question: 50 | **B** |
| `3.3.10` | Array: GATE CSE 2013 \| Question: 51 | **C** |
| `3.3.11` | Array: GATE CSE 2014 \| Set 3 \| Question: 42 | **B** |
| `3.3.12` | Array: GATE CSE 2015 \| Set 2 \| Question: 31 | **5** |
| `3.3.13` | Array: GATE CSE 2021 \| Set 1 \| Question: 2 | **C** |
| `3.4.1` | Binary Heap: GATE CSE 1990 \| Question: 2-viii | **N/A** |
| `3.4.2` | Binary Heap: GATE CSE 1996 \| Question: 2.11 | **C** |
| `3.4.3` | Binary Heap: GATE CSE 1999 \| Question: 12 | **N/A** |
| `3.4.4` | Binary Heap: GATE CSE 2001 \| Question: 1.15 | **B** |
| `3.4.5` | Binary Heap: GATE CSE 2003 \| Question: 23 | **D** |
| `3.4.6` | Binary Heap: GATE CSE 2004 \| Question: 37 | **A** |
| `3.4.7` | Binary Heap: GATE CSE 2005 \| Question: 34 | **D** |
| `3.4.8` | Binary Heap: GATE CSE 2006 \| Question: 10 | **A** |
| `3.4.9` | Binary Heap: GATE CSE 2006 \| Question: 76 | **D** |
| `3.4.10` | Binary Heap: GATE CSE 2006 \| Question: 77 | **A** |
| `3.4.11` | Binary Heap: GATE CSE 2007 \| Question: 47 | **B** |
| `3.4.12` | Binary Heap: GATE CSE 2009 \| Question: 59 | **C** |
| `3.4.13` | Binary Heap: GATE CSE 2009 \| Question: 60 | **D** |
| `3.4.14` | Binary Heap: GATE CSE 2011 \| Question: 23 | **B** |
| `3.4.15` | Binary Heap: GATE CSE 2014 \| Set 2 \| Question: 12 | **A** |
| `3.4.16` | Binary Heap: GATE CSE 2015 \| Set 1 \| Question: 32 | **B** |
| `3.4.17` | Binary Heap: GATE CSE 2015 \| Set 2 \| Question: 17 | **A** |
| `3.4.18` | Binary Heap: GATE CSE 2015 \| Set 3 \| Question: 19 | **D** |
| `3.4.19` | Binary Heap: GATE CSE 2016 \| Set 1 \| Question: 37 | **B** |
| `3.4.20` | Binary Heap: GATE CSE 2016 \| Set 2 \| Question: 34 | **8** |
| `3.4.21` | Binary Heap: GATE CSE 2018 \| Question: 46 | **80** |
| `3.4.22` | Binary Heap: GATE CSE 2019 \| Question: 40 | **A** |
| `3.4.23` | Binary Heap: GATE CSE 2020 \| Question: 47 | **511** |
| `3.4.24` | Binary Heap: GATE CSE 2021 \| Set 2 \| Question: 2 | **C** |
| `3.4.25` | Binary Heap: GATE CSE 2023 \| Question: 2 | **B** |
| `3.4.26` | Binary Heap: GATE CSE 2024 \| Set 1 \| Question: 33 | **A** |
| `3.4.27` | Binary Heap: GATE CSE 2025 \| Set 1 \| Question: 25 | **5:5** |
| `3.4.28` | Binary Heap: GATE IT 2004 \| Question: 53 | **B** |
| `3.4.29` | Binary Heap: GATE IT 2006 \| Question: 44 | **C** |
| `3.4.30` | Binary Heap: GATE IT 2006 \| Question: 72 | **B** |
| `3.5.1` | Binary Search Tree: GATE CSE 1996 \| Question: 2.14 | **B** |
| `3.5.2` | Binary Search Tree: GATE CSE 1996 \| Question: 4 | **N/A** |
| `3.5.3` | Binary Search Tree: GATE CSE 1997 \| Question: 4.5 | **D** |
| `3.5.4` | Binary Search Tree: GATE CSE 2001 \| Question: 14 | **N/A** |
| `3.5.5` | Binary Search Tree: GATE CSE 2003 \| Question: 19, ISRO2009-24 | **C** |
| `3.5.6` | Binary Search Tree: GATE CSE 2003 \| Question: 6 | **B** |
| `3.5.7` | Binary Search Tree: GATE CSE 2003 \| Question: 63, ISRO2009-25 | **B** |
| `3.5.8` | Binary Search Tree: GATE CSE 2004 \| Question: 4, ISRO2009-26 | **B** |
| `3.5.9` | Binary Search Tree: GATE CSE 2004 \| Question: 85 | **B** |
| `3.5.10` | Binary Search Tree: GATE CSE 2005 \| Question: 33 | **A** |
| `3.5.11` | Binary Search Tree: GATE CSE 2005 \| Question: 35 | **B** |
| `3.5.12` | Binary Search Tree: GATE CSE 2008 \| Question: 46 | **B** |
| `3.5.13` | Binary Search Tree: GATE CSE 2012 \| Question: 5 | **C** |
| `3.5.14` | Binary Search Tree: GATE CSE 2013 \| Question: 43 | **D** |
| `3.5.15` | Binary Search Tree: GATE CSE 2013 \| Question: 7 | **C** |
| `3.5.16` | Binary Search Tree: GATE CSE 2014 \| Set 3 \| Question: 39 | **110** |
| `3.5.17` | Binary Search Tree: GATE CSE 2015 \| Set 1 \| Question: 10 | **A** |
| `3.5.18` | Binary Search Tree: GATE CSE 2015 \| Set 1 \| Question: 23 | **B** |
| `3.5.19` | Binary Search Tree: GATE CSE 2015 \| Set 3 \| Question: 13 | **B** |
| `3.5.20` | Binary Search Tree: GATE CSE 2016 \| Set 2 \| Question: 40 | **64** |
| `3.5.21` | Binary Search Tree: GATE CSE 2017 \| Set 1 \| Question: 6 | **B** |
| `3.5.22` | Binary Search Tree: GATE CSE 2017 \| Set 2 \| Question: 36 | **B** |
| `3.5.23` | Binary Search Tree: GATE CSE 2020 \| Question: 41 | **B** |
| `3.5.24` | Binary Search Tree: GATE CSE 2020 \| Question: 5 | **B** |
| `3.5.25` | Binary Search Tree: GATE CSE 2021 \| Set 1 \| Question: 10 | **D** |
| `3.5.26` | Binary Search Tree: GATE CSE 2022 \| Question: 18 | **509** |
| `3.5.27` | Binary Search Tree: GATE CSE 2024 \| Set 2 \| Question: 29 | **A** |
| `3.5.28` | Binary Search Tree: GATE CSE 2025 \| Set 1 \| Question: 16 | **A;B** |
| `3.5.29` | Binary Search Tree: GATE CSE 2025 \| Set 2 \| Question: 25 | **4:4** |
| `3.5.30` | Binary Search Tree: GATE IT 2005 \| Question: 12 | **C** |
| `3.5.31` | Binary Search Tree: GATE IT 2005 \| Question: 55 | **D** |
| `3.5.32` | Binary Search Tree: GATE IT 2006 \| Question: 45 | **C** |
| `3.5.33` | Binary Search Tree: GATE IT 2007 \| Question: 29 | **A** |
| `3.5.34` | Binary Search Tree: GATE IT 2008 \| Question: 71 | **D** |
| `3.5.35` | Binary Search Tree: GATE IT 2008 \| Question: 72 | **C** |
| `3.5.36` | Binary Search Tree: GATE IT 2008 \| Question: 73 | **B** |
| `3.6.1` | Binary Tree: GATE CSE 1987 \| Question: 2c | **False** |
| `3.6.2` | Binary Tree: GATE CSE 1987 \| Question: 2g | **False** |
| `3.6.3` | Binary Tree: GATE CSE 1987 \| Question: 7b | **N/A** |
| `3.6.4` | Binary Tree: GATE CSE 1988 \| Question: 7i | **N/A** |
| `3.6.5` | Binary Tree: GATE CSE 1988 \| Question: 7iii | **N/A** |
| `3.6.6` | Binary Tree: GATE CSE 1989 \| Question: 3-ixa | **A;C;D** |
| `3.6.7` | Binary Tree: GATE CSE 1990 \| Question: 3-iv | **B** |
| `3.6.8` | Binary Tree: GATE CSE 1991 \| Question: 01,viii | **144** |
| `3.6.9` | Binary Tree: GATE CSE 1991 \| Question: 1,ix | **N/A** |
| `3.6.10` | Binary Tree: GATE CSE 1991 \| Question: 14,a | **N/A** |
| `3.6.11` | Binary Tree: GATE CSE 1991 \| Question: 14,b | **N/A** |
| `3.6.12` | Binary Tree: GATE CSE 1991 \| Question: 14,c | **N/A** |
| `3.6.13` | Binary Tree: GATE CSE 1993 \| Question: 16 | **N/A** |
| `3.6.14` | Binary Tree: GATE CSE 1994 \| Question: 8 | **N/A** |
| `3.6.15` | Binary Tree: GATE CSE 1995 \| Question: 1.17 | **B** |
| `3.6.16` | Binary Tree: GATE CSE 1995 \| Question: 6 | **N/A** |
| `3.6.17` | Binary Tree: GATE CSE 1996 \| Question: 1.15 | **C** |
| `3.6.18` | Binary Tree: GATE CSE 1997 \| Question: 16 | **N/A** |
| `3.6.19` | Binary Tree: GATE CSE 1998 \| Question: 20 | **N/A** |
| `3.6.20` | Binary Tree: GATE CSE 2000 \| Question: 1.14 | **C** |
| `3.6.21` | Binary Tree: GATE CSE 2000 \| Question: 2.16 | **D** |
| `3.6.22` | Binary Tree: GATE CSE 2002 \| Question: 2.12 | **D** |
| `3.6.23` | Binary Tree: GATE CSE 2002 \| Question: 6 | **N/A** |
| `3.6.24` | Binary Tree: GATE CSE 2004 \| Question: 35 | **B** |
| `3.6.25` | Binary Tree: GATE CSE 2004 \| Question: 43 | **D** |
| `3.6.26` | Binary Tree: GATE CSE 2006 \| Question: 13 | **D** |
| `3.6.27` | Binary Tree: GATE CSE 2007 \| Question: 12 | **C** |
| `3.6.28` | Binary Tree: GATE CSE 2007 \| Question: 13 | **B** |
| `3.6.29` | Binary Tree: GATE CSE 2007 \| Question: 39, UGCNET-June2015-II: 22 | **A** |
| `3.6.30` | Binary Tree: GATE CSE 2007 \| Question: 46 | **C** |
| `3.6.31` | Binary Tree: GATE CSE 2010 \| Question: 10 | **A** |
| `3.6.32` | Binary Tree: GATE CSE 2011 \| Question: 29 | **B** |
| `3.6.33` | Binary Tree: GATE CSE 2012 \| Question: 47 | **A** |
| `3.6.34` | Binary Tree: GATE CSE 2014 \| Set 1 \| Question: 12 | **1** |
| `3.6.35` | Binary Tree: GATE CSE 2015 \| Set 1 \| Question: 25 | **A** |
| `3.6.36` | Binary Tree: GATE CSE 2015 \| Set 2 \| Question: 10 | **19** |
| `3.6.37` | Binary Tree: GATE CSE 2015 \| Set 3 \| Question: 25 | **199** |
| `3.6.38` | Binary Tree: GATE CSE 2016 \| Set 2 \| Question: 36 | **C** |
| `3.6.39` | Binary Tree: GATE CSE 2018 \| Question: 20 | **4** |
| `3.6.40` | Binary Tree: GATE CSE 2019 \| Question: 46 | **4.25** |
| `3.6.41` | Binary Tree: GATE CSE 2021 \| Set 2 \| Question: 16 | **1** |
| `3.6.42` | Binary Tree: GATE CSE 2023 \| Question: 37 | **C** |
| `3.6.43` | Binary Tree: GATE CSE 2025 \| Set 2 \| Question: 3 | **B** |
| `3.6.44` | Binary Tree: GATE DS&AI 2024 \| Question: 18 | **A;B;C** |
| `3.6.45` | Binary Tree: GATE DS&AI 2024 \| Question: 42 | **A;B;C** |
| `3.6.46` | Binary Tree: GATE IT 2004 \| Question: 54 | **D** |
| `3.6.47` | Binary Tree: GATE IT 2005 \| Question: 50 | **B** |
| `3.6.48` | Binary Tree: GATE IT 2006 \| Question: 71 | **D** |
| `3.6.49` | Binary Tree: GATE IT 2006 \| Question: 73 | **C** |
| `3.6.50` | Binary Tree: GATE IT 2006 \| Question: 9 | **B** |
| `3.6.51` | Binary Tree: GATE IT 2008 \| Question: 46 | **D** |
| `3.6.52` | Binary Tree: GATE IT 2008 \| Question: 76 | **B** |
| `3.6.53` | Binary Tree: GATE IT 2008 \| Question: 77 | **A** |
| `3.7.1` | Data Structures: GATE CSE 1997 \| Question: 6.2 | **B** |
| `3.7.2` | Data Structures: GATE CSE 2014 \| Set 1 \| Question: 3 | **B** |
| `3.7.3` | Data Structures: GATE CSE 2016 \| Set 1 \| Question: 38 | **12** |
| `3.7.4` | Data Structures: GATE DS&AI 2024 \| Question: 6 | **A** |
| `3.8.1` | Hashing: GATE CSE 1996 \| Question: 1.13 | **C** |
| `3.8.2` | Hashing: GATE CSE 1996 \| Question: 15 | **N/A** |
| `3.8.3` | Hashing: GATE CSE 1997 \| Question: 12 | **N/A** |
| `3.8.4` | Hashing: GATE CSE 2004 \| Question: 7 | **C** |
| `3.8.5` | Hashing: GATE CSE 2007 \| Question: 40 | **B** |
| `3.8.6` | Hashing: GATE CSE 2009 \| Question: 36 | **C** |
| `3.8.7` | Hashing: GATE CSE 2010 \| Question: 52 | **C** |
| `3.8.8` | Hashing: GATE CSE 2010 \| Question: 53 | **C** |
| `3.8.9` | Hashing: GATE CSE 2014 \| Set 1 \| Question: 40 | **A** |
| `3.8.10` | Hashing: GATE CSE 2014 \| Set 3 \| Question: 40 | **A** |
| `3.8.11` | Hashing: GATE CSE 2015 \| Set 2 \| Question: 33 | **B** |
| `3.8.12` | Hashing: GATE CSE 2015 \| Set 3 \| Question: 17 | **80** |
| `3.8.13` | Hashing: GATE IT 2006 \| Question: 20 | **C** |
| `3.8.14` | Hashing: GATE IT 2007 \| Question: 28 | **B** |
| `3.8.15` | Hashing: GATE IT 2008 \| Question: 48 | **D** |
| `3.9.1` | Infix Prefix: GATE CSE 1997 \| Question: 1.7 | **A** |
| `3.9.2` | Infix Prefix: GATE CSE 1998 \| Question: 19b | **N/A** |
| `3.9.3` | Infix Prefix: GATE CSE 2004 \| Question: 38, ISRO2009-27 | **A** |
| `3.9.4` | Infix Prefix: GATE CSE 2007 \| Question: 38, ISRO2016-27 | **A** |
| `3.10.1` | Linked List: GATE CSE 1987 \| Question: 1-xv | **B** |
| `3.10.2` | Linked List: GATE CSE 1987 \| Question: 6a | **N/A** |
| `3.10.3` | Linked List: GATE CSE 1993 \| Question: 13 | **N/A** |
| `3.10.4` | Linked List: GATE CSE 1994 \| Question: 1.17, UGCNET-Sep2013-II: 32 | **B** |
| `3.10.5` | Linked List: GATE CSE 1995 \| Question: 2.22 | **D** |
| `3.10.6` | Linked List: GATE CSE 1997 \| Question: 1.4 | **C** |
| `3.10.7` | Linked List: GATE CSE 1997 \| Question: 18 | **N/A** |
| `3.10.8` | Linked List: GATE CSE 1998 \| Question: 19a | **N/A** |
| `3.10.9` | Linked List: GATE CSE 1999 \| Question: 11b | **N/A** |
| `3.10.10` | Linked List: GATE CSE 2002 \| Question: 1.5 | **D** |
| `3.10.11` | Linked List: GATE CSE 2003 \| Question: 90 | **B** |
| `3.10.12` | Linked List: GATE CSE 2004 \| Question: 36 | **A** |
| `3.10.13` | Linked List: GATE CSE 2004 \| Question: 40 | **D** |
| `3.10.14` | Linked List: GATE CSE 2008 \| Question: 62 | **B** |
| `3.10.15` | Linked List: GATE CSE 2010 \| Question: 36 | **D** |
| `3.10.16` | Linked List: GATE CSE 2016 \| Set 2 \| Question: 15 | **C** |
| `3.10.17` | Linked List: GATE CSE 2017 \| Set 1 \| Question: 08 | **B** |
| `3.10.18` | Linked List: GATE CSE 2020 \| Question: 16 | **C** |
| `3.10.19` | Linked List: GATE CSE 2022 \| Question: 5 | **A** |
| `3.10.20` | Linked List: GATE CSE 2023 \| Question: 3 | **D** |
| `3.10.21` | Linked List: GATE CSE 2025 \| Set 1 \| Question: 52 | **5:5** |
| `3.10.22` | Linked List: GATE CSE 2026 \| Set 1 \| Question: 29 | **B** |
| `3.10.23` | Linked List: GATE IT 2004 \| Question: 13 | **A** |
| `3.10.24` | Linked List: GATE IT 2005 \| Question: 54 | **B** |
| `3.11.1` | Priority Queue: GATE CSE 1997 \| Question: 4.7 | **D** |
| `3.11.2` | Priority Queue: GATE CSE 2023 \| Question: 36 | **B** |
| `3.12.1` | Queue: GATE CSE 1992 \| Question: 09 | **N/A** |
| `3.12.2` | Queue: GATE CSE 1994 \| Question: 26 | **N/A** |
| `3.12.3` | Queue: GATE CSE 1996 \| Question: 1.12 | **A** |
| `3.12.4` | Queue: GATE CSE 2001 \| Question: 2.16 | **B** |
| `3.12.5` | Queue: GATE CSE 2006 \| Question: 49 | **A** |
| `3.12.6` | Queue: GATE CSE 2012 \| Question: 35 | **A** |
| `3.12.7` | Queue: GATE CSE 2013 \| Question: 44 | **A** |
| `3.12.8` | Queue: GATE CSE 2016 \| Set 1 \| Question: 10 | **A** |
| `3.12.9` | Queue: GATE CSE 2016 \| Set 1 \| Question: 41 | **256** |
| `3.12.10` | Queue: GATE CSE 2017 \| Set 2 \| Question: 13 | **B** |
| `3.12.11` | Queue: GATE CSE 2018 \| Question: 3 | **B** |
| `3.12.12` | Queue: GATE CSE 2022 \| Question: 52 | **0** |
| `3.12.13` | Queue: GATE CSE 2026 \| Set 2 \| Question: 40 | **A;B** |
| `3.12.14` | Queue: GATE DS&AI 2024 \| Question: 22 | **17** |
| `3.12.15` | Queue: GATE IT 2007 \| Question: 30 | **B** |
| `3.13.1` | Stack: GATE CSE 1989 \| Question: 4-ii | **N/A** |
| `3.13.2` | Stack: GATE CSE 1991 \| Question: 03,vii | **B** |
| `3.13.3` | Stack: GATE CSE 1994 \| Question: 1.14 | **B** |
| `3.13.4` | Stack: GATE CSE 1995 \| Question: 2.21 | **B** |
| `3.13.5` | Stack: GATE CSE 2000 \| Question: 13 | **N/A** |
| `3.13.6` | Stack: GATE CSE 2003 \| Question: 64 | **C** |
| `3.13.7` | Stack: GATE CSE 2004 \| Question: 3 | **D** |
| `3.13.8` | Stack: GATE CSE 2004 \| Question: 5 | **B** |
| `3.13.9` | Stack: GATE CSE 2014 \| Set 2 \| Question: 41 | **C** |
| `3.13.10` | Stack: GATE CSE 2015 \| Set 2 \| Question: 38 | **15** |
| `3.13.11` | Stack: GATE CSE 2015 \| Set 3 \| Question: 12 | **C** |
| `3.13.12` | Stack: GATE CSE 2021 \| Set 1 \| Question: 21 | **86** |
| `3.13.13` | Stack: GATE CSE 2023 \| Question: 49 | **8** |
| `3.13.14` | Stack: GATE CSE 2024 \| Set 2 \| Question: 38 | **B;C;D** |
| `3.13.15` | Stack: GATE CSE 2025 \| Set 2 \| Question: 35 | **A** |
| `3.13.16` | Stack: GATE DA 2025 \| Question: 54 | **24:24** |
| `3.13.17` | Stack: GATE IT 2004 \| Question: 52 | **D** |
| `3.13.18` | Stack: GATE IT 2005 \| Question: 13 | **C** |
| `3.13.19` | Stack: GATE IT 2007 \| Question: 32 | **B** |
| `3.14.1` | Time Complexity: GATE CSE 2025 \| Set 2 \| Question: 28 | **A** |
| `3.15.1` | Tree: GATE CSE 1990 \| Question: 13a | **N/A** |
| `3.15.2` | Tree: GATE CSE 1992 \| Question: 02,vii | **A;D** |
| `3.15.3` | Tree: GATE CSE 1994 \| Question: 5 | **N/A** |
| `3.15.4` | Tree: GATE CSE 1998 \| Question: 1.24 | **B;C** |
| `3.15.5` | Tree: GATE CSE 1998 \| Question: 2.11 | **A** |
| `3.15.6` | Tree: GATE CSE 2002 \| Question: 2.9 | **D** |
| `3.15.7` | Tree: GATE CSE 2004 \| Question: 6 | **D** |
| `3.15.8` | Tree: GATE CSE 2005 \| Question: 36 | **C** |
| `3.15.9` | Tree: GATE CSE 2007 \| Question: 43 | **C** |
| `3.15.10` | Tree: GATE CSE 2014 \| Set 3 \| Question: 12 | **A** |
| `3.15.11` | Tree: GATE CSE 2014 \| Set 3 \| Question: 41 | **D** |
| `3.15.12` | Tree: GATE CSE 2017 \| Set 1 \| Question: 20 | **18** |
| `3.15.13` | Tree: GATE CSE 2021 \| Set 1 \| Question: 41 | **B** |
| `3.16.1` | Tree Traversal: GATE CSE 2026 \| Set 2 \| Question: 2 | **A** |
| `3.17.1` | Uniform Hashing: GATE DS&AI 2024 \| Question: 11 | **B** |

