# Volume 2 — Chapter 6: Theory of Computation

- **Source PDF**: [filter1_volume2.pdf](file:///Users/adityaasaha/Documents/Academics/Gate/filter1_volume2.pdf)
- **Total GATE Questions in Chapter**: **293**

---

## 1. Subtopic Weightage & Question Distribution

| Subtopic # | Subtopic Name | Questions |
| :---: | :--- | :---: |
| **6.1** | Closure Property | 10 |
| **6.2** | Context Free Grammar | 2 |
| **6.3** | Context Free Language | 35 |
| **6.4** | Countable Uncountable Set | 3 |
| **6.5** | Decidability | 30 |
| **6.6** | Dpda | 1 |
| **6.7** | Finite Automata | 43 |
| **6.8** | Finite State Machines | 1 |
| **6.9** | Identify Class Language | 31 |
| **6.10** | Medium | 1 |
| **6.11** | Minimal State Automata | 25 |
| **6.12** | Non Determinism | 6 |
| **6.13** | Number of States | 2 |
| **6.14** | Pumping Lemma | 2 |
| **6.15** | Pushdown Automata | 15 |
| **6.16** | Recursive and Recursively Enumerable Languages | 16 |
| **6.17** | Reduction | 2 |
| **6.18** | Regular Expression | 29 |
| **6.20** | Regular Language | 35 |
| **6.21** | Turing Machine | 1 |


---

## 2. Comprehensive GATE CSE Theory of Computation Reference (Expanded Research & Formulas)

### 2.1 Chomsky Hierarchy & Automaton Equivalence
| Language Class | Grammar Type | Automaton | Closed Under | NOT Closed Under |
| :--- | :--- | :--- | :--- | :--- |
| **Regular (Type 3)** | Right-Linear / Left-Linear | DFA $\equiv$ NFA $\equiv$ $\epsilon$-NFA $\equiv$ RE | $\cup, \cap, \overline{L}, \cdot, *, L^R, L_1 - L_2$, Homomorphism, Quotient | Infinite union, subsets |
| **DCFL** | $LR(k)$ Grammar | Deterministic PDA (DPDA) | **Complement ($\overline{L}$)**, $L \cap R$ (with Regular $R$), Inverse Homomorphism | $\cup, \cap, \cdot, *, L^R$, Homomorphism |
| **CFL (Type 2)** | Context-Free ($A \to \alpha$) | Non-deterministic PDA (NPDA) | $\cup, \cdot, *, L^R$, Homomorphism, Inverse Homomorphism, **$L \cap R$** | **$\cap$, $\overline{L}$, $L_1 - L_2$** |
| **CSL (Type 1)** | Context-Sensitive ($|\alpha| \le |\beta|$) | Linear Bounded Automaton (LBA) | $\cup, \cap, \overline{L}, \cdot, *, L^R$ | $\epsilon$-free homomorphism |
| **Recursive (Decidable)** | — | Halting Turing Machine (Decider) | $\cup, \cap, \overline{L}, \cdot, *, L^R, L_1 - L_2$ | General Homomorphism |
| **Recursively Enumerable (Type 0)** | Unrestricted ($\alpha \to \beta$) | Turing Machine (TM) | $\cup, \cap, \cdot, *, L^R$, Homomorphism | **$\overline{L}$, $L_1 - L_2$** |

- **Crucial Closure Identities for GATE**:
  1. **Every Finite Language is Regular!** (Never be fooled by $L = \{a^n b^n \mid n \le 10^{100}\}$ — it is finite, hence **Regular**!)
  2. If $L$ is CFL and $R$ is Regular, then **$L \cap R$ is ALWAYS a CFL** (and if $L$ is DCFL, $L \cap R$ is DCFL).
  3. **Complementation Theorem for RE**: $L$ is Recursive **iff** both $L$ and $\overline{L}$ are Recursively Enumerable (RE). If $L$ is RE but not Recursive, then $\overline{L}$ is **NOT RE**.

### 2.2 Finite Automata (DFA / NFA) & Minimum State Counts
- **Subset Construction**: An $n$-state NFA converts to an equivalent DFA with at most **$2^n$ states**.
- **Myhill-Nerode Theorem**: Minimum number of states in a DFA for $L$ = number of equivalence classes of the distinguishability relation $\equiv_L$.
- **Standard Minimum DFA State Counts (Over $\Sigma = \{a, b\}$)**:
  - Strings of length $\ge k$ (or $\le k$, or $= k$): **$k + 2$ states**.
  - Strings where $k$-th symbol from the **left** is `'a'`: **$k + 2$ states**.
  - Strings where $k$-th symbol from the **right (end)** is `'a'`: NFA $= k + 1$ states; **Minimal DFA $= 2^k$ states**!
  - Strings containing a specific substring of length $k$: **$k + 1$ states**.
  - Strings with $\#_a(w) \equiv 0 \pmod{m}$ and $\#_b(w) \equiv 0 \pmod{n}$: **$m \times n$ states**.
  - Divisibility by $k$ in binary: at most $k$ states (more precisely, if $k = 2^r \cdot m$ with $m$ odd, minimal DFA has $m + r$ or $k$ states depending on leading-zero rules).

### 2.3 Master Table of Decidability & Undecidability (High-Yield GATE Table!)
| Problem | Regular (DFA/NFA/RE) | DCFL (DPDA) | CFL (CFG/NPDA) | CSL (LBA) | Rec. / RE (TM) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Membership ($w \in L?$)** | **Decidable** | **Decidable** | **Decidable** ($O(n^3)$ CYK) | **Decidable** | **Undecidable** (RE-complete) |
| **Emptiness ($L = \emptyset?$)** | **Decidable** | **Decidable** | **Decidable** | **Undecidable** | **Undecidable** (Not RE!) |
| **Finiteness ($|L| < \infty?$)** | **Decidable** | **Decidable** | **Decidable** | **Undecidable** | **Undecidable** |
| **Universality ($L = \Sigma^*?$)** | **Decidable** | **Decidable** | **Undecidable** | **Undecidable** | **Undecidable** |
| **Equivalence ($L_1 = L_2?$)** | **Decidable** | **Decidable!** | **Undecidable** | **Undecidable** | **Undecidable** |
| **Inclusion ($L_1 \subseteq L_2?$)** | **Decidable** | **Undecidable** | **Undecidable** | **Undecidable** | **Undecidable** |
| **Disjointness ($L_1 \cap L_2 = \emptyset?$)** | **Decidable** | **Undecidable** | **Undecidable** | **Undecidable** | **Undecidable** |
| **Regularity (Is $L$ Regular?)** | Trivial | **Decidable!** | **Undecidable** | **Undecidable** | **Undecidable** |
| **Ambiguity of Grammar** | — | — | **Undecidable** | **Undecidable** | **Undecidable** |

### 2.4 Rice's Theorem & Reductions
- **Rice's Theorem**: Every **non-trivial semantic property** $P$ of the language $L(M)$ recognized by a Turing machine $M$ is **undecidable**.
  - *Syntactic properties of the TM itself* (e.g., "Does $M$ have 50 states?", "Does $M$ halt on $w$ within 100 steps?", "Does $M$ ever move its head left on input $w$?") ARE **decidable**!
  - Furthermore, if $\emptyset \in P$ (the empty language satisfies property $P$), then $\{ \langle M \rangle \mid L(M) \in P \}$ is **not even RE**!
- **Many-One Reduction ($A \le_m B$)**:
  - If $A \le_m B$ and $B$ is Decidable $\implies A$ is Decidable.
  - If $A \le_m B$ and $A$ is Undecidable $\implies B$ is Undecidable.
  - If $A \le_m B$ and $B$ is RE $\implies A$ is RE.

---

## 3. Original PDF Chapter Notes (Preserved Verbatim)

6 Theory of Computation (293)
Regular expressions and finite automata, Context-free grammars and push-down automata, Regular and
context-free languages, Pumping lemma, Turing machines and undecidability.
Welcome to the "Theory of Computation" chapter, a cornerstone of Computer Science that delves into the fundamental
capabilities and limitations of computational models. This subject is crucial for the GATE CS exam as it builds a strong
theoretical foundation for understanding algorithms, programming languages, and system design. It typically carries a
weightage of 8-12 marks, with questions ranging from conceptual understanding of language classes and machine
models to problem-solving involving the design of automata, grammar conversions, and decidability proofs. Expect a
mix of Multiple Choice Questions (MCQs), Multiple Select Questions (MSQs), and Numerical Answer Type (NAT)
questions, often requiring a deep grasp of definitions, properties, and theorems.
Topic-wise Key Concepts
Finite Automata (FA)
Finite Automata are the simplest computational models, used to recognize regular languages. They have a finite
number of states and transitions based on input symbols, without any auxiliary memory. They are fundamental for
lexical analysis in compilers and designing simple control systems.
Definition: A Deterministic Finite Automaton (DFA) is formally defined as a 5-tuple , where:
1. is a finite set of states.
2. is a finite set of input symbols (alphabet).
3. is the transition function.
4. is the initial state.
5. is the set of final (accepting) states.
Key Properties:
Every NFA has an equivalent DFA.
DFA and NFA recognize the same class of languages (Regular Languages).
DFA can be minimized to a unique (up to isomorphism) minimal state DFA.
Common Pitfalls: Incorrectly handling epsilon transitions in NFA to DFA conversion; confusing acceptance criteria
for NFA/DFA.
Problem-Solving Techniques:
Subset Construction: For converting NFA to DFA.
Table Filling Algorithm / Myhill-Nerode Theorem: For DFA minimization.
State Elimination Method / Arden's Theorem: For converting FA to Regular Expression.
Finite State Machines (FSM)
Finite State Machines are mathematical models of computation used to design systems that can be in one of a finite
number of states. While often used interchangeably with FA, FSMs typically include an output function, making them
suitable for modeling sequential circuits and control logic.
Definition:
Mealy Machine: function. Output depends on current state and input.
Moore Machine: , where is the output alphabet, and , where is the output
is the output function. Output depends only on
the current state.
Key Properties:
Any Mealy machine can be converted to an equivalent Moore machine, and vice-versa.
Moore machine output is delayed by one clock cycle compared to Mealy.
Common Pitfalls: Incorrectly converting between Mealy and Moore machines, especially handling initial state
outputs.
Problem-Solving Techniques: State diagram construction, state table analysis, conversion algorithms between

*(PDF Page 322)*

Mealy and Moore.
Regular Expression (RE)
Regular Expressions are a powerful notation for describing regular languages. They provide a concise way to specify
patterns of strings, widely used in text processing, search engines, and lexical analysis.
Definition: A Regular Expression is built using basic symbols and three operations:
Union: (or ) represents strings in or .
Concatenation: represents strings formed by concatenating a string from with one from .
Kleene Star: represents zero or more concatenations of strings from , including the empty string .
Key Identities:
Common Pitfalls: Operator precedence (Kleene star > concatenation > union); incorrect application of identities.
Problem-Solving Techniques:
Arden's Theorem: For solving equations of the form to get .
State Elimination Method: For converting FA to RE.
Regular Grammar (RG)
Regular Grammars are a type of formal grammar that generates exactly the class of regular languages. They are
restricted in their production rules, making them less powerful than Context-Free Grammars but simpler to parse.
Definition: A grammar is regular if all its production rules are of one of the following forms:
Right-linear: or or , where (non-terminals), (terminal).
Left-linear: or or , where , .
Key Properties:
A grammar cannot be both right-linear and left-linear simultaneously (unless it generates a finite language).
Regular Grammars, Regular Expressions, and Finite Automata are all equivalent in terms of language
recognition power.
Common Pitfalls: Mixing right-linear and left-linear rules in the same grammar; incorrectly converting between FA
and RG.
Problem-Solving Techniques: Constructing an FA from a RG, and vice-versa, by mapping non-terminals to states
and productions to transitions.
Regular Language (RL)
Regular Languages are the simplest class of languages in the Chomsky Hierarchy, recognized by Finite Automata,
described by Regular Expressions, or generated by Regular Grammars. They represent patterns that can be matched
without requiring memory beyond the current state.
Definition: A language is regular if and only if it can be recognized by a Finite Automaton.
Key Properties (Closure Properties): Regular languages are closed under:
Union ( )
Intersection ( )
Complement ( )
Concatenation ( )
Kleene Star ( )
Reversal ( )
Homomorphism, Inverse Homomorphism
Common Pitfalls: Misidentifying non-regular languages as regular; incorrectly applying closure properties.
Problem-Solving Techniques:
Pumping Lemma for Regular Languages: The primary tool to prove a language is NOT regular.
Myhill-Nerode Theorem: Can be used to prove regularity or non-regularity, and for DFA minimization.

*(PDF Page 323)*

Non Determinism
Non-determinism in automata allows for multiple possible transitions from a given state on a given input symbol, or
transitions on an empty string (epsilon transitions). It often simplifies the design of automata, though it doesn't increase
their computational power for regular languages.
Definition: A Non-deterministic Finite Automaton (NFA) is a 5-tuple is the transition function, mapping to a set of states.
, where
Key Properties:
Every NFA has an equivalent DFA (recognizes the same language).
An NFA can be exponentially more concise than its equivalent DFA (e.g., an NFA with states might require up
to states in the equivalent DFA).
Non-determinism is crucial for Pushdown Automata (NPDA is more powerful than DPDA).
Common Pitfalls: Incorrectly handling epsilon closures; missing possible paths in non-deterministic transitions.
Problem-Solving Techniques:
Subset Construction Algorithm: The standard method to convert an NFA (with or without epsilon transitions)
to an equivalent DFA.
Understanding how to trace paths in an NFA to determine language acceptance.
Number of States
The "number of states" refers to the cardinality of the set of states in an automaton. This concept is critical for
understanding the complexity and minimality of machine models, particularly for finite automata.
Key Properties:
For an NFA with states, the equivalent DFA can have up to states.
A minimal DFA for a given regular language is unique (up to isomorphism) and has the fewest possible states.
The number of states in a minimal DFA is equal to the number of equivalence classes of the Myhill-Nerode
relation.
Common Pitfalls: Failing to identify redundant or unreachable states, which leads to non-minimal DFAs.
Problem-Solving Techniques:
DFA Minimization Algorithms: Partitioning states into distinguishable/indistinguishable sets.
Myhill-Nerode Theorem: Using equivalence classes of strings to determine the minimum number of states.
Minimal State Automata
A Minimal State Automaton (specifically, a Minimal DFA) is a Deterministic Finite Automaton that recognizes a given
regular language using the smallest possible number of states. It is unique for any given regular language and is crucial
for efficient implementation.
Definition: A DFA is minimal if there is no other DFA such that and .
Key Properties:
Every regular language has a unique minimal DFA (up to isomorphism).
All states in a minimal DFA must be reachable from the start state and must be distinguishable from each other.
Common Pitfalls: Incorrectly merging distinguishable states; not removing unreachable states before minimization.
Problem-Solving Techniques:
Table Filling Algorithm (or Partitioning Algorithm):
1. Initialize a table of all pairs of states . Mark all pairs where and (or vice versa) as
distinguishable.
2. Iteratively mark as distinguishable if for some input symbol , is already marked
distinguishable.
3. Repeat until no new pairs can be marked. All unmarked pairs are indistinguishable and can be merged.
Myhill-Nerode Theorem: States that a language is regular if and only if the number of equivalence classes of
the Myhill-Nerode relation is finite. The number of states in the minimal DFA is equal to the number of these
equivalence classes.
Pumping Lemma (for Regular Languages)
The Pumping Lemma for Regular Languages is a fundamental theorem used to prove that a language is NOT regular.
It states that all sufficiently long strings in a regular language can be "pumped" (i.e., a middle section of the string can
be repeated any number of times) and the resulting string will still be in the language.

*(PDF Page 324)*

Theorem: If is a regular language, then there exists some integer (the pumping length) such that for any
string with , can be divided into three parts satisfying the conditions:
1. (the middle part cannot be empty).
2. (the pumpable part must occur within the first symbols).
3. For all , the string .
Key Properties:
It is a necessary condition for regularity, not a sufficient one. It can only be used to prove non-regularity.
The proof strategy is usually by contradiction (an "adversary game").
Common Pitfalls:
Trying to prove regularity using the Pumping Lemma (it's impossible).
Incorrectly choosing the string or the partition to break the lemma.
Forgetting the condition or .
Problem-Solving Techniques:
1. Assume is regular and let be the pumping length.
2. Choose a "hard" string such that , typically one that grows with (e.g., ).
3. Consider all possible ways to divide into satisfying and .
4. For each division, find an such that . This contradicts the lemma, proving is not regular.
Closure Property
Closure properties describe whether a class of languages remains within that class after applying certain operations.
Understanding these properties is vital for classifying languages and proving relationships between language classes.
Definition: A class of languages is closed under an operation if, for any language , the result of
(or ) is also in .
Key Properties (to memorize):
Regular
Context-Free
Recursive
Operation
Languages
Languages
Languages
Recursively Enumerable
Languages
Union Yes Yes Yes Yes
Intersection Yes No Yes Yes
Complement Yes No Yes No
Concatenation Yes Yes Yes Yes
Kleene Star Yes Yes Yes Yes
Reversal Yes Yes Yes Yes
Homomorphism Yes Yes Yes Yes
Inverse
Yes Yes Yes Yes
Homomorphism
Common Pitfalls: Confusing closure properties between different language classes, especially for intersection and
complement.
Problem-Solving Techniques: Use closure properties to deduce the class of a new language based on known
languages and operations. For non-closure, use counterexamples.
Context Free Grammar (CFG)
Context-Free Grammars are more powerful than regular grammars and are used to describe Context-Free Languages.
They are fundamental to defining the syntax of programming languages and parsing. Productions allow a non-terminal
to be replaced by a string of terminals and non-terminals, regardless of its context.
Definition: A CFG is a 4-tuple , where:
1. is a finite set of non-terminal symbols.
2. is a finite set of terminal symbols.
3. is a finite set of production rules of the form , where and .
4. is the start symbol.
Key Forms:
Chomsky Normal Form (CNF): All productions are of the form or , where and
.
-productions are allowed only for the start symbol if it doesn't appear on the RHS.
Greibach Normal Form (GNF): All productions are of the form , where , , and .
Common Pitfalls: Detecting ambiguity (a string having more than one leftmost/rightmost derivation or parse tree);
incorrect conversion to CNF/GNF.

*(PDF Page 325)*

Problem-Solving Techniques:
Simplification of CFG: Removing useless symbols,
-productions, and unit productions.
Conversion to CNF/GNF: Systematic procedures involving variable substitution and rule modification.
Derivation trees, leftmost/rightmost derivations.
Context Free Language (CFL)
Context-Free Languages are recognized by Pushdown Automata and generated by Context-Free Grammars. They can
describe languages with nested structures, such as balanced parentheses or properly nested HTML tags, which regular
languages cannot handle.
Definition: A language is Context-Free if and only if it can be generated by a Context-Free Grammar.
Key Properties:
Closure Properties: Closed under union, concatenation, Kleene star, reversal, homomorphism, inverse
homomorphism.
Non-Closure Properties: NOT closed under intersection, complement.
Deterministic CFLs (DCFLs) are a proper subset of CFLs and are closed under complement.
Common Pitfalls: Misidentifying non-CFLs as CFLs; incorrectly applying closure properties.
Problem-Solving Techniques:
Pumping Lemma for CFLs: The primary tool to prove a language is NOT context-free.
Designing CFGs or PDAs for given languages.
Pushdown Automata (PDA)
Pushdown Automata are an extension of Finite Automata with an additional stack memory. This stack allows PDAs to
recognize Context-Free Languages, which require memory to handle nested structures, unlike regular languages.
Definition: A Pushdown Automaton is formally defined as a 7-tuple , where:
1. is a finite set of states.
2. is the input alphabet.
3. is the stack alphabet.
4. is the transition function.
5. is the initial state.
6. is the initial stack symbol.
7. is the set of final states.
Key Properties:
Non-deterministic PDAs (NPDAs) are more powerful than Deterministic PDAs (DPDAs). NPDAs recognize all
CFLs, while DPDAs recognize only DCFLs (a proper subset of CFLs).
PDAs can accept languages either by final state or by empty stack. These two modes are equivalent for NPDAs.
Common Pitfalls: Incorrectly handling stack operations (push/pop); confusing acceptance criteria; designing a
DPDA when an NPDA is required.
Problem-Solving Techniques:
Designing PDAs for given CFLs, focusing on how the stack is used to remember context.
Converting CFG to PDA and vice-versa.
Dpda (Deterministic Pushdown Automata)
A Deterministic Pushdown Automaton (DPDA) is a PDA where for any given state, input symbol (or epsilon), and stack
top, there is at most one possible transition. DPDAs recognize Deterministic Context-Free Languages (DCFLs), which
are a proper subset of CFLs.
Definition: A PDA is deterministic if its transition function satisfies:
1. For any , .
2. If , then for all . (No conflict between epsilon and input transitions).
Key Properties:
DPDAs recognize DCFLs. All regular languages are DCFLs.
DCFLs are closed under complement (unlike general CFLs).
Not all CFLs are DCFLs (e.g., is a CFL but not a DCFL).
Common Pitfalls: Failing to ensure determinism in all transition cases; confusing DCFLs with general CFLs.
Problem-Solving Techniques: Designing DPDAs requires careful consideration to avoid non-deterministic choices.
Often involves lookahead or specific stack symbol usage.

*(PDF Page 326)*

Pumping Lemma (for CFLs)
The Pumping Lemma for Context-Free Languages is a more generalized version of the Pumping Lemma for Regular
Languages. It's used to prove that certain languages are NOT context-free, by showing that sufficiently long strings in a
CFL can be "pumped" in a specific way.
Theorem: If is a Context-Free Language, then there exists some integer (the pumping length) such that for
any string with , can be divided into five parts satisfying the conditions:
1. (at least one of or must be non-empty).
2. (the pumpable parts must occur relatively close to each other).
3. For all , the string .
Key Properties:
It is a necessary condition for context-freeness, not a sufficient one. It can only be used to prove non-context-
freeness.
The proof strategy is by contradiction (an "adversary game"), similar to the regular pumping lemma.
Common Pitfalls:
Trying to prove context-freeness using the Pumping Lemma.
Incorrectly choosing the string or the partition .
Forgetting the conditions or .
Problem-Solving Techniques:
1. Assume is CFL and let be the pumping length.
2. Choose a "hard" string such that , typically one that involves three dependent counts (e.g.,
).
3. Consider all possible ways to divide into satisfying and .
4. For each division, find an such that . This contradicts the lemma, proving is not CFL.
Turing Machine (TM)
The Turing Machine is the most powerful and widely accepted model of computation, capable of simulating any
algorithm. It consists of a finite control unit, a read/write head, and an infinite tape. It forms the basis of the Church-
Turing Thesis, which states that any effectively computable function can be computed by a Turing Machine.
Definition: A Turing Machine is formally defined as a 7-tuple , where:
1. is a finite set of states.
2. is the input alphabet (not containing ).
3. is the tape alphabet ( , and ).
4. is the transition function (L for left, R for right).
5. is the initial state.
6. is the blank symbol.
7. is the set of final (halting) states.
Key Properties:
Turing Machines can recognize Recursively Enumerable Languages.
Variations of TMs (multi-tape, multi-head, non-deterministic) have equivalent computational power to the basic
TM.
The Halting Problem for Turing Machines is undecidable.
Common Pitfalls: Designing complex TMs; understanding the implications of the halting problem; confusing
decidability with recognizability.
Problem-Solving Techniques:
Designing TMs for various languages (e.g., , palindrome recognition).
Understanding the Church-Turing Thesis and its implications for computability.
Recursive and Recursively Enumerable Languages
These two classes of languages represent the limits of what Turing Machines can compute. They are central to the
study of computability and decidability.
Definition:
Recursively Enumerable Language (RE / Recognizable): A language is RE if there exists a Turing Machine
that halts and accepts every string , but may either halt and reject or loop indefinitely for strings
.

*(PDF Page 327)*

Recursive Language (Decidable): A language is Recursive if there exists a Turing Machine all inputs. For , accepts; for , rejects.
Key Properties:
Every Recursive Language is also Recursively Enumerable.
A language is Recursive if and only if both and its complement are Recursively Enumerable.
RE languages are closed under union, intersection, concatenation, Kleene star, homomorphism, inverse
homomorphism. They are NOT closed under complement.
Recursive languages are closed under union, intersection, complement, concatenation, Kleene star,
homomorphism, inverse homomorphism.
Common Pitfalls: Confusing the definitions of "halts on all inputs" (decidable) vs.
"halts and accepts"
(recognizable); misinterpreting closure properties.
Problem-Solving Techniques: Using closure properties to classify languages; applying reduction to prove
undecidability/non-recognizability.
that halts on
Decidability
Decidability refers to whether an algorithm (a Turing Machine that always halts) exists to solve a given problem. A
problem is decidable if there's an algorithm that can always give a "yes" or "no" answer in finite time for any instance of
the problem.
Definition: A problem is decidable if the language representing all "yes" instances of the problem is a Recursive
Language.
Key Properties (Examples of Decidable/Undecidable Problems):
Decidable:
Membership problem for Regular Languages (Is ?).
Emptiness problem for Regular Languages (Is ?).
Equivalence problem for Regular Languages (Is ?).
Membership problem for CFLs (Is ?).
Emptiness problem for CFLs (Is ?).
Undecidable:
Halting Problem for TMs (Does TM halt on input ?).
Equivalence problem for CFLs (Is ?).
Ambiguity problem for CFGs (Is CFG ambiguous?).
Membership problem for RE languages (Is ? - this is RE, but not Recursive).
Emptiness problem for TMs (Is ?).
Post Correspondence Problem (PCP).
Common Pitfalls: Assuming all problems are decidable; misremembering the decidability status of common
problems.
Problem-Solving Techniques:
Reduction: The primary method to prove a problem is undecidable.
Understanding Rice's Theorem (all non-trivial properties of RE languages are undecidable).
Reduction
Reduction is a powerful technique used to prove the undecidability of problems. If problem A can be "reduced" to
problem B, it means that an algorithm for solving B could be used to solve A. Therefore, if A is known to be
undecidable, B must also be undecidable.
Definition: A problem is reducible to problem (denoted for many-one reduction) if there exists a
computable function that transforms every instance of problem into an instance of problem such that
is a "yes" instance of if and only if is a "yes" instance of .
Key Properties:
If and is undecidable, then is undecidable.
If and is decidable, then is decidable.
If and is non-RE, then is non-RE.
If and is RE, then is RE.
Common Pitfalls: Reducing in the wrong direction (e.g., trying to reduce an undecidable problem to a decidable
one); constructing an incorrect transformation function .
Problem-Solving Techniques:
Identify a known undecidable problem (e.g., Halting Problem, Emptiness Problem for TMs) to reduce FROM.

*(PDF Page 328)*

Construct a transformation function into an instance of the target problem.
Prove that this transformation preserves the "yes/no" answer.
that takes an instance of the known undecidable problem and converts it
Countable Uncountable Set
These concepts from set theory are crucial for understanding the limits of computation, particularly why there exist
languages that are not recursively enumerable. It relates to the cardinality of sets.
Definition:
Countable Set: A set is countable if it is finite or if its elements can be put into a one-to-one correspondence with
the set of natural numbers (i.e., it can be enumerated). Examples: integers , rational numbers , set of all
finite strings .
Uncountable Set: A set is uncountable if it is infinite but cannot be put into a one-to-one correspondence with .
Examples: real numbers , power set of , set of all languages over .
Key Properties:
The set of all Turing Machines is countable.
The set of all possible languages over any alphabet is uncountable.
Since there are more languages than Turing Machines, there must exist languages that cannot be recognized by
any Turing Machine (i.e., non-RE languages).
Common Pitfalls: Confusing finite sets with infinite countable sets; misapplying diagonalization.
Problem-Solving Techniques:
Diagonalization Argument: A standard technique to prove a set is uncountable (e.g., Cantor's diagonalization
for real numbers).
Understanding the implications for computability theory.
Identify Class Language
This topic refers to the ability to correctly classify a given language within the Chomsky Hierarchy, which organizes
formal languages by their generative power and the type of automaton that recognizes them.
Chomsky Hierarchy (from least to most powerful):
1. Type 3: Regular Languages (RL): Recognized by Finite Automata (FA). Generated by Regular Grammars
(RG).
2. Type 2: Context-Free Languages (CFL): Recognized by Pushdown Automata (PDA). Generated by Context-
Free Grammars (CFG). (Deterministic CFLs (DCFLs) are a proper subset of CFLs, recognized by DPDAs).
3. Type 1: Context-Sensitive Languages (CSL): Recognized by Linear Bounded Automata (LBA). Generated by
Context-Sensitive Grammars (CSG). (Less common in GATE).
4. Type 0: Recursively Enumerable Languages (RE): Recognized by Turing Machines (TM). Generated by
Unrestricted Grammars. (Recursive Languages are a proper subset of RE languages, recognized by TMs that
always halt).
Relationships: .
Common Pitfalls: Incorrectly applying pumping lemmas; misjudging the memory requirements of a language;
confusing closure properties.
Problem-Solving Techniques:
Pumping Lemma: First attempt to prove non-regularity or non-context-freeness.
Closure Properties: Use them to combine or transform languages and deduce their class.
Machine Models: Try to design the simplest machine (FA, PDA, TM) that can recognize the language.
Grammar Rules: Analyze the structure of production rules if a grammar is given.
Medium (Computational Models)
In the context of Theory of Computation,
"Medium" refers to the abstract computational models or machines used to
define and study computation. These models, such as Finite Automata, Pushdown Automata, and Turing Machines,
represent different levels of computational power and memory capabilities.
Definition: Computational models are abstract machines that define the capabilities and limitations of algorithms.
Each model specifies a set of operations and memory structures it can use.
Key Models and Their Power:
Finite Automata (FA): No auxiliary memory. Recognizes Regular Languages. Simplest model.
Pushdown Automata (PDA): Finite control + a stack (LIFO memory). Recognizes Context-Free Languages.
More powerful than FA.

*(PDF Page 329)*

Turing Machine (TM): Finite control + an infinite tape (random access memory). Recognizes Recursively
Enumerable Languages. Most powerful model, equivalent to any real-world computer.
Key Properties:
The hierarchy of computational power (FA < PDA < TM) directly corresponds to the Chomsky Hierarchy of
languages.
Each model defines the class of languages it can recognize (its "computational power").
Common Pitfalls: Confusing the memory capabilities of different models; overestimating or underestimating the
power of a specific model.
Problem-Solving Techniques:
Analyze the memory requirements of a language to determine the minimum computational model needed to
recognize it.
Understand how each model's memory structure (or lack thereof) limits its ability to recognize certain patterns
(e.g., FA cannot count arbitrary numbers of symbols).
Quick Formula Reference
DFA:
NFA: , where
Regular Expression Operations: Union , Concatenation , Kleene Star
Arden's Theorem: If , then .
Regular Grammar (Right-linear): or or
Pumping Lemma for Regular Languages: For with : , , .
Context-Free Grammar (CFG): , with productions .
Chomsky Normal Form (CNF): or .
Greibach Normal Form (GNF): .
Pushdown Automata (PDA): , with transitions .
Pumping Lemma for Context-Free Languages: For with : , ,
.
Turing Machine (TM): , with transitions .
Chomsky Hierarchy: .
Closure Properties (Summary):
Operation RL CFL Recursive RE
Union Y Y Y Y
Intersection Y N Y Y
Complement Y N Y N
Concatenation Y Y Y Y
Kleene Star Y Y Y Y
Reversal Y Y Y Y
Important Tips for GATE
1. Master the Chomsky Hierarchy: Understand the relationships between language classes (Regular, CFL,
Recursive, RE) and their corresponding machine models (FA, PDA, TM). This is fundamental for classifying
languages and solving many conceptual questions.
2. Memorize Closure Properties: Create a table and commit to memory which language classes are closed under
which operations (union, intersection, complement, concatenation, Kleene star, reversal). This is a frequent source
of direct questions.
3. Practice Pumping Lemma Proofs: The Pumping Lemma for both Regular and Context-Free Languages is a
crucial tool. Practice choosing the "hard" string and demonstrating the contradiction for various non-regular/non-
CFLs. Remember, it only proves non-membership.
4. Understand NFA to DFA Conversion and Minimization: Be proficient in subset construction for NFA to DFA
conversion and the table-filling algorithm for DFA minimization. These are common problem-solving tasks.
5. Distinguish Decidability vs. Recognizability: Clearly understand the difference between Recursive (decidable)
and Recursively Enumerable (recognizable) languages, especially regarding the halting behavior of Turing
Machines. Know the decidability status of common problems (Halting Problem, Emptiness for TMs, Equivalence for
CFLs, etc.).
6. Focus on Design Principles: While complex designs are rare, understand the core principles of designing simple
FAs, PDAs, and TMs for basic languages. Pay attention to how memory (or lack thereof) is utilized.
7. Pay Attention to Formal Definitions: GATE questions often test your understanding of the precise formal

*(PDF Page 330)*

definitions of automata, grammars, and languages. Small details like epsilon transitions, initial stack symbols, or
blank tape symbols can be critical.
8. Time Management for Tricky Questions: Some ToC problems, especially those involving complex reductions or
intricate Pumping Lemma applications, can be time-consuming. Practice identifying these quickly and decide
whether to attempt them or mark for review.

---

## 4. Complete Question Index & Answer Key Record (293 Questions)

| Q # | Question Source / Title | Answer Key |
| :---: | :--- | :---: |
| `6.1.1` | Closure Property: GATE CSE 1989 \| Question: 3-ii | **A;C** |
| `6.1.2` | Closure Property: GATE CSE 1992 \| Question: 16 | **A;B** |
| `6.1.3` | Closure Property: GATE CSE 2002 \| Question: 2.14 | **A** |
| `6.1.4` | Closure Property: GATE CSE 2013 \| Question: 17 | **C** |
| `6.1.5` | Closure Property: GATE CSE 2016 \| Set 2 \| Question: 18 | **D** |
| `6.1.6` | Closure Property: GATE CSE 2017 \| Set 2 \| Question: 04 | **B** |
| `6.1.7` | Closure Property: GATE CSE 2018 \| Question: 7 | **B** |
| `6.1.8` | Closure Property: GATE CSE 2025 \| Set 2 \| Question: 20 | **B;C** |
| `6.1.9` | Closure Property: GATE CSE 2026 \| Set 1 \| Question: 41 | **C** |
| `6.1.10` | Closure Property: GATE IT 2006 \| Question: 32 | **D** |
| `6.2.1` | Context Free Grammar: GATE CSE 2025 \| Set 1 \| Question: 9 | **A** |
| `6.2.2` | Context Free Grammar: GATE CSE 2026 \| Set 1 \| Question: 15 | **A;B;C** |
| `6.3.1` | Context Free Language: GATE CSE 1987 \| Question: 2k | **False** |
| `6.3.2` | Context Free Language: GATE CSE 1992 \| Question: 02,xix | **A;D** |
| `6.3.3` | Context Free Language: GATE CSE 1995 \| Question: 2.20 | **A** |
| `6.3.4` | Context Free Language: GATE CSE 1996 \| Question: 2.8 | **B** |
| `6.3.5` | Context Free Language: GATE CSE 1996 \| Question: 2.9 | **B** |
| `6.3.6` | Context Free Language: GATE CSE 1999 \| Question: 1.5 | **B** |
| `6.3.7` | Context Free Language: GATE CSE 1999 \| Question: 7 | **N/A** |
| `6.3.8` | Context Free Language: GATE CSE 2000 \| Question: 7 | **N/A** |
| `6.3.9` | Context Free Language: GATE CSE 2001 \| Question: 1.5 | **B** |
| `6.3.10` | Context Free Language: GATE CSE 2003 \| Question: 51 | **C** |
| `6.3.11` | Context Free Language: GATE CSE 2005 \| Question: 57 | **B** |
| `6.3.12` | Context Free Language: GATE CSE 2006 \| Question: 19 | **D** |
| `6.3.13` | Context Free Language: GATE CSE 2009 \| Question: 12, ISRO2016-37 | **B** |
| `6.3.14` | Context Free Language: GATE CSE 2015 \| Set 3 \| Question: 32 | **B** |
| `6.3.15` | Context Free Language: GATE CSE 2016 \| Set 1 \| Question: 16 | **D** |
| `6.3.16` | Context Free Language: GATE CSE 2016 \| Set 1 \| Question: 42 | **D** |
| `6.3.17` | Context Free Language: GATE CSE 2016 \| Set 2 \| Question: 43 | **B** |
| `6.3.18` | Context Free Language: GATE CSE 2017 \| Set 1 \| Question: 10 | **B** |
| `6.3.19` | Context Free Language: GATE CSE 2017 \| Set 1 \| Question: 34 | **D** |
| `6.3.20` | Context Free Language: GATE CSE 2017 \| Set 1 \| Question: 38 | **A** |
| `6.3.21` | Context Free Language: GATE CSE 2017 \| Set 2 \| Question: 16 | **C** |
| `6.3.22` | Context Free Language: GATE CSE 2019 \| Question: 31 | **C** |
| `6.3.23` | Context Free Language: GATE CSE 2021 \| Set 1 \| Question: 1 | **C** |
| `6.3.24` | Context Free Language: GATE CSE 2021 \| Set 2 \| Question: 41 | **B;C;D** |
| `6.3.25` | Context Free Language: GATE CSE 2022 \| Question: 38 | **B;C;D** |
| `6.3.26` | Context Free Language: GATE CSE 2023 \| Question: 29 | **B** |
| `6.3.27` | Context Free Language: GATE CSE 2025 \| Set 1 \| Question: 35 | **C** |
| `6.3.28` | Context Free Language: GATE CSE 2026 \| Set 1 \| Question: 42 | **B;D** |
| `6.3.29` | Context Free Language: GATE CSE 2026 \| Set 2 \| Question: 38 | **A;C;D** |
| `6.3.30` | Context Free Language: GATE IT 2006 \| Question: 34 | **B** |
| `6.3.31` | Context Free Language: GATE IT 2006 \| Question: 4 | **B** |
| `6.3.32` | Context Free Language: GATE IT 2007 \| Question: 46 | **A** |
| `6.3.33` | Context Free Language: GATE IT 2007 \| Question: 48 | **C** |
| `6.3.34` | Context Free Language: GATE IT 2007 \| Question: 49 | **D** |
| `6.3.35` | Context Free Language: GATE IT 2008 \| Question: 34 | **B** |
| `6.4.1` | Countable Uncountable Set: GATE CSE 1997 \| Question: 3.4 | **B** |
| `6.4.2` | Countable Uncountable Set: GATE CSE 2014 \| Set 3 \| Question: 16 | **C** |
| `6.4.3` | Countable Uncountable Set: GATE CSE 2019 \| Question: 34 | **B** |
| `6.5.1` | Decidability: GATE CSE 1987 \| Question: 2l | **True** |
| `6.5.2` | Decidability: GATE CSE 1987 \| Question: 2m | **True** |
| `6.5.3` | Decidability: GATE CSE 1988 \| Question: 2viii | **N/A** |
| `6.5.4` | Decidability: GATE CSE 1989 \| Question: 3-iii | **B;D** |
| `6.5.5` | Decidability: GATE CSE 1990 \| Question: 3-vii | **B;C** |
| `6.5.6` | Decidability: GATE CSE 1995 \| Question: 11 | **N/A** |
| `6.5.7` | Decidability: GATE CSE 1996 \| Question: 1.9 | **D** |
| `6.5.8` | Decidability: GATE CSE 1997 \| Question: 6.5 | **B** |
| `6.5.9` | Decidability: GATE CSE 1999 \| Question: 10 | **N/A** |
| `6.5.10` | Decidability: GATE CSE 2000 \| Question: 2.9 | **A** |
| `6.5.11` | Decidability: GATE CSE 2001 \| Question: 2.7 | **B** |
| `6.5.12` | Decidability: GATE CSE 2001 \| Question: 7 | **N/A** |
| `6.5.13` | Decidability: GATE CSE 2002 \| Question: 14 | **N/A** |
| `6.5.14` | Decidability: GATE CSE 2003 \| Question: 52 | **C** |
| `6.5.15` | Decidability: GATE CSE 2003 \| Question: 53 | **A** |
| `6.5.16` | Decidability: GATE CSE 2007 \| Question: 6 | **B** |
| `6.5.17` | Decidability: GATE CSE 2008 \| Question: 10 | **B** |
| `6.5.18` | Decidability: GATE CSE 2012 \| Question: 24 | **D** |
| `6.5.19` | Decidability: GATE CSE 2013 \| Question: 41 | **D** |
| `6.5.20` | Decidability: GATE CSE 2014 \| Set 3 \| Question: 35 | **A** |
| `6.5.21` | Decidability: GATE CSE 2015 \| Set 2 \| Question: 21 | **D** |
| `6.5.22` | Decidability: GATE CSE 2015 \| Set 3 \| Question: 53 | **C** |
| `6.5.23` | Decidability: GATE CSE 2016 \| Set 1 \| Question: 17 | **C** |
| `6.5.24` | Decidability: GATE CSE 2017 \| Set 1 \| Question: 39 | **A** |
| `6.5.25` | Decidability: GATE CSE 2017 \| Set 2 \| Question: 41 | **D** |
| `6.5.26` | Decidability: GATE CSE 2018 \| Question: 36 | **D** |
| `6.5.27` | Decidability: GATE CSE 2020 \| Question: 26 | **A** |
| `6.5.28` | Decidability: GATE CSE 2021 \| Set 2 \| Question: 36 | **C** |
| `6.5.29` | Decidability: GATE CSE 2022 \| Question: 36 | **A;B;C** |
| `6.5.30` | Decidability: GATE CSE 2025 \| Set 2 \| Question: 15 | **D** |
| `6.6.1` | Dpda: GATE CSE 2025 \| Set 2 \| Question: 14 | **A** |
| `6.7.1` | Finite Automata: GATE CSE 1988 \| Question: 15 | **N/A** |
| `6.7.2` | Finite Automata: GATE CSE 1991 \| Question: 17,b | **N/A** |
| `6.7.3` | Finite Automata: GATE CSE 1993 \| Question: 27 | **N/A** |
| `6.7.4` | Finite Automata: GATE CSE 1996 \| Question: 12 | **N/A** |
| `6.7.5` | Finite Automata: GATE CSE 1997 \| Question: 21 | **N/A** |
| `6.7.6` | Finite Automata: GATE CSE 1998 \| Question: 1.10 | **A** |
| `6.7.7` | Finite Automata: GATE CSE 2001 \| Question: 5 | **N/A** |
| `6.7.8` | Finite Automata: GATE CSE 2002 \| Question: 2.5 | **A** |
| `6.7.9` | Finite Automata: GATE CSE 2002 \| Question: 21 | **N/A** |
| `6.7.10` | Finite Automata: GATE CSE 2003 \| Question: 50 | **C** |
| `6.7.11` | Finite Automata: GATE CSE 2003 \| Question: 55 | **B** |
| `6.7.12` | Finite Automata: GATE CSE 2004 \| Question: 86 | **A** |
| `6.7.13` | Finite Automata: GATE CSE 2005 \| Question: 53 | **X** |
| `6.7.14` | Finite Automata: GATE CSE 2005 \| Question: 63 | **B** |
| `6.7.15` | Finite Automata: GATE CSE 2007 \| Question: 74 | **C** |
| `6.7.16` | Finite Automata: GATE CSE 2008 \| Question: 49 | **A** |
| `6.7.17` | Finite Automata: GATE CSE 2008 \| Question: 52 | **C** |
| `6.7.18` | Finite Automata: GATE CSE 2009 \| Question: 41 | **C** |
| `6.7.19` | Finite Automata: GATE CSE 2012 \| Question: 12 | **B** |
| `6.7.20` | Finite Automata: GATE CSE 2012 \| Question: 46 | **D** |
| `6.7.21` | Finite Automata: GATE CSE 2013 \| Question: 33 | **D** |
| `6.7.22` | Finite Automata: GATE CSE 2014 \| Set 1 \| Question: 16 | **A** |
| `6.7.23` | Finite Automata: GATE CSE 2016 \| Set 2 \| Question: 42 | **B** |
| `6.7.24` | Finite Automata: GATE CSE 2017 \| Set 2 \| Question: 39 | **C** |
| `6.7.25` | Finite Automata: GATE CSE 2021 \| Set 1 \| Question: 38 | **D** |
| `6.7.26` | Finite Automata: GATE CSE 2021 \| Set 2 \| Question: 17 | **256** |
| `6.7.27` | Finite Automata: GATE CSE 2021 \| Set 2 \| Question: 28 | **B** |
| `6.7.28` | Finite Automata: GATE CSE 2024 \| Set 1 \| Question: 40 | **B;C** |
| `6.7.29` | Finite Automata: GATE CSE 2024 \| Set 2 \| Question: 12 | **A** |
| `6.7.30` | Finite Automata: GATE CSE 2024 \| Set 2 \| Question: 31 | **B** |
| `6.7.31` | Finite Automata: GATE CSE 2025 \| Set 1 \| Question: 40 | **C** |
| `6.7.32` | Finite Automata: GATE CSE 2026 \| Set 2 \| Question: 37 | **C;D** |
| `6.7.33` | Finite Automata: GATE IT 2004 \| Question: 41 | **B** |
| `6.7.34` | Finite Automata: GATE IT 2005 \| Question: 37 | **A** |
| `6.7.35` | Finite Automata: GATE IT 2005 \| Question: 39 | **B** |
| `6.7.36` | Finite Automata: GATE IT 2006 \| Question: 3 | **D** |
| `6.7.37` | Finite Automata: GATE IT 2006 \| Question: 37 | **A** |
| `6.7.38` | Finite Automata: GATE IT 2007 \| Question: 47 | **D** |
| `6.7.39` | Finite Automata: GATE IT 2007 \| Question: 50 | **A** |
| `6.7.40` | Finite Automata: GATE IT 2007 \| Question: 71 | **A** |
| `6.7.41` | Finite Automata: GATE IT 2007 \| Question: 72 | **A** |
| `6.7.42` | Finite Automata: GATE IT 2008 \| Question: 32 | **A** |
| `6.7.43` | Finite Automata: GATE IT 2008 \| Question: 36 | **X** |
| `6.8.1` | Finite State Machines: GATE CSE 2025 \| Set 1 \| Question: 49 | **5:5** |
| `6.9.1` | Identify Class Language: GATE CSE 1987 \| Question: 1-xiii | **C** |
| `6.9.2` | Identify Class Language: GATE CSE 1988 \| Question: 2ix | **N/A** |
| `6.9.3` | Identify Class Language: GATE CSE 1991 \| Question: 17,a | **N/A** |
| `6.9.4` | Identify Class Language: GATE CSE 1994 \| Question: 19 | **N/A** |
| `6.9.5` | Identify Class Language: GATE CSE 1999 \| Question: 2.4 | **A;C** |
| `6.9.6` | Identify Class Language: GATE CSE 2000 \| Question: 1.5 | **B** |
| `6.9.7` | Identify Class Language: GATE CSE 2002 \| Question: 1.7 | **B** |
| `6.9.8` | Identify Class Language: GATE CSE 2004 \| Question: 87 | **B** |
| `6.9.9` | Identify Class Language: GATE CSE 2005 \| Question: 55 | **A** |
| `6.9.10` | Identify Class Language: GATE CSE 2006 \| Question: 30 | **D** |
| `6.9.11` | Identify Class Language: GATE CSE 2006 \| Question: 33 | **B** |
| `6.9.12` | Identify Class Language: GATE CSE 2007 \| Question: 30 | **B** |
| `6.9.13` | Match the following: | **C** |
| `6.9.14` | Identify Class Language: GATE CSE 2008 \| Question: 9 | **D** |
| `6.9.15` | Identify Class Language: GATE CSE 2009 \| Question: 40 | **C** |
| `6.9.16` | Identify Class Language: GATE CSE 2010 \| Question: 40 | **D** |
| `6.9.17` | Identify Class Language: GATE CSE 2011 \| Question: 26 | **C** |
| `6.9.18` | Identify Class Language: GATE CSE 2013 \| Question: 32 | **D** |
| `6.9.19` | Identify Class Language: GATE CSE 2014 \| Set 3 \| Question: 36 | **C** |
| `6.9.20` | Identify Class Language: GATE CSE 2017 \| Set 1 \| Question: 37 | **B** |
| `6.9.21` | Identify Class Language: GATE CSE 2017 \| Set 2 \| Question: 40 | **D** |
| `6.9.22` | Identify Class Language: GATE CSE 2018 \| Question: 35 | **B** |
| `6.9.23` | Identify Class Language: GATE CSE 2020 \| Question: 10 | **C** |
| `6.9.24` | Identify Class Language: GATE CSE 2020 \| Question: 32 | **A** |
| `6.9.25` | Identify Class Language: GATE CSE 2021 \| Set 2 \| Question: 12 | **B;C;D** |
| `6.9.26` | Identify Class Language: GATE CSE 2022 \| Question: 13 | **B;C;D** |
| `6.9.27` | Identify Class Language: GATE CSE 2022 \| Question: 37 | **A;B;C** |
| `6.9.28` | Identify Class Language: GATE CSE 2023 \| Question: 14 | **A;C;D** |
| `6.9.29` | Identify Class Language: GATE IT 2005 \| Question: 4 | **D** |
| `6.9.30` | Identify Class Language: GATE IT 2005 \| Question: 6 | **A** |
| `6.9.31` | Identify Class Language: GATE IT 2008 \| Question: 33 | **B** |
| `6.10.1` | Medium: GATE CSE 2006 \| Question: 29 | **C** |
| `6.11.1` | Minimal State Automata: GATE CSE 1987 \| Question: 2j | **0** |
| `6.11.2` | Minimal State Automata: GATE CSE 1997 \| Question: 20 | **N/A** |
| `6.11.3` | Minimal State Automata: GATE CSE 1997 \| Question: 70 | **N/A** |
| `6.11.4` | Minimal State Automata: GATE CSE 1998 \| Question: 2.5 | **B** |
| `6.11.5` | Minimal State Automata: GATE CSE 1998 \| Question: 4 | **N/A** |
| `6.11.6` | Minimal State Automata: GATE CSE 1999 \| Question: 1.4 | **B** |
| `6.11.7` | Minimal State Automata: GATE CSE 2001 \| Question: 1.6 | **B** |
| `6.11.8` | Minimal State Automata: GATE CSE 2001 \| Question: 2.5 | **D** |
| `6.11.9` | Minimal State Automata: GATE CSE 2002 \| Question: 2.13 | **B** |
| `6.11.10` | Minimal State Automata: GATE CSE 2006 \| Question: 34 | **D** |
| `6.11.11` | Minimal State Automata: GATE CSE 2007 \| Question: 29 | **A** |
| `6.11.12` | Minimal State Automata: GATE CSE 2007 \| Question: 75 | **B** |
| `6.11.13` | Minimal State Automata: GATE CSE 2010 \| Question: 41 | **C** |
| `6.11.14` | Minimal State Automata: GATE CSE 2011 \| Question: 42 | **B** |
| `6.11.15` | Minimal State Automata: GATE CSE 2011 \| Question: 45 | **A** |
| `6.11.16` | Minimal State Automata: GATE CSE 2015 \| Set 1 \| Question: 52 | **1** |
| `6.11.17` | Minimal State Automata: GATE CSE 2015 \| Set 2 \| Question: 53 | **3** |
| `6.11.18` | Minimal State Automata: GATE CSE 2015 \| Set 3 \| Question: 18 | **B** |
| `6.11.19` | Minimal State Automata: GATE CSE 2016 \| Set 2 \| Question: 16 | **2** |
| `6.11.20` | Minimal State Automata: GATE CSE 2017 \| Set 1 \| Question: 22 | **4** |
| `6.11.21` | Minimal State Automata: GATE CSE 2017 \| Set 2 \| Question: 25 | **8** |
| `6.11.22` | Minimal State Automata: GATE CSE 2018 \| Question: 6 | **D** |
| `6.11.23` | Minimal State Automata: GATE CSE 2019 \| Question: 48 | **120** |
| `6.11.24` | Minimal State Automata: GATE CSE 2023 \| Question: 53 | **4** |
| `6.11.25` | Minimal State Automata: GATE IT 2008 \| Question: 6 | **A** |
| `6.12.1` | Non Determinism: GATE CSE 1992 \| Question: 02,xx | **A;C** |
| `6.12.2` | Non Determinism: GATE CSE 1994 \| Question: 1.16 | **C** |
| `6.12.3` | Non Determinism: GATE CSE 1998 \| Question: 1.11 | **B** |
| `6.12.4` | Non Determinism: GATE CSE 2005 \| Question: 54 | **D** |
| `6.12.5` | Non Determinism: GATE CSE 2011 \| Question: 8 | **B** |
| `6.12.6` | Non Determinism: GATE IT 2004 \| Question: 9 | **C** |
| `6.13.1` | Number of States: GATE CSE 2025 \| Set 2 \| Question: 50 | **6:6** |
| `6.13.2` | Number of States: GATE CSE 2026 \| Set 1 \| Question: 16 | **B;D** |
| `6.14.1` | Pumping Lemma: GATE CSE 2019 \| Question: 15 | **D** |
| `6.14.2` | Pumping Lemma: GATE IT 2005 \| Question: 40 | **D** |
| `6.15.1` | Pushdown Automata: GATE CSE 1996 \| Question: 13 | **N/A** |
| `6.15.2` | Pushdown Automata: GATE CSE 1997 \| Question: 6.6 | **A** |
| `6.15.3` | Pushdown Automata: GATE CSE 1998 \| Question: 13 | **N/A** |
| `6.15.4` | Pushdown Automata: GATE CSE 1999 \| Question: 1.6 | **A** |
| `6.15.5` | Pushdown Automata: GATE CSE 2000 \| Question: 8 | **N/A** |
| `6.15.6` | Pushdown Automata: GATE CSE 2001 \| Question: 6 | **N/A** |
| `6.15.7` | Pushdown Automata: GATE CSE 2009 \| Question: 16, ISRO2017-12 | **D** |
| `6.15.8` | Pushdown Automata: GATE CSE 2015 \| Set 1 \| Question: 51 | **B** |
| `6.15.9` | Pushdown Automata: GATE CSE 2016 \| Set 1 \| Question: 43 | **D** |
| `6.15.10` | Pushdown Automata: GATE CSE 2021 \| Set 1 \| Question: 51 | **50** |
| `6.15.11` | Pushdown Automata: GATE CSE 2023 \| Question: 30 | **A** |
| `6.15.12` | Pushdown Automata: GATE IT 2004 \| Question: 40 | **B** |
| `6.15.13` | Pushdown Automata: GATE IT 2005 \| Question: 38 | **D** |
| `6.15.14` | Pushdown Automata: GATE IT 2006 \| Question: 31 | **B** |
| `6.15.15` | Pushdown Automata: GATE IT 2006 \| Question: 33 | **C** |
| `6.16.1` | Recursive and Recursively Enumerable Languages: GATE CSE 1990 \| Question: 3-vi | **A;D** |
| `6.16.2` | Recursive and Recursively Enumerable Languages: GATE CSE 2003 \| Question: 13 | **A** |
| `6.16.3` | Recursive and Recursively Enumerable Languages: GATE CSE 2003 \| Question: 15 | **D** |
| `6.16.4` | Recursive and Recursively Enumerable Languages: GATE CSE 2003 \| Question: 54 | **D** |
| `6.16.5` | Recursive and Recursively Enumerable Languages: GATE CSE 2004 \| Question: 89 | **A** |
| `6.16.6` | Recursive and Recursively Enumerable Languages: GATE CSE 2005 \| Question: 56 | **B** |
| `6.16.7` | Recursive and Recursively Enumerable Languages: GATE CSE 2008 \| Question: 13, ISRO2016-36 | **D** |
| `6.16.8` | Recursive and Recursively Enumerable Languages: GATE CSE 2008 \| Question: 48 | **D** |
| `6.16.9` | Recursive and Recursively Enumerable Languages: GATE CSE 2010 \| Question: 17 | **B** |
| `6.16.10` | Recursive and Recursively Enumerable Languages: GATE CSE 2014 \| Set 1 \| Question: 35 | **C** |
| `6.16.11` | Recursive and Recursively Enumerable Languages: GATE CSE 2014 \| Set 2 \| Question: 16 | **D** |
| `6.16.12` | Recursive and Recursively Enumerable Languages: GATE CSE 2014 \| Set 2 \| Question: 35 | **B** |
| `6.16.13` | Recursive and Recursively Enumerable Languages: GATE CSE 2015 \| Set 1 \| Question: 3 | **D** |
| `6.16.14` | Recursive and Recursively Enumerable Languages: GATE CSE 2016 \| Set 2 \| Question: 44 | **C** |
| `6.16.15` | Recursive and Recursively Enumerable Languages: GATE CSE 2021 \| Set 1 \| Question: 12 | **D** |
| `6.16.16` | Recursive and Recursively Enumerable Languages: GATE CSE 2021 \| Set 1 \| Question: 39 | **A** |
| `6.17.1` | Reduction: GATE CSE 2005 \| Question: 45 | **C** |
| `6.17.2` | Reduction: GATE CSE 2016 \| Set 1 \| Question: 44 | **C** |
| `6.18.1` | Regular Expression: GATE CSE 1987 \| Question: 10d | **N/A** |
| `6.18.2` | Regular Expression: GATE CSE 1991 \| Question: 03,xiii | **A;C** |
| `6.18.3` | Regular Expression: GATE CSE 1992 \| Question: 02,xvii | **A** |
| `6.18.4` | Regular Expression: GATE CSE 1994 \| Question: 2.10 | **N/A** |
| `6.18.5` | Regular Expression: GATE CSE 1995 \| Question: 1.9 , ISRO2017-13 | **C** |
| `6.18.6` | Regular Expression: GATE CSE 1996 \| Question: 1.8 | **C** |
| `6.18.7` | Regular Expression: GATE CSE 1997 \| Question: 6.4 | **D** |
| `6.18.8` | Regular Expression: GATE CSE 1998 \| Question: 1.12 | **C;D** |
| `6.18.9` | Regular Expression: GATE CSE 1998 \| Question: 1.9 | **D** |
| `6.18.10` | Regular Expression: GATE CSE 1998 \| Question: 3b | **N/A** |
| `6.18.11` | Regular Expression: GATE CSE 2000 \| Question: 1.4 | **C** |
| `6.18.12` | Regular Expression: GATE CSE 2003 \| Question: 14 | **A** |
| `6.18.13` | Regular Expression: GATE CSE 2009 \| Question: 15 | **C** |
| `6.18.14` | Regular Expression: GATE CSE 2010 \| Question: 39 | **B** |
| `6.18.15` | Regular Expression: GATE CSE 2014 \| Set 1 \| Question: 36 | **B** |
| `6.18.16` | Regular Expression: GATE CSE 2014 \| Set 3 \| Question: 15 | **3** |
| `6.18.17` | Regular Expression: GATE CSE 2016 \| Set 1 \| Question: 18 | **B** |
| `6.18.18` | Regular Expression: GATE CSE 2020 \| Question: 7 | **X** |
| `6.18.19` | Regular Expression: GATE CSE 2021 \| Set 2 \| Question: 47 | **A;B;C** |
| `6.18.20` | Regular Expression: GATE CSE 2022 \| Question: 2 | **D** |
| `6.18.21` | Regular Expression: GATE CSE 2023 \| Question: 4 | **C** |
| `6.18.22` | Regular Expression: GATE CSE 2023 \| Question: 9 | **C** |
| `6.18.23` | Regular Expression: GATE CSE 2024 \| Set 1 \| Question: 51 | **44** |
| `6.18.24` | Regular Expression: GATE CSE 2024 \| Set 2 \| Question: 52 | **15** |
| `6.18.25` | Regular Expression: GATE IT 2004 \| Question: 7 | **C** |
| `6.18.26` | Regular Expression: GATE IT 2005 \| Question: 5 | **B** |
| `6.18.27` | Regular Expression: GATE IT 2006 \| Question: 5 | **A** |
| `6.18.28` | Regular Expression: GATE IT 2007 \| Question: 73 | **C** |
| `6.18.29` | Regular Expression: GATE IT 2008 \| Question: 5 | **C** |
| `6.19.1` | Regular Grammar: GATE CSE 1990 \| Question: 15a | **N/A** |
| `6.19.2` | Regular Grammar: GATE CSE 2015 \| Set 2 \| Question: 35 | **C** |
| `6.19.3` | Regular Grammar: GATE IT 2006 \| Question: 29 | **A** |
| `6.20.1` | Regular Language: GATE CSE 1987 \| Question: 2h | **True** |
| `6.20.2` | Regular Language: GATE CSE 1987 \| Question: 2i | **False** |
| `6.20.3` | Regular Language: GATE CSE 1990 \| Question: 3-viii | **B;C** |
| `6.20.4` | Regular Language: GATE CSE 1991 \| Question: 03,xiv | **D** |
| `6.20.5` | Regular Language: GATE CSE 1995 \| Question: 2.24 | **C** |
| `6.20.6` | Regular Language: GATE CSE 1996 \| Question: 1.10 | **D** |
| `6.20.7` | Regular Language: GATE CSE 1998 \| Question: 2.6 | **B** |
| `6.20.8` | Regular Language: GATE CSE 1999 \| Question: 6 | **N/A** |
| `6.20.9` | Regular Language: GATE CSE 2000 \| Question: 2.8 | **X** |
| `6.20.10` | Regular Language: GATE CSE 2001 \| Question: 1.4 | **A** |
| `6.20.11` | Regular Language: GATE CSE 2001 \| Question: 2.6 | **D** |
| `6.20.12` | Regular Language: GATE CSE 2007 \| Question: 31 | **C** |
| `6.20.13` | Regular Language: GATE CSE 2007 \| Question: 7 | **B** |
| `6.20.14` | Regular Language: GATE CSE 2008 \| Question: 53 | **A** |
| `6.20.15` | Regular Language: GATE CSE 2011 \| Question: 24 | **C** |
| `6.20.16` | Regular Language: GATE CSE 2012 \| Question: 25 | **C** |
| `6.20.17` | Regular Language: GATE CSE 2013 \| Question: 8 | **A** |
| `6.20.18` | Regular Language: GATE CSE 2014 \| Set 1 \| Question: 15 | **C** |
| `6.20.19` | Regular Language: GATE CSE 2014 \| Set 2 \| Question: 15 | **A** |
| `6.20.20` | Regular Language: GATE CSE 2014 \| Set 2 \| Question: 36 | **A** |
| `6.20.21` | Regular Language: GATE CSE 2015 \| Set 2 \| Question: 51 | **A** |
| `6.20.22` | Regular Language: GATE CSE 2016 \| Set 2 \| Question: 17 | **C** |
| `6.20.23` | Regular Language: GATE CSE 2018 \| Question: 52 | **2** |
| `6.20.24` | Regular Language: GATE CSE 2019 \| Question: 7 | **B** |
| `6.20.25` | Regular Language: GATE CSE 2020 \| Question: 51 | **6** |
| `6.20.26` | Regular Language: GATE CSE 2020 \| Question: 8 | **D** |
| `6.20.27` | Regular Language: GATE CSE 2021 \| Set 2 \| Question: 9 | **C** |
| `6.20.28` | Regular Language: GATE CSE 2024 \| Set 1 \| Question: 13 | **C;D** |
| `6.20.29` | Regular Language: GATE CSE 2025 \| Set 1 \| Question: 18 | **D** |
| `6.20.30` | Regular Language: GATE CSE 2025 \| Set 1 \| Question: 34 | **C** |
| `6.20.31` | Regular Language: GATE CSE 2025 \| Set 2 \| Question: 42 | **A;C** |
| `6.20.32` | Regular Language: GATE IT 2006 \| Question: 30 | **C** |
| `6.20.33` | Regular Language: GATE IT 2006 \| Question: 80 | **B** |
| `6.20.34` | Regular Language: GATE IT 2006 \| Question: 81 | **A** |
| `6.20.35` | Regular Language: GATE IT 2008 \| Question: 35 | **D** |
| `6.21.1` | Turing Machine: GATE CSE 2026 \| Set 2 \| Question: 3 | **D** |

