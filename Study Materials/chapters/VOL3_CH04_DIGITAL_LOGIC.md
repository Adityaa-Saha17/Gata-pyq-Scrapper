# Volume 3 — Chapter 4: Digital Logic

- **Source PDF**: [filter1_volume3.pdf](file:///Users/adityaasaha/Documents/Academics/Gate/filter1_volume3.pdf)
- **Total GATE Questions in Chapter**: **313**

---

## 1. Subtopic Weightage & Question Distribution

| Subtopic # | Subtopic Name | Questions |
| :---: | :--- | :---: |
| **4.1** | Adder | 9 |
| **4.2** | Array Multiplier | 2 |
| **4.4** | Boolean Algebra | 34 |
| **4.5** | Booths Algorithm | 7 |
| **4.6** | Canonical Normal Form | 10 |
| **4.7** | Carry Generator | 2 |
| **4.8** | Circuit Output | 40 |
| **4.9** | Combinational Circuit | 2 |
| **4.10** | Conjunctive Normal Form | 1 |
| **4.11** | Decoder | 3 |
| **4.13** | Digital Counter | 18 |
| **4.14** | Dual Function | 1 |
| **4.15** | Finite State Machines | 4 |
| **4.17** | Flip Flop | 7 |
| **4.18** | Floating Point Representation | 8 |
| **4.19** | Functional Completeness | 7 |
| **4.20** | IEEE Representation | 14 |
| **4.21** | K Map | 17 |
| **4.22** | Little Endian Big Endian | 1 |
| **4.23** | Memory Interfacing | 5 |
| **4.24** | Min No Gates | 6 |
| **4.25** | Min Products of Sum Form | 2 |
| **4.26** | Min Sum of Products Form | 16 |
| **4.27** | Multiplexer | 14 |
| **4.28** | Number Representation | 57 |
| **4.29** | Number System | 1 |
| **4.30** | Prime Implicants | 2 |
| **4.31** | ROM | 4 |
| **4.32** | Reduction | 1 |
| **4.33** | Ripple Counter Operation | 1 |
| **4.35** | Static Hazard | 1 |
| **4.36** | Synchronous Asynchronous Circuits | 4 |


---

## 2. Comprehensive GATE CSE Digital Logic Reference (Expanded Research & Formulas)

### 2.1 Number Systems, Signed Representations & IEEE 754 Floating Point
- **$n$-Bit Signed Integer Ranges**:
  - **Sign-Magnitude & 1's Complement**: $-\big(2^{n-1} - 1\big)$ to $+\big(2^{n-1} - 1\big)$ (Two representations of $0$: $+0$ and $-0$).
  - **2's Complement**: $-2^{n-1}$ to $+\big(2^{n-1} - 1\big)$ (Unique $0$; self-complementing after first $1$ from LSB).
  - **2's Complement Overflow Condition** (adding MSB carry-in $C_{\text{in}}$ and carry-out $C_{\text{out}}$): $\text{Overflow} = C_{\text{in}} \oplus C_{\text{out}}$.
- **IEEE 754 Floating-Point Standard**:
  - **Single Precision (32-bit)**: $1$ Sign bit ($S$) + $8$ Exponent bits ($E$, Bias $= 127$) + $23$ Mantissa/Fraction bits ($M$).
  - **Double Precision (64-bit)**: $1$ Sign bit ($S$) + $11$ Exponent bits ($E$, Bias $= 1023$) + $52$ Mantissa/Fraction bits ($M$).
  - **Values**:
    - **Normalized** ($0 < E < 255$): $(-1)^S \times (1.M)_2 \times 2^{E - \text{Bias}}$.
    - **Denormalized / Subnormal** ($E = 0, M \neq 0$): $(-1)^S \times (0.M)_2 \times 2^{1 - \text{Bias}}$.
    - **Zero** ($E = 0, M = 0$): $\pm 0$.
    - **Infinity** ($E = \text{all } 1\text{s}, M = 0$): $\pm \infty$.
    - **NaN** ($E = \text{all } 1\text{s}, M \neq 0$).

### 2.2 Boolean Algebra, Logic Gates & K-Maps
- **Boolean Functions of $n$ Variables**:
  - Total minterms / maxterms $= 2^n$; Total Boolean functions $= 2^{2^n}$.
  - **Self-Dual Functions** ($f^D(x_1, \dots, x_n) = \overline{f(\overline{x_1}, \dots, \overline{x_n})} = f$): Must have exactly $2^{n-1}$ minterms (no mutually opposite minterms); total self-dual functions of $n$ variables $= \mathbf{2^{2^{n-1}}}$.
- **Universal Gate Realization Counts (Minimum NAND / NOR Gates)**:

| Target Gate | Min 2-Input **NAND** Gates | Min 2-Input **NOR** Gates |
| :--- | :---: | :---: |
| **NOT** ($\overline{A}$) | $1$ | $1$ |
| **AND** ($AB$) | $2$ | $3$ |
| **OR** ($A + B$) | $3$ | $2$ |
| **XOR** ($A \oplus B$) | $4$ | $5$ |
| **XNOR** ($A \odot B$) | $5$ | $4$ |

- **Consensus Theorem (Redundant Term Elimination)**:
  $$AB + \overline{A}C + BC = AB + \overline{A}C, \qquad (A + B)(\overline{A} + C)(B + C) = (A + B)(\overline{A} + C)$$
- **XOR / XNOR Properties**:
  - For **odd** number of inputs, $A \oplus B \oplus C = A \odot B \odot C$!
  - $A \oplus 0 = A$ (Buffer), $A \oplus 1 = \overline{A}$ (Inverter).

### 2.3 Combinational Circuits (Adders, MUX, Decoders)
- **Half Adder**: $S = A \oplus B$, $C = AB$ ($5$ NAND or $5$ NOR gates).
- **Full Adder**: $S = A \oplus B \oplus C_{\text{in}}$, $C_{\text{out}} = AB + BC_{\text{in}} + AC_{\text{in}} = AB + C_{\text{in}}(A \oplus B)$ ($9$ NAND or $9$ NOR gates).
- **Ripple Carry vs Carry Lookahead Adder (CLA)**:
  - $n$-bit Ripple Carry Adder delay: $(n-1) t_{\text{carry}} + \max(t_{\text{carry}}, t_{\text{sum}})$ (or $2n + 1$ gate delays).
  - CLA: $P_i = A_i \oplus B_i$, $G_i = A_i B_i$, $C_{i+1} = G_i + P_i C_i$ (computes all carries in **2 gate delays** after $P_i, G_i$).
- **Multiplexer ($2^n : 1$ MUX)**: Output $Y = \sum_{i=0}^{2^n - 1} m_i I_i$. Any $n$-variable Boolean function can be implemented with a **$2^{n-1} : 1$ MUX** + $1$ NOT gate (or even without NOT if $0, 1, x, \overline{x}$ are available).

### 2.4 Sequential Circuits (Flip-Flops, Counters & Shift Registers)
- **Flip-Flop Characteristic & Excitation Tables**:
  - **SR FF**: $Q^+ = S + \overline{R}Q$ (Constraint: $SR = 0$).
  - **JK FF**: $Q^+ = J\overline{Q} + \overline{K}Q$ (when $J=K=1$, toggles: $Q^+ = \overline{Q}$; race-around avoided by Master-Slave or Edge Triggering).
  - **D FF**: $Q^+ = D$.
  - **T FF**: $Q^+ = T \oplus Q$.
- **Counters ($n$ Flip-Flops)**:
  - **MOD-$M$ Counter**: Divides input clock frequency by $M$: $f_{\text{out}} = \frac{f_{\text{clk}}}{M}$ (requires $n = \lceil \log_2 M \rceil$ FFs).
  - **Ripple (Asynchronous) Counter Max Clock Frequency**: $T_{\text{clk}} \ge n \cdot t_{pd\text{(FF)}} + t_{\text{strobe}}$.
  - **Synchronous Counter Max Clock Frequency**: $T_{\text{clk}} \ge t_{pd\text{(FF)}} + t_{\text{comb}} + t_{\text{setup}}$.
  - **Ring Counter ($n$ FFs)**: MOD-$n$ counter ($n$ used states, $2^n - n$ unused states).
  - **Johnson (Twisted Ring / Switch-Tail) Counter ($n$ FFs)**: MOD-$2n$ counter ($2n$ used states, $2^n - 2n$ unused states; output frequency $= f_{\text{clk}} / 2n$ with 50% duty cycle).

---

## 3. Original PDF Chapter Notes (Preserved Verbatim)

4 Digital Logic (313)
Boolean algebra. Combinational and sequential circuits. Minimization. Number representations and computer
arithmetic (fixed and floating point)
Welcome to the "Digital Logic" chapter of your GATE Computer Science exam preparation. This foundational subject is
the bedrock of computer hardware, providing the essential understanding of how digital circuits process information,
store data, and execute instructions. It delves into the fundamental building blocks of modern computing systems, from
basic logic gates to complex sequential circuits and memory elements. A strong grasp of Digital Logic is crucial not only
for direct questions in the GATE exam but also for understanding related concepts in Computer Architecture, Operating
Systems, and even some aspects of programming. Typically, Digital Logic carries a weightage of 8-12 marks in the
GATE CS paper, with questions ranging from conceptual understanding and circuit analysis to design problems
involving minimization, number representation, and sequential circuit behavior. Questions often include Multiple Choice
Questions (MCQs), Multiple Select Questions (MSQs), and Numerical Answer Type (NAT) questions, testing both
theoretical knowledge and problem-solving skills.
Topic-wise Key Concepts
Adder
An adder is a digital circuit that performs the addition of numbers. It is a fundamental component in Arithmetic Logic
Units (ALUs) of processors.
Half Adder (HA): Adds two single-bit binary numbers. It produces a sum (S) and a carry-out (Cout).
Formulas:
Full Adder (FA): Adds three single-bit binary numbers (two input bits and a carry-in). It produces a sum (S) and a
carry-out (Cout).
Formulas:
Ripple Carry Adder: An n-bit adder constructed by cascading n full adders, where the carry-out of one stage
becomes the carry-in of the next.
Propagation Delay: The total delay is proportional to n, as carry ripples through all stages.
.
Carry Look-Ahead Adder (CLA): A faster adder that generates carries in parallel, reducing propagation delay. It
uses carry generate (G) and carry propagate (P) signals.
Formulas for a single stage i:
For a 4-bit CLA:

*(PDF Page 276)*

Common Pitfalls: Confusing half adder and full adder functionality. Incorrectly calculating propagation delay for
ripple carry vs. CLA.
Problem-solving: Be able to draw and analyze basic adder circuits. Calculate delays for different adder types.
Array Multiplier
An array multiplier is a combinational circuit that performs multiplication of two binary numbers using an array of full
adders and AND gates. It's a direct hardware implementation of the traditional "paper-and-pencil" multiplication method.
Core Idea: For two n-bit numbers, it requires n rows of partial products. Each partial product is generated by
ANDing the multiplicand with one bit of the multiplier. These partial products are then summed using an array of
adders (often full adders) in a staggered fashion.
Structure: An n x m bit array multiplier typically uses n*m AND gates to generate partial products and (n-1)*m full
adders (or similar) to sum them.
Delay: The delay is proportional to n+m, as carries propagate diagonally across the array.
Problem-solving: Understand how partial products are formed and summed. Be able to trace the data flow for
small examples.
Binary Codes
Binary codes are systems used to represent numbers, characters, and instructions in digital systems using binary digits
(bits).
Weighted Codes: Each bit position has a specific weight.
BCD (8421): Each decimal digit is represented by its 4-bit binary equivalent. E.g., .
.
Excess-3: BCD code with 3 added to each digit. Self-complementing.
2421 Code: Another weighted code.
Non-Weighted Codes: Bit positions do not have fixed weights.
Gray Code: Only one bit changes between successive numbers. Used to prevent glitches in ADCs and K-maps.
Binary to Gray: (for MSB to LSB, , for ). More
commonly: , with for the MSB. Correct: , for
from MSB-1 down to 0. Alternative: for , . Example: Binary 1011 (11) ->
Gray: . So 1110.
Gray to Binary: , (for MSB to LSB). Correct: for from
MSB-1 down to 0, . Example: Gray 1110 -> Binary:
. So 1011.
ASCII: 7-bit or 8-bit code for characters.
Error Detection Codes (Parity): Adds an extra bit to detect single-bit errors.
Even Parity: Total number of 1s (including parity bit) is even.
Odd Parity: Total number of 1s (including parity bit) is odd.
Error Correction Codes (Hamming Code): Can detect and correct multiple-bit errors.
Common Pitfalls: Confusing BCD with pure binary. Incorrectly converting between binary and Gray code.
Problem-solving: Perform conversions between different binary codes.
Boolean Algebra
Boolean algebra is a mathematical system for analyzing and simplifying digital circuits. It deals with binary variables and
logical operations.
Basic Postulates:
1. Closure: and are in {0,1}.
2. Commutative: , .
3. Associative: , .

*(PDF Page 277)*

4. Distributive: , .
5. Identity: , .
6. Complement: , .
Theorems and Identities:
Idempotence: , .
Absorption: , .
Consensus: . (If is redundant).
De Morgan's Laws: , .
Involution: .
Null Elements: , .
Common Pitfalls: Forgetting the dual of De Morgan's Law. Incorrectly applying consensus theorem.
Problem-solving: Simplify Boolean expressions using theorems. Prove identities.
Booths Algorithm
Booth's algorithm is a multiplication algorithm that multiplies two signed binary numbers in 2's complement
representation. It is efficient for numbers with long sequences of 0s or 1s.
Core Idea: Instead of adding partial products for every '1' in the multiplier, it looks at pairs of bits in the multiplier.
No operation (0 * multiplicand).
Add multiplicand.
Subtract multiplicand (add 2's complement).
No operation (0 * multiplicand).
Steps:
1. Initialize Product (P) to 0, Multiplicand (M), Multiplier (Q), and an extra bit .
2. Repeat n times (where n is the number of bits in Q):
Examine :
If : .
If : (add 2's complement of M).
If or : No operation.
Arithmetic Right Shift (ASHR) the combined register .
3. The final product is in .
Common Pitfalls: Incorrectly performing 2's complement subtraction. Errors in arithmetic right shift (especially for
negative numbers). Forgetting the bit.
Problem-solving: Trace the algorithm step-by-step for given signed numbers.
Canonical Normal Form
Canonical normal forms are standard forms for Boolean expressions, ensuring uniqueness for a given function. They
are useful for comparison and synthesis.
Canonical Sum of Products (SOP) / Minterm Canonical Form: A sum of minterms. Each minterm is a product
term where all variables appear exactly once, either in true or complemented form.
A minterm is 1 for exactly one combination of inputs.
Example: For , minterms are . So .
Notation: , where i, j, k are decimal equivalents of minterms.
Canonical Product of Sums (POS) / Maxterm Canonical Form: A product of maxterms. Each maxterm is a sum
term where all variables appear exactly once, either in true or complemented form.
A maxterm is 0 for exactly one combination of inputs.
Example: For , maxterms are . So
.
Notation: , where i, j, k are decimal equivalents of maxterms.
Relationship: If , then . Also, .
Common Pitfalls: Confusing minterms with maxterms, and their corresponding sum/product forms. Incorrectly
converting between SOP and POS canonical forms.
Problem-solving: Convert truth tables to canonical SOP/POS. Convert between canonical SOP and POS.
Carry Generator

*(PDF Page 278)*

A carry generator is a combinational circuit used in adders, particularly in Carry Look-Ahead Adders, to quickly compute
carry bits, thereby speeding up addition.
Core Idea: It uses generate (G) and propagate (P) signals to calculate carries in parallel, rather than waiting for
them to ripple.
(carry is generated if both input bits are 1).
(carry is propagated if one input bit is 1).
(carry out is generated or propagated from carry in).
Look-ahead Logic: For a 4-bit block, the carry out can be expressed directly in terms of terms, as shown in the Adder section.
Problem-solving: Derive carry equations for multi-bit carry look-ahead blocks.
and the
Circuit Output
The circuit output refers to the final value(s) produced by a digital circuit based on its inputs and internal logic. It can be
a single bit or a multi-bit word.
Combinational Circuits: Output depends only on the present inputs.
Sequential Circuits: Output depends on present inputs and past inputs (stored state).
Analysis: For a given circuit diagram, determine the Boolean expression for the output(s) in terms of the inputs.
Problem-solving: Derive truth tables or Boolean expressions from circuit diagrams. Evaluate output for specific
input combinations.
Combinational Circuit
A combinational circuit is a type of digital circuit whose output depends solely on the current values of its inputs. It has
no memory elements.
Characteristics:
No feedback loops.
Output changes instantaneously with input changes (after propagation delay).
Examples: Adders, Subtractors, Decoders, Encoders, Multiplexers, Demultiplexers.
Design Steps:
1. Define the problem (inputs, outputs).
2. Derive the truth table.
3. Obtain simplified Boolean expressions (K-map, Quine-McCluskey).
4. Draw the logic diagram.
Common Pitfalls: Confusing combinational with sequential circuits. Overlooking propagation delays in timing
analysis.
Problem-solving: Design circuits from specifications. Analyze existing circuits.
Conjunctive Normal Form
Conjunctive Normal Form (CNF) is a standardized way of writing Boolean expressions as a conjunction (AND) of
clauses, where each clause is a disjunction (OR) of literals.
Core Idea: A product of sums (POS) form where each sum term (clause) contains one or more literals. It is not
necessarily canonical (i.e., not all variables need to be present in each clause).
Example: .
Relationship to Canonical POS: Canonical POS (maxterm form) is a specific type of CNF where each clause is a
maxterm (contains all variables).
Problem-solving: Convert Boolean expressions to CNF.
Decoder
A decoder is a combinational circuit that converts n input lines into or low) at any given time, corresponding to the binary value of the inputs.
output lines. Only one output line is active (high
Types:
Binary Decoder (n-to- ): E.g., 2-to-4 decoder, 3-to-8 decoder.
BCD-to-7 Segment Decoder: Converts BCD input to control a 7-segment display.
Enable Input: Most decoders have an enable input (E). If E is inactive, all outputs are inactive.

*(PDF Page 279)*

Applications: Memory address decoding, data demultiplexing, implementing Boolean functions.
An n-to- decoder can implement any n-variable Boolean function by ORing the appropriate minterms.
Common Pitfalls: Incorrectly interpreting active-high vs. active-low outputs.
Problem-solving: Design decoders. Use decoders to implement Boolean functions.
Digital Circuits
Digital circuits are electronic circuits that operate on discrete voltage levels, typically representing binary 0 and 1. They
form the basis of all modern digital systems.
Categories:
Combinational Circuits: Output depends only on current inputs (e.g., gates, adders, decoders).
Sequential Circuits: Output depends on current inputs and past inputs (memory elements) (e.g., flip-flops,
counters, registers).
Logic Gates: AND, OR, NOT, NAND, NOR, XOR, XNOR are the basic building blocks.
Key Properties: Speed (propagation delay), Power Consumption, Fan-in/Fan-out, Noise Margin.
Problem-solving: Analyze and design circuits using logic gates.
Digital Counter
A digital counter is a sequential circuit that cycles through a predefined sequence of states upon receiving input clock
pulses. It's essentially a register that increments or decrements its stored value.
Types:
Asynchronous (Ripple) Counter: Flip-flops are cascaded, and the output of one FF clocks the next. Simple to
design but suffers from propagation delay.
Synchronous Counter: All flip-flops are clocked simultaneously by a common clock pulse. More complex
design but faster and more reliable.
Up/Down Counter: Can count in increasing or decreasing order.
Mod-N Counter: Counts from 0 to N-1 and then resets.
Design: Involves state diagrams, state tables, flip-flop excitation tables, and K-maps for logic minimization.
Formulas: For an n-bit counter, it can count up to states (0 to ).
Common Pitfalls: Incorrectly determining the modulus of a counter. Errors in state table derivation or K-map
minimization for synchronous counters.
Problem-solving: Analyze existing counter circuits. Design synchronous counters for specific sequences.
Dual Function
The dual of a Boolean expression is obtained by interchanging OR and AND operations, and 0s and 1s. Variables and
their complements remain unchanged.
Procedure:
1. Replace all '+' with '
.
' (OR with AND).
2. Replace all '
.
' with '+' (AND with OR).
3. Replace all '0' with '1'
.
4. Replace all '1' with '0'
.
Example: Dual of is .
Principle of Duality: If a Boolean identity is true, its dual is also true.
Common Pitfalls: Accidentally complementing variables when finding the dual.
Problem-solving: Find the dual of a given Boolean expression.
Finite State Machines (FSM)
Finite State Machines (FSMs) are mathematical models of computation used to design sequential circuits. They consist
of a finite number of states, transitions between states, and actions based on inputs.
Components: States, Inputs, Outputs, Transitions.
Types:
Mealy Machine: Output depends on the present state AND the present input.
Moore Machine: Output depends only on the present state.
Representation: State diagrams, state tables.
Design Steps:

*(PDF Page 280)*

1. State Diagram.
2. State Table.
3. State Assignment (binary encoding).
4. Flip-flop excitation table.
5. K-maps for input equations and output equations.
6. Logic diagram.
Common Pitfalls: Confusing Mealy and Moore outputs. Errors in state assignment or deriving excitation equations.
Problem-solving: Design FSMs from specifications. Analyze given FSMs.
Fixed Point Representation
Fixed-point representation is a method of representing real numbers where the position of the binary point (radix point)
is fixed. It's used for numbers with a limited range and high precision.
Format: where I is the integer part and F is the fractional part.
For an n-bit number with k bits for the fractional part, the range is to (for signed 2's
complement).
Value: .
Signed Fixed-Point: Typically uses 2's complement for negative numbers.
Common Pitfalls: Incorrectly determining the range or precision for a given bit allocation.
Problem-solving: Convert decimal numbers to fixed-point binary and vice-versa. Perform arithmetic operations.
Flip Flop
A flip-flop is a basic 1-bit memory element (sequential circuit) that can store a binary value (0 or 1). It has two stable
states and is often edge-triggered.
Types and Characteristics:
SR Flip-Flop: Set-Reset.
Characteristic Equation: , (forbidden state if SR=1).
Excitation Table:
S R
0 0 0 X
0 1 1 0
1 0 0 1
1 1 X 0
JK Flip-Flop: J-K. Overcomes SR's forbidden state (toggle if JK=11).
Characteristic Equation: .
Excitation Table:
J K
0 0 0 X
0 1 1 X
1 0 X 1
1 1 X 0
D Flip-Flop: Data. Stores the input D when clocked.
Characteristic Equation: .
Excitation Table:
D
0 0 0
0 1 1
1 0 0
1 1 1
T Flip-Flop: Toggle. Toggles its state if T=1, holds if T=0.
Characteristic Equation: .
Excitation Table:
T
0 0 0
0 1 1

*(PDF Page 281)*

1 0 1
1 1 0
Edge-Triggered vs. Level-Triggered: Flip-flops are edge-triggered (positive or negative), latches are level-
triggered.
Setup Time: Data must be stable before clock edge.
Hold Time: Data must be stable after clock edge.
Propagation Delay: Time for output to change after clock edge.
Common Pitfalls: Confusing characteristic equations with excitation tables. Misinterpreting edge vs. level
triggering.
Problem-solving: Analyze flip-flop behavior. Use flip-flops to design sequential circuits.
Floating Point Representation
Floating-point representation is a method to represent real numbers over a wider dynamic range than fixed-point, at the
cost of precision. It uses a sign, exponent, and mantissa (significand).
Format: , where M is mantissa, B is base, E is exponent.
Normalization: Mantissa is typically normalized to have a leading '1' (implicit in IEEE standard).
Bias: Exponent is stored in biased form to allow representation of both positive and negative exponents without a
separate sign bit. Biased exponent = Actual exponent + Bias.
Common Pitfalls: Errors in converting between decimal and floating-point, especially with bias and normalization.
Problem-solving: Convert numbers to/from floating-point format. Understand the implications of range and
precision.
Functional Completeness
A set of logic gates is functionally complete if any Boolean function can be implemented using only gates from that set.
Minimum Functionally Complete Sets:
{AND, OR, NOT}
{NAND} (NAND is universal)
{NOR} (NOR is universal)
{AND, NOT}
{OR, NOT}
Properties: To be functionally complete, a set of gates must be able to implement NOT, AND, and OR (or
NAND/NOR). This requires the ability to implement:
Inversion (NOT)
AND (or OR)
The set must not be monotonic (cannot implement NOT).
The set must not be self-dual (cannot implement NOT).
The set must not be linear (cannot implement AND/OR).
The set must not preserve 0 (cannot implement NOT).
The set must not preserve 1 (cannot implement NOT).
Common Pitfalls: Incorrectly identifying functionally complete sets.
Problem-solving: Determine if a given set of gates is functionally complete. Implement basic gates using a
universal gate.
IEEE Representation
The IEEE 754 standard defines formats for representing floating-point numbers in computers, ensuring consistency
across different platforms.
Single Precision (32-bit):
1 bit for Sign (S)
8 bits for Exponent (E) - biased by 127
23 bits for Mantissa (M) - implicit leading '1'
Value:
Range: Approx. to
Double Precision (64-bit):
1 bit for Sign (S)
11 bits for Exponent (E) - biased by 1023

*(PDF Page 282)*

52 bits for Mantissa (M) - implicit leading '1'
Value:
Special Values:
Zero:
Denormalized Numbers: (for very small numbers, implicit leading '0')
Infinity:
NaN (Not a Number):
Common Pitfalls: Forgetting the implicit leading '1' in the mantissa. Incorrectly applying the exponent bias.
Handling special values.
Problem-solving: Convert decimal numbers to IEEE 754 format and vice-versa. Understand the representation of
special values.
K Map (Karnaugh Map)
A K-map is a graphical method for simplifying Boolean expressions. It provides a systematic way to find the minimal
sum-of-products (SOP) or product-of-sums (POS) form.
Core Idea: Arranges minterms (or maxterms) in a grid such that adjacent cells differ by only one bit, allowing visual
identification of adjacent terms for grouping.
Grouping Rules:
Groups must be powers of 2 (1, 2, 4, 8, ...).
Groups must be rectangular or square.
Groups can wrap around the edges.
Groups should be as large as possible.
Every '1' (for SOP) or '0' (for POS) must be covered at least once.
Prime Implicant (PI): A product term obtained by combining the maximum possible number of adjacent cells in a K-
map.
Essential Prime Implicant (EPI): A prime implicant that covers at least one minterm (or maxterm) that no other
prime implicant covers. EPIs must be included in the minimal expression.
Don't Cares (X): Input combinations that never occur or whose output doesn't matter. They can be grouped with 1s
(for SOP) or 0s (for POS) to make larger groups.
Common Pitfalls: Incorrect grouping (non-power of 2, non-rectangular). Not identifying all EPIs. Not finding the
minimal set of PIs.
Problem-solving: Simplify Boolean expressions using K-maps for up to 4-5 variables.
Little Endian Big Endian
These terms refer to the byte ordering conventions used to store multi-byte data (like integers or floating-point numbers)
in computer memory.
Big-Endian: The most significant byte (MSB) of a multi-byte data unit is stored at the lowest memory address.
, at address 1000:
Example: For Address Value
1000 12
1001 34
1002 56
1003 78
Little-Endian: The least significant byte (LSB) of a multi-byte data unit is stored at the lowest memory address.
, at address 1000:
Example: For Address Value
1000 78
1001 56
1002 34
1003 12
Common Pitfalls: Confusing the two, especially when dealing with memory dumps or network protocols.
Problem-solving: Determine how a given multi-byte value would be stored in memory under both endianness
conventions.
Memory Interfacing

*(PDF Page 283)*

Memory interfacing involves connecting memory chips to a processor or other digital system, ensuring proper address
decoding, data transfer, and control signaling.
Address Decoding: Logic circuitry that selects the correct memory chip (or block within a chip) based on the
address provided by the processor.
Full Decoding: Every unique address maps to a unique memory location.
Partial Decoding: Multiple addresses map to the same memory location (simpler but less efficient).
Chip Select (CS): An input pin on memory chips that, when active, enables the chip for read/write operations.
Address decoders generate the CS signal.
Output Enable (OE) / Read (RD): Enables data output from memory.
Write Enable (WE) / Write (WR): Enables data input to memory.
Memory Map: A diagram showing how memory addresses are allocated to different memory devices.
Formulas: For a memory chip with N address lines and M data lines, its capacity is bits.
Common Pitfalls: Incorrectly designing address decoding logic. Miscalculating memory capacity or address range.
Problem-solving: Design address decoding circuits for given memory chips and address ranges. Calculate
memory capacity.
Min No Gates
Minimizing the number of gates refers to finding the simplest possible logic circuit to implement a given Boolean
function, often after minimizing the Boolean expression.
Core Idea: Directly related to Boolean expression simplification (K-maps, Quine-McCluskey). Fewer terms and
fewer literals generally mean fewer gates.
Considerations:
Gate Type: NAND/NOR implementations often require fewer gates than AND/OR/NOT for universal logic.
Fan-in: Gates have a maximum number of inputs.
Gate Cost: Sometimes gates have different costs (e.g., XOR is more complex than AND).
Problem-solving: After K-map simplification, draw the circuit using the minimal SOP/POS. Then convert to
universal gates (NAND/NOR) if specified, and count the gates.
Min Products of Sum Form (MPOS)
The minimal Product of Sums (POS) form is the simplest Boolean expression representing a function as a product of
sum terms (maxterms or sum literals).
Derivation:
1. Identify the '0's in the truth table or K-map.
2. Group the '0's in the K-map (following K-map rules).
3. Each group corresponds to a sum term.
4. The product of these sum terms is the minimal POS expression.
Properties: Each sum term is an implicant of the complement of the function.
Common Pitfalls: Incorrectly forming sum terms from K-map groups (e.g., Problem-solving: Use K-maps to find the minimal POS expression.
for A=1).
Min Sum of Products Form (MSOP)
The minimal Sum of Products (SOP) form is the simplest Boolean expression representing a function as a sum of
product terms (minterms or product literals).
Derivation:
1. Identify the '1's in the truth table or K-map.
2. Group the '1's in the K-map (following K-map rules).
3. Each group corresponds to a product term.
4. The sum of these product terms is the minimal SOP expression.
Properties: Each product term is an implicant of the function.
Common Pitfalls: Not identifying all essential prime implicants. Not selecting the minimal set of prime implicants to
cover all 1s.
Problem-solving: Use K-maps to find the minimal SOP expression.
Multiplexer (MUX)

*(PDF Page 284)*

A multiplexer (MUX) is a combinational circuit that selects one of several input data lines and routes it to a single output
line. The selection is controlled by a set of select lines.
Core Idea: An n-to-1 MUX has n data inputs, select lines, and 1 output.
Functionality: If there are 's' select lines, it can select from data inputs.
Applications: Data selection, parallel-to-serial conversion, implementing Boolean functions.
An n-variable Boolean function can be implemented using a -variable MUX and external logic on the
data inputs.
Formulas: For a 2-to-1 MUX with select S, inputs : .
Common Pitfalls: Incorrectly mapping inputs to select lines when implementing functions.
Problem-solving: Design MUX circuits. Use MUXes to implement Boolean functions.
Number Representation
Number representation refers to the various ways in which numerical values (integers, real numbers) are stored and
manipulated in digital systems.
Unsigned Binary: All bits represent magnitude. Range for n bits: 0 to .
Signed Magnitude: MSB is sign bit (0 for positive, 1 for negative), remaining bits are magnitude.
Range for n bits: to .
Two representations for zero ( ).
1's Complement: Negative numbers are obtained by inverting all bits of the positive number.
Range for n bits: to .
Two representations for zero ( ).
Addition: Add normally, then add end-around carry to the sum.
2's Complement: Negative numbers are obtained by inverting all bits and adding 1 to the result. Most common
representation for signed integers.
Range for n bits: to .
Unique representation for zero.
Addition/Subtraction: Perform binary addition directly. Overflow detection: if signs of inputs are same but sign of
result is different.
Fixed-Point and Floating-Point: Covered in their respective sections.
Common Pitfalls: Errors in converting between signed representations. Incorrectly detecting overflow.
Problem-solving: Convert numbers between different representations. Perform arithmetic operations and detect
overflow.
Number System
A number system is a set of symbols and rules for representing numerical quantities. Digital systems primarily use
binary, but conversions to/from decimal, octal, and hexadecimal are common.
Decimal (Base 10): Digits 0-9.
Binary (Base 2): Digits 0, 1.
Octal (Base 8): Digits 0-7. Each octal digit corresponds to 3 binary bits.
Hexadecimal (Base 16): Digits 0-9, A-F. Each hex digit corresponds to 4 binary bits.
Conversions:
Decimal to Binary/Octal/Hex: Repeated division by base, collecting remainders.
Binary/Octal/Hex to Decimal: Sum of (digit * base^position).
Binary to Octal/Hex: Group bits (3 for octal, 4 for hex) and convert each group.
Octal/Hex to Binary: Convert each digit to its 3/4-bit binary equivalent.
Common Pitfalls: Errors in base conversions, especially with fractional parts.
Problem-solving: Perform conversions between any two number systems.
Prime Implicants
In Boolean algebra simplification (e.g., using K-maps), a prime implicant (PI) is a product term that cannot be combined
with any other term to eliminate a literal.
Core Idea: It represents a maximal group of adjacent 1s (or 0s for POS) in a K-map.
Essential Prime Implicant (EPI): A prime implicant that covers at least one minterm (or maxterm) that no other
prime implicant covers. All EPIs must be included in the minimal expression.

*(PDF Page 285)*

Redundant Prime Implicant: A prime implicant whose covered minterms are all covered by other prime implicants
(including EPIs).
Problem-solving: Identify all PIs and EPIs from a K-map. Use them to derive minimal SOP/POS expressions.
ROM (Read-Only Memory)
ROM is a non-volatile memory device whose contents are programmed during manufacturing or by the user and cannot
be easily changed during operation. It's used to store fixed programs or lookup tables.
Types:
Mask ROM: Programmed during manufacturing.
PROM (Programmable ROM): User-programmable once.
EPROM (Erasable PROM): Erasable by UV light, reprogrammable.
EEPROM (Electrically Erasable PROM): Electrically erasable, reprogrammable.
Flash Memory: A type of EEPROM, block-erasable.
Structure: Consists of an address decoder and an array of memory cells (fuses/transistors).
An n-input, m-output ROM can implement m different n-variable Boolean functions.
Applications: Storing BIOS, lookup tables, implementing combinational logic functions.
Problem-solving: Determine the size of ROM needed for a given function. Implement Boolean functions using
ROM.
Reduction
Reduction in digital logic refers to the process of simplifying Boolean expressions or minimizing the number of
gates/components in a circuit while maintaining its functionality.
Methods:
Boolean Algebra: Applying theorems and postulates.
Karnaugh Maps (K-maps): Graphical method for up to 5-6 variables.
Quine-McCluskey Algorithm: Tabular method for more variables, suitable for computer implementation.
Goals: Reduce cost (fewer gates), reduce power consumption, increase speed (fewer gate delays).
Common Pitfalls: Not finding the absolute minimal form. Errors in applying simplification rules.
Problem-solving: Apply various reduction techniques to simplify Boolean expressions.
Ripple Counter Operation
A ripple counter (asynchronous counter) is a sequential circuit where the output of one flip-flop serves as the clock input
for the next flip-flop in the chain.
Operation:
The first flip-flop (LSB) is clocked by the external clock.
Its output (Q) then clocks the next flip-flop, and so on.
This creates a "ripple" effect as the clock signal propagates through the stages.
Characteristics:
Simple Design: Easy to construct.
Propagation Delay: The total delay accumulates through each flip-flop, leading to a maximum operating
frequency limitation. .
Glitches: Due to varying propagation delays, intermediate states may appear briefly, causing glitches.
Modulus: An n-bit ripple counter counts states (Mod- ). To achieve Mod-N, external logic is needed to reset
the counter at N.
Common Pitfalls: Overlooking the cumulative propagation delay. Incorrectly determining the count sequence or
modulus.
Problem-solving: Analyze the timing and counting sequence of ripple counters. Calculate maximum operating
frequency.
Shift Registers
A shift register is a sequential circuit capable of storing binary data and shifting it left or right by one or more bit
positions on each clock pulse.
Types:
SISO (Serial-In, Serial-Out): Data enters and exits serially.

*(PDF Page 286)*

SIPO (Serial-In, Parallel-Out): Data enters serially, but all bits are available simultaneously at parallel outputs.
PISO (Parallel-In, Serial-Out): Data enters in parallel, then shifts out serially.
PIPO (Parallel-In, Parallel-Out): Data enters and exits in parallel.
Bidirectional Shift Register: Can shift data both left and right.
Universal Shift Register: Can perform all the above operations (SISO, SIPO, PISO, PIPO, load, hold).
Applications: Data conversion (serial-to-parallel, parallel-to-serial), data manipulation, sequence generation,
arithmetic operations (multiplication/division by powers of 2).
Structure: Typically built using D flip-flops.
Common Pitfalls: Incorrectly tracing data movement for different shift register types.
Problem-solving: Analyze the operation of various shift registers. Design circuits using shift registers.
Static Hazard
A static hazard is a momentary undesirable glitch (a brief 0 or 1 pulse) in the output of a combinational circuit when the
input changes, even though the output should remain constant.
Types:
Static-1 Hazard: Output should remain 1 but momentarily goes to 0. Occurs when a K-map has two adjacent 1s
that are covered by different prime implicants, and there's no overlapping prime implicant to cover the transition
path.
Static-0 Hazard: Output should remain 0 but momentarily goes to 1. Occurs in POS implementations.
Cause: Unequal propagation delays through different paths in the circuit.
Detection: In a K-map for SOP, a static-1 hazard exists between two adjacent 1s if they are not covered by a
common prime implicant.
Elimination: Add redundant prime implicants to cover all adjacent pairs of 1s (for static-1 hazards) or 0s (for static-0
hazards). This means adding an extra AND gate (for SOP) or OR gate (for POS).
Common Pitfalls: Forgetting to check for hazards in minimal circuits. Incorrectly adding redundant terms.
Problem-solving: Identify static hazards in a given circuit or K-map. Eliminate hazards by adding redundant terms.
Synchronous Asynchronous Circuits
This distinction refers to how sequential circuits handle timing and state changes.
Synchronous Circuits:
All memory elements (flip-flops) are controlled by a single, common clock signal.
State changes occur only at discrete clock edges.
Easier to design and debug due to predictable timing.
Less prone to race conditions and hazards.
Examples: Synchronous counters, shift registers, FSMs.
Asynchronous Circuits:
Memory elements are not controlled by a common clock.
State changes occur in response to changes in input signals, without a clock.
Can be faster (no clock propagation delay) and consume less power.
Much harder to design and verify due to potential for race conditions and hazards.
Examples: Asynchronous (ripple) counters, latches, arbiters.
Common Pitfalls: Confusing the characteristics and trade-offs of each type. Incorrectly identifying a circuit as
synchronous or asynchronous.
Problem-solving: Understand the timing behavior of both types of circuits.
Quick Formula Reference
Half Adder:
Full Adder:
Carry Look-Ahead Adder (stage i):

*(PDF Page 287)*

Binary to Gray Code: (with for MSB, or , for
).
Gray to Binary Code: (with ).
De Morgan's Laws:
Absorption Law:
Consensus Theorem:
SR Flip-Flop Characteristic Equation: (with )
JK Flip-Flop Characteristic Equation:
D Flip-Flop Characteristic Equation:
T Flip-Flop Characteristic Equation:
IEEE 754 Single Precision (32-bit):
IEEE 754 Double Precision (64-bit):
Multiplexer (2-to-1):
Ripple Counter Delay (n-bit):
Memory Capacity (N address, M data): bits
Important Tips for GATE
1. Master Boolean Algebra and K-Maps: These are fundamental. Practice simplification extensively for both SOP
and POS forms. Be quick and accurate in identifying prime implicants and essential prime implicants.
2. Understand Number Representations Thoroughly: Pay close attention to signed magnitude, 1's complement,
and especially 2's complement. Practice conversions, arithmetic operations (addition, subtraction), and overflow
detection for different bit lengths. IEEE 754 floating-point is a recurring topic; know the format, bias, and special
values.
3. Differentiate Combinational vs. Sequential Circuits: Clearly understand their definitions, characteristics, and
design methodologies. Be able to identify memory elements (flip-flops, latches) that make a circuit sequential.
4. Memorize Flip-Flop Characteristic and Excitation Tables: For SR, JK, D, and T flip-flops, these tables are crucial
for analyzing and designing sequential circuits (counters, shift registers, FSMs). Don't confuse them.
5. Practice FSM Design: Be comfortable with state diagrams, state tables, state assignment, and deriving next-state
and output equations using K-maps. Pay attention to Mealy vs. Moore machine characteristics.
6. Beware of "Minimum Number of Gates" Questions: These often require not just Boolean simplification but also
considering universal gate implementations (NAND-only or NOR-only logic) and gate fan-in/fan-out constraints.
7. Focus on Timing and Delays: Understand propagation delays in combinational circuits (e.g., adders) and
sequential circuits (e.g., ripple counters). Be able to calculate critical path delays and maximum operating
frequencies.
8. Don't Overlook Hazards: Static hazards are a common trap. Learn how to detect them using K-maps and eliminate
them by adding redundant terms.

---

## 4. Complete Question Index & Answer Key Record (313 Questions)

| Q # | Question Source / Title | Answer Key |
| :---: | :--- | :---: |
| `4.1.1` | Adder: GATE CSE 1988 \| Question: 4ii | **N/A** |
| `4.1.2` | Adder: GATE CSE 1990 \| Question: 1-i | **N/A** |
| `4.1.3` | Adder: GATE CSE 1997 \| Question: 2.5 | **B** |
| `4.1.4` | Adder: GATE CSE 1999 \| Question: 2.16 | **B** |
| `4.1.5` | Adder: GATE CSE 2003 \| Question: 46 | **A** |
| `4.1.6` | Adder: GATE CSE 2004 \| Question: 62 | **B** |
| `4.1.7` | Adder: GATE CSE 2015 \| Set 2 \| Question: 48 | **19.2** |
| `4.1.8` | Adder: GATE CSE 2016 \| Set 1 \| Question: 33 | **B** |
| `4.1.9` | Adder: GATE CSE 2016 \| Set 2 \| Question: 07 | **-1** |
| `4.2.1` | Array Multiplier: GATE CSE 1999 \| Question: 1.21 | **B** |
| `4.2.2` | Array Multiplier: GATE CSE 2003 \| Question: 11 | **C** |
| `4.3.1` | Binary Codes: GATE CSE 2006 \| Question: 40 | **C** |
| `4.4.1` | Boolean Algebra: GATE CSE 1987 \| Question: 1-II | **D** |
| `4.4.2` | Boolean Algebra: GATE CSE 1987 \| Question: 12-a | **C** |
| `4.4.3` | Boolean Algebra: GATE CSE 1988 \| Question: 2-iii | **N/A** |
| `4.4.4` | Boolean Algebra: GATE CSE 1989 \| Question: 4-x | **N/A** |
| `4.4.5` | Boolean Algebra: GATE CSE 1989 \| Question: 5-a | **N/A** |
| `4.4.6` | Boolean Algebra: GATE CSE 1992 \| Question: 02-i | **D** |
| `4.4.7` | Boolean Algebra: GATE CSE 1994 \| Question: 4 | **N/A** |
| `4.4.8` | Boolean Algebra: GATE CSE 1995 \| Question: 2.5 | **A** |
| `4.4.9` | Boolean Algebra: GATE CSE 1997 \| Question: 2-1 | **B** |
| `4.4.10` | Boolean Algebra: GATE CSE 1998 \| Question: 1.13 | **D** |
| `4.4.11` | Boolean Algebra: GATE CSE 1998 \| Question: 2.8 | **C** |
| `4.4.12` | Boolean Algebra: GATE CSE 1999 \| Question: 1.7 | **D** |
| `4.4.13` | Boolean Algebra: GATE CSE 2000 \| Question: 2.10 | **C** |
| `4.4.14` | Boolean Algebra: GATE CSE 2002 \| Question: 2-3 | **C** |
| `4.4.15` | Boolean Algebra: GATE CSE 2004 \| Question: 17 | **D** |
| `4.4.16` | Boolean Algebra: GATE CSE 2007 \| Question: 32 | **D** |
| `4.4.17` | Boolean Algebra: GATE CSE 2007 \| Question: 33 | **D** |
| `4.4.18` | Boolean Algebra: GATE CSE 2008 \| Question: 26 | **A** |
| `4.4.19` | Boolean Algebra: GATE CSE 2012 \| Question: 6 | **A** |
| `4.4.20` | Boolean Algebra: GATE CSE 2013 \| Question: 21 | **D** |
| `4.4.21` | Boolean Algebra: GATE CSE 2014 \| Set 3 \| Question: 55 | **D** |
| `4.4.22` | Boolean Algebra: GATE CSE 2015 \| Set 2 \| Question: 37 | **1** |
| `4.4.23` | Boolean Algebra: GATE CSE 2016 \| Set 1 \| Question: 06 | **A** |
| `4.4.24` | Boolean Algebra: GATE CSE 2016 \| Set 2 \| Question: 08 | **C** |
| `4.4.25` | Boolean Algebra: GATE CSE 2017 \| Set 2 \| Question: 27 | **C** |
| `4.4.26` | Boolean Algebra: GATE CSE 2018 \| Question: 4 | **D** |
| `4.4.27` | Boolean Algebra: GATE CSE 2019 \| Question: 6 | **B** |
| `4.4.28` | Boolean Algebra: GATE CSE 2021 \| Set 1 \| Question: 42 | **B;C;D** |
| `4.4.29` | Boolean Algebra: GATE CSE 2024 \| Set 2 \| Question: 20 | **B;C** |
| `4.4.30` | Boolean Algebra: GATE CSE 2025 \| Set 1 \| Question: 14 | **B;D** |
| `4.4.31` | Boolean Algebra: GATE CSE 2025 \| Set 2 \| Question: 40 | **B;C;D** |
| `4.4.32` | Boolean Algebra: GATE CSE 2026 \| Set 2 \| Question: 6 | **B** |
| `4.4.33` | Boolean Algebra: GATE IT 2004 \| Question: 44 | **B** |
| `4.4.34` | Boolean Algebra: GATE IT 2005 \| Question: 7 | **C** |
| `4.5.1` | Booths Algorithm: GATE CSE 1990 \| Question: 8b | **N/A** |
| `4.5.2` | Booths Algorithm: GATE CSE 1996 \| Question: 1.23 | **A** |
| `4.5.3` | Booths Algorithm: GATE CSE 1999 \| Question: 1.20 | **B** |
| `4.5.4` | Booths Algorithm: GATE CSE 2025 \| Set 2 \| Question: 22 | **13:13** |
| `4.5.5` | Booths Algorithm: GATE IT 2005 \| Question: 8 | **A** |
| `4.5.6` | Booths Algorithm: GATE IT 2006 \| Question: 38 | **C** |
| `4.5.7` | Booths Algorithm: GATE IT 2008 \| Question: 42 | **B** |
| `4.6.1` | Canonical Normal Form: GATE CSE 1988 \| Question: 2-v | **N/A** |
| `4.6.2` | Canonical Normal Form: GATE CSE 2002 \| Question: 2-1 | **A** |
| `4.6.3` | Canonical Normal Form: GATE CSE 2008 \| Question: 8 | **C** |
| `4.6.4` | Canonical Normal Form: GATE CSE 2010 \| Question: 6 | **A** |
| `4.6.5` | Canonical Normal Form: GATE CSE 2015 \| Set 3 \| Question: 43 | **3** |
| `4.6.6` | Canonical Normal Form: GATE CSE 2015 \| Set 3 \| Question: 44 | **A** |
| `4.6.7` | Canonical Normal Form: GATE CSE 2019 \| Question: 30 | **A** |
| `4.6.8` | Canonical Normal Form: GATE CSE 2019 \| Question: 50 | **3** |
| `4.6.9` | Canonical Normal Form: GATE CSE 2020 \| Question: 28 | **B** |
| `4.6.10` | Canonical Normal Form: GATE CSE 2024 \| Set 2 \| Question: 40 | **C;D** |
| `4.7.1` | Carry Generator: GATE CSE 2006 \| Question: 36 | **A** |
| `4.7.2` | Carry Generator: GATE CSE 2007 \| Question: 35 | **B** |
| `4.8.1` | Circuit Output: GATE CSE 1987 \| Question: 1-IV | **B** |
| `4.8.2` | Circuit Output: GATE CSE 1989 \| Question: 4-ix | **N/A** |
| `4.8.3` | Circuit Output: GATE CSE 1990 \| Question: 3-i | **B** |
| `4.8.4` | Circuit Output: GATE CSE 1991 \| Question: 5-a | **N/A** |
| `4.8.5` | Circuit Output: GATE CSE 1993 \| Question: 19 | **N/A** |
| `4.8.6` | Circuit Output: GATE CSE 1993 \| Question: 6-3 | **A;C** |
| `4.8.7` | Circuit Output: GATE CSE 1993 \| Question: 6.1 | **B** |
| `4.8.8` | Circuit Output: GATE CSE 1993 \| Question: 6.2 | **B** |
| `4.8.9` | Circuit Output: GATE CSE 1994 \| Question: 1.8 | **B** |
| `4.8.10` | Circuit Output: GATE CSE 1994 \| Question: 11 | **011** |
| `4.8.11` | Circuit Output: GATE CSE 1996 \| Question: 2.21 | **D** |
| `4.8.12` | Circuit Output: GATE CSE 1996 \| Question: 2.22 | **C** |
| `4.8.13` | Circuit Output: GATE CSE 1996 \| Question: 24-a | **N/A** |
| `4.8.14` | Circuit Output: GATE CSE 1996 \| Question: 24-b | **N/A** |
| `4.8.15` | Circuit Output: GATE CSE 1997 \| Question: 5.5 | **B** |
| `4.8.16` | Circuit Output: GATE CSE 1999 \| Question: 2.8 | **B** |
| `4.8.17` | Circuit Output: GATE CSE 2000 \| Question: 2.12 | **A** |
| `4.8.18` | Circuit Output: GATE CSE 2001 \| Question: 2.8 | **A** |
| `4.8.19` | Circuit Output: GATE CSE 2002 \| Question: 2.2 | **A** |
| `4.8.20` | Circuit Output: GATE CSE 2004 \| Question: 61 | **D** |
| `4.8.21` | Circuit Output: GATE CSE 2005 \| Question: 15 | **A** |
| `4.8.22` | Circuit Output: GATE CSE 2005 \| Question: 62 | **A** |
| `4.8.23` | Circuit Output: GATE CSE 2005 \| Question: 64 | **D** |
| `4.8.24` | Circuit Output: GATE CSE 2006 \| Question: 35 | **A** |
| `4.8.25` | Circuit Output: GATE CSE 2006 \| Question: 37 | **C** |
| `4.8.26` | Circuit Output: GATE CSE 2006 \| Question: 8 | **C** |
| `4.8.27` | Circuit Output: GATE CSE 2007 \| Question: 36 | **C** |
| `4.8.28` | Circuit Output: GATE CSE 2010 \| Question: 31 | **A** |
| `4.8.29` | Circuit Output: GATE CSE 2010 \| Question: 32 | **A** |
| `4.8.30` | Circuit Output: GATE CSE 2010 \| Question: 9 | **B** |
| `4.8.31` | Circuit Output: GATE CSE 2011 \| Question: 50 | **D** |
| `4.8.32` | Circuit Output: GATE CSE 2011 \| Question: 51 | **B** |
| `4.8.33` | Circuit Output: GATE CSE 2014 \| Set 3 \| Question: 45 | **C** |
| `4.8.34` | Circuit Output: GATE CSE 2025 \| Set 2 \| Question: 21 | **A;B;C** |
| `4.8.35` | Circuit Output: GATE IT 2005 \| Question: 10 | **C** |
| `4.8.36` | Circuit Output: GATE IT 2005 \| Question: 43 | **X** |
| `4.8.37` | Circuit Output: GATE IT 2006 \| Question: 36 | **D** |
| `4.8.38` | Circuit Output: GATE IT 2007 \| Question: 38 | **C** |
| `4.8.39` | Circuit Output: GATE IT 2007 \| Question: 40 | **A** |
| `4.8.40` | Circuit Output: GATE IT 2007 \| Question: 45 | **D** |
| `4.9.1` | Combinational Circuit: GATE CSE 2022 \| Question: 30 | **C** |
| `4.9.2` | Combinational Circuit: GATE CSE 2024 \| Set 1 \| Question: 18 | **A;C** |
| `4.10.1` | Conjunctive Normal Form: GATE CSE 2007 \| Question: 48 | **A** |
| `4.11.1` | Decoder: GATE CSE 2007 \| Question: 8, ISRO2011-31 | **C** |
| `4.11.2` | Decoder: GATE CSE 2020 \| Question: 20 | **1034** |
| `4.11.3` | Decoder: GATE IT 2008 \| Question: 9 | **B** |
| `4.12.1` | Digital Circuits: GATE CSE 1996 \| Question: 5 | **N/A** |
| `4.12.2` | Digital Circuits: GATE CSE 2002 \| Question: 7 | **N/A** |
| `4.12.3` | Digital Circuits: GATE CSE 2003 \| Question: 47 | **D** |
| `4.12.4` | Digital Circuits: GATE CSE 2011 \| Question: 13 | **D** |
| `4.12.5` | Digital Circuits: GATE CSE 2013 \| Question: 5 | **A** |
| `4.12.6` | Digital Circuits: GATE CSE 2014 \| Set 3 \| Question: 8 | **C** |
| `4.12.7` | Digital Circuits: GATE CSE 2026 \| Set 2 \| Question: 49 | **6:6** |
| `4.13.1` | Digital Counter: GATE CSE 1987 \| Question: 1-III | **C** |
| `4.13.2` | Digital Counter: GATE CSE 1987 \| Question: 10c | **N/A** |
| `4.13.3` | Digital Counter: GATE CSE 1990 \| Question: 5-c | **N/A** |
| `4.13.4` | Digital Counter: GATE CSE 1991 \| Question: 5-c | **33.33** |
| `4.13.5` | Digital Counter: GATE CSE 1994 \| Question: 2-1 | **N/A** |
| `4.13.6` | Digital Counter: GATE CSE 2002 \| Question: 8 | **N/A** |
| `4.13.7` | Digital Counter: GATE CSE 2011 \| Question: 15 | **A** |
| `4.13.8` | Digital Counter: GATE CSE 2014 \| Set 2 \| Question: 7 | **C** |
| `4.13.9` | Digital Counter: GATE CSE 2015 \| Set 1 \| Question: 20 | **D** |
| `4.13.10` | Digital Counter: GATE CSE 2015 \| Set 2 \| Question: 7 | **3** |
| `4.13.11` | Digital Counter: GATE CSE 2016 \| Set 1 \| Question: 8 | **3:4** |
| `4.13.12` | Digital Counter: GATE CSE 2017 \| Set 2 \| Question: 42 | **B** |
| `4.13.13` | Digital Counter: GATE CSE 2021 \| Set 1 \| Question: 28 | **A** |
| `4.13.14` | Digital Counter: GATE CSE 2023 \| Question: 33 | **A** |
| `4.13.15` | Digital Counter: GATE CSE 2026 \| Set 1 \| Question: 27 | **B** |
| `4.13.16` | Digital Counter: GATE IT 2005 \| Question: 11 | **D** |
| `4.13.17` | Digital Counter: GATE IT 2008 \| Question: 37 | **D** |
| `4.13.18` | Digital Counter: GATE1992-04-c | **N/A** |
| `4.14.1` | Dual Function: GATE CSE 2014 \| Set 2 \| Question: 6 | **D** |
| `4.15.1` | Finite State Machines: GATE CSE 1994 \| Question: 3.3 | **True** |
| `4.15.2` | Finite State Machines: GATE CSE 1995 \| Question: 2.23 | **B** |
| `4.15.3` | Finite State Machines: GATE CSE 1996 \| Question: 2.23 | **B** |
| `4.15.4` | Finite State Machines: GATE CSE 2009 \| Question: 27 | **A** |
| `4.16.1` | Fixed Point Representation (2) | **D** |
| `4.16.2` | Fixed Point Representation: GATE CSE 2018 \| Question: 33 | **C** |
| `4.17.1` | Flip Flop: GATE CSE 2001 \| Question: 11 | **N/A** |
| `4.17.2` | Flip Flop: GATE CSE 2004 \| Question: 18, ISRO2007-31 | **C** |
| `4.17.3` | Flip Flop: GATE CSE 2015 \| Set 1 \| Question: 37 | **A** |
| `4.17.4` | Flip Flop: GATE CSE 2017 \| Set 1 \| Question: 33 | **B** |
| `4.17.5` | Flip Flop: GATE CSE 2018 \| Question: 22 | **2** |
| `4.17.6` | Flip Flop: GATE CSE 2025 \| Set 1 \| Question: 50 | **7:8** |
| `4.17.7` | Flip Flop: GATE IT 2007 \| Question: 7 | **D** |
| `4.18.1` | Floating Point Representation: GATE CSE 1987 \| Question: 1-vii | **C** |
| `4.18.2` | Floating Point Representation: GATE CSE 1989 \| Question: 1-vi | **N/A** |
| `4.18.3` | Floating Point Representation: GATE CSE 1990 \| Question: 1-iv-a | **N/A** |
| `4.18.4` | Floating Point Representation: GATE CSE 1990 \| Question: 1-iv-b | **N/A** |
| `4.18.5` | Floating Point Representation: GATE CSE 1997 \| Question: 72 | **N/A** |
| `4.18.6` | Floating Point Representation: GATE CSE 2003 \| Question: 43 | **C** |
| `4.18.7` | Floating Point Representation: GATE CSE 2005 \| Question: 85-a | **D** |
| `4.18.8` | Floating Point Representation: GATE CSE 2005 \| Question: 85-b | **D** |
| `4.19.1` | Functional Completeness: GATE CSE 1989 \| Question: 4-iii | **N/A** |
| `4.19.2` | Functional Completeness: GATE CSE 1992 \| Question: 02-ii | **B;C** |
| `4.19.3` | Functional Completeness: GATE CSE 1993 \| Question: 9 | **N/A** |
| `4.19.4` | Functional Completeness: GATE CSE 1998 \| Question: 5 | **N/A** |
| `4.19.5` | Functional Completeness: GATE CSE 1999 \| Question: 2.9 | **B;C** |
| `4.19.6` | Functional Completeness: GATE CSE 2015 \| Set 1 \| Question: 39 | **B** |
| `4.19.7` | Functional Completeness: GATE IT 2008 \| Question: 1 | **A** |
| `4.20.1` | IEEE Representation: GATE CSE 2008 \| Question: 4 | **D** |
| `4.20.2` | IEEE Representation: GATE CSE 2012 \| Question: 7 | **B** |
| `4.20.3` | IEEE Representation: GATE CSE 2014 \| Set 2 \| Question: 45 | **A** |
| `4.20.4` | IEEE Representation: GATE CSE 2017 \| Set 2 \| Question: 12 | **C** |
| `4.20.5` | IEEE Representation: GATE CSE 2020 \| Question: 29 | **B** |
| `4.20.6` | IEEE Representation: GATE CSE 2021 \| Set 1 \| Question: 24 | **-7.75** |
| `4.20.7` | IEEE Representation: GATE CSE 2021 \| Set 2 \| Question: 4 | **C** |
| `4.20.8` | IEEE Representation: GATE CSE 2022 \| Question: 31 | **B** |
| `4.20.9` | IEEE Representation: GATE CSE 2023 \| Question: 35 | **C** |
| `4.20.10` | represented in the | **B** |
| `4.20.11` | IEEE Representation: GATE CSE 2025 \| Set 2 \| Question: 39 | **A;B;C** |
| `4.20.12` | IEEE Representation: GATE CSE 2026 \| Set 1 \| Question: 26 | **C** |
| `4.20.13` | IEEE Representation: GATE CSE 2026 \| Set 2 \| Question: 24 | **-60.25:-60.25** |
| `4.20.14` | IEEE Representation: GATE IT 2008 \| Question: 7 | **C** |
| `4.21.1` | K Map: GATE CSE 1987 \| Question: 16-a | **D** |
| `4.21.2` | K Map: GATE CSE 1988 \| Question: 3a-b | **N/A** |
| `4.21.3` | K Map: GATE CSE 1992 \| Question: 01-i | **N/A** |
| `4.21.4` | K Map: GATE CSE 1995 \| Question: 15-b | **N/A** |
| `4.21.5` | K Map: GATE CSE 1996 \| Question: 2.24 | **C** |
| `4.21.6` | K Map: GATE CSE 1998 \| Question: 2.7 | **C** |
| `4.21.7` | K Map: GATE CSE 1999 \| Question: 1.8 | **B** |
| `4.21.8` | K Map: GATE CSE 2000 \| Question: 2.11 | **D** |
| `4.21.9` | K Map: GATE CSE 2001 \| Question: 1.11 | **A** |
| `4.21.10` | K Map: GATE CSE 2002 \| Question: 1.12 | **B** |
| `4.21.11` | K Map: GATE CSE 2003 \| Question: 45 | **C** |
| `4.21.12` | K Map: GATE CSE 2008 \| Question: 5 | **A** |
| `4.21.13` | K Map: GATE CSE 2012 \| Question: 30 | **B** |
| `4.21.14` | K Map: GATE CSE 2025 \| Set 2 \| Question: 33 | **A;D** |
| `4.21.15` | map. | **D** |
| `4.21.16` | K Map: GATE IT 2007 \| Question: 78 | **A** |
| `4.21.17` | K Map: GATE IT 2007 \| Question: 79 | **C** |
| `4.22.1` | Little Endian Big Endian: GATE CSE 2021 \| Set 2 \| Question: 44 | **A;D** |
| `4.23.1` | Memory Interfacing: GATE CSE 1995 \| Question: 2.2 | **C** |
| `4.23.2` | Memory Interfacing: GATE CSE 2009 \| Question: 7, ISRO2015-3 | **C** |
| `4.23.3` | Memory Interfacing: GATE CSE 2010 \| Question: 7 | **B** |
| `4.23.4` | Memory Interfacing: GATE CSE 2013 \| Question: 46 | **B** |
| `4.23.5` | Memory Interfacing: GATE IT 2005 \| Question: 9 | **C** |
| `4.24.1` | Min No Gates: GATE CSE 1995 \| Question: 15-a | **N/A** |
| `4.24.2` | Min No Gates: GATE CSE 2000 \| Question: 9 | **N/A** |
| `4.24.3` | Min No Gates: GATE CSE 2004 \| Question: 58 | **B** |
| `4.24.4` | Min No Gates: GATE CSE 2009 \| Question: 6 | **B** |
| `4.24.5` | Min No Gates: GATE CSE 2017 \| Set 1 \| Question: 21 | **1** |
| `4.24.6` | Min No Gates: GATE IT 2004 \| Question: 8 | **B** |
| `4.25.1` | Min Products of Sum Form: GATE CSE 1990 \| Question: 5-a | **N/A** |
| `4.25.2` | Min Products of Sum Form: GATE CSE 2017 \| Set 2 \| Question: 28 | **A** |
| `4.26.1` | Min Sum of Products Form: GATE CSE 1991 \| Question: 5-b | **N/A** |
| `4.26.2` | Min Sum of Products Form: GATE CSE 1997 \| Question: 71 | **9** |
| `4.26.3` | Min Sum of Products Form: GATE CSE 2001 \| Question: 10 | **N/A** |
| `4.26.4` | Min Sum of Products Form: GATE CSE 2005 \| Question: 18 | **A** |
| `4.26.5` | Min Sum of Products Form: GATE CSE 2007 \| Question: 9 | **B** |
| `4.26.6` | Min Sum of Products Form: GATE CSE 2011 \| Question: 14 | **B** |
| `4.26.7` | Min Sum of Products Form: GATE CSE 2014 \| Set 1 \| Question: 45 | **A** |
| `4.26.8` | Min Sum of Products Form: GATE CSE 2014 \| Set 1 \| Question: 7 | **A** |
| `4.26.9` | Min Sum of Products Form: GATE CSE 2014 \| Set 3 \| Question: 7 | **B** |
| `4.26.10` | Min Sum of Products Form: GATE CSE 2018 \| Question: 49 | **3** |
| `4.26.11` | Min Sum of Products Form: GATE CSE 2021 \| Set 2 \| Question: 52 | **6** |
| `4.26.12` | Min Sum of Products Form: GATE CSE 2024 \| Set 1 \| Question: 37 | **A;B** |
| `4.26.13` | Min Sum of Products Form: GATE CSE 2025 \| Set 1 \| Question: 32 | **A** |
| `4.26.14` | Min Sum of Products Form: GATE CSE 2026 \| Set 1 \| Question: 38 | **B;D** |
| `4.26.15` | Min Sum of Products Form: GATE CSE 2026 \| Set 2 \| Question: 30 | **B** |
| `4.26.16` | Min Sum of Products Form: GATE IT 2008 \| Question: 8 | **A** |
| `4.27.1` | Multiplexer: GATE CSE 1990 \| Question: 5-b | **N/A** |
| `4.27.2` | Multiplexer: GATE CSE 1998 \| Question: 1.14 | **C** |
| `4.27.3` | Multiplexer: GATE CSE 2001 \| Question: 2.11 | **C** |
| `4.27.4` | Multiplexer: GATE CSE 2004 \| Question: 60 | **A** |
| `4.27.5` | Multiplexer: GATE CSE 2007 \| Question: 34 | **C** |
| `4.27.6` | Multiplexer: GATE CSE 2016 \| Set 1 \| Question: 30 | **D** |
| `4.27.7` | Multiplexer: GATE CSE 2020 \| Question: 19 | **5** |
| `4.27.8` | Multiplexer: GATE CSE 2021 \| Set 2 \| Question: 5 | **A** |
| `4.27.9` | Multiplexer: GATE CSE 2023 \| Question: 11 | **B** |
| `4.27.10` | Multiplexer: GATE CSE 2023 \| Question: 34 | **C** |
| `4.27.11` | Multiplexer: GATE CSE 2024 \| Set 1 \| Question: 54 | **4** |
| `4.27.12` | Multiplexer: GATE IT 2005 \| Question: 48 | **D** |
| `4.27.13` | Multiplexer: GATE IT 2007 \| Question: 8 | **A** |
| `4.27.14` | Multiplexer: GATE1992-04-b | **N/A** |
| `4.28.1` | Number Representation: GATE CSE 1990 \| Question: 1-viii | **N/A** |
| `4.28.2` | Number Representation: GATE CSE 1991 \| Question: 01-iii | **9** |
| `4.28.3` | Number Representation: GATE CSE 1991 \| Question: 01-v | **N/A** |
| `4.28.4` | Number Representation: GATE CSE 1992 \| Question: 4-a | **N/A** |
| `4.28.5` | Number Representation: GATE CSE 1993 \| Question: 6.5 | **N/A** |
| `4.28.6` | Number Representation: GATE CSE 1994 \| Question: 2.7 | **N/A** |
| `4.28.7` | Number Representation: GATE CSE 1995 \| Question: 18 | **N/A** |
| `4.28.8` | Number Representation: GATE CSE 1995 \| Question: 2.12, ISRO2015-9 | **C** |
| `4.28.9` | Number Representation: GATE CSE 1996 \| Question: 1.25 | **D** |
| `4.28.10` | Number Representation: GATE CSE 1997 \| Question: 5.4 | **C** |
| `4.28.11` | Number Representation: GATE CSE 1998 \| Question: 1.17 | **D** |
| `4.28.12` | Number Representation: GATE CSE 1998 \| Question: 2.20 | **C** |
| `4.28.13` | Number Representation: GATE CSE 1999 \| Question: 2.17 | **A;C** |
| `4.28.14` | Number Representation: GATE CSE 2000 \| Question: 1.6 | **C** |
| `4.28.15` | Number Representation: GATE CSE 2000 \| Question: 2.14 | **B** |
| `4.28.16` | Number Representation: GATE CSE 2001 \| Question: 2.10 | **C** |
| `4.28.17` | Number Representation: GATE CSE 2002 \| Question: 1.14 | **B** |
| `4.28.18` | Number Representation: GATE CSE 2002 \| Question: 1.15 | **D** |
| `4.28.19` | Number Representation: GATE CSE 2002 \| Question: 1.16 | **D** |
| `4.28.20` | Number Representation: GATE CSE 2002 \| Question: 1.21 | **B** |
| `4.28.21` | Number Representation: GATE CSE 2002 \| Question: 9 | **N/A** |
| `4.28.22` | Number Representation: GATE CSE 2003 \| Question: 9 | **A** |
| `4.28.23` | Number Representation: GATE CSE 2004 \| Question: 19 | **D** |
| `4.28.24` | Number Representation: GATE CSE 2004 \| Question: 28 | **A** |
| `4.28.25` | Number Representation: GATE CSE 2004 \| Question: 66 | **A** |
| `4.28.26` | Number Representation: GATE CSE 2005 \| Question: 16, ISRO2009-18, ISRO2015-2 | **A** |
| `4.28.27` | Number Representation: GATE CSE 2005 \| Question: 17 | **A** |
| `4.28.28` | Number Representation: GATE CSE 2006 \| Question: 39 | **B** |
| `4.28.29` | Number Representation: GATE CSE 2008 \| Question: 6 | **D** |
| `4.28.30` | Number Representation: GATE CSE 2009 \| Question: 5, ISRO2017-57 | **B** |
| `4.28.31` | Number Representation: GATE CSE 2010 \| Question: 8 | **A** |
| `4.28.32` | Number Representation: GATE CSE 2013 \| Question: 4 | **B** |
| `4.28.33` | Number Representation: GATE CSE 2014 \| Set 1 \| Question: 8 | **5** |
| `4.28.34` | Number Representation: GATE CSE 2014 \| Set 2 \| Question: 8 | **3** |
| `4.28.35` | Number Representation: GATE CSE 2015 \| Set 3 \| Question: 35 | **5** |
| `4.28.36` | Number Representation: GATE CSE 2016 \| Set 1 \| Question: 07 | **-11** |
| `4.28.37` | Number Representation: GATE CSE 2016 \| Set 2 \| Question: 09 | **1** |
| `4.28.38` | Number Representation: GATE CSE 2017 \| Set 1 \| Question: 9 | **C** |
| `4.28.39` | Number Representation: GATE CSE 2017 \| Set 2 \| Question: 1 | **D** |
| `4.28.40` | Number Representation: GATE CSE 2019 \| Question: 22 | **0.502** |
| `4.28.41` | Number Representation: GATE CSE 2019 \| Question: 4 | **C** |
| `4.28.42` | Number Representation: GATE CSE 2019 \| Question: 8 | **C** |
| `4.28.43` | Number Representation: GATE CSE 2021 \| Set 1 \| Question: 6 | **A** |
| `4.28.44` | Number Representation: GATE CSE 2021 \| Set 2 \| Question: 18 | **3** |
| `4.28.45` | Number Representation: GATE CSE 2022 \| Question: 8 | **B** |
| `4.28.46` | Number Representation: GATE CSE 2023 \| Question: 22 | **110** |
| `4.28.47` | Number Representation: GATE CSE 2024 \| Set 1 \| Question: 3 | **B** |
| `4.28.48` | Number Representation: GATE CSE 2024 \| Set 2 \| Question: 39 | **A;B;D** |
| `4.28.49` | Number Representation: GATE CSE 2025 \| Set 1 \| Question: 15 | **B;D** |
| `4.28.50` | Number Representation: GATE CSE 2026 \| Set 1 \| Question: 12 | **B;C** |
| `4.28.51` | Number Representation: GATE CSE 2026 \| Set 2 \| Question: 18 | **B;D** |
| `4.28.52` | Number Representation: GATE IT 2004 \| Question: 42 | **B** |
| `4.28.53` | Number Representation: GATE IT 2004 \| Question: 43 | **A** |
| `4.28.54` | Number Representation: GATE IT 2005 \| Question: 47 | **A** |
| `4.28.55` | Number Representation: GATE IT 2006 \| Question: 7, ISRO2009-41 | **C** |
| `4.28.56` | Number Representation: GATE IT 2007 \| Question: 42 | **A** |
| `4.28.57` | Number Representation: GATE IT 2008 \| Question: 15 | **B** |
| `4.29.1` | Number System: GATE CSE 1988 \| Question: 2-vi | **12** |
| `4.30.1` | Prime Implicants: GATE CSE 1997 \| Question: 5.1 | **C** |
| `4.30.2` | Prime Implicants: GATE CSE 2004 \| Question: 59 | **A** |
| `4.31.1` | ROM: GATE CSE 1993 \| Question: 6.6 | **N/A** |
| `4.31.2` | ROM: GATE CSE 1996 \| Question: 1.21 | **D** |
| `4.31.3` | ROM: GATE CSE 2012 \| Question: 19 | **D** |
| `4.31.4` | ROM: GATE IT 2004 \| Question: 10 | **B** |
| `4.32.1` | Reduction: GATE CSE 2026 \| Set 1 \| Question: 11 | **A;C** |
| `4.33.1` | Ripple Counter Operation: GATE CSE 2025 \| Set 2 \| Question: 24 | **250:250** |
| `4.34.1` | microseconds, then the | **D** |
| `4.34.2` | Shift Registers: GATE CSE 1991 \| Question: 06,a | **N/A** |
| `4.35.1` | Static Hazard: GATE CSE 2006 \| Question: 38 | **D** |
| `4.36.1` | Synchronous Asynchronous Circuits: GATE CSE 1991 \| Question: 03-ii | **B** |
| `4.36.2` | Synchronous Asynchronous Circuits: GATE CSE 1998 \| Question: 16 | **N/A** |
| `4.36.3` | Synchronous Asynchronous Circuits: GATE CSE 2001 \| Question: 2.12 | **B** |
| `4.36.4` | Synchronous Asynchronous Circuits: GATE CSE 2003 \| Question: 44 | **A** |

