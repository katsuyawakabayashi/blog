# Statistics

# Conditional Probability

$\mathbb{P}(A|B)= \frac{\mathbb{P}(A \cap B)} {\mathbb{P}(B)}$

### Bayes’ Theorem

$\mathbb{P}(A|B)= \frac {\mathbb{P}(B|A) \cdot\mathbb{P}(A)}{\mathbb{P}(B)}$

### Law of Conditional Probability

$\mathbb{P}(A)=\mathbb{P}(A \cap I) \cdot \mathbb{P}(B \cap II )\cdot \mathbb{P}(A \cap III) = {\mathbb{P}(A | I)} \cdot {\mathbb{P}(I)}+{\mathbb{P}(B | II)} \cdot {\mathbb{P}(II)}+{\mathbb{P}(C | III)} \cdot {\mathbb{P}(III)}$

# Independence

The following are equivalent

$\mathbb{P}(A \cap B) = \mathbb{P}(A) \cdot \mathbb{P}(B)$

$\mathbb{P}(A | B) = \mathbb{P}(A)$ 

$\mathbb{P}(B|A) = \mathbb{P}(B)$ 

Q. Is A independent of B?

Show

$\mathbb{P}(A \cap B) = \mathbb{P}(A) \cdot \mathbb{P}(B)$

$\mathbb{P}(A | B) = \mathbb{P}(A)$  or $\mathbb{P}(B|A) = \mathbb{P}(B)$ 

## Mutually independent

### Pairwise independence

$A$, $B$, and $C$ are pairwise independent if

$\mathbb{P}(A \cap B) = \mathbb{P}(A) \cdot \mathbb{P}(B)$

$\mathbb{P}(B \cap C) = \mathbb{P}(B) \cdot \mathbb{P}(C)$

$\mathbb{P}(C \cap A) = \mathbb{P}(C) \cdot \mathbb{P}(A)$

### Triple-wise independence

$A$, $B$, and $C$ are triple-wise independent if

$\mathbb{P}(A \cap B \cap C) = \mathbb{P}(A) \cdot \mathbb{P}(B)\cdot \mathbb{P}(C)$

*Note:*

Pairwise independent $\nLeftrightarrow$ Triple-wise independent

### Independent events vs disjoint events

“Event A is independent of B”: Event A is not contingent of B’s occurrence.

$\mathbb{P}(A \cap B) = \mathbb{P}(A) \cdot \mathbb{P}(B)$

### Disjoint

- “Event A is disjoint of B”: Event A and B do not occur simultaneously.”
- If $A$ and $B$ are disjoint, they are not independent of each other
- Since if $A$ has already happened, then there’s zero chance of $B$

$\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B)$

$\mathbb{P}(A|B)=0$

$\mathbb{P}(B|A)=0$

# Probability Distribution Functions (PDFs)

# PMF (Mass)

- Discrete
- “Histogram”
- $f(X=x)=c$
- $f(X)\geq0$
- $µ=\mathbb{E}[x]=\sum_{x\in S_x}xf(x)$

# CDF of PMF

- P(X=<n) = P(1) + P(2) + ... + P(n) = 1
- Staircase
- Used to evaluate accumulated probability

# PDF (Density)

- $f(X=x)=0$
- $f(X)\geq0$
- $\int_{-\infin}^{\infin}f(x)dx=1$
- $µ=\mathbb{E}[x]=\int_{\mathbb{R}}xf(x)$

# CDF of PDF

- Gradient of each point represents the probability
- Probability = (area under the curve)

# Distribution Terminology

- Mean (PMF)

$\mathbb{E}[x]=µ$

$\sum_{x\in S_x}xf(x)$

$\int_{A \in S_x}x  f(x)dx$

- Variance

$\sigma^2=\mathbb{E}[(x-µ)^2]=\mathbb{E}(X^2)-\mathbb{E}(X)^2$

$\sum_{x\in S_x}(x-\mu)^2f(x)$

$\int_{-\infin}^{\infin}(x-\mu)^2f(x)dx$

- nth moment

$\mathbb{E[x^n]}$

- Standard deviation

$\sigma=\sqrt\sigma^2$

- Expected values arithmetics

$\mathbb{E[c]}=c$

$\mathbb{E[c \cdot u(x)]}=c\cdot \mathbb{E[x]}$

$\mathbb{E}[c_1\cdot u_1(x)+c_2 \cdot u_2(x)]=c_1\mathbb{E[u_1(x)]}+c_2 \mathbb{E}[u_2(x)]$

$\mathbb{E}[u_1(x) \cdot u_2(x)] \neq \mathbb{E}[u_1(x)]\cdot\mathbb{E}[{u_2(x)}]$

# Uniform Distribution

$X \sim U(a, b)$

- PDF

$f(x)=\frac{1}{b-a}$

$\mathbb{E}(X)=\mu= \frac{1}{2}(a+b)$

- CDF

$F(x)= \frac{x-a}{b-a}$

(area of the triangle shape)

# Poisson Distribution

- Each event is random and independent
- Events per single unit of time (ex. Number of guests per hour)

$X \sim Pois(\lambda)$

$S_x= \mathbb{N}=\{1,2,3, ...\}$

- PMF

$f(x)=\frac{\lambda^xe^{-\lambda}}{x!}$

$\mathbb{E}[X] = \lambda$

$Var[x] = \lambda$

- CDF

$F(x)=\Sigma_{i=0}^{x}\frac{\lambda^xe^{-\lambda}}{x!}$

# Exponential Distribution

- Time per single event (ex. Number of hours between guest arrivals)

$X \sim Exp(\lambda)$

- PDF

$f(x) = λe^{-λx}$

$\mathbb{E}(X)= \frac{1}{\lambda}$

$Var(x)=\frac{1}{\lambda^2}$

- CDF

$P(X≤ x) = 1-e^{-λx}$

$P(a≤X≤b) = 1-e^{-λb}-1-e^{-λa}$

*Note*

- Memoryless (wait for s min after waiting for t min already = wait for s min)

$\mathbb{P}(X>t+s|X>t) = \mathbb{P}(X>s)$

# Normal (Gaussian) Distribution

- “Bell curve” distribution (ex.  people’s height)
- Centered on the average value

$X\sim N(\mu, \sigma^2)$

$x \in \mathbb{R}$

$S_x=\mathbb{R}$

- PDF

$f(x)=\frac{1}{\sqrt {2\pi\sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$

$\mathbb{E}(X)=\mu$

$Var(X)=\sigma^2$

- If $X\sim N(0,1)$ (standard normal distribution)

$y=\frac{x-\mu}{\sigma}$  

$f(x)= \Phi(x)=\frac{1}{\sqrt {2\pi}}e^{-\frac{x^2}{2}}$

- If $X\sim N(\mu, \sigma^2)$

$Z=\frac{X-\mu}{\sigma}\sim N(0,1)$

*Note*

$\int_{\mathbb{R}}e^{-\lambda^2}=\pi$

# Hypergeometric Distribution

$X \sim Hypergeometric(N, A, n)$ 

- PMF

$\mathbb{P}(X=x)=\frac{\binom{A}{x} \binom{N-A}{n-x}}{\binom {N}{n}}$

$\mathbb{E}(X)=\mu=n \frac{K}{N}$

$\sum_{x \in S_x} \mathbb{P}(X=x)=1$

$N$ := Total population size

$n$ := Sample size

$A$ := Total items of interest in the population

$x$ := Number of success in the sample

$N-A$ := Total items of non-interest in the population

$n-x$ := Number of failures in the sample

Example: “Probability of getting x spade cards in a 5-card poker hand”

N = 52

A = 13

n  = 5

# Geometric Distribution

- Distribution of number of trials needed to get the first success in repeated independent Bernoulli trials
- The probability of getting the first success $p$ in $x$ trials

$X \sim Geom(x,p)$

- PMF

$\mathbb{P}[X=x]=(1-p)^{x-1}p$

$\mathbb{P}[X≤x]=1-(1-p)^{x}$

$\mathbb{E}(X)=\frac{1}{p}$

$Var(X)=\frac{1-p}{p^2}$

# Binomial Distribution

- Distribution of number of successes in a fixed number of independent Bernoulli trials

$X \sim Binom(n, p)$

$S_x=\{1,2,3,...,n\}$

- PMF

$f(x)=\mathbb{P}[X=x]=\binom{n}{k}p^k(1-p)^{n-k}$

$\mathbb{E}(X)=np$

$\mathbb{E}(X^2)=np(1-p)+n^2p^2$

$Var(X)=np(1-p)$

# Negative Binomial Distribution

- Distribution of number of trials needed to get the $r$th success i.e.  r-1 successes in k-1 trials
- Generalized ver of geometric-distribution

$X\sim NG(r,p)$

$S_x=\{r, r+1, r+2, ...\}$

- PMF

$k$ trials to get $r$th success of probability $p$

$\mathbb{P}(X=k)=\binom{k-1}{r-1}p^{r-1}(1-p)^{(k-1)-(r-1)}\cdot p  = \binom{k-1}{r-1}p^r(1-p)^{k-r}$

$\mathbb{E}(X)=\frac {r}{p}$

$Var(X)=\frac {r(1-p)}{p^2}$

*Note*

 $r≤x<\infin$ as at least $r$ trials are needed for $x$th success to occur.

# Solve distribution

## Monotonic

- $y=u(x)$ is strictly increasing or decreasing in a domain $A \subset \mathbb{R}$

$f_y(y)=f_x(v(y)) \cdot |v'(y)|$

$x=v(y)$ is the inverse function of $y=u(x)$

Step 0: Check monotonic-ness

Step 1: Verify by taking a derivative

Step 2: Find inverse

Step 3: Apply theorem 

## Non-monotonic

- Z~?

Step 0: Determine $S_z$ from $Z \in[?,?]$ based on  $X \in ?$

Step 1: Get CDF $F_z(t)=\mathbb{P}(Z\le t)$ and express $Z$ with $X$

Step 2: $F_z(t)=\int_{a}^{b} f(x)dx$? Where $a \le X \le b$ and both include $t$. $f(x)$ is from $X\sim$

*No need to solve the integral, just differentiate in step3*

Step 3: Differentiate $F$ to get $f$

# Gamma Function

$\alpha>1$

$\Gamma(\alpha)\vcentcolon= \int_{0}^{\infin}x^{\alpha-1}e^{-x}dx$

$\Gamma(n)=(n-1)!$

$\Gamma(\alpha+1)=\alpha\cdot\Gamma(\alpha)$

### Taylor expansion

$e^{\lambda}= \Sigma_{k=0}^{\infin}\frac{\lambda^k}{k!}$