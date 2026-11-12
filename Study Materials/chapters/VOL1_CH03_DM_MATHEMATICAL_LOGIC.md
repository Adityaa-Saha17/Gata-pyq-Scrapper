# Volume 1 — Chapter 3: Discrete Mathematics: Mathematical Logic

- **Source PDF**: [filter1_volume1.pdf](file:///Users/adityaasaha/Documents/Academics/Gate/filter1_volume1.pdf)
- **Total GATE Questions in Chapter**: **78**

---

## 1. Subtopic Weightage & Question Distribution

| Subtopic # | Subtopic Name | Questions |
| :---: | :--- | :---: |
| **3.1** | First Order Logic | 35 |
| **3.3** | Propositional Logic | 40 |


---

## 2. Comprehensive GATE CSE Mathematical Logic Reference (Expanded Research & Formulas)

### 2.1 Propositional Logic Connectives & Equivalences
- **Implication ($p \rightarrow q$)**: False **only** when $p = \text{True}$ and $q = \text{False}$.
  $$p \rightarrow q \equiv \neg p \lor q \equiv \neg q \rightarrow \neg p \quad \text{(Contrapositive)}$$
  - Negation of implication: $\neg(p \rightarrow q) \equiv p \land \neg q$.
- **Biconditional ($p \leftrightarrow q$ / XNOR)**:
  $$p \leftrightarrow q \equiv (p \rightarrow q) \land (q \rightarrow p) \equiv (p \land q) \lor (\neg p \land \neg q) \equiv \neg(p \oplus q)$$
- **Key Equivalences**:
  - **Distributive**: $p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$, $p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$
  - **Absorption**: $p \lor (p \land q) \equiv p$, $p \land (p \lor q) \equiv p$
  - **Exportation**: $p \rightarrow (q \rightarrow r) \equiv (p \land q) \rightarrow r$
  - **Implication Distribution**: $p \rightarrow (q \lor r) \equiv (p \rightarrow q) \lor (p \rightarrow r)$, $p \rightarrow (q \land r) \equiv (p \rightarrow q) \land (p \rightarrow r)$
  - **Disjunctive Antecedent**: $(p \lor q) \rightarrow r \equiv (p \rightarrow r) \land (q \rightarrow r)$
  - **Conjunctive Antecedent**: $(p \land q) \rightarrow r \equiv (p \rightarrow r) \lor (q \rightarrow r)$
- **Number of Truth Tables / Boolean Functions on $n$ Variables**: $2^{2^n}$.

### 2.2 Rules of Inference (Valid Arguments)
An argument $(P_1, P_2, \dots, P_k) \therefore C$ is **valid** iff $(P_1 \land P_2 \land \dots \land P_k) \rightarrow C$ is a **tautology**.
- **Modus Ponens**: $p, \; p \rightarrow q \vdash q$
- **Modus Tollens**: $\neg q, \; p \rightarrow q \vdash \neg p$
- **Hypothetical Syllogism**: $p \rightarrow q, \; q \rightarrow r \vdash p \rightarrow r$
- **Disjunctive Syllogism**: $p \lor q, \; \neg p \vdash q$
- **Resolution**: $p \lor q, \; \neg p \lor r \vdash q \lor r$
- *Common Fallacies (Invalid!)*:
  - Affirming the Consequent: $p \rightarrow q, \; q \not\vdash p$
  - Denying the Antecedent: $p \rightarrow q, \; \neg p \not\vdash \neg q$

### 2.3 First-Order (Predicate) Logic & Quantifier Laws
- **Standard Translation Idioms**:
  - "Every $A$ is $B$": $\forall x \big(A(x) \rightarrow B(x)\big)$ *(NEVER $\forall x (A(x) \land B(x))$!)*
  - "Some $A$ is $B$": $\exists x \big(A(x) \land B(x)\big)$ *(NEVER $\exists x (A(x) \rightarrow B(x))$!)*
- **De Morgan's Laws for Quantifiers**:
  $$\neg \forall x \, P(x) \equiv \exists x \, \neg P(x), \qquad \neg \exists x \, P(x) \equiv \forall x \, \neg P(x)$$
- **Quantifier Distribution Laws (Crucial for GATE!)**:
  1. $\forall$ distributes over **$\land$**: $\forall x (P(x) \land Q(x)) \equiv \forall x P(x) \land \forall x Q(x)$
  2. $\exists$ distributes over **$\lor$**: $\exists x (P(x) \lor Q(x)) \equiv \exists x P(x) \lor \exists x Q(x)$
  3. **One-Way Implications Only**:
     - $\forall x P(x) \lor \forall x Q(x) \implies \forall x (P(x) \lor Q(x))$ *(converse is FALSE!)*
     - $\exists x (P(x) \land Q(x)) \implies \exists x P(x) \land \exists x Q(x)$ *(converse is FALSE!)*
- **Nested Quantifier Order**:
  - $\forall x \forall y P(x, y) \equiv \forall y \forall x P(x, y)$
  - $\exists x \exists y P(x, y) \equiv \exists y \exists x P(x, y)$
  - $\exists x \forall y P(x, y) \implies \forall y \exists x P(x, y)$ *(converse is FALSE!)*

---

## 3. Original PDF Chapter Notes (Preserved Verbatim)

3 Discrete Mathematics: Mathematical Logic (78)
Syllabus: Propositional and first order logic.
Welcome to the "Discrete Mathematics: Mathematical Logic" chapter of your GATE Computer Science exam
preparation. This section is designed to provide a comprehensive, exam-focused overview of the fundamental concepts,
formulas, and problem-solving techniques you'll need to master. Mathematical Logic is the bedrock of computer
science, providing the formal tools to reason about computation, verify program correctness, design circuits, and
understand artificial intelligence. For the GATE CS exam, this subject typically carries a weightage of 5-8 marks.
Questions often involve determining the validity of arguments, checking logical equivalence, translating natural
language statements into logical expressions, and identifying tautologies or contradictions. A strong grasp of these
concepts is indispensable not just for direct questions but also for understanding the logical underpinnings of other
topics like set theory, relations, and algorithms.
Topic-wise Key Concepts
Propositional Logic
Propositional Logic, also known as propositional calculus, is the study of propositions (declarative sentences that are
either true or false, but not both) and their combinations using logical connectives. It forms the most basic level of
logical reasoning, focusing on the truth values of simple statements and how they combine to determine the truth values
of complex statements.
Definition and Core Idea: A proposition is a statement that is unequivocally true or false. Propositional logic uses
symbols to represent propositions and logical connectives to form compound propositions, allowing us to analyze
their truth values systematically.
Important Formulas, Theorems, and Results:
1. Logical Connectives:
Negation (NOT): (read as "not p")
Conjunction (AND): (read as "p and q")
Disjunction (OR): (read as "p or q")
Implication (IF...THEN): (read as "if p then q" or "p implies q")
Biconditional (IF AND ONLY IF): (read as "p if and only if q")
Exclusive OR (XOR): (read as "p xor q")
NAND:
NOR:
2. Truth Tables: Essential for defining connectives and evaluating compound propositions.
: T if p is F, F if p is T.
: T if both p and q are T, else F.
: T if p is T or q is T (or both), else F.
: F only if p is T and q is F, else T.
: T if p and q have the same truth value, else F.
: T if p and q have different truth values, else F.
3. Tautology, Contradiction, Contingency:
Tautology: A compound proposition that is always true, regardless of the truth values of its atomic
propositions. Example: .
Contradiction (or Absurdity): A compound proposition that is always false. Example: .
Contingency: A compound proposition that is neither a tautology nor a contradiction (i.e., its truth value
depends on the truth values of its atomic propositions).
4. Logical Equivalence ( ): Two propositions and are logically equivalent if is a tautology. This
means they always have the same truth value.
5. Laws of Logic (Logical Equivalences):
Identity Laws:

*(PDF Page 58)*

Domination Laws:
Idempotent Laws:
Double Negation Law:
Commutative Laws:
Associative Laws:
Distributive Laws:
De Morgan's Laws:
Absorption Laws:
Inverse Laws (Complement Laws):
Implication Equivalences:
Biconditional Equivalences:
(Contrapositive)
6. Conjunctive Normal Form (CNF) and Disjunctive Normal Form (DNF):
Literal: A propositional variable or its negation (e.g., ).
Clause: A disjunction of literals (e.g., ).
CNF: A conjunction of clauses (e.g., ).
Minterm: A conjunction of literals where each variable appears exactly once (e.g., Maxterm: A disjunction of literals where each variable appears exactly once (e.g., ).
).
DNF: A disjunction of minterms (e.g., ).
Any propositional formula can be converted into an equivalent CNF or DNF.
Key Properties and Identities: All the laws of logic listed above are crucial identities for simplification and proving
equivalence. Understanding the truth conditions for each connective is fundamental.
Common Pitfalls or Tricky Points:
Confusing implication ( ) with causation or "if and only if"
. Remember is false only when is true
and is false.
Incorrectly applying De Morgan's Laws, especially with more complex expressions.
Misinterpreting the biconditional; it implies mutual implication.
Errors in constructing truth tables, particularly for propositions with many variables.
Assuming logical equivalence based on partial truth values.
Standard Problem-Solving Techniques or Shortcuts:
Truth Tables: The most direct method for small propositions to check tautology, contradiction, or equivalence.
Logical Equivalences: Use the laws of logic to simplify expressions or prove equivalence without truth tables.
This is often faster for complex expressions.
Substitution: Replace sub-expressions with their known equivalents.
Proof by Contradiction: To show is a tautology, assume is true and derive a contradiction. To show
, assume is true and derive a contradiction.
Conversion to CNF/DNF: Useful for standardization and for certain proof methods like resolution.

*(PDF Page 59)*

First Order Logic (Predicate Logic)
First Order Logic (FOL), also known as Predicate Logic, extends propositional logic by allowing us to express more
complex statements about objects, their properties, and relationships. It introduces predicates, variables, and
quantifiers, enabling reasoning about "all" or "some" elements within a domain.
Definition and Core Idea: FOL allows us to break down propositions into predicates (properties or relations) and
arguments (variables or constants). It introduces quantifiers ( for "for all" and for "there exists") to make
statements about collections of objects, providing a richer expressive power than propositional logic.
Important Formulas, Theorems, and Results:
1. Components of FOL:
Predicates: Represent properties or relations (e.g., for "x is prime"
, for "x loves y").
Variables: Placeholders for objects (e.g., Constants: Specific objects (e.g.,
"Socrates"
,
).
"5").
Functions: Map objects to other objects (e.g., for "father of x").
Quantifiers:
Universal Quantifier ( ): "For all"
,
"for every"
,
"for each"
. means is true for every in the
domain.
Existential Quantifier ( ): "There exists"
,
"for some"
,
"for at least one"
. means there is at least
one in the domain for which is true.
2. Scope of Quantifiers, Free and Bound Variables:
The scope of a quantifier is the part of the formula to which it applies.
A variable is bound if it is within the scope of a quantifier using that variable.
A variable is free if it is not bound by any quantifier.
A formula with no free variables is called a sentence or closed formula and has a definite truth value.
3. Quantifier Equivalences (Negation Rules):
(It is not true that all x have property P if and only if there exists an x that does not
have property P).
(It is not true that there exists an x with property P if and only if all x do not have
property P).
4. Distributive Properties of Quantifiers:
Important Non-Equivalences:
is NOT equivalent to . (e.g.,
"Every number is even or odd" is true,
but "Every number is even or every number is odd" is false).
is NOT equivalent to . (e.g.,
"There is a number that is both even
and prime" (2) is true, but "There is an even number and there is a prime number" is also true, but the
existence of one doesn't imply the other is the same number).
5. Interchange of Quantifiers:
Order Matters for Mixed Quantifiers:
(For every x, there exists a y such that P(x,y)) is NOT equivalent to (There
exists a y such that for every x, P(x,y)).
Example: Let be "x loves y"
. means "Everyone loves someone"
.
means "There is someone whom everyone loves"
. These are clearly different.
6. Prenex Normal Form (PNF): A formula is in PNF if all quantifiers are at the beginning of the formula, followed
by a quantifier-free formula (called the matrix). Any FOL formula can be converted to an equivalent PNF.
Key Properties and Identities: The quantifier negation rules are fundamental for manipulating and simplifying FOL
expressions. Understanding the implications of quantifier order is critical.
Common Pitfalls or Tricky Points:
Incorrect Translation: Translating natural language statements into FOL is a major source of errors. Pay close
attention to words like "all"
,
"some"
,
"no"
,
"only if"
,
"unless"
.
"All A are B": (NOT )
"Some A are B": (NOT )
"No A are B": or
Scope Errors: Misplacing parentheses or incorrectly determining the scope of a quantifier.
Variable Binding: Confusing free and bound variables, or using the same variable name for different purposes
in nested scopes.

*(PDF Page 60)*

Order of Mixed Quantifiers: Assuming is the same as .
Standard Problem-Solving Techniques or Shortcuts:
Step-by-step Translation: Break down complex natural language sentences into smaller parts, translate each,
and then combine them. Identify predicates, variables, and connectives first.
Applying Quantifier Equivalences: Use negation rules to simplify expressions or move negations inwards.
Domain Awareness: Always consider the domain of discourse when evaluating truth values or translating.
Counterexamples: To show a statement is false or not equivalent, try to find a specific example in a small
domain that makes it false.
Logical Reasoning (Inference)
Logical Reasoning, or Inference, is the process of deriving conclusions from a set of premises using valid rules. It
focuses on the structure of arguments to determine whether a conclusion necessarily follows from the premises,
regardless of the actual truth of the premises.
Definition and Core Idea: An argument is a sequence of propositions, where the first propositions are premises
and the final proposition is the conclusion. An argument is valid if, whenever all its premises are true, the conclusion
must also be true. The goal is to determine if an argument's structure guarantees the truth of its conclusion given
true premises.
Important Formulas, Theorems, and Results:
1. Argument Validity: An argument with premises and conclusion is valid if the proposition
is a tautology.
2. Rules of Inference (for Propositional Logic): These are fundamental valid argument forms.
Modus Ponens (Law of Detachment):
Equivalent to being a tautology.
Modus Tollens:
Equivalent to being a tautology.
Hypothetical Syllogism:
Equivalent to being a tautology.
Disjunctive Syllogism:
Equivalent to being a tautology.
Addition:
Simplification:

*(PDF Page 61)*

Conjunction:
Resolution:
This is particularly useful in automated theorem proving and for converting to CNF.
Constructive Dilemma:
Destructive Dilemma:
3. Rules of Inference (for First Order Logic):
Universal Instantiation (UI): If is true, then is true for any arbitrary individual in the domain.
Universal Generalization (UG): If true.
is true for an arbitrary individual in the domain, then is
Existential Instantiation (EI): If domain. This is true, then must be a new constant not previously used in the proof.
is true for some specific individual in the
Existential Generalization (EG): If true.
is true for some specific individual in the domain, then is
4. Proof Methods:
conclusion.
Direct Proof: Assume premises are true, and use inference rules and logical equivalences to derive the

*(PDF Page 62)*

Indirect Proof (Proof by Contradiction): To prove from premises , assume is true along
with , and derive a contradiction ( ).
Proof by Contraposition: To prove , prove its contrapositive .
Key Properties and Identities: The validity of each inference rule is a key property. Understanding that these rules
preserve truth is fundamental.
Common Pitfalls or Tricky Points:
Fallacies: Invalid argument forms that resemble valid ones.
Fallacy of Affirming the Consequent: (NOT a tautology). Example: "If it rains, the
ground is wet. The ground is wet. Therefore, it rained.
" (Could be wet from a sprinkler).
Fallacy of Denying the Antecedent: (NOT a tautology). Example: "If it rains, the
ground is wet. It did not rain. Therefore, the ground is not wet.
" (Could be wet from a sprinkler).
Confusing Validity with Soundness: A valid argument can have false premises and a false conclusion. A
sound argument is a valid argument with all true premises (and thus, a true conclusion). GATE questions
usually focus on validity.
Incorrect Application of Quantifier Rules: Especially with EI and UG, ensure the constant chosen for
instantiation is new (for EI) or truly arbitrary (for UG).
Circular Reasoning: Assuming the conclusion (or something equivalent to it) as a premise.
Standard Problem-Solving Techniques or Shortcuts:
Formal Proofs: List premises and then systematically apply inference rules and logical equivalences to derive
the conclusion, citing the rule for each step.
Truth Tables (for small arguments): Convert the argument into a single conditional statement
and check if it's a tautology.
Resolution Principle: Convert all premises and the negation of the conclusion into CNF clauses. Add the
negation of the conclusion as a clause. If an empty clause ( ) can be derived through resolution, the original
argument is valid.
Look for Fallacies: If an argument resembles a common fallacy, it's likely invalid.
Quick Formula Reference
Propositional Logic Equivalences
(Double Negation)
(Commutative)
(Commutative)
(Associative)
(Associative)
(Distributive)
(Distributive)
(De Morgan's)
(De Morgan's)
(Contrapositive)
(Inverse Law)
(Inverse Law)
(Domination Law)
(Domination Law)
(Identity Law)
(Identity Law)
(Idempotent Law)
(Idempotent Law)
(Absorption Law)
(Absorption Law)
Quantifier Equivalences

*(PDF Page 63)*

Rules of Inference (Propositional Logic)
Modus Ponens:
Modus Tollens:
Hypothetical Syllogism:
Disjunctive Syllogism:
Addition:
Simplification:
Conjunction:
Resolution:
Rules of Inference (First Order Logic)
Universal Instantiation (UI):
Universal Generalization (UG):
Existential Instantiation (EI):
Existential Generalization (EG):
Important Tips for GATE
1. Master Truth Tables: They are the foundation. Be able to quickly construct and interpret truth tables for any
compound proposition, especially for 2-3 variables. This helps in verifying tautologies, contradictions, and
equivalences.
2. Memorize Key Equivalences and Inference Rules: Speed and accuracy in GATE questions heavily rely on your
ability to recall and apply De Morgan's laws, implication equivalences, and the common rules of inference (Modus
Ponens, Modus Tollens, etc.) without hesitation.
3. Practice Natural Language Translation: A significant portion of GATE questions involves translating English
sentences into logical expressions (and vice-versa). Pay close attention to keywords like "all"
,
"some"
,
"no"
,
"only if"
,
"unless"
, and the correct use of quantifiers and connectives.
4. Understand Quantifier Scope and Order: Incorrectly interpreting the scope of quantifiers or swapping the order of
mixed quantifiers ( vs. ) is a very common mistake. Always visualize the domain and what each quantifier
implies.
5. Distinguish Validity from Soundness: GATE questions usually ask about the validity of an argument (whether the
conclusion logically follows from the premises), not its soundness (which also requires premises to be true in the
real world). Focus on the logical structure.
6. Systematic Approach to Proofs: When asked to prove an argument's validity, don't guess. Start with the premises
and systematically apply inference rules and logical equivalences, one step at a time, until you reach the conclusion.
Clearly state the rule used for each step.
7. Identify Common Fallacies: Be aware of fallacies like "Affirming the Consequent" and "Denying the Antecedent"
. If
an argument structure matches a known fallacy, you can quickly identify it as invalid.
8. Time Management: Some logical reasoning problems can be lengthy, especially those involving formal proofs or
complex translations. If a question seems too time-consuming, make an educated guess or mark it for review if time
permits, and move on to other questions.

---

## 4. Complete Question Index & Answer Key Record (78 Questions)

| Q # | Question Source / Title | Answer Key |
| :---: | :--- | :---: |
| `3.1.1` | First Order Logic: GATE CSE 1989 \| Question: 14a | **N/A** |
| `3.1.2` | First Order Logic: GATE CSE 1991 \| Question: 15,b | **N/A** |
| `3.1.3` | First Order Logic: GATE CSE 1992 \| Question: 92,xv | **A** |
| `3.1.4` | First Order Logic: GATE CSE 2003 \| Question: 32 | **D** |
| `3.1.5` | First Order Logic: GATE CSE 2003 \| Question: 33 | **D** |
| `3.1.6` | First Order Logic: GATE CSE 2004 \| Question: 23, ISRO2007-32 | **D** |
| `3.1.7` | First Order Logic: GATE CSE 2005 \| Question: 41 | **B** |
| `3.1.8` | First Order Logic: GATE CSE 2006 \| Question: 26 | **D** |
| `3.1.9` | Let denotes that statement: | **D** |
| `3.1.10` | First Order Logic: GATE CSE 2008 \| Question: 30 | **X** |
| `3.1.11` | First Order Logic: GATE CSE 2009 \| Question: 23 | **D** |
| `3.1.12` | First Order Logic: GATE CSE 2009 \| Question: 26 | **B** |
| `3.1.13` | First Order Logic: GATE CSE 2010 \| Question: 30 | **B** |
| `3.1.14` | First Order Logic: GATE CSE 2011 \| Question: 30 | **A** |
| `3.1.15` | First Order Logic: GATE CSE 2012 \| Question: 13 | **C** |
| `3.1.16` | First Order Logic: GATE CSE 2013 \| Question: 27 | **D** |
| `3.1.17` | First Order Logic: GATE CSE 2013 \| Question: 47 | **X** |
| `3.1.18` | Consider the statement | **D** |
| `3.1.19` | First Order Logic: GATE CSE 2014 \| Set 3 \| Question: 53 | **D** |
| `3.1.20` | First Order Logic: GATE CSE 2015 \| Set 2 \| Question: 55 | **C** |
| `3.1.21` | First Order Logic: GATE CSE 2016 \| Set 2 \| Question: 27 | **D** |
| `3.1.22` | First Order Logic: GATE CSE 2017 \| Set 1 \| Question: 02 | **B** |
| `3.1.23` | First Order Logic: GATE CSE 2018 \| Question: 28 | **A** |
| `3.1.24` | First Order Logic: GATE CSE 2019 \| Question: 35 | **C** |
| `3.1.25` | First Order Logic: GATE CSE 2020 \| Question: 39 | **C** |
| `3.1.26` | First Order Logic: GATE CSE 2023 \| Question: 16 | **B;C** |
| `3.1.27` | First Order Logic: GATE CSE 2025 \| Set 1 \| Question: 38 | **B;D** |
| `3.1.28` | First Order Logic: GATE CSE 2025 \| Set 2 \| Question: 5 | **A** |
| `3.1.29` | First Order Logic: GATE CSE 2026 \| Set 2 \| Question: 1 | **A** |
| `3.1.30` | First Order Logic: GATE IT 2004 \| Question: 3 | **C** |
| `3.1.31` | First Order Logic: GATE IT 2005 \| Question: 36 | **B** |
| `3.1.32` | First Order Logic: GATE IT 2006 \| Question: 21 | **B** |
| `3.1.33` | First Order Logic: GATE IT 2007 \| Question: 21 | **A** |
| `3.1.34` | First Order Logic: GATE IT 2008 \| Question: 21 | **C** |
| `3.1.35` | First Order Logic: GATE IT 2008 \| Question: 22 | **D** |
| `3.2.1` | Logical Reasoning: GATE CSE 2012 \| Question: 1 | **B** |
| `3.2.2` | Logical Reasoning: GATE CSE 2015 \| Set 2 \| Question: 3 | **C** |
| `3.2.3` | Logical Reasoning: GATE CSE 2015 \| Set 3 \| Question: 24 | **A** |
| `3.3.1` | Propositional Logic: GATE CSE 1987 \| Question: 10e | **N/A** |
| `3.3.2` | Propositional Logic: GATE CSE 1988 \| Question: 2vii | **N/A** |
| `3.3.3` | Propositional Logic: GATE CSE 1989 \| Question: 3-v | **A;B;C** |
| `3.3.4` | Propositional Logic: GATE CSE 1990 \| Question: 3-x | **A** |
| `3.3.5` | Propositional Logic: GATE CSE 1991 \| Question: 03,xii | **B** |
| `3.3.6` | Propositional Logic: GATE CSE 1992 \| Question: 02,xvi | **B** |
| `3.3.7` | Propositional Logic: GATE CSE 1992 \| Question: 15.a | **N/A** |
| `3.3.8` | Propositional Logic: GATE CSE 1993 \| Question: 18 | **N/A** |
| `3.3.9` | Propositional Logic: GATE CSE 1993 \| Question: 8.2 | **B** |
| `3.3.10` | Propositional Logic: GATE CSE 1994 \| Question: 3.13 | **True** |
| `3.3.11` | Propositional Logic: GATE CSE 1995 \| Question: 13 | **N/A** |
| `3.3.12` | Propositional Logic: GATE CSE 1995 \| Question: 2.19 | **D** |
| `3.3.13` | Propositional Logic: GATE CSE 1996 \| Question: 2.3 | **D** |
| `3.3.14` | Propositional Logic: GATE CSE 1997 \| Question: 3.2 | **C** |
| `3.3.15` | Propositional Logic: GATE CSE 1998 \| Question: 1.5 | **A** |
| `3.3.16` | Propositional Logic: GATE CSE 1999 \| Question: 14 | **N/A** |
| `3.3.17` | Propositional Logic: GATE CSE 2000 \| Question: 2.7 | **A** |
| `3.3.18` | Propositional Logic: GATE CSE 2001 \| Question: 1.3 | **A** |
| `3.3.19` | Propositional Logic: GATE CSE 2002 \| Question: 1.8 | **A** |
| `3.3.20` | Propositional Logic: GATE CSE 2002 \| Question: 5b | **N/A** |
| `3.3.21` | Propositional Logic: GATE CSE 2003 \| Question: 72 | **B** |
| `3.3.22` | Propositional Logic: GATE CSE 2004 \| Question: 70 | **A** |
| `3.3.23` | Propositional Logic: GATE CSE 2005 \| Question: 40 | **B** |
| `3.3.24` | Propositional Logic: GATE CSE 2006 \| Question: 27 | **D** |
| `3.3.25` | Propositional Logic: GATE CSE 2008 \| Question: 31 | **B** |
| `3.3.26` | Propositional Logic: GATE CSE 2009 \| Question: 24 | **B** |
| `3.3.27` | Propositional Logic: GATE CSE 2014 \| Set 1 \| Question: 53 | **B** |
| `3.3.28` | Propositional Logic: GATE CSE 2014 \| Set 2 \| Question: 53 | **B** |
| `3.3.29` | Propositional Logic: GATE CSE 2014 \| Set 3 \| Question: 1 | **D** |
| `3.3.30` | Propositional Logic: GATE CSE 2015 \| Set 1 \| Question: 14 | **C** |
| `3.3.31` | Propositional Logic: GATE CSE 2016 \| Set 1 \| Question: 1 | **11** |
| `3.3.32` | Propositional Logic: GATE CSE 2016 \| Set 2 \| Question: 01 | **4** |
| `3.3.33` | Propositional Logic: GATE CSE 2017 \| Set 1 \| Question: 01 | **D** |
| `3.3.34` | Propositional Logic: GATE CSE 2017 \| Set 1 \| Question: 29 | **D** |
| `3.3.35` | Propositional Logic: GATE CSE 2017 \| Set 2 \| Question: 11 | **A** |
| `3.3.36` | Let and Propositional Logic: GATE CSE 2021 \| Set 1 \| Question: 7 | **B** |
| `3.3.37` | Propositional Logic: GATE CSE 2021 \| Set 2 \| Question: 15 | **B;D** |
| `3.3.38` | Propositional Logic: GATE CSE 2024 \| Set 2 \| Question: 2 | **A** |
| `3.3.39` | Propositional Logic: GATE DS&AI 2024 \| Question: 19 | **B;C;D** |
| `3.3.40` | Let Propositional Logic: GATE IT 2004 \| Question: 31 | **C** |

