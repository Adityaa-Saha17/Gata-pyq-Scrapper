# Volume 3 — Chapter 3: Databases

- **Source PDF**: [filter1_volume3.pdf](file:///Users/adityaasaha/Documents/Academics/Gate/filter1_volume3.pdf)
- **Total GATE Questions in Chapter**: **302**

---

## 1. Subtopic Weightage & Question Distribution

| Subtopic # | Subtopic Name | Questions |
| :---: | :--- | :---: |
| **3.1** | Armstrong Axioms | 1 |
| **3.2** | B Tree | 32 |
| **3.3** | Candidate Key | 7 |
| **3.4** | Conflict Serializable | 12 |
| **3.5** | Database Design | 1 |
| **3.6** | Database Normalization | 56 |
| **3.7** | Database Schema | 1 |
| **3.8** | Decomposition | 1 |
| **3.9** | ER Diagram | 12 |
| **3.10** | Functional Dependency | 3 |
| **3.11** | Indexing | 15 |
| **3.12** | Joins | 7 |
| **3.13** | Multivalued Dependency 4nf | 1 |
| **3.14** | Natural Join | 3 |
| **3.15** | Normal Forms | 1 |
| **3.16** | Query | 3 |
| **3.17** | Referential Integrity | 6 |
| **3.18** | Relational Algebra | 33 |
| **3.20** | Relational Model | 2 |
| **3.21** | SQL | 58 |
| **3.22** | Safe Query | 1 |
| **3.23** | Super Key | 1 |
| **3.24** | Timestamp Ordering | 1 |
| **3.25** | Transaction and Concurrency | 27 |
| **3.26** | Tuple Relational Calculus | 3 |
| **3.27** | Two Phase Locking Protocol | 1 |


---

## 2. Comprehensive GATE CSE Databases Reference (Expanded Research & Formulas)

### 2.1 Functional Dependencies (FDs), Keys & Normalization
- **Armstrong's Axioms** (Sound & Complete):
  - **Reflexivity**: If $Y \subseteq X$, then $X \to Y$.
  - **Augmentation**: If $X \to Y$, then $XZ \to YZ$.
  - **Transitivity**: If $X \to Y$ and $Y \to Z$, then $X \to Z$.
  - *(Derived)* Union ($X \to Y, X \to Z \implies X \to YZ$), Decomposition ($X \to YZ \implies X \to Y, X \to Z$), Pseudotransitivity ($X \to Y, WY \to Z \implies WX \to Z$).
- **Normal Forms Hierarchy** ($\text{BCNF} \subsetneq \text{3NF} \subsetneq \text{2NF} \subsetneq \text{1NF}$):

| Normal Form | Exact Condition for Every Non-Trivial FD $X \to A$ ($A \notin X$) | Always Dependency-Preserving? | Always Lossless-Join? |
| :--- | :--- | :---: | :---: |
| **1NF** | All attributes have **atomic** (indivisible) domains (every relation in RDBMS is in 1NF). | Yes | Yes |
| **2NF** | **No partial dependency**: No **non-prime** attribute is functionally dependent on any **proper subset** of a candidate key. *(If all candidate keys are simple/single-attribute, $R$ is automatically in 2NF!)* | Yes | Yes |
| **3NF** | Either **$X$ is a Superkey**, OR **$A$ is a Prime Attribute** (part of some candidate key). | **Yes (Always!)** | **Yes (Always!)** |
| **BCNF** | **$X$ MUST be a Superkey** for every non-trivial FD $X \to Y$. *(Every 2-attribute relation is automatically in BCNF!)* | **Not always** | **Yes (Always!)** |

- **Lossless-Join Decomposition Test** for $R \to (R_1, R_2)$:
  - Decomposition is **lossless** iff $(R_1 \cap R_2) \to R_1$ OR $(R_1 \cap R_2) \to R_2$ holds in $F^+$ (i.e., $R_1 \cap R_2$ is a superkey of $R_1$ or $R_2$).
- **Dependency Preservation Test**:
  - Decomposition $(R_1, \dots, R_k)$ preserves $F$ iff $\big(\bigcup_{i=1}^k \pi_{R_i}(F)\big)^+ = F^+$.

### 2.2 Relational Algebra, Tuple Calculus & SQL
- **Join Cardinality Bounds** for $R(A, B)$ ($m$ tuples) and $S(B, C)$ ($n$ tuples):
  - If $B$ has no relation constraint: **$0 \le |R \bowtie S| \le m \times n$**.
  - If $S.B$ is a **Foreign Key** referencing Primary Key $R.B$ (and not null): $|R \bowtie S| = n$.
- **Division Operator $R(A, B) \div S(B)$**:
  $$R \div S = \pi_A(R) - \pi_A\Big( \big(\pi_A(R) \times S\big) - R \Big)$$
- **SQL `NULL` and Aggregate Rules (Critical GATE Traps!)**:
  - Any arithmetic or comparison with `NULL` (`=`, `<>`, `<`, `>`) evaluates to **`UNKNOWN`** (Only `IS NULL` / `IS NOT NULL` return `TRUE`/`FALSE`).
  - `COUNT(*)` counts **all rows** (including `NULL`s); `COUNT(A)`, `SUM(A)`, `AVG(A)`, `MIN(A)`, `MAX(A)` **ignore `NULL`s**!
  - `WHERE` filters **individual rows before `GROUP BY`**; `HAVING` filters **groups after `GROUP BY`**.
  - **`NOT IN (subquery)` Trap**: `x NOT IN (a, b, NULL)` is equivalent to `x <> a AND x <> b AND x <> NULL`, which **NEVER evaluates to TRUE** (returns empty set if the subquery produces any `NULL`!). `IN` with `NULL` still matches non-null values (`x = a OR x = b OR UNKNOWN`).

### 2.3 Indexing, B-Trees & B+ Trees
- **Indexing Classification**:
  - **Primary Index**: Ordered file on **Ordering Key field** (Sparse: 1 index entry per disk block).
  - **Clustering Index**: Ordered file on **Ordering Non-Key field** (Sparse: 1 entry per distinct value).
  - **Secondary Index**: Unordered field (Key or Non-Key) — **MUST be Dense** (1 entry per record or per key value with pointer buckets).
- **B-Tree vs B+ Tree of Order $p$** (block size $B$, key size $K$, block pointer $P_b$, record pointer $P_r$):
  - **B-Tree Internal Node** (stores record pointers $P_r$ at every level):
    $$p \cdot P_b + (p - 1)(K + P_r) \le B$$
  - **B+ Tree Internal Node** (NO record pointers in internal nodes!):
    $$p_{\text{internal}} \cdot P_b + (p_{\text{internal}} - 1)K \le B$$
  - **B+ Tree Leaf Node** (stores $(K, P_r)$ pairs + 1 sibling block pointer $P_b$):
    $$p_{\text{leaf}}(K + P_r) + P_b \le B$$
  - **Node Occupancy Bounds** (for order $p =$ max children):
    - Root: $2$ to $p$ children ($1$ to $p-1$ keys).
    - Non-root internal node: $\lceil p/2 \rceil$ to $p$ children ($\lceil p/2 \rceil - 1$ to $p - 1$ keys).

### 2.4 Transactions, Serializability & Concurrency Control
- **Number of Schedules** for $k$ transactions with $n_1, n_2, \dots, n_k$ operations ($N = \sum n_i$):
  - **Serial Schedules**: $k!$
  - **Total Concurrent Schedules**: $\frac{N!}{n_1! n_2! \dots n_k!}$
- **Conflict Serializability**:
  - Two operations conflict iff they belong to **different transactions**, access the **same data item**, and **at least one is a Write** ($RW, WR, WW$).
  - A schedule $S$ is **Conflict Serializable iff its Precedence (Serialization) Graph has NO cycle**!
  - $\text{Serial} \subsetneq \text{Conflict Serializable} \subsetneq \text{View Serializable}$. (If a schedule has no **blind writes**, View Serializable $\iff$ Conflict Serializable).
- **Recoverability Hierarchy** ($\text{Strict} \subsetneq \text{Cascadeless (ACA)} \subsetneq \text{Recoverable}$):
  - **Recoverable**: If $T_j$ reads a dirty value written by $T_i$, then $T_i$ must **commit before** $T_j$ commits.
  - **Cascadeless (Avoids Cascading Aborts — ACA)**: $T_j$ can only read values written by **already committed** transactions.
  - **Strict**: $T_j$ can neither **read nor overwrite** a data item written by $T_i$ until $T_i$ commits or aborts.
- **2PL & Timestamp Ordering**:
  - **Basic 2PL**: Guarantees Conflict Serializability, but **NOT** freedom from deadlock or cascading rollback.
  - **Strict 2PL**: Hold all Exclusive (Write) locks until commit/abort $\implies$ Conflict Serializable + Strict (Recoverable & Cascadeless).
  - **Rigorous 2PL**: Hold **ALL** locks (Shared & Exclusive) until commit/abort.
  - **Conservative (Static) 2PL**: Pre-declare and acquire all locks before execution $\implies$ **Deadlock-Free**!
  - **Wait-Die (Non-Preemptive)** vs **Wound-Wait (Preemptive)**: Both prevent deadlock and starvation (if rolled-back transactions keep their original timestamp!).

---

## 3. Original PDF Chapter Notes (Preserved Verbatim)

3 Databases (302)
ER‐model. Relational model:Relational algebra, Tuple calculus, SQL. Integrity constraints, Normal forms. File
organization, Indexing (e.g., B and B+ trees). Transactions and concurrency control.
Welcome to the Databases chapter of your GATE Computer Science preparation. This crucial subject forms the
backbone of modern data management and is indispensable for any computer science professional. In GATE,
Databases typically carries a significant weightage, ranging from 6 to 10 marks, often featuring a mix of conceptual
questions, problem-solving scenarios, and direct application of formulas. You can expect questions on topics like
relational algebra/calculus, SQL queries, functional dependencies, normal forms, B-trees, and concurrency control
protocols. A strong grasp of these fundamentals is vital not just for the exam but also for practical applications in
software development and data engineering.
Topic-wise Key Concepts
Armstrong Axioms
Armstrong Axioms are a set of inference rules used to derive all functional dependencies (FDs) implied by a given set of
FDs. They are sound (do not generate incorrect FDs) and complete (can generate all correct FDs).
Formulas/Theorems:
1. Reflexivity: If , then . (Trivial FD)
2. Augmentation: If , then (where is any set of attributes).
3. Transitivity: If and , then .
Derived Rules:
4. Union: If and , then .
5. Decomposition: If , then and .
6. Pseudotransitivity: If and , then .
Key Properties/Identities:
Used to find the closure of an attribute set .
Fundamental for determining candidate keys and normal forms.
Common Pitfalls:
Confusing derived rules with basic axioms.
Incorrectly applying augmentation or transitivity.
Problem-Solving Techniques:
To find given FDs.
To check if : Start with . Repeatedly add attributes to if they are determined by any subset of using the
is implied by a set of FDs : Check if .
B Tree
A B-tree is a self-balancing tree data structure that maintains sorted data and allows searches, sequential access,
insertions, and deletions in logarithmic time. It is optimized for systems that read and write large blocks of data, such as
disk storage.

*(PDF Page 168)*

Formulas/Theorems:
Order : Each node (except root) has at least children and at most Number of keys: A node with children has keys.
Minimum keys (non-root): .
Maximum keys: .
Maximum height : For keys and order , .
Minimum height : For keys and order , .
children.
Key Properties/Identities:
All leaf nodes are at the same level.
Keys within a node are sorted.
Efficient for disk-based indexing due to high fan-out.
Common Pitfalls:
Miscalculating minimum/maximum number of keys or children per node.
Incorrectly performing split/merge operations during insertion/deletion.
Problem-Solving Techniques:
Trace insertion/deletion operations step-by-step, paying attention to splits (when a node overflows) and merges
(when a node underflows).
Calculate disk I/Os by counting the number of nodes visited (including root and leaf) for search, insertion, or
deletion.
Candidate Key
A Candidate Key is a minimal Super Key. It is a set of attributes that uniquely identifies each tuple in a relation, and no
proper subset of these attributes can uniquely identify tuples.
Formulas/Theorems:
A set of attributes is a Candidate Key if:
1. (where is all attributes in the relation) - Uniqueness property.
2. For no proper subset ,
- Minimality property.
Key Properties/Identities:
Every relation must have at least one candidate key.
One candidate key is chosen as the Primary Key.
Common Pitfalls:
Confusing with Super Key (Super Key doesn't require minimality).
Forgetting to check the minimality condition.
Problem-Solving Techniques:
Find the closure of various attribute sets. A set is a super key if contains all attributes of the relation.
From the super keys, identify those that are minimal (i.e., no subset is also a super key) to find candidate keys.
Conflict Serializable
A schedule is Conflict Serializable if it is conflict equivalent to some serial schedule. Two operations conflict if they are
on the same data item, belong to different transactions, and at least one of them is a write operation (W-W, W-R, R-W
conflicts).

*(PDF Page 169)*

Formulas/Theorems:
Precedence Graph (Serialization Graph):
Nodes represent transactions.
An edge exists if performs an operation that conflicts with an operation of , and 's operation
occurs before 's.
Theorem: A schedule is conflict serializable if and only if its precedence graph contains no cycles.
Key Properties/Identities:
Guarantees that the concurrent execution produces the same result as some sequential execution.
A weaker condition than view serializability but easier to test.
Common Pitfalls:
Incorrectly identifying conflicting operations (e.g., R-R operations do not conflict).
Missing cycles in the precedence graph, especially in complex schedules.
Problem-Solving Techniques:
Construct the precedence graph by identifying all conflicting pairs of operations and drawing edges accordingly.
Use a cycle detection algorithm (e.g., DFS) on the graph to check for serializability.
Database Design
Database design is the process of creating a detailed data model for a database. It involves translating conceptual
requirements into a logical schema, and then into a physical schema, ensuring data integrity, efficiency, and scalability.
Formulas/Theorems:
No direct formulas, but relies on principles of normalization and ER-to-Relational mapping rules.
Key Properties/Identities:
Phases: Conceptual (ER Model), Logical (Relational Schema), Physical (Storage details).
Goals: Minimize redundancy, maximize integrity, optimize performance.
Common Pitfalls:
Poor choice of primary/foreign keys.
Not adequately normalizing the schema, leading to update anomalies.
Over-normalization, leading to complex queries and performance issues.
Problem-Solving Techniques:
Start with an ER diagram to capture requirements.
Apply ER-to-Relational mapping rules systematically.
Normalize relations to an appropriate normal form (e.g., BCNF or 3NF) using functional dependencies.
Database Normalization
Database Normalization is a systematic process of restructuring a relational database schema to minimize data
redundancy and improve data integrity. It involves decomposing relations into smaller, well-structured relations based
on functional dependencies.
Formulas/Theorems:
1NF (First Normal Form): All attributes must be atomic (no multi-valued or composite attributes).
2NF (Second Normal Form): In 1NF and no non-prime attribute is partially dependent on a candidate key.
3NF (Third Normal Form): In 2NF and no non-prime attribute is transitively dependent on a candidate key.

*(PDF Page 170)*

BCNF (Boyce-Codd Normal Form): For every non-trivial functional dependency 4NF (Fourth Normal Form): In BCNF and no non-trivial multi-valued dependencies exist.
5NF (Fifth Normal Form): In 4NF and no non-trivial join dependencies exist.
, must be a super key.
Key Properties/Identities:
Hierarchy: .
Desirable properties of decomposition: Lossless Join and Dependency Preservation. BCNF decomposition is always
lossless but not always dependency preserving. 3NF decomposition is always lossless and dependency preserving.
Common Pitfalls:
Incorrectly identifying prime and non-prime attributes.
Mistaking partial dependency for transitive dependency.
Failing to check for both lossless join and dependency preservation after decomposition.
Problem-Solving Techniques:
Identify all candidate keys and functional dependencies.
Systematically check for violations of each normal form.
If a violation exists, decompose the relation into smaller relations.
Database Schema
A Database Schema is the logical structure or design of the entire database. It defines the tables, attributes, data types,
relationships, and constraints that govern the data within the database. It is defined using Data Definition Language
(DDL).
Formulas/Theorems:
No specific formulas, but it's the blueprint for the database.
Key Properties/Identities:
Internal Schema: Physical storage structure.
Conceptual Schema: Logical structure of the entire database.
External Schema (View): User-specific views of the database.
Schema defines the intension, while data (instance) defines the extension.
Common Pitfalls:
Confusing schema (structure) with database instance (actual data).
Overlooking important constraints during schema design.
Problem-Solving Techniques:
Understand the mapping from ER diagrams to relational schemas.
Be familiar with DDL commands like CREATE TABLE, ALTER TABLE, DROP TABLE.
Decomposition
Decomposition is the process of breaking down a relation (table) into two or more smaller relations. It is primarily used
in normalization to eliminate redundancy and anomalies, ensuring that the resulting relations are in a higher normal
form.
Formulas/Theorems:
Lossless Join Decomposition: A decomposition of into and is lossless if .
Condition: or must hold based on the FDs of .
Dependency Preservation: A decomposition preserves dependencies if the union of FDs on the decomposed

*(PDF Page 171)*

relations is equivalent to the original set of FDs. Formally, if , then .
is the original set of FDs and is the set of FDs on
Key Properties/Identities:
Desirable properties for decomposition are lossless join and dependency preservation.
BCNF decomposition is always lossless but not always dependency preserving.
3NF decomposition is always lossless and dependency preserving.
Common Pitfalls:
Incorrectly applying the lossless join test.
Failing to check for dependency preservation, especially for BCNF.
Problem-Solving Techniques:
For lossless join: Check if the common attributes form a super key for at least one of the decomposed relations.
For dependency preservation: For each original FD , check if it can be derived from the FDs of the
decomposed relations.
ER Diagram
An Entity-Relationship (ER) Diagram is a high-level conceptual data model that represents the entities, attributes, and
relationships within a system. It is used during the conceptual design phase of database development.
Formulas/Theorems:
No direct formulas, but specific rules for mapping to relational schema.
Key Properties/Identities:
Entities: Represented by rectangles (e.g., Student, Course).
Attributes: Represented by ovals (e.g., Name, ID). Key attributes are underlined.
Relationships: Represented by diamonds (e.g., Enrolls, Teaches).
Cardinality: (1:1, 1:N, M:N) specifies the number of instances of one entity that can be associated with another.
Participation: (Total/Partial) specifies whether an entity instance must participate in a relationship.
Weak Entity: An entity that cannot be uniquely identified by its own attributes and depends on a strong (owner)
entity. Represented by double rectangles.
Common Pitfalls:
Incorrectly identifying cardinalities or participation constraints.
Confusing strong and weak entities.
Errors in mapping complex ER constructs (e.g., ternary relationships, generalization) to relational schema.
Problem-Solving Techniques:
Carefully read the problem description to identify entities, attributes, and relationships.
Pay close attention to cardinality and participation rules.
Practice mapping ER diagrams to relational schemas using standard rules.
Functional Dependency
A Functional Dependency (FD) attribute set attributes in .
means that the value of attribute set . If two tuples have the same values for attributes in uniquely determines the value of
, they must also have the same values for
Formulas/Theorems:
Closure of an attribute set : The set of all attributes that are functionally determined by .

*(PDF Page 172)*

Algorithm: Start with . Repeatedly add attributes to if there is an FD such that
.
Minimal Cover (or Minimal Basis): A set of FDs equivalent to 1. Every FD in has a single attribute on the right-hand side.
2. No FD in can be removed without changing .
3. No attribute can be removed from the left-hand side of any FD in such that:
without changing .
Key Properties/Identities:
Fundamental for database normalization and identifying keys.
Armstrong's Axioms are used to infer FDs.
Common Pitfalls:
Incorrectly calculating attribute closure.
Errors in finding a minimal cover.
Problem-Solving Techniques:
Master the algorithm for finding .
For minimal cover, systematically apply the three conditions: right-hand side single attribute, remove redundant FDs,
remove redundant attributes from LHS.
Indexing
Indexing is a technique used to optimize the performance of database queries by allowing the database server to
quickly locate and retrieve specific rows without scanning the entire table. It creates a data structure (like B-tree or hash
table) that stores a small, ordered subset of the data.
Formulas/Theorems:
Disk I/O for B-tree index: For a search, typically Disk I/O for hash index: Typically 1-2 disk accesses for exact match, if no collision.
(for data block) disk accesses.
Key Properties/Identities:
Primary Index: Index on the primary key, usually clustered.
Secondary Index: Index on non-key attributes, usually unclustered.
Clustered Index: Data rows are stored physically in the order of the index key. Only one per table.
Unclustered Index: Index stores pointers to the data rows, which are not physically ordered by the index key.
Common Pitfalls:
Misunderstanding the difference between clustered and unclustered indexes.
Incorrectly calculating disk I/Os for different index types and query patterns.
Problem-Solving Techniques:
Analyze the query type (equality search, range search) and index type to determine disk I/O.
Remember that clustered indexes can retrieve multiple data records with fewer I/Os for range queries.
Joins
Joins combine rows from two or more tables based on a related column between them. They are fundamental
operations in relational algebra and SQL for retrieving data from multiple relations.
Formulas/Theorems:
Cartesian Product (Cross Join): . Combines every row of with every row of . If has tuples and

*(PDF Page 173)*

has tuples, has tuples.
Theta Join: Equijoin: A theta join where Natural Join: result.
attributes with NULLs.
. Combines tuples from and where the condition is true.
is an equality condition (e.g., ).
. An equijoin on all common attributes, with duplicate common columns removed from the
Outer Joins (Left, Right, Full): Preserve tuples that do not have a match in the other relation, filling unmatched
Key Properties/Identities:
Result schema of a join is the union of attributes from participating relations (with common attributes appearing once
in natural join).
Join operations are associative and commutative (for inner joins).
Common Pitfalls:
Confusing different types of joins, especially natural join vs. equijoin.
Misunderstanding how NULL values are handled in outer joins.
Incorrectly calculating the number of tuples in the result.
Problem-Solving Techniques:
For natural join, identify common attributes and their values.
For outer joins, remember to include unmatched tuples from the specified side(s).
Trace the operation step-by-step for small example relations.
Multivalued Dependency 4NF
A Multivalued Dependency (MVD) exists in a relation and this set is independent of the values of other attributes in trivial MVD in a relation, must be a super key.
if, for a given value of , there is a set of values for ,
. 4NF (Fourth Normal Form) requires that for every non-
Formulas/Theorems:
Trivial MVD: is trivial if or .
MVD Inference Rules (some are similar to FDs):
Reflexivity: If , then .
Augmentation: If , then .
Transitivity: If and , then .
Complementation: If , then .
Union: If and , then .
Decomposition: If and , then , , and .
Replication (FD to MVD): If , then .
Key Properties/Identities:
MVDs address redundancy arising from multi-valued facts that are independent of each other.
4NF eliminates these MVDs by decomposition.
Common Pitfalls:
Confusing MVDs with FDs. MVDs imply FDs, but not vice versa.
Incorrectly identifying trivial MVDs.
Problem-Solving Techniques:
Identify MVDs by looking for independent multi-valued facts.
Decompose relations based on non-trivial MVDs to achieve 4NF. For and .
with , decompose into

*(PDF Page 174)*

Natural Join
The Natural Join operation ( ) combines two relations based on equality of their common attributes. It implicitly creates
an equijoin condition for all attributes that share the same name in both relations and projects out the duplicate common
attributes.
Formulas/Theorems:
Given relations and , let be the set of common attributes.
where .
Key Properties/Identities:
The resulting schema contains all attributes from both relations, with common attributes appearing only once.
It is a special case of equijoin followed by projection.
Common Pitfalls:
Misunderstanding the implicit join condition (all common attributes).
Incorrectly determining the schema or number of tuples in the result.
Problem-Solving Techniques:
Identify all common attributes between the two relations.
For each pair of tuples (one from each relation), check if their values for all common attributes are equal. If so,
combine them into a single result tuple, keeping common attributes only once.
Normal Forms
Normal Forms (1NF, 2NF, 3NF, BCNF, 4NF, 5NF) are a series of guidelines for designing relational database schemas
to reduce data redundancy and improve data integrity. Each normal form builds upon the previous one, imposing stricter
rules.
Formulas/Theorems:
1NF: All attributes are atomic.
2NF: In 1NF and no non-prime attribute is partially dependent on any candidate key.
3NF: In 2NF and no non-prime attribute is transitively dependent on any candidate key.
BCNF: For every non-trivial FD , is a super key.
4NF: In BCNF and no non-trivial MVDs exist.
5NF: In 4NF and no non-trivial join dependencies exist.
Key Properties/Identities:
Higher normal forms generally reduce more redundancy but may require more joins for queries.
BCNF is generally preferred, but 3NF is often a practical compromise as it guarantees lossless join and dependency
preservation.
Common Pitfalls:
Incorrectly identifying candidate keys, which is crucial for all normal forms.
Confusing partial, transitive, and multi-valued dependencies.
Problem-Solving Techniques:
First, find all candidate keys and the closure of all FDs.
Then, systematically check the conditions for 1NF, 2NF, 3NF, and BCNF in order.

*(PDF Page 175)*

If a relation is not in a desired normal form, decompose it into smaller relations that satisfy the conditions.
Query
A query is a request for data or information from a database. Queries are typically written using a query language like
SQL, Relational Algebra, or Relational Calculus. They specify what data to retrieve, how to filter it, and how to present
it.
Formulas/Theorems:
No specific formulas, but relies on the syntax and semantics of query languages.
Key Properties/Identities:
Selectivity: The fraction of tuples that satisfy a selection condition.
Projection: Selecting specific columns.
Join: Combining data from multiple tables.
Common Pitfalls:
Syntax errors in SQL.
Logical errors leading to incorrect results (e.g., wrong join conditions, incorrect aggregation).
Inefficient queries that perform poorly.
Problem-Solving Techniques:
Break down complex queries into smaller, manageable parts.
Understand the order of operations in SQL (FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY).
Practice translating natural language requirements into formal query language expressions.
Referential Integrity
Referential Integrity is a database concept that ensures that relationships between tables remain consistent. It is
enforced using foreign key constraints, which dictate that a foreign key in one table must either match a primary key in
another table or be NULL.
Formulas/Theorems:
No specific formulas, but it's a constraint rule.
Key Properties/Identities:
Prevents "dangling references" where a foreign key refers to a non-existent primary key.
Actions on deletion/update of primary key: CASCADE, SET NULL, SET DEFAULT, RESTRICT (default).
Common Pitfalls:
Violating referential integrity constraints during data modification.
Misunderstanding the behavior of different ON DELETE/ON UPDATE actions.
Problem-Solving Techniques:
Identify primary and foreign keys correctly during schema design.
Choose appropriate ON DELETE/ON UPDATE actions based on business rules.
Trace data modification operations to check for constraint violations.
Relational Algebra
Relational Algebra is a procedural query language that takes relations as input and produces relations as output. It
consists of a set of fundamental operations (selection, projection, union, set difference, Cartesian product, rename) and

*(PDF Page 176)*

derived operations (join, intersection, division).
Formulas/Theorems:
Select: (selects tuples satisfying predicate ).
Project: (selects attributes ).
Union: (combines tuples from and ; relations must be union-compatible).
Set Difference: (tuples in but not in ; union-compatible).
Cartesian Product: (combines every tuple of with every tuple of ).
Rename: (renames relation to and its attributes).
Intersection: (derived).
Join: (derived).
Key Properties/Identities:
Closure property: The result of any operation is also a relation.
Forms the theoretical basis for SQL.
Common Pitfalls:
Incorrectly applying operators, especially for complex queries.
Forgetting union compatibility requirements for set operations.
Operator precedence issues.
Problem-Solving Techniques:
Break down complex queries into a sequence of simpler relational algebra operations.
Practice converting SQL queries to relational algebra and vice versa.
Relational Calculus
Relational Calculus is a non-procedural (declarative) query language that describes what data to retrieve without
specifying how to retrieve it. It comes in two forms: Tuple Relational Calculus (TRC) and Domain Relational Calculus
(DRC).
Formulas/Theorems:
Tuple Relational Calculus (TRC): where is a tuple variable and is a formula (predicate) involving
.
Example:
Domain Relational Calculus (DRC): is a formula.
Example:
where are domain variables and
Key Properties/Identities:
Expressive power equivalent to Relational Algebra (Codd's Theorem).
Uses quantifiers ( - existential,
- universal).
Common Pitfalls:
Incorrectly using quantifiers, especially universal quantification.
Formulating predicates that are not "safe" (may yield infinite results).
Problem-Solving Techniques:
Translate natural language queries into logical predicates using tuple or domain variables.
Pay close attention to the scope of quantifiers.
Ensure queries are safe by bounding all variables.

*(PDF Page 177)*

Relational Model
The Relational Model is a data model based on the concept of relations (tables). Data is organized into two-dimensional
tables, where each table represents an entity or a relationship, and rows (tuples) represent records, while columns
(attributes) represent fields.
Formulas/Theorems:
No specific formulas, but defines the structure.
Key Properties/Identities:
Relation (Table): A set of tuples.
Tuple (Row): A record in a relation.
Attribute (Column): A named property of a relation.
Domain: The set of permissible values for an attribute.
Schema: The logical design of the database.
Instance: The actual data stored in the database at a particular time.
Integrity Constraints: Entity Integrity (Primary Key not NULL), Referential Integrity (Foreign Key rules).
Common Pitfalls:
Confusing the formal definitions of relation, tuple, and attribute.
Not understanding the role of domains and integrity constraints.
Problem-Solving Techniques:
Understand the basic terminology and how data is represented.
Be able to identify components of a relational schema.
SQL
SQL (Structured Query Language) is the standard language for managing and manipulating relational databases. It is
used for defining database schemas (DDL), querying data (DML), controlling access (DCL), and managing transactions
(TCL).
Formulas/Theorems:
No specific formulas, but adheres to a strict syntax.
Key Properties/Identities:
DDL (Data Definition Language): CREATE, ALTER, DROP (for schema objects).
DML (Data Manipulation Language): SELECT, INSERT, UPDATE, DELETE (for data).
DCL (Data Control Language): GRANT, REVOKE (for permissions).
TCL (Transaction Control Language): COMMIT, ROLLBACK, SAVEPOINT.
Common Pitfalls:
Complex queries involving subqueries, aggregate functions, GROUP BY, and HAVING clauses.
Understanding the order of execution of SQL clauses.
Differences in SQL dialects (though GATE usually sticks to standard SQL).
Problem-Solving Techniques:
Practice writing queries for various scenarios, including joins, subqueries, and aggregation.
Understand the logical processing order of a SELECT statement: FROM -> WHERE -> GROUP BY -> HAVING ->
SELECT -> ORDER BY.
Safe Query

*(PDF Page 178)*

A query in Relational Calculus is considered "safe" if it produces a finite number of tuples as its result for any valid
database instance. Unsafe queries can potentially produce an infinite result set, which is undesirable in practice.
Formulas/Theorems:
No direct formulas, but a conceptual property.
Key Properties/Identities:
Every query expressible in Relational Algebra is safe.
Safety typically requires that all variables are "bounded"
database (values currently present in the tables).
– their values must come from the active domain of the
Common Pitfalls:
Queries with unbounded variables, especially those using universal quantifiers without proper restrictions.
Example of unsafe query: (all tuples not in R, potentially infinite).
Problem-Solving Techniques:
Ensure that all variables in a relational calculus query are restricted to range over finite sets (e.g., relations in the
database or active domain).
For universal quantifiers, ensure they are used in a limited context (e.g.,
"for all X in Y...
").
Super Key
A Super Key is any set of attributes in a relation that, taken together, uniquely identifies each tuple in that relation. It
guarantees uniqueness but does not necessarily imply minimality.
Formulas/Theorems:
A set of attributes is a Super Key if (where is all attributes in the relation).
Key Properties/Identities:
Every candidate key is a super key.
A super key can contain redundant attributes (i.e., attributes not necessary for uniqueness).
Common Pitfalls:
Confusing with Candidate Key (Candidate Key is a minimal super key).
Forgetting that adding more attributes to a super key still results in a super key.
Problem-Solving Techniques:
To find super keys, start with candidate keys and add any combination of remaining attributes.
Alternatively, find the closure of attribute sets. Any set for which contains all attributes of the relation is a
super key.
Timestamp Ordering
Timestamp Ordering is a concurrency control protocol that ensures serializability by assigning a unique timestamp to
each transaction. Transactions are executed in the order of their timestamps, and conflicts are resolved by rolling back
transactions that violate this order.
Formulas/Theorems:
Each transaction is assigned a unique timestamp .
Each data item has a (read timestamp) and a (write timestamp).
Read Rule: If , must abort and restart with a new timestamp. Otherwise, read and set

*(PDF Page 179)*

.
Write Rule: If set .
or , must abort and restart. Otherwise, write and
Key Properties/Identities:
Guarantees conflict serializability.
Can lead to cascading rollbacks and starvation.
Basic timestamp ordering is prone to aborts.
Common Pitfalls:
Incorrectly applying the read/write rules, especially the abort conditions.
Tracing complex schedules with multiple transactions.
Problem-Solving Techniques:
Assign timestamps to transactions.
Maintain and for each data item.
Step through the schedule, applying the read and write rules and determining if any transaction needs to abort.
Transaction and Concurrency
A Transaction is a logical unit of work that accesses and possibly modifies the contents of a database. Concurrency
Control is the management of simultaneous operations on a database to ensure data consistency and integrity,
especially when multiple transactions execute concurrently.
Formulas/Theorems:
No direct formulas, but concepts like serializability and isolation levels are key.
Key Properties/Identities:
ACID Properties of Transactions:
Atomicity: All or nothing.
Consistency: Transaction takes database from one consistent state to another.
Isolation: Concurrent transactions appear to execute serially.
Durability: Changes are permanent once committed.
Concurrency Anomalies: Dirty Read, Lost Update, Unrepeatable Read, Phantom Read.
Isolation Levels: Read Uncommitted, Read Committed, Repeatable Read, Serializable.
Common Pitfalls:
Identifying which anomaly occurs in a given schedule.
Understanding how different concurrency control mechanisms (locking, timestamping) prevent anomalies.
Problem-Solving Techniques:
Analyze schedules to identify potential anomalies.
Understand how each ACID property is maintained or violated.
Relate isolation levels to the anomalies they prevent.
Tuple Relational Calculus
Tuple Relational Calculus (TRC) is a non-procedural query language where variables range over tuples. It allows users
to specify the properties of the tuples they want in the result without detailing the exact steps to retrieve them.
Formulas/Theorems:
General form: where is a tuple variable and is a formula (predicate) that must satisfy.

*(PDF Page 180)*

Predicates can involve:
Membership:
Attribute access:
Comparison operators:
Logical connectives:
Quantifiers: (exists), (for all)
Key Properties/Identities:
Expressive power equivalent to Relational Algebra.
More declarative than Relational Algebra.
Common Pitfalls:
Incorrectly formulating complex predicates, especially with multiple tuple variables and quantifiers.
Ensuring the query is "safe" (produces a finite result).
Problem-Solving Techniques:
Break down the query into smaller logical conditions.
Use a separate tuple variable for each relation involved in the query.
Carefully use quantifiers, ensuring variables are appropriately bound.
Two Phase Locking Protocol
The Two-Phase Locking (2PL) protocol is a concurrency control mechanism that ensures serializability by requiring
transactions to acquire all necessary locks before releasing any. It divides a transaction's execution into two phases: a
growing phase and a shrinking phase.
Formulas/Theorems:
No direct formulas, but a protocol with rules for lock acquisition and release.
Key Properties/Identities:
Growing Phase: Transaction can acquire new locks but cannot release any.
Shrinking Phase: Transaction can release existing locks but cannot acquire new ones.
Guarantees conflict serializability.
Can lead to deadlocks.
Strict 2PL: All exclusive (write) locks are held until commit/rollback, preventing cascading rollbacks.
Common Pitfalls:
Incorrectly identifying the growing and shrinking phases.
Detecting deadlocks in schedules using 2PL (e.g., using a wait-for graph).
Understanding the difference between basic 2PL and strict 2PL.
Problem-Solving Techniques:
Trace transaction execution, noting when locks are acquired and released.
Construct a wait-for graph to detect deadlocks: an edge exists if indicates a deadlock.
is waiting for a lock held by . A cycle
Quick Formula Reference
Armstrong Axioms:
Reflexivity: If , then
Augmentation: If , then
Transitivity: If and , then
B-Tree (Order ):

*(PDF Page 181)*

Min keys (non-root):
Max keys:
Min children (non-root):
Max children:
Candidate Key: and is minimal.
Conflict Serializable: Precedence graph has no cycles.
Functional Dependency Closure: (algorithm based on Armstrong's axioms).
Decomposition Lossless Join: For , or .
Relational Algebra Operators:
Select:
Project:
Union:
Set Difference:
Cartesian Product:
Natural Join:
Tuple Relational Calculus:
Timestamp Ordering Rules (for transaction on data item ):
Read: If , abort . Else, .
Write: If or , abort . Else, .
Important Tips for GATE
Master Functional Dependencies and Normal Forms: These are high-yield topics. Practice finding candidate
keys, attribute closures, and checking normal forms (especially 3NF and BCNF). Understand the implications of
lossless join and dependency preservation.
Hands-on with Relational Algebra/Calculus and SQL: Be proficient in writing queries in all three languages.
Practice converting queries between them. Pay attention to operator precedence in RA and quantifier usage in RC.
B-Tree Operations and I/O Calculation: Understand the structure, insertion, deletion, and search operations.
Crucially, be able to calculate the number of disk I/Os for various scenarios, as this is a common numerical
question.
Concurrency Control Protocols: Understand the ACID properties, common anomalies (dirty read, lost update,
etc.), and how 2PL and Timestamp Ordering prevent them. Practice drawing precedence graphs for conflict
serializability and wait-for graphs for deadlock detection.
ER Diagram to Relational Schema Mapping: Know the standard rules for mapping entities, attributes (simple,
composite, multi-valued), and relationships (1:1, 1:N, M:N, weak entities) to relational tables.
Read Questions Carefully: Database questions often have subtle details. For example, in normalization, the given
FDs are critical. In concurrency, the exact sequence of operations matters.
Time Management: Some problems, like tracing B-tree operations or complex concurrency schedules, can be time-
consuming. Practice efficiently solving these to save time during the exam.
Conceptual Clarity: While formulas are important, a deep conceptual understanding of why certain rules exist (e.g.,
why BCNF is stricter than 3NF, why 2PL guarantees serializability) will help you tackle tricky theoretical questions.

---

## 4. Complete Question Index & Answer Key Record (301 Questions)

| Q # | Question Source / Title | Answer Key |
| :---: | :--- | :---: |
| `3.1.1` | Armstrong Axioms: GATE CSE 2026 \| Set 2 \| Question: 32 | **D** |
| `3.2.1` | B Tree: GATE CSE 1989 \| Question: 12a | **N/A** |
| `3.2.2` | B Tree: GATE CSE 1994 \| Question: 14a | **N/A** |
| `3.2.3` | B Tree: GATE CSE 1994 \| Question: 14b | **N/A** |
| `3.2.4` | B Tree: GATE CSE 1997 \| Question: 19 | **N/A** |
| `3.2.5` | B Tree: GATE CSE 1999 \| Question: 1.25 | **B** |
| `3.2.6` | B Tree: GATE CSE 1999 \| Question: 21 | **N/A** |
| `3.2.7` | B Tree: GATE CSE 2000 \| Question: 1.22, UGCNET-June2012-II: 11 | **B** |
| `3.2.8` | B Tree: GATE CSE 2000 \| Question: 21 | **N/A** |
| `3.2.9` | B Tree: GATE CSE 2001 \| Question: 22 | **N/A** |
| `3.2.10` | B Tree: GATE CSE 2002 \| Question: 17 | **N/A** |
| `3.2.11` | B Tree: GATE CSE 2002 \| Question: 2.23, UGCNET-June2012-II: 26 | **C** |
| `3.2.12` | B Tree: GATE CSE 2003 \| Question: 65 | **B** |
| `3.2.13` | B Tree: GATE CSE 2004 \| Question: 52 | **C** |
| `3.2.14` | B Tree: GATE CSE 2005 \| Question: 28 | **D** |
| `3.2.15` | B Tree: GATE CSE 2007 \| Question: 63, ISRO2016-59 | **A** |
| `3.2.16` | B Tree: GATE CSE 2008 \| Question: 41 | **C** |
| `3.2.17` | B Tree: GATE CSE 2009 \| Question: 44 | **C** |
| `3.2.18` | B Tree: GATE CSE 2010 \| Question: 18 | **B** |
| `3.2.19` | B Tree: GATE CSE 2015 \| Set 2 \| Question: 6 | **5** |
| `3.2.20` | B Tree: GATE CSE 2015 \| Set 3 \| Question: 46 | **50** |
| `3.2.21` | B Tree: GATE CSE 2016 \| Set 2 \| Question: 21 | **A** |
| `3.2.22` | B Tree: GATE CSE 2017 \| Set 2 \| Question: 49 | **52** |
| `3.2.23` | B Tree: GATE CSE 2019 \| Question: 14 | **B** |
| `3.2.24` | B Tree: GATE CSE 2024 \| Set 1 \| Question: 11 | **A** |
| `3.2.25` | B Tree: GATE CSE 2025 \| Set 1 \| Question: 11 | **B;D** |
| `3.2.26` | B Tree: GATE CSE 2025 \| Set 2 \| Question: 47 | **33:33** |
| `3.2.27` | B Tree: GATE DA 2026 \| Question: 31 | **A** |
| `3.2.28` | B Tree: GATE IT 2004 \| Question: 79 | **C** |
| `3.2.29` | B Tree: GATE IT 2005 \| Question: 23, ISRO2017-67 | **A** |
| `3.2.30` | B Tree: GATE IT 2006 \| Question: 61 | **C** |
| `3.2.31` | B Tree: GATE IT 2007 \| Question: 84 | **A** |
| `3.2.32` | B Tree: GATE IT 2007 \| Question: 85 | **A** |
| `3.3.1` | Candidate Key: GATE CSE 1994 \| Question: 3.7 | **N/A** |
| `3.3.2` | Candidate Key: GATE CSE 2005 \| Question: 78 | **D** |
| `3.3.3` | Candidate Key: GATE CSE 2011 \| Question: 12 | **A** |
| `3.3.4` | Candidate Key: GATE CSE 2014 \| Set 2 \| Question: 21 | **8** |
| `3.3.5` | Candidate Key: GATE CSE 2014 \| Set 2 \| Question: 22 | **19** |
| `3.3.6` | Candidate Key: GATE CSE 2014 \| Set 3 \| Question: 22 | **B** |
| `3.3.7` | Candidate Key: GATE DA 2026 \| Question: 7 | **A** |
| `3.4.1` | Conflict Serializable: GATE CSE 2007 \| Question: 64 | **C** |
| `3.4.2` | Conflict Serializable: GATE CSE 2009 \| Question: 43 | **B** |
| `3.4.3` | Conflict Serializable: GATE CSE 2014 \| Set 1 \| Question: 29 | **D** |
| `3.4.4` | Conflict Serializable: GATE CSE 2014 \| Set 2 \| Question: 29 | **C** |
| `3.4.5` | Conflict Serializable: GATE CSE 2014 \| Set 3 \| Question: 29 | **A** |
| `3.4.6` | Conflict Serializable: GATE CSE 2017 \| Set 2 \| Question: 44 | **54** |
| `3.4.7` | Conflict Serializable: GATE CSE 2020 \| Question: 37 | **A** |
| `3.4.8` | Conflict Serializable: GATE CSE 2021 \| Set 1 \| Question: 32 | **B** |
| `3.4.9` | Conflict Serializable: GATE CSE 2021 \| Set 2 \| Question: 32 | **B** |
| `3.4.10` | Conflict Serializable: GATE CSE 2022 \| Question: 29 | **A** |
| `3.4.11` | Conflict Serializable: GATE CSE 2024 \| Set 1 \| Question: 36 | **B;C;D** |
| `3.4.12` | Conflict Serializable: GATE CSE 2025 \| Set 2 \| Question: 43 | **B** |
| `3.5.1` | Database Design: GATE CSE 1994 \| Question: 3.11 | **False** |
| `3.6.1` | Database Normalization: GATE CSE 1987 \| Question: 2n | **True** |
| `3.6.2` | Database Normalization: GATE CSE 1988 \| Question: 12i | **N/A** |
| `3.6.3` | Database Normalization: GATE CSE 1988 \| Question: 12iia | **N/A** |
| `3.6.4` | Database Normalization: GATE CSE 1988 \| Question: 12iib | **N/A** |
| `3.6.5` | Database Normalization: GATE CSE 1988 \| Question: 12iic | **N/A** |
| `3.6.6` | Database Normalization: GATE CSE 1990 \| Question: 2-iv | **N/A** |
| `3.6.7` | Database Normalization: GATE CSE 1990 \| Question: 3-ii | **A;B;D** |
| `3.6.8` | Database Normalization: GATE CSE 1994 \| Question: 3.6 | **False** |
| `3.6.9` | Database Normalization: GATE CSE 1995 \| Question: 26 | **N/A** |
| `3.6.10` | Database Normalization: GATE CSE 1997 \| Question: 6.9 | **A** |
| `3.6.11` | Database Normalization: GATE CSE 1998 \| Question: 1.34 | **D** |
| `3.6.12` | Database Normalization: GATE CSE 1998 \| Question: 26 | **N/A** |
| `3.6.13` | Database Normalization: GATE CSE 1999 \| Question: 1.24 | **B** |
| `3.6.14` | Database Normalization: GATE CSE 1999 \| Question: 2.7, UGCNET-June2014-III: 25 | **D** |
| `3.6.15` | Database Normalization: GATE CSE 2000 \| Question: 2.24 | **B** |
| `3.6.16` | Database Normalization: GATE CSE 2001 \| Question: 2.23 | **C** |
| `3.6.17` | Database Normalization: GATE CSE 2002 \| Question: 1.19 | **A** |
| `3.6.18` | Database Normalization: GATE CSE 2002 \| Question: 16 | **N/A** |
| `3.6.19` | Database Normalization: GATE CSE 2002 \| Question: 2.24 | **C** |
| `3.6.20` | Database Normalization: GATE CSE 2002 \| Question: 2.25 | **C** |
| `3.6.21` | Database Normalization: GATE CSE 2003 \| Question: 85 | **D** |
| `3.6.22` | Database Normalization: GATE CSE 2004 \| Question: 50 | **B** |
| `3.6.23` | Database Normalization: GATE CSE 2005 \| Question: 29, UGCNET-June2015-III: 9 | **C** |
| `3.6.24` | Database Normalization: GATE CSE 2006 \| Question: 70 | **C** |
| `3.6.25` | Database Normalization: GATE CSE 2007 \| Question: 62, UGCNET-June2014-II: 47 | **D** |
| `3.6.26` | Database Normalization: GATE CSE 2008 \| Question: 69 | **C** |
| `3.6.27` | Database Normalization: GATE CSE 2012 \| Question: 2 | **C** |
| `3.6.28` | Database Normalization: GATE CSE 2013 \| Question: 54 | **B** |
| `3.6.29` | Database Normalization: GATE CSE 2013 \| Question: 55 | **A** |
| `3.6.30` | Database Normalization: GATE CSE 2014 \| Set 1 \| Question: 21 | **B** |
| `3.6.31` | Database Normalization: GATE CSE 2014 \| Set 1 \| Question: 30 | **A** |
| `3.6.32` | Database Normalization: GATE CSE 2015 \| Set 3 \| Question: 20 | **C** |
| `3.6.33` | Database Normalization: GATE CSE 2016 \| Set 1 \| Question: 21 | **B** |
| `3.6.34` | Database Normalization: GATE CSE 2016 \| Set 1 \| Question: 23 | **B** |
| `3.6.35` | Database Normalization: GATE CSE 2017 \| Set 1 \| Question: 16 | **A** |
| `3.6.36` | Database Normalization: GATE CSE 2018 \| Question: 42 | **B** |
| `3.6.37` | Database Normalization: GATE CSE 2019 \| Question: 32 | **C** |
| `3.6.38` | Database Normalization: GATE CSE 2020 \| Question: 36 | **A** |
| `3.6.39` | Database Normalization: GATE CSE 2021 \| Set 1 \| Question: 33 | **A** |
| `3.6.40` | Database Normalization: GATE CSE 2021 \| Set 2 \| Question: 40 | **A;C;D** |
| `3.6.41` | Database Normalization: GATE CSE 2022 \| Question: 21 | **8** |
| `3.6.42` | Database Normalization: GATE CSE 2022 \| Question: 4 | **A** |
| `3.6.43` | Database Normalization: GATE CSE 2024 \| Set 1 \| Question: 12 | **A;C** |
| `3.6.44` | Database Normalization: GATE CSE 2024 \| Set 1 \| Question: 34 | **B;C;D** |
| `3.6.45` | Database Normalization: GATE CSE 2024 \| Set 2 \| Question: 46 | **50** |
| `3.6.46` | Database Normalization: GATE CSE 2025 \| Set 2 \| Question: 36 | **C;D** |
| `3.6.47` | Database Normalization: GATE CSE 2026 \| Set 1 \| Question: 21 | **A;B;C** |
| `3.6.48` | Database Normalization: GATE DS&AI 2024 \| Question: 36 | **A;B;D** |
| `3.6.49` | 26 | **TBA** |
| `3.6.50` | Database Normalization: GATE IT 2004 \| Question: 75 | **B** |
| `3.6.51` | Database Normalization: GATE IT 2005 \| Question: 22 | **A** |
| `3.6.52` | Database Normalization: GATE IT 2005 \| Question: 70 | **B** |
| `3.6.53` | Database Normalization: GATE IT 2006 \| Question: 60 | **B** |
| `3.6.54` | Database Normalization: GATE IT 2008 \| Question: 61 | **A** |
| `3.6.55` | Database Normalization: GATE IT 2008 \| Question: 62 | **D** |
| `3.6.56` | Database Normalization: GATE2001-1.23, UGCNET-June2012-III: 18 | **C** |
| `3.7.1` | Database Schema: GATE CSE 2026 \| Set 2 \| Question: 5 | **C** |
| `3.8.1` | Decomposition: GATE DA 2025 \| Question: 6 | **C** |
| `3.9.1` | ER Diagram: GATE CSE 2005 \| Question: 75 | **B** |
| `3.9.2` | ER Diagram: GATE CSE 2008 \| Question: 82 | **B** |
| `3.9.3` | ER Diagram: GATE CSE 2008 \| Question: 83 | **A** |
| `3.9.4` | ER Diagram: GATE CSE 2012 \| Question: 14 | **C** |
| `3.9.5` | ER Diagram: GATE CSE 2015 \| Set 1 \| Question: 41 | **4** |
| `3.9.6` | ER Diagram: GATE CSE 2017 \| Set 2 \| Question: 17 | **C** |
| `3.9.7` | ER Diagram: GATE CSE 2018 \| Question: 11 | **A** |
| `3.9.8` | ER Diagram: GATE CSE 2020 \| Question: 14 | **A** |
| `3.9.9` | ER Diagram: GATE CSE 2024 \| Set 1 \| Question: 10 | **D** |
| `3.9.10` | ER Diagram: GATE CSE 2024 \| Set 2 \| Question: 10 | **A** |
| `3.9.11` | ER Diagram: GATE IT 2004 \| Question: 73 | **B** |
| `3.9.12` | ER Diagram: GATE IT 2005 \| Question: 21 | **C** |
| `3.10.1` | Functional Dependency: GATE CSE 2025 \| Set 1 \| Question: 37 | **B;C** |
| `3.10.2` | Functional Dependency: GATE CSE 2026 \| Set 1 \| Question: 20 | **C;D** |
| `3.10.3` | Functional Dependency: GATE DA 2025 \| Question: 47 | **B;D** |
| `3.11.1` | Indexing: GATE CSE 1989 \| Question: 4-xiv | **N/A** |
| `3.11.2` | Indexing: GATE CSE 1990 \| Question: 10b | **N/A** |
| `3.11.3` | Indexing: GATE CSE 1993 \| Question: 14 | **3** |
| `3.11.4` | Indexing: GATE CSE 1998 \| Question: 1.35 | **C** |
| `3.11.5` | Indexing: GATE CSE 2008 \| Question: 16, ISRO2016-60 | **A** |
| `3.11.6` | Indexing: GATE CSE 2008 \| Question: 70 | **C** |
| `3.11.7` | Indexing: GATE CSE 2011 \| Question: 39 | **C** |
| `3.11.8` | Indexing: GATE CSE 2013 \| Question: 15 | **C** |
| `3.11.9` | Indexing: GATE CSE 2015 \| Set 1 \| Question: 24 | **C** |
| `3.11.10` | Indexing: GATE CSE 2020 \| Question: 54 | **4** |
| `3.11.11` | Indexing: GATE CSE 2021 \| Set 2 \| Question: 21 | **698** |
| `3.11.12` | Indexing: GATE CSE 2023 \| Question: 52 | **6** |
| `3.11.13` | Indexing: GATE CSE 2024 \| Set 2 \| Question: 16 | **A;B** |
| `3.11.14` | Indexing: GATE CSE 2026 \| Set 2 \| Question: 36 | **A** |
| `3.11.15` | Indexing: GATE DA 2026 \| Question: 22 | **195:195** |
| `3.12.1` | Joins: GATE CSE 2004 \| Question: 14 | **A** |
| `3.12.2` | Joins: GATE CSE 2012 \| Question: 50 | **A** |
| `3.12.3` | Joins: GATE CSE 2014 \| Set 2 \| Question: 30 | **A** |
| `3.12.4` | Joins: GATE IT 2005 \| Question: 82a | **C** |
| `3.12.5` | Joins: GATE IT 2005 \| Question: 82b | **B** |
| `3.12.6` | Joins: GATE IT 2006 \| Question: 14 | **A** |
| `3.12.7` | Joins: GATE IT 2007 \| Question: 68 | **A** |
| `3.13.1` | Multivalued Dependency 4nf: GATE IT 2007 \| Question: 67 | **C** |
| `3.14.1` | Natural Join: GATE CSE 2005 \| Question: 30 | **C** |
| `3.14.2` | Natural Join: GATE CSE 2010 \| Question: 43 | **A** |
| `3.14.3` | Natural Join: GATE CSE 2015 \| Set 2 \| Question: 32 | **C** |
| `3.15.1` | Normal Forms: GATE DA 2026 \| Question: 51 | **4:4** |
| `3.16.1` | Query: GATE CSE 1997 \| Question: 76-b | **N/A** |
| `3.16.2` | Query: GATE DA 2026 \| Question: 41 | **A** |
| `3.16.3` | Query: GATE DA 2026 \| Question: 50 | **3:3** |
| `3.17.1` | Referential Integrity: GATE CSE 1997 \| Question: 6.10, ISRO2016-54 | **B** |
| `3.17.2` | Referential Integrity: GATE CSE 2005 \| Question: 76 | **C** |
| `3.17.3` | Referential Integrity: GATE CSE 2012 \| Question: 43 | **A** |
| `3.17.4` | Referential Integrity: GATE CSE 2017 \| Set 2 \| Question: 19 | **0.00** |
| `3.17.5` | Referential Integrity: GATE CSE 2021 \| Set 2 \| Question: 6 | **D** |
| `3.17.6` | Referential Integrity: GATE DA 2026 \| Question: 16 | **A;B** |
| `3.18.1` | Relational Algebra: GATE CSE 1992 \| Question: 13b | **N/A** |
| `3.18.2` | Relational Algebra: GATE CSE 1994 \| Question: 13 | **N/A** |
| `3.18.3` | Relational Algebra: GATE CSE 1994 \| Question: 3.8 | **N/A** |
| `3.18.4` | Relational Algebra: GATE CSE 1995 \| Question: 27 | **N/A** |
| `3.18.5` | Relational Algebra: GATE CSE 1996 \| Question: 27 | **N/A** |
| `3.18.6` | Relational Algebra: GATE CSE 1997 \| Question: 76-a | **N/A** |
| `3.18.7` | Relational Algebra: GATE CSE 1998 \| Question: 1.33 | **D** |
| `3.18.8` | Relational Algebra: GATE CSE 1998 \| Question: 27 | **N/A** |
| `3.18.9` | Relational Algebra: GATE CSE 1999 \| Question: 1.18, ISRO2016-53 | **B** |
| `3.18.10` | Relational Algebra: GATE CSE 2000 \| Question: 1.23, ISRO2016-57 | **C** |
| `3.18.11` | Relational Algebra: GATE CSE 2001 \| Question: 1.24 | **D** |
| `3.18.12` | Relational Algebra: GATE CSE 2001 \| Question: 1.25 | **C** |
| `3.18.13` | Relational Algebra: GATE CSE 2001 \| Question: 21-a | **N/A** |
| `3.18.14` | Relational Algebra: GATE CSE 2002 \| Question: 15 | **N/A** |
| `3.18.15` | Relational Algebra: GATE CSE 2003 \| Question: 30 | **A** |
| `3.18.16` | Relational Algebra: GATE CSE 2004 \| Question: 51 | **D** |
| `3.18.17` | Relational Algebra: GATE CSE 2007 \| Question: 59 | **B** |
| `3.18.18` | Relational Algebra: GATE CSE 2008 \| Question: 68 | **D** |
| `3.18.19` | Relational Algebra: GATE CSE 2014 \| Set 3 \| Question: 21 | **A** |
| `3.18.20` | Relational Algebra: GATE CSE 2014 \| Set 3 \| Question: 30 | **D** |
| `3.18.21` | Relational Algebra: GATE CSE 2015 \| Set 1 \| Question: 7 | **D** |
| `3.18.22` | Relational Algebra: GATE CSE 2017 \| Set 1 \| Question: 46 | **4** |
| `3.18.23` | Relational Algebra: GATE CSE 2018 \| Question: 41 | **C** |
| `3.18.24` | Relational Algebra: GATE CSE 2019 \| Question: 55 | **1** |
| `3.18.25` | Relational Algebra: GATE CSE 2021 \| Set 1 \| Question: 27 | **C** |
| `3.18.26` | Relational Algebra: GATE CSE 2022 \| Question: 15 | **A;B** |
| `3.18.27` | Relational Algebra: GATE CSE 2024 \| Set 1 \| Question: 25 | **2** |
| `3.18.28` | Relational Algebra: GATE CSE 2024 \| Set 2 \| Question: 35 | **B** |
| `3.18.29` | Relational Algebra: GATE DA 2025 \| Question: 52 | **1:1** |
| `3.18.30` | Relational Algebra: GATE DA 2025 \| Question: 7 | **C** |
| `3.18.31` | Relational Algebra: GATE DA 2026 \| Question: 32 | **D** |
| `3.18.32` | Relational Algebra: GATE DS&AI 2024 \| Question: 16 | **C** |
| `3.18.33` | Relational Algebra: GATE IT 2005 \| Question: 68 | **B** |
| `3.19.1` | Relational Calculus: GATE CSE 1993 \| Question: 23 | **N/A** |
| `3.19.2` | Relational Calculus: GATE CSE 1998 \| Question: 2.19 | **D** |
| `3.19.3` | Relational Calculus: GATE CSE 1999 \| Question: 1.19 | **C** |
| `3.19.4` | Relational Calculus: GATE CSE 2001 \| Question: 2.24 | **C** |
| `3.19.5` | Relational Calculus: GATE CSE 2002 \| Question: 1.20 | **C** |
| `3.19.6` | Relational Calculus: GATE CSE 2004 \| Question: 13 | **B** |
| `3.19.7` | Relational Calculus: GATE CSE 2007 \| Question: 60 | **C** |
| `3.19.8` | Relational Calculus: GATE CSE 2008 \| Question: 15 | **C** |
| `3.19.9` | Relational Calculus: GATE CSE 2009 \| Question: 45 | **A** |
| `3.19.10` | Relational Calculus: GATE CSE 2013 \| Question: 35 | **A** |
| `3.19.11` | Relational Calculus: GATE IT 2006 \| Question: 15 | **D** |
| `3.19.12` | Relational Calculus: GATE IT 2007 \| Question: 65 | **D** |
| `3.19.13` | Relational Calculus: GATE IT 2008 \| Question: 75 | **C** |
| `3.20.1` | Relational Model: GATE CSE 2023 \| Question: 6 | **A** |
| `3.20.2` | Relational Model: GATE DA 2025 \| Question: 46 | **B;C** |
| `3.21.1` | SQL: GATE CSE 1988 \| Question: 12iii | **N/A** |
| `3.21.2` | SQL: GATE CSE 1988 \| Question: 12iv | **N/A** |
| `3.21.3` | SQL: GATE CSE 1990 \| Question: 10-a | **N/A** |
| `3.21.4` | SQL: GATE CSE 1991 \| Question: 12,b | **N/A** |
| `3.21.5` | SQL: GATE CSE 1991 \| Question: 12-a | **N/A** |
| `3.21.6` | SQL: GATE CSE 1993 \| Question: 24 | **N/A** |
| `3.21.7` | SQL: GATE CSE 1998 \| Question: 7-a | **N/A** |
| `3.21.8` | SQL: GATE CSE 1999 \| Question: 2.25 | **D** |
| `3.21.9` | SQL: GATE CSE 1999 \| Question: 22-a | **N/A** |
| `3.21.10` | SQL: GATE CSE 1999 \| Question: 22-b | **N/A** |
| `3.21.11` | SQL: GATE CSE 2000 \| Question: 2.25 | **A** |
| `3.21.12` | SQL: GATE CSE 2000 \| Question: 2.26 | **C** |
| `3.21.13` | SQL: GATE CSE 2000 \| Question: 22 | **N/A** |
| `3.21.14` | SQL: GATE CSE 2001 \| Question: 2.25 | **C** |
| `3.21.15` | SQL: GATE CSE 2001 \| Question: 21-b | **N/A** |
| `3.21.16` | SQL: GATE CSE 2001 \| Question: 21-c | **N/A** |
| `3.21.17` | SQL: GATE CSE 2003 \| Question: 86 | **C** |
| `3.21.18` | SQL: GATE CSE 2004 \| Question: 53 | **D** |
| `3.21.19` | SQL: GATE CSE 2005 \| Question: 77, ISRO2016-55 | **D** |
| `3.21.20` | SQL: GATE CSE 2006 \| Question: 67 | **C** |
| `3.21.21` | SQL: GATE CSE 2006 \| Question: 68 | **B** |
| `3.21.22` | SQL: GATE CSE 2006 \| Question: 69 | **C** |
| `3.21.23` | SQL: GATE CSE 2007 \| Question: 61 | **A** |
| `3.21.24` | SQL: GATE CSE 2009 \| Question: 55 | **X** |
| `3.21.25` | SQL: GATE CSE 2009 \| Question: 56 | **A** |
| `3.21.26` | SQL: GATE CSE 2010 \| Question: 19 | **C** |
| `3.21.27` | SQL: GATE CSE 2011 \| Question: 32 | **A** |
| `3.21.28` | SQL: GATE CSE 2011 \| Question: 46 | **C** |
| `3.21.29` | SQL: GATE CSE 2012 \| Question: 15 | **C** |
| `3.21.30` | SQL: GATE CSE 2012 \| Question: 51 | **B** |
| `3.21.31` | SQL: GATE CSE 2014 \| Set 1 \| Question: 22 | **D** |
| `3.21.32` | SQL: GATE CSE 2014 \| Set 1 \| Question: 54 | **B** |
| `3.21.33` | SQL: GATE CSE 2014 \| Set 2 \| Question: 54 | **C** |
| `3.21.34` | SQL: GATE CSE 2014 \| Set 3 \| Question: 54 | **D** |
| `3.21.35` | SQL: GATE CSE 2015 \| Set 1 \| Question: 27 | **2** |
| `3.21.36` | SQL: GATE CSE 2015 \| Set 3 \| Question: 3 | **A** |
| `3.21.37` | SQL: GATE CSE 2016 \| Set 2 \| Question: 52 | **2** |
| `3.21.38` | SQL: GATE CSE 2017 \| Set 1 \| Question: 23 | **2.6** |
| `3.21.39` | SQL: GATE CSE 2017 \| Set 2 \| Question: 46 | **7** |
| `3.21.40` | SQL: GATE CSE 2018 \| Question: 12 | **D** |
| `3.21.41` | SQL: GATE CSE 2019 \| Question: 51 | **5** |
| `3.21.42` | SQL: GATE CSE 2020 \| Question: 13 | **A** |
| `3.21.43` | SQL: GATE CSE 2021 \| Set 1 \| Question: 23 | **819** |
| `3.21.44` | SQL: GATE CSE 2021 \| Set 2 \| Question: 31 | **B** |
| `3.21.45` | SQL: GATE CSE 2022 \| Question: 46 | **2** |
| `3.21.46` | SQL: GATE CSE 2023 \| Question: 51 | **2** |
| `3.21.47` | SQL: GATE CSE 2025 \| Set 1 \| Question: 45 | **26:26** |
| `3.21.48` | SQL: GATE CSE 2025 \| Set 2 \| Question: 44 | **A;C;D** |
| `3.21.49` | SQL: GATE DA 2025 \| Question: 23 | **3:3** |
| `3.21.50` | SQL: GATE DS&AI 2024 \| Question: 21 | **3** |
| `3.21.51` | SQL: GATE DS&AI 2024 \| Question: 45 | **A;B** |
| `3.21.52` | SQL: GATE IT 2004 \| Question: 74 | **D** |
| `3.21.53` | SQL: GATE IT 2004 \| Question: 76 | **C** |
| `3.21.54` | SQL: GATE IT 2004 \| Question: 78 | **C** |
| `3.21.55` | SQL: GATE IT 2005 \| Question: 69 | **D** |
| `3.21.56` | SQL: GATE IT 2006 \| Question: 84 | **A** |
| `3.21.57` | SQL: GATE IT 2006 \| Question: 85 | **B** |
| `3.21.58` | SQL: GATE IT 2008 \| Question: 74 | **D** |
| `3.22.1` | Safe Query: GATE CSE 2017 \| Set 1 \| Question: 41 | **D** |
| `3.23.1` | Super Key: GATE CSE 2026 \| Set 1 \| Question: 55 | **6** |
| `3.24.1` | Timestamp Ordering: GATE CSE 2017 \| Set 1 \| Question: 42 | **A** |
| `3.25.1` | Transaction and Concurrency: GATE CS Practice : Transaction Concurrency Control (DBMS) | **TBA** |
| `3.25.2` | Transaction and Concurrency: GATE CSE 1999 \| Question: 2.6 | **D** |
| `3.25.3` | Transaction and Concurrency: GATE CSE 2003 \| Question: 29, ISRO2009-73 | **D** |
| `3.25.4` | Transaction and Concurrency: GATE CSE 2003 \| Question: 87 | **D** |
| `3.25.5` | Transaction and Concurrency: GATE CSE 2006 \| Question: 20, ISRO2015-17 | **B** |
| `3.25.6` | Transaction and Concurrency: GATE CSE 2010 \| Question: 20 | **B** |
| `3.25.8` | Transaction and Concurrency: GATE CSE 2012 \| Question: 27 | **B** |
| `3.25.9` | Transaction and Concurrency: GATE CSE 2015 \| Set 2 \| Question: 1 | **B** |
| `3.25.10` | Transaction and Concurrency: GATE CSE 2015 \| Set 2 \| Question: 46 | **A** |
| `3.25.11` | Transaction and Concurrency: GATE CSE 2015 \| Set 3 \| Question: 29 | **B** |
| `3.25.12` | Transaction and Concurrency: GATE CSE 2016 \| Set 1 \| Question: 22 | **D** |
| `3.25.13` | Transaction and Concurrency: GATE CSE 2016 \| Set 1 \| Question: 51 | **A** |
| `3.25.14` | Transaction and Concurrency: GATE CSE 2016 \| Set 2 \| Question: 22 | **A** |
| `3.25.15` | Transaction and Concurrency: GATE CSE 2016 \| Set 2 \| Question: 51 | **C** |
| `3.25.16` | Transaction and Concurrency: GATE CSE 2019 \| Question: 11 | **C** |
| `3.25.17` | Transaction and Concurrency: GATE CSE 2021 \| Set 1 \| Question: 13 | **A** |
| `3.25.18` | Transaction and Concurrency: GATE CSE 2024 \| Set 2 \| Question: 9 | **A** |
| `3.25.19` | Transaction and Concurrency: GATE CSE 2025 \| Set 1 \| Question: 5 | **C** |
| `3.25.20` | Transaction and Concurrency: GATE CSE 2025 \| Set 2 \| Question: 17 | **B;C** |
| `3.25.21` | Transaction and Concurrency: GATE CSE 2026 \| Set 2 \| Question: 10 | **A** |
| `3.25.22` | Transaction and Concurrency: GATE IT 2004 \| Question: 21 | **C** |
| `3.25.23` | Transaction and Concurrency: GATE IT 2004 \| Question: 77 | **X** |
| `3.25.24` | Transaction and Concurrency: GATE IT 2005 \| Question: 24 | **D** |
| `3.25.25` | Transaction and Concurrency: GATE IT 2005 \| Question: 67 | **D** |
| `3.25.26` | Transaction and Concurrency: GATE IT 2007 \| Question: 66 | **C** |
| `3.25.27` | Transaction and Concurrency: GATE IT 2008 \| Question: 63 | **D** |
| `3.26.1` | Tuple Relational Calculus: GATE CSE 2025 \| Set 1 \| Question: 29 | **A** |
| `3.26.2` | Tuple Relational Calculus: GATE CSE 2026 \| Set 1 \| Question: 33 | **B** |
| `3.26.3` | Tuple Relational Calculus: GATE DA 2026 \| Question: 49 | **2** |
| `3.27.1` | Two Phase Locking Protocol: GATE CSE 2024 \| Set 2 \| Question: 17 | **A;C;D** |

