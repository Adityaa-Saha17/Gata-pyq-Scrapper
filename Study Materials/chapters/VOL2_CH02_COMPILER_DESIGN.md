# Volume 2 — Chapter 2: Compiler Design

- **Source PDF**: [filter1_volume2.pdf](file:///Users/adityaasaha/Documents/Academics/Gate/filter1_volume2.pdf)
- **Total GATE Questions in Chapter**: **242**

---

## 1. Subtopic Weightage & Question Distribution

| Subtopic # | Subtopic Name | Questions |
| :---: | :--- | :---: |
| **2.1** | Abstract Syntax Tree | 1 |
| **2.2** | Ambiguous Grammar | 2 |
| **2.3** | Assembler | 9 |
| **2.4** | Backpatching | 1 |
| **2.5** | Basic Blocks | 2 |
| **2.6** | Code Optimization | 8 |
| **2.7** | Compilation Phases | 13 |
| **2.8** | Compiler tokenization | 1 |
| **2.9** | Directed Acyclic Graph | 2 |
| **2.10** | Expression Evaluation | 2 |
| **2.11** | First and Follow | 6 |
| **2.13** | Intermediate Code | 11 |
| **2.14** | LR Parser | 20 |
| **2.15** | Lexical Analysis | 6 |
| **2.16** | Linker | 3 |
| **2.17** | Live Variable Analysis | 3 |
| **2.18** | Ll Parser | 2 |
| **2.19** | Macros | 4 |
| **2.20** | Operator Precedence | 9 |
| **2.21** | ✍ Practice Test: Parameter Passing | 14 |
| **2.22** | Parsing | 22 |
| **2.23** | Register Allocation | 6 |
| **2.24** | Runtime Environment | 22 |
| **2.26** | Symbol Table | 1 |
| **2.27** | Syntax Directed Translation | 19 |
| **2.28** | Variable Scope | 2 |
| **2.29** | Viable Prefix | 1 |


---

## 2. Comprehensive GATE CSE Compiler Design Reference (PDF Concepts + Expanded Research)

### 2.1 Compilation Phases & Supporting Components
1. **Lexical Analysis (Scanner)**:
   - Input: Character stream $\rightarrow$ Output: Token stream $\langle \text{token-name}, \text{attribute-value} \rangle$.
   - Formalism: **Regular Expressions** and **Deterministic Finite Automata (DFA)**.
   - **Maximal Munch (Longest Match Rule)**: Scans the longest prefix that matches any token pattern.
   - **Rule Priority**: If two patterns match the same longest string (e.g., keyword `if` vs identifier `if`), the pattern listed first wins.
   - **Number of Tokens**: Comments (`/* ... */`, `// ...`) and whitespace are stripped; macros are expanded in the **Preprocessing** step *before* lexical analysis.
2. **Syntax Analysis (Parser)**:
   - Input: Token stream $\rightarrow$ Output: Parse Tree / Abstract Syntax Tree (AST).
   - Formalism: **Context-Free Grammar (CFG)** and **Pushdown Automata (PDA)**.
   - Checks syntactic structure (balanced parentheses, valid statement structure), *not* type checking or undeclared variables.
3. **Semantic Analysis**:
   - Checks static semantics using **Syntax-Directed Translation (SDT)** and the **Symbol Table**:
     - Type checking and implicit type coercion (e.g., `int` to `float`).
     - Undeclared variables, multiple declarations in the same scope.
     - Function call argument count and type matching.
     - Checking that `break`/`continue` are inside loops and `return` matches function signature.
4. **Intermediate Code Generation (ICG)**:
   - Produces machine-independent representation: **Three-Address Code (TAC)**, **Quadruples**, **Triples**, **Indirect Triples**, **Static Single Assignment (SSA)**, **Syntax Trees / DAGs**.
5. **Code Optimization (Machine-Independent)**:
   - Constant folding, constant propagation, common subexpression elimination (CSE), dead-code elimination, copy propagation, loop-invariant code motion, strength reduction, induction variable elimination.
6. **Target Code Generation & Machine-Dependent Optimization**:
   - Instruction selection, **Register Allocation** (via Liveness Analysis + Graph Coloring), peephole optimization, instruction scheduling.

---

### 2.2 Grammars, Ambiguity, Left Recursion & Left Factoring
- **Context-Free Grammar**: $G = (V, T, P, S)$ where $V$ = non-terminals, $T$ = terminals ($V \cap T = \emptyset$), $P$ = productions $A \rightarrow \alpha$, $S$ = start symbol.
- **Ambiguity**:
  - A CFG is **ambiguous** iff there exists at least one string $w \in L(G)$ having **two or more distinct parse trees** (equivalently, $\ge 2$ distinct **leftmost derivations (LMD)** or $\ge 2$ distinct **rightmost derivations (RMD)**).
  - **Undecidability**: Determining whether an arbitrary CFG is ambiguous is **undecidable**.
  - **Key Theorem**: No ambiguous grammar can ever be $LL(k)$ or $LR(k)$ for any $k$. Every deterministic parser ($LL(1), LR(0), SLR(1), LALR(1), CLR(1)$) accepts only **unambiguous** grammars (unless disambiguating rules are manually supplied).
  - **Enforcing Precedence & Associativity in Expression Grammars**:
    - Lower precedence operators appear **closer to the start symbol** (higher in the parse tree).
    - **Left-associative** operator (`+`, `-`, `*`, `/`): make production **left-recursive** ($E \rightarrow E + T \mid T$).
    - **Right-associative** operator (`^`, `=`): make production **right-recursive** ($F \rightarrow P \text{ \textasciicircum } F \mid P$).
- **Eliminating Immediate Left Recursion** (required for Top-Down / $LL(1)$ parsers):
  $$A \rightarrow A\alpha_1 \mid A\alpha_2 \mid \dots \mid A\alpha_m \mid \beta_1 \mid \beta_2 \mid \dots \mid \beta_n$$
  is rewritten as:
  $$A \rightarrow \beta_1 A' \mid \beta_2 A' \mid \dots \mid \beta_n A'$$
  $$A' \rightarrow \alpha_1 A' \mid \alpha_2 A' \mid \dots \mid \alpha_m A' \mid \epsilon$$
- **Left Factoring** (eliminating common prefixes for $LL(1)$):
  $$A \rightarrow \alpha \beta_1 \mid \alpha \beta_2 \mid \gamma \quad \Longrightarrow \quad A \rightarrow \alpha A' \mid \gamma, \quad A' \rightarrow \beta_1 \mid \beta_2$$

---

### 2.3 FIRST and FOLLOW Sets (Exact Rules & Formulas)
- **$\text{FIRST}(\alpha)$**: Set of terminals that begin strings derived from $\alpha$ (plus $\epsilon$ if $\alpha \Rightarrow^* \epsilon$).
  1. $\text{FIRST}(a) = \{a\}$ for terminal $a \in T$.
  2. For $A \rightarrow X_1 X_2 \dots X_k$:
     - Add $\text{FIRST}(X_1) \setminus \{\epsilon\}$ to $\text{FIRST}(A)$.
     - If $\epsilon \in \text{FIRST}(X_1)$, add $\text{FIRST}(X_2) \setminus \{\epsilon\}$, and so on.
     - Add $\epsilon$ to $\text{FIRST}(A)$ **iff** $\epsilon \in \text{FIRST}(X_i)$ for all $i = 1 \dots k$.
- **$\text{FOLLOW}(A)$**: Set of terminals (plus end-marker `$`) that can appear immediately to the right of $A$ in some sentential form $S \Rightarrow^* \alpha A a \beta$.
  - **Crucial Rule**: $\epsilon$ is **NEVER** in $\text{FOLLOW}(A)$.
  1. Put `$` in $\text{FOLLOW}(S)$ where $S$ is the start symbol.
  2. If $A \rightarrow \alpha B \beta$, add $\text{FIRST}(\beta) \setminus \{\epsilon\}$ to $\text{FOLLOW}(B)$.
  3. If $A \rightarrow \alpha B$ or ($A \rightarrow \alpha B \beta$ and $\epsilon \in \text{FIRST}(\beta)$), add $\text{FOLLOW}(A)$ to $\text{FOLLOW}(B)$.

---

### 2.4 Top-Down Parsing & $LL(1)$ Conditions
- **Recursive Descent Parser**: Top-down parser built from mutually recursive procedures (one per non-terminal). Cannot handle left-recursive grammars (infinite loop).
- **$LL(1)$ Parsing Table $M[A, a]$**:
  - For each production $A \rightarrow \alpha$:
    1. For each terminal $a \in \text{FIRST}(\alpha)$, add $A \rightarrow \alpha$ to $M[A, a]$.
    2. If $\epsilon \in \text{FIRST}(\alpha)$, for each $b \in \text{FOLLOW}(A)$ (including `$`), add $A \rightarrow \alpha$ to $M[A, b]$.
- **Necessary & Sufficient Conditions for a Grammar $G$ to be $LL(1)$**:
  1. $G$ must be **unambiguous** and **free of left recursion** (both direct and indirect).
  2. For every non-terminal $A$ with productions $A \rightarrow \alpha_1 \mid \alpha_2 \mid \dots \mid \alpha_k$:
     - **Condition 1 (Disjoint FIRSTs)**: $\text{FIRST}(\alpha_i) \cap \text{FIRST}(\alpha_j) = \emptyset$ for all $i \neq j$. *(At most one $\alpha_i$ can derive $\epsilon$.)*
     - **Condition 2 (FIRST/FOLLOW Disjointness when Nullable)**: If $\epsilon \in \text{FIRST}(\alpha_i)$, then for every $j \neq i$:
       $$\text{FIRST}(\alpha_j) \cap \text{FOLLOW}(A) = \emptyset$$

---

### 2.5 Bottom-Up Parsing & Complete $LR$ Parser Hierarchy
- **Core Mechanism**: **Shift-Reduce Parsing** — constructs a **Rightmost Derivation in Reverse** (reduces the **handle** at each step).
- **Handle**: A substring $\beta$ matching the RHS of a production $A \rightarrow \beta$ whose reduction to $A$ represents one step along the reverse of a rightmost derivation.
- **Viable Prefix**: Any prefix of a right-sentential form that does not extend past the right end of the rightmost handle. The set of all viable prefixes of a CFG is a **Regular Language** (recognized by the DFA of LR items).

| Parser Type | Items Used | Reduce Action Placement for $[A \rightarrow \alpha \cdot]$ | Typical State Count | Conflict Notes |
| :--- | :--- | :--- | :--- | :--- |
| **$LR(0)$** | $LR(0)$ items ($A \rightarrow \alpha \cdot \beta$) | Entire row (all terminals $a \in T \cup \{\$\}$) | $n_0$ (Smallest) | Any state with both $[A \rightarrow \alpha \cdot a \beta]$ and $[B \rightarrow \gamma \cdot]$ has SR conflict |
| **$SLR(1)$** | $LR(0)$ items | Only under columns $a \in \text{FOLLOW}(A)$ | $n_0$ (Same DFA as $LR(0)$) | Resolves many $LR(0)$ conflicts using $\text{FOLLOW}(A)$ |
| **$LALR(1)$** | $LR(1)$ items with **merged cores** | Under lookahead columns $a \in L$ | $n_0$ (Same state count as $SLR(1)$!) | Merging states with identical $LR(0)$ cores can introduce **RR conflicts**, **NEVER SR conflicts** |
| **$CLR(1)$ / $LR(1)$** | Full $LR(1)$ items ($[A \rightarrow \alpha \cdot \beta, a]$) | Only under exact lookahead $a$ | $n_1 \ge n_0$ (Largest) | Most powerful deterministic bottom-up parser |

- **Grammar Inclusion Hierarchy (Strictly Proper)**:
  $$\text{Regular} \subsetneq LL(1) \subsetneq LR(1), \qquad LR(0) \subsetneq SLR(1) \subsetneq LALR(1) \subsetneq CLR(1) \subsetneq \text{Unambiguous CFG} \subsetneq \text{All CFG}$$
  *(Note: $LL(1)$ is neither a subset nor a superset of $LR(0)/SLR(1)/LALR(1)$ in edge cases, though every $LL(1)$ grammar is $CLR(1)$.)*
- **Why Merging $CLR(1)$ States into $LALR(1)$ Never Creates a Shift-Reduce (SR) Conflict**:
  - Shift actions depend **only on the $LR(0)$ core** ($[A \rightarrow \alpha \cdot a \beta, \_]$). Since only states with identical $LR(0)$ cores are merged, if the merged $LALR(1)$ state has a shift on $a$ and a reduce on $a$, one of the original $CLR(1)$ states already had both $[A \rightarrow \alpha \cdot a \beta, \_]$ and $[B \rightarrow \gamma \cdot, a]$—meaning the conflict already existed in $CLR(1)$! However, **Reduce-Reduce (RR) conflicts CAN be created** when merging states with different lookahead sets.
- **Operator Precedence Parser**:
  - Bottom-up parser for **Operator Grammars** (no production has $\epsilon$ on RHS, and no two adjacent non-terminals appear on RHS).
  - Can parse certain **ambiguous grammars** by embedding precedence ($\lessdot, \doteq, \gtrdot$) directly in the table.

---

### 2.6 Syntax-Directed Translation (SDT): S-Attributed vs L-Attributed
- **Synthesized Attribute**: Computed for node $N$ solely from attribute values of $N$'s **children** (and $N$ itself). For $A \rightarrow X_1 X_2 \dots X_n$, $A.s = f(X_1.\text{attr}, \dots, X_n.\text{attr})$.
- **Inherited Attribute**: Computed for node $X_i$ from attribute values of $X_i$'s **parent**, **siblings**, or $X_i$ itself.

| Property | **S-Attributed SDT** | **L-Attributed SDT** |
| :--- | :--- | :--- |
| **Allowed Attributes** | **Synthesized ONLY** | **Synthesized + Restricted Inherited** |
| **Inherited Dependency Rule** | None | For $A \rightarrow X_1 X_2 \dots X_n$, $X_i.inh$ may depend only on: (1) **Parent $A$'s inherited** attributes, and (2) **Left siblings** $X_1, X_2, \dots, X_{i-1}$ (synthesized or inherited). **Never right siblings!** |
| **Action Placement** | Semantic actions placed only at the **end (rightmost end)** of productions (Postfix SDT). | Semantic actions can be placed **anywhere** on the RHS. |
| **Evaluation Order** | Bottom-up (Postorder traversal / during $LR$ reductions). | Depth-First Left-to-Right traversal (Top-down $LL(1)$ parsing or on-the-fly during traversal). |
| **Relationship** | **Every S-attributed SDT is also L-attributed** ($\text{S-Attributed} \subsetneq \text{L-Attributed}$). | Superset of S-attributed. |

---

### 2.7 Intermediate Code, Basic Blocks, DAG, SSA & Backpatching
1. **Three-Address Code (TAC) Representations**:
   - **Quadruples**: `(op, arg1, arg2, result)` — uses explicit temporary names; easy to rearrange statements during optimization.
   - **Triples**: `(op, arg1, arg2)` — refers to temporary results by instruction index `(0), (1)...`; moving statements requires updating all references.
   - **Indirect Triples**: Array of pointers to triples + table of triples — combines space efficiency of triples with ease of code movement.
2. **Basic Blocks & Control Flow Graph (CFG)**:
   - **3 Leader Selection Rules**:
     1. The **first statement** of the three-address code is a leader.
     2. Any statement that is the **target of a conditional or unconditional jump** (`goto L`) is a leader.
     3. Any statement **immediately following** a conditional or unconditional jump is a leader.
   - Every leader starts a basic block containing itself and all instructions up to (but not including) the next leader.
3. **Directed Acyclic Graph (DAG) for a Basic Block**:
   - Eliminates **local common subexpressions** and identifies dead stores within a basic block.
   - **Minimum registers / nodes**: Only distinct expressions with unchanged operands share a node; if variable $x$ is reassigned, subsequent uses of $x$ point to the new node.
4. **Static Single Assignment (SSA) Form**:
   - Every variable is assigned **exactly once** in the static program text ($x_1 = \dots, x_2 = \dots$).
   - At control-flow join points (where multiple basic blocks converge), a **$\phi$-function (phi-node)** $x_3 = \phi(x_1, x_2)$ selects the value based on which control path was taken.
5. **Backpatching**:
   - Single-pass code generation using `makelist(i)`, `merge(p1, p2)`, and `backpatch(p, i)` with attributes `E.truelist`, `E.falselist`, and `S.nextlist`.

---

### 2.8 Data-Flow Analysis (Liveness) & Register Allocation
- **Live Variable Analysis (Backward Data-Flow Analysis)**:
  - A variable $x$ is **live at point $p$** if the value of $x$ at $p$ could be used along some path in the flow graph starting at $p$ before $x$ is redefined.
  - For each basic block $B$:
    - $use[B]$: Set of variables **used in $B$ prior to any definition** of them in $B$.
    - $def[B]$: Set of variables **defined (assigned) in $B$ prior to any use** of them in $B$.
  - **Backward Data-Flow Equations (Iterative until Fixed Point)**:
    $$OUT[B] = \bigcup_{S \in succ(B)} IN[S]$$
    $$IN[B] = use[B] \cup \big( OUT[B] \setminus def[B] \big)$$
- **Register Allocation via Graph Coloring (Chaitin's Algorithm)**:
  - Build the **Register Interference Graph (RIG)**:
    - **Nodes**: Variables / temporaries.
    - **Undirected Edge $(u, v)$**: Added iff $u$ and $v$ are **simultaneously live** at some point in the program (cannot share a register).
  - **Minimum Number of Registers Needed** (without spilling) = **Chromatic Number $\chi(G)$** of the interference graph.
  - *Special Note for Straight-Line Basic Blocks*: Intervals of live ranges form an **Interval Graph** (a chordal graph), where $\chi(G) = \omega(G)$ (maximum number of variables simultaneously live at any single point).

---

### 2.9 Runtime Environments, Scoping & Parameter Passing
- **Memory Layout of a Program**:
  - **Code / Text Segment** (Static size): Machine instructions.
  - **Static / Global Data Area** (Static size): Global variables and `static` variables.
  - **Stack** (Dynamic, LIFO): **Activation Records (Stack Frames)** for active procedure calls (contains local variables, actual parameters, return value, saved machine status, return address, **Control/Dynamic Link**, and **Access/Static Link**).
  - **Heap** (Dynamic): `malloc`/`new` dynamically allocated memory.
- **Control Link vs Access Link**:
  - **Control Link (Dynamic Link)**: Points to the activation record of the **caller** (runtime call chain).
  - **Access Link (Static Link)**: Points to the latest activation record of the **lexically enclosing procedure** (used to implement **Static / Lexical Scoping** in nested procedures like Pascal/Ada).
- **Scoping Rules**:
  - **Static (Lexical) Scoping** (C, Java, Python, Pascal): Non-local variable references are resolved based on the **compile-time textual nesting structure** of the code.
  - **Dynamic Scoping** (Lisp macros, Bash/Perl `local`): Non-local variable references are resolved by searching down the **runtime call stack** for the most recently active binding of that variable name.
- **Parameter Passing Modes (High-Yield GATE Comparison)**:
  1. **Call by Value**: Actual parameter is evaluated; its **r-value** is copied into formal parameter's local storage. Callee modifications **do not** affect caller.
  2. **Call by Reference (Address)**: **l-value (address)** of actual parameter is passed. Callee reads/writes directly to caller's variable (creates **aliasing** if same variable passed twice or global variable passed).
  3. **Call by Value-Result (Copy-In / Copy-Out / Copy-Restore)**:
     - On entry: Value of actual parameter is copied into local formal variable.
     - During execution: Callee modifies only its **local copy** (so globals/aliases do **not** change mid-execution!).
     - On return: Final value of formal parameter is copied back to actual parameter's l-value.
  4. **Call by Name (Algol-60 Thunks / Lazy Textual Substitution)**:
     - Actual parameter expression is **textually substituted** (with renaming to avoid variable capture) for every occurrence of the formal parameter, and re-evaluated in the caller's environment **every time** the formal parameter is read or written (e.g., passing `i` and `A[i]` where `i` changes inside the function changes which array element `A[i]` refers to!).

---

## 3. Original PDF Chapter Notes (Preserved Verbatim)


2 Compiler Design (242)
Lexical analysis, Parsing, Syntax-directed translation, Runtime environments, Intermediate code generation.
Subject Overview
Compiler Design is a fundamental area of Computer Science that deals with the theory and practice of building
compilers – programs that translate source code written in a high-level programming language into an equivalent low-
level machine-understandable form (like assembly or machine code). Understanding compiler design is crucial for a
GATE CS aspirant as it provides deep insights into how programming languages work, how software interacts with
hardware, and the underlying mechanisms of program execution. This subject often carries a weightage of 6-10 marks
in the GATE CS exam, typically involving 2-3 questions of 2 marks and 1-2 questions of 1 mark. Questions range from
theoretical concepts (phases of compilation, definitions) and conceptual understanding (optimization techniques,
runtime environment) to numerical problems (parsing table construction, FIRST/FOLLOW sets, DAG generation,
register allocation). A strong grasp of this subject is vital not just for the exam, but also for a holistic understanding of
computer systems.
Topic-wise Key Concepts
Abstract Syntax Tree (AST)
An AST is a tree representation of the abstract syntactic structure of source code, where each node denotes a construct
in the source code. It abstracts away the concrete syntax (like parentheses or semicolons) and focuses on the essential
structure and meaning of the program. ASTs are crucial for semantic analysis, intermediate code generation, and
various optimization techniques.
Key Properties:
Nodes represent operators and keywords, while leaves represent operands and identifiers.
More compact than a parse tree, omitting unnecessary details like non-terminals that only derive other non-
terminals.
Used as an intermediate representation for subsequent compiler phases.
Common Pitfalls: Confusing AST with a parse tree. A parse tree shows every detail of the derivation; an AST
shows only the essential structure.
Standard Problem-Solving Technique: Given a grammar and an expression, construct its parse tree first, then
derive the AST by eliminating redundant nodes and structuring it based on operator precedence and associativity.
Ambiguous Grammar
A grammar is said to be ambiguous if there exists at least one string that can be generated by the grammar in more
than one leftmost derivation, or more than one rightmost derivation, or has more than one parse tree. Ambiguity is
undesirable in programming language grammars because it leads to multiple interpretations of the same program
statement.
Key Properties:
Causes difficulty for parsers as they cannot uniquely determine the structure of an input string.
Common sources include dangling-else problem and lack of operator precedence/associativity rules.
Common Pitfalls: Not being able to identify ambiguity. A common test is to find a string with two distinct parse
trees.
Standard Problem-Solving Technique: To resolve ambiguity, rewrite the grammar by introducing new non-
terminals or by incorporating precedence and associativity rules directly into the grammar productions. For example,
for arithmetic expressions, introduce non-terminals like Term and Factor.
Assembler
An assembler is a program that translates assembly language code into machine code. Assembly language uses

*(PDF Page 118)*

mnemonics for operations and symbolic names for memory locations, making it more human-readable than raw
machine code. Assemblers typically perform a one-to-one translation of assembly instructions to machine instructions.
Key Properties:
Two-Pass Assembler:
1. Pass 1: Scans the source code to build a symbol table (mapping symbolic labels to memory addresses) and
determines the length of machine instructions.
2. Pass 2: Uses the symbol table to translate assembly instructions into machine code, filling in operand
addresses.
Handles pseudo-operations (directives) like ORG, EQU, START, END, which guide the assembly process but
don't translate into machine instructions.
Common Pitfalls: Confusing assembler with compiler or linker. Assembler works at a lower level, translating
assembly to machine code.
Standard Problem-Solving Technique: Trace the assembly process, building a symbol table and calculating
location counter values for each instruction and data item.
Backpatching
Backpatching is a technique used in one-pass code generation, particularly for control flow statements (like if-else, while
loops) and boolean expressions. It involves generating jump instructions with initially unspecified target addresses,
which are later filled in (patched) once the true target address becomes known.
Key Properties:
Uses lists of incomplete jumps (e.g., truelist, falselist, nextlist).
: Creates a new list containing only (an index into the list of quadruples).
: Concatenates lists and , returning the combined list.
: Inserts as the target label for each of the jumps in list .
Standard Problem-Solving Technique: Trace the generation of three-address code for control flow statements,
maintaining and updating , , and as new quadruples are generated.
Basic Blocks
A basic block is a sequence of consecutive statements in which flow of control enters at the beginning and leaves at the
end without halt or possibility of branching except at the end. Basic blocks are fundamental units for many code
optimization techniques.
Key Properties:
No jumps into the middle of a basic block.
No jumps out of the middle of a basic block.
The first statement is called a leader.
Standard Problem-Solving Technique:
1. Identify leaders:
The first statement of the program is a leader.
Any statement that is the target of a conditional or unconditional jump is a leader.
Any statement immediately following a conditional or unconditional jump is a leader.
2. For each leader, its basic block consists of the leader and all subsequent statements up to, but not including, the
next leader or the end of the program.
Code Optimization
Code optimization is the phase of a compiler that attempts to improve the intermediate code or target code to make it
run faster, use less memory, or consume less power, without changing the program's observable behavior. It can be
machine-independent or machine-dependent.
Key Types/Techniques:
Machine-Independent:
Peephole Optimization: Examines a small sliding window of instructions and replaces suboptimal
sequences with better ones (e.g., redundant loads/stores, strength reduction).
Common Subexpression Elimination (CSE): Identifies and removes redundant computations of the same
expression.
Dead Code Elimination: Removes code that is never executed or whose results are never used.
Constant Folding: Evaluates constant expressions at compile time (e.g., becomes ).

*(PDF Page 119)*

Loop Optimizations: Loop invariant code motion, induction variable elimination, loop unrolling.
Strength Reduction: Replacing expensive operations with cheaper ones (e.g., with or ).
Machine-Dependent: Register allocation, instruction scheduling.
Key Property: Optimization must preserve the semantic equivalence of the program.
Common Pitfalls: Misidentifying opportunities for optimization or applying an optimization that changes program
behavior.
Compilation Phases
The compilation process is typically divided into several phases, each performing a specific task in the translation of
source code to target code. These phases operate sequentially, with the output of one phase serving as the input to the
next.
Phases in Order:
1. Lexical Analysis (Scanning): Breaks source code into tokens.
2. Syntax Analysis (Parsing): Checks grammar rules and builds a parse tree/AST.
3. Semantic Analysis: Checks for type compatibility, undeclared variables, etc. (meaning of the program).
4. Intermediate Code Generation: Creates an abstract machine-independent representation (e.g., three-address
code).
5. Code Optimization: Improves the intermediate or target code for efficiency.
6. Code Generation: Translates intermediate code into target machine code (e.g., assembly).
Supporting Components:
Symbol Table Management: Stores information about identifiers, used across multiple phases.
Error Handling: Detects and reports errors at each phase.
Common Pitfalls: Confusing the order or specific responsibilities of each phase.
Compiler Tokenization (Lexical Analysis)
Compiler tokenization, or Lexical Analysis, is the first phase of a compiler where the input stream of characters is
grouped into meaningful sequences called tokens. Each token represents a basic unit of the language, such as
keywords, identifiers, operators, or literals.
Core Idea: Converts a stream of characters into a stream of tokens.
Key Properties:
Tokens are defined by regular expressions.
Lexical analyzers (scanners) are typically implemented using Finite Automata (NFA or DFA).
Handles whitespace and comments, usually discarding them.
Longest Match Rule: When multiple token patterns match a prefix of the input, the longest possible token is
chosen.
Precedence Rule: If multiple patterns match the same longest prefix, the pattern listed first (or with higher
precedence) is chosen.
Common Pitfalls: Incorrectly applying longest match or precedence rules.
Standard Problem-Solving Technique: Given a string and a set of regular expressions for tokens, identify the
sequence of tokens.
Directed Acyclic Graph (DAG)
A DAG is a directed graph data structure used as an intermediate representation for basic blocks in compilers. Nodes in
a DAG represent operations, and edges represent the flow of values between operations. It effectively highlights
common subexpressions and the order of operations within a basic block.
Key Properties:
Each node has a unique value. If an expression is computed multiple times, it corresponds to a single node in
the DAG.
Leaf nodes are identifiers or constants. Interior nodes are operators.
Used for common subexpression elimination, dead code elimination, and reordering of operations.
Standard Problem-Solving Technique:
1. For each statement :
If or are not in the DAG, create nodes for them.
If is not in the DAG with children and , create a node for it.
Add as a label to the node representing .
2. If , make a label for the node representing .

*(PDF Page 120)*

Expression Evaluation
Expression evaluation is the process of computing the value of an arithmetic or logical expression according to operator
precedence and associativity rules. Compilers often convert infix expressions to postfix or prefix notation for easier
evaluation using a stack-based approach.
Key Notations:
Infix: Operators between operands (e.g., ).
Postfix (Reverse Polish Notation - RPN): Operators after operands (e.g., ).
Prefix (Polish Notation): Operators before operands (e.g., ).
Key Properties:
Precedence: Determines which operator is evaluated first (e.g., multiplication before addition).
Associativity: Determines evaluation order for operators of the same precedence (e.g., left-to-right for , , ,
; right-to-left for ).
Standard Problem-Solving Technique:
Infix to Postfix/Prefix: Use a stack to manage operators based on precedence and associativity.
Postfix Evaluation: Scan from left to right. Push operands onto a stack. When an operator is encountered, pop
required operands, perform operation, push result back.
First and Follow
FIRST and FOLLOW sets are crucial for constructing predictive (LL(1)) parsing tables and for resolving ambiguities in
grammars. They help determine which production to apply or which token to expect next.
FIRST(X): The set of terminal symbols that begin strings derived from . If can derive (empty string), then is
in .
FOLLOW(A): The set of terminal symbols that can immediately follow the non-terminal in some sentential form.
never contains .
Important Formulas/Rules:
1. FIRST for a terminal : .
2. FIRST for : .
3. FIRST for a non-terminal : For each production :
Add to .
If for all , then add to .
If for all , then add to .
4. FOLLOW for a non-terminal :
Place (end-marker) in where is the start symbol.
For each production : Add to .
For each production or where : Add to .
Common Pitfalls: Incorrectly handling productions, or not iterating until sets stabilize.
Standard Problem-Solving Technique: Apply rules iteratively until no new terminals can be added to any set.
Grammar
A grammar is a formal system that describes the syntax of a language. It consists of a set of terminal symbols (the
basic symbols of the language), non-terminal symbols (syntactic variables), a start symbol, and a set of production rules
that specify how non-terminals can be replaced by sequences of terminals and non-terminals.
Formal Definition: A Context-Free Grammar (CFG) is a 4-tuple , where:
: Finite set of non-terminal symbols.
: Finite set of terminal symbols ( ).
: Finite set of production rules of the form , where and .
\( \text

---

## 4. Complete Question Index & Answer Key Record (242 Questions)

| Q # | Question Source / Title | Answer Key |
| :---: | :--- | :---: |
| `2.1.1` | Abstract Syntax Tree: GATE CSE 2015 \| Set 2 \| Question: 14 | **C** |
| `2.2.1` | Ambiguous Grammar: GATE CSE 1987 \| Question: 1-xii | **B** |
| `2.2.2` | Ambiguous Grammar: GATE CSE 2026 \| Set 2 \| Question: 19 | **B;C** |
| `2.3.1` | Assembler: GATE CSE 1992 \| Question: 01,viii | **N/A** |
| `2.3.2` | Assembler: GATE CSE 1992 \| Question: 03,ii | **TBA** |
| `2.3.3` | Assembler: GATE CSE 1992 \| Question: 3,i | **N/A** |
| `2.3.4` | Assembler: GATE CSE 1993 \| Question: 7.6 | **A;B;C** |
| `2.3.5` | Assembler: GATE CSE 1994 \| Question: 17a | **True** |
| `2.3.6` | Assembler: GATE CSE 1994 \| Question: 17b | **N/A** |
| `2.3.7` | Assembler: GATE CSE 1994 \| Question: 18a | **True** |
| `2.3.8` | Assembler: GATE CSE 1994 \| Question: 18b | **False** |
| `2.3.9` | Assembler: GATE CSE 1996 \| Question: 1.17 | **B** |
| `2.4.1` | Backpatching: GATE CSE 2025 \| Set 2 \| Question: 11 | **C** |
| `2.5.1` | Basic Blocks: GATE CSE 2025 \| Set 1 \| Question: 42 | **6:6** |
| `2.5.2` | Basic Blocks: GATE CSE 2026 \| Set 2 \| Question: 35 | **A** |
| `2.6.1` | Code Optimization: GATE CSE 2006 \| Question: 55 | **A** |
| `2.6.2` | Code Optimization: GATE CSE 2006 \| Question: 60 | **D** |
| `2.6.3` | Code Optimization: GATE CSE 2008 \| Question: 12 | **A** |
| `2.6.4` | Code Optimization: GATE CSE 2014 \| Set 1 \| Question: 17 | **D** |
| `2.6.5` | Code Optimization: GATE CSE 2014 \| Set 3 \| Question: 11 | **7** |
| `2.6.6` | Code Optimization: GATE CSE 2021 \| Set 2 \| Question: 30 | **D** |
| `2.6.7` | Code Optimization: GATE CSE 2025 \| Set 1 \| Question: 3 | **B** |
| `2.6.8` | Code Optimization: GATE CSE 2026 \| Set 1 \| Question: 32 | **D** |
| `2.7.1` | Compilation Phases: GATE CSE 1987 \| Question: 1-xi | **C** |
| `2.7.2` | Compilation Phases: GATE CSE 1990 \| Question: 2-ix | **N/A** |
| `2.7.3` | Compilation Phases: GATE CSE 2005 \| Question: 61 | **A** |
| `2.7.4` | Compilation Phases: GATE CSE 2009 \| Question: 17 | **B** |
| `2.7.5` | Compilation Phases: GATE CSE 2015 \| Set 2 \| Question: 19 | **C** |
| `2.7.6` | Compilation Phases: GATE CSE 2016 \| Set 2 \| Question: 19 | **B** |
| `2.7.7` | Compilation Phases: GATE CSE 2017 \| Set 2 \| Question: 05 | **C** |
| `2.7.8` | Compilation Phases: GATE CSE 2018 \| Question: 8 | **B** |
| `2.7.9` | Compilation Phases: GATE CSE 2020 \| Question: 9 | **D** |
| `2.7.10` | Compilation Phases: GATE CSE 2021 \| Set 2 \| Question: 3 | **C** |
| `2.7.11` | Compilation Phases: GATE CSE 2023 \| Question: 1 | **B** |
| `2.7.12` | Compilation Phases: GATE CSE 2024 \| Set 2 \| Question: 11 | **B** |
| `2.7.13` | Compilation Phases: GATE CSE 2026 \| Set 1 \| Question: 17 | **C** |
| `2.8.1` | Compiler tokenization: GATE CSE 2026 \| Set 2 \| Question: 25 | **13:13** |
| `2.9.1` | Directed Acyclic Graph: GATE CSE 2014 \| Set 3 \| Question: 34 | **A** |
| `2.9.2` | Directed Acyclic Graph: GATE CSE 2021 \| Set 1 \| Question: 50 | **6** |
| `2.10.1` | Expression Evaluation: GATE CSE 2002 \| Question: 2.19 | **A** |
| `2.10.2` | Expression Evaluation: GATE CSE 2014 \| Set 2 \| Question: 39 | **6** |
| `2.11.1` | First and Follow: GATE CSE 1992 \| Question: 02,xiii | **A;B** |
| `2.11.2` | First and Follow: GATE CSE 2012 \| Question: 52 | **A** |
| `2.11.3` | First and Follow: GATE CSE 2017 \| Set 1 \| Question: 17 | **C** |
| `2.11.4` | First and Follow: GATE CSE 2019 \| Question: 19 | **31** |
| `2.11.5` | First and Follow: GATE CSE 2024 \| Set 1 \| Question: 28 | **A** |
| `2.11.6` | First and Follow: GATE CSE 2025 \| Set 1 \| Question: 36 | **A;D** |
| `2.12.1` | Grammar: GATE CSE 1988 \| Question: 10ia | **N/A** |
| `2.12.2` | Grammar: GATE CSE 1988 \| Question: 10ib | **N/A** |
| `2.12.3` | Grammar: GATE CSE 1990 \| Question: 16a | **N/A** |
| `2.12.4` | Grammar: GATE CSE 1991 \| Question: 10b | **N/A** |
| `2.12.5` | Grammar: GATE CSE 1991 \| Question: 10c | **N/A** |
| `2.12.6` | Grammar: GATE CSE 1992 \| Question: 02,xviii | **C** |
| `2.12.7` | Grammar: GATE CSE 1994 \| Question: 1.18 | **C** |
| `2.12.8` | Grammar: GATE CSE 1994 \| Question: 20 | **N/A** |
| `2.12.9` | Grammar: GATE CSE 1994 \| Question: 3.5 | **N/A** |
| `2.12.10` | Grammar: GATE CSE 1995 \| Question: 1.10 | **X** |
| `2.12.11` | Grammar: GATE CSE 1995 \| Question: 9 | **N/A** |
| `2.12.12` | Grammar: GATE CSE 1996 \| Question: 11 | **N/A** |
| `2.12.13` | Grammar: GATE CSE 1996 \| Question: 2.10 | **D** |
| `2.12.14` | Grammar: GATE CSE 1997 \| Question: 11 | **N/A** |
| `2.12.15` | Grammar: GATE CSE 1998 \| Question: 14 | **N/A** |
| `2.12.16` | Grammar: GATE CSE 1998 \| Question: 6b | **N/A** |
| `2.12.17` | Grammar: GATE CSE 1999 \| Question: 2.15 | **C** |
| `2.12.18` | Grammar: GATE CSE 2001 \| Question: 1.18 | **A** |
| `2.12.19` | Grammar: GATE CSE 2001 \| Question: 18 | **N/A** |
| `2.12.20` | Grammar: GATE CSE 2003 \| Question: 56 | **D** |
| `2.12.21` | Grammar: GATE CSE 2003 \| Question: 57 | **A** |
| `2.12.22` | Grammar: GATE CSE 2003 \| Question: 58 | **B** |
| `2.12.23` | Grammar: GATE CSE 2004 \| Question: 8 | **B** |
| `2.12.24` | Grammar: GATE CSE 2004 \| Question: 88 | **C** |
| `2.12.25` | Grammar: GATE CSE 2005 \| Question: 14 | **A** |
| `2.12.26` | Consider the grammar: | **D** |
| `2.12.27` | Grammar: GATE CSE 2006 \| Question: 32, ISRO2016-35 | **B** |
| `2.12.28` | Grammar: GATE CSE 2006 \| Question: 59 | **D** |
| `2.12.29` | Grammar: GATE CSE 2006 \| Question: 84 | **D** |
| `2.12.30` | The grammar | **A** |
| `2.12.31` | Grammar: GATE CSE 2007 \| Question: 52 | **C** |
| `2.12.32` | Grammar: GATE CSE 2007 \| Question: 53 | **C** |
| `2.12.33` | Grammar: GATE CSE 2007 \| Question: 78 | **C** |
| `2.12.34` | Grammar: GATE CSE 2007 \| Question: 79 | **B** |
| `2.12.35` | Grammar: GATE CSE 2008 \| Question: 50 | **C** |
| `2.12.36` | Grammar: GATE CSE 2010 \| Question: 38 | **C** |
| `2.12.37` | Grammar: GATE CSE 2016 \| Set 2 \| Question: 45 | **B** |
| `2.12.38` | Grammar: GATE CSE 2016 \| Set 2 \| Question: 46 | **A** |
| `2.12.39` | Grammar: GATE CSE 2017 \| Set 2 \| Question: 32 | **C** |
| `2.12.40` | Grammar: GATE CSE 2019 \| Question: 43 | **5** |
| `2.12.41` | Grammar: GATE CSE 2021 \| Set 1 \| Question: 31 | **A** |
| `2.12.42` | Grammar: GATE CSE 2024 \| Set 1 \| Question: 49 | **179** |
| `2.12.43` | Grammar: GATE CSE 2024 \| Set 2 \| Question: 42 | **B;C** |
| `2.12.44` | Grammar: GATE CSE 2025 \| Set 2 \| Question: 41 | **C;D** |
| `2.12.45` | Grammar: GATE IT 2005 \| Question: 83a | **A** |
| `2.12.46` | Grammar: GATE IT 2007 \| Question: 9 | **C** |
| `2.12.47` | Grammar: GATE IT 2008 \| Question: 78 | **D** |
| `2.13.1` | Intermediate Code: GATE CSE 1988 \| Question: 2xvii | **N/A** |
| `2.13.2` | Intermediate Code: GATE CSE 1989 \| Question: 4-v | **N/A** |
| `2.13.3` | Intermediate Code: GATE CSE 1992 \| Question: 11b | **N/A** |
| `2.13.4` | Intermediate Code: GATE CSE 1994 \| Question: 1.12 | **C** |
| `2.13.5` | Intermediate Code: GATE CSE 2014 \| Set 2 \| Question: 34 | **A** |
| `2.13.6` | Intermediate Code: GATE CSE 2014 \| Set 3 \| Question: 17 | **C** |
| `2.13.7` | Intermediate Code: GATE CSE 2015 \| Set 1 \| Question: 8 | **A** |
| `2.13.8` | Intermediate Code: GATE CSE 2015 \| Set 2 \| Question: 29 | **B** |
| `2.13.9` | Intermediate Code: GATE CSE 2021 \| Set 2 \| Question: 13 | **D** |
| `2.13.10` | Intermediate Code: GATE CSE 2024 \| Set 1 \| Question: 29 | **D** |
| `2.13.11` | Intermediate Code: GATE CSE 2024 \| Set 2 \| Question: 33 | **A** |
| `2.14.1` | LR Parser: GATE CSE 1992 \| Question: 02,xiv | **B;C;D** |
| `2.14.2` | LR Parser: GATE CSE 1998 \| Question: 1.26 | **C** |
| `2.14.3` | LR Parser: GATE CSE 2003 \| Question: 17 | **B** |
| `2.14.4` | LR Parser: GATE CSE 2005 \| Question: 60 | **B** |
| `2.14.5` | LR Parser: GATE CSE 2006 \| Question: 7 | **D** |
| `2.14.6` | LR Parser: GATE CSE 2008 \| Question: 55 | **B** |
| `2.14.7` | LR Parser: GATE CSE 2013 \| Question: 40 | **D** |
| `2.14.8` | LR Parser: GATE CSE 2013 \| Question: 9 | **B** |
| `2.14.9` | LR Parser: GATE CSE 2014 \| Set 1 \| Question: 34 | **D** |
| `2.14.10` | LR Parser: GATE CSE 2015 \| Set 3 \| Question: 16 | **C** |
| `2.14.11` | LR Parser: GATE CSE 2017 \| Set 2 \| Question: 6 | **A** |
| `2.14.12` | LR Parser: GATE CSE 2019 \| Question: 3 | **D** |
| `2.14.13` | LR Parser: GATE CSE 2020 \| Question: 24 | **7** |
| `2.14.14` | LR Parser: GATE CSE 2021 \| Set 1 \| Question: 5 | **C** |
| `2.14.15` | LR Parser: GATE CSE 2021 \| Set 2 \| Question: 51 | **8** |
| `2.14.16` | LR Parser: GATE CSE 2022 \| Question: 19 | **5** |
| `2.14.17` | LR Parser: GATE CSE 2022 \| Question: 3 | **D** |
| `2.14.18` | LR Parser: GATE CSE 2024 \| Set 2 \| Question: 55 | **9** |
| `2.14.19` | LR Parser: GATE CSE 2025 \| Set 2 \| Question: 30 | **C** |
| `2.14.20` | LR Parser: GATE CSE 2026 \| Set 2 \| Question: 31 | **D** |
| `2.15.1` | Lexical Analysis: GATE CSE 1987 \| Question: 1-xvii | **A** |
| `2.15.2` | Lexical Analysis: GATE CSE 2000 \| Question: 1.18, ISRO2015-25 | **C** |
| `2.15.3` | Lexical Analysis: GATE CSE 2010 \| Question: 13 | **B** |
| `2.15.4` | Lexical Analysis: GATE CSE 2011 \| Question: 1 | **C** |
| `2.15.5` | Lexical Analysis: GATE CSE 2011 \| Question: 19 | **A** |
| `2.15.6` | Lexical Analysis: GATE CSE 2018 \| Question: 37 | **D** |
| `2.16.1` | Linker: GATE CSE 1991 \| Question: 03,ix | **B** |
| `2.16.2` | Linker: GATE CSE 2003 \| Question: 76 | **C** |
| `2.16.3` | Linker: GATE CSE 2004 \| Question: 9 | **C** |
| `2.17.1` | Live Variable Analysis: GATE CSE 2015 \| Set 1 \| Question: 50 | **C** |
| `2.17.2` | Live Variable Analysis: GATE CSE 2021 \| Set 2 \| Question: 38 | **A** |
| `2.17.3` | Live Variable Analysis: GATE CSE 2023 \| Question: 27 | **D** |
| `2.18.1` | Ll Parser: GATE CSE 2024 \| Set 2 \| Question: 30 | **A** |
| `2.18.2` | Ll Parser: GATE CSE 2026 \| Set 1 \| Question: 18 | **C** |
| `2.19.1` | Macros: GATE CSE 1992 \| Question: 01,vii | **N/A** |
| `2.19.2` | Macros: GATE CSE 1995 \| Question: 1.11 | **D** |
| `2.19.3` | Macros: GATE CSE 1996 \| Question: 2.16 | **A** |
| `2.19.4` | Macros: GATE CSE 1997 \| Question: 1.9 | **D** |
| `2.20.1` | Operator Precedence: GATE CSE 1991 \| Question: 10a | **N/A** |
| `2.20.2` | Operator Precedence: GATE CSE 1997 \| Question: 1.6 | **A** |
| `2.20.3` | Operator Precedence: GATE CSE 2000 \| Question: 2.21, ISRO2015-24 | **B** |
| `2.20.4` | Operator Precedence: GATE CSE 2002 \| Question: 22 | **N/A** |
| `2.20.5` | Operator Precedence: GATE CSE 2011 \| Question: 27 | **B** |
| `2.20.6` | Operator Precedence: GATE CSE 2014 \| Set 2 \| Question: 17 | **B** |
| `2.20.7` | Operator Precedence: GATE CSE 2016 \| Set 1 \| Question: 45 | **9** |
| `2.20.8` | Operator Precedence: GATE CSE 2018 \| Question: 38 | **A** |
| `2.20.9` | Operator Precedence: GATE CSE 2024 \| Set 1 \| Question: 23 | **6** |
| `2.21.1` | Parameter Passing: GATE CSE 1988 \| Question: 2xv | **10** |
| `2.21.2` | Parameter Passing: GATE CSE 1988 \| Question: 8i | **N/A** |
| `2.21.3` | Parameter Passing: GATE CSE 1989 \| Question: 3-viii | **A;D** |
| `2.21.4` | Parameter Passing: GATE CSE 1990 \| Question: 11a | **N/A** |
| `2.21.5` | Parameter Passing: GATE CSE 1991 \| Question: 03,x | **A;D** |
| `2.21.6` | Parameter Passing: GATE CSE 1991 \| Question: 09a | **N/A** |
| `2.21.7` | Parameter Passing: GATE CSE 1991 \| Question: 09b | **N/A** |
| `2.21.8` | Parameter Passing: GATE CSE 1993 \| Question: 26 | **N/A** |
| `2.21.9` | Parameter Passing: GATE CSE 1995 \| Question: 2.4 | **A** |
| `2.21.10` | Parameter Passing: GATE CSE 1999 \| Question: 15 | **N/A** |
| `2.21.11` | Parameter Passing: GATE CSE 2003 \| Question: 74 | **X** |
| `2.21.12` | Parameter Passing: GATE CSE 2004 \| Question: 2,ISRO2017-54 | **D** |
| `2.21.13` | Parameter Passing: GATE CSE 2016 \| Set 1 \| Question: 36 | **D** |
| `2.21.14` | Parameter Passing: GATE IT 2007 \| Question: 33 | **D** |
| `2.22.1` | Parsing: GATE CSE 1987 \| Question: 1-xiv | **A** |
| `2.22.2` | Parsing: GATE CSE 1989 \| Question: 1-iii | **N/A** |
| `2.22.3` | Parsing: GATE CSE 1993 \| Question: 25 | **N/A** |
| `2.22.4` | Parsing: GATE CSE 1995 \| Question: 8 | **N/A** |
| `2.22.5` | Parsing: GATE CSE 1998 \| Question: 1.27 | **C** |
| `2.22.6` | Parsing: GATE CSE 1998 \| Question: 22 | **N/A** |
| `2.22.7` | Parsing: GATE CSE 1999 \| Question: 1.17 | **B** |
| `2.22.8` | Parsing: GATE CSE 2000 \| Question: 1.19, UGCNET-Dec2013-II: 30 | **A** |
| `2.22.9` | Parsing: GATE CSE 2001 \| Question: 16 | **N/A** |
| `2.22.10` | Parsing: GATE CSE 2003 \| Question: 16 | **D** |
| `2.22.11` | Parsing: GATE CSE 2005 \| Question: 83a | **C** |
| `2.22.12` | Parsing: GATE CSE 2005 \| Question: 83b | **B** |
| `2.22.13` | Parsing: GATE CSE 2006 \| Question: 58 | **A** |
| `2.22.14` | Parsing: GATE CSE 2007 \| Question: 18 | **A** |
| `2.22.15` | Parsing: GATE CSE 2008 \| Question: 11 | **D** |
| `2.22.16` | Parsing: GATE CSE 2009 \| Question: 42 | **B** |
| `2.22.17` | Parsing: GATE CSE 2012 \| Question: 53 | **C** |
| `2.22.18` | Parsing: GATE CSE 2015 \| Set 3 \| Question: 31 | **D** |
| `2.22.19` | Parsing: GATE CSE 2017 \| Set 1 \| Question: 43 | **1024** |
| `2.22.20` | Parsing: GATE CSE 2024 \| Set 1 \| Question: 16 | **A;D** |
| `2.22.21` | Parsing: GATE IT 2005 \| Question: 83b | **A** |
| `2.22.22` | Parsing: GATE IT 2008 \| Question: 79 | **A** |
| `2.23.1` | Register Allocation: GATE CSE 1997 \| Question: 4.9 | **A** |
| `2.23.2` | Register Allocation: GATE CSE 2004 \| Question: 10 | **B** |
| `2.23.3` | Register Allocation: GATE CSE 2010 \| Question: 37 | **B** |
| `2.23.4` | Register Allocation: GATE CSE 2011 \| Question: 36 | **D** |
| `2.23.5` | Register Allocation: GATE CSE 2013 \| Question: 48 | **B** |
| `2.23.6` | Register Allocation: GATE CSE 2017 \| Set 1 \| Question: 52 | **2** |
| `2.24.1` | Runtime Environment: GATE CSE 1988 \| Question: 2xii | **N/A** |
| `2.24.2` | Runtime Environment: GATE CSE 1989 \| Question: 10a | **N/A** |
| `2.24.3` | Runtime Environment: GATE CSE 1989 \| Question: 8b | **N/A** |
| `2.24.4` | Runtime Environment: GATE CSE 1990 \| Question: 2-v | **N/A** |
| `2.24.5` | Runtime Environment: GATE CSE 1990 \| Question: 4-v | **True** |
| `2.24.6` | Runtime Environment: GATE CSE 1993 \| Question: 7.7 | **D** |
| `2.24.7` | Runtime Environment: GATE CSE 1995 \| Question: 1.14 | **C** |
| `2.24.8` | Runtime Environment: GATE CSE 1996 \| Question: 2.17 | **D** |
| `2.24.9` | Runtime Environment: GATE CSE 1997 \| Question: 1.10 | **B** |
| `2.24.10` | Runtime Environment: GATE CSE 1997 \| Question: 1.8 | **C** |
| `2.24.11` | Runtime Environment: GATE CSE 1998 \| Question: 1.25, ISRO2008-41 | **C** |
| `2.24.12` | Runtime Environment: GATE CSE 1998 \| Question: 1.28 | **B** |
| `2.24.13` | Runtime Environment: GATE CSE 1998 \| Question: 2.15 | **C** |
| `2.24.14` | Runtime Environment: GATE CSE 2001 \| Question: 1.17 | **C** |
| `2.24.15` | Runtime Environment: GATE CSE 2002 \| Question: 2.20 | **B** |
| `2.24.16` | Runtime Environment: GATE CSE 2008 \| Question: 54 | **A** |
| `2.24.17` | Runtime Environment: GATE CSE 2010 \| Question: 14 | **C** |
| `2.24.18` | Runtime Environment: GATE CSE 2012 \| Question: 36 | **D** |
| `2.24.19` | Runtime Environment: GATE CSE 2014 \| Set 2 \| Question: 18 | **A** |
| `2.24.20` | Runtime Environment: GATE CSE 2014 \| Set 3 \| Question: 18 | **D** |
| `2.24.21` | Runtime Environment: GATE CSE 2021 \| Set 1 \| Question: 4 | **C** |
| `2.24.22` | Runtime Environment: GATE CSE 2023 \| Question: 26 | **A** |
| `2.25.1` | Static Single Assignment: GATE CSE 2015 \| Set 1 \| Question: 55 | **8** |
| `2.25.2` | Static Single Assignment: GATE CSE 2016 \| Set 1 \| Question: 19 | **10** |
| `2.25.3` | Static Single Assignment: GATE CSE 2017 \| Set 1 \| Question: 12 | **B** |
| `2.26.1` | Symbol Table: GATE CSE 2025 \| Set 1 \| Question: 2 | **C** |
| `2.27.1` | Syntax Directed Translation: GATE CSE 1992 \| Question: 11a | **N/A** |
| `2.27.2` | Syntax Directed Translation: GATE CSE 1995 \| Question: 2.10 | **A** |
| `2.27.3` | Syntax Directed Translation: GATE CSE 1996 \| Question: 20 | **N/A** |
| `2.27.4` | Syntax Directed Translation: GATE CSE 1998 \| Question: 23 | **N/A** |
| `2.27.5` | Syntax Directed Translation: GATE CSE 2000 \| Question: 19 | **N/A** |
| `2.27.6` | Syntax Directed Translation: GATE CSE 2001 \| Question: 17 | **N/A** |
| `2.27.7` | Syntax Directed Translation: GATE CSE 2003 \| Question: 18 | **B** |
| `2.27.8` | Syntax Directed Translation: GATE CSE 2003 \| Question: 59 | **B** |
| `2.27.9` | Syntax Directed Translation: GATE CSE 2004 \| Question: 45 | **C** |
| `2.27.10` | Syntax Directed Translation: GATE CSE 2016 \| Set 1 \| Question: 46 | **C** |
| `2.27.11` | Syntax Directed Translation: GATE CSE 2019 \| Question: 36 | **A** |
| `2.27.12` | Syntax Directed Translation: GATE CSE 2020 \| Question: 33 | **B** |
| `2.27.13` | Syntax Directed Translation: GATE CSE 2021 \| Set 1 \| Question: 26 | **B** |
| `2.27.14` | Syntax Directed Translation: GATE CSE 2022 \| Question: 55 | **80** |
| `2.27.15` | Syntax Directed Translation: GATE CSE 2023 \| Question: 50 | **2.375** |
| `2.27.16` | Syntax Directed Translation: GATE CSE 2024 \| Set 1 \| Question: 27 | **A** |
| `2.27.17` | Syntax Directed Translation: GATE CSE 2024 \| Set 2 \| Question: 19 | **B;D** |
| `2.27.18` | Syntax Directed Translation: GATE CSE 2025 \| Set 2 \| Question: 12 | **C** |
| `2.27.19` | Syntax Directed Translation: GATE CSE 2026 \| Set 1 \| Question: 43 | **A;B;D** |
| `2.28.1` | Variable Scope: GATE CSE 1987 \| Question: 1-xix | **A** |
| `2.28.2` | Variable Scope: GATE CSE 1987 \| Question: 1-xx | **B** |
| `2.29.1` | Viable Prefix: GATE CSE 2015 \| Set 1 \| Question: 13 | **C** |

