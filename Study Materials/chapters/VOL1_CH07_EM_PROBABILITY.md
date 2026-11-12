# Volume 1 — Chapter 7: Engineering Mathematics: Probability

- **Source PDF**: [filter1_volume1.pdf](file:///Users/adityaasaha/Documents/Academics/Gate/filter1_volume1.pdf)
- **Total GATE Questions in Chapter**: **125**

---

## 1. Subtopic Weightage & Question Distribution

| Subtopic # | Subtopic Name | Questions |
| :---: | :--- | :---: |
| **7.1** | Bayes Theorem | 3 |
| **7.2** | Bayesian Network | 2 |
| **7.3** | Bernoulli Distribution | 2 |
| **7.4** | Binomial Distribution | 6 |
| **7.5** | Chi Square Distribution | 1 |
| **7.6** | Conditional Probability | 14 |
| **7.7** | Continuous Distribution | 1 |
| **7.8** | Expectation | 15 |
| **7.9** | Exponential Distribution | 6 |
| **7.10** | Independent Events | 6 |
| **7.11** | Normal Distribution | 4 |
| **7.12** | Poisson Distribution | 5 |
| **7.13** | Probability | 31 |
| **7.14** | Probability Density Function | 1 |
| **7.15** | Probability Distribution | 1 |
| **7.16** | Random Variable | 10 |
| **7.17** | Square Invariant | 1 |
| **7.18** | Statistics | 3 |
| **7.19** | Uniform Distribution | 11 |
| **7.20** | Variance | 2 |


---

## 2. Comprehensive GATE CSE Probability & Statistics Reference (Expanded Research & Formulas)

### 2.1 Axioms, Conditional Probability & Bayes' Theorem
- **Inclusion-Exclusion**: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
- **Conditional Probability**: $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$ for $P(B) > 0$.
- **Independent Events**: $P(A \cap B) = P(A)P(B)$.
  - *Crucial Trap*: **Mutually exclusive ($A \cap B = \emptyset$) $\neq$ Independent**! If $P(A) > 0, P(B) > 0$, mutually exclusive events are NEVER independent.
  - Pairwise independence of $A, B, C$ does **not** imply mutual independence ($P(A \cap B \cap C) = P(A)P(B)P(C)$ is also required).
- **Law of Total Probability & Bayes' Theorem**:
  $$P(B) = \sum_{i=1}^{n} P(A_i) P(B \mid A_i), \qquad P(A_k \mid B) = \frac{P(A_k) P(B \mid A_k)}{\sum_{i=1}^{n} P(A_i) P(B \mid A_i)}$$

### 2.2 Random Variables, Expectation & Variance
- **PMF / PDF Normalization**: $\sum_x P(X=x) = 1$, $\int_{-\infty}^{\infty} f_X(x)\,dx = 1$.
- **CDF**: $F_X(x) = P(X \le x)$, $f_X(x) = \frac{d}{dx} F_X(x)$, $P(a < X \le b) = F_X(b) - F_X(a)$.
- **Expectation (Linearity ALWAYS holds, even for dependent RVs!)**:
  $$E[aX + bY + c] = aE[X] + bE[Y] + c$$
  - For non-negative integer RV: $E[X] = \sum_{k=1}^{\infty} P(X \ge k)$.
- **Variance & Covariance**:
  $$\text{Var}(X) = E[X^2] - (E[X])^2, \qquad \text{Var}(aX + b) = a^2 \text{Var}(X)$$
  $$\text{Var}(aX \pm bY) = a^2 \text{Var}(X) + b^2 \text{Var}(Y) \pm 2ab\,\text{Cov}(X, Y)$$
  where $\text{Cov}(X, Y) = E[XY] - E[X]E[Y]$. (If $X, Y$ are independent $\implies \text{Cov}(X, Y) = 0$, converse is not always true).

### 2.3 Master Table of Standard Distributions
| Distribution | Parameters | PMF / PDF | Mean $E[X]$ | Variance $\text{Var}(X)$ | Notes / Memoryless |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **Bernoulli** | $p$ | $p^x (1-p)^{1-x}, \; x \in \{0,1\}$ | $p$ | $p(1-p)$ | Single trial |
| **Binomial** | $n, p$ | $\binom{n}{k} p^k (1-p)^{n-k}$ | $np$ | $np(1-p)$ | Sum of $n$ iid Bernoulli |
| **Geometric** | $p$ (trials till 1st success) | $(1-p)^{k-1} p, \; k \ge 1$ | $\frac{1}{p}$ | $\frac{1-p}{p^2}$ | **Discrete Memoryless**: $P(X > m+n \mid X > m) = P(X > n)$ |
| **Poisson** | $\lambda > 0$ | $\frac{e^{-\lambda} \lambda^k}{k!}, \; k \ge 0$ | $\lambda$ | $\lambda$ | Rare events ($n \to \infty, np = \lambda$) |
| **Uniform (Cont.)** | $[a, b]$ | $\frac{1}{b-a}, \; x \in [a,b]$ | $\frac{a+b}{2}$ | $\frac{(b-a)^2}{12}$ | Constant density on $[a,b]$ |
| **Exponential** | $\lambda > 0$ (rate) | $\lambda e^{-\lambda x}, \; x \ge 0$ | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$ | **Continuous Memoryless**: $P(X > s+t \mid X > s) = e^{-\lambda t}$ |
| **Normal (Gaussian)** | $\mu, \sigma^2$ | $\frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ | $\mu$ | $\sigma^2$ | $68.27\%\;(\pm 1\sigma), 95.45\%\;(\pm 2\sigma), 99.73\%\;(\pm 3\sigma)$ |

- **Min of Independent Exponentials**: If $X_1 \sim \text{Exp}(\lambda_1)$ and $X_2 \sim \text{Exp}(\lambda_2)$ are independent, then $\min(X_1, X_2) \sim \text{Exp}(\lambda_1 + \lambda_2)$.
- **Sum of Independent Poissons**: If $X \sim \text{Pois}(\lambda_1), Y \sim \text{Pois}(\lambda_2)$, then $X + Y \sim \text{Pois}(\lambda_1 + \lambda_2)$.

---

## 3. Original PDF Chapter Notes (Preserved Verbatim)

7 Engineering Mathematics: Probability (125)
Syllabus: Random variables, Uniform, Normal, Exponential, Poisson and Binomial distributions. Mean,
median, mode and standard deviation. Conditional probability and Bayes theorem
Welcome to the "Engineering Mathematics: Probability" chapter, a cornerstone for any aspiring GATE Computer
Science candidate. This subject delves into the mathematical framework for quantifying uncertainty, analyzing random
phenomena, and making informed decisions in the face of incomplete information. For GATE CS, a solid understanding
of probability is indispensable, as it forms the theoretical bedrock for crucial areas like algorithms (randomized
algorithms, average-case analysis), data structures (hash tables, skip lists), machine learning (classification, regression,
neural networks, Bayesian inference), artificial intelligence, networking (queueing theory, packet loss), and even
operating systems (scheduling, resource allocation). Typically, probability questions constitute a significant portion of
the Engineering Mathematics section, often contributing 3-5 marks directly, with concepts frequently integrated into 1-
mark or 2-mark questions across other CS topics. Questions can range from direct formula application and conceptual
understanding to problem-solving involving combinations of distributions and theorems, often requiring careful
interpretation of scenarios.
Topic-wise Key Concepts
Bayes Theorem
Definition and Core Idea: Bayes' Theorem describes the probability of an event, based on prior knowledge of
conditions that might be related to the event. It's a fundamental concept for updating beliefs or probabilities as new
evidence becomes available, forming the basis of Bayesian inference.
Important Formulas, Theorems, and Results:
1. Bayes' Theorem: For two events and , where ,
where can be expanded using the law of total probability:
More generally, for a partition of the sample space,
Key Properties and Identities:
Allows for the calculation of posterior probability from prior probability and likelihood .
Crucial for diagnostic testing, spam filtering, and machine learning algorithms (e.g., Naive Bayes).
Common Pitfalls or Tricky Points:
Confusing with .
Incorrectly calculating the denominator Not identifying the correct prior probabilities by not considering all mutually exclusive and exhaustive cases.
and conditional probabilities .
Standard Problem-Solving Techniques or Shortcuts:
Clearly define events and .
Break down the problem into identifying , , and (or ).
Use tree diagrams to visualize conditional probabilities and total probability.
Bayesian Network
Definition and Core Idea: A Bayesian Network (BN) is a probabilistic graphical model that represents a set of random

*(PDF Page 190)*

variables and their conditional dependencies via a directed acyclic graph (DAG). Nodes represent random variables,
and directed edges represent conditional dependencies, allowing for efficient representation and inference of joint
probability distributions.
Important Formulas, Theorems, and Results:
1. Joint Probability Distribution: For a Bayesian Network with nodes , the joint probability
distribution is given by the product of the conditional probability distributions of each node given its parents:
2. Conditional Independence: A node is conditionally independent of its non-descendants given its parents.
Key Properties and Identities:
Provides a compact representation of joint probability distributions, especially for many variables.
Facilitates inference (e.g., calculating where is evidence).
The graph structure explicitly shows the assumed conditional independencies.
Common Pitfalls or Tricky Points:
Misinterpreting the direction of edges or the meaning of conditional independence.
Incorrectly applying the chain rule for joint probability without respecting the network's structure.
Confusing marginal independence with conditional independence.
Standard Problem-Solving Techniques or Shortcuts:
Identify parents for each node to write down the joint probability.
Use d-separation rules to determine conditional independencies graphically.
For inference, apply variable elimination or message passing algorithms (though GATE questions are usually
simpler, focusing on structure and basic inference).
Bernoulli Distribution
Definition and Core Idea: The Bernoulli distribution is a discrete probability distribution for a random variable that takes
(success) and value 0 with probability (failure). It models a single trial of an experiment
value 1 with probability with only two possible outcomes.
Important Formulas, Theorems, and Results:
1. Probability Mass Function (PMF): For a Bernoulli random variable ,
2. Mean (Expectation):
3. Variance:
Key Properties and Identities:
It's the simplest discrete distribution.
The sum of independent Bernoulli trials follows a Binomial distribution.
Common Pitfalls or Tricky Points:
Confusing Bernoulli with Binomial (Bernoulli is a single trial, Binomial is multiple trials).
Incorrectly identifying (probability of success).
Standard Problem-Solving Techniques or Shortcuts:
Identify the "success" event and its probability .
Directly apply formulas for mean and variance.
Binomial Distribution
Definition and Core Idea: The Binomial distribution models the number of successes in a fixed number of independent
Bernoulli trials, each with the same probability of success . It is a discrete probability distribution.
Important Formulas, Theorems, and Results:
1. Probability Mass Function (PMF): For ,
where is the binomial coefficient.

*(PDF Page 191)*

2. Mean (Expectation):
3. Variance:
4. Standard Deviation:
Key Properties and Identities:
Sum of independent Bernoulli random variables.
Symmetric if , skewed otherwise.
Approximated by Poisson distribution when is large and is small (and is moderate).
Approximated by Normal distribution when is large (and , ).
Common Pitfalls or Tricky Points:
Incorrectly identifying (number of trials) or (probability of success).
Miscalculating binomial coefficients.
Confusing "at least,
" "at most,
" "exactly" in problem statements (e.g., vs. ).
Standard Problem-Solving Techniques or Shortcuts:
Identify if the problem involves a fixed number of independent trials with two outcomes.
Use the complement rule for "at least" or "at most" probabilities (e.g., Memorize mean and variance formulas.
).
Chi Square Distribution
Definition and Core Idea: The Chi-Square ( ) distribution is a continuous probability distribution that arises in
statistics, particularly in hypothesis testing and confidence interval estimation. It is the distribution of a sum of the
squares of independent standard normal random variables.
Important Formulas, Theorems, and Results:
1. Definition: If are independent standard normal random variables (i.e., random variable follows a Chi-Square distribution with degrees of freedom, denoted
.
2. Probability Density Function (PDF):
), then the
where is the Gamma function.
3. Mean (Expectation):
4. Variance:
Key Properties and Identities:
Skewed to the right, but becomes more symmetric as increases.
Used in goodness-of-fit tests, tests of independence, and for variance estimation.
The sum of independent chi-square random variables is also a chi-square random variable with degrees of
freedom equal to the sum of their individual degrees of freedom.
Common Pitfalls or Tricky Points:
Incorrectly identifying the degrees of freedom .
Confusing the definition with other squared terms.
GATE questions usually focus on its properties or its role in statistical tests rather than direct PDF calculations.
Standard Problem-Solving Techniques or Shortcuts:
Understand that it's a sum of squared standard normal variables.
Memorize mean and variance in terms of degrees of freedom.
Recognize its application in hypothesis testing contexts (e.g., for categorical data).
Conditional Probability
Definition and Core Idea: Conditional probability is the probability of an event occurring given that another event has
already occurred. It quantifies how the probability of an event changes when new information is available.
Important Formulas, Theorems, and Results:
1. Definition: For two events and , with , the conditional probability of given is:

*(PDF Page 192)*

2. Multiplication Rule of Probability:
3. Law of Total Probability: If form a partition of the sample space, then for any event :
Key Properties and Identities:
If and are independent, .
.
.
Common Pitfalls or Tricky Points:
Incorrectly identifying or .
Confusing with or .
Not recognizing when events are independent, which simplifies calculations.
Standard Problem-Solving Techniques or Shortcuts:
Clearly define the events and .
Use Venn diagrams or tree diagrams to visualize the sample space and events.
Break down complex problems into simpler conditional probabilities.
Continuous Distribution
Definition and Core Idea: A continuous probability distribution describes the probabilities of a random variable taking
on values in a continuous range (e.g., real numbers). Unlike discrete distributions, the probability of a continuous
random variable taking on any single exact value is zero.
Important Formulas, Theorems, and Results:
1. Probability Density Function (PDF): such that for all , and .
2. Probability of an Interval: .
3. Cumulative Distribution Function (CDF): .
4. Relationship between PDF and CDF: (where is differentiable).
5. Mean (Expectation): .
6. Variance: .
Key Properties and Identities:
for any specific value .
The area under the PDF curve over its entire range is 1.
The CDF is non-decreasing and ranges from 0 to 1.
Common Pitfalls or Tricky Points:
Confusing PDF with PMF (for discrete distributions).
Incorrectly calculating integrals for probabilities, mean, or variance.
Forgetting that for continuous distributions.
Standard Problem-Solving Techniques or Shortcuts:
Always check if the given function is a valid PDF (non-negative and integrates to 1).
Use integration for calculating probabilities and moments.
Understand the relationship between PDF and CDF.
Expectation
Definition and Core Idea: The expectation (or expected value, mean) of a random variable is the weighted average of
all possible values that the random variable can take, with the weights being their respective probabilities. It represents
the "long-run average" or central tendency of the random variable.
Important Formulas, Theorems, and Results:
1. For Discrete Random Variable :

*(PDF Page 193)*

2. For Continuous Random Variable :
3. Expectation of a Function of a Random Variable :
Discrete:
Continuous:
4. Linearity of Expectation: For any random variables and constants :
5. Expectation of Product (for Independent Variables): If and are independent, then
.
Key Properties and Identities:
for a constant .
.
Expectation is a linear operator.
Common Pitfalls or Tricky Points:
Confusing with . They are generally not equal.
Applying when and are not independent.
Incorrectly summing or integrating over the wrong range.
Standard Problem-Solving Techniques or Shortcuts:
Identify whether the variable is discrete or continuous.
Use linearity of expectation extensively, as it holds even for dependent variables.
For complex functions, break them down using linearity.
Exponential Distribution
Definition and Core Idea: The Exponential distribution is a continuous probability distribution that describes the time
between events in a Poisson process, i.e., a process in which events occur continuously and independently at a
constant average rate. It is memoryless, meaning the past duration does not affect future duration.
Important Formulas, Theorems, and Results:
1. Probability Density Function (PDF): For ,
where is the rate parameter.
2. Cumulative Distribution Function (CDF):
3. Mean (Expectation):
4. Variance:
5. Memoryless Property: for any .
Key Properties and Identities:
Models waiting times, lifetimes of components, etc.
Its rate parameter is the inverse of the mean.
The only continuous distribution with the memoryless property.
Common Pitfalls or Tricky Points:
Confusing the rate parameter with the mean .
Incorrectly applying the memoryless property or forgetting its implications.
Errors in integration for probabilities or moments if not using CDF.
Standard Problem-Solving Techniques or Shortcuts:
Identify problems involving "time until" an event or "lifetime" with a constant rate.
Directly use CDF for or .
Apply the memoryless property to simplify conditional probability questions.
Independent Events

*(PDF Page 194)*

Definition and Core Idea: Two events are independent if the occurrence of one does not affect the probability of the
other occurring. Their probabilities multiply to give the probability of both occurring.
Important Formulas, Theorems, and Results:
1. Definition: Events and are independent if and only if:
2. Equivalent Conditions: If , then and are independent if and only if . Similarly,
if , then .
3. Independence of Complements: If and are independent, then and , and , and and are
also independent.
Key Properties and Identities:
Simplifies calculations involving joint probabilities.
Crucial assumption for many statistical models and distributions (e.g., Binomial, Poisson).
Common Pitfalls or Tricky Points:
Confusing independent events with mutually exclusive events (disjoint events). Mutually exclusive events cannot
be independent unless one has zero probability.
Assuming independence when it's not explicitly stated or logically implied.
Incorrectly applying the product rule for dependent events.
Standard Problem-Solving Techniques or Shortcuts:
Always check the definition to verify independence.
If events are independent, use the simplified conditional probability .
Normal Distribution
Definition and Core Idea: The Normal (or Gaussian) distribution is a symmetric, bell-shaped continuous probability
distribution that is ubiquitous in natural and social sciences. It is characterized by its mean ( ) and standard deviation (
), and is central to the Central Limit Theorem.
Important Formulas, Theorems, and Results:
1. Probability Density Function (PDF): For ,
2. Mean (Expectation):
3. Variance:
4. Standard Deviation:
5. Standard Normal Distribution: A normal distribution with and , denoted .
6. Standardization: If , then .
7. Empirical Rule (68-95-99.7 Rule): Approximately 68% of data falls within of the mean, 95% within , and
99.7% within .
Key Properties and Identities:
Symmetric about its mean.
The mean, median, and mode are all equal to .
Sum of independent normal random variables is also normal.
Central Limit Theorem: The sum/average of a large number of independent and identically distributed random
variables, regardless of their original distribution, tends towards a normal distribution.
Common Pitfalls or Tricky Points:
Not standardizing correctly before using Z-tables (if tables were provided, though GATE usually tests concepts).
Confusing variance with standard deviation .
Assuming normality when not justified, especially for small sample sizes.
Standard Problem-Solving Techniques or Shortcuts:
Convert any normal variable to a standard normal variable using .
Use the symmetry of the normal distribution: .
Apply the empirical rule for quick estimations.
Poisson Distribution

*(PDF Page 195)*

Definition and Core Idea: The Poisson distribution is a discrete probability distribution that expresses the probability of
a given number of events occurring in a fixed interval of time or space if these events occur with a known constant
mean rate and independently of the time since the last event.
Important Formulas, Theorems, and Results:
1. Probability Mass Function (PMF): For ,
where is the average rate of events in the interval.
2. Mean (Expectation):
3. Variance:
Key Properties and Identities:
Models rare events.
The mean and variance are equal ( ).
Can approximate the Binomial distribution when is large and is small, with .
The sum of independent Poisson random variables is also a Poisson random variable (with rate parameter equal
to the sum of individual rates).
Common Pitfalls or Tricky Points:
Incorrectly identifying (the average rate for the specified interval). Ensure is consistent with the time/space
unit of the problem.
Miscalculating factorials or powers of .
Confusing "at least,
" "at most,
" "exactly" in problem statements.
Standard Problem-Solving Techniques or Shortcuts:
Identify problems involving counts of events over a fixed interval.
Use the complement rule for "at least" probabilities.
Remember that mean and variance are both .
Probability
Definition and Core Idea: Probability is a numerical measure of the likelihood of an event occurring. It is a value
between 0 and 1, where 0 indicates impossibility and 1 indicates certainty. It forms the foundation for understanding
randomness and uncertainty.
Important Formulas, Theorems, and Results:
1. Axioms of Probability:
For any event , .
where is the sample space.
For a sequence of mutually exclusive events , .
2. Complement Rule: .
3. Addition Rule: .
4. For Mutually Exclusive Events: If , then .
Key Properties and Identities:
Probabilities are non-negative.
The sum of probabilities of all possible outcomes is 1.
The probability of the impossible event is 0.
Common Pitfalls or Tricky Points:
Incorrectly identifying the sample space or events.
Misapplying the addition rule without accounting for overlaps.
Confusing "and" ( ) with "or" ( ).
Standard Problem-Solving Techniques or Shortcuts:
Clearly define the sample space and events.
Use Venn diagrams for visualizing events and their intersections/unions.
For equally likely outcomes, .
Probability Density Function (PDF)
Definition and Core Idea: The Probability Density Function (PDF), denoted , is a function associated with
continuous random variables. It describes the relative likelihood for the random variable to take on a given value. The
area under the PDF curve over an interval gives the probability that the variable falls within that interval.

*(PDF Page 196)*

Important Formulas, Theorems, and Results:
1. Properties of a PDF:
for all .
.
2. Probability Calculation: .
3. Relationship with CDF: , where is the Cumulative Distribution Function.
Key Properties and Identities:
The PDF itself does not give a probability; rather, its integral over an interval does.
For continuous variables, .
Common Pitfalls or Tricky Points:
Interpreting as . This is incorrect for continuous variables.
Forgetting to check if the PDF integrates to 1 over its entire domain.
Errors in integration limits or the function itself.
Standard Problem-Solving Techniques or Shortcuts:
Always verify the two properties of a PDF.
Use integration to find probabilities over intervals.
If given a CDF, differentiate to find the PDF.
Probability Distribution
Definition and Core Idea: A probability distribution is a mathematical function that describes all possible values and
likelihoods that a random variable can take within a given range. It can be discrete (Probability Mass Function, PMF) or
continuous (Probability Density Function, PDF).
Important Formulas, Theorems, and Results:
1. For Discrete Distributions (PMF for all .
):
.
2. For Continuous Distributions (PDF for all .
):
.
3. Cumulative Distribution Function (CDF): .
For discrete: .
For continuous: .
Key Properties and Identities:
Completely characterizes a random variable's behavior.
CDF is non-decreasing, , .
Allows calculation of probabilities, expected values, and variances.
Common Pitfalls or Tricky Points:
Confusing PMF and PDF.
Incorrectly applying summation for continuous or integration for discrete.
Not understanding the difference between and .
Standard Problem-Solving Techniques or Shortcuts:
Identify whether the random variable is discrete or continuous.
Use the appropriate function (PMF/PDF) and its properties to solve problems.
Understand the relationship between PMF/PDF and CDF.
Random Variable
Definition and Core Idea: A random variable is a variable whose value is a numerical outcome of a random
phenomenon. It is a function that maps outcomes from a sample space to real numbers. Random variables can be
discrete (taking countable values) or continuous (taking values in an interval).
Important Formulas, Theorems, and Results:
1. Discrete Random Variable: Takes on a finite or countably infinite number of values (e.g., number of heads in
coin flips).
2. Continuous Random Variable: Takes on any value within a given interval (e.g., height, temperature).
3. Probability Distribution: Each random variable has an associated probability distribution (PMF or PDF) that
describes the probabilities of its possible values.
Key Properties and Identities:

*(PDF Page 197)*

Transforms qualitative outcomes into quantitative values.
Allows for mathematical analysis of random phenomena.
The sum, difference, product, or quotient of random variables is also a random variable.
Common Pitfalls or Tricky Points:
Confusing the random variable itself with the values it can take.
Not correctly defining the sample space before defining the random variable.
Misidentifying whether a variable is discrete or continuous.
Standard Problem-Solving Techniques or Shortcuts:
Clearly define the random variable and its possible values.
Determine if it's discrete or continuous to choose the correct probability distribution type.
Map real-world scenarios to appropriate random variable definitions.
Square Invariant
Definition and Core Idea: While "Square Invariant" is not a standard term for a probability distribution or theorem, in
the context of probability and statistics, it most likely refers to properties or transformations related to the square of a
random variable, particularly in the calculation of moments or variance, or in the context of distributions like the Chi-
Square distribution which involves sums of squared normal variables. It implies that certain properties hold true even
after squaring the variable or that a transformation involving squaring preserves some characteristic.
Important Formulas, Theorems, and Results:
1. Second Moment: (discrete) or (continuous). This is a key "square"
quantity.
2. Variance Definition: . This formula shows how is
used to calculate variance.
3. Chi-Square Distribution: Defined as the sum of squares of independent standard normal random variables,
. This is a direct application of squaring random variables.
. This shows how scaling affects the variance (a square
4. Properties of Variance: property).
Key Properties and Identities:
is always non-negative.
Variance measures the spread of a distribution in squared units.
The Chi-Square distribution is fundamental for statistical inference involving variances.
Common Pitfalls or Tricky Points:
Confusing with . They are distinct and generally not equal.
Incorrectly calculating by not squaring the values before applying expectation.
Misinterpreting the degrees of freedom in Chi-Square related problems.
Standard Problem-Solving Techniques or Shortcuts:
When calculating variance, always compute and separately.
Recognize that problems involving sums of squared normal variables point towards the Chi-Square distribution.
Remember that variance is always non-negative.
Statistics
Definition and Core Idea: Statistics is the science of collecting, analyzing, interpreting, presenting, and organizing
data. In the context of probability, statistics involves using data from a sample to make inferences about a larger
population, often relying on probability distributions to quantify uncertainty.
Important Formulas, Theorems, and Results:
1. Measures of Central Tendency:
Mean ( or ): Average value.
Median: Middle value when data is ordered.
Mode: Most frequent value.
2. Measures of Dispersion:
Variance ( or Standard Deviation ( or Range: Max value - Min value.
3. Sample vs. Population:
Population Mean:
Sample Mean:
): Average of the squared differences from the mean.
): Square root of variance, in original units.

*(PDF Page 198)*

Population Variance:
Sample Variance: (unbiased estimator)
Key Properties and Identities:
Statistics provides tools to summarize and interpret data.
Probability distributions are models for the underlying data generation process.
Central Limit Theorem is a bridge between probability and statistics.
Common Pitfalls or Tricky Points:
Confusing population parameters ( ) with sample statistics ( ).
Using instead of in the denominator for sample variance (for unbiased estimation).
Misinterpreting the meaning of different measures (e.g., mean vs. median for skewed data).
Standard Problem-Solving Techniques or Shortcuts:
Identify whether the problem refers to a population or a sample.
Know the definitions and formulas for common descriptive statistics.
Understand how probability distributions are used to model observed data.
Uniform Distribution
Definition and Core Idea: The Uniform distribution is a continuous probability distribution where all values within a
given interval are equally likely. It has a constant probability density over its support and zero elsewhere.
Important Formulas, Theorems, and Results:
1. Probability Density Function (PDF): For ,
2. Cumulative Distribution Function (CDF):
3. Mean (Expectation):
4. Variance:
Key Properties and Identities:
All outcomes within the interval are equally probable.
Often used as a null hypothesis or a simple model when no other information is available.
Common Pitfalls or Tricky Points:
Incorrectly identifying the interval .
Errors in calculating probabilities for sub-intervals (e.g., ).
Forgetting the constant in the variance formula.
Standard Problem-Solving Techniques or Shortcuts:
Draw the PDF as a rectangle for visualization.
Probabilities are simply the ratio of the length of the sub-interval to the length of the total interval.
Memorize mean and variance formulas.
Variance
Definition and Core Idea: Variance is a measure of the spread or dispersion of a set of data points around their mean.
It quantifies how much the values of a random variable deviate from its expected value, on average. A higher variance
indicates greater variability.
Important Formulas, Theorems, and Results:
1. Definition:
2. Computational Formula:
3. For Discrete Random Variable :

*(PDF Page 199)*

4. For Continuous Random Variable :
5. Properties of Variance:
for a constant .
for a constant .
for a constant .
.
For independent random variables : .
For independent random variables : .
6. Standard Deviation: .
Key Properties and Identities:
Variance is always non-negative.
It is expressed in squared units of the random variable.
It measures the average squared deviation from the mean.
Common Pitfalls or Tricky Points:
Forgetting to square the deviations or the constant Assuming when applying properties.
when and are not independent (this requires covariance
terms).
Confusing variance with standard deviation.
Standard Problem-Solving Techniques or Shortcuts:
Always use the computational formula as it's often easier.
Leverage the properties of variance to simplify calculations for linear transformations or sums of independent
variables.
Calculate first, then .
Quick Formula Reference
Basic Probability
Addition Rule:
Complement Rule:
Conditional Probability
Definition:
Multiplication Rule:
Law of Total Probability:
Independent Events
Condition: or
Bayes Theorem
Formula:
Expectation (Mean)
Discrete:
Continuous:
Linearity:
Variance
Definition:
Computational:
Properties:
For independent :
Standard Deviation:
Bernoulli Distribution ( , )
PMF:
Mean:
Variance:
Binomial Distribution ( )

*(PDF Page 200)*

PMF:
Mean:
Variance:
Poisson Distribution ( )
PMF:
Mean:
Variance:
Uniform Distribution ( )
PDF: for , else 0
Mean:
Variance:
Exponential Distribution ( )
PDF: for , else 0
CDF: for
Mean:
Variance:
Memoryless:
Normal Distribution ( )
PDF:
Mean:
Variance:
Standardization:
Chi-Square Distribution ( )
Definition: Sum of squared independent standard normal variables.
Mean:
Variance:
Important Tips for GATE
1. Master the Fundamentals: Ensure a strong grasp of basic probability axioms, conditional probability, and
independence. Many complex problems are built upon these foundational concepts. Don't rush through them.
2. Understand Discrete vs. Continuous: Clearly distinguish between discrete and continuous random variables.
Know when to use summation (PMF) versus integration (PDF), and remember that for continuous
variables.
3. Memorize Key Distribution Properties: For each distribution (Bernoulli, Binomial, Poisson, Uniform, Exponential,
Normal, Chi-Square), memorize their PMF/PDF, mean, and variance. This saves crucial time in the exam.
4. Practice Conditional Probability and Bayes' Theorem: These are frequently tested. Practice problems that
require careful identification of events and application of the formulas, especially those involving multiple stages or
diagnostic scenarios.
5. Pay Attention to Keywords: Words like "at least,
" "at most,
" "exactly,
" "given that,
" "independent,
" and "without
replacement" significantly alter problem interpretation and solution approach. Read questions carefully.
6. Leverage Linearity of Expectation and Variance Properties: is powerful as it
holds even for dependent variables. For variance, remember and
only for independent variables.
7. Don't Confuse Mean and Variance Parameters: For Exponential distribution, is the rate, mean is . For
Normal, is mean, is variance (not ). Small errors here are common pitfalls.
8. Practice Problem Solving: The best way to prepare is to solve a wide variety of problems from previous GATE
papers and standard textbooks. Focus on understanding the logic behind each step, not just getting the answer.

---

## 4. Complete Question Index & Answer Key Record (125 Questions)

| Q # | Question Source / Title | Answer Key |
| :---: | :--- | :---: |
| `7.1.1` | Bayes Theorem: GATE CSE 2018 \| Question: 44 | **0.60** |
| `7.1.2` | Bayes Theorem: GATE CSE 2021 \| Set 1 \| Question: 54 | **0.04** |
| `7.1.3` | Bayes Theorem: GATE DA 2025 \| Question: 21 | **0.25:0.25** |
| `7.2.1` | Bayesian Network: GATE DS&AI 2024 \| Question: 14 | **C** |
| `7.2.2` | Bayesian Network: GATE DS&AI 2024 \| Question: 54 | **0.125** |
| `7.3.1` | Bernoulli Distribution: GATE DA 2025 \| Question: 30 | **A** |
| `7.3.2` | Bernoulli Distribution: GATE DA 2026 \| Question: 54 | **0.08:0.12** |
| `7.4.1` | Binomial Distribution: GATE CSE 2002 \| Question: 2.16 | **C** |
| `7.4.2` | Binomial Distribution: GATE CSE 2005 \| Question: 52 | **D** |
| `7.4.3` | Binomial Distribution: GATE CSE 2006 \| Question: 21 | **A** |
| `7.4.4` | Binomial Distribution: GATE IT 2005 \| Question: 32 | **A** |
| `7.4.5` | Binomial Distribution: GATE IT 2006 \| Question: 22 | **A** |
| `7.4.6` | Binomial Distribution: GATE IT 2007 \| Question: 1 | **C** |
| `7.5.1` | Chi Square Distribution: GATE DA 2026 \| Question: 43 | **A;B;C** |
| `7.6.1` | Conditional Probability: GATE CSE 1994 \| Question: 1.4, ISRO2017-2 | **D** |
| `7.6.2` | Conditional Probability: GATE CSE 1994 \| Question: 2.6 | **N/A** |
| `7.6.3` | Conditional Probability: GATE CSE 2003 \| Question: 3 | **D** |
| `7.6.4` | Conditional Probability: GATE CSE 2005 \| Question: 51 | **A** |
| `7.6.5` | Conditional Probability: GATE CSE 2008 \| Question: 27 | **C** |
| `7.6.6` | Conditional Probability: GATE CSE 2009 \| Question: 21 | **B** |
| `7.6.7` | Conditional Probability: GATE CSE 2011 \| Question: 3 | **A** |
| `7.6.8` | Conditional Probability: GATE CSE 2012 \| Question: 33 | **B** |
| `7.6.9` | Conditional Probability: GATE CSE 2016 \| Set 2 \| Question: 05 | **0.55** |
| `7.6.10` | Conditional Probability: GATE CSE 2017 \| Set 2 \| Question: 26 | **A** |
| `7.6.11` | Conditional Probability: GATE CSE 2024 \| Set 1 \| Question: 53 | **0.375** |
| `7.6.12` | Conditional Probability: GATE CSE 2026 \| Set 2 \| Question: 53 | **0.5:0.5** |
| `7.6.13` | Conditional Probability: GATE DA 2026 \| Question: 47 | **0.76:0.78** |
| `7.6.14` | Conditional Probability: GATE IT 2006 \| Question: 1 | **C** |
| `7.7.1` | Continuous Distribution: GATE CSE 2016 \| Set 1 \| Question: 04 | **0.5** |
| `7.8.1` | Expectation: GATE CSE 1999 \| Question: 1.1 | **C** |
| `7.8.2` | Expectation: GATE CSE 2004 \| Question: 74 | **D** |
| `7.8.3` | Expectation: GATE CSE 2006 \| Question: 18 | **D** |
| `7.8.4` | Expectation: GATE CSE 2011 \| Question: 18 | **C** |
| `7.8.5` | Expectation: GATE CSE 2013 \| Question: 24 | **C** |
| `7.8.6` | Expectation: GATE CSE 2014 \| Set 2 \| Question: 2 | **3.8** |
| `7.8.7` | Expectation: GATE CSE 2017 \| Set 2 \| Question: 31 | **B** |
| `7.8.8` | Expectation: GATE CSE 2021 \| Set 1 \| Question: 35 | **D** |
| `7.8.9` | Expectation: GATE CSE 2021 \| Set 2 \| Question: 29 | **D** |
| `7.8.10` | Expectation: GATE CSE 2026 \| Set 1 \| Question: 48 | **4.24** |
| `7.8.11` | Expectation: GATE DA 2025 \| Question: 1 | **C** |
| `7.8.12` | Expectation: GATE DA 2025 \| Question: 10 | **A** |
| `7.8.13` | Expectation: GATE DA 2025 \| Question: 51 | **66.6:66.7** |
| `7.8.14` | Expectation: GATE DS&AI 2024 \| Question: 26 | **C** |
| `7.8.15` | Expectation: GATE DS&AI 2024 \| Question: 49 | **X** |
| `7.9.1` | Exponential Distribution: GATE CSE 2021 \| Set 1 \| Question: 18 | **0.35** |
| `7.9.2` | Exponential Distribution: GATE DA 2025 \| Question: 11 | **A** |
| `7.9.3` | Exponential Distribution: GATE DA 2025 \| Question: 31 | **A** |
| `7.9.4` | Exponential Distribution: GATE DA 2026 \| Question: 24 | **0.34:0.36** |
| `7.9.5` | Exponential Distribution: GATE DS&AI 2024 \| Question: 47 | **0.2** |
| `7.9.6` | Exponential Distribution: GATE IT 2004 \| Question: 33 | **C** |
| `7.10.1` | Independent Events: GATE CSE 1994 \| Question: 2.8 | **0.93** |
| `7.10.2` | Independent Events: GATE CSE 1999 \| Question: 2.1 | **C** |
| `7.10.3` | Independent Events: GATE CSE 2000 \| Question: 2.2 | **D** |
| `7.10.4` | Independent Events: GATE CSE 2023 \| Question: 43 | **C;D** |
| `7.10.5` | Independent Events: GATE DA 2025 \| Question: 44 | **A;C** |
| `7.10.6` | Independent Events: GATE DS&AI 2024 \| Question: 2 | **A** |
| `7.11.1` | Normal Distribution: GATE CSE 2008 \| Question: 29 | **A** |
| `7.11.2` | Normal Distribution: GATE CSE 2017 Set-1 \| Question:37 | **TBA** |
| `7.11.3` | Normal Distribution: GATE CSE 2017 \| Set 1 \| Question: 19 | **0** |
| `7.11.4` | Normal Distribution: GATE DA 2026 \| Question: 18 | **A;C** |
| `7.12.1` | Poisson Distribution: GATE CSE 1989 \| Question: 4-viii | **N/A** |
| `7.12.2` | Poisson Distribution: GATE CSE 2013 \| Question: 2 | **C** |
| `7.12.3` | Poisson Distribution: GATE CSE 2017 \| Set 2 \| Question: 48 | **54** |
| `7.12.4` | Poisson Distribution: GATE DA 2026 \| Question: 35 | **A** |
| `7.12.5` | Poisson Distribution: GATE IT 2007 \| Question: 57 | **B** |
| `7.13.1` | Probability: GATE CSE 1995 \| Question: 1.18 | **D** |
| `7.13.2` | Probability: GATE CSE 1995 \| Question: 2.14 | **C** |
| `7.13.3` | Probability: GATE CSE 1996 \| Question: 1.5 | **D** |
| `7.13.4` | Probability: GATE CSE 1996 \| Question: 2.7 | **C** |
| `7.13.5` | Probability: GATE CSE 1997 \| Question: 1.1 | **D** |
| `7.13.6` | Probability: GATE CSE 1998 \| Question: 1.1 | **B** |
| `7.13.7` | Probability: GATE CSE 2001 \| Question: 2.4 | **B** |
| `7.13.8` | Probability: GATE CSE 2004 \| Question: 25 | **A** |
| `7.13.9` | Probability: GATE CSE 2010 \| Question: 26 | **A** |
| `7.13.10` | Probability: GATE CSE 2010 \| Question: 27 | **A** |
| `7.13.11` | Probability: GATE CSE 2011 \| Question: 34 | **A** |
| `7.13.12` | Probability: GATE CSE 2014 \| Set 1 \| Question: 48 | **10** |
| `7.13.13` | Probability: GATE CSE 2014 \| Set 2 \| Question: 1 | **11.85** |
| `7.13.14` | Probability: GATE CSE 2014 \| Set 2 \| Question: 48 | **0.259** |
| `7.13.15` | Probability: GATE CSE 2014 \| Set 3 \| Question: 48 | **0.25** |
| `7.13.16` | Probability: GATE CSE 2016 \| Set 1 \| Question: 29 | **0.33** |
| `7.13.17` | Probability: GATE CSE 2018 \| Question: 15 | **0.0230** |
| `7.13.18` | Probability: GATE CSE 2021 \| Set 2 \| Question: 33 | **A** |
| `7.13.19` | Probability: GATE CSE 2024 \| Set 1 \| Question: 17 | **B;C** |
| `7.13.20` | Probability: GATE CSE 2024 \| Set 2 \| Question: 8 | **B** |
| `7.13.21` | Probability: GATE CSE 2025 \| Set 1 \| Question: 22 | **0.49:0.51** |
| `7.13.22` | Probability: GATE CSE 2026 \| Set 1 \| Question: 1 | **B** |
| `7.13.23` | Probability: GATE DA 2025 \| Question: 35 | **C** |
| `7.13.24` | Probability: GATE DA 2026 \| Question: 10 | **A** |
| `7.13.25` | Probability: GATE DA 2026 \| Question: 9 | **C** |
| `7.13.26` | Probability: GATE DS&AI 2024 \| Question: 48 | **0.25** |
| `7.13.27` | is | **B** |
| `7.13.28` | Probability: GATE IT 2004 \| Question: 1 | **B** |
| `7.13.29` | Probability: GATE IT 2005 \| Question: 1 | **B** |
| `7.13.30` | Probability: GATE IT 2008 \| Question: 2 | **B** |
| `7.13.31` | Probability: GATE IT 2008 \| Question: 23 | **X** |
| `7.14.1` | Probability Density Function: GATE CSE 2003 \| Question: 60, ISRO2007-45 | **C** |
| `7.15.1` | Probability Distribution: GATE CSE 2025 \| Set 1 \| Question: 48 | **0.300:0.302** |
| `7.16.1` | Random Variable: GATE CSE 2005 \| Question: 12, ISRO2009-64 | **C** |
| `7.16.2` | Random Variable: GATE CSE 2011 \| Question: 33 | **D** |
| `7.16.3` | Random Variable: GATE CSE 2012 \| Question: 21 | **C** |
| `7.16.4` | Random Variable: GATE CSE 2015 \| Set 3 \| Question: 37 | **0.75** |
| `7.16.5` | Random Variable: GATE CSE 2026 \| Set 2 \| Question: 4 | **B** |
| `7.16.6` | Random Variable: GATE DA 2025 \| Question: 29 | **C** |
| `7.16.7` | Random Variable: GATE DA 2025 \| Question: 9 | **A** |
| `7.16.8` | Random Variable: GATE DA 2026 \| Question: 44 | **B;C** |
| `7.16.9` | Random Variable: GATE DS&AI 2024 \| Question: 1 | **A** |
| `7.16.10` | Random Variable: GATE DS&AI 2024 \| Question: 55 | **0.062:0.063** |
| `7.17.1` | Square Invariant: GATE CSE 2025 \| Set 2 \| Question: 54 | **0.5:0.5** |
| `7.18.1` | Statistics: GATE CSE 2021 \| Set 2 \| Question: 22 | **15.00** |
| `7.18.2` | Statistics: GATE CSE 2024 \| Set 2 \| Question: 34 | **D** |
| `7.18.3` | Statistics: GATE DA 2026 \| Question: 52 | **10:10** |
| `7.19.1` | Uniform Distribution: GATE CSE 1998 \| Question: 3a | **0.69:0.70** |
| `7.19.2` | Uniform Distribution: GATE CSE 2004 \| Question: 78 | **A** |
| `7.19.3` | Uniform Distribution: GATE CSE 2004 \| Question: 80 | **D** |
| `7.19.4` | Uniform Distribution: GATE CSE 2007 \| Question: 24 | **B** |
| `7.19.5` | Uniform Distribution: GATE CSE 2014 \| Set 1 \| Question: 2 | **0.24** |
| `7.19.6` | Uniform Distribution: GATE CSE 2019 \| Question: 47 | **0.8** |
| `7.19.7` | Uniform Distribution: GATE CSE 2020 \| Question: 45 | **0.5** |
| `7.19.8` | Uniform Distribution: GATE CSE 2024 \| Set 1 \| Question: 4 | **B** |
| `7.19.9` | Uniform Distribution: GATE CSE 2025 \| Set 2 \| Question: 55 | **0.70:0.80** |
| `7.19.10` | Uniform Distribution: GATE DA 2026 \| Question: 53 | **0:0** |
| `7.19.11` | Uniform Distribution: GATE DS&AI 2024 \| Question: 46 | **0.125** |
| `7.20.1` | Variance: GATE DA 2025 \| Question: 26 | **B** |
| `7.20.2` | Variance: GATE DA 2026 \| Question: 34 | **A** |

