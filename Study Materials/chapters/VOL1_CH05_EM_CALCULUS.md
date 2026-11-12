# Volume 1 — Chapter 5: Engineering Mathematics: Calculus

- **Source PDF**: [filter1_volume1.pdf](file:///Users/adityaasaha/Documents/Academics/Gate/filter1_volume1.pdf)
- **Total GATE Questions in Chapter**: **69**

---

## 1. Subtopic Weightage & Question Distribution

| Subtopic # | Subtopic Name | Questions |
| :---: | :--- | :---: |
| **5.1** | Continuity | 11 |
| **5.3** | Differentiation | 11 |
| **5.5** | Limits | 15 |
| **5.6** | Maxima Minima | 14 |
| **5.7** | Polynomials | 2 |
| **5.8** | Summation | 1 |


---

## 2. Comprehensive GATE CSE Calculus Reference (Expanded Research & Formulas)

### 2.1 Limits & Standard Expansions
- **Standard Limits ($x \rightarrow 0$)**:
  $$\lim_{x \to 0} \frac{\sin x}{x} = 1, \quad \lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2}, \quad \lim_{x \to 0} \frac{e^x - 1}{x} = 1, \quad \lim_{x \to 0} \frac{\ln(1+x)}{x} = 1$$
  $$\lim_{x \to 0} (1 + x)^{1/x} = e, \qquad \lim_{n \to \infty} \left(1 + \frac{k}{n}\right)^{m n} = e^{km}$$
- **1^\infty Indeterminate Form Shortcut**: If $\lim_{x \to a} f(x) = 1$ and $\lim_{x \to a} g(x) = \infty$, then:
  $$\lim_{x \to a} \big(f(x)\big)^{g(x)} = \exp\!\left( \lim_{x \to a} g(x)\big(f(x) - 1\big) \right)$$
- **Taylor / Maclaurin Series ($x \rightarrow 0$)**:
  - $e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots$
  - $\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots$
  - $\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots$
  - $\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \dots$
- **L'Hôpital's Rule**: For $0/0$ or $\infty/\infty$, $\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$ (if the latter exists).

### 2.2 Continuity, Differentiability & Mean Value Theorems
- **Differentiability $\implies$ Continuity**, but **Continuity $\not\implies$ Differentiability** (e.g., $|x|$ at $x = 0$).
- **Rolle's Theorem**: If $f$ is continuous on $[a, b]$, differentiable on $(a, b)$, and $f(a) = f(b)$, there exists $c \in (a, b)$ such that $f'(c) = 0$.
- **Lagrange's Mean Value Theorem (LMVT)**: If $f$ is continuous on $[a, b]$ and differentiable on $(a, b)$, there exists $c \in (a, b)$ such that:
  $$f'(c) = \frac{f(b) - f(a)}{b - a}$$

### 2.3 Maxima and Minima
- **Single Variable $f(x)$**:
  1. Find critical points where $f'(x) = 0$ or $f'(x)$ is undefined.
  2. **Second Derivative Test**:
     - $f''(c) > 0 \implies$ **Local Minimum** at $x = c$.
     - $f''(c) < 0 \implies$ **Local Maximum** at $x = c$.
     - $f''(c) = 0 \implies$ Test higher derivatives: if first non-zero derivative $f^{(k)}(c)$ has **even** $k$, extremum; if **odd** $k$, **point of inflection**.
  3. **Global Max/Min on Closed Interval $[a, b]$**: Always evaluate $f(x)$ at all critical points inside $(a, b)$ **AND at the endpoints $a$ and $b$**!
- **Two Variables $f(x, y)$**:
  - Stationary point: $f_x = 0, f_y = 0$. Let $r = f_{xx}, s = f_{xy}, t = f_{yy}$, and $\Delta = rt - s^2$:
    - $\Delta > 0$ and $r > 0 \implies$ Local Minimum.
    - $\Delta > 0$ and $r < 0 \implies$ Local Maximum.
    - $\Delta < 0 \implies$ Saddle Point.

### 2.4 Definite Integrals & Leibniz Rule
- **Key Definite Integral Properties**:
  - $\int_{a}^{b} f(x)\,dx = \int_{a}^{b} f(a + b - x)\,dx$
  - $\int_{-a}^{a} f(x)\,dx = \begin{cases} 0 & \text{if } f(-x) = -f(x) \text{ (odd)} \\ 2\int_{0}^{a} f(x)\,dx & \text{if } f(-x) = f(x) \text{ (even)} \end{cases}$
- **Leibniz Rule (Differentiating under the Integral Sign)**:
  $$\frac{d}{dx} \left( \int_{u(x)}^{v(x)} f(t)\,dt \right) = f(v(x)) \cdot v'(x) - f(u(x)) \cdot u'(x)$$

---

## 3. Original PDF Chapter Notes (Preserved Verbatim)

5 Engineering Mathematics: Calculus (69)
Syllabus: Limits, Continuity, and Differentiability, Maxima and minima, Mean value theorem, Integration.
Welcome to the "Engineering Mathematics: Calculus" chapter, a cornerstone of your GATE Computer Science
preparation. This section is designed as a comprehensive, exam-focused reference to equip you with the essential
concepts, formulas, and problem-solving strategies required to excel in the calculus portion of the GATE exam.
Calculus is not merely a collection of mathematical techniques; it is the language of change and optimization,
fundamental to understanding algorithms, data structures, probability, and various computational models. A solid grasp
of calculus concepts will not only help you score well in the dedicated Engineering Mathematics section but also
enhance your analytical abilities for other subjects. Typically, Engineering Mathematics accounts for 8-10% of the total
GATE marks, with Calculus being a significant component of this weightage. Questions usually range from direct
application of formulas and theorems to conceptual problems involving limits, continuity, differentiation, and integration,
often requiring a blend of analytical reasoning and careful calculation. Expect a mix of Multiple Choice Questions
(MCQ), Multiple Select Questions (MSQ), and Numerical Answer Type (NAT) questions.
Topic-wise Key Concepts
Limits
Definition and Core Idea: A limit describes the behavior of a function as its input approaches a certain value. It tells us
what value the function 'tends to' or 'approaches' as the independent variable gets arbitrarily close to a specific point,
without necessarily reaching it.
Important Formulas, Theorems, and Results:
1. Algebra of Limits: If and , then:
, provided
2. Standard Limits:
3. L'Hopital's Rule: If is of the indeterminate form or , then , provided
the latter limit exists. This can be applied repeatedly.
4. Squeeze Theorem (Sandwich Theorem): If for all in an open interval containing (except
possibly at itself), and if and , then .
Key Properties and Identities:
Indeterminate forms: algebraic manipulation.
. These require special techniques like L'Hopital's Rule or

*(PDF Page 129)*

One-sided limits: For a limit to exist, the left-hand limit ( ) and the right-hand limit ( ) must
be equal.
Common Pitfalls or Tricky Points:
Applying L'Hopital's Rule when the limit is not an indeterminate form.
Incorrectly handling one-sided limits, especially for piecewise functions or functions with square roots.
Errors in algebraic simplification before applying standard limits.
Misinterpreting limits involving infinity (e.g., , but is indeterminate).
Standard Problem-Solving Techniques or Shortcuts:
Direct Substitution: Always try this first. If it yields a finite value, that's the limit.
Factorization and Cancellation: For forms involving polynomials, factorize the numerator and denominator to
cancel common terms.
Rationalization: For expressions involving square roots, multiply by the conjugate to simplify.
Using Standard Limits: Manipulate the expression to fit one of the standard limit forms.
L'Hopital's Rule: Apply for or forms. Remember to differentiate numerator and denominator separately.
Transforming Indeterminate Forms:
or
combine terms, rationalize, or find a common denominator.
take natural logarithm: If , then . Then find and
exponentiate the result.
Continuity
Definition and Core Idea: A function is continuous at a point if its graph has no breaks, jumps, or holes at that point.
Informally, you can draw the graph without lifting your pen. Formally, it means the function's value at the point is equal
to its limit as the input approaches that point.
Important Formulas, Theorems, and Results:
1. Conditions for Continuity at a Point : A function is continuous at conditions are met:
a. is defined (the function exists at ).
b. exists (the limit exists at ). This implies .
c. (the limit equals the function value).
2. Continuity on an Interval: A function is continuous on an open interval interval. It is continuous on a closed interval if it is continuous on ), and continuous from the left at ( ).
3. Intermediate Value Theorem (IVT): If is continuous on the closed interval and , then there exists at least one number in such that .
4. Extreme Value Theorem (EVT): If is continuous on a closed interval , then maximum value and an absolute minimum value on that interval.
if and only if all three
if it is continuous at every point in the
, continuous from the right at (
and is any number between
attains both an absolute
Key Properties and Identities:
The sum, difference, product, and quotient (where the denominator is non-zero) of continuous functions are
continuous.
The composition of continuous functions is continuous: If is continuous at and is continuous at , then
is continuous at .
Polynomials, exponential functions ( ), logarithmic functions ( ), trigonometric functions (
), and rational functions (where the denominator is non-zero) are continuous in their domains.
Common Pitfalls or Tricky Points:
Piecewise Functions: Pay close attention to the points where the definition of the function changes. These are the
critical points to check for continuity.
Removable Discontinuities: Occur when exists but is not equal to , or is undefined (e.g.,
holes in the graph).
Jump Discontinuities: Occur when the left-hand and right-hand limits exist but are not equal (e.g., step functions).

*(PDF Page 130)*

Infinite Discontinuities: Occur when one or both of the one-sided limits are infinite (e.g., vertical asymptotes).
Forgetting to check all three conditions for continuity.
Standard Problem-Solving Techniques or Shortcuts:
For piecewise functions, evaluate the function value at the transition point, and calculate both the left-hand and right-
hand limits at that point. Equate them to find unknown constants.
Identify the domain of the function first. Discontinuities often occur at points where the function is undefined (e.g.,
denominator is zero, negative under square root).
For functions involving absolute values, rewrite them as piecewise functions.
Differentiation
Definition and Core Idea: Differentiation is the process of finding the derivative of a function. The derivative represents
the instantaneous rate of change of a function with respect to its independent variable. Geometrically, it gives the slope
of the tangent line to the function's graph at a given point.
Important Formulas, Theorems, and Results:
1. Definition of Derivative:
2. Basic Differentiation Rules:
(where is a constant)
3. Rules of Differentiation:
Constant Multiple Rule:
Sum/Difference Rule:
Product Rule:
Quotient Rule:
Chain Rule:
4. Implicit Differentiation: Used when equation with respect to , treating 5. Rolle's Theorem: If is continuous on is not explicitly defined as a function of . Differentiate both sides of the
as a function of (i.e., use the chain rule for terms involving ).
, differentiable on , and , then there exists at least
one such that .
6. Mean Value Theorem (Lagrange's MVT): If is continuous on and differentiable on , then there exists
at least one such that .
7. Cauchy's Mean Value Theorem: If and are continuous on and differentiable on , and for
any , then there exists at least one such that .
Key Properties and Identities:
Differentiability implies continuity, but continuity does not imply differentiability (e.g., at ).

*(PDF Page 131)*

Higher-order derivatives: , , etc.
Common Pitfalls or Tricky Points:
Forgetting the chain rule, especially with composite functions like or .
Errors in applying the product or quotient rule.
Mistakes in implicit differentiation, particularly when differentiating terms involving Confusing the derivative of with .
Not simplifying expressions before differentiating when possible.
(e.g., ).
Standard Problem-Solving Techniques or Shortcuts:
Logarithmic Differentiation: For functions of the form natural logarithm of both sides before differentiating implicitly.
Parametric Differentiation: If and , then .
or complex products/quotients, take the
Derivative of Inverse Function: If , then .
Practice recognizing common derivative patterns for speed.
Maxima Minima
Definition and Core Idea: Maxima and minima (collectively called extrema) refer to the highest and lowest values a
function attains within a given interval or its entire domain. A local maximum/minimum is the highest/lowest point in its
immediate neighborhood, while a global (absolute) maximum/minimum is the highest/lowest point over the entire
domain/interval.
Important Formulas, Theorems, and Results:
1. Critical Points: A critical point of a function is a point in the domain of where either undefined. Local extrema can only occur at critical points or endpoints of a closed interval.
2. First Derivative Test: Let be a critical point of a continuous function .
If changes from positive to negative at , then has a local maximum at .
If changes from negative to positive at , then has a local minimum at .
If does not change sign at , then has neither a local maximum nor a local minimum at .
3. Second Derivative Test: Let be a critical point where and exists.
If , then has a local minimum at .
If , then has a local maximum at .
If , the test is inconclusive (use the First Derivative Test).
4. Concavity:
If on an interval, is concave up (graph opens upwards).
If on an interval, is concave down (graph opens downwards).
5. Inflection Point: A point where the concavity of the function changes. This occurs where undefined, and changes sign.
or is
or is
Key Properties and Identities:
For global extrema on a closed interval , evaluate at all critical points in and at the endpoints . The largest of these values is the absolute maximum, and the smallest is the absolute minimum.
and
Common Pitfalls or Tricky Points:
Forgetting to check endpoints when finding global extrema on a closed interval.
Misinterpreting the results of the second derivative test, especially when .
Not considering points where is undefined as critical points.
Errors in algebraic manipulation while finding critical points or second derivatives.
Confusing local extrema with global extrema.
Standard Problem-Solving Techniques or Shortcuts:
Optimization Problems:
1. Understand the problem and identify the quantity to be maximized or minimized.

*(PDF Page 132)*

2. Draw a diagram if helpful.
3. Introduce variables and write the primary equation for the quantity to be optimized.
4. Write a secondary equation (constraint) relating the variables.
5. Use the secondary equation to express the primary equation in terms of a single independent variable.
6. Find the domain of this function.
7. Differentiate the function, find critical points, and apply the First or Second Derivative Test.
8. Verify the solution makes sense in the context of the problem.
For simple functions, sometimes the graph can quickly indicate extrema.
Integration
Definition and Core Idea: Integration is the reverse process of differentiation, also known as antidifferentiation. It finds
the function whose derivative is the given function. Geometrically, definite integration calculates the area under the
curve of a function between two specified limits.
Important Formulas, Theorems, and Results:
1. Basic Integration Formulas (Indefinite Integrals):
, for
2. Properties of Indefinite Integrals:
3. Integration by Substitution (u-substitution): If , then . .
4. Integration by Parts: . Often remembered by the mnemonic "LIATE" (Logarithmic, Inverse
trig, Algebraic, Trigonometric, Exponential) for choosing .
Key Properties and Identities:
Always include the constant of integration for indefinite integrals.
Trigonometric identities are often crucial for simplifying integrands before integration.
Common Pitfalls or Tricky Points:
Forgetting the constant of integration .
Incorrectly choosing and in integration by parts.
Errors in algebraic manipulation or trigonometric identities.
Not recognizing when substitution is appropriate.
Confusing integration formulas with differentiation formulas (e.g., vs. ).
Standard Problem-Solving Techniques or Shortcuts:
Direct Integration: If the integrand matches a basic formula.
Substitution: Look for a function and its derivative within the integrand. Let the inner function be .
Integration by Parts: Use for products of functions (e.g., ).
Partial Fractions: For rational functions (polynomials divided by polynomials), decompose into simpler fractions that
are easier to integrate. (Briefly mention as it's a common technique).

*(PDF Page 133)*

Trigonometric Identities: Use identities to simplify powers of trig functions or products of trig functions.
Definite Integral
Definition and Core Idea: A definite integral represents the net signed area between the graph of a function and the x-
axis over a specified interval . It is evaluated by finding the antiderivative of the function and then evaluating it at
the upper and lower limits of integration.
Important Formulas, Theorems, and Results:
1. Fundamental Theorem of Calculus (Part 1): If is continuous on , then the function has
a derivative at every point in , and .
2. Fundamental Theorem of Calculus (Part 2): If is continuous on and is any antiderivative of on ,
then .
3. Properties of Definite Integrals:
, where
(useful for simplifying integrals)
Even/Odd Functions:
If is an even function ( ), then .
If is an odd function ( ), then .
Key Properties and Identities:
The definite integral evaluates to a numerical value, not a function.
The constant of integration is not included in definite integrals because it cancels out (
).
Common Pitfalls or Tricky Points:
Incorrectly applying the limits of integration (upper limit minus lower limit).
Sign errors when evaluating .
Forgetting to change the limits of integration when using substitution for definite integrals.
Not recognizing even/odd function properties to simplify integrals over symmetric intervals.
Improper integrals (involving infinite limits or discontinuities within the interval) are less common in GATE CS but
good to be aware of.
Standard Problem-Solving Techniques or Shortcuts:
Direct Application of FTC: Find the antiderivative and evaluate at the limits.
Substitution: If using substitution, either change the limits of integration to be in terms of or revert back to
before applying the original limits.
Properties of Definite Integrals: Use properties like linearity, interval splitting, and even/odd function rules to
simplify the integral before evaluation.
Symmetry: For integrals over , check if the integrand is even or odd.
Polynomials
Definition and Core Idea: A polynomial is an expression consisting of variables and coefficients, involving only the
operations of addition, subtraction, multiplication, and non-negative integer exponents of variables. They are
fundamental building blocks in calculus as they are continuous and differentiable everywhere.
Important Formulas, Theorems, and Results:
1. General Form: integer (degree).
2. Remainder Theorem: If a polynomial , where are coefficients and is a non-negative
is divided by , the remainder is .

*(PDF Page 134)*

3. Factor Theorem: is a factor of a polynomial if and only if (i.e., is a root of the
polynomial).
4. Fundamental Theorem of Algebra: Every non-constant single-variable polynomial with complex coefficients has at
least one complex root. Consequently, a polynomial of degree has exactly roots (counting multiplicity) in the
complex numbers.
5. Vieta's Formulas (for quadratic and cubic):
For with roots :
For with roots :
Key Properties and Identities:
Polynomials are continuous and infinitely differentiable everywhere.
The degree of a polynomial determines the maximum number of roots it can have.
If a polynomial has real coefficients, then any complex roots must occur in conjugate pairs.
Common Pitfalls or Tricky Points:
Errors in polynomial division or synthetic division.
Misapplying Vieta's formulas (e.g., sign errors).
Not considering multiplicity of roots.
Confusing roots with factors.
Standard Problem-Solving Techniques or Shortcuts:
Synthetic Division: A quick method for dividing a polynomial by a linear factor .
Rational Root Theorem: Helps find potential rational roots of a polynomial with integer coefficients.
Factoring: Look for common factors, use grouping, or quadratic formula for quadratic factors.
Derivative for Repeated Roots: If is a root of with multiplicity , then is also a root of with
multiplicity .
Summation
Definition and Core Idea: Summation is the process of adding a sequence of numbers or terms. It is often represented
using sigma notation ( ). In calculus, summation is foundational to understanding series, Riemann sums (for
integration), and numerical methods.
Important Formulas, Theorems, and Results:
1. Arithmetic Progression (AP) Sum: For an AP with first term , common difference , and terms:
, where is the last term.
2. Geometric Progression (GP) Sum: For a GP with first term , common ratio , and terms:
, for
, for
Sum to Infinity for GP: 3. Standard Summation Formulas:
, for
Key Properties and Identities:
Linearity of Summation:

*(PDF Page 135)*

Telescoping Sums: Sums where intermediate terms cancel out, e.g., .
Common Pitfalls or Tricky Points:
Off-by-one errors in summation limits.
Confusing AP and GP formulas.
Incorrectly applying the sum to infinity formula (only valid for ).
Errors in algebraic manipulation when simplifying complex summations.
Standard Problem-Solving Techniques or Shortcuts:
Identify Series Type: Determine if it's an AP, GP, or a combination.
Use Standard Formulas: Apply the formulas for .
Split and Combine: Use linearity to break down complex summations into simpler ones.
Method of Differences (Telescoping Sums): Express each term as a difference of two consecutive terms to
simplify the sum.
Generating Functions: (Advanced, less common for direct GATE CS questions, but good for understanding
series).
Quick Formula Reference
Limits
L'Hopital's Rule: If is or , then .
Continuity
Continuous at if: defined, exists, and .
Differentiation
Let be functions of , be a constant.

*(PDF Page 136)*

(Chain Rule)
Rolle's Theorem:
Mean Value Theorem:
Maxima Minima
Critical points: or undefined.
First Derivative Test: Sign change of at critical point.
Second Derivative Test: If : local min; local max.
Integration (Indefinite)
, for
Integration by Parts:
Definite Integral
Fundamental Theorem of Calculus: where .
Even function ( ):
Odd function ( ):
Polynomials
Remainder Theorem: divided by has remainder .
Factor Theorem: is a factor of iff .
Vieta's Formulas (for ): , .
Summation
AP Sum: or
GP Sum:
GP Sum to Infinity: for
Important Tips for GATE

*(PDF Page 137)*

1. Master the Fundamentals: Calculus builds upon basic algebra, trigonometry, and functions. Ensure your
foundation in these areas is strong to avoid silly mistakes.
2. Practice with PYQs: Solve previous year's GATE questions extensively. This helps you understand the typical
question patterns, difficulty levels, and time constraints.
3. Understand Concepts, Don't Just Memorize: While formulas are crucial, knowing *why* they work (e.g., the
geometric interpretation of derivatives and integrals) will help you tackle trickier conceptual questions and apply
them correctly in unfamiliar scenarios.
4. Pay Attention to Domains and Conditions: For limits, continuity, and differentiability, always check the domain of
the function and any specific conditions (e.g., for quotient rule, for infinite GP sum). Piecewise
functions are common traps.
5. Be Careful with Signs and Constants: A common source of error in differentiation and integration is incorrect
signs or forgetting the constant of integration ( ) for indefinite integrals. Double-check your calculations.
6. Time Management: Some calculus problems can be lengthy. Learn to identify problems that might take too much
time and mark them for review. Practice solving problems within a strict time limit. Shortcuts like L'Hopital's rule or
properties of definite integrals can save valuable time.
7. Visualize Functions: For problems involving maxima/minima or definite integrals, sketching a rough graph of the
function can often provide intuition and help verify your analytical results.
8. Review Properties of Even/Odd Functions: These properties are frequently tested in definite integral problems,
especially over symmetric intervals like , and can significantly simplify calculations.

---

## 4. Complete Question Index & Answer Key Record (68 Questions)

| Q # | Question Source / Title | Answer Key |
| :---: | :--- | :---: |
| `5.1.1` | Continuity: GATE CSE 1996 \| Question: 3 | **N/A** |
| `5.1.2` | Continuity: GATE CSE 1998 \| Question: 1.4 | **B** |
| `5.1.3` | Continuity: GATE CSE 2007 \| Question: 1 | **A** |
| `5.1.4` | Continuity: GATE CSE 2013 \| Question: 22 | **A** |
| `5.1.5` | Continuity: GATE CSE 2014 \| Set 1 \| Question: 47 | **A** |
| `5.1.6` | Continuity: GATE CSE 2015 \| Set 2 \| Question: 26 | **C** |
| `5.1.7` | Continuity: GATE CSE 2021 \| Set 2 \| Question: 25 | **19** |
| `5.1.8` | Continuity: GATE CSE 2026 \| Set 1 \| Question: 22 | **03** |
| `5.1.9` | Continuity: GATE CSE 2026 \| Set 2 \| Question: 54 | **40:40** |
| `5.1.10` | Continuity: GATE DS&AI 2024 \| Question: 27 | **A** |
| `5.1.11` | Continuity: GATE2010 ME | **C** |
| `5.2.1` | Definite Integral: GATE CSE 2023 \| Question: 21 | **0** |
| `5.2.2` | Definite Integral: GATE CSE 2024 \| Set 2 \| Question: 6 | **B** |
| `5.2.3` | Definite Integral: GATE CSE 2025 \| Set 2 \| Question: 2 | **A** |
| `5.2.4` | Definite Integral: GATE CSE 2026 \| Set 2 \| Question: 17 | **A;C** |
| `5.3.1` | Differentiation: GATE CSE 1996 \| Question: 1.6 | **D** |
| `5.3.2` | Differentiation: GATE CSE 2014 \| Set 1 \| Question: 46 | **-2** |
| `5.3.3` | Differentiation: GATE CSE 2014 \| Set 1 \| Question: 6 | **C** |
| `5.3.4` | Differentiation: GATE CSE 2016 \| Set 2 \| Question: 02 | **9** |
| `5.3.5` | Differentiation: GATE CSE 2017 \| Set 2 \| Question: 10 | **C** |
| `5.3.6` | Differentiation: GATE CSE 2024 \| Set 1 \| Question: 1 | **D** |
| `5.3.7` | Differentiation: GATE CSE 2025 \| Set 1 \| Question: 21 | **-2.1:-1.9** |
| `5.3.8` | Differentiation: GATE CSE 2026 \| Set 1 \| Question: 36 | **A;C;D** |
| `5.3.9` | Differentiation: GATE DA 2025 \| Question: 14 | **A;B;C** |
| `5.3.10` | Differentiation: GATE DA 2025 \| Question: 4 | **A** |
| `5.3.11` | Differentiation: GATE DA 2025 \| Question: 41 | **B;C;D** |
| `5.4.2` | Integration: GATE CSE 1998 \| Question: 8 | **N/A** |
| `5.4.3` | Integration: GATE CSE 2000 \| Question: 2.3 | **A** |
| `5.4.4` | Integration: GATE CSE 2009 \| Question: 25 | **D** |
| `5.4.5` | Integration: GATE CSE 2011 \| Question: 31 | **D** |
| `5.4.6` | Integration: GATE CSE 2014 \| Set 3 \| Question: 47 | **A** |
| `5.4.7` | Integration: GATE CSE 2014 \| Set 3 \| Question: 6 | **4** |
| `5.4.8` | Integration: GATE CSE 2015 \| Set 1 \| Question: 44 | **-1** |
| `5.4.9` | Integration: GATE CSE 2015 \| Set 3 \| Question: 45 | **A** |
| `5.4.10` | Integration: GATE CSE 2018 \| Question: 16 | **0.288** |
| `5.4.11` | Integration: GATE IT 2005 \| Question: 35 | **B** |
| `5.5.1` | Limits: GATE CSE 1993 \| Question: 02.1 | **1** |
| `5.5.2` | Limits: GATE CSE 1995 \| Question: 7(B) | **1** |
| `5.5.3` | Limits: GATE CSE 2008 \| Question: 1 | **A** |
| `5.5.4` | Limits: GATE CSE 2010 \| Question: 5 | **B** |
| `5.5.5` | Limits: GATE CSE 2015 \| Set 1 \| Question: 4 | **C** |
| `5.5.6` | Limits: GATE CSE 2015 \| Set 3 \| Question: 9 | **C** |
| `5.5.7` | Limits: GATE CSE 2016 \| Set 1 \| Question: 3 | **1** |
| `5.5.8` | Limits: GATE CSE 2017 \| Set 1 \| Question: 28 | **C** |
| `5.5.9` | Limits: GATE CSE 2019 \| Question: 13 | **C** |
| `5.5.10` | Limits: GATE CSE 2021 \| Set 1 \| Question: 20 | **0.25** |
| `5.5.11` | Limits: GATE CSE 2022 \| Question: 24 | **-0.5** |
| `5.5.12` | Limits: GATE DA 2025 \| Question: 22 | **0.5:0.5** |
| `5.5.13` | Limits: GATE DA 2025 \| Question: 49 | **0:0** |
| `5.5.14` | Limits: GATE DS&AI 2024 \| Question: 50 | **0.5** |
| `5.5.15` | Limits: GATE Data Science and Artificial Intelligence 2024 \| Sample Paper \| Question: 5 | **C** |
| `5.6.1` | Maxima Minima: GATE CSE 1987 \| Question: 1-xxvi | **A** |
| `5.6.2` | Maxima Minima: GATE CSE 1995 \| Question: 1.21 | **B** |
| `5.6.3` | Maxima Minima: GATE CSE 1995 \| Question: 25a | **1** |
| `5.6.4` | Maxima Minima: GATE CSE 1997 \| Question: 4.1 | **B** |
| `5.6.5` | Maxima Minima: GATE CSE 2008 \| Question: 25 | **B** |
| `5.6.6` | Maxima Minima: GATE CSE 2012 \| Question: 9 | **D** |
| `5.6.7` | Maxima Minima: GATE CSE 2015 \| Set 2 \| GA \| Question: 3 | **C** |
| `5.6.8` | Maxima Minima: GATE CSE 2020 \| Question: 1 | **A** |
| `5.6.9` | Maxima Minima: GATE CSE 2023 \| Question: 18 | **B;D** |
| `5.6.10` | Maxima Minima: GATE DA 2025 \| Question: 39 | **C;D** |
| `5.6.11` | Maxima Minima: GATE DA 2026 \| Question: 17 | **B;D** |
| `5.6.12` | Maxima Minima: GATE DS&AI 2024 \| Question: 40 | **A;B** |
| `5.6.13` | Maxima Minima: GATE DS&AI 2024 \| Question: 5 | **A** |
| `5.6.14` | Maxima Minima: GATE IT 2008 \| Question: 31 | **B** |
| `5.7.1` | Polynomials: GATE CSE 1987 \| Question: 1-xxii | **B** |
| `5.7.2` | Polynomials: GATE CSE 1995 \| Question: 2.8 | **C** |
| `5.8.1` | Summation: GATE DA 2026 \| Question: 25 | **1:1** |

