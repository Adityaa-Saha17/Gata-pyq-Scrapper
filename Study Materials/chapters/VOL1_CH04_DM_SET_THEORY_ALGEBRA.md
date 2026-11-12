# Volume 1 — Chapter 4: Discrete Mathematics: Set Theory & Algebra

- **Source PDF**: [filter1_volume1.pdf](file:///Users/adityaasaha/Documents/Academics/Gate/filter1_volume1.pdf)
- **Total GATE Questions in Chapter**: **173**

---

## 1. Subtopic Weightage & Question Distribution

| Subtopic # | Subtopic Name | Questions |
| :---: | :--- | :---: |
| **4.1** | Binary Operation | 8 |
| **4.2** | Countable Uncountable Set | 2 |
| **4.3** | Functions | 30 |
| **4.5** | Identify Function | 1 |
| **4.6** | Lattice | 10 |
| **4.7** | Mathematical Induction | 2 |
| **4.8** | Number Theory | 7 |
| **4.9** | Onto | 1 |
| **4.11** | Polynomials | 4 |
| **4.12** | Relations | 38 |
| **4.13** | Set Theory | 27 |


---

## 2. Comprehensive GATE CSE Set Theory, Relations, Functions, Posets & Group Theory Reference

### 2.1 Set Theory & Cardinality
- **Power Set $|\mathcal{P}(A)|$**: If $|A| = n$, then $|\mathcal{P}(A)| = 2^n$.
- **Countability**:
  - Countably Infinite ($\aleph_0$): $\mathbb{N}, \mathbb{Z}, \mathbb{Q}$, set of all finite binary strings $\Sigma^*$, set of all C programs / Turing machines.
  - Uncountable ($\mathfrak{c} = 2^{\aleph_0}$): $\mathbb{R}$, $\mathcal{P}(\mathbb{N})$, set of all languages over $\Sigma$ ($2^{\Sigma^*}$), set of all functions $\mathbb{N} \rightarrow \{0, 1\}$.

### 2.2 Relations on a Set $A$ ($|A| = n$)
Total binary relations on $A$: $2^{n^2}$.

| Relation Property | Definition | Exact Number of Relations on $n$ Elements |
| :--- | :--- | :--- |
| **Reflexive** | $\forall a, (a,a) \in R$ | $2^{n(n-1)}$ |
| **Irreflexive** | $\forall a, (a,a) \notin R$ | $2^{n(n-1)}$ |
| **Symmetric** | $(a,b) \in R \implies (b,a) \in R$ | $2^{n(n+1)/2}$ |
| **Antisymmetric** | $(a,b) \in R \land (b,a) \in R \implies a=b$ | $2^n \cdot 3^{n(n-1)/2}$ |
| **Asymmetric** | $(a,b) \in R \implies (b,a) \notin R$ (Irreflexive + Antisymmetric) | $3^{n(n-1)/2}$ |
| **Reflexive & Symmetric** | Diagonal $= 1$, upper $=$ lower | $2^{n(n-1)/2}$ |
| **Reflexive & Antisymmetric** | Diagonal $= 1$, no $(a,b)$ & $(b,a)$ pair | $3^{n(n-1)/2}$ |
| **Equivalence Relation** | Reflexive + Symmetric + Transitive | **Bell Number $B_n = \sum_{k=1}^{n} S(n, k)$** ($B_1=1, B_2=2, B_3=5, B_4=15, B_5=52$) |

### 2.3 Functions ($f: A \rightarrow B$ where $|A| = m, |B| = n$)
- **Total Functions**: $n^m$
- **One-to-One (Injective)**: $P(n, m) = \frac{n!}{(n-m)!}$ if $m \le n$, else $0$.
- **Onto (Surjective)**: $n! \cdot S(m, n) = \sum_{k=0}^{n} (-1)^k \binom{n}{k} (n-k)^m$ if $m \ge n$, else $0$.
- **Bijective (One-to-One & Onto)**: $n!$ if $m = n$, else $0$.
- **Strictly Increasing / Decreasing Functions** from $\{1..m\}$ to $\{1..n\}$: $\binom{n}{m}$.
- **Monotonically Non-Decreasing Functions** from $\{1..m\}$ to $\{1..n\}$: $\binom{n+m-1}{m}$.

### 2.4 Partial Orders (Posets) & Lattices
- **Poset $(P, \preceq)$**: Reflexive + Antisymmetric + Transitive.
- **Hasse Diagram**: Directed edges go upward; self-loops (reflexivity) and transitive edges are omitted.
  - **Minimal / Maximal Elements**: Elements with no element below / above them (at least one always exists in a finite non-empty poset).
  - **Least (Minimum) / Greatest (Maximum) Element**: Unique if it exists; comparable to *every* element.
- **Lattice**: A poset in which every pair of elements $a, b$ has a unique **Least Upper Bound (LUB / Join $a \lor b$)** and **Greatest Lower Bound (GLB / Meet $a \land b$)**.
  - **Distributive Lattice**: Join and meet distribute over each other. A lattice is distributive **iff** it contains no sublattice isomorphic to **$M_3$ (diamond)** or **$N_5$ (pentagon)**.
  - **Complemented Lattice**: Bounded lattice (with $0$ and $1$) where every element $a$ has at least one complement $a'$ such that $a \lor a' = 1$ and $a \land a' = 0$.
  - **Boolean Algebra**: A **Complemented Distributive Lattice**.
    - Every finite Boolean Algebra is isomorphic to $(\mathcal{P}(S), \subseteq)$ and has cardinality **$2^n$** for some $n \ge 1$ (with $n$ atoms).
    - For divisor poset $(D_N, \mid)$: $D_N$ is a **Boolean Algebra iff $N$ is square-free** (product of distinct primes, e.g., $D_{30} = D_{2 \cdot 3 \cdot 5}$ has $2^3 = 8$ divisors).

### 2.5 Algebraic Structures & Group Theory
- **Hierarchy of Algebraic Structures** $(G, *)$:
  1. **Groupoid / Magma**: Closure ($a * b \in G$). Total binary operations on $n$ elements: $n^{n^2}$ (commutative: $n^{n(n+1)/2}$).
  2. **Semigroup**: Closure + Associativity.
  3. **Monoid**: Semigroup + Identity element $e$ (unique).
  4. **Group**: Monoid + Inverse $a^{-1}$ for every element $a \in G$.
  5. **Abelian (Commutative) Group**: Group + Commutativity ($a * b = b * a$).
- **Key Theorems of Finite Groups**:
  - **Lagrange's Theorem**: If $H$ is a subgroup of finite group $G$, then $|H|$ divides $|G|$. Moreover, the order of any element $a \in G$ divides $|G|$, and $a^{|G|} = e$.
  - **Prime Order Group**: Every group of prime order $p$ is **cyclic** and therefore **Abelian**, with $p-1$ generators.
  - **Small Groups**: Every group of order $\le 5$ is Abelian! The **smallest non-Abelian group** is $S_3$ (or $D_3$) of order **$6$**.
  - **Cyclic Group $G = \langle g \rangle$ of Order $n$**:
    - Number of **generators** of $G$ = $\phi(n)$ (Euler's totient function).
    - Number of **subgroups** of $G$ = number of positive divisors $d(n)$ of $n$ (one unique subgroup of order $d$ for each divisor $d \mid n$).
  - **Multiplicative Group $\mathbb{Z}_n^*$**: $\{a \in \{1 \dots n-1\} : \gcd(a, n) = 1\}$ under multiplication $\bmod\, n$ is an Abelian group of order $\phi(n)$. For prime $p$, $|\mathbb{Z}_p^*| = p - 1$ and it is cyclic.

---

## 3. Original PDF Chapter Notes (Preserved Verbatim)

4 Discrete Mathematics: Set Theory & Algebra (173)
Syllabus: Sets, Relations, Functions, Partial orders, Lattices, Monoids, Groups.
Welcome to the "Discrete Mathematics: Set Theory & Algebra" chapter, a cornerstone of computer science that
underpins many advanced topics. This section is crucial for the GATE Computer Science exam, typically accounting for
8-12 marks. Questions often test your foundational understanding of definitions, properties, and the application of
theorems, ranging from direct formula recall to multi-step problem-solving involving logical deduction. Mastering these
concepts is not just about scoring well; it's about building the analytical and problem-solving skills essential for a career
in computing.
Topic-wise Key Concepts
Set Theory
Set theory is the fundamental language for describing collections of objects. It provides the basis for understanding
relations, functions, and many other discrete structures.
Definition and Core Idea:
A set is a well-defined collection of distinct objects, called elements. Sets are typically denoted by capital letters, and
their elements are enclosed in curly braces. The core idea is to classify and manipulate collections of items.
Important Formulas and Results:
Cardinality: The number of elements in a set is denoted by .
Power Set: The set of all subsets of , denoted . If , then .
Principle of Inclusion-Exclusion:
For two sets:
For three sets:
Key Properties and Identities:
Commutative Laws:
Associative Laws:
Distributive Laws:
De Morgan's Laws:
Idempotent Laws:
Identity Laws:
(where is the universal set)
Complement Laws:

*(PDF Page 83)*

Common Pitfalls & Tricky Points:
Confusing elements with sets containing those elements (e.g., but ).
Misinterpreting the empty set . Remember is a subset of every set, and .
Errors in applying De Morgan's Laws or Inclusion-Exclusion for complex scenarios.
Problem-Solving Techniques:
Use Venn diagrams for visualizing set operations and proving identities for up to three sets.
For formal proofs, use element-wise arguments (e.g., to prove , show that if , then ).
Apply the Principle of Inclusion-Exclusion systematically for counting problems involving overlapping sets.
Relations
A relation describes how elements from one set relate to elements of another set (or the same set). It's a fundamental
concept for modeling connections and dependencies.
Definition and Core Idea:
A relation from set to set is a subset of the Cartesian product . If often written . The core idea is to define specific associations between elements.
, we say is related to ,
Important Formulas and Results:
Number of relations: If and , the number of relations from to is .
Types of Relations on a Set :
1. Reflexive: For all , .
2. Irreflexive: For all , .
3. Symmetric: For all , if , then .
4. Antisymmetric: For all , if and , then .
5. Asymmetric: For all , if , then . (Implies irreflexive and antisymmetric).
6. Transitive: For all , if and , then .
Equivalence Relation: A relation that is Reflexive, Symmetric, and Transitive.
Equivalence Class: If is an equivalence relation on , the equivalence class of an element is
. Equivalence classes partition the set .
Partial Order Relation: A relation that is Reflexive, Antisymmetric, and Transitive. (See Partial Order section for
more details).
Key Properties and Identities:
The inverse of a relation is .
Composition of relations: If and , then
.
Common Pitfalls & Tricky Points:
Confusing symmetric with antisymmetric. A relation can be neither, both (only if it contains only pairs but not the other.
Verifying transitivity requires checking all possible chains and .
Forgetting to check reflexivity for equivalence or partial order relations.
), or one

*(PDF Page 84)*

Problem-Solving Techniques:
Represent relations using directed graphs (digraphs) or adjacency matrices, especially for small sets.
To prove a relation is of a certain type, systematically check each property by definition.
For equivalence relations, identify the equivalence classes to understand the partition of the set.
Functions
Functions are special types of relations where each input maps to exactly one output. They are central to all areas of
mathematics and computer science.
Definition and Core Idea:
A function from set (domain) to set (codomain), denoted , assigns to each element exactly
one element . The core idea is a deterministic mapping from inputs to outputs.
Important Formulas and Results:
Range: The set of all actual output values, Types of Functions:
1. Injective (One-to-one): If for all mapped to by at most one element in the domain.
2. Surjective (Onto): For every , there exists at least one such that equal to its codomain .
3. Bijective (One-to-one and Onto): A function that is both injective and surjective.
Inverse Function: A function has an inverse function . Note that .
. Each element in the codomain is
. The range of is
if and only if is bijective. Then
.
Composition of Functions: If and , then is defined as
.
Number of Functions: If and :
Total functions from to :
Injective functions from to : if , else 0.
Bijective functions from to : if , else 0.
Surjective functions from to : , where is the Stirling number of the second kind.
Alternatively, using Inclusion-Exclusion: .
Key Properties and Identities:
Composition of functions is associative: .
If is bijective, then and , where and are identity functions on sets and
respectively.
Common Pitfalls & Tricky Points:
Confusing the codomain with the range.
Incorrectly assuming a function has an inverse when it's not bijective.
Proving surjectivity requires showing that every element in the codomain has a preimage, not just some.
Problem-Solving Techniques:
To prove injectivity, assume and algebraically show .
To prove surjectivity, take an arbitrary from the codomain and show there exists an in the domain such that
.
When counting functions, carefully identify the constraints (injective, surjective, bijective).
Binary Operation
A binary operation combines two elements from a set to produce a third element within the same set. It's the foundation

*(PDF Page 85)*

for algebraic structures like groups and rings.
Definition and Core Idea:
A binary operation on a set is a function core idea is to define an internal way to combine elements.
. For any , is a unique element in . The
Important Formulas and Results:
Properties of a Binary Operation:
1. Closure: For all , . (This is inherent in the definition).
2. Associativity: For all , .
3. Commutativity: For all , .
4. Identity Element: An element such that for all , . If it exists, it is unique.
5. Inverse Element: For an element , an element is its inverse if is the identity element. If an identity exists, inverses are unique for each element.
, where
Key Properties and Identities:
If an identity element exists, it is unique.
If an identity element exists and the operation is associative, then inverses are unique.
Common Pitfalls & Tricky Points:
Forgetting to check closure: the result of the operation must always be in the original set.
Misidentifying the identity element or assuming it always exists.
Assuming commutativity or associativity when not explicitly stated or proven.
Problem-Solving Techniques:
To check properties, test with arbitrary elements or counterexamples.
For finite sets, construct a Cayley table (operation table) to check properties visually.
Group Theory
Group theory studies algebraic structures called groups, which are sets equipped with a binary operation satisfying
specific axioms. It's fundamental in cryptography, coding theory, and physics.
Definition and Core Idea:
A group is a set together with a binary operation that satisfies four axioms:
1. Closure: For all , .
2. Associativity: For all , .
3. Identity Element: There exists an element such that for all , .
4. Inverse Element: For each , there exists an element such that .
The core idea is to formalize symmetry and transformations.
Important Formulas and Results:
Related Structures:
Semigroup: A set with an associative binary operation.
Monoid: A semigroup with an identity element.
Abelian Group (Commutative Group): A group where the operation is commutative ( ).
Subgroup: A non-empty subset of a group is a subgroup if is itself a group under the same operation.
Subgroup Test: is a subgroup of if for all , .
Cyclic Group: A group is cyclic if there exists an element such that every element of can be written as
a power of (i.e., ). is called a generator.
Order of an element: The smallest positive integer such that . If no such exists, the element has infinite

*(PDF Page 86)*

order.
Lagrange's Theorem: If (i.e., ).
Key Properties and Identities:
The identity element is unique.
Every element has a unique inverse.
is a finite group and is a subgroup of , then the order of divides the order of
Common Pitfalls & Tricky Points:
Forgetting to check all four group axioms, especially the existence of inverses for every element.
Confusing the order of an element with the order of the group.
Misapplying Lagrange's Theorem (it states a necessary condition for a subgroup, not a sufficient one).
Problem-Solving Techniques:
To prove a set with an operation is a group, systematically verify all four axioms.
To find subgroups, look for subsets that are closed under the operation and contain the identity and inverses.
Use Lagrange's Theorem to quickly rule out potential subgroup orders.
Identity Function
The identity function is a fundamental concept in functions and algebraic structures, acting as a neutral element for
function composition.
Definition and Core Idea:
For any set , the identity function on , denoted or , is a function , . The core idea is a mapping that leaves elements unchanged.
such that for every element
Important Formulas and Results:
If is any function, then and .
If is a bijective function, then its inverse satisfies and .
Key Properties and Identities:
The identity function is always bijective (one-to-one and onto).
It serves as the identity element for the operation of function composition.
Common Pitfalls & Tricky Points:
Confusing the identity function with a constant function (e.g., Forgetting that the identity function is specific to a set .
).
Problem-Solving Techniques:
Use the properties of the identity function when simplifying compositions or proving inverse relationships.
Lattice
Lattices are special types of partially ordered sets where every pair of elements has a unique "least upper bound" and
"greatest lower bound.
" They are crucial in areas like logic, set theory, and computer science for modeling hierarchical
structures.
Definition and Core Idea:

*(PDF Page 87)*

A poset is a lattice if for every pair of elements ) and greatest lower bound (GLB or meet, denoted elements always have well-defined "closest" common superiors and inferiors.
, both their least upper bound (LUB or join, denoted
) exist and are unique. The core idea is a structure where
Important Formulas and Results:
Join (Supremum): .
Meet (Infimum): .
Types of Lattices:
Distributive Lattice: A lattice where the distributive laws hold:
Complemented Lattice: A bounded lattice (has a greatest element element has a complement such that and .
Boolean Algebra: A distributive and complemented lattice.
and a least element ) where every
Key Properties and Identities:
Idempotent Laws: ,
Commutative Laws: ,
Associative Laws: ,
Absorption Laws: ,
Duality Principle: If a statement is true for a lattice, its dual (exchanging with , with , with ) is also true.
Common Pitfalls & Tricky Points:
Not every poset is a lattice. A poset fails to be a lattice if any pair of elements lacks a unique LUB or GLB.
Distinguishing between maximal/minimal elements and greatest/least elements in a poset (a lattice always has a
greatest and least element if it's bounded).
Problem-Solving Techniques:
Draw Hasse diagrams to visually identify LUBs and GLBs for all pairs.
To check for distributivity, look for sublattices isomorphic to Hasse diagram (they are non-distributive).
(pentagon lattice) or (diamond lattice) in the
Mathematical Induction
Mathematical Induction is a powerful proof technique used to establish the truth of a statement for all natural numbers
(or a subset thereof). It's essential for proving properties of algorithms, data structures, and number theory results.
Definition and Core Idea:
The Principle of Mathematical Induction states that to prove a statement is true for all integers :
1. Base Case: Show that is true.
2. Inductive Hypothesis: Assume that 3. Inductive Step: Show that is true for some arbitrary integer .
is true, using the inductive hypothesis.
The core idea is like a chain reaction: if the first domino falls, and falling dominoes always knock over the next one, then
all dominoes will fall.
Important Formulas and Results:
Principle of Strong Induction:
1. Base Case: Show that is true.
2. Inductive Hypothesis: Assume that integer .
3. Inductive Step: Show that is true for all integers such that , for some arbitrary
is true, using the inductive hypothesis.

*(PDF Page 88)*

Key Properties and Identities:
Both standard and strong induction are equivalent in power; strong induction is often more convenient for proofs
where depends on more than just .
Common Pitfalls & Tricky Points:
Incorrect base case: The statement must hold for the starting value.
Assuming what needs to be proven in the inductive step. The inductive hypothesis must be explicitly used.
Not clearly stating the inductive hypothesis or the inductive step.
Algebraic errors during the inductive step.
Problem-Solving Techniques:
Clearly label each step: Base Case, Inductive Hypothesis, Inductive Step.
In the inductive step, try to manipulate the expression for substituted using the hypothesis.
For inequalities, sometimes it's easier to prove to isolate an instance of that can be
or similar.
Number Theory
Number theory is the study of integers and their properties, including divisibility, prime numbers, and modular arithmetic.
It has direct applications in cryptography, error correction codes, and algorithm analysis.
Definition and Core Idea:
Number theory explores the relationships and properties of integers. The core idea is to understand the structure and
behavior of numbers under various operations.
Important Formulas and Results:
Divisibility: means divides (i.e., for some integer ).
Division Algorithm: For integers (dividend) and (divisor) with , there exist unique integers (quotient)
and (remainder) such that , where .
Greatest Common Divisor (GCD): is the largest integer that divides both and .
Euclidean Algorithm: An efficient method to compute GCD. .
Bézout's Identity: For any integers , there exist integers such that .
Least Common Multiple (LCM): is the smallest positive integer divisible by both and .
Relationship: .
Prime Numbers: A positive integer greater than 1 with exactly two positive divisors: 1 and itself.
Fundamental Theorem of Arithmetic: Every integer greater than 1 can be uniquely represented as a product
of prime numbers (up to the order of factors).
Modular Arithmetic: means . This is an equivalence relation.
Properties:
If and , then and .
Fermat's Little Theorem: If is a prime number and is an integer not divisible by , then .
Also, for any integer .
Euler's Totient Function : Counts the number of positive integers up to that are relatively prime to .
If is the prime factorization of , then .
If is prime, .
Euler's Theorem: If is a positive integer and is an integer relatively prime to (i.e., ), then
.
Key Properties and Identities:
Congruence modulo is an equivalence relation.

*(PDF Page 89)*

The set of integers modulo is prime, is a field.
, , forms a ring under addition and multiplication modulo . If
Common Pitfalls & Tricky Points:
Mistakes in applying modular arithmetic, especially with negative numbers or division. Remember division is not
always well-defined in modular arithmetic (requires modular inverse).
Confusing prime numbers with relatively prime numbers.
Incorrectly calculating for composite numbers.
Problem-Solving Techniques:
Use the Euclidean algorithm for GCD and extended Euclidean algorithm for modular inverses.
Simplify large powers in modular arithmetic using Fermat's Little Theorem or Euler's Theorem.
For divisibility problems, use properties of congruences.
Onto (Surjective Functions)
Onto functions, also known as surjective functions, ensure that every element in the codomain is "hit" by at least one
element from the domain. This property is vital for understanding mappings that cover their entire target set.
Definition and Core Idea:
A function one element codomain.
is said to be onto (or surjective) if for every element (the codomain), there exists at least
(the domain) such that . The core idea is that the function's range completely fills its
Important Formulas and Results:
A function is surjective if and only if .
If and are finite sets, and is surjective, then .
The number of surjective functions from a set of size to a set of size is given by .
Key Properties and Identities:
If and are surjective, then is surjective.
If is surjective, then must be surjective (but need not be).
Common Pitfalls & Tricky Points:
Confusing surjectivity with injectivity. An onto function doesn't require unique preimages.
Failing to demonstrate a preimage for an arbitrary element in the codomain, instead just showing some elements
have preimages.
Problem-Solving Techniques:
To prove a function is surjective, pick an arbitrary that . This often involves solving for .
For finite sets, compare the cardinalities of the domain and codomain. If can exist.
, then show how to construct an such
, no surjective function from to
Partial Order
Partial order relations define a sense of relative order among elements in a set, but not necessarily for every pair. They
are crucial for modeling hierarchies, dependencies, and precedence in computer science (e.g., task scheduling, class
inheritance).
Definition and Core Idea:

*(PDF Page 90)*

A relation on a set is a partial order relation if it is reflexive, antisymmetric, and transitive. A set with a partial
order relation is called a partially ordered set (poset), denoted . The core idea is to establish an ordering
where some elements might be incomparable.
Important Formulas and Results:
Properties of Partial Order:
1. Reflexive: For all , .
2. Antisymmetric: For all , if and , then .
3. Transitive: For all , if and , then .
Comparability: Two elements are comparable if or . Otherwise, they are incomparable.
Total Order (Linear Order): A partial order where every pair of elements is comparable.
Hasse Diagram: A graphical representation of a finite poset, where:
Elements are represented by nodes.
An edge goes upwards from to if and there is no such that (i.e., covers ).
Reflexive loops and transitive edges are omitted.
Elements in a Poset:
Maximal Element: An element such that there is no with and .
Minimal Element: An element such that there is no with and .
Greatest Element (Maximum): An element such that for all , . (If it exists, it is unique).
Least Element (Minimum): An element such that for all , . (If it exists, it is unique).
Upper Bound: For a subset , an element is an upper bound of if for all .
Lower Bound: For a subset , an element is a lower bound of if for all .
Least Upper Bound (LUB / Supremum): The least element among all upper bounds of , denoted .
Greatest Lower Bound (GLB / Infimum): The greatest element among all lower bounds of , denoted .
Key Properties and Identities:
A greatest element is always a maximal element, but a maximal element is not necessarily the greatest. Similarly for
least and minimal elements.
A finite poset always has at least one maximal and one minimal element.
Common Pitfalls & Tricky Points:
Confusing maximal/minimal elements with greatest/least elements. A poset can have multiple maximal elements but
at most one greatest element.
Errors in drawing Hasse diagrams, especially omitting necessary edges or including redundant ones.
Incorrectly identifying LUBs or GLBs for subsets.
Problem-Solving Techniques:
To verify a partial order, systematically check reflexivity, antisymmetry, and transitivity.
Draw Hasse diagrams to visualize the order and identify special elements (maximal, minimal, greatest, least, LUB,
GLB).
For LUB/GLB, first find all upper/lower bounds, then identify the least/greatest among them.
Polynomials
Polynomials are fundamental algebraic expressions used extensively in computer science for modeling, interpolation,
error correction, and algorithm analysis (e.g., complexity). In discrete mathematics, they often appear in contexts like
finite fields and generating functions.
Definition and Core Idea:
A polynomial in a variable is an expression of the form , where are
coefficients (often real or complex numbers, but can be from finite fields in discrete math) and is a non-negative
integer called the degree of the polynomial (if ). The core idea is to represent relationships using sums of powers
of a variable.
Important Formulas and Results:

*(PDF Page 91)*

Degree: The highest power of with a non-zero coefficient.
Root (or Zero): A value such that .
Polynomial Division Algorithm: For polynomials (dividend) and (divisor) with , there exist
unique polynomials (quotient) and (remainder) such that , where
or .
Remainder Theorem: If a polynomial is divided by , the remainder is .
Factor Theorem: is a factor of if and only if (i.e., is a root of ).
Fundamental Theorem of Algebra: Every non-constant polynomial with complex coefficients has at least one
complex root. Consequently, a polynomial of degree has exactly complex roots (counting multiplicity).
Vieta's Formulas: Relate the coefficients of a polynomial to the sums and products of its roots. For a quadratic
with roots : , .
Key Properties and Identities:
A polynomial of degree has at most distinct roots.
Polynomials form a ring under addition and multiplication.
Common Pitfalls & Tricky Points:
Algebraic errors in polynomial division or evaluating polynomials.
Forgetting to count root multiplicities when applying the Fundamental Theorem of Algebra.
Not considering the domain of coefficients (e.g., real vs. complex vs. finite field).
Problem-Solving Techniques:
Use synthetic division for quick division by .
Apply the Remainder and Factor Theorems to find roots or factors efficiently.
For problems involving roots, Vieta's formulas can often provide shortcuts.
Quick Formula Reference
Set Theory:
De Morgan's Laws: ,
Relations:
Number of relations from to :
Equivalence Relation: Reflexive, Symmetric, Transitive.
Partial Order: Reflexive, Antisymmetric, Transitive.
Functions (from to ):
Total functions:
Injective functions: (if )
Bijective functions: (if )
Surjective functions:
Identity function
Group Theory:
Group Axioms: Closure, Associativity, Identity, Inverse.
Lagrange's Theorem: for subgroup of group .
Lattice:
Poset where every pair has unique LUB (join ) and GLB (meet ).
Distributive Lattice: , etc.
Mathematical Induction:
Base Case , Inductive Hypothesis , Inductive Step .
Number Theory:
Division Algorithm: ,
Fermat's Little Theorem: (for prime , )

*(PDF Page 92)*

Euler's Totient Function:
Euler's Theorem: (for )
Polynomials:
Remainder Theorem:
Factor Theorem: is a factor
Important Tips for GATE
1. Master Definitions and Properties: Many GATE questions directly test your understanding of definitions (e.g.,
what makes a relation symmetric?) and properties (e.g., De Morgan's laws). Memorize them thoroughly.
2. Practice with Hasse Diagrams: For partial orders and lattices, drawing Hasse diagrams is crucial. Practice
identifying maximal/minimal elements, greatest/least elements, and LUB/GLB from diagrams.
3. Systematic Verification: When asked to check if a structure is a group, a relation is an equivalence relation, or a
function is bijective, systematically go through each axiom/property. Don't skip steps or assume properties.
4. Number Theory Shortcuts: Familiarize yourself with the Euclidean algorithm for GCD, modular arithmetic
properties, and theorems like Fermat's Little Theorem and Euler's Theorem. These are vital for efficiently solving
problems involving large numbers or powers.
5. Inclusion-Exclusion Principle: This principle is frequently tested for counting problems in set theory and functions
(especially surjective functions). Practice applying it for 2, 3, and general cases.
6. Mathematical Induction Structure: Always clearly state your base case, inductive hypothesis, and inductive step.
Ensure your inductive step explicitly uses the inductive hypothesis to avoid circular reasoning.
7. Cardinality vs. Countability: Understand the difference between finite, countably infinite, and uncountable sets. Be
familiar with standard examples (e.g., are countable; are uncountable) and Cantor's
diagonalization argument.
8. Watch for "If and Only If": Pay close attention to conditions that are "if and only if" (iff) as they imply equivalence
and are often key to proving properties or identifying specific structures.

---

## 4. Complete Question Index & Answer Key Record (173 Questions)

| Q # | Question Source / Title | Answer Key |
| :---: | :--- | :---: |
| `4.1.1` | Binary Operation: GATE CSE 1989 \| Question: 1-v | **N/A** |
| `4.1.2` | Binary Operation: GATE CSE 1994 \| Question: 2.2 | **N/A** |
| `4.1.3` | Binary Operation: GATE CSE 2003 \| Question: 38 | **C** |
| `4.1.4` | Binary Operation: GATE CSE 2006 \| Question: 28 | **D** |
| `4.1.5` | Binary Operation: GATE CSE 2013 \| Question: 1 | **A** |
| `4.1.6` | Binary Operation: GATE CSE 2015 \| Set 1 \| Question: 28 | **A** |
| `4.1.7` | Binary Operation: GATE CSE 2015 \| Set 3 \| Question: 2 | **B** |
| `4.1.8` | Binary Operation: GATE IT 2006 \| Question: 2 | **A** |
| `4.2.1` | Countable Uncountable Set: GATE CSE 1994 \| Question: 3.9 | **True** |
| `4.2.2` | Countable Uncountable Set: GATE CSE 2018 \| Question: 27 | **D** |
| `4.3.1` | Functions: GATE CSE 1987 \| Question: 9b | **N/A** |
| `4.3.2` | Functions: GATE CSE 1988 \| Question: 13ii | **N/A** |
| `4.3.3` | Functions: GATE CSE 1989 \| Question: 13c | **N/A** |
| `4.3.4` | Functions: GATE CSE 1993 \| Question: 8.6 | **B** |
| `4.3.5` | Functions: GATE CSE 1996 \| Question: 1.3 | **A** |
| `4.3.6` | Functions: GATE CSE 1996 \| Question: 2.1 | **C** |
| `4.3.7` | Functions: GATE CSE 1997 \| Question: 13 | **N/A** |
| `4.3.8` | Functions: GATE CSE 1998 \| Question: 1.8 | **C** |
| `4.3.9` | Functions: GATE CSE 2001 \| Question: 2.3 | **A** |
| `4.3.10` | Functions: GATE CSE 2001 \| Question: 4 | **N/A** |
| `4.3.11` | Functions: GATE CSE 2003 \| Question: 37 | **A** |
| `4.3.12` | Functions: GATE CSE 2003 \| Question: 39 | **B** |
| `4.3.13` | Functions: GATE CSE 2005 \| Question: 43 | **B** |
| `4.3.14` | Functions: GATE CSE 2006 \| Question: 2 | **D** |
| `4.3.15` | Functions: GATE CSE 2006 \| Question: 25 | **B** |
| `4.3.16` | Functions: GATE CSE 2007 \| Question: 3 | **C** |
| `4.3.17` | Functions: GATE CSE 2012 \| Question: 37 | **C** |
| `4.3.18` | Functions: GATE CSE 2014 \| Set 1 \| Question: 50 | **16** |
| `4.3.19` | Functions: GATE CSE 2014 \| Set 3 \| Question: 2 | **D** |
| `4.3.20` | Functions: GATE CSE 2014 \| Set 3 \| Question: 49 | **B** |
| `4.3.21` | Functions: GATE CSE 2015 \| Set 1 \| Question: 5 | **A** |
| `4.3.22` | Functions: GATE CSE 2015 \| Set 2 \| Question: 40 | **36** |
| `4.3.23` | Functions: GATE CSE 2015 \| Set 2 \| Question: 54 | **0.95** |
| `4.3.24` | Functions: GATE CSE 2016 \| Set 1 \| Question: 28 | **2** |
| `4.3.25` | Functions: GATE CSE 2021 \| Set 2 \| Question: 11 | **B;C** |
| `4.3.26` | Functions: GATE CSE 2023 \| Question: 39 | **B;C;D** |
| `4.3.27` | Functions: GATE CSE 2024 \| Set 1 \| Question: 22 | **2** |
| `4.3.28` | Functions: GATE DA 2026 \| Question: 23 | **10:10** |
| `4.3.29` | Functions: GATE IT 2005 \| Question: 31 | **C** |
| `4.3.30` | Functions: GATE IT 2006 \| Question: 6 | **D** |
| `4.4.1` | Group Theory: GATE CSE 1988 \| Question: 2xviii | **N/A** |
| `4.4.2` | Group Theory: GATE CSE 1990 \| Question: 2-x | **N/A** |
| `4.4.3` | Group Theory: GATE CSE 1992 \| Question: 14a | **N/A** |
| `4.4.4` | Group Theory: GATE CSE 1993 \| Question: 28 | **N/A** |
| `4.4.5` | Group Theory: GATE CSE 1994 \| Question: 1.10 | **C** |
| `4.4.6` | Group Theory: GATE CSE 1995 \| Question: 2.17 | **D** |
| `4.4.7` | Group Theory: GATE CSE 1995 \| Question: 21 | **N/A** |
| `4.4.8` | Group Theory: GATE CSE 1996 \| Question: 1.4 | **C** |
| `4.4.9` | Group Theory: GATE CSE 1996 \| Question: 2.4 | **C** |
| `4.4.10` | Group Theory: GATE CSE 1997 \| Question: 3.1 | **D** |
| `4.4.11` | Group Theory: GATE CSE 1998 \| Question: 12 | **N/A** |
| `4.4.12` | Group Theory: GATE CSE 1999 \| Question: 4 | **N/A** |
| `4.4.13` | Group Theory: GATE CSE 2000 \| Question: 4 | **N/A** |
| `4.4.14` | Group Theory: GATE CSE 2002 \| Question: 1.6 | **B** |
| `4.4.15` | Group Theory: GATE CSE 2003 \| Question: 7 | **A** |
| `4.4.16` | Group Theory: GATE CSE 2004 \| Question: 72 | **D** |
| `4.4.17` | Group Theory: GATE CSE 2005 \| Question: 13 | **C** |
| `4.4.18` | Group Theory: GATE CSE 2005 \| Question: 46 | **A** |
| `4.4.19` | Group Theory: GATE CSE 2006 \| Question: 3 | **C** |
| `4.4.20` | Group Theory: GATE CSE 2007 \| Question: 21 | **A** |
| `4.4.21` | Group Theory: GATE CSE 2009 \| Question: 1 | **A** |
| `4.4.22` | Group Theory: GATE CSE 2009 \| Question: 22 | **C** |
| `4.4.23` | Group Theory: GATE CSE 2010 \| Question: 4 | **A** |
| `4.4.24` | Group Theory: GATE CSE 2014 \| Set 3 \| Question: 3 | **5** |
| `4.4.25` | Group Theory: GATE CSE 2014 \| Set 3 \| Question: 50 | **4** |
| `4.4.26` | Group Theory: GATE CSE 2018 \| Question: 19 | **42** |
| `4.4.27` | Group Theory: GATE CSE 2019 \| Question: 10 | **B** |
| `4.4.28` | Group Theory: GATE CSE 2020 \| Question: 18 | **7** |
| `4.4.29` | Group Theory: GATE CSE 2021 \| Set 1 \| Question: 34 | **B** |
| `4.4.30` | Group Theory: GATE CSE 2022 \| Question: 17 | **A;B;C** |
| `4.4.31` | Group Theory: GATE CSE 2023 \| Question: 41 | **A;D** |
| `4.4.32` | Group Theory: GATE CSE 2024 \| Set 1 \| Question: 42 | **B;D** |
| `4.4.33` | Group Theory: GATE CSE 2024 \| Set 2 \| Question: 53 | **4** |
| `4.5.1` | Identify Function: GATE CSE 2025 \| Set 1 \| Question: 39 | **B** |
| `4.6.1` | Lattice: GATE CSE 1988 \| Question: 1vii | **N/A** |
| `4.6.2` | Lattice: GATE CSE 1990 \| Question: 17c | **N/A** |
| `4.6.3` | Lattice: GATE CSE 1992 \| Question: 14b | **D** |
| `4.6.4` | Lattice: GATE CSE 1994 \| Question: 2.9 | **5** |
| `4.6.5` | Lattice: GATE CSE 1997 \| Question: 3.3 | **B** |
| `4.6.6` | Lattice: GATE CSE 2002 \| Question: 4 | **N/A** |
| `4.6.7` | Lattice: GATE CSE 2005 \| Question: 9 | **B** |
| `4.6.8` | Lattice: GATE CSE 2015 \| Set 1 \| Question: 34 | **D** |
| `4.6.9` | Lattice: GATE CSE 2017 \| Set 2 \| Question: 21 | **0** |
| `4.6.10` | Lattice: GATE IT 2008 \| Question: 28 | **A** |
| `4.7.1` | Mathematical Induction: GATE CSE 1995 \| Question: 23 | **N/A** |
| `4.7.2` | Mathematical Induction: GATE CSE 2000 \| Question: 3 | **N/A** |
| `4.8.1` | Number Theory: GATE CSE 1995 \| Question: 7(A) | **24** |
| `4.8.2` | Number Theory: GATE CSE 2014 \| Set 2 \| Question: 49 | **8** |
| `4.8.3` | Number Theory: GATE CSE 2015 \| Set 2 \| Question: 9 | **36** |
| `4.8.4` | Number Theory: GATE IT 2005 \| Question: 34 | **D** |
| `4.8.5` | Number Theory: GATE IT 2007 \| Question: 16 | **D** |
| `4.8.6` | Number Theory: GATE IT 2008 \| Question: 24 | **C** |
| `4.8.7` | Number Theory: GATE1991-15,a | **N/A** |
| `4.9.1` | Onto: GATE CSE 2025 \| Set 1 \| Question: 7 | **D** |
| `4.10.1` | Partial Order: GATE CSE 1991 \| Question: 01,xiv | **N/A** |
| `4.10.2` | Partial Order: GATE CSE 1993 \| Question: 8.5 | **E** |
| `4.10.3` | Partial Order: GATE CSE 1996 \| Question: 1.2 | **B** |
| `4.10.4` | Partial Order: GATE CSE 1997 \| Question: 6.1 | **A** |
| `4.10.5` | Partial Order: GATE CSE 1998 \| Question: 11 | **N/A** |
| `4.10.6` | Partial Order: GATE CSE 2003 \| Question: 31 | **D** |
| `4.10.7` | Partial Order: GATE CSE 2004 \| Question: 73 | **A** |
| `4.10.8` | Partial Order: GATE CSE 2007 \| Question: 26 | **C** |
| `4.10.9` | Partial Order: GATE CSE 2024 \| Set 2 \| Question: 24 | **5** |
| `4.10.10` | Partial Order: GATE IT 2007 \| Question: 23 | **D** |
| `4.11.1` | Polynomials: GATE CSE 1997 \| Question: 4.4 | **B** |
| `4.11.2` | Polynomials: GATE CSE 2000 \| Question: 2.4 | **D** |
| `4.11.3` | Polynomials: GATE CSE 2014 \| Set 2 \| Question: 5 | **A** |
| `4.11.4` | Polynomials: GATE CSE 2017 \| Set 2 \| Question: 24 | **8** |
| `4.12.1` | Relations: GATE CSE 1987 \| Question: 2d | **False** |
| `4.12.2` | Relations: GATE CSE 1987 \| Question: 9a | **N/A** |
| `4.12.3` | Relations: GATE CSE 1987 \| Question: 9e | **N/A** |
| `4.12.4` | Relations: GATE CSE 1989 \| Question: 1-iv | **N/A** |
| `4.12.5` | Relations: GATE CSE 1992 \| Question: 15.b | **N/A** |
| `4.12.6` | Relations: GATE CSE 1994 \| Question: 2.3 | **N/A** |
| `4.12.7` | Relations: GATE CSE 1995 \| Question: 1.19 | **D** |
| `4.12.8` | Relations: GATE CSE 1996 \| Question: 2.2 | **B** |
| `4.12.9` | Relations: GATE CSE 1996 \| Question: 8 | **N/A** |
| `4.12.10` | Relations: GATE CSE 1997 \| Question: 14 | **N/A** |
| `4.12.11` | Relations: GATE CSE 1997 \| Question: 6.3 | **A** |
| `4.12.12` | Relations: GATE CSE 1998 \| Question: 1.6 | **B** |
| `4.12.13` | Relations: GATE CSE 1998 \| Question: 1.7 | **C** |
| `4.12.14` | Relations: GATE CSE 1998 \| Question: 10a | **N/A** |
| `4.12.15` | Relations: GATE CSE 1998 \| Question: 10b | **N/A** |
| `4.12.16` | Relations: GATE CSE 1998 \| Question: 2.3 | **B** |
| `4.12.17` | Relations: GATE CSE 1999 \| Question: 1.2 | **C** |
| `4.12.18` | Relations: GATE CSE 1999 \| Question: 2.3 | **A;C** |
| `4.12.19` | Relations: GATE CSE 1999 \| Question: 3 | **N/A** |
| `4.12.20` | Relations: GATE CSE 2000 \| Question: 2.5 | **C** |
| `4.12.21` | Relations: GATE CSE 2001 \| Question: 1.2 | **B** |
| `4.12.22` | Relations: GATE CSE 2002 \| Question: 2.17 | **D** |
| `4.12.23` | Relations: GATE CSE 2002 \| Question: 3 | **N/A** |
| `4.12.24` | Relations: GATE CSE 2004 \| Question: 24 | **B** |
| `4.12.25` | Relations: GATE CSE 2005 \| Question: 42 | **C** |
| `4.12.26` | Relations: GATE CSE 2005 \| Question: 7 | **D** |
| `4.12.27` | Relations: GATE CSE 2006 \| Question: 4 | **A** |
| `4.12.28` | Relations: GATE CSE 2007 \| Question: 2 | **B** |
| `4.12.29` | Relations: GATE CSE 2009 \| Question: 4 | **D** |
| `4.12.30` | Relations: GATE CSE 2010 \| Question: 3 | **C** |
| `4.12.31` | Relations: GATE CSE 2015 \| Set 2 \| Question: 16 | **D** |
| `4.12.32` | Relations: GATE CSE 2015 \| Set 3 \| Question: 41 | **C** |
| `4.12.33` | Relations: GATE CSE 2016 \| Set 2 \| Question: 26 | **B** |
| `4.12.34` | Relations: GATE CSE 2020 \| Question: 17 | **0.1249:0.1259** |
| `4.12.35` | Relations: GATE CSE 2021 \| Set 1 \| Question: 43 | **C** |
| `4.12.36` | Relations: GATE CSE 2025 \| Set 2 \| Question: 32 | **B;C** |
| `4.12.37` | Relations: GATE CSE 2026 \| Set 2 \| Question: 16 | **A;B;C** |
| `4.12.38` | Relations: GATE IT 2004 \| Question: 4 | **C** |
| `4.13.1` | Set Theory: GATE CSE 1993 \| Question: 17 | **N/A** |
| `4.13.2` | Set Theory: GATE CSE 1993 \| Question: 8.3 | **C** |
| `4.13.3` | Set Theory: GATE CSE 1993 \| Question: 8.4 | **B** |
| `4.13.4` | Set Theory: GATE CSE 1994 \| Question: 2.4 | **N/A** |
| `4.13.5` | Set Theory: GATE CSE 1995 \| Question: 1.20 | **C** |
| `4.13.6` | Set Theory: GATE CSE 1995 \| Question: 25b | **192** |
| `4.13.7` | Set Theory: GATE CSE 1996 \| Question: 1.1 | **A** |
| `4.13.8` | Set Theory: GATE CSE 1998 \| Question: 2.4 | **D** |
| `4.13.9` | Set Theory: GATE CSE 2000 \| Question: 2.6 | **B** |
| `4.13.10` | Set Theory: GATE CSE 2000 \| Question: 6 | **N/A** |
| `4.13.11` | Set Theory: GATE CSE 2001 \| Question: 2.2 | **C** |
| `4.13.12` | Set Theory: GATE CSE 2001 \| Question: 3 | **N/A** |
| `4.13.13` | Set Theory: GATE CSE 2005 \| Question: 8 | **A** |
| `4.13.14` | Set Theory: GATE CSE 2006 \| Question: 22 | **C** |
| `4.13.15` | Set Theory: GATE CSE 2006 \| Question: 24 | **C** |
| `4.13.16` | Set Theory: GATE CSE 2008 \| Question: 2 | **D** |
| `4.13.17` | Set Theory: GATE CSE 2014 \| Set 2 \| Question: 50 | **A** |
| `4.13.18` | Set Theory: GATE CSE 2015 \| Set 1 \| Question: 16 | **C** |
| `4.13.19` | Set Theory: GATE CSE 2015 \| Set 2 \| Question: 18 | **2048** |
| `4.13.20` | Set Theory: GATE CSE 2015 \| Set 3 \| Question: 23 | **D** |
| `4.13.21` | Set Theory: GATE CSE 2016 \| Set 2 \| Question: 28 | **B** |
| `4.13.22` | Set Theory: GATE CSE 2017 \| Set 1 \| Question: 47 | **271** |
| `4.13.23` | Set Theory: GATE CSE 2021 \| Set 2 \| Question: 37 | **B** |
| `4.13.24` | Set Theory: GATE IT 2004 \| Question: 2 | **C** |
| `4.13.25` | Set Theory: GATE IT 2005 \| Question: 33 | **B** |
| `4.13.26` | Set Theory: GATE IT 2006 \| Question: 23 | **C** |
| `4.13.27` | Set Theory: GATE IT 2006 \| Question: 24 | **B** |

