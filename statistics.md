# Statistics

# Conditional Probability

$\mathbb{P}(A|B)= \frac{\mathbb{P}(A \cap B)} {\mathbb{P}(B)}$

### Bayes’ Theorem

$\mathbb{P}(A|B)= \frac {\mathbb{P}(B|A) \cdot\mathbb{P}(A)}{\mathbb{P}(B)}$

### Law of Conditional Probability

$\mathbb{P}(A)=\mathbb{P}(A \cap I) \cdot \mathbb{P}(B \cap II )\cdot \mathbb{P}(A \cap III) = {\mathbb{P}(A | I)} \cdot {\mathbb{P}(I)}+{\mathbb{P}(B | II)} \cdot {\mathbb{P}(II)}+{\mathbb{P}(C | III)} \cdot {\mathbb{P}(III)}$

## Independence

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

## PMF (Mass)

- Discrete
- “Histogram”
- $f(X=x)=c$
- $f(X)\geq0$
- $µ=\mathbb{E}[x]=\sum_{x\in S_x}xf(x)$

## CDF of PMF

- P(X=<n) = P(1) + P(2) + ... + P(n) = 1
- Staircase
- Used to evaluate accumulated probability

## PDF (Density)

- $f(X=x)=0$
- $f(X)\geq0$
- $\int_{-\infin}^{\infin}f(x)dx=1$
- $µ=\mathbb{E}[x]=\int_{\mathbb{R}}xf(x)$

# CDF of PDF

- Gradient of each point represents the probability
- Probability = (area under the curve)

## Distribution Terminology

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

## Uniform Distribution

$X \sim U(a, b)$

- PDF

$f(x)=\frac{1}{b-a}$

$\mathbb{E}(X)=\mu= \frac{1}{2}(a+b)$

- CDF

$F(x)= \frac{x-a}{b-a}$

(area of the triangle shape)

## Poisson Distribution

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

## Exponential Distribution

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

## Normal (Gaussian) Distribution

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

## Hypergeometric Distribution

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

Then N = 52, A = 13, and n  = 5

## Geometric Distribution

- Distribution of number of trials needed to get the first success in repeated independent Bernoulli trials
- The probability of getting the first success $p$ in $x$ trials

$X \sim Geom(x,p)$

- PMF

$\mathbb{P}[X=x]=(1-p)^{x-1}p$

$\mathbb{P}[X≤x]=1-(1-p)^{x}$

$\mathbb{E}(X)=\frac{1}{p}$

$Var(X)=\frac{1-p}{p^2}$

## Binomial Distribution

- Distribution of number of successes in a fixed number of independent Bernoulli trials

$X \sim Binom(n, p)$

$S_x=\{1,2,3,...,n\}$

- PMF

$f(x)=\mathbb{P}[X=x]=\binom{n}{k}p^k(1-p)^{n-k}$

$\mathbb{E}(X)=np$

$\mathbb{E}(X^2)=np(1-p)+n^2p^2$

$Var(X)=np(1-p)$

## Negative Binomial Distribution

- Distribution of number of trials needed to get the $r$th success i.e.  r-1 successes in k-1 trials
- Generalized ver of geometric-distribution

$X\sim NG(r,p)$

$S_x=\{r, r+1, r+2, ...\}$

- PMF

$k$ trials to get $r$-th success of probability $p$

$\mathbb{P}(X=k)=\binom{k-1}{r-1}p^{r-1}(1-p)^{(k-1)-(r-1)}\cdot p  = \binom{k-1}{r-1}p^r(1-p)^{k-r}$

$\mathbb{E}(X)=\frac {r}{p}$

$Var(X)=\frac {r(1-p)}{p^2}$

*Note: $r≤x<\infin$ as at least $r$ trials are needed for $x$th success to occur.*

## Gamma Distribution

$X \sim Gamma(\alpha, \lambda)$

- PDF

$f(x, \alpha, \lambda) = \frac{\lambda ^\alpha x^{\alpha-1}e^{-\lambda x}}{\Gamma(\alpha)}$

$\alpha>1$

$\Gamma(\alpha)\vcentcolon= \int_{0}^{\infin}x^{\alpha-1}e^{-x}dx$

$\Gamma(n)=(n-1)!$

$\Gamma(\alpha+1)=\alpha\cdot\Gamma(\alpha)$

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

### Taylor expansion

$e^{\lambda}= \Sigma_{k=0}^{\infin}\frac{\lambda^k}{k!}$

# Bivariate RV

Suppose $(X,Y)$ is a bivariate RV.

- Independency

$\mathbb{P}[X \in A, Y\in B]=\mathbb{P}[X \in A] \cdot \mathbb{P}[Y \in B]$

- Covariant

 $\sigma_{XY}=cov(X,Y)=\mathbb{E}[(X-\mu_X)(X-\mu_Y)]$

$=\mathbb{E}[XY]-{E}[X]{E}[Y]$

$=\mathbb{E}[XY]-\mu_x \mu_y$

This is 0 when $X$ and $Y$ are independent since $X$, $Y$ are independent

- Correlation coefficient

$e_{XY}=\frac{\sigma_{XY}}{\sigma_X \sigma_Y}$

- Independence

$f(x,y)=f_X(x) \cdot f_Y(y)$

Then for all $u(X)$, $v(Y)$

$\mathbb{E}[u(X) \cdot v(Y)]= \mathbb{E}[u(X)] \cdot \mathbb{E}[u(Y)]$

$cov(X,Y) = 0$

$i.e.$  $f(x,y)=f(x) \cdot f(y)$ $\Rightarrow$  $cov(X,Y) =0$

( “$\Leftarrow$” is not always true)

$\mathbb{E}[X-Y]=\mathbb{E}[X]-\mathbb{E}[Y]$

$Var[X-Y]=Var[X]+Var[Y]$

## Discrete Bivariate

- Joint space of values

$S_{xy}=\{x, y: X=x, Y=y\}$

- Joint PMF

$f(x, y)=\mathbb{P}(\{X=x\} \cap \{Y=y \})$

for each $(x,y) \in S_{xy}$

$\mathbb{P}[X=x, Y=y]=f(x, y) \ge0$

$\Sigma_{(x,y)}f(x,y)=1$

For $A \in S_{xy}$

$\mathbb{P}[(x, y) \in A] = \Sigma_{A}f(x,y)$

- Independency

$f(x,y)=\mathbb{P}[X=x, Y=y]=\mathbb {P}[X=x]\mathbb{P}[Y=y]=f_X(x) \cdot f_Y(y)$

- Marginal PMF (ex. $x$)

$f_X(x)= \mathbb{P}[X=x]=\Sigma_yf(x,y)$

- Marginal mean of PMF (ex. $x$)

$\mu_x=\mathbb{E}[X]$

- Marginal Variance of PMF (ex. $x$)

${\sigma_x}^2 = Var[X]$

## Trinomial Distribution

$(X, Y) \sim trinom(n, p_1, p_2)$

where

$X \sim Binom(n, p_1)$

$Y \sim Binom(n, p_2)$

*i.e. X is success with p1 or non-success with the “rest probability”.*

- PMF

$\mathbb{P}[X=x, Y=y]$

$=\binom{n}{x, y,n-x-y}\cdot {p_1}^x \cdot {p_2}^y \cdot {(1- p_1-p_2)}^{n-x-y}$

where

$\binom{n}{x, y,n-x-y}=\frac{n!}{x! \cdot y! \cdot (n-x-y)!}$

# Continuous Bivariate

1. $f(x)\ge0, \space (x,y) \in S_{x \times y}$ and 0 for the rest
2. $\int\int_{S_{X\times Y}}f(x,y)dxdy =1$
3. $\int \int_{A} f(x,y)dxdy = \mathbb{P}[(x,y) \in A]$

- PDF

$\mathbb{P}[(x,y) \in A]=\int \int_{A} f(x,y)dxdy$

where $A \in \int_{X \times Y}$

- Marginal PDF (ex. $x$)

$f_X(x)= \int_{\R}f(x, y)dy$

Use 1 or 2 to determine C

- Independency

For all $(x,y) \in S_{X \times Y}$

$f(x,y) = f_X(x) \cdot f_Y(y)$

# Joint RV Transformation

- Partial derivatives

$\delta_xf = \frac{d}{dx}f(x,y)$

$\delta_yf = \frac{d}{dy}f(x,y)$

- Jacobian Matrix

$J(x,y):=\begin{bmatrix} 
\delta_xf & \delta_yf  \\ 
\delta_xg & \delta_yg  \\  
\end{bmatrix}$

- Determinant

$det \space J = \delta_xf \cdot \delta_yg - \delta_yf \cdot \delta_xg$

$\{x_i\}$ are ind $\Leftrightarrow$ $f(x_1, \dots, x_n) =f_{x1}(x_1) \cdots f_{xn}(x_n)$

$f$’s are either pmf or pdf

### Linear Combination and Expectations

If $x_1, \dots ,x_n$ are independent with mean $\mu_1, \dots , \mu_n$ and variances  $\sigma_1, ... \dots \sigma_n$ respectively,

Let 

$y=a_1x_1+a_2x_2+ \cdots + a_nx_n$

The expectation value of y is

$\mathbb{E}[y]=\mathbb{E}[a_1x_1]+\mathbb{E}[a_2x_2]+\cdots+\mathbb{E}[a_nx_n]$

Since $a_kx_k$ is constant

$\mathbb{E}[y]=a_1\mathbb{E}[x_1]+a_2\mathbb{E}[x_2]+\cdots+a_n\mathbb{E}[x_n]$

Since $\mathbb{E}[x_k] = \mu_k$

*Note: no independency is required*

Since $\mathbb{E}[x_i]= \mu_i$

$\mathbb{E}[y]=\Sigma a_i \cdot  \mathbb{E}[x_i]=\Sigma a_i \cdot \mu_i$

Since $Var[x_i] = \sigma^2$

$Var(y)= \Sigma a_i^2 \cdot Var[x_i]=\Sigma a_i^2 \cdot \sigma_i^2$$Var(y)= \Sigma a_i^2 Var[x_i]=\Sigma a_i^2 \cdot \sigma_i^2$

### Sample mean

Suppose $\{x_i \}$ are independent and iid with the same mean $\mu$ and var $\sigma$, for a sample mean $\bar{X}$

- $\bar{X} := \frac{1}{n} \Sigma X_i= \frac{X_1+ \cdots + X_n}{n}$

Then with $a_i = \frac{1}{n}$

- $\mathbb{E}[\bar{X}]=\Sigma \frac{1}{n}\cdot\mu_i = \mu$
- $Var[\bar{X}]=\Sigma (\frac{1}{n})^2 \cdot \sigma_i^2 = \frac{1}{n}\sigma ^2$

## Independent and Identically Distributed (iid)

- Given a sequence of RVs $x_1, x_2, \cdots$  that are mutually independent and have the same distribution.
- Mutually independent
    - $\mathbb{P}(x_1 \in A_1, \dots, x_n \in A_n) = \mathbb{P}(x_1 \in A_1) \cdots \mathbb{P}(x_n \in A_n)$
    

## Moment Generating Function (MGF)

- $M_X(t) = \mathbb{E}[e^{tX}], \space  
t \in \mathbb{R}$  such that for all $t$ is finite
- If for $X$ and $Y$, $M_X(t) = M_Y(t)$ then $X$ and $Y$  have the same distribution
- If $M_X(t)=e^t\cdot p + (1-p)$  then $X\sim Ber(p)$
- If $X_i$ are independent, $M_{X_1+ \cdots + X_n}(t)=M_{X_1}(t) \cdots M_{X_n}(t)$

### Bernoulli

$X\sim Ber(p)$

- PDF

$\mathbb{P}[X=x]$

- MGF

$M_X(t) = \mathbb{E}[e^{tX}]$ 

$= \Sigma e^{tX} \cdot \mathbb{P}[X=x]$

$=e^{t\cdot1}\mathbb{P}[X=1]+e^{t\cdot0}\mathbb{P}[X=0]$

$=e^t\cdot p + (1-p)$ 

### Exponential

$X\sim Exp(\lambda, p)$

- MGF

$M_X(t) = \mathbb{E}[e^{tX}]$ 

$= \int_{0}^{\infin} e^{tX} \cdot f(x)$

$= \int_{0}^{\infin} e^{tX} \cdot \lambda e^{-\lambda x}$

$=\frac{\lambda}{\lambda -t}$  for $\lambda-t >0$

### Normal

$X \sim N(\mu, \sigma^1)$

- PDF

$f(x)=\frac{1}{\sqrt {2\pi\sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}, \quad x \in \mathbb{R}$

- MGF

$M_X(t)= \int_\mathbb{R}e^{tX}\cdot f(x) dx$

$=\int_\mathbb{R}e^{tX}\frac{1}{\sqrt {2\pi\sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}dx$

$=e^{t \mu + \frac{1}{2}\sigma^2t^2}$

### Bimom

$X_i \sim Ber(p)$ and iid

$Y \sim Binom(n, p)$

- MGF

$M_y(t)=M_{X_1+ \cdots + X_n}(t)$

$=M_{X_1}(t) \cdots M_{X_n}(t)$

$=(e^t\cdot p + 1-p)\cdots(e^t\cdot p + 1-p)$

$=(e^t\cdot p + 1-p)^n$

### Random sample

- Any sub-collection $\{x_2, \dotsx_n \}$ is called random sample of size n