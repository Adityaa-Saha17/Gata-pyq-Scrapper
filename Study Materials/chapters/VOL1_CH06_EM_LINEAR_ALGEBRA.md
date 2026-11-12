# Volume 1 — Chapter 6: Engineering Mathematics: Linear Algebra

- **Source PDF**: [filter1_volume1.pdf](file:///Users/adityaasaha/Documents/Academics/Gate/filter1_volume1.pdf)
- **Total GATE Questions in Chapter**: **112**

---

## 1. Subtopic Weightage & Question Distribution

| Subtopic # | Subtopic Name | Questions |
| :---: | :--- | :---: |
| **6.1** | Cartesian Coordinates | 1 |
| **6.3** | Eigen Value | 33 |
| **6.4** | Gaussian Elimination | 1 |
| **6.5** | Lu Decomposition | 3 |
| **6.6** | Matrix | 24 |
| **6.7** | Multiplicity | 1 |
| **6.8** | Orthonormality | 2 |
| **6.9** | Rank of Matrix | 7 |
| **6.10** | Singular Value Decomposition | 1 |
| **6.11** | Statistics | 2 |
| **6.13** | System of Equations | 17 |
| **6.14** | Vector Space | 7 |


---

## 2. Comprehensive GATE CSE Linear Algebra Reference (Expanded Research & Formulas)

### 2.1 Determinants, Rank & Nullity
- **Determinant Properties ($A, B \in \mathbb{R}^{n \times n}$)**:
  - $|AB| = |A||B|$, $|A^T| = |A|$, $|A^{-1}| = 1/|A|$, $|kA| = k^n |A|$.
  - $|	ext{adj}(A)| = |A|^{n-1}$, $\text{adj}(\text{adj}(A)) = |A|^{n-2} A$.
  - For block triangular matrix $\begin{pmatrix} A & B \\ 0 & D \end{pmatrix}$, $\det = \det(A)\det(D)$.
- **Rank-Nullity Theorem** for $A \in \mathbb{R}^{m \times n}$:
  $$\text{rank}(A) + \text{nullity}(A) = n \quad (\text{number of columns})$$
- **Rank Inequalities**:
  - $\text{rank}(A_{m \times n}) \le \min(m, n)$
  - $\text{rank}(A + B) \le \text{rank}(A) + \text{rank}(B)$
  - $\text{rank}(A) + \text{rank}(B) - n \le \text{rank}(AB) \le \min(\text{rank}(A), \text{rank}(B))$ *(Sylvester's Inequality)*
  - $\text{rank}(A^T A) = \text{rank}(A A^T) = \text{rank}(A)$

### 2.2 Systems of Linear Equations ($Ax = b$, $A \in \mathbb{R}^{m \times n}$)
Let $[A \mid b]$ be the augmented matrix:

| Condition | Consistency | Number of Solutions |
| :--- | :--- | :--- |
| $\text{rank}(A) < \text{rank}([A \mid b])$ | **Inconsistent** | **$0$ (No solution)** |
| $\text{rank}(A) = \text{rank}([A \mid b]) = n$ | **Consistent** | **Unique solution** |
| $\text{rank}(A) = \text{rank}([A \mid b]) = r < n$ | **Consistent** | **Infinitely many solutions** ($n - r$ free variables) |

- **Homogeneous System ($Ax = 0$)**: Always consistent ($x = 0$ is trivial solution).
  - Dimension of solution space (Null space) = $n - \text{rank}(A)$ = number of linearly independent solutions.
  - Non-trivial solution exists **iff** $\text{rank}(A) < n$ (for square $A$: $\det(A) = 0$).

### 2.3 Eigenvalues & Eigenvectors ($Ax = \lambda x$)
- **Characteristic Equation**: $\det(A - \lambda I) = 0$.
- **Golden Eigenvalue Identities** (for eigenvalues $\lambda_1, \lambda_2, \dots, \lambda_n$ of $A_{n \times n}$):
  1. **Sum of Eigenvalues**: $\sum_{i=1}^{n} \lambda_i = \text{Trace}(A) = \sum_{i=1}^{n} a_{ii}$
  2. **Product of Eigenvalues**: $\prod_{i=1}^{n} \lambda_i = \det(A)$
  3. Eigenvalues of $A^T$: $\lambda_i$
  4. Eigenvalues of $kA$: $k\lambda_i$
  5. Eigenvalues of $A + kI$: $\lambda_i + k$
  6. Eigenvalues of $A^m$ (or polynomial $P(A)$): $\lambda_i^m$ (or $P(\lambda_i)$)
  7. Eigenvalues of $A^{-1}$: $1/\lambda_i$
  8. Eigenvalues of $\text{adj}(A)$: $\det(A)/\lambda_i$
- **Eigenvalues of Special Matrices**:
  - **Triangular / Diagonal Matrix**: Diagonal entries $a_{11}, a_{22}, \dots, a_{nn}$.
  - **Real Symmetric Matrix ($A^T = A$)**: All eigenvalues are **real**; eigenvectors of distinct eigenvalues are **orthogonal**; always diagonalizable ($	ext{AM} = 	ext{GM}$).
  - **Skew-Symmetric Matrix ($A^T = -A$)**: Eigenvalues are $0$ or purely imaginary; diagonal entries are $0$.
  - **Orthogonal Matrix ($A^T A = I$)**: $|\lambda_i| = 1$; $\det(A) = \pm 1$.
  - **Idempotent Matrix ($A^2 = A$)**: Eigenvalues are $0$ or $1$; $\text{rank}(A) = \text{Trace}(A)$.
  - **Nilpotent Matrix ($A^k = 0$)**: All eigenvalues are $0$; $\text{Trace}(A) = 0$.
  - **Involutory Matrix ($A^2 = I$)**: Eigenvalues are $+1$ or $-1$.
  - **Rank-1 Matrix / All-Constant Matrix** ($a_{ij} = c$): One eigenvalue is $nc$, and $(n-1)$ eigenvalues are $0$.
- **Cayley-Hamilton Theorem**: Every square matrix satisfies its own characteristic equation $P(A) = 0$.
- **Algebraic vs Geometric Multiplicity**: $1 \le \text{GM}(\lambda) = n - \text{rank}(A - \lambda I) \le \text{AM}(\lambda)$. Matrix is diagonalizable iff $\text{GM}(\lambda) = \text{AM}(\lambda)$ for all $\lambda$.

### 2.4 LU Decomposition, Quadratic Forms & SVD
- **LU Decomposition ($A = LU$)**: $L$ = unit lower triangular, $U$ = upper triangular (from Gaussian elimination without row swaps; multiplier $l_{ij} = m_{ij}$).
- **Positive Definite Symmetric Matrix ($x^T A x > 0$ for all $x \neq 0$)**:
  - All eigenvalues $\lambda_i > 0$, AND all leading principal minors $\Delta_1, \Delta_2, \dots, \Delta_n > 0$.

---

## 3. Original PDF Chapter Notes (Preserved Verbatim)

6 Engineering Mathematics: Linear Algebra (112)
Syllabus: Matrices, determinants, System of linear equations, Eigenvalues and eigenvectors, LU
decomposition.
Welcome to the "Engineering Mathematics: Linear Algebra" chapter of your GATE Computer Science preparation. This
section serves as a comprehensive, exam-focused reference to help you master the fundamental concepts and
problem-solving techniques essential for success.
Subject Overview
Linear Algebra is the branch of mathematics concerning vector spaces and linear mappings between such spaces. It is
a cornerstone of modern computing, underpinning areas like machine learning (e.g., PCA, SVMs, neural networks),
computer graphics, data science, algorithm design, and optimization. For GATE CS, Linear Algebra typically contributes
a significant portion of the Engineering Mathematics section, often carrying 3-5 marks out of the total 8-10 marks
allocated to mathematics. Questions can range from direct computational problems (e.g., finding determinants,
eigenvalues, ranks) to conceptual understanding (e.g., properties of vector spaces, subspaces, consistency of systems
of equations) and application-based scenarios. Proficiency in this subject is not just about scoring marks but also about
building a strong mathematical foundation for advanced computer science topics.
Topic-wise Key Concepts
Cartesian Coordinates
Cartesian coordinates provide a way to uniquely specify the position of a point in a space using numerical values. In 2D,
a point is defined by its distance from two perpendicular axes (x, y), and in 3D, by its distance from three mutually
perpendicular axes (x, y, z).
Definition: A system that uses an ordered set of numbers (coordinates) to specify the location of a point in a space.
For a 2D plane, it's ; for 3D space, it's .
Distance Formula (2D): The distance between two points and is given by:
Distance Formula (3D): The distance between two points and is given by:
Midpoint Formula (2D): The midpoint of a line segment connecting and is:
Properties:
Allows geometric problems to be translated into algebraic ones.
Forms the basis for vector representation and operations.
Common Pitfalls:
Confusing x and y coordinates, especially when dealing with transformations.
Incorrectly applying distance or midpoint formulas.
Problem-Solving Techniques:
Visualize the points and vectors in the coordinate system.
Break down complex geometric problems into simpler algebraic calculations.
Determinant

*(PDF Page 153)*

The determinant is a scalar value that can be computed from the elements of a square matrix. It provides crucial
information about the matrix, such as its invertibility and the volume scaling factor of the linear transformation it
represents.
Definition: A scalar value associated with a square matrix , denoted as Formulas:
1. For a matrix: If , then .
or .
2. For a matrix (Sarrus' Rule): If , then
. This can also be written as .
3. General matrix (Laplace Expansion/Cofactor Expansion): (along row )
(along column ) where is the minor (determinant of the submatrix obtained
or Properties:
by deleting row and column ).
for an matrix and scalar .
If a matrix has a row or column of zeros, its determinant is 0.
If a matrix has two identical rows or columns, its determinant is 0.
If a matrix is triangular (upper or lower), its determinant is the product of its diagonal elements.
Swapping two rows/columns changes the sign of the determinant.
Adding a multiple of one row/column to another row/column does not change the determinant.
A square matrix is invertible if and only if .
Common Pitfalls:
Sign errors in cofactor expansion.
Incorrectly applying properties, especially for scalar multiplication .
Assuming (which is generally false).
Problem-Solving Techniques:
For larger matrices, use row/column operations to create zeros and simplify the calculation before applying
cofactor expansion (e.g., make it triangular).
Exploit properties (e.g., identical rows/columns, triangular form) to quickly find the determinant.
Choose the row or column with the most zeros for cofactor expansion.
Eigen Value
Eigenvalues are special scalar values associated with a square matrix that characterize its fundamental properties.
When a linear transformation is applied to an eigenvector, the eigenvector's direction remains unchanged, only its
magnitude is scaled by the corresponding eigenvalue.
Definition: For a square matrix , a scalar is an eigenvalue if there exists a non-zero vector (eigenvector) such
that .
Formulas/Theorems:
1. Characteristic Equation: To find eigenvalues, solve the equation , where is the identity
matrix of the same dimension as .
2. Cayley-Hamilton Theorem: Every square matrix satisfies its own characteristic equation. If
is the characteristic polynomial, then . This is useful for finding powers of a
matrix or its inverse.
3. Sum of Eigenvalues: The sum of the eigenvalues of a matrix is equal to its trace (sum of diagonal elements):
.
4. Product of Eigenvalues: The product of the eigenvalues of a matrix is equal to its determinant:
.
Properties:
If is an eigenvalue of , then is an eigenvalue of .
If is an eigenvalue of , then is an eigenvalue of (if is invertible).

*(PDF Page 154)*

If is an eigenvalue of , then is an eigenvalue of .
The eigenvalues of a symmetric matrix are always real.
Eigenvectors corresponding to distinct eigenvalues are linearly independent.
For a real symmetric matrix, eigenvectors corresponding to distinct eigenvalues are orthogonal.
The eigenvalues of a triangular matrix (upper or lower) are its diagonal entries.
A matrix is singular (non-invertible) if and only if 0 is an eigenvalue of .
Common Pitfalls:
Algebraic errors when solving the characteristic equation.
Forgetting to check for non-zero eigenvectors.
Confusing algebraic and geometric multiplicity.
Problem-Solving Techniques:
Always start by setting up the characteristic equation .
For matrices, use .
Use the sum and product of eigenvalues properties to verify your calculated eigenvalues or to find a missing
eigenvalue.
For eigenvectors, substitute each eigenvalue back into and solve the resulting system of
equations.
Gaussian Elimination
Gaussian elimination is an algorithm used to solve systems of linear equations, find the rank of a matrix, compute the
inverse of a matrix, and calculate determinants. It transforms a matrix into row echelon form using elementary row
operations.
Definition: A systematic procedure to transform a matrix into row echelon form (or reduced row echelon form) using
elementary row operations.
Elementary Row Operations:
1. Swapping two rows ( ).
2. Multiplying a row by a non-zero scalar ( ).
3. Adding a multiple of one row to another row ( ).
Row Echelon Form (REF): A matrix is in REF if:
All non-zero rows are above any rows of all zeros.
The leading entry (pivot) of each non-zero row is in a column to the right of the leading entry of the row above it.
All entries in a column below a leading entry are zeros.
Reduced Row Echelon Form (RREF): A matrix is in RREF if it is in REF and:
The leading entry in each non-zero row is 1 (called a leading 1).
Each column containing a leading 1 has zeros everywhere else.
Applications:
Solving systems of linear equations.
Finding the rank of a matrix.
Computing the inverse of a matrix (by augmenting and reducing to ).
Calculating determinants (by keeping track of row operations).
Common Pitfalls:
Arithmetic errors during row operations.
Forgetting to apply operations to the augmented part of the matrix when solving systems or finding inverses.
Incorrectly identifying pivot elements.
Problem-Solving Techniques:
Always aim to create zeros below the pivot elements first.
Work column by column from left to right.
Use fractions carefully; sometimes it's better to multiply a row to avoid fractions temporarily.
For solving systems, use back-substitution after reaching REF.
LU Decomposition
LU decomposition factors a square matrix into the product of a lower triangular matrix and an upper triangular
matrix . This factorization is particularly useful for efficiently solving multiple systems of linear equations with the same
coefficient matrix, as it simplifies the process into two triangular systems.
Definition: A factorization of a square matrix diagonal) and an upper triangular matrix Process:
into the product of a lower triangular matrix , such that .
(with 1s on the

*(PDF Page 155)*

1. Use Gaussian elimination to transform into an upper triangular matrix .
2. The lower triangular matrix is constructed using the multipliers used in the Gaussian elimination process. If
was used, then . The diagonal elements of are 1s.
3. If row swaps are needed, a permutation matrix is introduced, such that .
Solving using LU Decomposition:
1. Substitute : .
2. Let .
3. Solve for using forward substitution (since is lower triangular).
4. Solve for using backward substitution (since is upper triangular).
Properties:
Not all matrices have an LU decomposition without pivoting (row swaps).
If is non-singular and all its leading principal minors are non-zero, then has a unique LU decomposition.
Common Pitfalls:
Incorrectly forming from the multipliers.
Errors in forward or backward substitution.
Forgetting the permutation matrix if row swaps are involved.
Problem-Solving Techniques:
Carefully track the multipliers used in Gaussian elimination to construct .
Practice forward and backward substitution for efficiency.
Recognize when pivoting is necessary (e.g., if a pivot element becomes zero).
Matrix
A matrix is a rectangular array of numbers, symbols, or expressions arranged in rows and columns. Matrices are
fundamental to linear algebra, representing linear transformations, systems of equations, and data structures.
Definition: A rectangular array of numbers (or functions) arranged in rows and columns. Denoted as .
Types of Matrices:
Square Matrix: .
Row Matrix: .
Column Matrix (Vector): .
Identity Matrix ( ): Square matrix with 1s on the main diagonal and 0s elsewhere. .
Zero Matrix ( ): All elements are 0. .
Diagonal Matrix: Square matrix where all non-diagonal elements are 0.
Scalar Matrix: A diagonal matrix where all diagonal elements are equal.
Symmetric Matrix: .
Skew-Symmetric Matrix: . Diagonal elements are 0.
Orthogonal Matrix: , which implies . Determinant is .
Invertible/Non-singular Matrix: A square matrix for which there exists a matrix such that
. .
Singular Matrix: A square matrix for which . It does not have an inverse.
Operations:
1. Addition/Subtraction: Element-wise, only for matrices of the same dimensions. .
2. Scalar Multiplication: Multiply each element by the scalar. .
3. Matrix Multiplication: . Requires number of columns of to equal number of rows of
. Resulting matrix has dimensions if is and is .
4. Transpose ( ): Rows become columns and columns become rows. .
5. Inverse ( ): For a matrix , . For general ,
, where is the adjugate matrix (transpose of the cofactor matrix).
Properties:
Matrix addition is commutative: .
Matrix multiplication is associative: .
Matrix multiplication is generally NOT commutative: .
.
.
.

*(PDF Page 156)*

.
.
Common Pitfalls:
Incorrect dimensions for addition or multiplication.
Assuming commutativity for matrix multiplication.
Errors in calculating inverses, especially for larger matrices.
Problem-Solving Techniques:
Always check dimensions before performing operations.
For matrix multiplication, visualize the dot products of rows and columns.
For inverses, use the adjugate formula for and Gaussian elimination for larger matrices.
Multiplicity
Multiplicity refers to how many times an eigenvalue appears as a root of the characteristic polynomial (algebraic
multiplicity) and the dimension of its corresponding eigenspace (geometric multiplicity). These concepts are crucial for
understanding diagonalizability of a matrix.
Definition:
Algebraic Multiplicity (AM): The number of times an eigenvalue appears as a root of the characteristic
polynomial .
Geometric Multiplicity (GM): The dimension of the eigenspace corresponding to linearly independent eigenvectors associated with . It is given by , which is the number of
, where is the dimension
of the matrix.
Properties/Theorems:
For any eigenvalue , .
A matrix is diagonalizable if and only if for every eigenvalue , .
If all eigenvalues are distinct, then for all , and the matrix is diagonalizable.
Common Pitfalls:
Confusing AM and GM.
Incorrectly calculating the rank of .
Assuming diagonalizability based only on AM without checking GM.
Problem-Solving Techniques:
First, find all eigenvalues and their algebraic multiplicities by solving .
For each eigenvalue, calculate the rank of to find its geometric multiplicity.
Compare AM and GM for each eigenvalue to determine diagonalizability.
Orthonormality
Orthonormality describes a set of vectors that are mutually orthogonal (perpendicular) and each has a unit length
(normalized). Orthonormal bases simplify many calculations in linear algebra, particularly in projections and coordinate
transformations.
Definition:
Orthogonal Vectors: Two vectors and are orthogonal if their dot product is zero: .
Normalized Vector: A vector is normalized if its length (magnitude) is 1: .
Orthonormal Set: A set of vectors is orthonormal if they are mutually orthogonal and each
vector is normalized. That is, (Kronecker delta), where if and if .
Gram-Schmidt Orthonormalization Process: A procedure to transform a set of linearly independent vectors
into an orthonormal set .
1.
2.
3.
4. Continue for all vectors.
5. Normalize each : .
Properties:
An orthonormal set of vectors is always linearly independent.
If is an orthogonal matrix (columns form an orthonormal set), then For an orthogonal matrix , (preserves length).
For an orthogonal matrix , (preserves dot product and angle).
, and .

*(PDF Page 157)*

Common Pitfalls:
Arithmetic errors in Gram-Schmidt, especially with projections.
Forgetting to normalize vectors after making them orthogonal.
Confusing orthogonal with orthonormal.
Problem-Solving Techniques:
Systematically apply the Gram-Schmidt process, calculating one orthogonal vector at a time.
Double-check dot products to ensure orthogonality.
Always normalize the final set of orthogonal vectors.
Rank of Matrix
The rank of a matrix is a fundamental property that measures the "linear independence" present in its rows and
columns. It indicates the dimension of the vector space spanned by its rows or columns, and is crucial for
understanding the solvability of linear systems.
Definition: The maximum number of linearly independent row vectors (row rank) or column vectors (column rank) in
a matrix. The row rank is always equal to the column rank.
Calculation Methods:
1. Using Row Echelon Form: The rank of a matrix is the number of non-zero rows in its row echelon form.
2. Using Determinants (Minors): The rank of a matrix is the largest integer such that there exists an
submatrix of with a non-zero determinant.
Properties/Theorems:
For an matrix , .
if and only if is a zero matrix.
.
.
Rank-Nullity Theorem: For an matrix , , where is the
dimension of the null space (kernel) of .
A square matrix of size is invertible if and only if .
For a system :
Consistent if .
Unique solution if (number of variables).
Infinitely many solutions if .
Inconsistent if .
Common Pitfalls:
Errors in Gaussian elimination leading to incorrect row echelon form.
Misinterpreting the number of non-zero rows.
Not considering the augmented matrix for system consistency.
Problem-Solving Techniques:
The most reliable method is to reduce the matrix to row echelon form using Gaussian elimination and count the
number of non-zero rows.
For smaller matrices, checking determinants of submatrices can be faster.
Use the Rank-Nullity Theorem to find nullity if rank is known, or vice versa.
Singular Value Decomposition (SVD)
Singular Value Decomposition is a powerful matrix factorization technique that decomposes any matrix into
three matrices: , , and . It generalizes the concept of eigenvalues and eigenvectors to non-square matrices and
has broad applications in data compression, noise reduction, and recommender systems.
Definition: Any matrix can be factored as , where:
is an orthogonal matrix whose columns are the left singular vectors of .
is an diagonal matrix with non-negative real numbers on the diagonal, called singular values ( ),
arranged in decreasing order. The non-zero singular values are is an orthogonal matrix whose columns are the right singular vectors of , where .
. is its transpose.
Relationship to Eigenvalues:
The singular values of are the square roots of the eigenvalues of (or ).
The columns of are the eigenvectors of .
The columns of are the eigenvectors of .

*(PDF Page 158)*

Properties/Applications:
SVD exists for any matrix (square or rectangular).
The number of non-zero singular values is equal to the rank of the matrix.
Low-rank approximation: By keeping only the largest singular values and corresponding singular vectors, SVD
can approximate a matrix with fewer components, useful for data compression.
Pseudo-inverse: The SVD can be used to compute the Moore-Penrose pseudo-inverse of a matrix.
Principal Component Analysis (PCA): SVD is closely related to PCA, where singular vectors correspond to
principal components.
Common Pitfalls:
Confusing singular values with eigenvalues.
Incorrectly calculating eigenvectors for or .
Not arranging singular values in decreasing order.
Problem-Solving Techniques:
Calculate (or ).
Find the eigenvalues of Find the eigenvectors of Find the eigenvectors of . The square roots of these eigenvalues are the singular values .
. These form the columns of .
. These form the columns of .
Alternatively, .
Statistics
While a broad field, within the context of linear algebra for GATE CS, statistics primarily involves concepts like mean,
variance, covariance, and their matrix representations. These are crucial for understanding data analysis techniques
like PCA, which heavily rely on linear algebra.
Definition (Linear Algebra Context): Focuses on the mathematical tools (vectors, matrices) used to analyze and
model data, particularly in multivariate statistics.
Key Concepts:
1. Mean: For a vector , the mean is .
2. Variance: A measure of how spread out the data is. For a vector 3. Covariance: A measure of how two variables change together. For two vectors , .
and ,
.
4. Covariance Matrix: For a dataset with variables and observations, the covariance matrix is a
symmetric matrix where and .
where is the data matrix with columns centered (mean subtracted).
5. Principal Component Analysis (PCA): A dimensionality reduction technique that uses the eigenvectors of the
covariance matrix (or SVD of the data matrix) to find orthogonal directions (principal components) of maximum
variance in the data.
Properties:
Covariance matrix is always symmetric and positive semi-definite.
Eigenvalues of the covariance matrix represent the variance along the principal components.
Eigenvectors of the covariance matrix are the principal components.
Common Pitfalls:
Confusing variance with standard deviation.
Incorrectly calculating covariance or covariance matrix.
Not centering data before calculating covariance matrix for PCA.
Problem-Solving Techniques:
Understand the definitions of mean, variance, and covariance.
For PCA, compute the covariance matrix, then find its eigenvalues and eigenvectors.
Relate SVD to PCA: SVD of the centered data matrix directly gives principal components and singular values
related to variance.
Subspace
A subspace is a subset of a vector space that itself satisfies the properties of a vector space. It must contain the zero
vector, be closed under vector addition, and closed under scalar multiplication. Subspaces are fundamental building

*(PDF Page 159)*

blocks for understanding the structure of vector spaces.
Definition: A subset of a vector space is a subspace of if is itself a vector space under the operations
defined on .
Conditions for a Subspace: A non-empty subset of a vector space is a subspace if and only if:
1. The zero vector of is in ( ).
2. is closed under vector addition: If , then .
3. is closed under scalar multiplication: If and is any scalar, then .
Important Subspaces Associated with a Matrix :
Column Space ( ): The span of the column vectors of . It is a subspace of (if is ).
.
Row Space ( ): The span of the row vectors of . It is a subspace of . .
Null Space ( or ): The set of all vectors such that . It is a subspace of .
.
Left Null Space ( ): The set of all vectors such that . It is a subspace of .
Properties:
The intersection of two subspaces is always a subspace.
The union of two subspaces is generally not a subspace.
The sum of two subspaces is a subspace.
Common Pitfalls:
Forgetting to check all three conditions for a subspace (especially the zero vector).
Confusing the column space with the null space.
Assuming the union of subspaces is a subspace.
Problem-Solving Techniques:
To check if a set is a subspace, verify the three conditions.
To find a basis for the column space, identify the pivot columns of the original matrix after reducing to REF.
To find a basis for the null space, solve and express the solution in terms of free variables.
To find a basis for the row space, use the non-zero rows of the REF of the matrix.
System of Equations
A system of linear equations is a collection of one or more linear equations involving the same set of variables. Linear
algebra provides powerful tools to determine the existence and nature of solutions (unique, infinite, or no solution) for
such systems.
Definition: A set of equations of the form , ..., be written in matrix form as , where is the coefficient matrix, is the vector of variables, and . This can
is the
constant vector.
Types of Systems:
Homogeneous System: . Always consistent (has at least the trivial solution ).
Non-homogeneous System: where .
Consistency and Number of Solutions (using Rank):
1. Consistent System: A system has at least one solution if .
Unique Solution: If (number of variables).
Infinitely Many Solutions: If . The number of free variables is .
2. Inconsistent System: A system has no solution if .
Solution Methods:
Gaussian Elimination/Row Reduction: Transform the augmented matrix into row echelon form to solve
by back-substitution.
Matrix Inverse Method: If is square and invertible, Cramer's Rule: For a square system with a unique solution, . (Only for unique solutions).
, where is the matrix formed by
replacing the -th column of with . (Computationally expensive for larger systems).
Properties of Homogeneous Systems:
Always has the trivial solution .
Has non-trivial solutions if and only if (for square ) or .
The set of all solutions forms the null space of .
Common Pitfalls:
Arithmetic errors during row operations.
Incorrectly determining consistency or number of solutions.

*(PDF Page 160)*

Applying Cramer's rule or inverse method when not applicable (e.g., non-square matrix, singular matrix).
Problem-Solving Techniques:
Always form the augmented matrix .
Use Gaussian elimination to reduce the augmented matrix to row echelon form.
Analyze the rank of and to determine consistency and number of solutions.
For homogeneous systems, look for non-trivial solutions if or .
Vector Space
A vector space is a fundamental algebraic structure consisting of a set of vectors, along with two operations: vector
addition and scalar multiplication, which satisfy a set of ten axioms. It provides a generalized framework for working
with vectors beyond simple geometric arrows.
Definition: A non-empty set of objects, called vectors, on which two operations are defined: vector addition
(denoted by ) and scalar multiplication (denoted by juxtaposition), subject to ten axioms. The scalars are typically
real numbers ( ) or complex numbers ( ).
Axioms of a Vector Space: For all and all scalars :
1. (Closure under addition)
2. (Commutativity of addition)
3. (Associativity of addition)
4. There exists a zero vector such that (Additive identity)
5. For each , there exists an additive inverse such that (Additive inverse)
6. (Closure under scalar multiplication)
7. (Distributivity of scalar over vector addition)
8. (Distributivity of scalar over scalar addition)
9. (Associativity of scalar multiplication)
10. (Multiplicative identity)
Key Concepts:
Span: The set of all possible linear combinations of a set of vectors . Denoted as
. It is always a subspace.
Linear Independence: A set of vectors is linearly independent if the only solution to
is .
Basis: A set of vectors in a vector space that is linearly independent and spans . The number of vectors in
a basis is unique and is called the dimension of the vector space.
Dimension: The number of vectors in any basis for a vector space , denoted as .
Examples of Vector Spaces:
(n-dimensional real coordinate space)
The set of all matrices.
The set of all polynomials of degree at most .
The set of all continuous functions on an interval.
Common Pitfalls:
Forgetting to check all axioms when verifying if a set is a vector space.
Confusing a vector space with a subspace.
Incorrectly determining linear independence or a basis.
Problem-Solving Techniques:
To check if a set is a vector space, verify all ten axioms.
To check linear independence, set up the equation and solve the resulting system of
linear equations.
To find a basis, identify a linearly independent set that spans the space. For , this often involves finding pivot
columns of a matrix formed by the vectors.
Quick Formula Reference
Determinant:
: for
Properties: , , ,
Invertible iff
Matrix Operations:
Matrix Multiplication:

*(PDF Page 161)*

Inverse :
General Inverse:
Transpose Properties: ,
Inverse Properties: ,
Eigenvalues & Eigenvectors:
Characteristic Equation:
Sum of Eigenvalues:
Product of Eigenvalues:
Cayley-Hamilton Theorem: where is the characteristic polynomial.
Algebraic Multiplicity (AM): Number of times is a root.
Geometric Multiplicity (GM):
Diagonalizable if for all .
Rank of Matrix:
Number of non-zero rows in REF.
for matrix.
Rank-Nullity Theorem: (number of columns).
System consistent if .
Unique solution if .
Infinite solutions if .
No solution if .
LU Decomposition:
(or with permutation matrix )
Solve by (forward substitution) then (backward substitution).
Orthonormality:
Orthogonal:
Normalized:
Orthonormal:
Orthogonal Matrix : .
Singular Value Decomposition (SVD):
Singular values are .
Columns of are eigenvectors of .
Columns of are eigenvectors of .
Subspace Conditions:
Contains zero vector.
Closed under addition.
Closed under scalar multiplication.
Important Tips for GATE
1. Master the Basics: Ensure a strong understanding of fundamental definitions (e.g., matrix types, vector space
axioms, linear independence). Many conceptual questions test these directly.
2. Practice Gaussian Elimination: This is a core algorithm. Practice it diligently for solving systems, finding rank, and
computing inverses. Accuracy and speed are crucial here.
3. Understand Eigenvalue/Eigenvector Properties: Don't just memorize formulas. Understand *why* the sum of
eigenvalues equals the trace and the product equals the determinant. These properties are often used as shortcuts
or for verification.
4. Pay Attention to Matrix Dimensions: Always check if matrix operations (addition, multiplication) are valid based on
dimensions. This prevents common errors, especially in matrix multiplication.
5. Rank-Nullity Theorem is Your Friend: This theorem is incredibly useful for quickly finding the nullity if the rank is
known, or vice versa, and for analyzing the nature of solutions to linear systems.
6. Beware of Calculation Errors: Linear algebra problems often involve extensive calculations. Use the virtual
calculator carefully and double-check intermediate steps. Simple arithmetic mistakes are a common reason for
losing marks.
7. Distinguish Between Similar Concepts: Clearly differentiate between algebraic and geometric multiplicity,
orthogonal and orthonormal vectors, and the various matrix subspaces (column space, null space, row space).
8. Practice Previous Year Questions: Solve as many GATE previous year questions as possible. This will familiarize

*(PDF Page 162)*

you with the typical question patterns, difficulty levels, and time constraints. Focus on understanding the solution
approach rather than just getting the answer.

---

## 4. Complete Question Index & Answer Key Record (112 Questions)

| Q # | Question Source / Title | Answer Key |
| :---: | :--- | :---: |
| `6.1.1` | Cartesian Coordinates: GATE IT 2007 \| Question: 80 | **A** |
| `6.2.1` | Determinant: GATE CSE 1997 \| Question: 1.3 | **B** |
| `6.2.2` | Determinant: GATE CSE 2000 \| Question: 1.3 | **A** |
| `6.2.3` | Determinant: GATE CSE 2013 \| Question: 3 | **A** |
| `6.2.4` | Determinant: GATE CSE 2014 \| Set 2 \| Question: 4 | **0** |
| `6.2.5` | Determinant: GATE CSE 2019 \| Question: 9 | **D** |
| `6.2.6` | Determinant: GATE CSE 2023 \| Question: 8 | **B** |
| `6.2.7` | Determinant: GATE CSE 2024 \| Set 2 \| Question: 37 | **A;B** |
| `6.2.8` | Determinant: GATE CSE 2025 \| Set 2 \| Question: 4 | **A** |
| `6.2.9` | Determinant: GATE CSE 2026 \| Set 2 \| Question: 52 | **48:48** |
| `6.2.10` | Determinant: GATE DS&AI 2024 \| Question: 25 | **0** |
| `6.2.11` | Determinant: GATE IT 2004 \| Question: 32 | **D** |
| `6.2.12` | Determinant: GATE IT 2005 \| Question: 3 | **A** |
| `6.3.1` | Eigen Value: GATE CSE 1993 \| Question: 01.1 | **B;D** |
| `6.3.2` | Eigen Value: GATE CSE 2002 \| Question: 5a | **N/A** |
| `6.3.3` | Eigen Value: GATE CSE 2005 \| Question: 49 | **B** |
| `6.3.4` | Eigen Value: GATE CSE 2007 \| Question: 25 | **C** |
| `6.3.5` | Eigen Value: GATE CSE 2008 \| Question: 28 | **A** |
| `6.3.6` | Eigen Value: GATE CSE 2010 \| Question: 29 | **D** |
| `6.3.7` | Eigen Value: GATE CSE 2011 \| Question: 40 | **A** |
| `6.3.8` | Eigen Value: GATE CSE 2012 \| Question: 11 | **D** |
| `6.3.9` | Eigen Value: GATE CSE 2014 \| Set 1 \| Question: 5 | **0** |
| `6.3.10` | Eigen Value: GATE CSE 2014 \| Set 2 \| Question: 47 | **6** |
| `6.3.11` | Eigen Value: GATE CSE 2014 \| Set 3 \| Question: 4 | **A** |
| `6.3.12` | Eigen Value: GATE CSE 2015 \| Set 1 \| Question: 36 | **D** |
| `6.3.13` | Eigen Value: GATE CSE 2015 \| Set 2 \| Question: 5 | **6** |
| `6.3.14` | Eigen Value: GATE CSE 2015 \| Set 3 \| Question: 15 | **B** |
| `6.3.15` | Eigen Value: GATE CSE 2016 \| Set 1 \| Question: 05 | **15** |
| `6.3.16` | Eigen Value: GATE CSE 2016 \| Set 2 \| Question: 06 | **0.125** |
| `6.3.17` | Eigen Value: GATE CSE 2017 \| Set 1 \| Question: 31 | **B** |
| `6.3.18` | Eigen Value: GATE CSE 2017 \| Set 2 \| Question: 52 | **5** |
| `6.3.19` | Eigen Value: GATE CSE 2018 \| Question: 17 | **3** |
| `6.3.20` | Eigen Value: GATE CSE 2018 \| Question: 26 | **D** |
| `6.3.21` | Eigen Value: GATE CSE 2019 \| Question: 44 | **12** |
| `6.3.22` | Eigen Value: GATE CSE 2021 \| Set 1 \| Question: 52 | **3** |
| `6.3.23` | Eigen Value: GATE CSE 2022 \| Question: 43 | **A;C;D** |
| `6.3.24` | Eigen Value: GATE CSE 2023 \| Question: 20 | **2** |
| `6.3.25` | Eigen Value: GATE CSE 2024 \| Set 1 \| Question: 2 | **B** |
| `6.3.26` | Eigen Value: GATE CSE 2025 \| Set 1 \| Question: 31 | **D** |
| `6.3.27` | Eigen Value: GATE DA 2025 \| Question: 18 | **A;B** |
| `6.3.28` | Eigen Value: GATE DA 2026 \| Question: 36 | **C** |
| `6.3.29` | Eigen Value: GATE DA 2026 \| Question: 55 | **1:1** |
| `6.3.30` | Eigen Value: GATE DS&AI 2024 \| Question: 3 | **B** |
| `6.3.31` | Eigen Value: GATE Data Science and Artificial Intelligence 2024 \| Sample Paper \| Question: 17 | **B** |
| `6.3.32` | Eigen Value: GATE IT 2006 \| Question: 26 | **A** |
| `6.3.33` | Eigen Value: GATE IT 2007 \| Question: 2 | **B** |
| `6.4.1` | Gaussian Elimination: GATE DA 2025 \| Question: 2 | **B** |
| `6.5.1` | Lu Decomposition: GATE CSE 2015 \| Set 1 \| Question: 18 | **5** |
| `6.5.2` | Lu Decomposition: GATE CSE 2022 \| Question: 35 | **D** |
| `6.5.3` | Lu Decomposition: GATE CSE 2025 \| Set 2 \| Question: 34 | **A;B;C** |
| `6.6.1` | Matrix: GATE CSE 1987 \| Question: 1-xxiii | **C** |
| `6.6.2` | Matrix: GATE CSE 1988 \| Question: 16i | **N/A** |
| `6.6.3` | Matrix: GATE CSE 1993 \| Question: 02.7 | **N/A** |
| `6.6.4` | Matrix: GATE CSE 1994 \| Question: 1.2 | **D** |
| `6.6.5` | Matrix: GATE CSE 1994 \| Question: 3.12 | **N/A** |
| `6.6.6` | Matrix: GATE CSE 1996 \| Question: 10 | **N/A** |
| `6.6.7` | Matrix: GATE CSE 1996 \| Question: 2.6 | **A** |
| `6.6.8` | Matrix: GATE CSE 1997 \| Question: 4.2 | **C** |
| `6.6.9` | Matrix: GATE CSE 1998 \| Question: 2.2 | **B** |
| `6.6.10` | Matrix: GATE CSE 2001 \| Question: 1.1 | **A** |
| `6.6.11` | Matrix: GATE CSE 2004 \| Question: 26 | **C** |
| `6.6.12` | Matrix: GATE CSE 2004 \| Question: 27 | **B** |
| `6.6.13` | Matrix: GATE CSE 2004 \| Question: 76 | **D** |
| `6.6.14` | Matrix: GATE CSE 2006 \| Question: 23 | **D** |
| `6.6.15` | Matrix: GATE CSE 2015 \| Set 2 \| Question: 27 | **0** |
| `6.6.16` | Matrix: GATE CSE 2022 \| Question: 10 | **C** |
| `6.6.17` | Matrix: GATE CSE 2025 \| Set 2 \| Question: 1 | **C** |
| `6.6.18` | Matrix: GATE CSE 2026 \| Set 1 \| Question: 10 | **B;D** |
| `6.6.19` | Matrix: GATE DA 2025 \| Question: 27 | **D** |
| `6.6.20` | Matrix: GATE DA 2025 \| Question: 42 | **A;D** |
| `6.6.21` | Matrix: GATE DA 2026 \| Question: 11 | **B** |
| `6.6.22` | Matrix: GATE DA 2026 \| Question: 42 | **A;D** |
| `6.6.23` | Matrix: GATE IT 2004 \| Question: 36 | **B** |
| `6.6.24` | Matrix: GATE IT 2008 \| Question: 29 | **D** |
| `6.7.1` | Multiplicity: GATE CSE 2026 \| Set 1 \| Question: 3 | **A** |
| `6.8.1` | Orthonormality: GATE DA 2025 \| Question: 15 | **B;D** |
| `6.8.2` | Orthonormality: GATE DA 2025 \| Question: 40 | **A;B** |
| `6.9.1` | Rank of Matrix: GATE CSE 1994 \| Question: 1.9 | **C** |
| `6.9.2` | Rank of Matrix: GATE CSE 1995 \| Question: 1.24 | **A** |
| `6.9.3` | Rank of Matrix: GATE CSE 1998 \| Question: 2.1 | **A** |
| `6.9.4` | Rank of Matrix: GATE CSE 2002 \| Question: 1.1 | **C** |
| `6.9.5` | Rank of Matrix: GATE CSE 2017 \| Set 2 \| Question: 22 | **2** |
| `6.9.6` | Rank of Matrix: GATE CSE 2020 \| Question: 27 | **C** |
| `6.9.7` | Rank of Matrix: GATE CSE 2021 \| Set 2 \| Question: 24 | **4** |
| `6.10.1` | Singular Value Decomposition: GATE DS&AI 2024 \| Question: 51 | **55** |
| `6.11.1` | Statistics: GATE 2023 Stats Exam Q. 13 | **TBA** |
| `6.11.2` | Statistics: GATE STATISTICS 2021 Q.13 | **TBA** |
| `6.12.1` | Subspace: GATE DS&AI 2024 \| Question: 37 | **A;C** |
| `6.13.1` | System of Equations: GATE CSE 1996 \| Question: 1.7 | **C** |
| `6.13.2` | System of Equations: GATE CSE 1998 \| Question: 1.2 | **B** |
| `6.13.3` | System of Equations: GATE CSE 1998 \| Question: 9 | **N/A** |
| `6.13.4` | System of Equations: GATE CSE 2003 \| Question: 41 | **B** |
| `6.13.5` | System of Equations: GATE CSE 2004 \| Question: 71 | **C** |
| `6.13.6` | System of Equations: GATE CSE 2005 \| Question: 48 | **B** |
| `6.13.7` | System of Equations: GATE CSE 2008 \| Question: 3 | **X** |
| `6.13.8` | System of Equations: GATE CSE 2014 \| Set 1 \| Question: 4 | **1** |
| `6.13.9` | System of Equations: GATE CSE 2015 \| Set 3 \| Question: 33 | **C** |
| `6.13.10` | System of Equations: GATE CSE 2016 \| Set 2 \| Question: 04 | **C** |
| `6.13.11` | System of Equations: GATE CSE 2017 \| Set 1 \| Question: 3 | **C** |
| `6.13.12` | System of Equations: GATE CSE 2024 \| Set 1 \| Question: 39 | **A** |
| `6.13.13` | System of Equations: GATE CSE 2025 \| Set 1 \| Question: 13 | **A;D** |
| `6.13.14` | System of Equations: GATE CSE 2026 \| Set 2 \| Question: 21 | **24:24** |
| `6.13.15` | System of Equations: GATE DA 2025 \| Question: 3 | **C** |
| `6.13.16` | System of Equations: GATE DS&AI 2024 \| Question: 38 | **B;D** |
| `6.13.17` | System of Equations: GATE IT 2004 \| Question: 6 | **C** |
| `6.14.1` | Vector Space: GATE CSE 1995 \| Question: 2.13 | **A** |
| `6.14.2` | Vector Space: GATE CSE 2007 \| Question: 27 | **A** |
| `6.14.3` | Vector Space: GATE CSE 2014 \| Set 3 \| Question: 5 | **2** |
| `6.14.4` | Vector Space: GATE CSE 2017 \| Set 1 \| Question: 30 | **A** |
| `6.14.5` | Vector Space: GATE DA 2025 \| Question: 28 | **A** |
| `6.14.6` | Vector Space: GATE DA 2026 \| Question: 12 | **A** |
| `6.14.7` | Vector Space: GATE DS&AI 2024 \| Question: 39 | **B;C;D** |

